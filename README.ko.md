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
  <img alt="Styles" src="https://img.shields.io/badge/styles-172-ff5a7a?style=flat-square">
  <img alt="Previews" src="https://img.shields.io/badge/previews-344-4cc9f0?style=flat-square">
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
  🖼️ <strong><a href="https://prompts.vigocreativeai.com/site/">온라인 갤러리</a></strong> · 또는 아래 <a href="#all-styles">All Styles 갤러리</a> / <a href="docs/CATALOG.md">전체 카탈로그</a>를 확인하세요.
</p>

<p align="center">
  💬 스타일로 만든 작품이 있다면 <a href="https://github.com/VigoZhao/AI-Visual-Prompt-Cookbook/discussions/categories/show-and-tell">Show and tell에 공유하세요</a> · 원하는 스타일이 없다면 <a href="https://github.com/VigoZhao/AI-Visual-Prompt-Cookbook/discussions/categories/ideas">요청하기</a>
</p>

## 빠른 링크

| 카테고리 | 적합한 용도 | 먼저 볼 스타일 |
| --- | --- | --- |
| 사진 + 드로잉 | 소셜 스냅, 라이프스타일 장면, 장난스러운 스티커 오버레이 | [Playful Mascot Doodle Snapshot](styles/playful-mascot-doodle-snapshot-style), [Subway Doodle Photo Hybrid](styles/subway-doodle-photo-hybrid-style) |
| Zine + 콜라주 | 패션 포스터, 음악 비주얼, 맥시멀 에디토리얼 레이아웃 | [K-pop Apocalypse Ransom Zine](styles/k-pop-apocalypse-ransom-zine-style), [Y2K Grunge Hip-hop Cutout Poster](styles/y2k-grunge-hiphop-cutout-poster-style) |
| 타이포그래피 포스터 | 큰 헤드라인, 강한 캠페인 그래픽, 시각적 임팩트 | [Impact Burst Halftone Comic Poster](styles/impact-burst-halftone-comic-poster-style), [Neon Kinetic Typographic Poster](styles/neon-kinetic-typographic-poster-style) |
| 여행 + 도시 | 여행지 포스터, 거리 장면, 도시 비주얼 다이어리 | [Clean Triptych Travel Vlog Thumbnail](styles/clean-triptych-travel-vlog-thumbnail-style), [Tokyo Kawaii Travel Collage Poster](styles/tokyo-kawaii-travel-collage-poster-style) |
| 에디토리얼 + 미니멀 | 깔끔한 구성, 구조적인 레이아웃, 차분한 아트 디렉션 | [Tri Color Hardcut Portrait Poster](styles/tri-color-hardcut-portrait-poster-style), [Soft Analog Future Editorial Poster](styles/soft-analog-future-editorial-poster-style) |

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

<!-- BEGIN GENERATED: featured (generated by scripts/generate-readme.py from data/catalog.json; do not edit by hand) -->
이 6개 스타일로 시작하면 라이브러리의 범위를 빠르게 이해할 수 있습니다. 모든 스타일은 JSON 하나와 미리보기 이미지 두 장으로 구성됩니다. 전체 172개는 [온라인 갤러리](https://prompts.vigocreativeai.com/site/) 또는 영어 README의 [All Styles](README.md#all-styles)에서 볼 수 있습니다.

<!-- HTML table used for rich image+link cells -->

<table>
<tr>
<td width="33%" valign="top">
<a href="styles/orange-type-street-editorial"><img src="assets/thumbs/orange-type-street-editorial-16x9.jpg" alt="Orange Type Street Editorial preview"></a>
<h3>Orange Type Street Editorial</h3>
<p>White-paper street-magazine collage: giant vermilion-orange ultra-condensed type, high-saturation photoreal figures, black headline islands, thin oval callouts and electric-blue hand-drawn marks. The action and the shape of the props drive each case's layout.</p>
<p><a href="styles/orange-type-street-editorial/style.json"><strong>style.json 열기</strong></a> · <a href="docs/copy-prompts/orange-type-street-editorial.md">프롬프트 복사</a> · <a href="styles/orange-type-street-editorial">폴더</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/pixel-weave-editorial"><img src="assets/thumbs/pixel-weave-editorial-16x9.jpg" alt="Pixel Weave Editorial preview"></a>
<h3>Pixel Weave Editorial</h3>
<p>Analog editorial photography meets local square displacement, restless ivory cut lettering and a fine woven print grid. Four content-led reinterpretations explore circular rhythm, bodily motion, an organic spiral and architectural steps.</p>
<p><a href="styles/pixel-weave-editorial/style.json"><strong>style.json 열기</strong></a> · <a href="docs/copy-prompts/pixel-weave-editorial.md">프롬프트 복사</a> · <a href="styles/pixel-weave-editorial">폴더</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/obsidian-signal-motion"><img src="assets/thumbs/obsidian-signal-motion-16x9.jpg" alt="Obsidian Signal Motion preview"></a>
<h3>Obsidian Signal Motion</h3>
<p>Near-black photographic forms against cool white silence, a concentrated ember-orange translucent signal, and horizontally stretched optical afterimages; restrained futuristic editorial typography.</p>
<p><a href="styles/obsidian-signal-motion/style.json"><strong>style.json 열기</strong></a> · <a href="docs/copy-prompts/obsidian-signal-motion.md">프롬프트 복사</a> · <a href="styles/obsidian-signal-motion">폴더</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a href="styles/everyday-riso"><img src="assets/thumbs/everyday-riso-16x9.jpg" alt="Everyday Riso preview"></a>
<h3>Everyday Riso</h3>
<p>Warm, cute everyday-life risograph posters: one chunky rounded person does an ordinary daily action while exactly one object is absurdly oversized, printed in three inks (warm orange, olive green, near-black) on cream paper with misregistration, ink grain, coarse halftone and overprint brown, plus one tiny corner label.</p>
<p><a href="styles/everyday-riso/style.json"><strong>style.json 열기</strong></a> · <a href="docs/copy-prompts/everyday-riso.md">프롬프트 복사</a> · <a href="styles/everyday-riso">폴더</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/chromatic-gesture-characters"><img src="assets/thumbs/chromatic-gesture-characters-16x9.jpg" alt="Chromatic Gesture Characters preview"></a>
<h3>Chromatic Gesture Characters</h3>
<p>Exaggerated geometric character illustration: sculptural color blocks, minimal black cut-paper faces, hot-pink clashes, selectively airbrushed shadows and fine print grain compress emotion and action into a bold poster silhouette.</p>
<p><a href="styles/chromatic-gesture-characters/style.json"><strong>style.json 열기</strong></a> · <a href="docs/copy-prompts/chromatic-gesture-characters.md">프롬프트 복사</a> · <a href="styles/chromatic-gesture-characters">폴더</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/velocity-type-sport"><img src="assets/thumbs/velocity-type-sport-16x9.jpg" alt="Velocity Type Sport preview"></a>
<h3>Velocity Type Sport</h3>
<p>Extreme near-to-far sports photography interlocked with giant white oblique type, a dark vignetted gradient lit by a bright colored haze, and close-up gear or contact points that express each sport's force and direction.</p>
<p><a href="styles/velocity-type-sport/style.json"><strong>style.json 열기</strong></a> · <a href="docs/copy-prompts/velocity-type-sport.md">프롬프트 복사</a> · <a href="styles/velocity-type-sport">폴더</a></p>
</td>
</tr>
</table>
<!-- END GENERATED: featured -->

## 패키지 구조

```text
styles/<style-slug>/
  style.json          # 기계가 읽을 수 있는 프롬프트 스타일 템플릿
  preview-16x9.jpg    # 가로 미리보기
  preview-9x16.jpg    # 세로 미리보기
```

## style.json v2.1 / v2.2

각 `style.json` 은 자체 완결형입니다. 파일 전체를 LLM 에 복사한 뒤 `environment_variables` 에 선언된 변수에 값을 지정하거나 `examples[*].values` 의 사례 값을 수정하면 됩니다.

- `prompt_template` 은 `{VARIABLE}` 플레이스홀더가 있는 재사용 가능한 스타일 프롬프트입니다.
- `environment_variables` 는 템플릿에서 사용할 수 있는 모든 변수를 선언합니다.
- 새 스타일은 `"schema_version": "2.2"`를 가지며 템플릿에서 실제로 쓰는 변수만 선언합니다(예: `SUBJECT`, `MAIN_TEXT`, `DESIGN_DIRECTION`). 이전 v2.1 스타일은 10개의 표준 변수를 사용합니다.
- `examples` 는 바로 수정할 수 있는 사례이며, 각 사례는 `case_name` 과 `values` 만 저장합니다.
- `style_fidelity_anchors` 와 `source_content_to_avoid` 는 유지해야 할 스타일 요소와 복사하면 안 되는 원본 요소를 구분합니다.
- `negative_prompt` 는 워터마크, 로고, 원본 직접 재현, 스타일 이탈을 줄입니다.

`prompt_9x16`, `prompt_16x9`, `full_prompt` 같은 렌더링된 전체 프롬프트는 저장하지 않습니다. 생성 시점에 `prompt_template` 과 선택한 값으로 만들기 때문에 JSON 이 가볍고 오래 유지됩니다.

검증 명령:

```bash
python3 scripts/validate-style-json.py .
```

## All Styles

<!-- BEGIN GENERATED: all-styles (generated by scripts/generate-readme.py from data/catalog.json; do not edit by hand) -->
아래는 최신 9개 스타일입니다. 전체 172개 스타일은 [온라인 갤러리](https://prompts.vigocreativeai.com/site/), 영어 README의 [All Styles](README.md#all-styles), 또는 전체 설명이 있는 [docs/CATALOG.md](docs/CATALOG.md)에서 볼 수 있습니다.

<!-- HTML table used for rich image+link cells -->

<table>
<tr>
<td width="33%" valign="top">
<a id="orange-type-street-editorial"></a>
<a href="styles/orange-type-street-editorial"><img src="assets/thumbs/orange-type-street-editorial-16x9.jpg" alt="Orange Type Street Editorial preview"></a>
<p><strong><a href="styles/orange-type-street-editorial">Orange Type Street Editorial</a></strong><br>
<em>Street-magazine collage on white paper: giant vermilion ultra-condensed type, photoreal figure cutouts, black headline islands, oval callouts and blue marker gestures driven by each action.</em><br>
<a href="styles/orange-type-street-editorial/style.json">style.json</a> · <a href="docs/copy-prompts/orange-type-street-editorial.md">prompt</a> · <a href="styles/orange-type-street-editorial/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="pixel-weave-editorial"></a>
<a href="styles/pixel-weave-editorial"><img src="assets/thumbs/pixel-weave-editorial-16x9.jpg" alt="Pixel Weave Editorial preview"></a>
<p><strong><a href="styles/pixel-weave-editorial">Pixel Weave Editorial</a></strong><br>
<em>Analog editorial photography with local square pixel displacement, restless ivory cut-out lettering and a fine woven print grid across vinyl, motion, citrus and architecture.</em><br>
<a href="styles/pixel-weave-editorial/style.json">style.json</a> · <a href="docs/copy-prompts/pixel-weave-editorial.md">prompt</a> · <a href="styles/pixel-weave-editorial/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="obsidian-signal-motion"></a>
<a href="styles/obsidian-signal-motion"><img src="assets/thumbs/obsidian-signal-motion-16x9.jpg" alt="Obsidian Signal Motion preview"></a>
<p><strong><a href="styles/obsidian-signal-motion">Obsidian Signal Motion</a></strong><br>
<em>Near-black photographic forms on cool white silence, one ember-orange translucent signal and stretched optical afterimages, set in restrained futuristic editorial type.</em><br>
<a href="styles/obsidian-signal-motion/style.json">style.json</a> · <a href="docs/copy-prompts/obsidian-signal-motion.md">prompt</a> · <a href="styles/obsidian-signal-motion/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="everyday-riso"></a>
<a id="everyday-riso-part-02"></a>
<a id="everyday-riso-part-03"></a>
<a id="everyday-riso-part-04"></a>
<a href="styles/everyday-riso"><img src="assets/thumbs/everyday-riso-16x9.jpg" alt="Everyday Riso preview"></a>
<p><strong><a href="styles/everyday-riso">Everyday Riso</a></strong><br>
<em>Three-ink risograph posters of one chunky rounded person doing a daily routine with exactly one absurdly oversized object, misregistration, halftone grain and a tiny corner label.</em><br>
<a href="styles/everyday-riso/style.json">style.json</a> · <a href="docs/copy-prompts/everyday-riso.md">prompt</a> · <a href="styles/everyday-riso/preview-9x16.jpg">9:16</a></p>
<p>시리즈: <a href="styles/everyday-riso-part-02">Part 2</a> · <a href="styles/everyday-riso-part-03">Part 3</a> · <a href="styles/everyday-riso-part-04">Part 4</a></p>
</td>
<td width="33%" valign="top">
<a id="chromatic-gesture-characters"></a>
<a id="chromatic-gesture-characters-part-02"></a>
<a id="chromatic-gesture-characters-part-03"></a>
<a id="chromatic-gesture-characters-part-04"></a>
<a id="chromatic-gesture-characters-part-05"></a>
<a id="chromatic-gesture-characters-part-06"></a>
<a id="chromatic-gesture-characters-part-07"></a>
<a href="styles/chromatic-gesture-characters"><img src="assets/thumbs/chromatic-gesture-characters-16x9.jpg" alt="Chromatic Gesture Characters preview"></a>
<p><strong><a href="styles/chromatic-gesture-characters">Chromatic Gesture Characters</a></strong><br>
<em>Exaggerated geometric character posters with sculptural color blocks, minimal black faces, hot-pink clashes, airbrushed shadows and fine print grain.</em><br>
<a href="styles/chromatic-gesture-characters/style.json">style.json</a> · <a href="docs/copy-prompts/chromatic-gesture-characters.md">prompt</a> · <a href="styles/chromatic-gesture-characters/preview-9x16.jpg">9:16</a></p>
<p>시리즈: <a href="styles/chromatic-gesture-characters-part-02">Part 2</a> · <a href="styles/chromatic-gesture-characters-part-03">Part 3</a> · <a href="styles/chromatic-gesture-characters-part-04">Part 4</a> · <a href="styles/chromatic-gesture-characters-part-05">Part 5</a> · <a href="styles/chromatic-gesture-characters-part-06">Part 6</a> · <a href="styles/chromatic-gesture-characters-part-07">Part 7</a></p>
</td>
<td width="33%" valign="top">
<a id="velocity-type-sport"></a>
<a id="velocity-type-sport-part-02"></a>
<a id="velocity-type-sport-part-03"></a>
<a id="velocity-type-sport-part-04"></a>
<a href="styles/velocity-type-sport"><img src="assets/thumbs/velocity-type-sport-16x9.jpg" alt="Velocity Type Sport preview"></a>
<p><strong><a href="styles/velocity-type-sport">Velocity Type Sport</a></strong><br>
<em>Extreme-perspective sports photos woven through giant white oblique type, with a bright color haze in a dark field.</em><br>
<a href="styles/velocity-type-sport/style.json">style.json</a> · <a href="docs/copy-prompts/velocity-type-sport.md">prompt</a> · <a href="styles/velocity-type-sport/preview-9x16.jpg">9:16</a></p>
<p>시리즈: <a href="styles/velocity-type-sport-part-02">Part 2</a> · <a href="styles/velocity-type-sport-part-03">Part 3</a> · <a href="styles/velocity-type-sport-part-04">Part 4</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="acid-jolt-photo-collage"></a>
<a href="styles/acid-jolt-photo-collage"><img src="assets/thumbs/acid-jolt-photo-collage-16x9.jpg" alt="Acid Jolt Portrait Collage preview"></a>
<p><strong><a href="styles/acid-jolt-photo-collage">Acid Jolt Portrait Collage</a></strong><br>
<em>Punchy portrait posters mixing warm low-fi close-ups, blunt photo fragments, massive lemon-yellow lettering, and loose marker signals.</em><br>
<a href="styles/acid-jolt-photo-collage/style.json">style.json</a> · <a href="docs/copy-prompts/acid-jolt-photo-collage.md">prompt</a> · <a href="styles/acid-jolt-photo-collage/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="amber-orbit-editorial"></a>
<a href="styles/amber-orbit-editorial"><img src="assets/thumbs/amber-orbit-editorial-16x9.jpg" alt="Amber Orbit Editorial preview"></a>
<p><strong><a href="styles/amber-orbit-editorial">Amber Orbit Editorial</a></strong><br>
<em>Warm amber macros with ivory serif type and fine orbital lines, turning tactile details into quiet editorial stories.</em><br>
<a href="styles/amber-orbit-editorial/style.json">style.json</a> · <a href="docs/copy-prompts/amber-orbit-editorial.md">prompt</a> · <a href="styles/amber-orbit-editorial/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="felt-motion-brand-campaign"></a>
<a id="felt-motion-brand-campaign-set-02"></a>
<a href="styles/felt-motion-brand-campaign"><img src="assets/thumbs/felt-motion-brand-campaign-16x9.jpg" alt="Felt Motion Brand Campaign preview"></a>
<p><strong><a href="styles/felt-motion-brand-campaign">Felt Motion Brand Campaign</a></strong><br>
<em>Intimate sports photographs with moody warm light, selective focus, and a white original logo plus two-line wordmark at center.</em><br>
<a href="styles/felt-motion-brand-campaign/style.json">style.json</a> · <a href="docs/copy-prompts/felt-motion-brand-campaign.md">prompt</a> · <a href="styles/felt-motion-brand-campaign/preview-9x16.jpg">9:16</a></p>
<p>시리즈: <a href="styles/felt-motion-brand-campaign-set-02">Set 2</a></p>
</td>
</tr>
</table>
<!-- END GENERATED: all-styles -->

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
