#!/usr/bin/env python3
"""Validate AI Visual Prompt Cookbook style.json files.

Two schema versions are accepted:
  - v2.1 (no "schema_version" field): the ten standard environment_variables
    (SUBJECT ... ASPECT_RATIO) are required and every example sets at least five.
  - v2.2 ("schema_version": "2.2"): each style declares its own variables. Only
    ASPECT_RATIO is required, every declared variable must be used by
    prompt_template, and every example must set every content variable.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


GALLERY_CATEGORIES = (
    "Photo + Doodle",
    "Zine + Collage",
    "Type Posters",
    "Travel + City",
    "Editorial + Minimal",
    "Product + Campaign",
)

ALLOWED_TOP_LEVEL_FIELDS = {
    "style_name",
    "style_slug",
    "style_version",
    "style_summary",
    "category",
    "environment_variables",
    "style_fidelity_anchors",
    "source_content_to_avoid",
    "visual_deconstruction",
    "image_treatment",
    "photographic_direction",
    "composition",
    "typography",
    "color_palette",
    "design_rules",
    "do",
    "avoid",
    "prompt_template",
    "negative_prompt",
    "examples",
    "schema_version",
}

SCHEMA_VERSIONS = ("2.1", "2.2")

REQUIRED_TOP_LEVEL_FIELDS = {
    "style_name",
    "style_slug",
    "style_version",
    "style_summary",
    "category",
    "environment_variables",
    "style_fidelity_anchors",
    "source_content_to_avoid",
    "visual_deconstruction",
    "composition",
    "typography",
    "color_palette",
    "design_rules",
    "do",
    "avoid",
    "prompt_template",
    "negative_prompt",
    "examples",
}

REQUIRED_ENVIRONMENT_VARIABLES = {
    "SUBJECT",
    "SUBJECT_ACTION",
    "PRODUCT_OR_PROP",
    "LOCATION",
    "BACKGROUND_ELEMENTS",
    "MAIN_TEXT",
    "SECONDARY_TEXT",
    "ACCENT_SYMBOL",
    "WARDROBE_STYLE",
    "ASPECT_RATIO",
}

# v2.2 variables that need no per-example value: the gallery fills ASPECT_RATIO
# from the chosen ratio and the others from the style's own fields.
AUTO_FILLED_VARIABLES = {"ASPECT_RATIO", "STYLE_FIDELITY_ANCHORS", "SOURCE_CONTENT_TO_AVOID", "NEGATIVE_PROMPT"}

FORBIDDEN_EXAMPLE_FIELDS = {
    "prompt_9x16",
    "prompt_16x9",
    "9x16_prompt",
    "16x9_prompt",
    "prompt_vertical",
    "prompt_horizontal",
    "full_prompt",
    "rendered_prompt",
    "final_prompt",
}

GENERIC_EXAMPLE_VALUES = {
    "main subject",
    "main action or pose",
    "object, product, prop, or visual anchor",
    "environment or setting",
    "secondary scene details and visual texture",
    "main headline or graphic text",
    "small supporting text or microcopy",
    "separator, sticker, symbol, or decorative mark",
    "styling, clothing, character, or visual treatment",
}

GENERIC_TEXT_SNIPPETS = {
    "provided variable value",
    "lorem ipsum",
    "todo",
    "tbd",
    "fixme",
}

MIN_LIST_LENGTHS = {
    "style_fidelity_anchors": 6,
    "source_content_to_avoid": 4,
    "design_rules": 4,
    "do": 3,
    "avoid": 3,
}

EXPECTED_STYLE_FILES = {"style.json", "preview-16x9.jpg", "preview-9x16.jpg"}
PLACEHOLDER_RE = re.compile(r"\{([A-Z0-9_]+)\}")
CJK_RE = re.compile(r"[\u3040-\u30ff\u3400-\u9fff\uac00-\ud7af\uff00-\uffef]")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class ErrorCollector:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def add(self, message: str) -> None:
        self.errors.append(message)

    def prefixed(self, prefix: str) -> "ErrorCollector":
        child = ErrorCollector()

        def add(message: str) -> None:
            self.add(f"{prefix}: {message}")

        child.add = add  # type: ignore[method-assign]
        return child


def load_json(path: Path, errors: ErrorCollector) -> dict[str, Any] | None:
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.add(f"{path}: I/O error: {exc}")
        return None
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        errors.add(f"{path}: invalid JSON: {exc}")
        return None
    if not isinstance(data, dict):
        errors.add(f"{path}: top-level JSON value must be an object")
        return None
    return data


def require_non_empty(value: Any, label: str, errors: ErrorCollector) -> None:
    if isinstance(value, str):
        if not value.strip():
            errors.add(f"{label} must be a non-empty string")
    elif isinstance(value, list):
        if not value:
            errors.add(f"{label} must be a non-empty list")
        for index, item in enumerate(value):
            if isinstance(item, str) and not item.strip():
                errors.add(f"{label}[{index}] must be non-empty")
    elif isinstance(value, dict):
        if not value:
            errors.add(f"{label} must be a non-empty object")
    elif value is None:
        errors.add(f"{label} is missing")


def iter_strings(value: Any, path: str) -> list[tuple[str, str]]:
    if isinstance(value, str):
        return [(path, value)]
    if isinstance(value, list):
        strings: list[tuple[str, str]] = []
        for index, item in enumerate(value):
            strings.extend(iter_strings(item, f"{path}[{index}]"))
        return strings
    if isinstance(value, dict):
        strings = []
        for key, item in value.items():
            child_path = f"{path}.{key}" if path else str(key)
            strings.extend(iter_strings(item, child_path))
        return strings
    return []


def validate_style_file(style_json: Path, errors: ErrorCollector) -> None:
    data = load_json(style_json, errors)
    if data is None:
        return

    schema_version = data.get("schema_version", "2.1")
    if schema_version not in SCHEMA_VERSIONS:
        errors.add("schema_version must be one of: " + ", ".join(SCHEMA_VERSIONS))
    v22 = schema_version == "2.2"

    extra = sorted(set(data) - ALLOWED_TOP_LEVEL_FIELDS)
    if extra:
        errors.add("unexpected top-level fields: " + ", ".join(extra))

    missing = sorted(REQUIRED_TOP_LEVEL_FIELDS - set(data))
    if missing:
        errors.add("missing top-level fields: " + ", ".join(missing))

    if "image_treatment" not in data and "photographic_direction" not in data:
        errors.add("must include image_treatment or photographic_direction")

    slug = data.get("style_slug")
    if not isinstance(slug, str) or not SLUG_RE.match(slug):
        errors.add("style_slug must be lowercase kebab-case")
    elif slug != style_json.parent.name:
        errors.add(f"style_slug must match folder name ({style_json.parent.name})")

    style_name = data.get("style_name")
    if isinstance(style_name, str) and isinstance(slug, str) and style_name == slug:
        errors.add("style_name must be human-readable, not a duplicate of style_slug")

    for field in ("style_name", "style_summary"):
        if isinstance(data.get(field), str) and CJK_RE.search(data[field]):
            errors.add(f"{field} must be written in English (README, catalog and gallery show it as is)")

    category = data.get("category")
    if isinstance(category, str) and category not in GALLERY_CATEGORIES:
        errors.add("category must be one of: " + ", ".join(GALLERY_CATEGORIES))

    for field in REQUIRED_TOP_LEVEL_FIELDS:
        if field in data:
            require_non_empty(data[field], field, errors)

    for path, text in iter_strings(data, ""):
        lowered = text.lower()
        if any(snippet in lowered for snippet in GENERIC_TEXT_SNIPPETS):
            errors.add(f"{path} contains generic helper text")

    for field, min_length in MIN_LIST_LENGTHS.items():
        value = data.get(field)
        if not isinstance(value, list):
            errors.add(f"{field} must be a list")
        elif any(not isinstance(item, str) for item in value):
            errors.add(f"{field} entries must all be strings")
        elif len(value) < min_length:
            errors.add(f"{field} has too few entries")
        elif len(value) != len(set(value)):
            errors.add(f"{field} contains duplicate entries")

    env = data.get("environment_variables")
    if not isinstance(env, dict):
        errors.add("environment_variables must be an object")
        env_keys: set[str] = set()
    else:
        env_keys = set(env)
        required_env = {"ASPECT_RATIO"} if v22 else REQUIRED_ENVIRONMENT_VARIABLES
        missing_env = sorted(required_env - env_keys)
        if missing_env:
            errors.add("missing environment_variables keys: " + ", ".join(missing_env))
        for key, value in env.items():
            if not isinstance(key, str) or not key:
                errors.add("environment_variables keys must be non-empty strings")
            if not isinstance(value, str) or not value.strip():
                errors.add(f"environment_variables.{key} must be a non-empty string")

    prompt_template = data.get("prompt_template")
    if isinstance(prompt_template, str):
        placeholders = set(PLACEHOLDER_RE.findall(prompt_template))
        undefined = sorted(placeholders - env_keys)
        if undefined:
            errors.add("prompt_template has undefined placeholders: " + ", ".join(undefined))
        unused = sorted(env_keys - placeholders)
        if v22 and unused:
            errors.add("environment_variables not used by prompt_template: " + ", ".join(unused))
    else:
        errors.add("prompt_template must be a string")

    examples = data.get("examples")
    if not isinstance(examples, list):
        errors.add("examples must be a list")
        return
    if len(examples) < 3:
        errors.add("examples must contain at least 3 cases")

    for index, case in enumerate(examples):
        prefix = f"examples[{index}]"
        if not isinstance(case, dict):
            errors.add(f"{prefix} must be an object")
            continue

        case_keys = set(case)
        forbidden = sorted(case_keys & FORBIDDEN_EXAMPLE_FIELDS)
        if forbidden:
            errors.add(f"{prefix} contains rendered-prompt fields: " + ", ".join(forbidden))
        extra_case_keys = sorted(case_keys - {"case_name", "values"})
        if extra_case_keys:
            errors.add(f"{prefix} has unexpected keys: " + ", ".join(extra_case_keys))

        case_name = case.get("case_name")
        if not isinstance(case_name, str) or not case_name.strip():
            errors.add(f"{prefix}.case_name must be a non-empty string")

        values = case.get("values")
        if not isinstance(values, dict):
            errors.add(f"{prefix}.values must be an object")
            continue
        value_keys = set(values)
        if v22:
            unset = sorted(env_keys - AUTO_FILLED_VARIABLES - value_keys)
            if unset:
                errors.add(f"{prefix}.values must set every content variable; missing: " + ", ".join(unset))
        elif len(values) < 5:
            errors.add(f"{prefix}.values must define at least 5 usable variables")

        if "ASPECT_RATIO" in value_keys:
            errors.add(f"{prefix}.values must not include ASPECT_RATIO")
        unknown_value_keys = sorted(value_keys - env_keys)
        if unknown_value_keys:
            errors.add(f"{prefix}.values has keys not declared in environment_variables: " + ", ".join(unknown_value_keys))
        forbidden_value_keys = sorted(value_keys & FORBIDDEN_EXAMPLE_FIELDS)
        if forbidden_value_keys:
            errors.add(f"{prefix}.values contains rendered-prompt keys: " + ", ".join(forbidden_value_keys))

        for key, value in values.items():
            if not isinstance(value, str) or not value.strip():
                errors.add(f"{prefix}.values.{key} must be a non-empty string")
            elif value.strip() in GENERIC_EXAMPLE_VALUES:
                errors.add(f"{prefix}.values.{key} is still a generic placeholder")


def validate_style_folder(folder: Path, errors: ErrorCollector) -> None:
    files = {path.name for path in folder.iterdir() if path.is_file() and not path.name.startswith(".")}
    if files != EXPECTED_STYLE_FILES:
        errors.add(
            f"{folder}: expected exactly {sorted(EXPECTED_STYLE_FILES)}, found {sorted(files)}"
        )
    validate_style_file(folder / "style.json", errors.prefixed(str(folder / "style.json")))


def iter_style_folders(path: Path) -> list[Path]:
    if (path / "styles").is_dir():
        return sorted(child for child in (path / "styles").iterdir() if child.is_dir())
    if (path / "style.json").exists():
        return [path]
    raise SystemExit(f"No styles directory or style.json found at {path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate style.json v2.1 / v2.2 quality gates.")
    parser.add_argument("path", type=Path, nargs="?", default=Path("."))
    args = parser.parse_args()

    errors = ErrorCollector()
    folders = iter_style_folders(args.path.expanduser().resolve())
    for folder in folders:
        validate_style_folder(folder, errors)

    if errors.errors:
        for message in errors.errors:
            print("FAIL:", message, file=sys.stderr)
        raise SystemExit(1)

    print(f"PASS: {len(folders)} style folders validated against style.json v2.1 / v2.2 quality gates")


if __name__ == "__main__":
    main()
