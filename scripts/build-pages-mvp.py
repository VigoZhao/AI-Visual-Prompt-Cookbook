#!/usr/bin/env python3
"""Build the local static MVP for the style browser."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from typing import Any

import seo_pages


ROOT = Path(__file__).resolve().parents[1]
STYLES_DIR = ROOT / "styles"
README = ROOT / "README.md"
SITE_DIR = ROOT / "site"
OUTPUT = SITE_DIR / "styles-data.js"

SWITCHABLE_ASPECT_RATIOS = ("16:9", "9:16", "4:5", "5:4")
RATIO_RE = re.compile(r"\b(\d+:\d+)\b")

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
                "styleJson": f"../styles/{slug}/style.json",
                "copyPromptDoc": f"../docs/copy-prompts/{slug}.md",
                "folder": f"../styles/{slug}/",
                "anchors": first_text_list(data.get("style_fidelity_anchors"), 6),
                "variables": variables,
                "aspectRatios": aspect_ratios_for(data),
                "jsonText": json_text,
            }
        )

    used_categories = {style["category"] for style in styles}
    payload = {
        "styleCount": len(styles),
        "categories": [category for category in GALLERY_CATEGORIES if category in used_categories],
        "styles": styles,
    }
    SITE_DIR.mkdir(exist_ok=True)
    OUTPUT.write_text(
        "window.COOKBOOK_STYLES = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    seo_pages.build_all(ROOT, SITE_DIR, styles, payload["categories"])
    print(f"PASS: wrote {OUTPUT.relative_to(ROOT)} with {len(styles)} styles")
    print(f"PASS: wrote {len(styles)} style pages, sitemap.xml and llms.txt")


if __name__ == "__main__":
    build()
