<h1 align="center">AI Visual Prompt Cookbook</h1>

<p align="center">
  <img src="assets/hero-collage.jpg" alt="AI Visual Prompt Cookbook 風格展示">
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="README.zh-CN.md">简体中文</a> |
  繁體中文 |
  <a href="README.ja.md">日本語</a> |
  <a href="README.ko.md">한국어</a> |
  <a href="README.id.md">Bahasa Indonesia</a>
</p>

<p align="center">
  <img alt="風格數量" src="https://img.shields.io/badge/styles-172-ff5a7a?style=flat-square">
  <img alt="預覽圖" src="https://img.shields.io/badge/previews-344-4cc9f0?style=flat-square">
  <img alt="格式" src="https://img.shields.io/badge/format-style.json-111111?style=flat-square">
  <img alt="語言" src="https://img.shields.io/badge/languages-6-f7b801?style=flat-square">
</p>

<p align="center">
  <strong>複製一個 JSON，得到一種風格。</strong> 把一個 <code>style.json</code> 放進 ChatGPT、Claude、Nano Banana Pro、即夢或其他 LLM 圖像工作流，替換變數，保留完整視覺系統。
</p>

<p align="center">
  這是一個面向 AI 圖像生成的可重用視覺提示詞風格庫：每個風格都整理成可直接使用的 <code>style.json</code>，並配套橫向與直向預覽圖，方便瀏覽、複製和二次生成。
</p>

<p align="center">
  由 <a href="https://x.com/VigoCreativeAI">@VigoCreativeAI</a> 策劃整理，並在 OpenAI Codex 協助下結構化。Star 這個倉庫即可追蹤新的風格更新。
</p>

<p align="center">
  🖼️ <strong><a href="https://prompts.vigocreativeai.com/site/">線上畫廊</a></strong> · 或瀏覽下方 <a href="#all-styles">All Styles 畫廊</a> / <a href="docs/CATALOG.md">完整目錄</a>。
</p>

<p align="center">
  💬 用這裡的風格做了圖？<a href="https://github.com/VigoZhao/AI-Visual-Prompt-Cookbook/discussions/categories/show-and-tell">來 Show and tell 曬一曬</a> · 想要還沒有的風格？<a href="https://github.com/VigoZhao/AI-Visual-Prompt-Cookbook/discussions/categories/ideas">在這裡許願</a>
</p>

## 快速入口

| 分類 | 適合做什麼 | 先看這些 |
| --- | --- | --- |
| 照片 + 塗鴉 | 社交隨拍、生活方式場景、輕快貼紙覆蓋層 | [Playful Mascot Doodle Snapshot](styles/playful-mascot-doodle-snapshot-style), [Subway Doodle Photo Hybrid](styles/subway-doodle-photo-hybrid-style) |
| Zine + 拼貼 | 時尚海報、音樂視覺、極繁編輯版式 | [K-pop Apocalypse Ransom Zine](styles/k-pop-apocalypse-ransom-zine-style), [Y2K Grunge Hip-hop Cutout Poster](styles/y2k-grunge-hiphop-cutout-poster-style) |
| 字體海報 | 大標題系統、高衝擊廣告圖、強烈視覺識別 | [Impact Burst Halftone Comic Poster](styles/impact-burst-halftone-comic-poster-style), [Neon Kinetic Typographic Poster](styles/neon-kinetic-typographic-poster-style) |
| 旅行 + 城市 | 目的地海報、街頭場景、城市視覺日記 | [Clean Triptych Travel Vlog Thumbnail](styles/clean-triptych-travel-vlog-thumbnail-style), [Tokyo Kawaii Travel Collage Poster](styles/tokyo-kawaii-travel-collage-poster-style) |
| 編輯 + 極簡 | 更乾淨的構圖、結構化版面、安靜的藝術指導 | [Tri Color Hardcut Portrait Poster](styles/tri-color-hardcut-portrait-poster-style), [Soft Analog Future Editorial Poster](styles/soft-analog-future-editorial-poster-style) |

## 為什麼做這個項目

多數 AI 圖像提示詞都是一次性的文字塊：難以重用、難以比較，也難以穩定迭代。這個項目採用另一種方式：把每一種視覺風格拆解成結構化的 `style.json`，你可以把它放進 ChatGPT、Claude 或其他 LLM 圖像生成流程中。換主題時，風格結構仍然保持穩定。

## 快速開始

1. 瀏覽 [精選風格](#精選風格)、[快速入口](#快速入口) 或 [All Styles](#all-styles)。
2. 打開某個風格目錄，複製裡面的 `style.json`。
3. 把完整 JSON 放進 ChatGPT Images 2、Nano Banana Pro 或其他端到端多模態圖像模型。
4. 根據 `environment_variables` 裡的變數說明填寫你的變數值，或直接修改 `examples[*].values` 裡的案例值。
5. 生成最終圖像。

參見下面的 [Complete Example](#complete-example)，查看完整的輸入到輸出示例。

### Recommended Image Models

這個工作流最適合端到端多模態圖像模型：它們能讀取較長的結構化 JSON 提示詞，並一步生成最終圖像。

- ChatGPT Images 2 (OpenAI, gpt-image-2) — 文字渲染強，支援 2K/4K 輸出，可在生成前進行推理
- Nano Banana Pro (Google, Gemini 3 Pro Image) — 支援 4K 輸出，多語言文字準確性好，主體一致性強

其他能接受長 JSON 提示詞的多模態 LLM 也可能可用，但不是主要推薦。

## Complete Example

### 輸入 → 輸出演示

這個示例使用 [Mono Noir Type Portrait Poster Style](styles/mono-noir-type-portrait-poster-style/)。

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

## 複製提示詞入口

想先快速試效果？可以打開自動生成的 [Copy Prompt Library](docs/copy-prompts/README.md)，每個風格都有一段可直接複製的簡版提示詞。完整可重用風格系統仍然保留在各自的 `style.json` 裡。

## 精選風格

<!-- BEGIN GENERATED: featured (generated by scripts/generate-readme.py from data/catalog.json; do not edit by hand) -->
先看這 6 個風格。每個風格都保持輕量：一個 JSON 加兩張預覽圖。完整 172 個風格見[線上畫廊](https://prompts.vigocreativeai.com/site/)或英文 README 的 [All Styles](README.md#all-styles)。

<!-- HTML table used for rich image+link cells -->

<table>
<tr>
<td width="33%" valign="top">
<a href="styles/orange-type-street-editorial"><img src="assets/thumbs/orange-type-street-editorial-16x9.jpg" alt="Orange Type Street Editorial preview"></a>
<h3>Orange Type Street Editorial</h3>
<p>White-paper street-magazine collage: giant vermilion-orange ultra-condensed type, high-saturation photoreal figures, black headline islands, thin oval callouts and electric-blue hand-drawn marks. The action and the shape of the props drive each case's layout.</p>
<p><a href="styles/orange-type-street-editorial/style.json"><strong>打開 style.json</strong></a> · <a href="docs/copy-prompts/orange-type-street-editorial.md">複製提示詞</a> · <a href="styles/orange-type-street-editorial">目錄</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/pixel-weave-editorial"><img src="assets/thumbs/pixel-weave-editorial-16x9.jpg" alt="Pixel Weave Editorial preview"></a>
<h3>Pixel Weave Editorial</h3>
<p>Analog editorial photography meets local square displacement, restless ivory cut lettering and a fine woven print grid. Four content-led reinterpretations explore circular rhythm, bodily motion, an organic spiral and architectural steps.</p>
<p><a href="styles/pixel-weave-editorial/style.json"><strong>打開 style.json</strong></a> · <a href="docs/copy-prompts/pixel-weave-editorial.md">複製提示詞</a> · <a href="styles/pixel-weave-editorial">目錄</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/obsidian-signal-motion"><img src="assets/thumbs/obsidian-signal-motion-16x9.jpg" alt="Obsidian Signal Motion preview"></a>
<h3>Obsidian Signal Motion</h3>
<p>Near-black photographic forms against cool white silence, a concentrated ember-orange translucent signal, and horizontally stretched optical afterimages; restrained futuristic editorial typography.</p>
<p><a href="styles/obsidian-signal-motion/style.json"><strong>打開 style.json</strong></a> · <a href="docs/copy-prompts/obsidian-signal-motion.md">複製提示詞</a> · <a href="styles/obsidian-signal-motion">目錄</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a href="styles/everyday-riso"><img src="assets/thumbs/everyday-riso-16x9.jpg" alt="Everyday Riso preview"></a>
<h3>Everyday Riso</h3>
<p>Warm, cute everyday-life risograph posters: one chunky rounded person does an ordinary daily action while exactly one object is absurdly oversized, printed in three inks (warm orange, olive green, near-black) on cream paper with misregistration, ink grain, coarse halftone and overprint brown, plus one tiny corner label.</p>
<p><a href="styles/everyday-riso/style.json"><strong>打開 style.json</strong></a> · <a href="docs/copy-prompts/everyday-riso.md">複製提示詞</a> · <a href="styles/everyday-riso">目錄</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/chromatic-gesture-characters"><img src="assets/thumbs/chromatic-gesture-characters-16x9.jpg" alt="Chromatic Gesture Characters preview"></a>
<h3>Chromatic Gesture Characters</h3>
<p>Exaggerated geometric character illustration: sculptural color blocks, minimal black cut-paper faces, hot-pink clashes, selectively airbrushed shadows and fine print grain compress emotion and action into a bold poster silhouette.</p>
<p><a href="styles/chromatic-gesture-characters/style.json"><strong>打開 style.json</strong></a> · <a href="docs/copy-prompts/chromatic-gesture-characters.md">複製提示詞</a> · <a href="styles/chromatic-gesture-characters">目錄</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/velocity-type-sport"><img src="assets/thumbs/velocity-type-sport-16x9.jpg" alt="Velocity Type Sport preview"></a>
<h3>Velocity Type Sport</h3>
<p>Extreme near-to-far sports photography interlocked with giant white oblique type, a dark vignetted gradient lit by a bright colored haze, and close-up gear or contact points that express each sport's force and direction.</p>
<p><a href="styles/velocity-type-sport/style.json"><strong>打開 style.json</strong></a> · <a href="docs/copy-prompts/velocity-type-sport.md">複製提示詞</a> · <a href="styles/velocity-type-sport">目錄</a></p>
</td>
</tr>
</table>
<!-- END GENERATED: featured -->

## 文件結構

```text
styles/<style-slug>/
  style.json          # 機器可讀的提示詞風格模板
  preview-16x9.jpg    # 橫向預覽圖
  preview-9x16.jpg    # 直向預覽圖
```

## style.json v2.1 / v2.2

每個 `style.json` 都是自包含的：把完整文件複製給 LLM，然後根據 `environment_variables` 的變數說明填寫新值，或直接改寫某個 `examples[*].values` 案例。

- `prompt_template` 是帶 `{VARIABLE}` 佔位符的可重用風格提示詞。
- `environment_variables` 聲明模板裡可使用的所有變數。
- 較新的風格帶有 `"schema_version": "2.2"`，只宣告模板真正用到的變數（如 `SUBJECT`、`MAIN_TEXT`、`DESIGN_DIRECTION`）；較早的 v2.1 風格使用固定的 10 個標準變數。
- `examples` 提供可直接改寫的案例；每個案例只包含 `case_name` 和 `values`。
- `style_fidelity_anchors` 和 `source_content_to_avoid` 分別說明要保留的風格錨點，以及不能複製的源內容。
- `negative_prompt` 用來排除水印、Logo、直接複刻源圖和偏離風格的輸出。

倉庫不會保存 `prompt_9x16`、`prompt_16x9` 或 `full_prompt` 這類渲染後的完整提示詞。它們可以在生成時由 `prompt_template` 和變數值臨時推導出來，讓 JSON 更輕，也不容易過期。

校驗命令：

```bash
python3 scripts/validate-style-json.py .
```

## All Styles

<!-- BEGIN GENERATED: all-styles (generated by scripts/generate-readme.py from data/catalog.json; do not edit by hand) -->
下面是最新的 9 個風格。全部 172 個風格請看[線上畫廊](https://prompts.vigocreativeai.com/site/)、英文 README 的 [All Styles](README.md#all-styles)，或帶完整描述的 [docs/CATALOG.md](docs/CATALOG.md)。

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
<p>系列：<a href="styles/everyday-riso-part-02">Part 2</a> · <a href="styles/everyday-riso-part-03">Part 3</a> · <a href="styles/everyday-riso-part-04">Part 4</a></p>
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
<p>系列：<a href="styles/chromatic-gesture-characters-part-02">Part 2</a> · <a href="styles/chromatic-gesture-characters-part-03">Part 3</a> · <a href="styles/chromatic-gesture-characters-part-04">Part 4</a> · <a href="styles/chromatic-gesture-characters-part-05">Part 5</a> · <a href="styles/chromatic-gesture-characters-part-06">Part 6</a> · <a href="styles/chromatic-gesture-characters-part-07">Part 7</a></p>
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
<p>系列：<a href="styles/velocity-type-sport-part-02">Part 2</a> · <a href="styles/velocity-type-sport-part-03">Part 3</a> · <a href="styles/velocity-type-sport-part-04">Part 4</a></p>
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
<p>系列：<a href="styles/felt-motion-brand-campaign-set-02">Set 2</a></p>
</td>
</tr>
</table>
<!-- END GENERATED: all-styles -->

## 發布規則

- 一個目錄 = 一種風格
- 新風格會優先出現在精選風格和 All Styles 畫廊中，完整描述同步添加到 [docs/CATALOG.md](docs/CATALOG.md)
- main 分支只放每個風格的 `style.json` 和兩張預覽 JPG
- 完整圖庫不放在這個倉庫中
- 不發布原始參考圖、水印圖、平台標識、QR code、帳號資訊、私有提示詞，或未經授權的品牌素材

## Contributing

提交新風格時，請遵循 [CONTRIBUTING.md](CONTRIBUTING.md) 中的公開包結構、校驗規則和 PR checklist。

## 授權

程式碼、腳本和文件採用 [MIT 授權](LICENSE)。`style.json` 的提示詞內容採用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授權——歡迎註明出處 [@VigoCreativeAI](https://x.com/VigoCreativeAI) 後複用和改編。預覽圖僅作為視覺參考隨倉庫展示。
