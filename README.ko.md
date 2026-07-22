<h1 align="center">AI Visual Prompt Cookbook</h1>

<p align="center">
  <img src="assets/hero-collage.jpg" alt="AI Visual Prompt Cookbook showcase">
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.zh-TW.md">繁體中文</a> |
  <a href="README.ja.md">日本語</a> |
  한국어 |
  <a href="README.id.md">Bahasa Indonesia</a>
</p>

<p align="center">
  <img alt="Styles" src="https://img.shields.io/badge/styles-100-ff5a7a?style=flat-square">
  <img alt="Previews" src="https://img.shields.io/badge/previews-200-4cc9f0?style=flat-square">
  <img alt="Format" src="https://img.shields.io/badge/format-style.json-111111?style=flat-square">
  <img alt="Languages" src="https://img.shields.io/badge/languages-6-f7b801?style=flat-square">
</p>

<p align="center">
  <strong>JSON 하나를 복사하면 하나의 스타일을 얻을 수 있습니다.</strong> <code>style.json</code> 을 ChatGPT, Claude, Nano Banana Pro 또는 원하는 LLM 이미지 워크플로에 넣고 변수만 바꾸면 시각 시스템을 유지할 수 있습니다.
</p>

<p align="center">
  AI 이미지 생성을 위한 재사용 가능한 비주얼 프롬프트 스타일 라이브러리입니다. 각 스타일은 바로 쓸 수 있는 <code>style.json</code> 과 가로/세로 미리보기 이미지로 정리되어 있습니다.
</p>

<p align="center">
  Curated by <a href="https://x.com/VigoCreativeAI">@VigoCreativeAI</a>, structured with assistance from OpenAI Codex. 새 스타일 업데이트를 보려면 이 저장소를 Star 해 주세요.
</p>

<p align="center">
  🖼️ <strong><a href="https://vigozhao.github.io/AI-Visual-Prompt-Cookbook/site/">온라인 갤러리</a></strong> · 또는 아래 <a href="#all-styles">All Styles 갤러리</a> / <a href="docs/CATALOG.md">전체 카탈로그</a>를 확인하세요.
</p>

## 빠른 링크

| 카테고리 | 적합한 용도 | 먼저 볼 스타일 |
| --- | --- | --- |
| 사진 + 드로잉 | 소셜 스냅, 라이프스타일 장면, 장난스러운 스티커 오버레이 | [Playful Mascot Doodle Snapshot](#playful-mascot-doodle-snapshot-style), [Subway Doodle Photo Hybrid](#subway-doodle-photo-hybrid-style) |
| Zine + 콜라주 | 패션 포스터, 음악 비주얼, 맥시멀 에디토리얼 레이아웃 | [K-pop Apocalypse Ransom Zine](#k-pop-apocalypse-ransom-zine-style), [Y2K Grunge Hip-hop Cutout Poster](#y2k-grunge-hiphop-cutout-poster-style) |
| 타이포그래피 포스터 | 큰 헤드라인, 강한 캠페인 그래픽, 시각적 임팩트 | [Impact Burst Halftone Comic Poster](#impact-burst-halftone-comic-poster-style), [Neon Kinetic Typographic Poster](#neon-kinetic-typographic-poster-style) |
| 여행 + 도시 | 여행지 포스터, 거리 장면, 도시 비주얼 다이어리 | [Clean Triptych Travel Vlog Thumbnail](#clean-triptych-travel-vlog-thumbnail-style), [Tokyo Kawaii Travel Collage Poster](#tokyo-kawaii-travel-collage-poster-style) |
| 에디토리얼 + 미니멀 | 깔끔한 구성, 구조적인 레이아웃, 차분한 아트 디렉션 | [Tri Color Hardcut Portrait Poster](#tri-color-hardcut-portrait-poster-style), [Soft Analog Future Editorial Poster](#soft-analog-future-editorial-poster-style) |

## 이 프로젝트를 만든 이유

대부분의 AI 이미지 프롬프트는 한 번 쓰고 버리는 텍스트 덩어리라 재사용, 비교, 반복 개선이 어렵습니다. 이 저장소는 각 비주얼 스타일을 구조화된 `style.json` 으로 분해합니다. 주제는 바꿔도 스타일 구조는 유지할 수 있습니다.

## 빠른 시작

1. [추천 스타일](#추천-스타일), [빠른 링크](#빠른-링크), [All Styles](#all-styles)를 둘러봅니다.
2. 원하는 스타일 폴더를 열고 `style.json` 을 복사합니다.
3. 전체 JSON 을 ChatGPT Images 2, Nano Banana Pro 또는 다른 엔드투엔드 멀티모달 이미지 모델에 붙여 넣습니다.
4. `environment_variables` 에 선언된 변수에 값을 지정하거나 `examples[*].values` 의 사례 값을 수정합니다.
5. 최종 이미지를 생성합니다.

전체 입력에서 출력까지의 흐름은 아래 [Complete Example](#complete-example)을 참고하세요.

### Recommended Image Models

이 워크플로는 긴 구조화 JSON 프롬프트를 읽고 최종 이미지를 한 번에 생성할 수 있는 엔드투엔드 멀티모달 이미지 모델에서 가장 잘 작동합니다.

- ChatGPT Images 2 (OpenAI, gpt-image-2) — 텍스트 렌더링이 강하고 2K/4K 출력을 지원하며 생성 전 추론이 가능
- Nano Banana Pro (Google, Gemini 3 Pro Image) — 4K 출력, 다국어 텍스트 정확도, 강한 주체 일관성

긴 JSON 프롬프트를 받을 수 있는 다른 멀티모달 LLM 도 동작할 수 있지만, 주 추천 대상은 아닙니다.

## Complete Example

### 입력 → 출력 워크스루

이 예시는 [Mono Noir Type Portrait Poster Style](styles/mono-noir-type-portrait-poster-style/)을 사용합니다.

#### Step 1 — The Style

<details>
<summary>prompt_template excerpt</summary>

```text
Create a {ASPECT_RATIO} monochrome editorial poster in the Mono Noir Type Portrait Poster Style. Style fidelity lock: {STYLE_FIDELITY_ANCHORS}. Source content to avoid: {SOURCE_CONTENT_TO_AVOID}. Scene: {SUBJECT} {SUBJECT_ACTION} with {PRODUCT_OR_PROP} in {LOCATION}. Background elements: {BACKGROUND_ELEMENTS}. Wardrobe and styling: {WARDROBE_STYLE}. Composition: one large high-contrast black-and-white photographic subject, close crop, deep charcoal background, sparse negative space, shallow depth of field, serious noir editorial mood. If the aspect ratio is 16:9, make a landscape poster with the subject weighted to the right side and the headline block on the left. If the aspect ratio is 9:16, make a vertical poster with the headline stacked in the upper-left or middle-left field and the subject cropped large on the right or lower-right. Typography: render the exact readable lowercase headline text "{MAIN_TEXT}" as three short left-aligned lines...
```

</details>

#### Step 2 — Your Variables

```text
SUBJECT = a tired architect with silver hair
SUBJECT_ACTION = studying a folded blueprint in a late-night pause
PRODUCT_OR_PROP = a rolled plan tube and a pencil held low
LOCATION = a dim concrete studio after midnight
BACKGROUND_ELEMENTS = soft charcoal wall gradient, blurred drafting table edge, deep empty space
MAIN_TEXT = focus / outlasts / noise.
SECONDARY_TEXT = studio log 02:14
ACCENT_SYMBOL = a tiny white plus
WARDROBE_STYLE = dark work jacket over a plain black shirt
ASPECT_RATIO = 16:9
```

#### Step 3 — The Final Prompt

```text
Create a 16:9 monochrome editorial poster in the Mono Noir Type Portrait Poster Style. Style fidelity lock: black-and-white photographic portrait, deep charcoal background, giant lowercase left-aligned headline, first word in a white label, remaining words in white, high contrast, sparse negative space, close crop. Source content to avoid: no young woman with blunt bangs, no freckles close-up, no discipline beats procrastination text, no copied face or exact source crop. Scene: a tired architect with silver hair studying a folded blueprint in a late-night pause with a rolled plan tube and a pencil held low in a dim concrete studio after midnight. Background elements: soft charcoal wall gradient, blurred drafting table edge, deep empty space. Wardrobe and styling: dark work jacket over a plain black shirt. Composition: one large high-contrast black-and-white photographic subject, close crop, deep charcoal background, sparse negative space, shallow depth of field, serious noir editorial mood. If the aspect ratio is 16:9, make a landscape poster with the subject weighted to the right side and the headline block on the left. If the aspect ratio is 9:16, make a vertical poster with the headline stacked in the upper-left or middle-left field and the subject cropped large on the right or lower-right. Typography: render the exact readable lowercase headline text "focus
outlasts
noise." as three short left-aligned lines with tight leading; put the first headline word as black type inside a crisp white rectangular label, then set the remaining lines in heavy white type directly on the dark background. Add "studio log 02:14" only as tiny unobtrusive white microcopy if it fits. Use a tiny white plus only as a minimal typographic mark. Keep type sharp, flat, square-cornered, and massive. Photo treatment: realistic black-and-white studio photography, strong shadow falloff, visible facial or fabric texture, subtle grain, no color, no illustration, no collage, no extra panels, no logos, no watermark.
```

#### Step 4 — The Result

<img src="assets/thumbs/mono-noir-type-portrait-poster-style-16x9.jpg" alt="Mono Noir Type Portrait Poster Style result preview">

## Copy Prompt Library

짧은 버전부터 먼저 써 보고 싶다면 자동 생성된 [Copy Prompt Library](docs/copy-prompts/README.md) 를 열면 됩니다. 각 스타일마다 바로 복사해 쓸 수 있는 간단한 프롬프트가 있습니다. 전체 재사용 스타일 시스템은 계속 각 `style.json` 에 있습니다.

## 추천 스타일

이 6개 스타일로 시작하면 라이브러리의 범위를 빠르게 이해할 수 있습니다. 모든 스타일은 JSON 하나와 미리보기 이미지 두 장으로 구성됩니다. 전체 100개는 아래 [All Styles](#all-styles) 갤러리에서 볼 수 있습니다.

<!-- HTML table used for rich image+link cells -->

<table>
<tr>
<td width="33%" valign="top">
<a href="styles/cyan-grain-macro-megatype-poster-style"><img src="assets/thumbs/cyan-grain-macro-megatype-poster-style-16x9.jpg" alt="Cyan Grain Macro Megatype Poster preview"></a>
<h3>Cyan Grain Macro Megatype Poster</h3>
<p>A sparse experimental editorial poster system built from one radically enlarged macro photograph, a saturated cyan field, monumental white geometric letterforms that interlock with the subject, wide white margins, compact technical metadata, and tactile analog print grain.</p>
<p><a href="styles/cyan-grain-macro-megatype-poster-style/style.json"><strong>style.json 열기</strong></a> · <a href="docs/copy-prompts/cyan-grain-macro-megatype-poster-style.md">프롬프트 복사</a> · <a href="styles/cyan-grain-macro-megatype-poster-style">폴더</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/retro-future-chrome-portrait-dossier"><img src="assets/thumbs/retro-future-chrome-portrait-dossier-16x9.jpg" alt="Retro Future Chrome Portrait Dossier preview"></a>
<h3>Retro Future Chrome Portrait Dossier</h3>
<p>A retro-futurist editorial portrait system built from an asymmetric technical dossier sidebar, an edge-cropped posterized face, liquid-chrome interruptions, modular grid lines, optical diagrams, and coarse halftone print grain in midnight indigo, warm cream, hot magenta, cobalt, and coral.</p>
<p><a href="styles/retro-future-chrome-portrait-dossier/style.json"><strong>style.json 열기</strong></a> · <a href="docs/copy-prompts/retro-future-chrome-portrait-dossier.md">프롬프트 복사</a> · <a href="styles/retro-future-chrome-portrait-dossier">폴더</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/pink-anime-motorcycle-spec-poster-style"><img src="assets/thumbs/pink-anime-motorcycle-spec-poster-style-16x9.jpg" alt="Pink Anime Motorcycle Spec Poster Style preview"></a>
<h3>Pink Anime Motorcycle Spec Poster Style</h3>
<p>A dense anime motorsport dossier poster system pairing one original cel-shaded rider with one hero motorcycle, built from a glossy three-quarter product view, oversized italic model-code typography, a cream-and-hot-magenta editorial grid, a monochrome halftone character echo, and a compact technical spec card.</p>
<p><a href="styles/pink-anime-motorcycle-spec-poster-style/style.json"><strong>style.json 열기</strong></a> · <a href="docs/copy-prompts/pink-anime-motorcycle-spec-poster-style.md">프롬프트 복사</a> · <a href="styles/pink-anime-motorcycle-spec-poster-style">폴더</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a href="styles/xerox-neon-editorial-collage-style"><img src="assets/thumbs/xerox-neon-editorial-collage-style-16x9.jpg" alt="Xerox Neon Editorial Collage preview"></a>
<h3>Xerox Neon Editorial Collage</h3>
<p>A high-impact editorial poster system combining an oversized distressed black headline, one monochrome halftone photo cutout, electric cyan and green registration shadows, horizontal fluorescent paint swashes, loose marker scribbles, and a pale photocopied paper field.</p>
<p><a href="styles/xerox-neon-editorial-collage-style/style.json"><strong>style.json 열기</strong></a> · <a href="docs/copy-prompts/xerox-neon-editorial-collage-style.md">프롬프트 복사</a> · <a href="styles/xerox-neon-editorial-collage-style">폴더</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/crimson-ink-manga-dossier"><img src="assets/thumbs/crimson-ink-manga-dossier-16x9.jpg" alt="Crimson Ink Manga Dossier preview"></a>
<h3>Crimson Ink Manga Dossier</h3>
<p>A high-density manga editorial dossier poster built from one dramatically foreshortened illustrated hero, oversized distressed condensed headlines, modular newspaper sidebars, monochrome comic insets, and a strict crimson-black-warm-paper palette.</p>
<p><a href="styles/crimson-ink-manga-dossier/style.json"><strong>style.json 열기</strong></a> · <a href="docs/copy-prompts/crimson-ink-manga-dossier.md">프롬프트 복사</a> · <a href="styles/crimson-ink-manga-dossier">폴더</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/lime-loop-megatype-action-poster-style"><img src="assets/thumbs/lime-loop-megatype-action-poster-style-16x9.jpg" alt="Lime Loop Megatype Action Poster preview"></a>
<h3>Lime Loop Megatype Action Poster</h3>
<p>A high-energy studio action-poster system combining an overhead wide-angle photographic subject, enormous stacked dark-green display type, a continuous fluorescent-lime motion loop, clean white negative space, and crisp commercial lighting.</p>
<p><a href="styles/lime-loop-megatype-action-poster-style/style.json"><strong>style.json 열기</strong></a> · <a href="docs/copy-prompts/lime-loop-megatype-action-poster-style.md">프롬프트 복사</a> · <a href="styles/lime-loop-megatype-action-poster-style">폴더</a></p>
</td>
</tr>
</table>

## 패키지 구조

```text
styles/<style-slug>/
  style.json          # 기계가 읽을 수 있는 프롬프트 스타일 템플릿
  preview-16x9.jpg    # 가로 미리보기
  preview-9x16.jpg    # 세로 미리보기
```

## style.json v2.1

각 `style.json` 은 자체 완결형입니다. 파일 전체를 LLM 에 복사한 뒤 `environment_variables` 에 선언된 변수에 값을 지정하거나 `examples[*].values` 의 사례 값을 수정하면 됩니다.

- `prompt_template` 은 `{VARIABLE}` 플레이스홀더가 있는 재사용 가능한 스타일 프롬프트입니다.
- `environment_variables` 는 템플릿에서 사용할 수 있는 모든 변수를 선언합니다.
- `examples` 는 바로 수정할 수 있는 사례이며, 각 사례는 `case_name` 과 `values` 만 저장합니다.
- `style_fidelity_anchors` 와 `source_content_to_avoid` 는 유지해야 할 스타일 요소와 복사하면 안 되는 원본 요소를 구분합니다.
- `negative_prompt` 는 워터마크, 로고, 원본 직접 재현, 스타일 이탈을 줄입니다.

`prompt_9x16`, `prompt_16x9`, `full_prompt` 같은 렌더링된 전체 프롬프트는 저장하지 않습니다. 생성 시점에 `prompt_template` 과 선택한 값으로 만들기 때문에 JSON 이 가볍고 오래 유지됩니다.

검증 명령:

```bash
python3 scripts/validate-style-json.py .
```

## All Styles

아래에서 전체 100개 스타일을 둘러볼 수 있습니다.

위 추천 스타일을 포함한 전체 라이브러리입니다. 각 스타일의 전체 설명과 모든 파일 링크는 [docs/CATALOG.md](docs/CATALOG.md)를 참고하세요.

<!-- HTML table used for rich image+link cells -->

<table>
<tr>
<td width="33%" valign="top">
<a id="cyan-grain-macro-megatype-poster-style"></a>
<a href="styles/cyan-grain-macro-megatype-poster-style"><img src="assets/thumbs/cyan-grain-macro-megatype-poster-style-16x9.jpg" alt="Cyan Grain Macro Megatype Poster preview"></a>
<p><strong><a href="styles/cyan-grain-macro-megatype-poster-style">Cyan Grain Macro Megatype Poster</a></strong><br>
<em>Sparse experimental posters built from one radically enlarged macro photograph, a saturated cyan field, monumental interlocking white letterforms, and tactile analog print grain.</em><br>
<a href="styles/cyan-grain-macro-megatype-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/cyan-grain-macro-megatype-poster-style.md">prompt</a> · <a href="styles/cyan-grain-macro-megatype-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="retro-future-chrome-portrait-dossier"></a>
<a href="styles/retro-future-chrome-portrait-dossier"><img src="assets/thumbs/retro-future-chrome-portrait-dossier-16x9.jpg" alt="Retro Future Chrome Portrait Dossier preview"></a>
<p><strong><a href="styles/retro-future-chrome-portrait-dossier">Retro Future Chrome Portrait Dossier</a></strong><br>
<em>Retro-futurist editorial portrait posters with a technical dossier sidebar, an edge-cropped posterized face, liquid-chrome interruptions, optical diagrams, and coarse halftone print grain.</em><br>
<a href="styles/retro-future-chrome-portrait-dossier/style.json">style.json</a> · <a href="docs/copy-prompts/retro-future-chrome-portrait-dossier.md">prompt</a> · <a href="styles/retro-future-chrome-portrait-dossier/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="pink-anime-motorcycle-spec-poster-style"></a>
<a href="styles/pink-anime-motorcycle-spec-poster-style"><img src="assets/thumbs/pink-anime-motorcycle-spec-poster-style-16x9.jpg" alt="Pink Anime Motorcycle Spec Poster Style preview"></a>
<p><strong><a href="styles/pink-anime-motorcycle-spec-poster-style">Pink Anime Motorcycle Spec Poster Style</a></strong><br>
<em>Anime motorsport dossier posters pairing an original rider with a hero motorcycle, oversized italic model codes, a cream-and-magenta editorial grid, and a compact spec card.</em><br>
<a href="styles/pink-anime-motorcycle-spec-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/pink-anime-motorcycle-spec-poster-style.md">prompt</a> · <a href="styles/pink-anime-motorcycle-spec-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="xerox-neon-editorial-collage-style"></a>
<a href="styles/xerox-neon-editorial-collage-style"><img src="assets/thumbs/xerox-neon-editorial-collage-style-16x9.jpg" alt="Xerox Neon Editorial Collage preview"></a>
<p><strong><a href="styles/xerox-neon-editorial-collage-style">Xerox Neon Editorial Collage</a></strong><br>
<em>Photocopied editorial collage posters with a distressed black headline, a halftone photo cutout, cyan-green misregistration, fluorescent paint swashes, and marker scribbles.</em><br>
<a href="styles/xerox-neon-editorial-collage-style/style.json">style.json</a> · <a href="docs/copy-prompts/xerox-neon-editorial-collage-style.md">prompt</a> · <a href="styles/xerox-neon-editorial-collage-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="crimson-ink-manga-dossier"></a>
<a href="styles/crimson-ink-manga-dossier"><img src="assets/thumbs/crimson-ink-manga-dossier-16x9.jpg" alt="Crimson Ink Manga Dossier preview"></a>
<p><strong><a href="styles/crimson-ink-manga-dossier">Crimson Ink Manga Dossier</a></strong><br>
<em>High-density manga dossier posters with a foreshortened hero, distressed condensed headlines, newspaper sidebars, and a crimson-black-paper palette.</em><br>
<a href="styles/crimson-ink-manga-dossier/style.json">style.json</a> · <a href="docs/copy-prompts/crimson-ink-manga-dossier.md">prompt</a> · <a href="styles/crimson-ink-manga-dossier/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="lime-loop-megatype-action-poster-style"></a>
<a href="styles/lime-loop-megatype-action-poster-style"><img src="assets/thumbs/lime-loop-megatype-action-poster-style-16x9.jpg" alt="Lime Loop Megatype Action Poster preview"></a>
<p><strong><a href="styles/lime-loop-megatype-action-poster-style">Lime Loop Megatype Action Poster</a></strong><br>
<em>Studio action posters with an overhead subject, stacked dark-green megatype, a fluorescent-lime motion loop, and clean white space.</em><br>
<a href="styles/lime-loop-megatype-action-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/lime-loop-megatype-action-poster-style.md">prompt</a> · <a href="styles/lime-loop-megatype-action-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="yellow-graffiti-fisheye-manga-street-poster-style"></a>
<a href="styles/yellow-graffiti-fisheye-manga-street-poster-style"><img src="assets/thumbs/yellow-graffiti-fisheye-manga-street-poster-style-16x9.jpg" alt="Yellow Graffiti Fisheye Manga Street Poster Style preview"></a>
<p><strong><a href="styles/yellow-graffiti-fisheye-manga-street-poster-style">Yellow Graffiti Fisheye Manga Street Poster Style</a></strong><br>
<em>Fisheye street posters mixing manga ink cutouts, sprayed yellow graffiti type, pavement tag texture, and anxious character energy.</em><br>
<a href="styles/yellow-graffiti-fisheye-manga-street-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/yellow-graffiti-fisheye-manga-street-poster-style.md">prompt</a> · <a href="styles/yellow-graffiti-fisheye-manga-street-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="red-yellow-product-trophy-collage-style"></a>
<a href="styles/red-yellow-product-trophy-collage-style"><img src="assets/thumbs/red-yellow-product-trophy-collage-style-16x9.jpg" alt="Red Yellow Product Trophy Collage Style preview"></a>
<p><strong><a href="styles/red-yellow-product-trophy-collage-style">Red Yellow Product Trophy Collage Style</a></strong><br>
<em>Fast-food billboard collages with red-and-yellow blocks, glossy cutout products, and a trophy silhouette built from product objects.</em><br>
<a href="styles/red-yellow-product-trophy-collage-style/style.json">style.json</a> · <a href="docs/copy-prompts/red-yellow-product-trophy-collage-style.md">prompt</a> · <a href="styles/red-yellow-product-trophy-collage-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="manga-dossier-blueprint-poster"></a>
<a href="styles/manga-dossier-blueprint-poster"><img src="assets/thumbs/manga-dossier-blueprint-poster-16x9.jpg" alt="Manga Dossier Blueprint Poster preview"></a>
<p><strong><a href="styles/manga-dossier-blueprint-poster">Manga Dossier Blueprint Poster</a></strong><br>
<em>Manga dossier posters with cream margins, grayscale ink portraits, cobalt-blue technical panels, and editorial annotation rails.</em><br>
<a href="styles/manga-dossier-blueprint-poster/style.json">style.json</a> · <a href="docs/copy-prompts/manga-dossier-blueprint-poster.md">prompt</a> · <a href="styles/manga-dossier-blueprint-poster/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="red-black-manga-tabloid-poster-style"></a>
<a href="styles/red-black-manga-tabloid-poster-style"><img src="assets/thumbs/red-black-manga-tabloid-poster-style-16x9.jpg" alt="Red Black Manga Tabloid Poster Style preview"></a>
<p><strong><a href="styles/red-black-manga-tabloid-poster-style">Red Black Manga Tabloid Poster Style</a></strong><br>
<em>Dense red-black manga tabloids with cropped ink characters, editorial metadata blocks, halftone shading, and photocopy paper texture.</em><br>
<a href="styles/red-black-manga-tabloid-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/red-black-manga-tabloid-poster-style.md">prompt</a> · <a href="styles/red-black-manga-tabloid-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="ice-cyan-megatype-action-poster-style"></a>
<a href="styles/ice-cyan-megatype-action-poster-style"><img src="assets/thumbs/ice-cyan-megatype-action-poster-style-16x9.jpg" alt="Ice Cyan Megatype Action Poster Style preview"></a>
<p><strong><a href="styles/ice-cyan-megatype-action-poster-style">Ice Cyan Megatype Action Poster Style</a></strong><br>
<em>Ice-white action posters with oversized cyan megatype, ghost text layers, a cutout action photo, and chartreuse motion blur.</em><br>
<a href="styles/ice-cyan-megatype-action-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/ice-cyan-megatype-action-poster-style.md">prompt</a> · <a href="styles/ice-cyan-megatype-action-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="scarlet-megatype-action-collage-style"></a>
<a href="styles/scarlet-megatype-action-collage-style"><img src="assets/thumbs/scarlet-megatype-action-collage-style-16x9.jpg" alt="Scarlet Megatype Action Collage Style preview"></a>
<p><strong><a href="styles/scarlet-megatype-action-collage-style">Scarlet Megatype Action Collage Style</a></strong><br>
<em>Scarlet action key-art with diagonal block megatype, layered cutout subjects, hard graphic shadows, and controlled print grain.</em><br>
<a href="styles/scarlet-megatype-action-collage-style/style.json">style.json</a> · <a href="docs/copy-prompts/scarlet-megatype-action-collage-style.md">prompt</a> · <a href="styles/scarlet-megatype-action-collage-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="jagged-red-street-photo-event-poster-style"></a>
<a href="styles/jagged-red-street-photo-event-poster-style"><img src="assets/thumbs/jagged-red-street-photo-event-poster-style-16x9.jpg" alt="Jagged Red Street Photo Event Poster Style preview"></a>
<p><strong><a href="styles/jagged-red-street-photo-event-poster-style">Jagged Red Street Photo Event Poster Style</a></strong><br>
<em>High-impact street posters with black-and-white photo cores, jagged red-and-black display type, thick white gutters, and three-color print energy.</em><br>
<a href="styles/jagged-red-street-photo-event-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/jagged-red-street-photo-event-poster-style.md">prompt</a> · <a href="styles/jagged-red-street-photo-event-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="neon-stadium-3d-hero-type-poster-style"></a>
<a href="styles/neon-stadium-3d-hero-type-poster-style"><img src="assets/thumbs/neon-stadium-3d-hero-type-poster-style-16x9.jpg" alt="Neon Stadium 3D Hero Type Poster Style preview"></a>
<p><strong><a href="styles/neon-stadium-3d-hero-type-poster-style">Neon Stadium 3D Hero Type Poster Style</a></strong><br>
<em>Hyper-saturated 3D stadium posters with toy-like heroes, cropped condensed type, lime-and-purple fields, and motion-blurred debris.</em><br>
<a href="styles/neon-stadium-3d-hero-type-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/neon-stadium-3d-hero-type-poster-style.md">prompt</a> · <a href="styles/neon-stadium-3d-hero-type-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="dusk-cyan-layered-type-poster-style"></a>
<a href="styles/dusk-cyan-layered-type-poster-style"><img src="assets/thumbs/dusk-cyan-layered-type-poster-style-16x9.jpg" alt="Dusk Cyan Layered Type Poster Style preview"></a>
<p><strong><a href="styles/dusk-cyan-layered-type-poster-style">Dusk Cyan Layered Type Poster Style</a></strong><br>
<em>Full-bleed dusk photo posters with navy silhouettes, oversized cyan-and-white type, script swashes, and crisp vector icons.</em><br>
<a href="styles/dusk-cyan-layered-type-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/dusk-cyan-layered-type-poster-style.md">prompt</a> · <a href="styles/dusk-cyan-layered-type-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="electric-blue-cutout-manga-poster-style"></a>
<a href="styles/electric-blue-cutout-manga-poster-style"><img src="assets/thumbs/electric-blue-cutout-manga-poster-style-16x9.jpg" alt="Electric Blue Cutout Manga Poster Style preview"></a>
<p><strong><a href="styles/electric-blue-cutout-manga-poster-style">Electric Blue Cutout Manga Poster Style</a></strong><br>
<em>Electric-blue manga posters with white cutout geometry, rounded modular type, orange microtype, and a cel-shaded subject in exaggerated perspective.</em><br>
<a href="styles/electric-blue-cutout-manga-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/electric-blue-cutout-manga-poster-style.md">prompt</a> · <a href="styles/electric-blue-cutout-manga-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="y2k-streetwear-sticker-collage-style"></a>
<a href="styles/y2k-streetwear-sticker-collage-style"><img src="assets/thumbs/y2k-streetwear-sticker-collage-style-16x9.jpg" alt="Y2K Streetwear Sticker Collage Style preview"></a>
<p><strong><a href="styles/y2k-streetwear-sticker-collage-style">Y2K Streetwear Sticker Collage Style</a></strong><br>
<em>Dense Y2K street collages with cutout subjects, sticker props, comic typography, and saturated yellow-blue-green accents.</em><br>
<a href="styles/y2k-streetwear-sticker-collage-style/style.json">style.json</a> · <a href="docs/copy-prompts/y2k-streetwear-sticker-collage-style.md">prompt</a> · <a href="styles/y2k-streetwear-sticker-collage-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="cream-smoke-city-manga-poster-style"></a>
<a href="styles/cream-smoke-city-manga-poster-style"><img src="assets/thumbs/cream-smoke-city-manga-poster-style-16x9.jpg" alt="Cream Smoke City Manga Poster Style preview"></a>
<p><strong><a href="styles/cream-smoke-city-manga-poster-style">Cream Smoke City Manga Poster Style</a></strong><br>
<em>Manga ink city scenes with cream cloud masses, sparse teal frames, peach accents, and precise miniature urban architecture.</em><br>
<a href="styles/cream-smoke-city-manga-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/cream-smoke-city-manga-poster-style.md">prompt</a> · <a href="styles/cream-smoke-city-manga-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="red-yellow-grunge-skate-cover-style"></a>
<a href="styles/red-yellow-grunge-skate-cover-style"><img src="assets/thumbs/red-yellow-grunge-skate-cover-style-16x9.jpg" alt="Red Yellow Grunge Skate Cover Style preview"></a>
<p><strong><a href="styles/red-yellow-grunge-skate-cover-style">Red Yellow Grunge Skate Cover Style</a></strong><br>
<em>Raw red-and-yellow action-culture covers with flash-lit cutouts, warped headline type, boxed callouts, and analog print grit.</em><br>
<a href="styles/red-yellow-grunge-skate-cover-style/style.json">style.json</a> · <a href="docs/copy-prompts/red-yellow-grunge-skate-cover-style.md">prompt</a> · <a href="styles/red-yellow-grunge-skate-cover-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="monochrome-xerox-sports-dossier"></a>
<a href="styles/monochrome-xerox-sports-dossier"><img src="assets/thumbs/monochrome-xerox-sports-dossier-16x9.jpg" alt="Monochrome Xerox Sports Dossier preview"></a>
<p><strong><a href="styles/monochrome-xerox-sports-dossier">Monochrome Xerox Sports Dossier</a></strong><br>
<em>Black-and-white xerox sports dossiers with cropped subjects, inset photo panels, distressed condensed type, and press-kit grain.</em><br>
<a href="styles/monochrome-xerox-sports-dossier/style.json">style.json</a> · <a href="docs/copy-prompts/monochrome-xerox-sports-dossier.md">prompt</a> · <a href="styles/monochrome-xerox-sports-dossier/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="liquid-chrome-clearance-poster-style"></a>
<a href="styles/liquid-chrome-clearance-poster-style"><img src="assets/thumbs/liquid-chrome-clearance-poster-style-16x9.jpg" alt="Liquid Chrome Clearance Poster Style preview"></a>
<p><strong><a href="styles/liquid-chrome-clearance-poster-style">Liquid Chrome Clearance Poster Style</a></strong><br>
<em>High-impact clearance posters with glossy liquid-chrome 3D type, acid-lime gradients, sale-interface microcopy, and barcode-style retail panels.</em><br>
<a href="styles/liquid-chrome-clearance-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/liquid-chrome-clearance-poster-style.md">prompt</a> · <a href="styles/liquid-chrome-clearance-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="hot-ink-comic-poster"></a>
<a href="styles/hot-ink-comic-poster"><img src="assets/thumbs/hot-ink-comic-poster-16x9.jpg" alt="Hot Ink Comic Poster preview"></a>
<p><strong><a href="styles/hot-ink-comic-poster">Hot Ink Comic Poster</a></strong><br>
<em>Loud underground comic flyers with mustard fields, coral cutouts, heavy marker outlines, hand-lettered bubble type, and dense comic symbols.</em><br>
<a href="styles/hot-ink-comic-poster/style.json">style.json</a> · <a href="docs/copy-prompts/hot-ink-comic-poster.md">prompt</a> · <a href="styles/hot-ink-comic-poster/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="kinetic-editorial-photo-collage-style"></a>
<a href="styles/kinetic-editorial-photo-collage-style"><img src="assets/thumbs/kinetic-editorial-photo-collage-style-16x9.jpg" alt="Kinetic Editorial Photo Collage preview"></a>
<p><strong><a href="styles/kinetic-editorial-photo-collage-style">Kinetic Editorial Photo Collage</a></strong><br>
<em>High-energy action posters built from staggered photo tiles, a cutout motion subject, bold black condensed type, loose ink speed marks, and sparse line-art scaffolding.</em><br>
<a href="styles/kinetic-editorial-photo-collage-style/style.json">style.json</a> · <a href="docs/copy-prompts/kinetic-editorial-photo-collage-style.md">prompt</a> · <a href="styles/kinetic-editorial-photo-collage-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="sunlit-coastal-product-blitz"></a>
<a href="styles/sunlit-coastal-product-blitz"><img src="assets/thumbs/sunlit-coastal-product-blitz-16x9.jpg" alt="Sunlit Coastal Product Blitz preview"></a>
<p><strong><a href="styles/sunlit-coastal-product-blitz">Sunlit Coastal Product Blitz</a></strong><br>
<em>Sunlit photoreal coastal product ads with tropical botanicals, ocean-blue depth, distressed white brush type, dense label blocks, curved callouts, and gold seal badges.</em><br>
<a href="styles/sunlit-coastal-product-blitz/style.json">style.json</a> · <a href="docs/copy-prompts/sunlit-coastal-product-blitz.md">prompt</a> · <a href="styles/sunlit-coastal-product-blitz/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="monochrome-grid-sneaker-tech-spec"></a>
<a href="styles/monochrome-grid-sneaker-tech-spec"><img src="assets/thumbs/monochrome-grid-sneaker-tech-spec-16x9.jpg" alt="Monochrome Grid Sneaker Tech Spec preview"></a>
<p><strong><a href="styles/monochrome-grid-sneaker-tech-spec">Monochrome Grid Sneaker Tech Spec</a></strong><br>
<em>Black-and-white footwear tech-spec posters with an oversized sneaker hero, engineering grid, evidence panels, macro callouts, pixelated uppercase type, and coarse halftone print.</em><br>
<a href="styles/monochrome-grid-sneaker-tech-spec/style.json">style.json</a> · <a href="docs/copy-prompts/monochrome-grid-sneaker-tech-spec.md">prompt</a> · <a href="styles/monochrome-grid-sneaker-tech-spec/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="sky-blue-lucky-tag-doodle-poster-style"></a>
<a href="styles/sky-blue-lucky-tag-doodle-poster-style"><img src="assets/thumbs/sky-blue-lucky-tag-doodle-poster-style-16x9.jpg" alt="Sky Blue Lucky Tag Doodle Poster Style preview"></a>
<p><strong><a href="styles/sky-blue-lucky-tag-doodle-poster-style">Sky Blue Lucky Tag Doodle Poster Style</a></strong><br>
<em>Sky-blue doodle posters with chunky white type, a hanging lucky-tag plaque, thick black outlines, and one big playful mascot.</em><br>
<a href="styles/sky-blue-lucky-tag-doodle-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/sky-blue-lucky-tag-doodle-poster-style.md">prompt</a> · <a href="styles/sky-blue-lucky-tag-doodle-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="neon-type-photo-scribble-poster"></a>
<a href="styles/neon-type-photo-scribble-poster"><img src="assets/thumbs/neon-type-photo-scribble-poster-16x9.jpg" alt="Neon Type Photo Scribble Poster preview"></a>
<p><strong><a href="styles/neon-type-photo-scribble-poster">Neon Type Photo Scribble Poster</a></strong><br>
<em>Neon event posters with huge condensed type, documentary photo crops, and raw white scribble gestures.</em><br>
<a href="styles/neon-type-photo-scribble-poster/style.json">style.json</a> · <a href="docs/copy-prompts/neon-type-photo-scribble-poster.md">prompt</a> · <a href="styles/neon-type-photo-scribble-poster/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="loose-scribble-riso-print-style"></a>
<a href="styles/loose-scribble-riso-print-style"><img src="assets/thumbs/loose-scribble-riso-print-style-16x9.jpg" alt="Loose Scribble Riso Print Style preview"></a>
<p><strong><a href="styles/loose-scribble-riso-print-style">Loose Scribble Riso Print Style</a></strong><br>
<em>Sparse riso posters with wavering contours, overprint accents, handwritten margins, and visible paper grain.</em><br>
<a href="styles/loose-scribble-riso-print-style/style.json">style.json</a> · <a href="docs/copy-prompts/loose-scribble-riso-print-style.md">prompt</a> · <a href="styles/loose-scribble-riso-print-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="jade-glyph-grocer-collage-poster-style"></a>
<a href="styles/jade-glyph-grocer-collage-poster-style"><img src="assets/thumbs/jade-glyph-grocer-collage-poster-style-16x9.jpg" alt="Jade Glyph Grocer Collage Poster Style preview"></a>
<p><strong><a href="styles/jade-glyph-grocer-collage-poster-style">Jade Glyph Grocer Collage Poster Style</a></strong><br>
<em>Cream grocer posters with jade glyphs, vegetable silhouettes, and glossy produce-photo centerpieces.</em><br>
<a href="styles/jade-glyph-grocer-collage-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/jade-glyph-grocer-collage-poster-style.md">prompt</a> · <a href="styles/jade-glyph-grocer-collage-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="scarlet-court-photo-type-poster-style"></a>
<a href="styles/scarlet-court-photo-type-poster-style"><img src="assets/thumbs/scarlet-court-photo-type-poster-style-16x9.jpg" alt="Scarlet Court Photo Type Poster preview"></a>
<p><strong><a href="styles/scarlet-court-photo-type-poster-style">Scarlet Court Photo Type Poster</a></strong><br>
<em>Scarlet action posters with blue sports panels, cutout athletes, cream typography, and gritty print texture.</em><br>
<a href="styles/scarlet-court-photo-type-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/scarlet-court-photo-type-poster-style.md">prompt</a> · <a href="styles/scarlet-court-photo-type-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="sunlit-kinetic-block-type-photo-poster-style"></a>
<a href="styles/sunlit-kinetic-block-type-photo-poster-style"><img src="assets/thumbs/sunlit-kinetic-block-type-photo-poster-style-16x9.jpg" alt="Sunlit Kinetic Block Type Photo Poster preview"></a>
<p><strong><a href="styles/sunlit-kinetic-block-type-photo-poster-style">Sunlit Kinetic Block Type Photo Poster</a></strong><br>
<em>Sunlit sports editorials with oversized cream block type, diagonal photo crops, and bright sky fields.</em><br>
<a href="styles/sunlit-kinetic-block-type-photo-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/sunlit-kinetic-block-type-photo-poster-style.md">prompt</a> · <a href="styles/sunlit-kinetic-block-type-photo-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="scarlet-block-cutout-doodle-book-cover-style"></a>
<a href="styles/scarlet-block-cutout-doodle-book-cover-style"><img src="assets/thumbs/scarlet-block-cutout-doodle-book-cover-style-16x9.jpg" alt="Scarlet Block Cutout Doodle Book Cover Style preview"></a>
<p><strong><a href="styles/scarlet-block-cutout-doodle-book-cover-style">Scarlet Block Cutout Doodle Book Cover Style</a></strong><br>
<em>Literary white-paper covers with scarlet letterforms, central cutout objects, marker contours, and asymmetrical space.</em><br>
<a href="styles/scarlet-block-cutout-doodle-book-cover-style/style.json">style.json</a> · <a href="docs/copy-prompts/scarlet-block-cutout-doodle-book-cover-style.md">prompt</a> · <a href="styles/scarlet-block-cutout-doodle-book-cover-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="halftone-assemblage-metaphor-psa-poster-style"></a>
<a href="styles/halftone-assemblage-metaphor-psa-poster-style"><img src="assets/thumbs/halftone-assemblage-metaphor-psa-poster-style-16x9.jpg" alt="Halftone Assemblage Metaphor PSA Poster Style preview"></a>
<p><strong><a href="styles/halftone-assemblage-metaphor-psa-poster-style">Halftone Assemblage Metaphor PSA Poster Style</a></strong><br>
<em>일상 소재로 상징적 하프톤 실루엣을 만드는 낡은 종이 질감의 레트로 PSA 포스터.</em><br>
<a href="styles/halftone-assemblage-metaphor-psa-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/halftone-assemblage-metaphor-psa-poster-style.md">prompt</a> · <a href="styles/halftone-assemblage-metaphor-psa-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="school-grid-paper-cutout-poster"></a>
<a href="styles/school-grid-paper-cutout-poster"><img src="assets/thumbs/school-grid-paper-cutout-poster-16x9.jpg" alt="School Grid Paper Cutout Poster preview"></a>
<p><strong><a href="styles/school-grid-paper-cutout-poster">School Grid Paper Cutout Poster</a></strong><br>
<em>격자 종이에 찢은 종이 오브젝트, 손글씨 메모, 부드러운 그림자를 얹은 향수 어린 포스터.</em><br>
<a href="styles/school-grid-paper-cutout-poster/style.json">style.json</a> · <a href="docs/copy-prompts/school-grid-paper-cutout-poster.md">prompt</a> · <a href="styles/school-grid-paper-cutout-poster/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="naive-marker-quote-card-style"></a>
<a href="styles/naive-marker-quote-card-style"><img src="assets/thumbs/naive-marker-quote-card-style-16x9.jpg" alt="Naive Marker Quote Card Style preview"></a>
<p><strong><a href="styles/naive-marker-quote-card-style">Naive Marker Quote Card Style</a></strong><br>
<em>거친 마커 윤곽, 파스텔 패널, 파란 블록 글자, 사물 개그가 있는 부조리한 인용 카드 포스터.</em><br>
<a href="styles/naive-marker-quote-card-style/style.json">style.json</a> · <a href="docs/copy-prompts/naive-marker-quote-card-style.md">prompt</a> · <a href="styles/naive-marker-quote-card-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="sky-blue-home-life-doodle-poster-style"></a>
<a href="styles/sky-blue-home-life-doodle-poster-style"><img src="assets/thumbs/sky-blue-home-life-doodle-poster-style-16x9.jpg" alt="Sky Blue Home Life Doodle Poster Style preview"></a>
<p><strong><a href="styles/sky-blue-home-life-doodle-poster-style">Sky Blue Home Life Doodle Poster Style</a></strong><br>
<em>하늘색 집 모양 인셋, 거대한 검은 손글씨, 배지, 마커 일상 장면의 홈 라이프 포스터.</em><br>
<a href="styles/sky-blue-home-life-doodle-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/sky-blue-home-life-doodle-poster-style.md">prompt</a> · <a href="styles/sky-blue-home-life-doodle-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="playful-marker-grounding-poster-style"></a>
<a href="styles/playful-marker-grounding-poster-style"><img src="assets/thumbs/playful-marker-grounding-poster-style-16x9.jpg" alt="Playful Marker Grounding Poster Style preview"></a>
<p><strong><a href="styles/playful-marker-grounding-poster-style">Playful Marker Grounding Poster Style</a></strong><br>
<em>크림 여백, 마커 색면, 굵은 불균형 선, 큰 글자, 마스코트 인물이 있는 경쾌한 그라운딩 포스터.</em><br>
<a href="styles/playful-marker-grounding-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/playful-marker-grounding-poster-style.md">prompt</a> · <a href="styles/playful-marker-grounding-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="rough-marker-monster-poster-style"></a>
<a href="styles/rough-marker-monster-poster-style"><img src="assets/thumbs/rough-marker-monster-poster-style-16x9.jpg" alt="Rough Marker Monster Poster Style preview"></a>
<p><strong><a href="styles/rough-marker-monster-poster-style">Rough Marker Monster Poster Style</a></strong><br>
<em>굵은 마커 윤곽, 크레용 채색, 크림 종이, 손글씨 타입의 순진한 몬스터 포스터.</em><br>
<a href="styles/rough-marker-monster-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/rough-marker-monster-poster-style.md">prompt</a> · <a href="styles/rough-marker-monster-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="cyan-red-shockwave-type-poster-style"></a>
<a href="styles/cyan-red-shockwave-type-poster-style"><img src="assets/thumbs/cyan-red-shockwave-type-poster-style-16x9.jpg" alt="Cyan Red Shockwave Type Poster Style preview"></a>
<p><strong><a href="styles/cyan-red-shockwave-type-poster-style">Cyan Red Shockwave Type Poster Style</a></strong><br>
<em>거대한 빨간 블록 타입, 들쭉날쭉한 쇼크웨이브, 노란 포인트, 회전 마이크로카피의 시안 임팩트 포스터.</em><br>
<a href="styles/cyan-red-shockwave-type-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/cyan-red-shockwave-type-poster-style.md">prompt</a> · <a href="styles/cyan-red-shockwave-type-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="fantasy-scribble-mascot-poster-style"></a>
<a href="styles/fantasy-scribble-mascot-poster-style"><img src="assets/thumbs/fantasy-scribble-mascot-poster-style-16x9.jpg" alt="Fantasy Scribble Mascot Poster Style preview"></a>
<p><strong><a href="styles/fantasy-scribble-mascot-poster-style">Fantasy Scribble Mascot Poster Style</a></strong><br>
<em>네온 마커 마스코트, 커다란 손글씨, 빽빽한 낙서로 만든 순진한 판타지 포스터.</em><br>
<a href="styles/fantasy-scribble-mascot-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/fantasy-scribble-mascot-poster-style.md">prompt</a> · <a href="styles/fantasy-scribble-mascot-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="crayon-catalog-doodle-poster-style"></a>
<a href="styles/crayon-catalog-doodle-poster-style"><img src="assets/thumbs/crayon-catalog-doodle-poster-style-16x9.jpg" alt="Crayon Catalog Doodle Poster Style preview"></a>
<p><strong><a href="styles/crayon-catalog-doodle-poster-style">Crayon Catalog Doodle Poster Style</a></strong><br>
<em>빨간 손글씨 헤드라인, 단순한 낙서, 접힌 종이 질감의 성긴 크레용 카탈로그 포스터.</em><br>
<a href="styles/crayon-catalog-doodle-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/crayon-catalog-doodle-poster-style.md">prompt</a> · <a href="styles/crayon-catalog-doodle-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="blue-halftone-ransom-zine-poster-style"></a>
<a href="styles/blue-halftone-ransom-zine-poster-style"><img src="assets/thumbs/blue-halftone-ransom-zine-poster-style-16x9.jpg" alt="Blue Halftone Ransom Zine Poster Style preview"></a>
<p><strong><a href="styles/blue-halftone-ransom-zine-poster-style">Blue Halftone Ransom Zine Poster Style</a></strong><br>
<em>찢어진 종이 조각, 하프톤 컷아웃, 마커 글자를 결합한 코발트 블루 랜섬 진 포스터.</em><br>
<a href="styles/blue-halftone-ransom-zine-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/blue-halftone-ransom-zine-poster-style.md">prompt</a> · <a href="styles/blue-halftone-ransom-zine-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="market-brush-produce-poster-style"></a>
<a href="styles/market-brush-produce-poster-style"><img src="assets/thumbs/market-brush-produce-poster-style-16x9.jpg" alt="Market Brush Produce Poster Style preview"></a>
<p><strong><a href="styles/market-brush-produce-poster-style">Market Brush Produce Poster Style</a></strong><br>
<em>거대한 광택 농산물, 거친 붓글씨, 아이보리 종이 여백의 시장 포스터.</em><br>
<a href="styles/market-brush-produce-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/market-brush-produce-poster-style.md">prompt</a> · <a href="styles/market-brush-produce-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="folded-newspaper-product-ad-style"></a>
<a href="styles/folded-newspaper-product-ad-style"><img src="assets/thumbs/folded-newspaper-product-ad-style-16x9.jpg" alt="Folded Newspaper Product Ad Style preview"></a>
<p><strong><a href="styles/folded-newspaper-product-ad-style">Folded Newspaper Product Ad Style</a></strong><br>
<em>접힌 신문 애드버토리얼, 거대한 제품 컷아웃, 촘촘한 칼럼, 스탬프, 앤티크 골드 타이프.</em><br>
<a href="styles/folded-newspaper-product-ad-style/style.json">style.json</a> · <a href="docs/copy-prompts/folded-newspaper-product-ad-style.md">prompt</a> · <a href="styles/folded-newspaper-product-ad-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="sunlit-supermodel-nameplate-editorial"></a>
<a href="styles/sunlit-supermodel-nameplate-editorial"><img src="assets/thumbs/sunlit-supermodel-nameplate-editorial-16x9.jpg" alt="Sunlit Supermodel Nameplate Editorial preview"></a>
<p><strong><a href="styles/sunlit-supermodel-nameplate-editorial">Sunlit Supermodel Nameplate Editorial</a></strong><br>
<em>햇빛 슈퍼모델 에디토리얼, 야외 질감, 네임플레이트, 정돈된 하단 타이포.</em><br>
<a href="styles/sunlit-supermodel-nameplate-editorial/style.json">style.json</a> · <a href="docs/copy-prompts/sunlit-supermodel-nameplate-editorial.md">prompt</a> · <a href="styles/sunlit-supermodel-nameplate-editorial/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="black-cutout-food-card-ad-style"></a>
<a href="styles/black-cutout-food-card-ad-style"><img src="assets/thumbs/black-cutout-food-card-ad-style-16x9.jpg" alt="Black Cutout Food Card Ad preview"></a>
<p><strong><a href="styles/black-cutout-food-card-ad-style">Black Cutout Food Card Ad</a></strong><br>
<em>검은 음식 카드 광고, 손글씨 중국어, 컷아웃 사진, 길거리 간식 인쇄 질감.</em><br>
<a href="styles/black-cutout-food-card-ad-style/style.json">style.json</a> · <a href="docs/copy-prompts/black-cutout-food-card-ad-style.md">prompt</a> · <a href="styles/black-cutout-food-card-ad-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="kinetic-geometric-doodle-cutouts"></a>
<a href="styles/kinetic-geometric-doodle-cutouts"><img src="assets/thumbs/kinetic-geometric-doodle-cutouts-16x9.jpg" alt="Kinetic Geometric Doodle Cutouts preview"></a>
<p><strong><a href="styles/kinetic-geometric-doodle-cutouts">Kinetic Geometric Doodle Cutouts</a></strong><br>
<em>플랫 기하 색면, 느슨한 선, 종이 질감의 장난스러운 낙서 컷아웃.</em><br>
<a href="styles/kinetic-geometric-doodle-cutouts/style.json">style.json</a> · <a href="docs/copy-prompts/kinetic-geometric-doodle-cutouts.md">prompt</a> · <a href="styles/kinetic-geometric-doodle-cutouts/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="quiet-luxury-furniture-nameplate-poster-style"></a>
<a href="styles/quiet-luxury-furniture-nameplate-poster-style"><img src="assets/thumbs/quiet-luxury-furniture-nameplate-poster-style-16x9.jpg" alt="Quiet Luxury Furniture Nameplate Poster Style preview"></a>
<p><strong><a href="styles/quiet-luxury-furniture-nameplate-poster-style">Quiet Luxury Furniture Nameplate Poster Style</a></strong><br>
<em>포레스트 그린 대형 글자와 카탈로그 칩이 있는 조용한 럭셔리 가구 포스터.</em><br>
<a href="styles/quiet-luxury-furniture-nameplate-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/quiet-luxury-furniture-nameplate-poster-style.md">prompt</a> · <a href="styles/quiet-luxury-furniture-nameplate-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="kinetic-luxury-street-fashion-cover-style"></a>
<a href="styles/kinetic-luxury-street-fashion-cover-style"><img src="assets/thumbs/kinetic-luxury-street-fashion-cover-style-16x9.jpg" alt="Kinetic Luxury Street Fashion Cover Style preview"></a>
<p><strong><a href="styles/kinetic-luxury-street-fashion-cover-style">Kinetic Luxury Street Fashion Cover Style</a></strong><br>
<em>모션 블러 건축, 럭셔리 의상, 넓은 자간 세리프체의 패션 커버.</em><br>
<a href="styles/kinetic-luxury-street-fashion-cover-style/style.json">style.json</a> · <a href="docs/copy-prompts/kinetic-luxury-street-fashion-cover-style.md">prompt</a> · <a href="styles/kinetic-luxury-street-fashion-cover-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="sunlit-architectural-fashion-editorial"></a>
<a href="styles/sunlit-architectural-fashion-editorial"><img src="assets/thumbs/sunlit-architectural-fashion-editorial-16x9.jpg" alt="Sunlit Architectural Fashion Editorial preview"></a>
<p><strong><a href="styles/sunlit-architectural-fashion-editorial">Sunlit Architectural Fashion Editorial</a></strong><br>
<em>낮은 건축 시점, 따뜻한 석재, 길어진 실루엣의 햇빛 하이패션 에디토리얼.</em><br>
<a href="styles/sunlit-architectural-fashion-editorial/style.json">style.json</a> · <a href="docs/copy-prompts/sunlit-architectural-fashion-editorial.md">prompt</a> · <a href="styles/sunlit-architectural-fashion-editorial/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="multi-color-beverage-splash-ad-system-style"></a>
<a href="styles/multi-color-beverage-splash-ad-system-style"><img src="assets/thumbs/multi-color-beverage-splash-ad-system-style-16x9.jpg" alt="Multi-Color Beverage Splash Ad System Style preview"></a>
<p><strong><a href="styles/multi-color-beverage-splash-ad-system-style">Multi-Color Beverage Splash Ad System Style</a></strong><br>
<em>흰색 3D 대형 타이포와 얼어붙은 스플래시가 있는 다색 음료 출시 광고.</em><br>
<a href="styles/multi-color-beverage-splash-ad-system-style/style.json">style.json</a> · <a href="docs/copy-prompts/multi-color-beverage-splash-ad-system-style.md">prompt</a> · <a href="styles/multi-color-beverage-splash-ad-system-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="yellow-black-manga-food-zine-ad-style"></a>
<a href="styles/yellow-black-manga-food-zine-ad-style"><img src="assets/thumbs/yellow-black-manga-food-zine-ad-style-16x9.jpg" alt="Yellow Black Manga Food Zine Ad Style preview"></a>
<p><strong><a href="styles/yellow-black-manga-food-zine-ad-style">Yellow Black Manga Food Zine Ad Style</a></strong><br>
<em>검정-노랑 만화 음식 zine 광고, 뒤틀린 대형 타이포와 광택 주인공 오브젝트.</em><br>
<a href="styles/yellow-black-manga-food-zine-ad-style/style.json">style.json</a> · <a href="docs/copy-prompts/yellow-black-manga-food-zine-ad-style.md">prompt</a> · <a href="styles/yellow-black-manga-food-zine-ad-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="neon-outdoor-diary-longform-collage-style"></a>
<a href="styles/neon-outdoor-diary-longform-collage-style"><img src="assets/thumbs/neon-outdoor-diary-longform-collage-style-16x9.jpg" alt="Neon Outdoor Diary Longform Collage Style preview"></a>
<p><strong><a href="styles/neon-outdoor-diary-longform-collage-style">Neon Outdoor Diary Longform Collage Style</a></strong><br>
<em>산성 그린 제목, 찢어진 종이 패널, 사진 컷아웃의 야외 다이어리 롱폼 콜라주.</em><br>
<a href="styles/neon-outdoor-diary-longform-collage-style/style.json">style.json</a> · <a href="docs/copy-prompts/neon-outdoor-diary-longform-collage-style.md">prompt</a> · <a href="styles/neon-outdoor-diary-longform-collage-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="acid-lime-3d-streetwear-type-poster-style"></a>
<a href="styles/acid-lime-3d-streetwear-type-poster-style"><img src="assets/thumbs/acid-lime-3d-streetwear-type-poster-style-16x9.jpg" alt="Acid Lime 3D Streetwear Type Poster Style preview"></a>
<p><strong><a href="styles/acid-lime-3d-streetwear-type-poster-style">Acid Lime 3D Streetwear Type Poster Style</a></strong><br>
<em>검정 블록 타이포와 산성 라임 포인트의 광택 C4D 스트리트웨어 캠페인.</em><br>
<a href="styles/acid-lime-3d-streetwear-type-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/acid-lime-3d-streetwear-type-poster-style.md">prompt</a> · <a href="styles/acid-lime-3d-streetwear-type-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="electric-blue-silhouette-product-launch-style"></a>
<a href="styles/electric-blue-silhouette-product-launch-style"><img src="assets/thumbs/electric-blue-silhouette-product-launch-style-16x9.jpg" alt="Electric Blue Silhouette Product Launch Style preview"></a>
<p><strong><a href="styles/electric-blue-silhouette-product-launch-style">Electric Blue Silhouette Product Launch Style</a></strong><br>
<em>검정과 블루의 프리미엄 제품 런칭, 빛나는 실루엣과 크롭 타이포.</em><br>
<a href="styles/electric-blue-silhouette-product-launch-style/style.json">style.json</a> · <a href="docs/copy-prompts/electric-blue-silhouette-product-launch-style.md">prompt</a> · <a href="styles/electric-blue-silhouette-product-launch-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="luxury-perspective-checkerboard-editorial"></a>
<a href="styles/luxury-perspective-checkerboard-editorial"><img src="assets/thumbs/luxury-perspective-checkerboard-editorial-16x9.jpg" alt="Luxury Perspective Checkerboard Editorial preview"></a>
<p><strong><a href="styles/luxury-perspective-checkerboard-editorial">Luxury Perspective Checkerboard Editorial</a></strong><br>
<em>체크보드 원근, 스크립트 타이포, 세련된 여백의 럭셔리 에디토리얼.</em><br>
<a href="styles/luxury-perspective-checkerboard-editorial/style.json">style.json</a> · <a href="docs/copy-prompts/luxury-perspective-checkerboard-editorial.md">prompt</a> · <a href="styles/luxury-perspective-checkerboard-editorial/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="sunny-3d-avatar-campaign-style"></a>
<a href="styles/sunny-3d-avatar-campaign-style"><img src="assets/thumbs/sunny-3d-avatar-campaign-style-16x9.jpg" alt="Sunny 3D Avatar Campaign Style preview"></a>
<p><strong><a href="styles/sunny-3d-avatar-campaign-style">Sunny 3D Avatar Campaign Style</a></strong><br>
<em>맑은 캠페인형 3D 아바타, 푸른 하늘, 큰 사선 타이포와 네온 동선.</em><br>
<a href="styles/sunny-3d-avatar-campaign-style/style.json">style.json</a> · <a href="docs/copy-prompts/sunny-3d-avatar-campaign-style.md">prompt</a> · <a href="styles/sunny-3d-avatar-campaign-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="y2k-mirror-ui-scribble-collage-style"></a>
<a href="styles/y2k-mirror-ui-scribble-collage-style"><img src="assets/thumbs/y2k-mirror-ui-scribble-collage-style-16x9.jpg" alt="Y2K Mirror UI Scribble Collage Style preview"></a>
<p><strong><a href="styles/y2k-mirror-ui-scribble-collage-style">Y2K Mirror UI Scribble Collage Style</a></strong><br>
<em>플래시 사진 위에 Y2K UI 패널, 전기 블루 낙서선, 거친 화면 노이즈.</em><br>
<a href="styles/y2k-mirror-ui-scribble-collage-style/style.json">style.json</a> · <a href="docs/copy-prompts/y2k-mirror-ui-scribble-collage-style.md">prompt</a> · <a href="styles/y2k-mirror-ui-scribble-collage-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="neon-plush-gadget-pop-3d-style"></a>
<a href="styles/neon-plush-gadget-pop-3d-style"><img src="assets/thumbs/neon-plush-gadget-pop-3d-style-16x9.jpg" alt="Neon Plush Gadget Pop 3D Style preview"></a>
<p><strong><a href="styles/neon-plush-gadget-pop-3d-style">Neon Plush Gadget Pop 3D Style</a></strong><br>
<em>플러시 마스코트와 두툼한 가젯 소품을 결합한 네온 장난감 제품 3D 렌더.</em><br>
<a href="styles/neon-plush-gadget-pop-3d-style/style.json">style.json</a> · <a href="docs/copy-prompts/neon-plush-gadget-pop-3d-style.md">prompt</a> · <a href="styles/neon-plush-gadget-pop-3d-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="blue-lime-kinetic-comic-type-poster-style"></a>
<a href="styles/blue-lime-kinetic-comic-type-poster-style"><img src="assets/thumbs/blue-lime-kinetic-comic-type-poster-style-16x9.jpg" alt="Blue Lime Kinetic Comic Type Poster Style preview"></a>
<p><strong><a href="styles/blue-lime-kinetic-comic-type-poster-style">Blue Lime Kinetic Comic Type Poster Style</a></strong><br>
<em>Electric-blue comic posters with lime speech panels and massive black type.</em><br>
<a href="styles/blue-lime-kinetic-comic-type-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/blue-lime-kinetic-comic-type-poster-style.md">prompt</a> · <a href="styles/blue-lime-kinetic-comic-type-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="blue-chinese-perspective-type-canyon-style"></a>
<a href="styles/blue-chinese-perspective-type-canyon-style"><img src="assets/thumbs/blue-chinese-perspective-type-canyon-style-16x9.jpg" alt="Blue Chinese Perspective Type Canyon Style preview"></a>
<p><strong><a href="styles/blue-chinese-perspective-type-canyon-style">Blue Chinese Perspective Type Canyon Style</a></strong><br>
<em>Blue perspective corridors with stacked Chinese display type.</em><br>
<a href="styles/blue-chinese-perspective-type-canyon-style/style.json">style.json</a> · <a href="docs/copy-prompts/blue-chinese-perspective-type-canyon-style.md">prompt</a> · <a href="styles/blue-chinese-perspective-type-canyon-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="rough-ink-music-doodle-poster-style"></a>
<a href="styles/rough-ink-music-doodle-poster-style"><img src="assets/thumbs/rough-ink-music-doodle-poster-style-16x9.jpg" alt="Rough Ink Music Doodle Poster Style preview"></a>
<p><strong><a href="styles/rough-ink-music-doodle-poster-style">Rough Ink Music Doodle Poster Style</a></strong><br>
<em>Hand-inked music posters with brush lettering and playful doodles.</em><br>
<a href="styles/rough-ink-music-doodle-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/rough-ink-music-doodle-poster-style.md">prompt</a> · <a href="styles/rough-ink-music-doodle-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="mono-noir-type-portrait-poster-style"></a>
<a href="styles/mono-noir-type-portrait-poster-style"><img src="assets/thumbs/mono-noir-type-portrait-poster-style-16x9.jpg" alt="Mono Noir Type Portrait Poster Style preview"></a>
<p><strong><a href="styles/mono-noir-type-portrait-poster-style">Mono Noir Type Portrait Poster Style</a></strong><br>
<em>Black-and-white editorial portraits with massive lowercase type.</em><br>
<a href="styles/mono-noir-type-portrait-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/mono-noir-type-portrait-poster-style.md">prompt</a> · <a href="styles/mono-noir-type-portrait-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="bold-block-mascot-poster-style"></a>
<a href="styles/bold-block-mascot-poster-style"><img src="assets/thumbs/bold-block-mascot-poster-style-16x9.jpg" alt="Bold Block Mascot Poster Style preview"></a>
<p><strong><a href="styles/bold-block-mascot-poster-style">Bold Block Mascot Poster Style</a></strong><br>
<em>Flat mascot posters with chunky block type and sticker figures.</em><br>
<a href="styles/bold-block-mascot-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/bold-block-mascot-poster-style.md">prompt</a> · <a href="styles/bold-block-mascot-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="blue-hud-macro-product-poster"></a>
<a href="styles/blue-hud-macro-product-poster"><img src="assets/thumbs/blue-hud-macro-product-poster-16x9.jpg" alt="Blue HUD Macro Creator Tech Poster preview"></a>
<p><strong><a href="styles/blue-hud-macro-product-poster">Blue HUD Macro Creator Tech Poster</a></strong><br>
<em>Glossy macro product posters with blue HUD launch graphics.</em><br>
<a href="styles/blue-hud-macro-product-poster/style.json">style.json</a> · <a href="docs/copy-prompts/blue-hud-macro-product-poster.md">prompt</a> · <a href="styles/blue-hud-macro-product-poster/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="warm-fisheye-product-impact-ad-style"></a>
<a href="styles/warm-fisheye-product-impact-ad-style"><img src="assets/thumbs/warm-fisheye-product-impact-ad-style-16x9.jpg" alt="Warm Fisheye Product Impact Ad Style preview"></a>
<p><strong><a href="styles/warm-fisheye-product-impact-ad-style">Warm Fisheye Product Impact Ad Style</a></strong><br>
<em>Warm fisheye product ads with bold Chinese social-commerce type.</em><br>
<a href="styles/warm-fisheye-product-impact-ad-style/style.json">style.json</a> · <a href="docs/copy-prompts/warm-fisheye-product-impact-ad-style.md">prompt</a> · <a href="styles/warm-fisheye-product-impact-ad-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="olive-scribble-sports-poster-style"></a>
<a href="styles/olive-scribble-sports-poster-style"><img src="assets/thumbs/olive-scribble-sports-poster-style-16x9.jpg" alt="Olive Scribble Sports Poster Style preview"></a>
<p><strong><a href="styles/olive-scribble-sports-poster-style">Olive Scribble Sports Poster Style</a></strong><br>
<em>Handmade sports posters with olive blocks and kinetic scribbles.</em><br>
<a href="styles/olive-scribble-sports-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/olive-scribble-sports-poster-style.md">prompt</a> · <a href="styles/olive-scribble-sports-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="bold-anime-reaction-thumbnail-style"></a>
<a href="styles/bold-anime-reaction-thumbnail-style"><img src="assets/thumbs/bold-anime-reaction-thumbnail-style-16x9.jpg" alt="Bold Anime Reaction Thumbnail Style preview"></a>
<p><strong><a href="styles/bold-anime-reaction-thumbnail-style">Bold Anime Reaction Thumbnail Style</a></strong><br>
<em>High-impact anime thumbnails with bold yellow reaction typography.</em><br>
<a href="styles/bold-anime-reaction-thumbnail-style/style.json">style.json</a> · <a href="docs/copy-prompts/bold-anime-reaction-thumbnail-style.md">prompt</a> · <a href="styles/bold-anime-reaction-thumbnail-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="turquoise-red-techno-manga-poster-style"></a>
<a href="styles/turquoise-red-techno-manga-poster-style"><img src="assets/thumbs/turquoise-red-techno-manga-poster-style-16x9.jpg" alt="Turquoise Red Techno Manga Poster Style preview"></a>
<p><strong><a href="styles/turquoise-red-techno-manga-poster-style">Turquoise Red Techno Manga Poster Style</a></strong><br>
<em>Retro techno-manga posters with turquoise hardware and red lettering.</em><br>
<a href="styles/turquoise-red-techno-manga-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/turquoise-red-techno-manga-poster-style.md">prompt</a> · <a href="styles/turquoise-red-techno-manga-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="chromatic-fisheye-orbit-pop-poster-style"></a>
<a href="styles/chromatic-fisheye-orbit-pop-poster-style"><img src="assets/thumbs/chromatic-fisheye-orbit-pop-poster-style-16x9.jpg" alt="Chromatic Fisheye Orbit Pop Poster Style preview"></a>
<p><strong><a href="styles/chromatic-fisheye-orbit-pop-poster-style">Chromatic Fisheye Orbit Pop Poster Style</a></strong><br>
<em>Pop fisheye posters with orbiting type and chromatic arcs.</em><br>
<a href="styles/chromatic-fisheye-orbit-pop-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/chromatic-fisheye-orbit-pop-poster-style.md">prompt</a> · <a href="styles/chromatic-fisheye-orbit-pop-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="naive-marker-psa-poster-style"></a>
<a href="styles/naive-marker-psa-poster-style"><img src="assets/thumbs/naive-marker-psa-poster-style-16x9.jpg" alt="Naive Marker PSA Poster Style preview"></a>
<p><strong><a href="styles/naive-marker-psa-poster-style">Naive Marker PSA Poster Style</a></strong><br>
<em>Friendly civic PSA posters with naive marker drawings.</em><br>
<a href="styles/naive-marker-psa-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/naive-marker-psa-poster-style.md">prompt</a> · <a href="styles/naive-marker-psa-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="blue-bubble-fisheye-action-poster-style"></a>
<a href="styles/blue-bubble-fisheye-action-poster-style"><img src="assets/thumbs/blue-bubble-fisheye-action-poster-style-16x9.jpg" alt="Blue Bubble Fisheye Action Poster Style preview"></a>
<p><strong><a href="styles/blue-bubble-fisheye-action-poster-style">Blue Bubble Fisheye Action Poster Style</a></strong><br>
<em>Youth action posters with blue bubble type and fisheye photos.</em><br>
<a href="styles/blue-bubble-fisheye-action-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/blue-bubble-fisheye-action-poster-style.md">prompt</a> · <a href="styles/blue-bubble-fisheye-action-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="cozy-bedroom-doodle-companion-snapshot-style"></a>
<a href="styles/cozy-bedroom-doodle-companion-snapshot-style"><img src="assets/thumbs/cozy-bedroom-doodle-companion-snapshot-style-16x9.jpg" alt="Cozy Bedroom Doodle Companion Snapshot Style preview"></a>
<p><strong><a href="styles/cozy-bedroom-doodle-companion-snapshot-style">Cozy Bedroom Doodle Companion Snapshot Style</a></strong><br>
<em>Low-light bedroom snapshots with quiet doodle companion energy.</em><br>
<a href="styles/cozy-bedroom-doodle-companion-snapshot-style/style.json">style.json</a> · <a href="docs/copy-prompts/cozy-bedroom-doodle-companion-snapshot-style.md">prompt</a> · <a href="styles/cozy-bedroom-doodle-companion-snapshot-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="surreal-fish-doodle-landmark-photo-collage-style"></a>
<a href="styles/surreal-fish-doodle-landmark-photo-collage-style"><img src="assets/thumbs/surreal-fish-doodle-landmark-photo-collage-style-16x9.jpg" alt="Surreal Fish Doodle Landmark Photo Collage Style preview"></a>
<p><strong><a href="styles/surreal-fish-doodle-landmark-photo-collage-style">Surreal Fish Doodle Landmark Photo Collage Style</a></strong><br>
<em>Landmark travel photos remixed with folk-art fish doodles.</em><br>
<a href="styles/surreal-fish-doodle-landmark-photo-collage-style/style.json">style.json</a> · <a href="docs/copy-prompts/surreal-fish-doodle-landmark-photo-collage-style.md">prompt</a> · <a href="styles/surreal-fish-doodle-landmark-photo-collage-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="plush-comic-toy-product-poster-style"></a>
<a href="styles/plush-comic-toy-product-poster-style"><img src="assets/thumbs/plush-comic-toy-product-poster-style-16x9.jpg" alt="Plush Comic Toy Product Poster Style preview"></a>
<p><strong><a href="styles/plush-comic-toy-product-poster-style">Plush Comic Toy Product Poster Style</a></strong><br>
<em>Toy-product posters with fuzzy plush heroes and comic typography.</em><br>
<a href="styles/plush-comic-toy-product-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/plush-comic-toy-product-poster-style.md">prompt</a> · <a href="styles/plush-comic-toy-product-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="rough-animation-pet-sketch-storyboard-style"></a>
<a href="styles/rough-animation-pet-sketch-storyboard-style"><img src="assets/thumbs/rough-animation-pet-sketch-storyboard-style-16x9.jpg" alt="Rough Animation Pet Sketch Storyboard Style preview"></a>
<p><strong><a href="styles/rough-animation-pet-sketch-storyboard-style">Rough Animation Pet Sketch Storyboard Style</a></strong><br>
<em>Loose pet-comedy storyboard frames with warm sketch texture.</em><br>
<a href="styles/rough-animation-pet-sketch-storyboard-style/style.json">style.json</a> · <a href="docs/copy-prompts/rough-animation-pet-sketch-storyboard-style.md">prompt</a> · <a href="styles/rough-animation-pet-sketch-storyboard-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="tri-color-hardcut-portrait-poster-style"></a>
<a href="styles/tri-color-hardcut-portrait-poster-style"><img src="assets/thumbs/tri-color-hardcut-portrait-poster-style-16x9.jpg" alt="Tri Color Hardcut Portrait Poster Style preview"></a>
<p><strong><a href="styles/tri-color-hardcut-portrait-poster-style">Tri Color Hardcut Portrait Poster Style</a></strong><br>
<em>Three-color portrait posters built from hard-edged cutout planes.</em><br>
<a href="styles/tri-color-hardcut-portrait-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/tri-color-hardcut-portrait-poster-style.md">prompt</a> · <a href="styles/tri-color-hardcut-portrait-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="clean-triptych-travel-vlog-thumbnail-style"></a>
<a href="styles/clean-triptych-travel-vlog-thumbnail-style"><img src="assets/thumbs/clean-triptych-travel-vlog-thumbnail-style-16x9.jpg" alt="Clean Triptych Travel Vlog Thumbnail Style preview"></a>
<p><strong><a href="styles/clean-triptych-travel-vlog-thumbnail-style">Clean Triptych Travel Vlog Thumbnail Style</a></strong><br>
<em>Clean travel thumbnails with three photo panels and soft notes.</em><br>
<a href="styles/clean-triptych-travel-vlog-thumbnail-style/style.json">style.json</a> · <a href="docs/copy-prompts/clean-triptych-travel-vlog-thumbnail-style.md">prompt</a> · <a href="styles/clean-triptych-travel-vlog-thumbnail-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="playful-mascot-doodle-snapshot-style"></a>
<a href="styles/playful-mascot-doodle-snapshot-style"><img src="assets/thumbs/playful-mascot-doodle-snapshot-style-16x9.jpg" alt="Playful Mascot Doodle Snapshot Style preview"></a>
<p><strong><a href="styles/playful-mascot-doodle-snapshot-style">Playful Mascot Doodle Snapshot Style</a></strong><br>
<em>Real-life snapshots layered with mascot stickers and doodles.</em><br>
<a href="styles/playful-mascot-doodle-snapshot-style/style.json">style.json</a> · <a href="docs/copy-prompts/playful-mascot-doodle-snapshot-style.md">prompt</a> · <a href="styles/playful-mascot-doodle-snapshot-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="teenage-skate-scribble-screenprint-poster-style"></a>
<a href="styles/teenage-skate-scribble-screenprint-poster-style"><img src="assets/thumbs/teenage-skate-scribble-screenprint-poster-style-16x9.jpg" alt="Teenage Skate Scribble Screenprint Poster Style preview"></a>
<p><strong><a href="styles/teenage-skate-scribble-screenprint-poster-style">Teenage Skate Scribble Screenprint Poster Style</a></strong><br>
<em>Retro skate posters with scribbled borders and screenprint grit.</em><br>
<a href="styles/teenage-skate-scribble-screenprint-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/teenage-skate-scribble-screenprint-poster-style.md">prompt</a> · <a href="styles/teenage-skate-scribble-screenprint-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="impact-burst-halftone-comic-poster-style"></a>
<a href="styles/impact-burst-halftone-comic-poster-style"><img src="assets/thumbs/impact-burst-halftone-comic-poster-style-16x9.jpg" alt="Impact Burst Halftone Comic Poster Style preview"></a>
<p><strong><a href="styles/impact-burst-halftone-comic-poster-style">Impact Burst Halftone Comic Poster Style</a></strong><br>
<em>Loud comic posters with impact type and halftone bursts.</em><br>
<a href="styles/impact-burst-halftone-comic-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/impact-burst-halftone-comic-poster-style.md">prompt</a> · <a href="styles/impact-burst-halftone-comic-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="sunburst-fisheye-bubble-type-poster-style"></a>
<a href="styles/sunburst-fisheye-bubble-type-poster-style"><img src="assets/thumbs/sunburst-fisheye-bubble-type-poster-style-16x9.jpg" alt="Sunburst Fisheye Bubble Type Poster Style preview"></a>
<p><strong><a href="styles/sunburst-fisheye-bubble-type-poster-style">Sunburst Fisheye Bubble Type Poster Style</a></strong><br>
<em>Summer fisheye posters with sunny bubble typography.</em><br>
<a href="styles/sunburst-fisheye-bubble-type-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/sunburst-fisheye-bubble-type-poster-style.md">prompt</a> · <a href="styles/sunburst-fisheye-bubble-type-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="backseat-transit-doodle-letter-poster-style"></a>
<a href="styles/backseat-transit-doodle-letter-poster-style"><img src="assets/thumbs/backseat-transit-doodle-letter-poster-style-16x9.jpg" alt="Backseat Transit Doodle Letter Poster Style preview"></a>
<p><strong><a href="styles/backseat-transit-doodle-letter-poster-style">Backseat Transit Doodle Letter Poster Style</a></strong><br>
<em>Transit photos turned into energetic hand-lettered travel posters.</em><br>
<a href="styles/backseat-transit-doodle-letter-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/backseat-transit-doodle-letter-poster-style.md">prompt</a> · <a href="styles/backseat-transit-doodle-letter-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="analog-sticker-diary-portrait-poster-style"></a>
<a href="styles/analog-sticker-diary-portrait-poster-style"><img src="assets/thumbs/analog-sticker-diary-portrait-poster-style-16x9.jpg" alt="Analog Sticker Diary Portrait Poster Style preview"></a>
<p><strong><a href="styles/analog-sticker-diary-portrait-poster-style">Analog Sticker Diary Portrait Poster Style</a></strong><br>
<em>Nostalgic diary portraits with stickers and distressed lettering.</em><br>
<a href="styles/analog-sticker-diary-portrait-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/analog-sticker-diary-portrait-poster-style.md">prompt</a> · <a href="styles/analog-sticker-diary-portrait-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="folded-diamond-perspective-type-poster-style"></a>
<a href="styles/folded-diamond-perspective-type-poster-style"><img src="assets/thumbs/folded-diamond-perspective-type-poster-style-16x9.jpg" alt="Folded Diamond Perspective Type Poster Style preview"></a>
<p><strong><a href="styles/folded-diamond-perspective-type-poster-style">Folded Diamond Perspective Type Poster Style</a></strong><br>
<em>Minimal diamond-aperture posters with folded perspective typography.</em><br>
<a href="styles/folded-diamond-perspective-type-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/folded-diamond-perspective-type-poster-style.md">prompt</a> · <a href="styles/folded-diamond-perspective-type-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="gothic-cat-doodle-photo-collage-style"></a>
<a href="styles/gothic-cat-doodle-photo-collage-style"><img src="assets/thumbs/gothic-cat-doodle-photo-collage-style-16x9.jpg" alt="Gothic Cat Doodle Photo Collage Style preview"></a>
<p><strong><a href="styles/gothic-cat-doodle-photo-collage-style">Gothic Cat Doodle Photo Collage Style</a></strong><br>
<em>Dramatic architecture photos with playful cartoon creature overlays.</em><br>
<a href="styles/gothic-cat-doodle-photo-collage-style/style.json">style.json</a> · <a href="docs/copy-prompts/gothic-cat-doodle-photo-collage-style.md">prompt</a> · <a href="styles/gothic-cat-doodle-photo-collage-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="k-pop-apocalypse-ransom-zine-style"></a>
<a href="styles/k-pop-apocalypse-ransom-zine-style"><img src="assets/thumbs/k-pop-apocalypse-ransom-zine-style-16x9.jpg" alt="K-Pop Apocalypse Ransom Zine Style preview"></a>
<p><strong><a href="styles/k-pop-apocalypse-ransom-zine-style">K-Pop Apocalypse Ransom Zine Style</a></strong><br>
<em>Maximal K-pop zines with ransom type and sticker blocks.</em><br>
<a href="styles/k-pop-apocalypse-ransom-zine-style/style.json">style.json</a> · <a href="docs/copy-prompts/k-pop-apocalypse-ransom-zine-style.md">prompt</a> · <a href="styles/k-pop-apocalypse-ransom-zine-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="metro-doodle-snapshot-diary-style"></a>
<a href="styles/metro-doodle-snapshot-diary-style"><img src="assets/thumbs/metro-doodle-snapshot-diary-style-16x9.jpg" alt="Metro Doodle Snapshot Diary preview"></a>
<p><strong><a href="styles/metro-doodle-snapshot-diary-style">Metro Doodle Snapshot Diary</a></strong><br>
<em>Crowded transit snapshots layered with marker doodles and oversized comic faces.</em><br>
<a href="styles/metro-doodle-snapshot-diary-style/style.json">style.json</a> · <a href="docs/copy-prompts/metro-doodle-snapshot-diary-style.md">prompt</a> · <a href="styles/metro-doodle-snapshot-diary-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="mountain-trail-monster-doodle-poster-style"></a>
<a href="styles/mountain-trail-monster-doodle-poster-style"><img src="assets/thumbs/mountain-trail-monster-doodle-poster-style-16x9.jpg" alt="Mountain Trail Monster Doodle Poster Style preview"></a>
<p><strong><a href="styles/mountain-trail-monster-doodle-poster-style">Mountain Trail Monster Doodle Poster Style</a></strong><br>
<em>Outdoor hiking photos remixed with monster companions and annotations.</em><br>
<a href="styles/mountain-trail-monster-doodle-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/mountain-trail-monster-doodle-poster-style.md">prompt</a> · <a href="styles/mountain-trail-monster-doodle-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="neon-doodle-gallery-snapshot-style"></a>
<a href="styles/neon-doodle-gallery-snapshot-style"><img src="assets/thumbs/neon-doodle-gallery-snapshot-style-16x9.jpg" alt="Neon Doodle Gallery Snapshot preview"></a>
<p><strong><a href="styles/neon-doodle-gallery-snapshot-style">Neon Doodle Gallery Snapshot</a></strong><br>
<em>Phone photos covered in hot neon diary doodles.</em><br>
<a href="styles/neon-doodle-gallery-snapshot-style/style.json">style.json</a> · <a href="docs/copy-prompts/neon-doodle-gallery-snapshot-style.md">prompt</a> · <a href="styles/neon-doodle-gallery-snapshot-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="neon-kinetic-typographic-poster-style"></a>
<a href="styles/neon-kinetic-typographic-poster-style"><img src="assets/thumbs/neon-kinetic-typographic-poster-style-16x9.jpg" alt="Neon Kinetic Typographic Poster preview"></a>
<p><strong><a href="styles/neon-kinetic-typographic-poster-style">Neon Kinetic Typographic Poster</a></strong><br>
<em>Outdoor editorial posters with warped neon kinetic typography.</em><br>
<a href="styles/neon-kinetic-typographic-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/neon-kinetic-typographic-poster-style.md">prompt</a> · <a href="styles/neon-kinetic-typographic-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="orange-brush-mascot-action-poster-style"></a>
<a href="styles/orange-brush-mascot-action-poster-style"><img src="assets/thumbs/orange-brush-mascot-action-poster-style-16x9.jpg" alt="Orange Brush Mascot Action Poster Style preview"></a>
<p><strong><a href="styles/orange-brush-mascot-action-poster-style">Orange Brush Mascot Action Poster Style</a></strong><br>
<em>Sparse mascot illustrations with orange brush texture and print grain.</em><br>
<a href="styles/orange-brush-mascot-action-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/orange-brush-mascot-action-poster-style.md">prompt</a> · <a href="styles/orange-brush-mascot-action-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="photo-illustration-overlay-poster-style"></a>
<a href="styles/photo-illustration-overlay-poster-style"><img src="assets/thumbs/photo-illustration-overlay-poster-style-16x9.jpg" alt="Photo Illustration Overlay Poster preview"></a>
<p><strong><a href="styles/photo-illustration-overlay-poster-style">Photo Illustration Overlay Poster</a></strong><br>
<em>City photos composited with saturated 2D character overlays.</em><br>
<a href="styles/photo-illustration-overlay-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/photo-illustration-overlay-poster-style.md">prompt</a> · <a href="styles/photo-illustration-overlay-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="plush-city-festival-mobile-poster-style"></a>
<a href="styles/plush-city-festival-mobile-poster-style"><img src="assets/thumbs/plush-city-festival-mobile-poster-style-16x9.jpg" alt="Plush City Festival Mobile Poster preview"></a>
<p><strong><a href="styles/plush-city-festival-mobile-poster-style">Plush City Festival Mobile Poster</a></strong><br>
<em>Mobile city-event posters with fuzzy mascots and app-card framing.</em><br>
<a href="styles/plush-city-festival-mobile-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/plush-city-festival-mobile-poster-style.md">prompt</a> · <a href="styles/plush-city-festival-mobile-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="pop-bubble-letter-photo-poster-style"></a>
<a href="styles/pop-bubble-letter-photo-poster-style"><img src="assets/thumbs/pop-bubble-letter-photo-poster-style-16x9.jpg" alt="Pop Bubble Letter Photo Poster Style preview"></a>
<p><strong><a href="styles/pop-bubble-letter-photo-poster-style">Pop Bubble Letter Photo Poster Style</a></strong><br>
<em>Fashion photo posters framed by candy-colored bubble letters.</em><br>
<a href="styles/pop-bubble-letter-photo-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/pop-bubble-letter-photo-poster-style.md">prompt</a> · <a href="styles/pop-bubble-letter-photo-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="soft-analog-future-editorial-poster-style"></a>
<a href="styles/soft-analog-future-editorial-poster-style"><img src="assets/thumbs/soft-analog-future-editorial-poster-style-16x9.jpg" alt="Soft Analog Future Editorial Poster preview"></a>
<p><strong><a href="styles/soft-analog-future-editorial-poster-style">Soft Analog Future Editorial Poster</a></strong><br>
<em>Quiet analog-future editorials with grids and retro technology.</em><br>
<a href="styles/soft-analog-future-editorial-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/soft-analog-future-editorial-poster-style.md">prompt</a> · <a href="styles/soft-analog-future-editorial-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="subway-doodle-photo-hybrid-style"></a>
<a href="styles/subway-doodle-photo-hybrid-style"><img src="assets/thumbs/subway-doodle-photo-hybrid-style-16x9.jpg" alt="Subway Doodle Photo Hybrid preview"></a>
<p><strong><a href="styles/subway-doodle-photo-hybrid-style">Subway Doodle Photo Hybrid</a></strong><br>
<em>Subway photos overlaid with social-media-style cartoon doodles and handwritten notes.</em><br>
<a href="styles/subway-doodle-photo-hybrid-style/style.json">style.json</a> · <a href="docs/copy-prompts/subway-doodle-photo-hybrid-style.md">prompt</a> · <a href="styles/subway-doodle-photo-hybrid-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="tokyo-kawaii-travel-collage-poster-style"></a>
<a href="styles/tokyo-kawaii-travel-collage-poster-style"><img src="assets/thumbs/tokyo-kawaii-travel-collage-poster-style-16x9.jpg" alt="Tokyo Kawaii Travel Collage Poster preview"></a>
<p><strong><a href="styles/tokyo-kawaii-travel-collage-poster-style">Tokyo Kawaii Travel Collage Poster</a></strong><br>
<em>Maximal Tokyo travel collages with manga bubbles and stickers.</em><br>
<a href="styles/tokyo-kawaii-travel-collage-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/tokyo-kawaii-travel-collage-poster-style.md">prompt</a> · <a href="styles/tokyo-kawaii-travel-collage-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="urban-transit-doodle-diary-style"></a>
<a href="styles/urban-transit-doodle-diary-style"><img src="assets/thumbs/urban-transit-doodle-diary-style-16x9.jpg" alt="Urban Transit Doodle Diary Style preview"></a>
<p><strong><a href="styles/urban-transit-doodle-diary-style">Urban Transit Doodle Diary Style</a></strong><br>
<em>Public-space photos remixed with bold foreground gestures and travel diary notes.</em><br>
<a href="styles/urban-transit-doodle-diary-style/style.json">style.json</a> · <a href="docs/copy-prompts/urban-transit-doodle-diary-style.md">prompt</a> · <a href="styles/urban-transit-doodle-diary-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="y2k-grunge-hiphop-cutout-poster-style"></a>
<a href="styles/y2k-grunge-hiphop-cutout-poster-style"><img src="assets/thumbs/y2k-grunge-hiphop-cutout-poster-style-16x9.jpg" alt="Y2K Grunge Hip-Hop Cutout Poster Style preview"></a>
<p><strong><a href="styles/y2k-grunge-hiphop-cutout-poster-style">Y2K Grunge Hip-Hop Cutout Poster Style</a></strong><br>
<em>Y2K hip-hop collage posters with acid type and photocopy grit.</em><br>
<a href="styles/y2k-grunge-hiphop-cutout-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/y2k-grunge-hiphop-cutout-poster-style.md">prompt</a> · <a href="styles/y2k-grunge-hiphop-cutout-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
</table>

## 게시 모델

- 하나의 디렉터리 = 하나의 스타일
- 새 스타일은 추천 스타일과 All Styles 갤러리에 먼저 표시하고, 전체 설명은 [docs/CATALOG.md](docs/CATALOG.md)에 추가합니다
- main 브랜치에는 각 스타일의 `style.json` 과 두 장의 JPG 미리보기만 포함합니다
- 전체 갤러리는 이 저장소에 포함하지 않습니다
- 원본 레퍼런스 이미지, 워터마크, 플랫폼 식별자, QR 코드, 계정 핸들, 비공개 프롬프트, 허가되지 않은 브랜드 자산은 게시하지 않습니다

## Contributing

새 스타일 제출은 [CONTRIBUTING.md](CONTRIBUTING.md)의 공개 패키지 구조, 검증 규칙, PR checklist 를 따라야 합니다.

## 라이선스

코드, 스크립트, 문서는 [MIT 라이선스](LICENSE)를 따릅니다. `style.json` 프롬프트 내용은 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 라이선스입니다 — [@VigoCreativeAI](https://x.com/VigoCreativeAI) 출처 표기 후 자유롭게 재사용·변형할 수 있습니다. 미리보기 이미지는 시각 참고용으로 포함되어 있습니다.
