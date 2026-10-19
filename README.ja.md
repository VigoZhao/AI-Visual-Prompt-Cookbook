<h1 align="center">AI Visual Prompt Cookbook</h1>

<p align="center">
  <img src="assets/hero-collage.jpg" alt="AI Visual Prompt Cookbook showcase">
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.zh-TW.md">繁體中文</a> |
  日本語 |
  <a href="README.ko.md">한국어</a> |
  <a href="README.id.md">Bahasa Indonesia</a>
</p>

<p align="center">
  <img alt="Styles" src="https://img.shields.io/badge/styles-172-ff5a7a?style=flat-square">
  <img alt="Previews" src="https://img.shields.io/badge/previews-344-4cc9f0?style=flat-square">
  <img alt="Format" src="https://img.shields.io/badge/format-style.json-111111?style=flat-square">
  <img alt="Languages" src="https://img.shields.io/badge/languages-6-f7b801?style=flat-square">
</p>

<p align="center">
  <strong>JSON をコピーすれば、ひとつのスタイルが手に入ります。</strong> <code>style.json</code> を ChatGPT、Claude、Nano Banana Pro、または任意の LLM 画像生成ワークフローに入れ、変数だけを差し替えれば、視覚システムを保ったまま使えます。
</p>

<p align="center">
  AI 画像生成向けの、すぐ使えるビジュアルプロンプトスタイル集です。各スタイルは再利用しやすい <code>style.json</code> と、横長・縦長のプレビュー画像で整理されています。
</p>

<p align="center">
  Curated by <a href="https://x.com/VigoCreativeAI">@VigoCreativeAI</a>, structured with assistance from OpenAI Codex. 新しいスタイルを追うには、このリポジトリを Star してください。
</p>

<p align="center">
  🖼️ <strong><a href="https://prompts.vigocreativeai.com/site/">オンラインギャラリー</a></strong> · または下の <a href="#all-styles">All Styles ギャラリー</a> / <a href="docs/CATALOG.md">完全なカタログ</a> をご覧ください。
</p>

<p align="center">
  💬 スタイルで作品を作ったら <a href="https://github.com/VigoZhao/AI-Visual-Prompt-Cookbook/discussions/categories/show-and-tell">Show and tell でシェア</a> · 欲しいスタイルがなければ <a href="https://github.com/VigoZhao/AI-Visual-Prompt-Cookbook/discussions/categories/ideas">リクエストする</a>
</p>

## クイックリンク

| カテゴリ | 向いている用途 | まず見るスタイル |
| --- | --- | --- |
| 写真 + ドゥードル | SNS風スナップ、ライフスタイル写真、遊びのあるステッカー表現 | [Playful Mascot Doodle Snapshot](styles/playful-mascot-doodle-snapshot-style), [Subway Doodle Photo Hybrid](styles/subway-doodle-photo-hybrid-style) |
| Zine + コラージュ | ファッションポスター、音楽ビジュアル、情報量の多いエディトリアル | [K-pop Apocalypse Ransom Zine](styles/k-pop-apocalypse-ransom-zine-style), [Y2K Grunge Hip-hop Cutout Poster](styles/y2k-grunge-hiphop-cutout-poster-style) |
| タイポグラフィポスター | 大きな見出し、強いキャンペーングラフィック、視覚インパクト | [Impact Burst Halftone Comic Poster](styles/impact-burst-halftone-comic-poster-style), [Neon Kinetic Typographic Poster](styles/neon-kinetic-typographic-poster-style) |
| 旅 + 都市 | 目的地ポスター、ストリートシーン、都市のビジュアル日記 | [Clean Triptych Travel Vlog Thumbnail](styles/clean-triptych-travel-vlog-thumbnail-style), [Tokyo Kawaii Travel Collage Poster](styles/tokyo-kawaii-travel-collage-poster-style) |
| エディトリアル + ミニマル | すっきりした構図、構造的なレイアウト、落ち着いたアートディレクション | [Tri Color Hardcut Portrait Poster](styles/tri-color-hardcut-portrait-poster-style), [Soft Analog Future Editorial Poster](styles/soft-analog-future-editorial-poster-style) |

## このプロジェクトについて

多くの AI 画像プロンプトは一回限りの文章になりがちで、再利用や比較、安定した改善が難しいものです。このリポジトリでは、各ビジュアルスタイルを構造化された `style.json` に分解しています。テーマを変えても、同じスタイル構造を保ったまま生成を続けられます。

## 使い方

1. [注目スタイル](#注目スタイル)、[クイックリンク](#クイックリンク)、または [All Styles](#all-styles) を見る。
2. 気になるスタイルのフォルダを開き、`style.json` をコピーする。
3. JSON 全体を ChatGPT Images 2、Nano Banana Pro、または他のエンドツーエンドのマルチモーダル画像モデルに貼り付ける。
4. `environment_variables` で宣言された変数に自分の値を指定するか、`examples[*].values` のケースを編集する。
5. 最終画像を生成する。

完全な入力から出力までの流れは、下の [Complete Example](#complete-example) を参照してください。

### Recommended Image Models

このワークフローは、長い構造化 JSON プロンプトを読み取り、最終画像を一段階で生成できるエンドツーエンドのマルチモーダル画像モデルで最もよく機能します。

- ChatGPT Images 2 (OpenAI, gpt-image-2) — テキスト描画が強く、2K/4K 出力に対応し、生成前の推論が可能
- Nano Banana Pro (Google, Gemini 3 Pro Image) — 4K 出力、多言語テキスト精度、強い被写体一貫性

長い JSON プロンプトを受け取れる他のマルチモーダル LLM でも動作する場合がありますが、主な推奨対象ではありません。

## Complete Example

### 入力 → 出力ウォークスルー

この例では [Mono Noir Type Portrait Poster Style](styles/mono-noir-type-portrait-poster-style/) を使います。

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

まず短い入口から試したい場合は、自動生成された [Copy Prompt Library](docs/copy-prompts/README.md) を開いてください。各スタイルに、そのままコピーできる簡易プロンプトがあります。完全な再利用用スタイルシステムは、引き続き各 `style.json` にあります。

## 注目スタイル

<!-- BEGIN GENERATED: featured (generated by scripts/generate-readme.py from data/catalog.json; do not edit by hand) -->
まずこの 6 つを見ると、ライブラリの幅がわかります。すべてのスタイルは 1 つの JSON と 2 枚のプレビュー画像で構成されています。172 種すべては[オンラインギャラリー](https://prompts.vigocreativeai.com/site/)または英語版 README の [All Styles](README.md#all-styles) で確認できます。

<!-- HTML table used for rich image+link cells -->

<table>
<tr>
<td width="33%" valign="top">
<a href="styles/orange-type-street-editorial"><img src="assets/thumbs/orange-type-street-editorial-16x9.jpg" alt="Orange Type Street Editorial preview"></a>
<h3>Orange Type Street Editorial</h3>
<p>White-paper street-magazine collage: giant vermilion-orange ultra-condensed type, high-saturation photoreal figures, black headline islands, thin oval callouts and electric-blue hand-drawn marks. The action and the shape of the props drive each case's layout.</p>
<p><a href="styles/orange-type-street-editorial/style.json"><strong>style.json を開く</strong></a> · <a href="docs/copy-prompts/orange-type-street-editorial.md">プロンプトをコピー</a> · <a href="styles/orange-type-street-editorial">フォルダ</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/pixel-weave-editorial"><img src="assets/thumbs/pixel-weave-editorial-16x9.jpg" alt="Pixel Weave Editorial preview"></a>
<h3>Pixel Weave Editorial</h3>
<p>Analog editorial photography meets local square displacement, restless ivory cut lettering and a fine woven print grid. Four content-led reinterpretations explore circular rhythm, bodily motion, an organic spiral and architectural steps.</p>
<p><a href="styles/pixel-weave-editorial/style.json"><strong>style.json を開く</strong></a> · <a href="docs/copy-prompts/pixel-weave-editorial.md">プロンプトをコピー</a> · <a href="styles/pixel-weave-editorial">フォルダ</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/obsidian-signal-motion"><img src="assets/thumbs/obsidian-signal-motion-16x9.jpg" alt="Obsidian Signal Motion preview"></a>
<h3>Obsidian Signal Motion</h3>
<p>Near-black photographic forms against cool white silence, a concentrated ember-orange translucent signal, and horizontally stretched optical afterimages; restrained futuristic editorial typography.</p>
<p><a href="styles/obsidian-signal-motion/style.json"><strong>style.json を開く</strong></a> · <a href="docs/copy-prompts/obsidian-signal-motion.md">プロンプトをコピー</a> · <a href="styles/obsidian-signal-motion">フォルダ</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a href="styles/everyday-riso"><img src="assets/thumbs/everyday-riso-16x9.jpg" alt="Everyday Riso preview"></a>
<h3>Everyday Riso</h3>
<p>Warm, cute everyday-life risograph posters: one chunky rounded person does an ordinary daily action while exactly one object is absurdly oversized, printed in three inks (warm orange, olive green, near-black) on cream paper with misregistration, ink grain, coarse halftone and overprint brown, plus one tiny corner label.</p>
<p><a href="styles/everyday-riso/style.json"><strong>style.json を開く</strong></a> · <a href="docs/copy-prompts/everyday-riso.md">プロンプトをコピー</a> · <a href="styles/everyday-riso">フォルダ</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/chromatic-gesture-characters"><img src="assets/thumbs/chromatic-gesture-characters-16x9.jpg" alt="Chromatic Gesture Characters preview"></a>
<h3>Chromatic Gesture Characters</h3>
<p>Exaggerated geometric character illustration: sculptural color blocks, minimal black cut-paper faces, hot-pink clashes, selectively airbrushed shadows and fine print grain compress emotion and action into a bold poster silhouette.</p>
<p><a href="styles/chromatic-gesture-characters/style.json"><strong>style.json を開く</strong></a> · <a href="docs/copy-prompts/chromatic-gesture-characters.md">プロンプトをコピー</a> · <a href="styles/chromatic-gesture-characters">フォルダ</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/velocity-type-sport"><img src="assets/thumbs/velocity-type-sport-16x9.jpg" alt="Velocity Type Sport preview"></a>
<h3>Velocity Type Sport</h3>
<p>Extreme near-to-far sports photography interlocked with giant white oblique type, a dark vignetted gradient lit by a bright colored haze, and close-up gear or contact points that express each sport's force and direction.</p>
<p><a href="styles/velocity-type-sport/style.json"><strong>style.json を開く</strong></a> · <a href="docs/copy-prompts/velocity-type-sport.md">プロンプトをコピー</a> · <a href="styles/velocity-type-sport">フォルダ</a></p>
</td>
</tr>
</table>
<!-- END GENERATED: featured -->

## パッケージ構成

```text
styles/<style-slug>/
  style.json          # 機械可読のプロンプトスタイルテンプレート
  preview-16x9.jpg    # 横長プレビュー
  preview-9x16.jpg    # 縦長プレビュー
```

## style.json v2.1 / v2.2

各 `style.json` は自己完結しています。ファイル全体を LLM にコピーし、`environment_variables` で宣言された変数に値を指定するか、`examples[*].values` のケースを編集して使います。

- `prompt_template` は `{VARIABLE}` プレースホルダーを持つ再利用可能なスタイルプロンプトです。
- `environment_variables` はテンプレートで使えるすべての変数を宣言します。
- 新しいスタイルは `"schema_version": "2.2"` を持ち、テンプレートで実際に使う変数だけを宣言します（例：`SUBJECT`、`MAIN_TEXT`、`DESIGN_DIRECTION`）。以前の v2.1 スタイルは 10 個の標準変数を使います。
- `examples` は編集しやすいケース集で、各ケースは `case_name` と `values` だけを持ちます。
- `style_fidelity_anchors` と `source_content_to_avoid` は、保つべきスタイル要素とコピーしてはいけない元内容を分けます。
- `negative_prompt` はウォーターマーク、ロゴ、元画像の直接再現、スタイル外れを避けるために使います。

`prompt_9x16`、`prompt_16x9`、`full_prompt` のようなレンダリング済みプロンプトは保存しません。生成時に `prompt_template` と選んだ値から作るため、JSON は軽く、古くなりにくくなります。

検証コマンド：

```bash
python3 scripts/validate-style-json.py .
```

## All Styles

<!-- BEGIN GENERATED: all-styles (generated by scripts/generate-readme.py from data/catalog.json; do not edit by hand) -->
最新の 9 スタイルを下に掲載しています。全 172 スタイルは[オンラインギャラリー](https://prompts.vigocreativeai.com/site/)、英語版 README の [All Styles](README.md#all-styles)、または詳細説明付きの [docs/CATALOG.md](docs/CATALOG.md) をご覧ください。

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
<p>シリーズ：<a href="styles/everyday-riso-part-02">Part 2</a> · <a href="styles/everyday-riso-part-03">Part 3</a> · <a href="styles/everyday-riso-part-04">Part 4</a></p>
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
<p>シリーズ：<a href="styles/chromatic-gesture-characters-part-02">Part 2</a> · <a href="styles/chromatic-gesture-characters-part-03">Part 3</a> · <a href="styles/chromatic-gesture-characters-part-04">Part 4</a> · <a href="styles/chromatic-gesture-characters-part-05">Part 5</a> · <a href="styles/chromatic-gesture-characters-part-06">Part 6</a> · <a href="styles/chromatic-gesture-characters-part-07">Part 7</a></p>
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
<p>シリーズ：<a href="styles/velocity-type-sport-part-02">Part 2</a> · <a href="styles/velocity-type-sport-part-03">Part 3</a> · <a href="styles/velocity-type-sport-part-04">Part 4</a></p>
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
<p>シリーズ：<a href="styles/felt-motion-brand-campaign-set-02">Set 2</a></p>
</td>
</tr>
</table>
<!-- END GENERATED: all-styles -->

## 公開方針

- 1 つのディレクトリ = 1 つのスタイル
- 新しいスタイルは注目スタイルと All Styles ギャラリーに先に表示し、詳しい説明は [docs/CATALOG.md](docs/CATALOG.md) に追加します
- main ブランチには各スタイルの `style.json` と 2 枚の JPG プレビューのみを配置します
- 完全なギャラリーはこのリポジトリには含めません
- 元の参考画像、透かし、プラットフォームロゴ、QR コード、アカウント情報、非公開プロンプト、未許可のブランド素材は公開しません

## Contributing

新しいスタイルを投稿する場合は、[CONTRIBUTING.md](CONTRIBUTING.md) の公開パッケージ構成、検証ルール、PR checklist に従ってください。

## ライセンス

コード、スクリプト、ドキュメントは [MIT ライセンス](LICENSE) です。`style.json` のプロンプト内容は [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) でライセンスされています——[@VigoCreativeAI](https://x.com/VigoCreativeAI) のクレジット表記のうえ、自由に再利用・改変できます。プレビュー画像は視覚参照として含まれています。
