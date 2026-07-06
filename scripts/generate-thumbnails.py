#!/usr/bin/env python3
"""Generate README gallery thumbnails (assets/thumbs/<slug>-16x9.jpg).

Uses macOS `sips` to resample each style's preview-16x9.jpg down to 640px wide.
Skips thumbnails that are already newer than their source. Run after adding or
updating any style preview, before updating the README galleries.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STYLES_DIR = ROOT / "styles"
THUMBS_DIR = ROOT / "assets" / "thumbs"

THUMB_WIDTH = "640"
JPEG_QUALITY = "72"


def main() -> int:
    THUMBS_DIR.mkdir(parents=True, exist_ok=True)
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
        result = subprocess.run(
            [
                "sips",
                "--resampleWidth", THUMB_WIDTH,
                "-s", "format", "jpeg",
                "-s", "formatOptions", JPEG_QUALITY,
                str(source),
                "--out", str(thumb),
            ],
            capture_output=True,
        )
        if result.returncode != 0:
            print(f"FAIL: {style_dir.name}: {result.stderr.decode().strip()}", file=sys.stderr)
            failed += 1
        else:
            generated += 1

    print(f"thumbnails: {generated} generated, {skipped} up to date, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
