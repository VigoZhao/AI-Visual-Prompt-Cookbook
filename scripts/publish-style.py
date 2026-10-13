#!/usr/bin/env python3
"""Register new styles in data/catalog.json and regenerate everything derived from it.

This is the one command a publish run needs after the style folders, preview
JPGs and thumbnails are in place. It:
  1. checks each styles/<slug>/ has exactly style.json + the two preview JPGs,
     and that assets/thumbs/<slug>-16x9.jpg exists;
  2. adds each style to the top of "styles" in data/catalog.json (in the order
     given, so pass a series' part 1 first), or updates its summary if it is
     already listed;
  3. optionally moves styles to the front of "featured" (keeping six);
  4. runs validate-style-json.py, generate-readme.py, build-pages-mvp.py and
     generate-copy-prompts.py.
If any step fails, data/catalog.json is restored and the script exits non-zero.
It never commits or pushes; review `git status` and commit as usual.

Usage:
  python3 scripts/publish-style.py --add everyday-riso="Three-ink risograph posters of ..."
  python3 scripts/publish-style.py \\
      --add velocity-type-sport="Extreme near-to-far sports photography ..." \\
      --add velocity-type-sport-part-02="Part 2: ..." \\
      --feature velocity-type-sport
  python3 scripts/publish-style.py --check     # only regenerate and validate
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STYLES_DIR = ROOT / "styles"
THUMBS_DIR = ROOT / "assets" / "thumbs"
CATALOG_DATA = ROOT / "data" / "catalog.json"
STYLE_FILES = ["preview-16x9.jpg", "preview-9x16.jpg", "style.json"]
FEATURED_COUNT = 6
STEPS = [
    ["scripts/validate-style-json.py", "."],
    ["scripts/generate-readme.py"],
    ["scripts/build-pages-mvp.py"],
    ["scripts/generate-copy-prompts.py"],
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def parse_add(value: str) -> tuple[str, str]:
    slug, sep, summary = value.partition("=")
    slug, summary = slug.strip(), " ".join(summary.split())
    if not sep or not slug or not summary:
        raise argparse.ArgumentTypeError(f'expected SLUG="one-line summary", got {value!r}')
    return slug, summary


def check_style_folder(slug: str) -> None:
    folder = STYLES_DIR / slug
    if not folder.is_dir():
        fail(f"styles/{slug}/ does not exist")
    files = sorted(p.name for p in folder.iterdir() if p.name != ".DS_Store")
    if files != STYLE_FILES:
        fail(f"styles/{slug}/ must contain exactly {STYLE_FILES}, found {files}")
    if not (THUMBS_DIR / f"{slug}-16x9.jpg").exists():
        fail(f"missing assets/thumbs/{slug}-16x9.jpg (run scripts/generate-thumbnails.py)")


def update_catalog(data: dict, additions: list[tuple[str, str]], featured: list[str]) -> list[str]:
    changes = []
    styles = data["styles"]
    listed = {entry["slug"]: entry for entry in styles}
    new_entries = []
    for slug, summary in additions:
        if slug in listed:
            if listed[slug]["summary"] != summary:
                listed[slug]["summary"] = summary
                changes.append(f"updated summary: {slug}")
            continue
        new_entries.append({"slug": slug, "summary": summary})
        changes.append(f"added to top of gallery: {slug}")
    data["styles"] = new_entries + styles

    current = [entry["slug"] for entry in data["featured"]]
    for slug in reversed(featured):
        if slug in current:
            continue
        data["featured"].insert(0, {"slug": slug})
        current.insert(0, slug)
        changes.append(f"featured: {slug}")
    for entry in data["featured"][FEATURED_COUNT:]:
        changes.append(f"no longer featured: {entry['slug']}")
    data["featured"] = data["featured"][:FEATURED_COUNT]
    return changes


def run_steps() -> None:
    for step in STEPS:
        print(f"--> python3 {' '.join(step)}")
        result = subprocess.run([sys.executable, *step], cwd=ROOT)
        if result.returncode != 0:
            raise RuntimeError(f"{step[0]} failed")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--add", action="append", type=parse_add, default=[], metavar='SLUG="summary"',
                        help="style to add (or re-summarize); repeat for several, first ends up on top")
    parser.add_argument("--feature", action="append", default=[], metavar="SLUG",
                        help="move this style to the front of Featured; repeat for several")
    parser.add_argument("--check", action="store_true", help="only regenerate and validate")
    args = parser.parse_args()
    if not args.add and not args.feature and not args.check:
        parser.error("nothing to do: pass --add, --feature or --check")

    added = [slug for slug, _ in args.add]
    if len(set(added)) != len(added):
        fail(f"--add lists a style twice: {added}")
    for slug in added + args.feature:
        check_style_folder(slug)

    original = CATALOG_DATA.read_text(encoding="utf-8")
    data = json.loads(original)
    changes = update_catalog(data, args.add, args.feature)
    CATALOG_DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for change in changes:
        print(f"catalog: {change}")

    try:
        run_steps()
    except RuntimeError as error:
        CATALOG_DATA.write_text(original, encoding="utf-8")
        fail(f"{error}; data/catalog.json restored. Generated files may be partly rewritten: "
             "fix the problem and run again, or `git checkout -- .` to discard.")
    print("PASS: catalog, READMEs, docs and site regenerated. Review `git status`, then commit.")


if __name__ == "__main__":
    main()
