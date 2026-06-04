#!/usr/bin/env python3
"""Build the local static MVP for the style browser."""

from __future__ import annotations

import html
import json
import re
import textwrap
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
STYLES_DIR = ROOT / "styles"
README = ROOT / "README.md"
SITE_DIR = ROOT / "site"
OUTPUT = SITE_DIR / "styles-data.js"

VARIABLE_ORDER = [
    "SUBJECT",
    "SUBJECT_ACTION",
    "PRODUCT_OR_PROP",
    "LOCATION",
    "BACKGROUND_ELEMENTS",
    "MAIN_TEXT",
    "SECONDARY_TEXT",
    "ACCENT_SYMBOL",
    "WARDROBE_STYLE",
]

CATEGORY_RULES = [
    (
        "Photo + Doodle",
        [
            "doodle",
            "snapshot",
            "diary",
            "photo",
            "pet",
            "mascot",
            "monster",
            "landmark",
            "transit",
            "subway",
            "metro",
        ],
    ),
    (
        "Zine + Collage",
        [
            "zine",
            "collage",
            "grunge",
            "sticker",
            "ransom",
            "skate",
            "hip-hop",
            "y2k",
            "music",
        ],
    ),
    (
        "Type Posters",
        [
            "type",
            "typographic",
            "letter",
            "halftone",
            "comic",
            "anime",
            "manga",
            "bubble",
            "chinese",
            "poster",
        ],
    ),
    (
        "Travel + City",
        [
            "travel",
            "tokyo",
            "city",
            "vlog",
            "mountain",
            "trail",
            "outdoor",
            "backseat",
            "transit",
        ],
    ),
    (
        "Editorial + Minimal",
        [
            "editorial",
            "minimal",
            "noir",
            "portrait",
            "analog",
            "future",
            "diamond",
            "checkerboard",
            "luxury",
        ],
    ),
    (
        "Product + Campaign",
        [
            "product",
            "launch",
            "gadget",
            "hud",
            "macro",
            "plush",
            "avatar",
            "campaign",
            "tech",
            "toy",
            "food",
            "ad",
            "advertising",
            "promotion",
            "card",
        ],
    ),
]


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


def first_example_values(data: dict[str, Any]) -> tuple[str, dict[str, str]]:
    examples = data.get("examples")
    if not isinstance(examples, list) or not examples:
        return "Custom example", {}
    first = examples[0]
    if not isinstance(first, dict):
        return "Custom example", {}
    case_name = first.get("case_name")
    values = first.get("values")
    if not isinstance(case_name, str) or not case_name.strip():
        case_name = "Custom example"
    if not isinstance(values, dict):
        values = {}
    clean_values = {str(key): str(value) for key, value in values.items() if isinstance(value, str)}
    return case_name.strip(), clean_values


def fallback_value(data: dict[str, Any], values: dict[str, str], key: str) -> str:
    value = values.get(key)
    if value and value.strip():
        return value.strip()
    env = data.get("environment_variables")
    if isinstance(env, dict) and isinstance(env.get(key), str):
        return f"[your {env[key]}]"
    return f"[your {key.lower()}]"


def wrap(text: str, width: int = 96) -> str:
    return "\n".join(textwrap.fill(line, width=width) if line else "" for line in text.splitlines())


def copy_prompt(data: dict[str, Any], values: dict[str, str]) -> str:
    name = str(data.get("style_name", "Untitled Style")).strip()
    summary = str(data.get("style_summary", "")).strip()
    negative = str(data.get("negative_prompt", "")).strip()
    anchors = first_text_list(data.get("style_fidelity_anchors"), 5)

    lines = [
        f'Use the "{name}" visual style as the locked visual system.',
        "",
        "Create a 16:9 image.",
        "",
    ]
    for key in VARIABLE_ORDER:
        label = key.lower().replace("_", " ").capitalize()
        lines.append(f"{label}: {fallback_value(data, values, key)}")

    if summary:
        lines.extend(["", "Style direction:", wrap(summary)])
    if anchors:
        lines.extend(["", "Keep visible:"])
        lines.extend(f"- {anchor}" for anchor in anchors)
    if negative:
        lines.extend(["", "Avoid:", wrap(negative)])

    lines.extend(
        [
            "",
            "Do not copy source content, real logos, watermarks, platform UI, QR codes, or exact",
            "reference layouts. Keep the visual system, but change the subject, text, and scene.",
        ]
    )
    return "\n".join(lines).strip()


def category_for(slug: str, data: dict[str, Any]) -> str:
    parts = [
        slug,
        str(data.get("style_name", "")),
        str(data.get("style_summary", "")),
    ]
    visual = data.get("visual_deconstruction")
    if isinstance(visual, dict):
        parts.append(str(visual.get("style_category", "")))
    haystack = " ".join(parts).lower()

    best_category = "Editorial + Minimal"
    best_score = -1
    for category, keywords in CATEGORY_RULES:
        score = sum(1 for keyword in keywords if keyword in haystack)
        if score > best_score:
            best_category = category
            best_score = score
    return best_category


def build() -> None:
    readme_order, readme_descriptions = read_readme_order()
    style_paths = {path.parent.name: path for path in STYLES_DIR.glob("*/style.json")}
    ordered_slugs = [slug for slug in readme_order if slug in style_paths]
    ordered_slugs.extend(sorted(slug for slug in style_paths if slug not in ordered_slugs))

    styles: list[dict[str, Any]] = []
    for slug in ordered_slugs:
        data = load_json(style_paths[slug])
        name = str(data.get("style_name", slug)).strip()
        summary = str(data.get("style_summary", "")).strip()
        case_name, values = first_example_values(data)
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
                "exampleName": case_name,
                "copyPrompt": copy_prompt(data, values),
            }
        )

    payload = {
        "styleCount": len(styles),
        "categories": sorted({style["category"] for style in styles}),
        "styles": styles,
    }
    SITE_DIR.mkdir(exist_ok=True)
    OUTPUT.write_text(
        "window.COOKBOOK_STYLES = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    print(f"PASS: wrote {OUTPUT.relative_to(ROOT)} with {len(styles)} styles")


if __name__ == "__main__":
    build()
