#!/usr/bin/env python3
"""Generate the style galleries in all six READMEs and docs/CATALOG.md.

Single source of truth:
  - data/catalog.json    gallery order (newest first), short gallery summaries
                         (optionally translated), and the six Featured styles
  - styles/*/style.json  style names and full summaries

This script rewrites, in every README*.md:
  - the "styles" and "previews" badge counts
  - the region between the BEGIN/END GENERATED: featured markers
  - the region between the BEGIN/END GENERATED: all-styles markers
    (README.md gets every style; the translated READMEs get the newest few
    and link to the full gallery, so they stay small)
and rewrites docs/CATALOG.md completely.

Multi-part series (<base>-part-NN / <base>-set-NN, the same rule the online
gallery uses) are folded: one card for the series in the READMEs, and the
parts collapsed under the base style in docs/CATALOG.md.

To publish a new style, add it to the top of "styles" in data/catalog.json
(and to "featured" if it should be featured), then run this script. Never edit
the generated regions by hand: CI regenerates them and fails if they differ.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
STYLES_DIR = ROOT / "styles"
CATALOG_DATA = ROOT / "data" / "catalog.json"
CATALOG_MD = ROOT / "docs" / "CATALOG.md"

FEATURED_COUNT = 6
COLUMNS = 3
LATEST_COUNT = 9
GALLERY_URL = "https://prompts.vigocreativeai.com/site/"
VARIANT_RE = re.compile(r"^(?P<base>.+)-(?P<kind>set|part)-(?P<number>\d+)$")

LANGS: dict[str, dict[str, str]] = {
    "en": {
        "file": "README.md",
        "featured_intro": "Six visual systems to start with. Every style ships as one JSON plus two preview images. Browse the complete set of {count} in the [All Styles](#all-styles) gallery below.",
        "all_intro": "Browse all {count} styles below.\n\nThe complete library, including the featured styles above. Parts of a series share one card. For full descriptions and all file links per style, see [docs/CATALOG.md](docs/CATALOG.md).",
        "series": "Series: ",
        "open": "Open style.json",
        "copy": "Copy Prompt",
        "folder": "Folder",
    },
    "zh-CN": {
        "file": "README.zh-CN.md",
        "featured_intro": "先看这 6 个风格。每个风格都保持轻量：一个 JSON 加两张预览图。完整 {count} 个风格见[在线画廊]({gallery})或英文 README 的 [All Styles](README.md#all-styles)。",
        "latest_intro": "下面是最新的 {latest} 个风格。全部 {count} 个风格请看[在线画廊]({gallery})、英文 README 的 [All Styles](README.md#all-styles)，或带完整描述的 [docs/CATALOG.md](docs/CATALOG.md)。",
        "series": "系列：",
        "open": "打开 style.json",
        "copy": "复制提示词",
        "folder": "目录",
    },
    "zh-TW": {
        "file": "README.zh-TW.md",
        "featured_intro": "先看這 6 個風格。每個風格都保持輕量：一個 JSON 加兩張預覽圖。完整 {count} 個風格見[線上畫廊]({gallery})或英文 README 的 [All Styles](README.md#all-styles)。",
        "latest_intro": "下面是最新的 {latest} 個風格。全部 {count} 個風格請看[線上畫廊]({gallery})、英文 README 的 [All Styles](README.md#all-styles)，或帶完整描述的 [docs/CATALOG.md](docs/CATALOG.md)。",
        "series": "系列：",
        "open": "打開 style.json",
        "copy": "複製提示詞",
        "folder": "目錄",
    },
    "ja": {
        "file": "README.ja.md",
        "featured_intro": "まずこの 6 つを見ると、ライブラリの幅がわかります。すべてのスタイルは 1 つの JSON と 2 枚のプレビュー画像で構成されています。{count} 種すべては[オンラインギャラリー]({gallery})または英語版 README の [All Styles](README.md#all-styles) で確認できます。",
        "latest_intro": "最新の {latest} スタイルを下に掲載しています。全 {count} スタイルは[オンラインギャラリー]({gallery})、英語版 README の [All Styles](README.md#all-styles)、または詳細説明付きの [docs/CATALOG.md](docs/CATALOG.md) をご覧ください。",
        "series": "シリーズ：",
        "open": "style.json を開く",
        "copy": "プロンプトをコピー",
        "folder": "フォルダ",
    },
    "ko": {
        "file": "README.ko.md",
        "featured_intro": "이 6개 스타일로 시작하면 라이브러리의 범위를 빠르게 이해할 수 있습니다. 모든 스타일은 JSON 하나와 미리보기 이미지 두 장으로 구성됩니다. 전체 {count}개는 [온라인 갤러리]({gallery}) 또는 영어 README의 [All Styles](README.md#all-styles)에서 볼 수 있습니다.",
        "latest_intro": "아래는 최신 {latest}개 스타일입니다. 전체 {count}개 스타일은 [온라인 갤러리]({gallery}), 영어 README의 [All Styles](README.md#all-styles), 또는 전체 설명이 있는 [docs/CATALOG.md](docs/CATALOG.md)에서 볼 수 있습니다.",
        "series": "시리즈: ",
        "open": "style.json 열기",
        "copy": "프롬프트 복사",
        "folder": "폴더",
    },
    "id": {
        "file": "README.id.md",
        "featured_intro": "Enam sistem visual ini cocok untuk memulai. Setiap gaya berisi satu JSON dan dua gambar preview. Jelajahi {count} gaya lengkap di [galeri online]({gallery}) atau [All Styles](README.md#all-styles) di README bahasa Inggris.",
        "latest_intro": "Berikut {latest} gaya terbaru. Untuk semua {count} gaya, lihat [galeri online]({gallery}), [All Styles](README.md#all-styles) di README bahasa Inggris, atau [docs/CATALOG.md](docs/CATALOG.md) dengan deskripsi lengkap.",
        "series": "Seri: ",
        "open": "Buka style.json",
        "copy": "Salin Prompt",
        "folder": "Folder",
    },
}

TABLE_COMMENT = "<!-- HTML table used for rich image+link cells -->"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def load_styles() -> dict[str, dict[str, Any]]:
    styles = {}
    for path in sorted(STYLES_DIR.glob("*/style.json")):
        styles[path.parent.name] = json.loads(path.read_text(encoding="utf-8"))
    return styles


def load_catalog(styles: dict[str, dict[str, Any]]) -> dict[str, Any]:
    data = json.loads(CATALOG_DATA.read_text(encoding="utf-8"))
    order = [entry["slug"] for entry in data["styles"]]
    duplicates = sorted({slug for slug in order if order.count(slug) > 1})
    if duplicates:
        fail(f"data/catalog.json lists these styles more than once: {duplicates}")
    missing = sorted(set(styles) - set(order))
    if missing:
        fail(f"styles/ folders missing from data/catalog.json \"styles\" (add them at the top): {missing}")
    unknown = sorted(set(order) - set(styles))
    if unknown:
        fail(f"data/catalog.json lists styles with no styles/<slug>/style.json: {unknown}")
    for entry in data["styles"]:
        if not entry.get("summary", "").strip():
            fail(f"data/catalog.json: {entry['slug']} needs a short \"summary\"")
        for lang in entry.get("summary_i18n", {}):
            if lang not in LANGS or lang == "en":
                fail(f"data/catalog.json: {entry['slug']} has unknown summary_i18n language {lang!r}")
    featured = [entry["slug"] for entry in data["featured"]]
    if len(featured) != FEATURED_COUNT or len(set(featured)) != FEATURED_COUNT:
        fail(f"data/catalog.json \"featured\" must list exactly {FEATURED_COUNT} distinct styles, got {featured}")
    unknown = sorted(set(featured) - set(styles))
    if unknown:
        fail(f"data/catalog.json \"featured\" lists unknown styles: {unknown}")
    return data


def series_groups(data: dict[str, Any]) -> list[list[dict[str, Any]]]:
    """Group catalog entries into series, in gallery order.

    A <base>-part-NN / <base>-set-NN style joins the group of <base> when <base>
    is published; the group sits where its first member does. Everything else
    is a group of one.
    """
    slugs = {entry["slug"] for entry in data["styles"]}
    groups: dict[str, list[dict[str, Any]]] = {}
    for entry in data["styles"]:
        match = VARIANT_RE.match(entry["slug"])
        key = match.group("base") if match and match.group("base") in slugs else entry["slug"]
        groups.setdefault(key, []).append(entry)
    for key, members in groups.items():
        members.sort(key=lambda entry: (entry["slug"] != key, part_number(entry["slug"]), entry["slug"]))
    return list(groups.values())


def part_number(slug: str) -> int:
    match = VARIANT_RE.match(slug)
    return int(match.group("number")) if match else 0


def part_label(slug: str) -> str:
    match = VARIANT_RE.match(slug)
    return f"{match.group('kind').capitalize()} {int(match.group('number'))}"


def rows(cells: list[str]) -> list[str]:
    lines = ["<table>"]
    for start in range(0, len(cells), COLUMNS):
        lines.append("<tr>")
        lines.extend(cells[start : start + COLUMNS])
        lines.append("</tr>")
    lines.append("</table>")
    return lines


def featured_block(lang: dict[str, str], data: dict[str, Any], styles: dict[str, dict[str, Any]]) -> str:
    cells = []
    for entry in data["featured"]:
        slug = entry["slug"]
        name = styles[slug]["style_name"]
        description = entry.get("description") or styles[slug]["style_summary"]
        cells.append(
            "\n".join(
                [
                    '<td width="33%" valign="top">',
                    f'<a href="styles/{slug}"><img src="assets/thumbs/{slug}-16x9.jpg" alt="{name} preview"></a>',
                    f"<h3>{name}</h3>",
                    f"<p>{description}</p>",
                    f'<p><a href="styles/{slug}/style.json"><strong>{lang["open"]}</strong></a>'
                    f' · <a href="docs/copy-prompts/{slug}.md">{lang["copy"]}</a>'
                    f' · <a href="styles/{slug}">{lang["folder"]}</a></p>',
                    "</td>",
                ]
            )
        )
    count = len(data["styles"])
    intro = lang["featured_intro"].format(count=count, gallery=GALLERY_URL)
    return "\n".join([intro, "", TABLE_COMMENT, "", *rows(cells)])


def all_styles_block(lang_code: str, lang: dict[str, str], data: dict[str, Any], styles: dict[str, dict[str, Any]]) -> str:
    groups = series_groups(data)
    if lang_code != "en":
        groups = groups[:LATEST_COUNT]
    cells = []
    for members in groups:
        slug = members[0]["slug"]
        name = styles[slug]["style_name"]
        summary = members[0].get("summary_i18n", {}).get(lang_code, members[0]["summary"])
        lines = [
            '<td width="33%" valign="top">',
            *(f'<a id="{entry["slug"]}"></a>' for entry in members),
            f'<a href="styles/{slug}"><img src="assets/thumbs/{slug}-16x9.jpg" alt="{name} preview"></a>',
            f'<p><strong><a href="styles/{slug}">{name}</a></strong><br>',
            f"<em>{summary}</em><br>",
            f'<a href="styles/{slug}/style.json">style.json</a>'
            f' · <a href="docs/copy-prompts/{slug}.md">prompt</a>'
            f' · <a href="styles/{slug}/preview-9x16.jpg">9:16</a></p>',
        ]
        if len(members) > 1:
            parts = " · ".join(f'<a href="styles/{entry["slug"]}">{part_label(entry["slug"])}</a>' for entry in members[1:])
            lines.append(f'<p>{lang["series"]}{parts}</p>')
        lines.append("</td>")
        cells.append("\n".join(lines))
    count = len(data["styles"])
    if lang_code == "en":
        intro = lang["all_intro"].format(count=count)
    else:
        intro = lang["latest_intro"].format(count=count, latest=len(groups), gallery=GALLERY_URL)
    return "\n".join([intro, "", TABLE_COMMENT, "", *rows(cells)])


def replace_region(text: str, name: str, body: str, path: Path) -> str:
    pattern = re.compile(
        rf"(<!-- BEGIN GENERATED: {name} [^\n]*-->\n).*?(\n<!-- END GENERATED: {name} -->)",
        re.DOTALL,
    )
    if not pattern.search(text):
        fail(f"{path.name} is missing the BEGIN/END GENERATED: {name} markers")
    return pattern.sub(lambda m: m.group(1) + body + m.group(2), text, count=1)


def write_readmes(data: dict[str, Any], styles: dict[str, dict[str, Any]]) -> None:
    count = len(data["styles"])
    for code, lang in LANGS.items():
        path = ROOT / lang["file"]
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"(badge/styles-)\d+(-)", rf"\g<1>{count}\2", text)
        text = re.sub(r"(badge/previews-)\d+(-)", rf"\g<1>{count * 2}\2", text)
        text = replace_region(text, "featured", featured_block(lang, data, styles), path)
        text = replace_region(text, "all-styles", all_styles_block(code, lang, data, styles), path)
        path.write_text(text, encoding="utf-8")


def catalog_entry(slug: str, styles: dict[str, dict[str, Any]], heading: str) -> list[str]:
    name = styles[slug]["style_name"]
    return [
        f"{heading} {name}",
        "",
        f'<a href="../styles/{slug}"><img src="../assets/thumbs/{slug}-16x9.jpg" width="720" alt="{name} preview"></a>',
        "",
        styles[slug]["style_summary"],
        "",
        f"Files: [style.json](../styles/{slug}/style.json)"
        f" · [Copy Prompt](copy-prompts/{slug}.md)"
        f" · [16:9 preview](../styles/{slug}/preview-16x9.jpg)"
        f" · [9:16 preview](../styles/{slug}/preview-9x16.jpg)"
        f" · [Folder](../styles/{slug})",
        "",
    ]


def write_catalog(data: dict[str, Any], styles: dict[str, dict[str, Any]]) -> None:
    lines = [
        "# Style Catalog — Full Details",
        "",
        f"Complete descriptions and all file links for each of the {len(data['styles'])} styles."
        " Parts of a series are collapsed under the first style of the series."
        " For a visual gallery, see the [main README](../README.md#all-styles).",
        "",
        "[← Back to README](../README.md)",
        "",
    ]
    for members in series_groups(data):
        lines += catalog_entry(members[0]["slug"], styles, "###")
        if len(members) > 1:
            lines += [
                "<details>",
                f"<summary>{len(members) - 1} more in this series: "
                + ", ".join(part_label(entry["slug"]) for entry in members[1:])
                + "</summary>",
                "",
            ]
            for entry in members[1:]:
                lines += catalog_entry(entry["slug"], styles, "####")
            lines += ["</details>", ""]
        lines += ["---", ""]
    lines.append("[← Back to README](../README.md)")
    CATALOG_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    styles = load_styles()
    data = load_catalog(styles)
    write_readmes(data, styles)
    write_catalog(data, styles)
    print(f"PASS: wrote {len(LANGS)} READMEs and docs/CATALOG.md with {len(data['styles'])} styles")


if __name__ == "__main__":
    main()
