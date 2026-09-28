#!/usr/bin/env python3
"""Import per-case sample images from source style packages into assets/samples/.

A source package (the folder publish-style is given) holds one 16x9 and one 9x16
image per example case, e.g. 01-voice-carries-16x9.png. This script matches
each case_name in the published styles/<slug>/style.json to those files and
writes web-sized WebP copies to assets/samples/<slug>/<NN>-16x9.webp and
<NN>-9x16.webp, where NN is the case's 1-based position in `examples`.
Files are matched by slugified case name first, then by the NN- prefix.
build-pages-mvp.py picks them up automatically.

Usage:
  python3 scripts/import-samples.py <package-dir> <slug>     # one style
  python3 scripts/import-samples.py --scan <source-root>      # every published style found under root
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
STYLES_DIR = ROOT / "styles"
SAMPLES_DIR = ROOT / "assets" / "samples"
SIZES = {"16x9": (800, 450), "9x16": (450, 800)}
QUALITY = 76
IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".webp")


def case_names(slug: str) -> list[str]:
    data = json.loads((STYLES_DIR / slug / "style.json").read_text(encoding="utf-8"))
    names = []
    for item in data.get("examples") or []:
        name = item.get("case_name") if isinstance(item, dict) else None
        if isinstance(name, str) and name.strip():
            names.append(name.strip())
    return names


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def find_image(package: Path, case: str, position: int, ratio: str) -> Path | None:
    images = [p for p in sorted(package.iterdir()) if p.suffix.lower() in IMAGE_EXTS and p.stem.lower().endswith(ratio)]
    case_slug = slugify(case)
    if case_slug:
        by_name = re.compile(rf"(^|[-_]){re.escape(case_slug)}[-_]{ratio}$")
        for path in images:
            if by_name.search(path.stem.lower()):
                return path
    by_position = [p for p in images if p.stem.startswith(f"{position:02d}-")]
    return by_position[0] if len(by_position) == 1 else None


def import_package(package: Path, slug: str) -> int:
    cases = case_names(slug)
    written = 0
    out_dir = SAMPLES_DIR / slug
    for position, case in enumerate(cases, start=1):
        sources = {ratio: find_image(package, case, position, ratio) for ratio in SIZES}
        if not all(sources.values()):
            continue
        out_dir.mkdir(parents=True, exist_ok=True)
        for ratio, src in sources.items():
            with Image.open(src) as im:
                im = im.convert("RGB")
                im.thumbnail(SIZES[ratio], Image.LANCZOS)
                im.save(out_dir / f"{position:02d}-{ratio}.webp", "WEBP", quality=QUALITY, method=6)
            written += 1
    return written


def package_index(source_root: Path) -> dict[str, Path]:
    """Map style slug -> package folder, by style_slug in style-spec.json or by folder name."""
    index: dict[str, Path] = {}
    for spec in source_root.rglob("style-spec.json"):
        try:
            slug = json.loads(spec.read_text(encoding="utf-8")).get("style_slug")
        except (OSError, json.JSONDecodeError):
            slug = None
        for key in filter(None, (slug, spec.parent.name)):
            index.setdefault(key, spec.parent)
    return index


def main(argv: list[str]) -> int:
    if len(argv) == 3 and argv[1] == "--scan":
        index = package_index(Path(argv[2]).expanduser())
        styles = sorted(p.name for p in STYLES_DIR.iterdir() if (p / "style.json").exists())
        covered = 0
        for slug in styles:
            if slug in index and import_package(index[slug], slug):
                covered += 1
        print(f"PASS: imported samples for {covered} of {len(styles)} styles")
        return 0
    if len(argv) == 3:
        count = import_package(Path(argv[1]).expanduser(), argv[2])
        print(f"PASS: wrote {count} sample images for {argv[2]}" if count else f"WARN: no case images matched for {argv[2]}")
        return 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
