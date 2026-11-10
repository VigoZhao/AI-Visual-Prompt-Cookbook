#!/usr/bin/env python3
"""Generate README gallery thumbnails (assets/thumbs/<slug>-16x9.jpg).

Resamples each style's preview-16x9.jpg down to 640px wide at JPEG quality 72.
Uses macOS `sips` when it is available and falls back to Pillow elsewhere
(Linux, Windows, CI), so contributors are not limited to a Mac. Skips thumbnails that are already newer than their source. Run after adding or
updating any style preview, before updating the README galleries.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STYLES_DIR = ROOT / "styles"
THUMBS_DIR = ROOT / "assets" / "thumbs"

THUMB_WIDTH = 640
JPEG_QUALITY = 72


def resize_with_sips(source: Path, thumb: Path) -> str | None:
    result = subprocess.run(
        [
            "sips",
            "--resampleWidth", str(THUMB_WIDTH),
            "-s", "format", "jpeg",
            "-s", "formatOptions", str(JPEG_QUALITY),
            str(source),
            "--out", str(thumb),
        ],
        capture_output=True,
    )
    if result.returncode != 0:
        return result.stderr.decode().strip() or f"sips exited with status {result.returncode}"
    return None


def resize_with_pillow(source: Path, thumb: Path) -> str | None:
    try:
        from PIL import Image
    except ImportError:
        return "neither macOS sips nor Pillow is available (pip install pillow)"
    try:
        with Image.open(source) as im:
            im = im.convert("RGB")
            height = round(im.height * THUMB_WIDTH / im.width)
            im = im.resize((THUMB_WIDTH, height), Image.LANCZOS)
            im.save(thumb, "JPEG", quality=JPEG_QUALITY, optimize=True)
    except OSError as error:
        return str(error)
    return None


def main() -> int:
    THUMBS_DIR.mkdir(parents=True, exist_ok=True)
    resize = resize_with_sips if shutil.which("sips") else resize_with_pillow
    generated = skipped = failed = 0

    for style_dir in sorted(STYLES_DIR.iterdir()):
        if not style_dir.is_dir():
            continue
        source = style_dir / "preview-16x9.jpg"
        if not source.exists():
            print(f"WARN: missing source preview: {source}", file=sys.stderr)
            failed += 1
            continue
        thumb = THUMBS_DIR / f"{style_dir.name}-16x9.jpg"
        if thumb.exists() and thumb.stat().st_mtime >= source.stat().st_mtime:
            skipped += 1
            continue
        error = resize(source, thumb)
        if error:
            print(f"FAIL: {style_dir.name}: {error}", file=sys.stderr)
            failed += 1
        else:
            generated += 1

    print(f"thumbnails: {generated} generated, {skipped} up to date, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
