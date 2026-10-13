#!/usr/bin/env python3
"""Keep image files small so the repository (and every clone) stops growing fast.

Two modes:

  python3 scripts/optimize-images.py <slug> [<slug> ...]
      Re-encode styles/<slug>/preview-16x9.jpg and preview-9x16.jpg when one is
      over PREVIEW_MAX_KB or PREVIEW_MAX_PIXELS: downscale to PREVIEW_MAX_PIXELS
      (the usual 1672x941), save as a progressive JPEG without metadata, and lower
      the quality until it is at most PREVIEW_TARGET_KB. Files already within
      the limits are left untouched, so running it twice changes nothing.
      Needs Pillow. publish-style.py runs this for every style it adds.

  python3 scripts/optimize-images.py --check
      Fail if any preview, gallery thumbnail or sample image is over its limit.
      Needs only the standard library (CI runs it). Previews committed before
      this check existed are listed in LEGACY_PREVIEW_KB and may not grow.
"""

from __future__ import annotations

import argparse
import io
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STYLES_DIR = ROOT / "styles"
THUMBS_DIR = ROOT / "assets" / "thumbs"
SAMPLES_DIR = ROOT / "assets" / "samples"

PREVIEWS = ("preview-16x9.jpg", "preview-9x16.jpg")
PREVIEW_MAX_KB = 800
PREVIEW_TARGET_KB = 600
PREVIEW_MAX_PIXELS = 1672 * 941
PREVIEW_HARD_MAX_SIDE = 2560
START_QUALITY = 85
MIN_QUALITY = 70
THUMB_MAX_KB = 200
THUMB_MAX_WIDTH = 640
SAMPLE_MAX_KB = 200

# Previews that were already over PREVIEW_MAX_KB when the check was added
# (2026-10-13), with their size then in KB. They may shrink but not grow.
LEGACY_PREVIEW_KB = {
    "blue-halftone-ransom-zine-poster-style/preview-16x9.jpg": 823,
    "blue-halftone-ransom-zine-poster-style/preview-9x16.jpg": 801,
    "cream-smoke-city-manga-poster-style/preview-16x9.jpg": 811,
    "crimson-ink-manga-dossier/preview-16x9.jpg": 805,
    "crimson-vanishing-point-editorial/preview-16x9.jpg": 987,
    "crimson-vanishing-point-editorial/preview-9x16.jpg": 993,
    "fantasy-scribble-mascot-poster-style/preview-16x9.jpg": 895,
    "fantasy-scribble-mascot-poster-style/preview-9x16.jpg": 823,
    "impact-burst-halftone-comic-poster-style/preview-16x9.jpg": 984,
    "impact-burst-halftone-comic-poster-style/preview-9x16.jpg": 953,
    "motorsport-technical-editorial/preview-16x9.jpg": 1059,
    "motorsport-technical-editorial/preview-9x16.jpg": 1118,
    "multi-color-beverage-splash-ad-system-style/preview-16x9.jpg": 809,
    "multi-color-beverage-splash-ad-system-style/preview-9x16.jpg": 865,
    "red-black-manga-tabloid-poster-style/preview-16x9.jpg": 803,
    "red-monochrome-editorial-grid/preview-16x9.jpg": 1486,
    "red-monochrome-editorial-grid/preview-9x16.jpg": 1336,
    "retro-pop-sticker-cutout/preview-16x9.jpg": 1620,
    "retro-pop-sticker-cutout/preview-9x16.jpg": 1649,
    "rough-ink-music-doodle-poster-style/preview-16x9.jpg": 918,
    "rough-ink-music-doodle-poster-style/preview-9x16.jpg": 867,
    "split-ink-monumental-editorial/preview-16x9.jpg": 1486,
    "split-ink-monumental-editorial/preview-9x16.jpg": 1300,
    "split-scorched-editorial-poster/preview-16x9.jpg": 1331,
    "split-scorched-editorial-poster/preview-9x16.jpg": 1131,
    "teenage-skate-scribble-screenprint-poster-style/preview-16x9.jpg": 816,
    "turquoise-red-techno-manga-poster-style/preview-16x9.jpg": 843,
    "turquoise-red-techno-manga-poster-style/preview-9x16.jpg": 904,
    "y2k-mirror-ui-scribble-collage-style/preview-16x9.jpg": 857,
    "y2k-mirror-ui-scribble-collage-style/preview-9x16.jpg": 894,
    "yellow-black-manga-food-zine-ad-style/preview-16x9.jpg": 1137,
    "yellow-black-manga-food-zine-ad-style/preview-9x16.jpg": 1117,
}


def kb(path: Path) -> int:
    return path.stat().st_size // 1024


def jpeg_size(path: Path) -> tuple[int, int]:
    """Read (width, height) from a JPEG's SOF marker without Pillow."""
    with path.open("rb") as file:
        if file.read(2) != b"\xff\xd8":
            raise ValueError(f"{path} is not a JPEG")
        while True:
            byte = file.read(1)
            while byte and byte != b"\xff":
                byte = file.read(1)
            while byte == b"\xff":
                byte = file.read(1)
            if not byte:
                raise ValueError(f"{path}: no SOF marker found")
            marker = byte[0]
            if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
                continue
            length = struct.unpack(">H", file.read(2))[0]
            if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
                height, width = struct.unpack(">xHH", file.read(5))
                return width, height
            file.seek(length - 2, 1)


def check() -> int:
    errors = []
    for style_dir in sorted(p for p in STYLES_DIR.iterdir() if p.is_dir()):
        for name in PREVIEWS:
            path = style_dir / name
            if not path.exists():
                continue
            key = f"{style_dir.name}/{name}"
            size = kb(path)
            limit = max(PREVIEW_MAX_KB, LEGACY_PREVIEW_KB.get(key, 0))
            if size > limit:
                errors.append(f"styles/{key} is {size} KB (limit {limit} KB)")
            if max(jpeg_size(path)) > PREVIEW_HARD_MAX_SIDE:
                errors.append(f"styles/{key} is larger than {PREVIEW_HARD_MAX_SIDE}px on its long side")
    for path in sorted(THUMBS_DIR.glob("*-16x9.jpg")):
        if kb(path) > THUMB_MAX_KB:
            errors.append(f"{path.relative_to(ROOT)} is {kb(path)} KB (limit {THUMB_MAX_KB} KB)")
        if jpeg_size(path)[0] > THUMB_MAX_WIDTH:
            errors.append(f"{path.relative_to(ROOT)} is wider than {THUMB_MAX_WIDTH}px")
    for path in sorted(SAMPLES_DIR.glob("*/*.webp")):
        if kb(path) > SAMPLE_MAX_KB:
            errors.append(f"{path.relative_to(ROOT)} is {kb(path)} KB (limit {SAMPLE_MAX_KB} KB)")

    if errors:
        for message in errors:
            print(f"FAIL: {message}", file=sys.stderr)
        print("Run: python3 scripts/optimize-images.py <slug>  (previews) or regenerate thumbs/samples.", file=sys.stderr)
        return 1
    print("PASS: previews, thumbnails and samples are within size limits")
    return 0


def encode(image, quality: int) -> bytes:
    buffer = io.BytesIO()
    image.save(buffer, "JPEG", quality=quality, optimize=True, progressive=True)
    return buffer.getvalue()


def optimize(slug: str) -> None:
    from PIL import Image

    for name in PREVIEWS:
        path = STYLES_DIR / slug / name
        if not path.exists():
            raise SystemExit(f"ERROR: {path.relative_to(ROOT)} does not exist")
        before = kb(path)
        with Image.open(path) as source:
            image = source.convert("RGB")
        if before <= PREVIEW_MAX_KB and image.width * image.height <= PREVIEW_MAX_PIXELS:
            print(f"ok:   styles/{slug}/{name} {before} KB {image.width}x{image.height}")
            continue
        if image.width * image.height > PREVIEW_MAX_PIXELS:
            scale = (PREVIEW_MAX_PIXELS / (image.width * image.height)) ** 0.5
            image = image.resize((int(image.width * scale), int(image.height * scale)), Image.LANCZOS)
        quality = START_QUALITY
        data = encode(image, quality)
        while len(data) > PREVIEW_TARGET_KB * 1024 and quality > MIN_QUALITY:
            quality -= 5
            data = encode(image, quality)
        while len(data) > PREVIEW_MAX_KB * 1024:
            image = image.resize((int(image.width * 0.9), int(image.height * 0.9)), Image.LANCZOS)
            data = encode(image, quality)
        path.write_bytes(data)
        print(f"done: styles/{slug}/{name} {before} KB -> {kb(path)} KB, {image.width}x{image.height}, q{quality}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("slugs", nargs="*", help="styles whose previews to optimize")
    parser.add_argument("--check", action="store_true", help="only check every image against the size limits")
    args = parser.parse_args()
    if args.check:
        return check()
    if not args.slugs:
        parser.error("pass one or more style slugs, or --check")
    for slug in args.slugs:
        optimize(slug)
    return 0


if __name__ == "__main__":
    sys.exit(main())
