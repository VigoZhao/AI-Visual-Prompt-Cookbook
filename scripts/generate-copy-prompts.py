#!/usr/bin/env python3
"""Generate simple copy-prompt docs from style.json files."""

from __future__ import annotations

import argparse
import json
import textwrap
from pathlib import Path
from typing import Any


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

VARIABLE_LABELS = {
    "SUBJECT": "Subject",
    "SUBJECT_ACTION": "Action",
    "PRODUCT_OR_PROP": "Prop / product",
    "LOCATION": "Location",
    "BACKGROUND_ELEMENTS": "Background",
    "MAIN_TEXT": "Main text",
    "SECONDARY_TEXT": "Secondary text",
    "ACCENT_SYMBOL": "Accent symbol",
    "WARDROBE_STYLE": "Styling",
}

# v2.2 styles declare their own variables; these are filled from the style itself.
AUTO_FILLED_VARIABLES = {"ASPECT_RATIO", "STYLE_FIDELITY_ANCHORS", "SOURCE_CONTENT_TO_AVOID", "NEGATIVE_PROMPT"}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def first_example_values(data: dict[str, Any]) -> tuple[str, dict[str, str]]:
    examples = data.get("examples")
    if not isinstance(examples, list) or not examples:
        return "Custom example", {}

    case = examples[0]
    if not isinstance(case, dict):
        return "Custom example", {}

    case_name = case.get("case_name")
    values = case.get("values")
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


def bullets(items: Any, limit: int) -> list[str]:
    if not isinstance(items, list):
        return []
    result = []
    for item in items:
        if isinstance(item, str) and item.strip():
            result.append(item.strip())
        if len(result) == limit:
            break
    return result


def wrap_block(text: str, width: int = 96) -> str:
    return "\n".join(textwrap.fill(line, width=width) if line else "" for line in text.splitlines())


def prompt_variables(data: dict[str, Any]) -> list[str]:
    """v2.1 styles use the ten standard variables; v2.2 styles list their own, in declared order."""
    env = data.get("environment_variables")
    if data.get("schema_version") != "2.2" or not isinstance(env, dict):
        return VARIABLE_ORDER
    return [key for key in env if key not in AUTO_FILLED_VARIABLES]


def label_for(key: str) -> str:
    return VARIABLE_LABELS.get(key) or key.replace("_", " ").capitalize()


def render_prompt(data: dict[str, Any], case_name: str, values: dict[str, str]) -> str:
    style_name = str(data.get("style_name", "Untitled Style")).strip()
    style_summary = str(data.get("style_summary", "")).strip()
    negative_prompt = str(data.get("negative_prompt", "")).strip()
    anchors = bullets(data.get("style_fidelity_anchors"), 5)

    lines = [
        f'Use the "{style_name}" visual style as the locked style.',
        "",
        "Create a 16:9 image.",
        "",
    ]

    for key in prompt_variables(data):
        lines.append(f"{label_for(key)}: {fallback_value(data, values, key)}")

    if style_summary:
        lines.extend(["", "Style direction:", wrap_block(style_summary)])

    if anchors:
        lines.extend(["", "Keep visible:"])
        lines.extend(f"- {anchor}" for anchor in anchors)

    if negative_prompt:
        lines.extend(["", "Avoid:", wrap_block(negative_prompt)])

    lines.extend(
        [
            "",
            "Do not copy source content, real logos, watermarks, platform UI, QR codes, or exact",
            "reference layouts. Keep the visual system, but change the subject, text, and scene.",
        ]
    )
    return "\n".join(lines).strip() + "\n"


def render_style_doc(style_json: Path, docs_dir: Path) -> tuple[str, str]:
    data = load_json(style_json)
    slug = str(data.get("style_slug", style_json.parent.name)).strip()
    style_name = str(data.get("style_name", slug)).strip()
    summary = str(data.get("style_summary", "")).strip()
    case_name, values = first_example_values(data)
    prompt = render_prompt(data, case_name, values)

    style_link = f"../../styles/{slug}/style.json"
    preview_link = f"../../styles/{slug}/preview-16x9.jpg"
    folder_link = f"../../styles/{slug}/"

    body = [
        f"# {style_name}",
        "",
        f"![{style_name} preview]({preview_link})",
        "",
    ]

    if summary:
        body.extend([summary, ""])

    body.extend(
        [
            "## Copy Prompt",
            "",
            f"Default case: `{case_name}`",
            "",
            "```text",
            prompt.rstrip(),
            "```",
            "",
            "## Full Style",
            "",
            f"- [Open style.json]({style_link})",
            f"- [Open style folder]({folder_link})",
            "",
            "<!-- Generated by scripts/generate-copy-prompts.py. Do not edit manually. -->",
            "",
        ]
    )

    output_path = docs_dir / f"{slug}.md"
    output_path.write_text("\n".join(body), encoding="utf-8")
    return style_name, slug


def render_index(styles: list[tuple[str, str]], docs_dir: Path) -> None:
    rows = ["# Copy Prompt Library", ""]
    rows.extend(
        [
            "These quick prompts are generated from the canonical `style.json` files.",
            "Use them when you want a short copy-and-paste entry point; use `style.json` when you want the full reusable style system.",
            "",
            "| Style | Copy Prompt | Full JSON |",
            "| --- | --- | --- |",
        ]
    )

    for style_name, slug in styles:
        rows.append(f"| {style_name} | [Copy Prompt]({slug}.md) | [style.json](../../styles/{slug}/style.json) |")

    rows.extend(["", "<!-- Generated by scripts/generate-copy-prompts.py. Do not edit manually. -->", ""])
    (docs_dir / "README.md").write_text("\n".join(rows), encoding="utf-8")


def generate(repo: Path) -> None:
    styles_dir = repo / "styles"
    docs_dir = repo / "docs" / "copy-prompts"
    docs_dir.mkdir(parents=True, exist_ok=True)

    generated: list[tuple[str, str]] = []
    for style_json in sorted(styles_dir.glob("*/style.json")):
        generated.append(render_style_doc(style_json, docs_dir))

    render_index(generated, docs_dir)
    print(f"PASS: generated {len(generated)} copy prompts in {docs_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate simple copy-prompt docs from style.json files.")
    parser.add_argument("repo", type=Path, nargs="?", default=Path("."))
    args = parser.parse_args()
    generate(args.repo.resolve())


if __name__ == "__main__":
    main()
