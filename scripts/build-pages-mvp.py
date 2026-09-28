#!/usr/bin/env python3
"""Build the local static MVP for the style browser."""

from __future__ import annotations

import hashlib
import html
import json
import re
from pathlib import Path
from typing import Any

import seo_pages
from search_terms import FAMILY_OVERRIDES, QUICK_TAGS, ZH_TERMS


ROOT = Path(__file__).resolve().parents[1]
STYLES_DIR = ROOT / "styles"
README = ROOT / "README.md"
SITE_DIR = ROOT / "site"
OUTPUT = SITE_DIR / "styles-data.js"
SAMPLES_DIR = ROOT / "assets" / "samples"

SWITCHABLE_ASPECT_RATIOS = ("16:9", "9:16", "4:5", "5:4")
RATIO_RE = re.compile(r"\b(\d+:\d+)\b")
VARIANT_RE = re.compile(r"^(?P<base>.+)-(?:set|part)-\d+$")

GALLERY_CATEGORIES = (
    "Photo + Doodle",
    "Zine + Collage",
    "Type Posters",
    "Travel + City",
    "Editorial + Minimal",
    "Product + Campaign",
)


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def read_readme_order() -> tuple[list[str], dict[str, str]]:
    text = README.read_text(encoding="utf-8")
    match = re.search(r"^## All Styles\n(?P<body>.*?)(?=^## )", text, re.MULTILINE | re.DOTALL)
    if not match:
        return [], {}

    body = match.group("body")
    pairs = re.findall(
        r'<a id="([^"]+)"></a>.*?<em>(.*?)</em>',
        body,
        flags=re.DOTALL,
    )
    order: list[str] = []
    descriptions: dict[str, str] = {}
    for slug, description in pairs:
        order.append(slug)
        descriptions[slug] = html.unescape(re.sub(r"\s+", " ", description).strip())
    return order, descriptions


def first_text_list(items: Any, limit: int) -> list[str]:
    if not isinstance(items, list):
        return []
    result: list[str] = []
    for item in items:
        if isinstance(item, str) and item.strip():
            result.append(item.strip())
        if len(result) == limit:
            break
    return result


def aspect_ratios_for(data: dict[str, Any]) -> list[str]:
    env = data.get("environment_variables")
    text = ""
    if isinstance(env, dict) and isinstance(env.get("ASPECT_RATIO"), str):
        text = env["ASPECT_RATIO"]
    found: list[str] = []
    for ratio in RATIO_RE.findall(text):
        if ratio in SWITCHABLE_ASPECT_RATIOS and ratio not in found:
            found.append(ratio)
    return found or ["16:9", "9:16"]


def category_for(slug: str, data: dict[str, Any]) -> str:
    category = data.get("category")
    if category not in GALLERY_CATEGORIES:
        raise ValueError(
            f"{slug}: style.json category must be one of {list(GALLERY_CATEGORIES)}, got {category!r}"
        )
    return category


def tags_for(slug: str, name: str, summary: str) -> list[str]:
    haystack = f"{name} {summary} {slug.replace('-', ' ')}".lower()
    return [
        label
        for label, terms in QUICK_TAGS
        if any(re.search(r"\b" + re.escape(term), haystack) for term in terms)
    ]


def samples_for(slug: str, case_count: int) -> list[dict[str, Any]]:
    """Per-case images imported by scripts/import-samples.py, keyed by example index."""
    samples = []
    for index in range(case_count):
        stem = f"{index + 1:02d}"
        img16 = SAMPLES_DIR / slug / f"{stem}-16x9.webp"
        img9 = SAMPLES_DIR / slug / f"{stem}-9x16.webp"
        if img16.exists() and img9.exists():
            samples.append(
                {
                    "index": index,
                    "img16": f"../assets/samples/{slug}/{stem}-16x9.webp",
                    "img9": f"../assets/samples/{slug}/{stem}-9x16.webp",
                }
            )
    return samples


def family_key(slug: str, slugs: set[str]) -> str:
    if slug in FAMILY_OVERRIDES:
        return FAMILY_OVERRIDES[slug]
    match = VARIANT_RE.match(slug)
    return match.group("base") if match else slug


def assign_families(styles: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Group variant sets; returns {key: {name, members}} for families with 2+ members."""
    slugs = {s["slug"] for s in styles}
    groups: dict[str, list[dict[str, Any]]] = {}
    for style in styles:
        groups.setdefault(family_key(style["slug"], slugs), []).append(style)
    families = {}
    for key, members in groups.items():
        if len(members) < 2:
            continue
        # Name the family after its base style if published, else its oldest member.
        base = next((m for m in members if m["slug"] == key), members[-1])
        families[key] = {"name": base["name"], "members": [m["slug"] for m in members]}
        for member in members:
            member["family"] = key
    return families


def assign_similar(styles: list[dict[str, Any]], limit: int = 6) -> None:
    """Rank other styles by shared quick tags (+ same category); skip own family."""
    for style in styles:
        own_family = style.get("family")
        scored = []
        for position, other in enumerate(styles):
            if other["slug"] == style["slug"] or (own_family and other.get("family") == own_family):
                continue
            score = 2 * len(set(style["tags"]) & set(other["tags"])) + (other["category"] == style["category"])
            if score:
                scored.append((-score, position, other["slug"]))
        # One pick per family so a multi-set family does not fill the row.
        picked, families_used = [], set()
        by_slug = {s["slug"]: s for s in styles}
        for _, _, slug in sorted(scored):
            fam = by_slug[slug].get("family")
            if fam and fam in families_used:
                continue
            families_used.add(fam)
            picked.append(slug)
            if len(picked) == limit:
                break
        style["similar"] = picked


def build() -> None:
    readme_order, readme_descriptions = read_readme_order()
    style_paths = {path.parent.name: path for path in STYLES_DIR.glob("*/style.json")}
    ordered_slugs = [slug for slug in readme_order if slug in style_paths]
    ordered_slugs.extend(sorted(slug for slug in style_paths if slug not in ordered_slugs))

    styles: list[dict[str, Any]] = []
    for slug in ordered_slugs:
        json_text = style_paths[slug].read_text(encoding="utf-8")
        data = load_json(style_paths[slug])
        name = str(data.get("style_name", slug)).strip()
        summary = str(data.get("style_summary", "")).strip()
        env = data.get("environment_variables")
        variables = list(env.keys()) if isinstance(env, dict) else []

        styles.append(
            {
                "name": name,
                "slug": slug,
                "category": category_for(slug, data),
                "description": readme_descriptions.get(slug) or summary,
                "summary": summary,
                "preview16": f"../styles/{slug}/preview-16x9.jpg",
                "preview9": f"../styles/{slug}/preview-9x16.jpg",
                "thumb16": f"../assets/thumbs/{slug}-16x9.jpg",
                "samples": samples_for(slug, len(data.get("examples") or [])),
                "tags": tags_for(slug, name, summary),
                "styleJson": f"../styles/{slug}/style.json",
                "copyPromptDoc": f"../docs/copy-prompts/{slug}.md",
                "folder": f"../styles/{slug}/",
                "anchors": first_text_list(data.get("style_fidelity_anchors"), 6),
                "variables": variables,
                "aspectRatios": aspect_ratios_for(data),
                "jsonText": json_text,
            }
        )

    families = assign_families(styles)
    assign_similar(styles)
    used_categories = {style["category"] for style in styles}
    payload = {
        "styleCount": len(styles),
        "categories": [category for category in GALLERY_CATEGORIES if category in used_categories],
        "quickTags": [label for label, _ in QUICK_TAGS if any(label in s["tags"] for s in styles)],
        "zhTerms": ZH_TERMS,
        "families": families,
        "styles": styles,
    }
    SITE_DIR.mkdir(exist_ok=True)
    OUTPUT.write_text(
        "window.COOKBOOK_STYLES = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    # Cache-bust the data file in index.html whenever its content changes.
    digest = hashlib.sha1(OUTPUT.read_bytes()).hexdigest()[:10]
    index_html = SITE_DIR / "index.html"
    index_html.write_text(
        re.sub(r"styles-data\.js\?v=[^\"]+", f"styles-data.js?v={digest}", index_html.read_text(encoding="utf-8")),
        encoding="utf-8",
    )
    seo_pages.build_all(ROOT, SITE_DIR, styles, payload["categories"])
    print(f"PASS: wrote {OUTPUT.relative_to(ROOT)} with {len(styles)} styles")
    print(f"PASS: wrote {len(styles)} style pages, sitemap.xml and llms.txt")


if __name__ == "__main__":
    build()
