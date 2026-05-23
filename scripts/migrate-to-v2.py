#!/usr/bin/env python3
"""Migrate v1 style.json files in styles/ to the v2.1 schema (in place)."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


FIELD_RENAMES = {
    "version": "style_version",
    "summary": "style_summary",
    "variables": "environment_variables",
    "example_cases": "examples",
    "composition_rules": "composition",
    "style_rules": "design_rules",
    "typography_rules": "typography",
}

FIELDS_TO_DELETE = {
    "updated_at",
    "status",
    "preview",
    "usage_note",
    "license",
    "related_styles",
    "product_selection_strategy",
}

V2_REQUIRED_FIELDS = {
    "style_name",
    "style_slug",
    "style_summary",
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
}

V2_OPTIONAL_FIELDS = {
    "style_version",
    "image_treatment",
    "photographic_direction",
    "examples",
}

V2_ALLOWED_FIELDS = V2_REQUIRED_FIELDS | V2_OPTIONAL_FIELDS

ALLOWED_CASE_KEYS = {"case_name", "values"}

FORBIDDEN_CASE_FIELDS = {
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

PLACEHOLDER_RE = re.compile(r"\{([A-Z0-9_]+)\}")


def migrate_examples(examples: object) -> tuple[list, list[str]]:
    """Return (cleaned_examples, notes). Drops forbidden fields and ASPECT_RATIO from values."""
    notes: list[str] = []
    if not isinstance(examples, list):
        notes.append("examples-not-a-list-reset-to-[]")
        return [], notes

    cleaned: list = []
    for idx, case in enumerate(examples):
        if not isinstance(case, dict):
            notes.append(f"examples[{idx}]-not-a-dict-dropped")
            continue

        # Rename legacy keys
        if "variables" in case and "values" not in case:
            case["values"] = case.pop("variables")
        if "name" in case and "case_name" not in case:
            case["case_name"] = case.pop("name")

        # Drop forbidden rendered-prompt fields from the case
        for forbidden in list(FORBIDDEN_CASE_FIELDS & set(case)):
            case.pop(forbidden, None)

        # Build a clean case with only allowed keys
        new_case: dict = {}
        if "case_name" in case:
            new_case["case_name"] = case["case_name"]
        values = case.get("values")
        if isinstance(values, dict):
            clean_values = {
                k: v
                for k, v in values.items()
                if k not in FORBIDDEN_CASE_FIELDS and k != "ASPECT_RATIO"
            }
            new_case["values"] = clean_values
        else:
            new_case["values"] = {}

        cleaned.append(new_case)
    return cleaned, notes


def migrate_one(data: dict) -> tuple[dict, dict]:
    """Return (new_data, report). report has removed/added/renamed/notes."""
    report = {
        "renamed": [],
        "removed": [],
        "added": [],
        "extras_dropped": [],
        "notes": [],
    }

    # 1. Handle palette → color_palette merge before generic rename pass.
    if "palette" in data:
        if "color_palette" in data:
            data.pop("palette")
            report["notes"].append("palette-dropped-color_palette-present")
        else:
            data["color_palette"] = data.pop("palette")
            report["renamed"].append("palette->color_palette")

    # 2. Rename top-level fields.
    for old_name, new_name in FIELD_RENAMES.items():
        if old_name in data:
            if new_name in data:
                # Collision: prefer existing new_name, drop the old.
                data.pop(old_name)
                report["notes"].append(f"{old_name}-dropped-{new_name}-present")
            else:
                data[new_name] = data.pop(old_name)
                report["renamed"].append(f"{old_name}->{new_name}")

    # 3. Delete the explicit removal list.
    for field in FIELDS_TO_DELETE:
        if field in data:
            data.pop(field)
            report["removed"].append(field)

    # 4. Drop any remaining keys not in the v2.1 whitelist (catch-all).
    for field in list(data.keys()):
        if field not in V2_ALLOWED_FIELDS:
            data.pop(field)
            report["extras_dropped"].append(field)

    # 5. Clean examples (mutates in place semantics on cases).
    if "examples" in data:
        cleaned, notes = migrate_examples(data["examples"])
        data["examples"] = cleaned
        report["notes"].extend(notes)

    return data, report


def reorder_for_output(data: dict) -> dict:
    """Stable ordering: required fields first, then optional, in canonical order."""
    canonical_order = [
        "style_name",
        "style_slug",
        "style_version",
        "style_summary",
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
    ]
    out: dict = {}
    for key in canonical_order:
        if key in data:
            out[key] = data[key]
    # Append anything unexpected last (shouldn't happen after whitelist pass).
    for key in data:
        if key not in out:
            out[key] = data[key]
    return out


def undefined_prompt_placeholders(data: dict) -> list[str]:
    """Return prompt_template placeholders not declared in environment_variables."""
    prompt_template = data.get("prompt_template")
    environment_variables = data.get("environment_variables")
    if not isinstance(prompt_template, str) or not isinstance(environment_variables, dict):
        return []
    placeholders = set(PLACEHOLDER_RE.findall(prompt_template))
    return sorted(placeholders - set(environment_variables))


def format_report_line(slug: str, status: str, report: dict) -> str:
    parts = [
        f"renamed={len(report['renamed'])}",
        f"removed={len(report['removed']) + len(report['extras_dropped'])}",
        f"added={len(report['added'])}",
    ]
    line = f"{status} {slug}  " + "  ".join(parts)
    detail_bits = []
    removed_all = report["removed"] + report["extras_dropped"]
    if removed_all:
        detail_bits.append("removed: " + ", ".join(removed_all))
    if report["added"]:
        detail_bits.append("added: " + ", ".join(report["added"]))
    if report["renamed"]:
        detail_bits.append("renamed: " + ", ".join(report["renamed"]))
    if report["notes"]:
        detail_bits.append("notes: " + "; ".join(report["notes"]))
    if detail_bits:
        line += "\n    " + "\n    ".join(detail_bits)
    return line


def process_style_dir(style_dir: Path, dry_run: bool) -> tuple[str, dict | None]:
    style_json = style_dir / "style.json"
    if not style_json.exists():
        return "skip-no-style-json", None

    try:
        raw = style_json.read_text(encoding="utf-8")
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"X  {style_dir.name}  invalid JSON: {exc}", file=sys.stderr)
        return "error", None
    except OSError as exc:
        print(f"X  {style_dir.name}  read failed: {exc}", file=sys.stderr)
        return "error", None

    if not isinstance(data, dict):
        print(f"X  {style_dir.name}  top-level is not a JSON object", file=sys.stderr)
        return "error", None

    try:
        migrated, report = migrate_one(data)
    except Exception as exc:  # noqa: BLE001 - we want to keep going across styles
        print(f"X  {style_dir.name}  migration crashed: {exc}", file=sys.stderr)
        return "error", None

    ordered = reorder_for_output(migrated)
    undefined_placeholders = undefined_prompt_placeholders(ordered)
    if undefined_placeholders:
        print(
            f"X  {style_dir.name}  prompt_template has undefined placeholders: "
            + ", ".join(undefined_placeholders),
            file=sys.stderr,
        )
        return "error", None

    output = json.dumps(ordered, indent=2, ensure_ascii=False) + "\n"

    if not dry_run:
        try:
            style_json.write_text(output, encoding="utf-8")
        except OSError as exc:
            print(f"X  {style_dir.name}  write failed: {exc}", file=sys.stderr)
            return "error", None

    status = "[dry] " if dry_run else "OK   "
    return status, report


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Migrate every styles/*/style.json from v1 to v2.1 schema, in place."
    )
    parser.add_argument("repo_root", type=Path, help="Path to the repo root.")
    parser.add_argument("--dry-run", action="store_true", help="Do not write files.")
    parser.add_argument(
        "--only",
        type=str,
        default=None,
        help="Only process the named style folder (for testing).",
    )
    args = parser.parse_args()

    repo_root = args.repo_root.expanduser().resolve()
    styles_root = repo_root / "styles"
    if not styles_root.is_dir():
        print(f"X  styles directory not found at {styles_root}", file=sys.stderr)
        raise SystemExit(1)

    migrated = 0
    skipped = 0
    errored = 0

    for style_dir in sorted(styles_root.iterdir()):
        if not style_dir.is_dir():
            continue
        if args.only is not None and style_dir.name != args.only:
            continue

        status, report = process_style_dir(style_dir, dry_run=args.dry_run)
        if status == "skip-no-style-json":
            skipped += 1
            print(f"-    {style_dir.name}  (no style.json, skipped)")
            continue
        if status == "error" or report is None:
            errored += 1
            continue

        migrated += 1
        print(format_report_line(style_dir.name, status.strip(), report))

    print()
    print(
        f"Done. migrated={migrated}  skipped={skipped}  errored={errored}"
        + ("  [dry-run, no files written]" if args.dry_run else "")
    )


if __name__ == "__main__":
    main()
