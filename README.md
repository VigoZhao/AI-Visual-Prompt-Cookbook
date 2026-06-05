<h1 align="center">AI Visual Prompt Cookbook</h1>

<p align="center">
  <img src="assets/hero-collage.jpg" alt="AI Visual Prompt Cookbook showcase">
</p>

<p align="center">
  English |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.zh-TW.md">繁體中文</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.ko.md">한국어</a> |
  <a href="README.id.md">Bahasa Indonesia</a>
</p>

<p align="center">
  <img alt="Styles" src="https://img.shields.io/badge/styles-58-ff5a7a?style=flat-square">
  <img alt="Previews" src="https://img.shields.io/badge/previews-116-4cc9f0?style=flat-square">
  <img alt="Format" src="https://img.shields.io/badge/format-style.json-111111?style=flat-square">
  <img alt="Languages" src="https://img.shields.io/badge/languages-6-f7b801?style=flat-square">
</p>

<p align="center">
  <strong>Copy a JSON, get a style.</strong> Drop one <code>style.json</code> into ChatGPT, Claude, Nano Banana Pro, or any LLM image workflow. Replace the variables, keep the visual system.
</p>

<p align="center">
  A curated library of plug-and-play visual prompt styles for AI image generation, distilled from visual design references and structured for more consistent, reusable output.
</p>

<p align="center">
  Curated by <a href="https://x.com/VigoCreativeAI">@VigoCreativeAI</a>, structured with assistance from OpenAI Codex. Star this repo to follow new style drops.
</p>

<p align="center">
  Browse the <a href="#all-styles">All Styles gallery</a> or open the <a href="docs/CATALOG.md">full catalog</a>.
</p>

## Quick Links

| Category | Good for | Start with |
| --- | --- | --- |
| Photo + Doodle | Social snapshots, lifestyle scenes, playful overlays | [Playful Mascot Doodle Snapshot](#playful-mascot-doodle-snapshot-style), [Subway Doodle Photo Hybrid](#subway-doodle-photo-hybrid-style) |
| Zine + Collage | Fashion posters, music visuals, maximalist editorial layouts | [K-pop Apocalypse Ransom Zine](#k-pop-apocalypse-ransom-zine-style), [Y2K Grunge Hip-hop Cutout Poster](#y2k-grunge-hiphop-cutout-poster-style) |
| Type Posters | Big headline systems, loud campaign graphics, visual punch | [Impact Burst Halftone Comic Poster](#impact-burst-halftone-comic-poster-style), [Neon Kinetic Typographic Poster](#neon-kinetic-typographic-poster-style) |
| Travel + City | Destination posters, street scenes, urban diaries | [Clean Triptych Travel Vlog Thumbnail](#clean-triptych-travel-vlog-thumbnail-style), [Tokyo Kawaii Travel Collage Poster](#tokyo-kawaii-travel-collage-poster-style) |
| Editorial + Minimal | Cleaner compositions, structured layouts, quieter art direction | [Tri Color Hardcut Portrait Poster](#tri-color-hardcut-portrait-poster-style), [Soft Analog Future Editorial Poster](#soft-analog-future-editorial-poster-style) |

## Why This Exists

Most AI image prompts are one-off text blobs: hard to reuse, hard to compare, and hard to iterate on. This repo takes a different approach: each visual style is distilled into a structured `style.json` you can drop into any LLM-based image generation workflow. Same JSON, more consistent style direction across generations.

## Quick Start

1. Browse the [Featured Styles](#featured-styles), [Quick Links](#quick-links), or [All Styles](#all-styles).
2. Open a style folder and copy the `style.json`.
3. Paste the full JSON into ChatGPT, Claude, Nano Banana Pro, or any LLM-based image workflow.
4. Provide your own values for the variables declared in `environment_variables`, or edit a case in `examples[*].values`.
5. Generate the final image prompt and send it to your image model.

See the [Complete Example](#complete-example) below for a full input-to-output walkthrough.

### Recommended Image Models

This workflow works best with end-to-end multimodal image models that can read long structured JSON prompts and generate the final image in one step.

- ChatGPT Images 2 (OpenAI, gpt-image-2) — strong text rendering, 2K/4K output, reasoning before generation
- Nano Banana Pro (Google, Gemini 3 Pro Image) — 4K output, multilingual text accuracy, strong subject consistency

Other multimodal LLMs that accept long JSON prompts may also work but are not the primary recommendation.

## Complete Example

### Input → Output Walkthrough

This example uses [Mono Noir Type Portrait Poster Style](styles/mono-noir-type-portrait-poster-style/).

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

<img src="styles/mono-noir-type-portrait-poster-style/preview-16x9.jpg" alt="Mono Noir Type Portrait Poster Style result preview">

## Copy Prompt Library

Prefer the short path? Browse the generated [Copy Prompt Library](docs/copy-prompts/README.md) for a copy-ready prompt per style. The full reusable style systems still live in each `style.json`.

## Featured Styles

Six visual systems to start with. Every style ships as one JSON plus two preview images. Browse the complete set of 58 in the [All Styles](#all-styles) gallery below.

<!-- HTML table used for rich image+link cells -->

<table>
<tr>
<td width="33%" valign="top">
<a href="styles/market-brush-produce-poster-style"><img src="styles/market-brush-produce-poster-style/preview-16x9.jpg" alt="Market Brush Produce Poster Style preview"></a>
<h3>Market Brush Produce Poster Style</h3>
<p>A contemporary fresh-market poster system with warm ivory negative space, one oversized glossy produce hero, rough black brush typography, thin editorial microcopy, seasonal seals, and soft analog print grain.</p>
<p><a href="styles/market-brush-produce-poster-style/style.json"><strong>Open style.json</strong></a> · <a href="docs/copy-prompts/market-brush-produce-poster-style.md">Copy Prompt</a> · <a href="styles/market-brush-produce-poster-style">Folder</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/folded-newspaper-product-ad-style"><img src="styles/folded-newspaper-product-ad-style/preview-16x9.jpg" alt="Folded Newspaper Product Ad Style preview"></a>
<h3>Folded Newspaper Product Ad Style</h3>
<p>A folded broadsheet advertorial style combining off-white newspaper texture, dense bilingual editorial columns, oversized commercial product photography, black and antique-gold headline typography, angled stamp frames, red date tabs, and tactile print distress.</p>
<p><a href="styles/folded-newspaper-product-ad-style/style.json"><strong>Open style.json</strong></a> · <a href="docs/copy-prompts/folded-newspaper-product-ad-style.md">Copy Prompt</a> · <a href="styles/folded-newspaper-product-ad-style">Folder</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/sunlit-supermodel-nameplate-editorial"><img src="styles/sunlit-supermodel-nameplate-editorial/preview-16x9.jpg" alt="Sunlit Supermodel Nameplate Editorial preview"></a>
<h3>Sunlit Supermodel Nameplate Editorial</h3>
<p>A warm analog fashion editorial poster style combining an outdoor supermodel photograph, lush foreground texture, a small material nameplate detail, and clean white lower-third title/caption typography.</p>
<p><a href="styles/sunlit-supermodel-nameplate-editorial/style.json"><strong>Open style.json</strong></a> · <a href="docs/copy-prompts/sunlit-supermodel-nameplate-editorial.md">Copy Prompt</a> · <a href="styles/sunlit-supermodel-nameplate-editorial">Folder</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a href="styles/black-cutout-food-card-ad-style"><img src="styles/black-cutout-food-card-ad-style/preview-16x9.jpg" alt="Black Cutout Food Card Ad preview"></a>
<h3>Black Cutout Food Card Ad</h3>
<p>A black-background food promotion style built around one irregular cream paper card, oversized hand-brushed Chinese lettering, clipped food photography, small price medallions, warm red/yellow accents, and a handmade street-snack print texture.</p>
<p><a href="styles/black-cutout-food-card-ad-style/style.json"><strong>Open style.json</strong></a> · <a href="docs/copy-prompts/black-cutout-food-card-ad-style.md">Copy Prompt</a> · <a href="styles/black-cutout-food-card-ad-style">Folder</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/kinetic-geometric-doodle-cutouts"><img src="styles/kinetic-geometric-doodle-cutouts/preview-16x9.jpg" alt="Kinetic Geometric Doodle Cutouts preview"></a>
<h3>Kinetic Geometric Doodle Cutouts</h3>
<p>A sparse, playful illustration system where a character or object is assembled from oversized flat geometric color pieces, loose black doodle lines, paper grain, and buoyant off-center motion on a warm cream background.</p>
<p><a href="styles/kinetic-geometric-doodle-cutouts/style.json"><strong>Open style.json</strong></a> · <a href="docs/copy-prompts/kinetic-geometric-doodle-cutouts.md">Copy Prompt</a> · <a href="styles/kinetic-geometric-doodle-cutouts">Folder</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/quiet-luxury-furniture-nameplate-poster-style"><img src="styles/quiet-luxury-furniture-nameplate-poster-style/preview-16x9.jpg" alt="Quiet Luxury Furniture Nameplate Poster Style preview"></a>
<h3>Quiet Luxury Furniture Nameplate Poster Style</h3>
<p>A premium furniture editorial poster system with a warm off-white studio field, oversized deep forest-green display typography behind one realistic hero furniture object, sparse catalog microcopy, thin rules, outlined catalog chips, and a dark green rounded bottom information bar.</p>
<p><a href="styles/quiet-luxury-furniture-nameplate-poster-style/style.json"><strong>Open style.json</strong></a> · <a href="docs/copy-prompts/quiet-luxury-furniture-nameplate-poster-style.md">Copy Prompt</a> · <a href="styles/quiet-luxury-furniture-nameplate-poster-style">Folder</a></p>
</td>
</tr>
</table>

## Package Shape

```text
styles/<style-slug>/
  style.json          # Machine-readable prompt template
  preview-16x9.jpg    # Landscape preview
  preview-9x16.jpg    # Portrait preview
```

## style.json v2.1

Every `style.json` is self-contained: copy the whole file into your LLM, then provide values for the variables declared in `environment_variables` or edit one of the `examples[*].values` cases.

- `prompt_template` is the reusable style prompt with `{VARIABLE}` placeholders.
- `environment_variables` declares every placeholder the template can use.
- `examples` contains ready-to-edit cases; each case stores only `case_name` and `values`.
- `style_fidelity_anchors` and `source_content_to_avoid` tell the model what to preserve and what not to copy.
- `negative_prompt` keeps watermarks, logos, direct source recreations, and off-style outputs away.

Rendered prompts such as `prompt_9x16`, `prompt_16x9`, or `full_prompt` are intentionally not stored. They are derived at generation time from `prompt_template` plus chosen values, so the JSON stays compact and does not drift.

Validate the library with:

```bash
python3 scripts/validate-style-json.py .
```


## All Styles

Browse all 58 styles below.

The complete library, including the featured styles above. For full descriptions and all file links per style, see [docs/CATALOG.md](docs/CATALOG.md).

<!-- HTML table used for rich image+link cells -->

<table>
<tr>
<td width="33%" valign="top">
<a id="market-brush-produce-poster-style"></a>
<a href="styles/market-brush-produce-poster-style"><img src="styles/market-brush-produce-poster-style/preview-16x9.jpg" alt="Market Brush Produce Poster Style preview"></a>
<p><strong><a href="styles/market-brush-produce-poster-style">Market Brush Produce Poster Style</a></strong><br>
<em>Farmers-market produce posters with giant glossy crops, rough brush type, and ivory paper space.</em><br>
<a href="styles/market-brush-produce-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/market-brush-produce-poster-style.md">prompt</a> · <a href="styles/market-brush-produce-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="folded-newspaper-product-ad-style"></a>
<a href="styles/folded-newspaper-product-ad-style"><img src="styles/folded-newspaper-product-ad-style/preview-16x9.jpg" alt="Folded Newspaper Product Ad Style preview"></a>
<p><strong><a href="styles/folded-newspaper-product-ad-style">Folded Newspaper Product Ad Style</a></strong><br>
<em>Folded newspaper advertorials with oversized product cutouts, dense columns, stamps, and antique-gold type.</em><br>
<a href="styles/folded-newspaper-product-ad-style/style.json">style.json</a> · <a href="docs/copy-prompts/folded-newspaper-product-ad-style.md">prompt</a> · <a href="styles/folded-newspaper-product-ad-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="sunlit-supermodel-nameplate-editorial"></a>
<a href="styles/sunlit-supermodel-nameplate-editorial"><img src="styles/sunlit-supermodel-nameplate-editorial/preview-16x9.jpg" alt="Sunlit Supermodel Nameplate Editorial preview"></a>
<p><strong><a href="styles/sunlit-supermodel-nameplate-editorial">Sunlit Supermodel Nameplate Editorial</a></strong><br>
<em>Sunlit supermodel editorials with outdoor texture, nameplate details, and clean lower-third type.</em><br>
<a href="styles/sunlit-supermodel-nameplate-editorial/style.json">style.json</a> · <a href="docs/copy-prompts/sunlit-supermodel-nameplate-editorial.md">prompt</a> · <a href="styles/sunlit-supermodel-nameplate-editorial/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="black-cutout-food-card-ad-style"></a>
<a href="styles/black-cutout-food-card-ad-style"><img src="styles/black-cutout-food-card-ad-style/preview-16x9.jpg" alt="Black Cutout Food Card Ad preview"></a>
<p><strong><a href="styles/black-cutout-food-card-ad-style">Black Cutout Food Card Ad</a></strong><br>
<em>Black food-card ads with brush lettering, cutout photography, and street-snack print texture.</em><br>
<a href="styles/black-cutout-food-card-ad-style/style.json">style.json</a> · <a href="docs/copy-prompts/black-cutout-food-card-ad-style.md">prompt</a> · <a href="styles/black-cutout-food-card-ad-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="kinetic-geometric-doodle-cutouts"></a>
<a href="styles/kinetic-geometric-doodle-cutouts"><img src="styles/kinetic-geometric-doodle-cutouts/preview-16x9.jpg" alt="Kinetic Geometric Doodle Cutouts preview"></a>
<p><strong><a href="styles/kinetic-geometric-doodle-cutouts">Kinetic Geometric Doodle Cutouts</a></strong><br>
<em>Playful geometric doodle cutouts with flat color pieces, loose lines, and paper grain.</em><br>
<a href="styles/kinetic-geometric-doodle-cutouts/style.json">style.json</a> · <a href="docs/copy-prompts/kinetic-geometric-doodle-cutouts.md">prompt</a> · <a href="styles/kinetic-geometric-doodle-cutouts/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="quiet-luxury-furniture-nameplate-poster-style"></a>
<a href="styles/quiet-luxury-furniture-nameplate-poster-style"><img src="styles/quiet-luxury-furniture-nameplate-poster-style/preview-16x9.jpg" alt="Quiet Luxury Furniture Nameplate Poster Style preview"></a>
<p><strong><a href="styles/quiet-luxury-furniture-nameplate-poster-style">Quiet Luxury Furniture Nameplate Poster Style</a></strong><br>
<em>Quiet luxury furniture nameplates with forest-green type, catalog chips, and warm studio restraint.</em><br>
<a href="styles/quiet-luxury-furniture-nameplate-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/quiet-luxury-furniture-nameplate-poster-style.md">prompt</a> · <a href="styles/quiet-luxury-furniture-nameplate-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="kinetic-luxury-street-fashion-cover-style"></a>
<a href="styles/kinetic-luxury-street-fashion-cover-style"><img src="styles/kinetic-luxury-street-fashion-cover-style/preview-16x9.jpg" alt="Kinetic Luxury Street Fashion Cover Style preview"></a>
<p><strong><a href="styles/kinetic-luxury-street-fashion-cover-style">Kinetic Luxury Street Fashion Cover Style</a></strong><br>
<em>Street-fashion cover editorials with motion-blurred architecture, luxury garments, and wide-spaced serif type.</em><br>
<a href="styles/kinetic-luxury-street-fashion-cover-style/style.json">style.json</a> · <a href="docs/copy-prompts/kinetic-luxury-street-fashion-cover-style.md">prompt</a> · <a href="styles/kinetic-luxury-street-fashion-cover-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="sunlit-architectural-fashion-editorial"></a>
<a href="styles/sunlit-architectural-fashion-editorial"><img src="styles/sunlit-architectural-fashion-editorial/preview-16x9.jpg" alt="Sunlit Architectural Fashion Editorial preview"></a>
<p><strong><a href="styles/sunlit-architectural-fashion-editorial">Sunlit Architectural Fashion Editorial</a></strong><br>
<em>Sunlit fashion editorials with low-angle architecture, warm stone, and elongated silhouettes.</em><br>
<a href="styles/sunlit-architectural-fashion-editorial/style.json">style.json</a> · <a href="docs/copy-prompts/sunlit-architectural-fashion-editorial.md">prompt</a> · <a href="styles/sunlit-architectural-fashion-editorial/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="multi-color-beverage-splash-ad-system-style"></a>
<a href="styles/multi-color-beverage-splash-ad-system-style"><img src="styles/multi-color-beverage-splash-ad-system-style/preview-16x9.jpg" alt="Multi-Color Beverage Splash Ad System Style preview"></a>
<p><strong><a href="styles/multi-color-beverage-splash-ad-system-style">Multi-Color Beverage Splash Ad System Style</a></strong><br>
<em>Color-varied beverage launch ads with giant white 3D type and frozen splash motion.</em><br>
<a href="styles/multi-color-beverage-splash-ad-system-style/style.json">style.json</a> · <a href="docs/copy-prompts/multi-color-beverage-splash-ad-system-style.md">prompt</a> · <a href="styles/multi-color-beverage-splash-ad-system-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="yellow-black-manga-food-zine-ad-style"></a>
<a href="styles/yellow-black-manga-food-zine-ad-style"><img src="styles/yellow-black-manga-food-zine-ad-style/preview-16x9.jpg" alt="Yellow Black Manga Food Zine Ad Style preview"></a>
<p><strong><a href="styles/yellow-black-manga-food-zine-ad-style">Yellow Black Manga Food Zine Ad Style</a></strong><br>
<em>Black-yellow manga food zine ads with warped type and glossy hero objects.</em><br>
<a href="styles/yellow-black-manga-food-zine-ad-style/style.json">style.json</a> · <a href="docs/copy-prompts/yellow-black-manga-food-zine-ad-style.md">prompt</a> · <a href="styles/yellow-black-manga-food-zine-ad-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="neon-outdoor-diary-longform-collage-style"></a>
<a href="styles/neon-outdoor-diary-longform-collage-style"><img src="styles/neon-outdoor-diary-longform-collage-style/preview-16x9.jpg" alt="Neon Outdoor Diary Longform Collage Style preview"></a>
<p><strong><a href="styles/neon-outdoor-diary-longform-collage-style">Neon Outdoor Diary Longform Collage Style</a></strong><br>
<em>Longform outdoor diary collages with acid-green type and torn field-note panels.</em><br>
<a href="styles/neon-outdoor-diary-longform-collage-style/style.json">style.json</a> · <a href="docs/copy-prompts/neon-outdoor-diary-longform-collage-style.md">prompt</a> · <a href="styles/neon-outdoor-diary-longform-collage-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="acid-lime-3d-streetwear-type-poster-style"></a>
<a href="styles/acid-lime-3d-streetwear-type-poster-style"><img src="styles/acid-lime-3d-streetwear-type-poster-style/preview-16x9.jpg" alt="Acid Lime 3D Streetwear Type Poster Style preview"></a>
<p><strong><a href="styles/acid-lime-3d-streetwear-type-poster-style">Acid Lime 3D Streetwear Type Poster Style</a></strong><br>
<em>Glossy C4D streetwear campaigns with black block type and acid-lime accents.</em><br>
<a href="styles/acid-lime-3d-streetwear-type-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/acid-lime-3d-streetwear-type-poster-style.md">prompt</a> · <a href="styles/acid-lime-3d-streetwear-type-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="electric-blue-silhouette-product-launch-style"></a>
<a href="styles/electric-blue-silhouette-product-launch-style"><img src="styles/electric-blue-silhouette-product-launch-style/preview-16x9.jpg" alt="Electric Blue Silhouette Product Launch Style preview"></a>
<p><strong><a href="styles/electric-blue-silhouette-product-launch-style">Electric Blue Silhouette Product Launch Style</a></strong><br>
<em>Premium black-and-blue product launches with glowing silhouettes and cropped type.</em><br>
<a href="styles/electric-blue-silhouette-product-launch-style/style.json">style.json</a> · <a href="docs/copy-prompts/electric-blue-silhouette-product-launch-style.md">prompt</a> · <a href="styles/electric-blue-silhouette-product-launch-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="luxury-perspective-checkerboard-editorial"></a>
<a href="styles/luxury-perspective-checkerboard-editorial"><img src="styles/luxury-perspective-checkerboard-editorial/preview-16x9.jpg" alt="Luxury Perspective Checkerboard Editorial preview"></a>
<p><strong><a href="styles/luxury-perspective-checkerboard-editorial">Luxury Perspective Checkerboard Editorial</a></strong><br>
<em>Luxury editorials with checkerboard perspective, script typography, and polished white space.</em><br>
<a href="styles/luxury-perspective-checkerboard-editorial/style.json">style.json</a> · <a href="docs/copy-prompts/luxury-perspective-checkerboard-editorial.md">prompt</a> · <a href="styles/luxury-perspective-checkerboard-editorial/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="sunny-3d-avatar-campaign-style"></a>
<a href="styles/sunny-3d-avatar-campaign-style"><img src="styles/sunny-3d-avatar-campaign-style/preview-16x9.jpg" alt="Sunny 3D Avatar Campaign Style preview"></a>
<p><strong><a href="styles/sunny-3d-avatar-campaign-style">Sunny 3D Avatar Campaign Style</a></strong><br>
<em>Sunny campaign 3D avatars with blue skies, bold type, and neon motion marks.</em><br>
<a href="styles/sunny-3d-avatar-campaign-style/style.json">style.json</a> · <a href="docs/copy-prompts/sunny-3d-avatar-campaign-style.md">prompt</a> · <a href="styles/sunny-3d-avatar-campaign-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="y2k-mirror-ui-scribble-collage-style"></a>
<a href="styles/y2k-mirror-ui-scribble-collage-style"><img src="styles/y2k-mirror-ui-scribble-collage-style/preview-16x9.jpg" alt="Y2K Mirror UI Scribble Collage Style preview"></a>
<p><strong><a href="styles/y2k-mirror-ui-scribble-collage-style">Y2K Mirror UI Scribble Collage Style</a></strong><br>
<em>Flash-photo Y2K collages with mirror UI panels and electric-blue scribbles.</em><br>
<a href="styles/y2k-mirror-ui-scribble-collage-style/style.json">style.json</a> · <a href="docs/copy-prompts/y2k-mirror-ui-scribble-collage-style.md">prompt</a> · <a href="styles/y2k-mirror-ui-scribble-collage-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="neon-plush-gadget-pop-3d-style"></a>
<a href="styles/neon-plush-gadget-pop-3d-style"><img src="styles/neon-plush-gadget-pop-3d-style/preview-16x9.jpg" alt="Neon Plush Gadget Pop 3D Style preview"></a>
<p><strong><a href="styles/neon-plush-gadget-pop-3d-style">Neon Plush Gadget Pop 3D Style</a></strong><br>
<em>Neon toy-product 3D renders with plush mascots and chunky gadget props.</em><br>
<a href="styles/neon-plush-gadget-pop-3d-style/style.json">style.json</a> · <a href="docs/copy-prompts/neon-plush-gadget-pop-3d-style.md">prompt</a> · <a href="styles/neon-plush-gadget-pop-3d-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="blue-lime-kinetic-comic-type-poster-style"></a>
<a href="styles/blue-lime-kinetic-comic-type-poster-style"><img src="styles/blue-lime-kinetic-comic-type-poster-style/preview-16x9.jpg" alt="Blue Lime Kinetic Comic Type Poster Style preview"></a>
<p><strong><a href="styles/blue-lime-kinetic-comic-type-poster-style">Blue Lime Kinetic Comic Type Poster Style</a></strong><br>
<em>Electric-blue comic posters with lime speech panels and massive black type.</em><br>
<a href="styles/blue-lime-kinetic-comic-type-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/blue-lime-kinetic-comic-type-poster-style.md">prompt</a> · <a href="styles/blue-lime-kinetic-comic-type-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="blue-chinese-perspective-type-canyon-style"></a>
<a href="styles/blue-chinese-perspective-type-canyon-style"><img src="styles/blue-chinese-perspective-type-canyon-style/preview-16x9.jpg" alt="Blue Chinese Perspective Type Canyon Style preview"></a>
<p><strong><a href="styles/blue-chinese-perspective-type-canyon-style">Blue Chinese Perspective Type Canyon Style</a></strong><br>
<em>Blue perspective corridors with stacked Chinese display type.</em><br>
<a href="styles/blue-chinese-perspective-type-canyon-style/style.json">style.json</a> · <a href="docs/copy-prompts/blue-chinese-perspective-type-canyon-style.md">prompt</a> · <a href="styles/blue-chinese-perspective-type-canyon-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="rough-ink-music-doodle-poster-style"></a>
<a href="styles/rough-ink-music-doodle-poster-style"><img src="styles/rough-ink-music-doodle-poster-style/preview-16x9.jpg" alt="Rough Ink Music Doodle Poster Style preview"></a>
<p><strong><a href="styles/rough-ink-music-doodle-poster-style">Rough Ink Music Doodle Poster Style</a></strong><br>
<em>Hand-inked music posters with brush lettering and playful doodles.</em><br>
<a href="styles/rough-ink-music-doodle-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/rough-ink-music-doodle-poster-style.md">prompt</a> · <a href="styles/rough-ink-music-doodle-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="mono-noir-type-portrait-poster-style"></a>
<a href="styles/mono-noir-type-portrait-poster-style"><img src="styles/mono-noir-type-portrait-poster-style/preview-16x9.jpg" alt="Mono Noir Type Portrait Poster Style preview"></a>
<p><strong><a href="styles/mono-noir-type-portrait-poster-style">Mono Noir Type Portrait Poster Style</a></strong><br>
<em>Black-and-white editorial portraits with massive lowercase type.</em><br>
<a href="styles/mono-noir-type-portrait-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/mono-noir-type-portrait-poster-style.md">prompt</a> · <a href="styles/mono-noir-type-portrait-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="bold-block-mascot-poster-style"></a>
<a href="styles/bold-block-mascot-poster-style"><img src="styles/bold-block-mascot-poster-style/preview-16x9.jpg" alt="Bold Block Mascot Poster Style preview"></a>
<p><strong><a href="styles/bold-block-mascot-poster-style">Bold Block Mascot Poster Style</a></strong><br>
<em>Flat mascot posters with chunky block type and sticker figures.</em><br>
<a href="styles/bold-block-mascot-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/bold-block-mascot-poster-style.md">prompt</a> · <a href="styles/bold-block-mascot-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="blue-hud-macro-product-poster"></a>
<a href="styles/blue-hud-macro-product-poster"><img src="styles/blue-hud-macro-product-poster/preview-16x9.jpg" alt="Blue HUD Macro Creator Tech Poster preview"></a>
<p><strong><a href="styles/blue-hud-macro-product-poster">Blue HUD Macro Creator Tech Poster</a></strong><br>
<em>Glossy macro product posters with blue HUD launch graphics.</em><br>
<a href="styles/blue-hud-macro-product-poster/style.json">style.json</a> · <a href="docs/copy-prompts/blue-hud-macro-product-poster.md">prompt</a> · <a href="styles/blue-hud-macro-product-poster/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="warm-fisheye-product-impact-ad-style"></a>
<a href="styles/warm-fisheye-product-impact-ad-style"><img src="styles/warm-fisheye-product-impact-ad-style/preview-16x9.jpg" alt="Warm Fisheye Product Impact Ad Style preview"></a>
<p><strong><a href="styles/warm-fisheye-product-impact-ad-style">Warm Fisheye Product Impact Ad Style</a></strong><br>
<em>Warm fisheye product ads with bold Chinese social-commerce type.</em><br>
<a href="styles/warm-fisheye-product-impact-ad-style/style.json">style.json</a> · <a href="docs/copy-prompts/warm-fisheye-product-impact-ad-style.md">prompt</a> · <a href="styles/warm-fisheye-product-impact-ad-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="olive-scribble-sports-poster-style"></a>
<a href="styles/olive-scribble-sports-poster-style"><img src="styles/olive-scribble-sports-poster-style/preview-16x9.jpg" alt="Olive Scribble Sports Poster Style preview"></a>
<p><strong><a href="styles/olive-scribble-sports-poster-style">Olive Scribble Sports Poster Style</a></strong><br>
<em>Handmade sports posters with olive blocks and kinetic scribbles.</em><br>
<a href="styles/olive-scribble-sports-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/olive-scribble-sports-poster-style.md">prompt</a> · <a href="styles/olive-scribble-sports-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="bold-anime-reaction-thumbnail-style"></a>
<a href="styles/bold-anime-reaction-thumbnail-style"><img src="styles/bold-anime-reaction-thumbnail-style/preview-16x9.jpg" alt="Bold Anime Reaction Thumbnail Style preview"></a>
<p><strong><a href="styles/bold-anime-reaction-thumbnail-style">Bold Anime Reaction Thumbnail Style</a></strong><br>
<em>High-impact anime thumbnails with bold yellow reaction typography.</em><br>
<a href="styles/bold-anime-reaction-thumbnail-style/style.json">style.json</a> · <a href="docs/copy-prompts/bold-anime-reaction-thumbnail-style.md">prompt</a> · <a href="styles/bold-anime-reaction-thumbnail-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="turquoise-red-techno-manga-poster-style"></a>
<a href="styles/turquoise-red-techno-manga-poster-style"><img src="styles/turquoise-red-techno-manga-poster-style/preview-16x9.jpg" alt="Turquoise Red Techno Manga Poster Style preview"></a>
<p><strong><a href="styles/turquoise-red-techno-manga-poster-style">Turquoise Red Techno Manga Poster Style</a></strong><br>
<em>Retro techno-manga posters with turquoise hardware and red lettering.</em><br>
<a href="styles/turquoise-red-techno-manga-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/turquoise-red-techno-manga-poster-style.md">prompt</a> · <a href="styles/turquoise-red-techno-manga-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="chromatic-fisheye-orbit-pop-poster-style"></a>
<a href="styles/chromatic-fisheye-orbit-pop-poster-style"><img src="styles/chromatic-fisheye-orbit-pop-poster-style/preview-16x9.jpg" alt="Chromatic Fisheye Orbit Pop Poster Style preview"></a>
<p><strong><a href="styles/chromatic-fisheye-orbit-pop-poster-style">Chromatic Fisheye Orbit Pop Poster Style</a></strong><br>
<em>Pop fisheye posters with orbiting type and chromatic arcs.</em><br>
<a href="styles/chromatic-fisheye-orbit-pop-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/chromatic-fisheye-orbit-pop-poster-style.md">prompt</a> · <a href="styles/chromatic-fisheye-orbit-pop-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="naive-marker-psa-poster-style"></a>
<a href="styles/naive-marker-psa-poster-style"><img src="styles/naive-marker-psa-poster-style/preview-16x9.jpg" alt="Naive Marker PSA Poster Style preview"></a>
<p><strong><a href="styles/naive-marker-psa-poster-style">Naive Marker PSA Poster Style</a></strong><br>
<em>Friendly civic PSA posters with naive marker drawings.</em><br>
<a href="styles/naive-marker-psa-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/naive-marker-psa-poster-style.md">prompt</a> · <a href="styles/naive-marker-psa-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="blue-bubble-fisheye-action-poster-style"></a>
<a href="styles/blue-bubble-fisheye-action-poster-style"><img src="styles/blue-bubble-fisheye-action-poster-style/preview-16x9.jpg" alt="Blue Bubble Fisheye Action Poster Style preview"></a>
<p><strong><a href="styles/blue-bubble-fisheye-action-poster-style">Blue Bubble Fisheye Action Poster Style</a></strong><br>
<em>Youth action posters with blue bubble type and fisheye photos.</em><br>
<a href="styles/blue-bubble-fisheye-action-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/blue-bubble-fisheye-action-poster-style.md">prompt</a> · <a href="styles/blue-bubble-fisheye-action-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="cozy-bedroom-doodle-companion-snapshot-style"></a>
<a href="styles/cozy-bedroom-doodle-companion-snapshot-style"><img src="styles/cozy-bedroom-doodle-companion-snapshot-style/preview-16x9.jpg" alt="Cozy Bedroom Doodle Companion Snapshot Style preview"></a>
<p><strong><a href="styles/cozy-bedroom-doodle-companion-snapshot-style">Cozy Bedroom Doodle Companion Snapshot Style</a></strong><br>
<em>Low-light bedroom snapshots with quiet doodle companion energy.</em><br>
<a href="styles/cozy-bedroom-doodle-companion-snapshot-style/style.json">style.json</a> · <a href="docs/copy-prompts/cozy-bedroom-doodle-companion-snapshot-style.md">prompt</a> · <a href="styles/cozy-bedroom-doodle-companion-snapshot-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="surreal-fish-doodle-landmark-photo-collage-style"></a>
<a href="styles/surreal-fish-doodle-landmark-photo-collage-style"><img src="styles/surreal-fish-doodle-landmark-photo-collage-style/preview-16x9.jpg" alt="Surreal Fish Doodle Landmark Photo Collage Style preview"></a>
<p><strong><a href="styles/surreal-fish-doodle-landmark-photo-collage-style">Surreal Fish Doodle Landmark Photo Collage Style</a></strong><br>
<em>Landmark travel photos remixed with folk-art fish doodles.</em><br>
<a href="styles/surreal-fish-doodle-landmark-photo-collage-style/style.json">style.json</a> · <a href="docs/copy-prompts/surreal-fish-doodle-landmark-photo-collage-style.md">prompt</a> · <a href="styles/surreal-fish-doodle-landmark-photo-collage-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="plush-comic-toy-product-poster-style"></a>
<a href="styles/plush-comic-toy-product-poster-style"><img src="styles/plush-comic-toy-product-poster-style/preview-16x9.jpg" alt="Plush Comic Toy Product Poster Style preview"></a>
<p><strong><a href="styles/plush-comic-toy-product-poster-style">Plush Comic Toy Product Poster Style</a></strong><br>
<em>Toy-product posters with fuzzy plush heroes and comic typography.</em><br>
<a href="styles/plush-comic-toy-product-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/plush-comic-toy-product-poster-style.md">prompt</a> · <a href="styles/plush-comic-toy-product-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="rough-animation-pet-sketch-storyboard-style"></a>
<a href="styles/rough-animation-pet-sketch-storyboard-style"><img src="styles/rough-animation-pet-sketch-storyboard-style/preview-16x9.jpg" alt="Rough Animation Pet Sketch Storyboard Style preview"></a>
<p><strong><a href="styles/rough-animation-pet-sketch-storyboard-style">Rough Animation Pet Sketch Storyboard Style</a></strong><br>
<em>Loose pet-comedy storyboard frames with warm sketch texture.</em><br>
<a href="styles/rough-animation-pet-sketch-storyboard-style/style.json">style.json</a> · <a href="docs/copy-prompts/rough-animation-pet-sketch-storyboard-style.md">prompt</a> · <a href="styles/rough-animation-pet-sketch-storyboard-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="tri-color-hardcut-portrait-poster-style"></a>
<a href="styles/tri-color-hardcut-portrait-poster-style"><img src="styles/tri-color-hardcut-portrait-poster-style/preview-16x9.jpg" alt="Tri Color Hardcut Portrait Poster Style preview"></a>
<p><strong><a href="styles/tri-color-hardcut-portrait-poster-style">Tri Color Hardcut Portrait Poster Style</a></strong><br>
<em>Three-color portrait posters built from hard-edged cutout planes.</em><br>
<a href="styles/tri-color-hardcut-portrait-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/tri-color-hardcut-portrait-poster-style.md">prompt</a> · <a href="styles/tri-color-hardcut-portrait-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="clean-triptych-travel-vlog-thumbnail-style"></a>
<a href="styles/clean-triptych-travel-vlog-thumbnail-style"><img src="styles/clean-triptych-travel-vlog-thumbnail-style/preview-16x9.jpg" alt="Clean Triptych Travel Vlog Thumbnail Style preview"></a>
<p><strong><a href="styles/clean-triptych-travel-vlog-thumbnail-style">Clean Triptych Travel Vlog Thumbnail Style</a></strong><br>
<em>Clean travel thumbnails with three photo panels and soft notes.</em><br>
<a href="styles/clean-triptych-travel-vlog-thumbnail-style/style.json">style.json</a> · <a href="docs/copy-prompts/clean-triptych-travel-vlog-thumbnail-style.md">prompt</a> · <a href="styles/clean-triptych-travel-vlog-thumbnail-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="playful-mascot-doodle-snapshot-style"></a>
<a href="styles/playful-mascot-doodle-snapshot-style"><img src="styles/playful-mascot-doodle-snapshot-style/preview-16x9.jpg" alt="Playful Mascot Doodle Snapshot Style preview"></a>
<p><strong><a href="styles/playful-mascot-doodle-snapshot-style">Playful Mascot Doodle Snapshot Style</a></strong><br>
<em>Real-life snapshots layered with mascot stickers and doodles.</em><br>
<a href="styles/playful-mascot-doodle-snapshot-style/style.json">style.json</a> · <a href="docs/copy-prompts/playful-mascot-doodle-snapshot-style.md">prompt</a> · <a href="styles/playful-mascot-doodle-snapshot-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="teenage-skate-scribble-screenprint-poster-style"></a>
<a href="styles/teenage-skate-scribble-screenprint-poster-style"><img src="styles/teenage-skate-scribble-screenprint-poster-style/preview-16x9.jpg" alt="Teenage Skate Scribble Screenprint Poster Style preview"></a>
<p><strong><a href="styles/teenage-skate-scribble-screenprint-poster-style">Teenage Skate Scribble Screenprint Poster Style</a></strong><br>
<em>Retro skate posters with scribbled borders and screenprint grit.</em><br>
<a href="styles/teenage-skate-scribble-screenprint-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/teenage-skate-scribble-screenprint-poster-style.md">prompt</a> · <a href="styles/teenage-skate-scribble-screenprint-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="impact-burst-halftone-comic-poster-style"></a>
<a href="styles/impact-burst-halftone-comic-poster-style"><img src="styles/impact-burst-halftone-comic-poster-style/preview-16x9.jpg" alt="Impact Burst Halftone Comic Poster Style preview"></a>
<p><strong><a href="styles/impact-burst-halftone-comic-poster-style">Impact Burst Halftone Comic Poster Style</a></strong><br>
<em>Loud comic posters with impact type and halftone bursts.</em><br>
<a href="styles/impact-burst-halftone-comic-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/impact-burst-halftone-comic-poster-style.md">prompt</a> · <a href="styles/impact-burst-halftone-comic-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="sunburst-fisheye-bubble-type-poster-style"></a>
<a href="styles/sunburst-fisheye-bubble-type-poster-style"><img src="styles/sunburst-fisheye-bubble-type-poster-style/preview-16x9.jpg" alt="Sunburst Fisheye Bubble Type Poster Style preview"></a>
<p><strong><a href="styles/sunburst-fisheye-bubble-type-poster-style">Sunburst Fisheye Bubble Type Poster Style</a></strong><br>
<em>Summer fisheye posters with sunny bubble typography.</em><br>
<a href="styles/sunburst-fisheye-bubble-type-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/sunburst-fisheye-bubble-type-poster-style.md">prompt</a> · <a href="styles/sunburst-fisheye-bubble-type-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="backseat-transit-doodle-letter-poster-style"></a>
<a href="styles/backseat-transit-doodle-letter-poster-style"><img src="styles/backseat-transit-doodle-letter-poster-style/preview-16x9.jpg" alt="Backseat Transit Doodle Letter Poster Style preview"></a>
<p><strong><a href="styles/backseat-transit-doodle-letter-poster-style">Backseat Transit Doodle Letter Poster Style</a></strong><br>
<em>Transit photos turned into energetic hand-lettered travel posters.</em><br>
<a href="styles/backseat-transit-doodle-letter-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/backseat-transit-doodle-letter-poster-style.md">prompt</a> · <a href="styles/backseat-transit-doodle-letter-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="analog-sticker-diary-portrait-poster-style"></a>
<a href="styles/analog-sticker-diary-portrait-poster-style"><img src="styles/analog-sticker-diary-portrait-poster-style/preview-16x9.jpg" alt="Analog Sticker Diary Portrait Poster Style preview"></a>
<p><strong><a href="styles/analog-sticker-diary-portrait-poster-style">Analog Sticker Diary Portrait Poster Style</a></strong><br>
<em>Nostalgic diary portraits with stickers and distressed lettering.</em><br>
<a href="styles/analog-sticker-diary-portrait-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/analog-sticker-diary-portrait-poster-style.md">prompt</a> · <a href="styles/analog-sticker-diary-portrait-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="folded-diamond-perspective-type-poster-style"></a>
<a href="styles/folded-diamond-perspective-type-poster-style"><img src="styles/folded-diamond-perspective-type-poster-style/preview-16x9.jpg" alt="Folded Diamond Perspective Type Poster Style preview"></a>
<p><strong><a href="styles/folded-diamond-perspective-type-poster-style">Folded Diamond Perspective Type Poster Style</a></strong><br>
<em>Minimal diamond-aperture posters with folded perspective typography.</em><br>
<a href="styles/folded-diamond-perspective-type-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/folded-diamond-perspective-type-poster-style.md">prompt</a> · <a href="styles/folded-diamond-perspective-type-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="gothic-cat-doodle-photo-collage-style"></a>
<a href="styles/gothic-cat-doodle-photo-collage-style"><img src="styles/gothic-cat-doodle-photo-collage-style/preview-16x9.jpg" alt="Gothic Cat Doodle Photo Collage Style preview"></a>
<p><strong><a href="styles/gothic-cat-doodle-photo-collage-style">Gothic Cat Doodle Photo Collage Style</a></strong><br>
<em>Dramatic architecture photos with playful cartoon creature overlays.</em><br>
<a href="styles/gothic-cat-doodle-photo-collage-style/style.json">style.json</a> · <a href="docs/copy-prompts/gothic-cat-doodle-photo-collage-style.md">prompt</a> · <a href="styles/gothic-cat-doodle-photo-collage-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="k-pop-apocalypse-ransom-zine-style"></a>
<a href="styles/k-pop-apocalypse-ransom-zine-style"><img src="styles/k-pop-apocalypse-ransom-zine-style/preview-16x9.jpg" alt="K-Pop Apocalypse Ransom Zine Style preview"></a>
<p><strong><a href="styles/k-pop-apocalypse-ransom-zine-style">K-Pop Apocalypse Ransom Zine Style</a></strong><br>
<em>Maximal K-pop zines with ransom type and sticker blocks.</em><br>
<a href="styles/k-pop-apocalypse-ransom-zine-style/style.json">style.json</a> · <a href="docs/copy-prompts/k-pop-apocalypse-ransom-zine-style.md">prompt</a> · <a href="styles/k-pop-apocalypse-ransom-zine-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="metro-doodle-snapshot-diary-style"></a>
<a href="styles/metro-doodle-snapshot-diary-style"><img src="styles/metro-doodle-snapshot-diary-style/preview-16x9.jpg" alt="Metro Doodle Snapshot Diary preview"></a>
<p><strong><a href="styles/metro-doodle-snapshot-diary-style">Metro Doodle Snapshot Diary</a></strong><br>
<em>Crowded transit snapshots layered with marker doodles and oversized comic faces.</em><br>
<a href="styles/metro-doodle-snapshot-diary-style/style.json">style.json</a> · <a href="docs/copy-prompts/metro-doodle-snapshot-diary-style.md">prompt</a> · <a href="styles/metro-doodle-snapshot-diary-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="mountain-trail-monster-doodle-poster-style"></a>
<a href="styles/mountain-trail-monster-doodle-poster-style"><img src="styles/mountain-trail-monster-doodle-poster-style/preview-16x9.jpg" alt="Mountain Trail Monster Doodle Poster Style preview"></a>
<p><strong><a href="styles/mountain-trail-monster-doodle-poster-style">Mountain Trail Monster Doodle Poster Style</a></strong><br>
<em>Outdoor hiking photos remixed with monster companions and annotations.</em><br>
<a href="styles/mountain-trail-monster-doodle-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/mountain-trail-monster-doodle-poster-style.md">prompt</a> · <a href="styles/mountain-trail-monster-doodle-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="neon-doodle-gallery-snapshot-style"></a>
<a href="styles/neon-doodle-gallery-snapshot-style"><img src="styles/neon-doodle-gallery-snapshot-style/preview-16x9.jpg" alt="Neon Doodle Gallery Snapshot preview"></a>
<p><strong><a href="styles/neon-doodle-gallery-snapshot-style">Neon Doodle Gallery Snapshot</a></strong><br>
<em>Phone photos covered in hot neon diary doodles.</em><br>
<a href="styles/neon-doodle-gallery-snapshot-style/style.json">style.json</a> · <a href="docs/copy-prompts/neon-doodle-gallery-snapshot-style.md">prompt</a> · <a href="styles/neon-doodle-gallery-snapshot-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="neon-kinetic-typographic-poster-style"></a>
<a href="styles/neon-kinetic-typographic-poster-style"><img src="styles/neon-kinetic-typographic-poster-style/preview-16x9.jpg" alt="Neon Kinetic Typographic Poster preview"></a>
<p><strong><a href="styles/neon-kinetic-typographic-poster-style">Neon Kinetic Typographic Poster</a></strong><br>
<em>Outdoor editorial posters with warped neon kinetic typography.</em><br>
<a href="styles/neon-kinetic-typographic-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/neon-kinetic-typographic-poster-style.md">prompt</a> · <a href="styles/neon-kinetic-typographic-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="orange-brush-mascot-action-poster-style"></a>
<a href="styles/orange-brush-mascot-action-poster-style"><img src="styles/orange-brush-mascot-action-poster-style/preview-16x9.jpg" alt="Orange Brush Mascot Action Poster Style preview"></a>
<p><strong><a href="styles/orange-brush-mascot-action-poster-style">Orange Brush Mascot Action Poster Style</a></strong><br>
<em>Sparse mascot illustrations with orange brush texture and print grain.</em><br>
<a href="styles/orange-brush-mascot-action-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/orange-brush-mascot-action-poster-style.md">prompt</a> · <a href="styles/orange-brush-mascot-action-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="photo-illustration-overlay-poster-style"></a>
<a href="styles/photo-illustration-overlay-poster-style"><img src="styles/photo-illustration-overlay-poster-style/preview-16x9.jpg" alt="Photo Illustration Overlay Poster preview"></a>
<p><strong><a href="styles/photo-illustration-overlay-poster-style">Photo Illustration Overlay Poster</a></strong><br>
<em>City photos composited with saturated 2D character overlays.</em><br>
<a href="styles/photo-illustration-overlay-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/photo-illustration-overlay-poster-style.md">prompt</a> · <a href="styles/photo-illustration-overlay-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="plush-city-festival-mobile-poster-style"></a>
<a href="styles/plush-city-festival-mobile-poster-style"><img src="styles/plush-city-festival-mobile-poster-style/preview-16x9.jpg" alt="Plush City Festival Mobile Poster preview"></a>
<p><strong><a href="styles/plush-city-festival-mobile-poster-style">Plush City Festival Mobile Poster</a></strong><br>
<em>Mobile city-event posters with fuzzy mascots and app-card framing.</em><br>
<a href="styles/plush-city-festival-mobile-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/plush-city-festival-mobile-poster-style.md">prompt</a> · <a href="styles/plush-city-festival-mobile-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="pop-bubble-letter-photo-poster-style"></a>
<a href="styles/pop-bubble-letter-photo-poster-style"><img src="styles/pop-bubble-letter-photo-poster-style/preview-16x9.jpg" alt="Pop Bubble Letter Photo Poster Style preview"></a>
<p><strong><a href="styles/pop-bubble-letter-photo-poster-style">Pop Bubble Letter Photo Poster Style</a></strong><br>
<em>Fashion photo posters framed by candy-colored bubble letters.</em><br>
<a href="styles/pop-bubble-letter-photo-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/pop-bubble-letter-photo-poster-style.md">prompt</a> · <a href="styles/pop-bubble-letter-photo-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="soft-analog-future-editorial-poster-style"></a>
<a href="styles/soft-analog-future-editorial-poster-style"><img src="styles/soft-analog-future-editorial-poster-style/preview-16x9.jpg" alt="Soft Analog Future Editorial Poster preview"></a>
<p><strong><a href="styles/soft-analog-future-editorial-poster-style">Soft Analog Future Editorial Poster</a></strong><br>
<em>Quiet analog-future editorials with grids and retro technology.</em><br>
<a href="styles/soft-analog-future-editorial-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/soft-analog-future-editorial-poster-style.md">prompt</a> · <a href="styles/soft-analog-future-editorial-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="subway-doodle-photo-hybrid-style"></a>
<a href="styles/subway-doodle-photo-hybrid-style"><img src="styles/subway-doodle-photo-hybrid-style/preview-16x9.jpg" alt="Subway Doodle Photo Hybrid preview"></a>
<p><strong><a href="styles/subway-doodle-photo-hybrid-style">Subway Doodle Photo Hybrid</a></strong><br>
<em>Subway photos overlaid with social-media-style cartoon doodles and handwritten notes.</em><br>
<a href="styles/subway-doodle-photo-hybrid-style/style.json">style.json</a> · <a href="docs/copy-prompts/subway-doodle-photo-hybrid-style.md">prompt</a> · <a href="styles/subway-doodle-photo-hybrid-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="tokyo-kawaii-travel-collage-poster-style"></a>
<a href="styles/tokyo-kawaii-travel-collage-poster-style"><img src="styles/tokyo-kawaii-travel-collage-poster-style/preview-16x9.jpg" alt="Tokyo Kawaii Travel Collage Poster preview"></a>
<p><strong><a href="styles/tokyo-kawaii-travel-collage-poster-style">Tokyo Kawaii Travel Collage Poster</a></strong><br>
<em>Maximal Tokyo travel collages with manga bubbles and stickers.</em><br>
<a href="styles/tokyo-kawaii-travel-collage-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/tokyo-kawaii-travel-collage-poster-style.md">prompt</a> · <a href="styles/tokyo-kawaii-travel-collage-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="urban-transit-doodle-diary-style"></a>
<a href="styles/urban-transit-doodle-diary-style"><img src="styles/urban-transit-doodle-diary-style/preview-16x9.jpg" alt="Urban Transit Doodle Diary Style preview"></a>
<p><strong><a href="styles/urban-transit-doodle-diary-style">Urban Transit Doodle Diary Style</a></strong><br>
<em>Public-space photos remixed with bold foreground gestures and travel diary notes.</em><br>
<a href="styles/urban-transit-doodle-diary-style/style.json">style.json</a> · <a href="docs/copy-prompts/urban-transit-doodle-diary-style.md">prompt</a> · <a href="styles/urban-transit-doodle-diary-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="y2k-grunge-hiphop-cutout-poster-style"></a>
<a href="styles/y2k-grunge-hiphop-cutout-poster-style"><img src="styles/y2k-grunge-hiphop-cutout-poster-style/preview-16x9.jpg" alt="Y2K Grunge Hip-Hop Cutout Poster Style preview"></a>
<p><strong><a href="styles/y2k-grunge-hiphop-cutout-poster-style">Y2K Grunge Hip-Hop Cutout Poster Style</a></strong><br>
<em>Y2K hip-hop collage posters with acid type and photocopy grit.</em><br>
<a href="styles/y2k-grunge-hiphop-cutout-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/y2k-grunge-hiphop-cutout-poster-style.md">prompt</a> · <a href="styles/y2k-grunge-hiphop-cutout-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top"></td>
<td width="33%" valign="top"></td>
</tr>
</table>

## Publishing Model

- One directory = one style
- New styles appear first in Featured Styles and the All Styles gallery, with full descriptions added to [docs/CATALOG.md](docs/CATALOG.md)
- Main branch contains only `style.json` plus two preview JPGs per style
- Full galleries are not included in this repository
- Do not publish original reference images, watermarks, platform identifiers, QR codes, account handles, private prompts, or brand-owned assets without permission

## Contributing

New style submissions should follow the public package shape and validation rules in [CONTRIBUTING.md](CONTRIBUTING.md).

## Star History

<a href="https://star-history.com/#VigoZhao/AI-Visual-Prompt-Cookbook&Date">
  <picture>
    <source
      media="(prefers-color-scheme: dark)"
      srcset="https://api.star-history.com/svg?repos=VigoZhao/AI-Visual-Prompt-Cookbook&type=Date&theme=dark"
    >
    <source
      media="(prefers-color-scheme: light)"
      srcset="https://api.star-history.com/svg?repos=VigoZhao/AI-Visual-Prompt-Cookbook&type=Date"
    >
    <img
      alt="Star History Chart"
      src="https://api.star-history.com/svg?repos=VigoZhao/AI-Visual-Prompt-Cookbook&type=Date"
    >
  </picture>
</a>

## License

The repository structure and documentation are MIT licensed. Individual `style.json` files declare their own license. Preview images are included as visual references.
