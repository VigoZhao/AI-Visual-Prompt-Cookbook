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
  <img alt="Styles" src="https://img.shields.io/badge/styles-36-ff5a7a?style=flat-square">
  <img alt="Previews" src="https://img.shields.io/badge/previews-72-4cc9f0?style=flat-square">
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

## Quick Links

| Category | Good for | Start with |
| --- | --- | --- |
| Photo + Doodle | Social snapshots, lifestyle scenes, playful overlays | [Playful Mascot Doodle Snapshot](#playful-mascot-doodle-snapshot), [Subway Doodle Photo Hybrid](#subway-doodle-photo-hybrid) |
| Zine + Collage | Fashion posters, music visuals, maximalist editorial layouts | [K-pop Apocalypse Ransom Zine](#k-pop-apocalypse-ransom-zine), [Y2K Grunge Hip-hop Cutout Poster](#y2k-grunge-hiphop-cutout-poster) |
| Type Posters | Big headline systems, loud campaign graphics, visual punch | [Impact Burst Halftone Comic Poster](#impact-burst-halftone-comic-poster), [Neon Kinetic Typographic Poster](#neon-kinetic-typographic-poster) |
| Travel + City | Destination posters, street scenes, urban diaries | [Clean Triptych Travel Vlog Thumbnail](#clean-triptych-travel-vlog-thumbnail), [Tokyo Kawaii Travel Collage Poster](#tokyo-kawaii-travel-collage-poster) |
| Editorial + Minimal | Cleaner compositions, structured layouts, quieter art direction | [Tri Color Hardcut Portrait Poster](#tri-color-hardcut-portrait-poster), [Soft Analog Future Editorial Poster](#soft-analog-future-editorial-poster) |

## Why This Exists

Most AI image prompts are one-off text blobs: hard to reuse, hard to compare, and hard to iterate on. This repo takes a different approach: each visual style is distilled into a structured `style.json` you can drop into any LLM-based image generation workflow. Same JSON, more consistent style direction across generations.

## Quick Start

1. Browse the [Featured Styles](#featured-styles), [Quick Links](#quick-links), or [Style Index](#style-index).
2. Open a style folder and copy the `style.json`.
3. Paste the full JSON into ChatGPT, Claude, Nano Banana Pro, or any LLM-based image workflow.
4. Provide your own values for the variables declared in `environment_variables`, or edit a case in `examples[*].values`.
5. Generate the final image prompt and send it to your image model.

Example instruction:

```text
Use this style.json as the locked visual style.
Use these variable values:
SUBJECT = a streetwear product photographer
LOCATION = a rainy neon alley
MAIN_TEXT = NIGHT DROP
ASPECT_RATIO = 16:9
```

## Featured Styles

Six visual systems to understand the range of the library. Every style ships as one JSON plus two preview images.

<table>
<tr>
<td width="33%" valign="top">
<a href="styles/blue-hud-macro-product-poster"><img src="styles/blue-hud-macro-product-poster/preview-16x9.jpg" alt="Blue HUD Macro Creator Tech Poster preview"></a>
<h3>Blue HUD Macro Creator Tech Poster</h3>
<p>A glossy blue creator-tech launch poster style with macro 3D hardware heroes, oversized ribbed gloves, electric-cyan HUD glass panels, huge condensed white type, dense feature-card layering, and one warm gold performance badge.</p>
<p><a href="styles/blue-hud-macro-product-poster/style.json"><strong>Open style.json</strong></a> · <a href="styles/blue-hud-macro-product-poster">Folder</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/warm-fisheye-product-impact-ad-style"><img src="styles/warm-fisheye-product-impact-ad-style/preview-16x9.jpg" alt="Warm Fisheye Product Impact Ad preview"></a>
<h3>Warm Fisheye Product Impact Ad</h3>
<p>A dense Chinese social-commerce product ad style with macro fisheye product tunnels, close cropped hero products, giant slanted white Chinese headlines, warm caramel-brown lighting, blue callout tabs, bottom product strips, and glossy texture.</p>
<p><a href="styles/warm-fisheye-product-impact-ad-style/style.json"><strong>Open style.json</strong></a> · <a href="styles/warm-fisheye-product-impact-ad-style">Folder</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/olive-scribble-sports-poster-style"><img src="styles/olive-scribble-sports-poster-style/preview-16x9.jpg" alt="Olive Scribble Sports Poster preview"></a>
<h3>Olive Scribble Sports Poster</h3>
<p>A kinetic handmade sports poster style with off-white paper, irregular olive blocks, oversized diagonal action figures, rough black ink contours, red marker motion arcs, yellow-green dry-brush swaths, and screenprint texture.</p>
<p><a href="styles/olive-scribble-sports-poster-style/style.json"><strong>Open style.json</strong></a> · <a href="styles/olive-scribble-sports-poster-style">Folder</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a href="styles/bold-anime-reaction-thumbnail-style"><img src="styles/bold-anime-reaction-thumbnail-style/preview-16x9.jpg" alt="Bold Anime Reaction Thumbnail preview"></a>
<h3>Bold Anime Reaction Thumbnail</h3>
<p>A high-impact anime web-thumbnail style with oversized reaction characters, giant yellow-black headline type, split-screen framing, cyan glow reveals, and crisp cel-shaded illustration.</p>
<p><a href="styles/bold-anime-reaction-thumbnail-style/style.json"><strong>Open style.json</strong></a> · <a href="styles/bold-anime-reaction-thumbnail-style">Folder</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/turquoise-red-techno-manga-poster-style"><img src="styles/turquoise-red-techno-manga-poster-style/preview-16x9.jpg" alt="Turquoise Red Techno Manga Poster preview"></a>
<h3>Turquoise Red Techno Manga Poster</h3>
<p>A retro techno-manga poster style with cream paper, huge red-orange display type, turquoise technical clothing or hardware, dense mechanical linework, annotation panels, flat cel shading, and faded print grain.</p>
<p><a href="styles/turquoise-red-techno-manga-poster-style/style.json"><strong>Open style.json</strong></a> · <a href="styles/turquoise-red-techno-manga-poster-style">Folder</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/chromatic-fisheye-orbit-pop-poster-style"><img src="styles/chromatic-fisheye-orbit-pop-poster-style/preview-16x9.jpg" alt="Chromatic Fisheye Orbit Pop Poster preview"></a>
<h3>Chromatic Fisheye Orbit Pop Poster</h3>
<p>A high-key pop culture poster style with a convex fisheye photo dome, massive orbiting red-orange-magenta type, aqua refraction arcs, warm off-white negative space, and analog print grain.</p>
<p><a href="styles/chromatic-fisheye-orbit-pop-poster-style/style.json"><strong>Open style.json</strong></a> · <a href="styles/chromatic-fisheye-orbit-pop-poster-style">Folder</a></p>
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

## Style Index

1. [Blue HUD Macro Creator Tech Poster](#blue-hud-macro-creator-tech-poster)
2. [Warm Fisheye Product Impact Ad](#warm-fisheye-product-impact-ad)
3. [Olive Scribble Sports Poster](#olive-scribble-sports-poster)
4. [Bold Anime Reaction Thumbnail](#bold-anime-reaction-thumbnail)
5. [Turquoise Red Techno Manga Poster](#turquoise-red-techno-manga-poster)
6. [Chromatic Fisheye Orbit Pop Poster](#chromatic-fisheye-orbit-pop-poster)
7. [Naive Marker PSA Poster](#naive-marker-psa-poster)
8. [Blue Bubble Fisheye Action Poster](#blue-bubble-fisheye-action-poster)
9. [Cozy Bedroom Doodle Companion Snapshot](#cozy-bedroom-doodle-companion-snapshot)
10. [Surreal Fish Doodle Landmark Photo Collage](#surreal-fish-doodle-landmark-photo-collage)
11. [Plush Comic Toy Product Poster](#plush-comic-toy-product-poster)
12. [Rough Animation Pet Sketch Storyboard](#rough-animation-pet-sketch-storyboard)
13. [Tri Color Hardcut Portrait Poster](#tri-color-hardcut-portrait-poster)
14. [Clean Triptych Travel Vlog Thumbnail](#clean-triptych-travel-vlog-thumbnail)
15. [Playful Mascot Doodle Snapshot](#playful-mascot-doodle-snapshot)
16. [Teenage Skate Scribble Screenprint Poster](#teenage-skate-scribble-screenprint-poster)
17. [Impact Burst Halftone Comic Poster](#impact-burst-halftone-comic-poster)
18. [Sunburst Fisheye Bubble Type Poster](#sunburst-fisheye-bubble-type-poster)
19. [Backseat Transit Doodle Letter Poster](#backseat-transit-doodle-letter-poster)
20. [Analog Sticker Diary Portrait Poster](#analog-sticker-diary-portrait-poster)
21. [Folded Diamond Perspective Type Poster](#folded-diamond-perspective-type-poster)
22. [Gothic Cat Doodle Photo Collage](#gothic-cat-doodle-photo-collage)
23. [K-pop Apocalypse Ransom Zine](#k-pop-apocalypse-ransom-zine)
24. [Metro Doodle Snapshot Diary](#metro-doodle-snapshot-diary)
25. [Mountain Trail Monster Doodle Poster](#mountain-trail-monster-doodle-poster)
26. [Neon Doodle Gallery Snapshot](#neon-doodle-gallery-snapshot)
27. [Neon Kinetic Typographic Poster](#neon-kinetic-typographic-poster)
28. [Orange Brush Mascot Action Poster](#orange-brush-mascot-action-poster)
29. [Photo Illustration Overlay Poster](#photo-illustration-overlay-poster)
30. [Plush City Festival Mobile Poster](#plush-city-festival-mobile-poster)
31. [Pop Bubble Letter Photo Poster](#pop-bubble-letter-photo-poster)
32. [Soft Analog Future Editorial Poster](#soft-analog-future-editorial-poster)
33. [Subway Doodle Photo Hybrid](#subway-doodle-photo-hybrid)
34. [Tokyo Kawaii Travel Collage Poster](#tokyo-kawaii-travel-collage-poster)
35. [Urban Transit Doodle Diary](#urban-transit-doodle-diary)
36. [Y2K Grunge Hip-hop Cutout Poster](#y2k-grunge-hiphop-cutout-poster)

## Style Catalog

### Blue HUD Macro Creator Tech Poster

<a href="styles/blue-hud-macro-product-poster"><img src="styles/blue-hud-macro-product-poster/preview-16x9.jpg" width="720" alt="Blue HUD Macro Creator Tech Poster preview"></a>

A glossy blue creator-tech launch poster style with macro 3D hardware heroes, oversized ribbed gloves, electric-cyan HUD glass panels, huge condensed white type, dense feature-card layering, and one warm gold performance badge.

Files: [style.json](styles/blue-hud-macro-product-poster/style.json) · [16:9 preview](styles/blue-hud-macro-product-poster/preview-16x9.jpg) · [9:16 preview](styles/blue-hud-macro-product-poster/preview-9x16.jpg) · [Folder](styles/blue-hud-macro-product-poster)

---

### Warm Fisheye Product Impact Ad

<a href="styles/warm-fisheye-product-impact-ad-style"><img src="styles/warm-fisheye-product-impact-ad-style/preview-16x9.jpg" width="720" alt="Warm Fisheye Product Impact Ad preview"></a>

A dense Chinese social-commerce product ad style with macro fisheye product tunnels, close cropped hero products, giant slanted white Chinese headlines, warm caramel-brown lighting, blue callout tabs, bottom product strips, and glossy texture.

Files: [style.json](styles/warm-fisheye-product-impact-ad-style/style.json) · [16:9 preview](styles/warm-fisheye-product-impact-ad-style/preview-16x9.jpg) · [9:16 preview](styles/warm-fisheye-product-impact-ad-style/preview-9x16.jpg) · [folder](styles/warm-fisheye-product-impact-ad-style)

---

### Olive Scribble Sports Poster

<a href="styles/olive-scribble-sports-poster-style"><img src="styles/olive-scribble-sports-poster-style/preview-16x9.jpg" width="720" alt="Olive Scribble Sports Poster preview"></a>

A kinetic handmade sports poster style with off-white paper, irregular olive blocks, oversized diagonal action figures, rough black ink contours, red marker motion arcs, yellow-green dry-brush swaths, and screenprint texture.

Files: [style.json](styles/olive-scribble-sports-poster-style/style.json) · [16:9 preview](styles/olive-scribble-sports-poster-style/preview-16x9.jpg) · [9:16 preview](styles/olive-scribble-sports-poster-style/preview-9x16.jpg) · [folder](styles/olive-scribble-sports-poster-style)

---

### Bold Anime Reaction Thumbnail

<a href="styles/bold-anime-reaction-thumbnail-style"><img src="styles/bold-anime-reaction-thumbnail-style/preview-16x9.jpg" width="720" alt="Bold Anime Reaction Thumbnail preview"></a>

A high-impact anime web-thumbnail style built from oversized reaction characters, bold yellow headline typography with hard black shadows, split-screen framing, a smaller glowing action insert, cool blue/cyan backgrounds, and clean cel-shaded illustration.

Files: [style.json](styles/bold-anime-reaction-thumbnail-style/style.json) · [16:9 preview](styles/bold-anime-reaction-thumbnail-style/preview-16x9.jpg) · [9:16 preview](styles/bold-anime-reaction-thumbnail-style/preview-9x16.jpg) · [folder](styles/bold-anime-reaction-thumbnail-style)

---

### Turquoise Red Techno Manga Poster

<a href="styles/turquoise-red-techno-manga-poster-style"><img src="styles/turquoise-red-techno-manga-poster-style/preview-16x9.jpg" width="720" alt="Turquoise Red Techno Manga Poster preview"></a>

A retro techno-manga poster style built from a cream paper ground, huge red-orange display lettering, turquoise technical clothing or hardware, dense mechanical linework, annotation panels, flat cel-shaded figure drawing, and slightly faded printed texture.

Files: [style.json](styles/turquoise-red-techno-manga-poster-style/style.json) · [16:9 preview](styles/turquoise-red-techno-manga-poster-style/preview-16x9.jpg) · [9:16 preview](styles/turquoise-red-techno-manga-poster-style/preview-9x16.jpg) · [folder](styles/turquoise-red-techno-manga-poster-style)

---

### Chromatic Fisheye Orbit Pop Poster

<a href="styles/chromatic-fisheye-orbit-pop-poster-style"><img src="styles/chromatic-fisheye-orbit-pop-poster-style/preview-16x9.jpg" width="720" alt="Chromatic Fisheye Orbit Pop Poster preview"></a>

A high-key pop culture poster style built from extreme fisheye photography, a convex glass-dome center, oversized orbiting typography, hot red-magenta-orange letter fills, aqua chromatic light arcs, warm off-white negative space, and light analog print texture.

Files: [style.json](styles/chromatic-fisheye-orbit-pop-poster-style/style.json) · [16:9 preview](styles/chromatic-fisheye-orbit-pop-poster-style/preview-16x9.jpg) · [9:16 preview](styles/chromatic-fisheye-orbit-pop-poster-style/preview-9x16.jpg) · [folder](styles/chromatic-fisheye-orbit-pop-poster-style)

---

### Naive Marker PSA Poster

<a href="styles/naive-marker-psa-poster-style"><img src="styles/naive-marker-psa-poster-style/preview-16x9.jpg" width="720" alt="Naive Marker PSA Poster preview"></a>

A friendly hand-drawn public-service poster style built from chunky irregular marker outlines, oversized blue-bordered speech-panel typography, simplified cartoon people, flattened civic props, pastel paper backgrounds, warning-sign motifs, and intentionally naive perspective.

Files: [style.json](styles/naive-marker-psa-poster-style/style.json) · [16:9 preview](styles/naive-marker-psa-poster-style/preview-16x9.jpg) · [9:16 preview](styles/naive-marker-psa-poster-style/preview-9x16.jpg) · [folder](styles/naive-marker-psa-poster-style)

---

### Blue Bubble Fisheye Action Poster

<a href="styles/blue-bubble-fisheye-action-poster-style"><img src="styles/blue-bubble-fisheye-action-poster-style/preview-16x9.jpg" width="720" alt="Blue Bubble Fisheye Action Poster preview"></a>

A crisp white youth-culture action poster style with a rectangular fisheye photograph, oversized rounded royal-blue display typography, frame-breaking foreground scale, small blue editorial captions, and one red hand-drawn annotation circle.

Files: [style.json](styles/blue-bubble-fisheye-action-poster-style/style.json) · [16:9 preview](styles/blue-bubble-fisheye-action-poster-style/preview-16x9.jpg) · [9:16 preview](styles/blue-bubble-fisheye-action-poster-style/preview-9x16.jpg) · [folder](styles/blue-bubble-fisheye-action-poster-style)

---

### Cozy Bedroom Doodle Companion Snapshot

<a href="styles/cozy-bedroom-doodle-companion-snapshot-style"><img src="styles/cozy-bedroom-doodle-companion-snapshot-style/preview-16x9.jpg" width="720" alt="Cozy Bedroom Doodle Companion Snapshot preview"></a>

A candid low-light home photo style with a large flat 2D cushion-doll companion composited into the lower foreground, creating a quiet late-night creative diary mood with warm room texture, screen glow, and tiny handwritten doodle marks.

Files: [style.json](styles/cozy-bedroom-doodle-companion-snapshot-style/style.json) · [16:9 preview](styles/cozy-bedroom-doodle-companion-snapshot-style/preview-16x9.jpg) · [9:16 preview](styles/cozy-bedroom-doodle-companion-snapshot-style/preview-9x16.jpg) · [folder](styles/cozy-bedroom-doodle-companion-snapshot-style)

---

### Surreal Fish Doodle Landmark Photo Collage

<a href="styles/surreal-fish-doodle-landmark-photo-collage-style"><img src="styles/surreal-fish-doodle-landmark-photo-collage-style/preview-16x9.jpg" width="720" alt="Surreal Fish Doodle Landmark Photo Collage preview"></a>

A bright travel-photo collage style that overlays giant flat 2D cartoon travelers, fantastical folk-art fish, black marker loops, splash marks, and comic starbursts onto realistic landmark photography.

Files: [style.json](styles/surreal-fish-doodle-landmark-photo-collage-style/style.json) · [16:9 preview](styles/surreal-fish-doodle-landmark-photo-collage-style/preview-16x9.jpg) · [9:16 preview](styles/surreal-fish-doodle-landmark-photo-collage-style/preview-9x16.jpg) · [folder](styles/surreal-fish-doodle-landmark-photo-collage-style)

---

### Plush Comic Toy Product Poster

<a href="styles/plush-comic-toy-product-poster-style"><img src="styles/plush-comic-toy-product-poster-style/preview-16x9.jpg" width="720" alt="Plush Comic Toy Product Poster preview"></a>

A loud toy-product poster style built around a tactile fuzzy plush product hero, retro cream poster paper, cyan circular backdrop, oversized slanted comic typography, thick black shadows, doodle annotations, sticker labels, and campaign microcopy.

Files: [style.json](styles/plush-comic-toy-product-poster-style/style.json) · [16:9 preview](styles/plush-comic-toy-product-poster-style/preview-16x9.jpg) · [9:16 preview](styles/plush-comic-toy-product-poster-style/preview-9x16.jpg) · [folder](styles/plush-comic-toy-product-poster-style)

---

### Rough Animation Pet Sketch Storyboard

<a href="styles/rough-animation-pet-sketch-storyboard-style"><img src="styles/rough-animation-pet-sketch-storyboard-style/preview-16x9.jpg" width="720" alt="Rough Animation Pet Sketch Storyboard preview"></a>

A loose animation pet-comedy storyboard style with warm beige paper, red-brown construction lines, scratchy burgundy contours, semi-transparent color wash, lightly sketched interiors, and oversized animal expressions.

Files: [style.json](styles/rough-animation-pet-sketch-storyboard-style/style.json) · [16:9 preview](styles/rough-animation-pet-sketch-storyboard-style/preview-16x9.jpg) · [9:16 preview](styles/rough-animation-pet-sketch-storyboard-style/preview-9x16.jpg) · [folder](styles/rough-animation-pet-sketch-storyboard-style)

---

### Tri Color Hardcut Portrait Poster

<a href="styles/tri-color-hardcut-portrait-poster-style"><img src="styles/tri-color-hardcut-portrait-poster-style/preview-16x9.jpg" width="720" alt="Tri Color Hardcut Portrait Poster preview"></a>

A clean three-color hardcut portrait poster style using flat teal background fields, coral-red subject planes, and near-black silhouettes or shadows, with all detail reduced into large hard-edged vector-like cutouts.

Files: [style.json](styles/tri-color-hardcut-portrait-poster-style/style.json) · [16:9 preview](styles/tri-color-hardcut-portrait-poster-style/preview-16x9.jpg) · [9:16 preview](styles/tri-color-hardcut-portrait-poster-style/preview-9x16.jpg) · [folder](styles/tri-color-hardcut-portrait-poster-style)

---

### Clean Triptych Travel Vlog Thumbnail

<a href="styles/clean-triptych-travel-vlog-thumbnail-style"><img src="styles/clean-triptych-travel-vlog-thumbnail-style/preview-16x9.jpg" width="720" alt="Clean Triptych Travel Vlog Thumbnail preview"></a>

A clean travel-vlog thumbnail system built from three vertical photographic panels, oversized lowercase white destination type, small italic travel annotations, sparse hand-drawn marks, and a soft phone-camera editorial finish.

Files: [style.json](styles/clean-triptych-travel-vlog-thumbnail-style/style.json) · [16:9 preview](styles/clean-triptych-travel-vlog-thumbnail-style/preview-16x9.jpg) · [9:16 preview](styles/clean-triptych-travel-vlog-thumbnail-style/preview-9x16.jpg) · [folder](styles/clean-triptych-travel-vlog-thumbnail-style)

---

### Playful Mascot Doodle Snapshot

<a href="styles/playful-mascot-doodle-snapshot-style"><img src="styles/playful-mascot-doodle-snapshot-style/preview-16x9.jpg" width="720" alt="Playful Mascot Doodle Snapshot preview"></a>

A casual real-life social photo transformed into a playful poster by layering original cartoon mascot stickers, hand-drawn outlines, ribbon headline panels, sparkles, spirals, and sketchy decorative marks over the photographic scene.

Files: [style.json](styles/playful-mascot-doodle-snapshot-style/style.json) · [16:9 preview](styles/playful-mascot-doodle-snapshot-style/preview-16x9.jpg) · [9:16 preview](styles/playful-mascot-doodle-snapshot-style/preview-9x16.jpg) · [folder](styles/playful-mascot-doodle-snapshot-style)

---

### Teenage Skate Scribble Screenprint Poster

<a href="styles/teenage-skate-scribble-screenprint-poster-style"><img src="styles/teenage-skate-scribble-screenprint-poster-style/preview-16x9.jpg" width="720" alt="Teenage Skate Scribble Screenprint Poster preview"></a>

A retro skate zine poster style with a distorted central skateboarder cutout, cream paper field, loose red hand-lettered border typography, rough duotone screen-print texture, and a limited navy-gray-green-ochre palette.

Files: [style.json](styles/teenage-skate-scribble-screenprint-poster-style/style.json) · [16:9 preview](styles/teenage-skate-scribble-screenprint-poster-style/preview-16x9.jpg) · [9:16 preview](styles/teenage-skate-scribble-screenprint-poster-style/preview-9x16.jpg) · [folder](styles/teenage-skate-scribble-screenprint-poster-style)

---

### Impact Burst Halftone Comic Poster

<a href="styles/impact-burst-halftone-comic-poster-style"><img src="styles/impact-burst-halftone-comic-poster-style/preview-16x9.jpg" width="720" alt="Impact Burst Halftone Comic Poster preview"></a>

A loud retro comic poster system built from thick black ink, flat high-saturation colors, oversized impact typography, exaggerated illustrated subjects, diagonal props, speech bursts, smoke puffs, halftone dots, and distressed screen-print grain.

Files: [style.json](styles/impact-burst-halftone-comic-poster-style/style.json) · [16:9 preview](styles/impact-burst-halftone-comic-poster-style/preview-16x9.jpg) · [9:16 preview](styles/impact-burst-halftone-comic-poster-style/preview-9x16.jpg) · [folder](styles/impact-burst-halftone-comic-poster-style)

---

### Sunburst Fisheye Bubble Type Poster

<a href="styles/sunburst-fisheye-bubble-type-poster-style"><img src="styles/sunburst-fisheye-bubble-type-poster-style/preview-16x9.jpg" width="720" alt="Sunburst Fisheye Bubble Type Poster preview"></a>

An ultra-low-angle fisheye summer lifestyle poster style with a close photographic subject, saturated cobalt sky, huge arched lemon-yellow bubble typography, warm orange type shading, Y2K accessories, and heavy analog grain.

Files: [style.json](styles/sunburst-fisheye-bubble-type-poster-style/style.json) · [16:9 preview](styles/sunburst-fisheye-bubble-type-poster-style/preview-16x9.jpg) · [9:16 preview](styles/sunburst-fisheye-bubble-type-poster-style/preview-9x16.jpg) · [folder](styles/sunburst-fisheye-bubble-type-poster-style)

---

### Backseat Transit Doodle Letter Poster

<a href="styles/backseat-transit-doodle-letter-poster-style"><img src="styles/backseat-transit-doodle-letter-poster-style/preview-16x9.jpg" width="720" alt="Backseat Transit Doodle Letter Poster preview"></a>

A realistic passenger-seat transport photo transformed into a high-energy travel poster with a central rear-view subject, electric yellow silhouette halo, oversized yellow-orange hand-drawn letters, comic rays, purple music marks, sticker icons, and cyan-white cloud swooshes.

Files: [style.json](styles/backseat-transit-doodle-letter-poster-style/style.json) · [16:9 preview](styles/backseat-transit-doodle-letter-poster-style/preview-16x9.jpg) · [9:16 preview](styles/backseat-transit-doodle-letter-poster-style/preview-9x16.jpg) · [folder](styles/backseat-transit-doodle-letter-poster-style)

---

### Analog Sticker Diary Portrait Poster

<a href="styles/analog-sticker-diary-portrait-poster-style"><img src="styles/analog-sticker-diary-portrait-poster-style/preview-16x9.jpg" width="720" alt="Analog Sticker Diary Portrait Poster preview"></a>

A nostalgic analog diary-collage portrait system with a large side-profile illustrated subject, cream graph-paper background, sticker-like personal objects, distressed orange hand lettering, and heavy scanned print texture.

Files: [style.json](styles/analog-sticker-diary-portrait-poster-style/style.json) · [16:9 preview](styles/analog-sticker-diary-portrait-poster-style/preview-16x9.jpg) · [9:16 preview](styles/analog-sticker-diary-portrait-poster-style/preview-9x16.jpg) · [folder](styles/analog-sticker-diary-portrait-poster-style)

---

### Folded Diamond Perspective Type Poster

<a href="styles/folded-diamond-perspective-type-poster-style"><img src="styles/folded-diamond-perspective-type-poster-style/preview-16x9.jpg" width="720" alt="Folded Diamond Perspective Type Poster preview"></a>

A bold minimalist editorial poster style using low-angle hero photography inside a diamond aperture, folded tan paper or canvas planes, and oversized white perspective typography printed across the lower surface.

Files: [style.json](styles/folded-diamond-perspective-type-poster-style/style.json) · [16:9 preview](styles/folded-diamond-perspective-type-poster-style/preview-16x9.jpg) · [9:16 preview](styles/folded-diamond-perspective-type-poster-style/preview-9x16.jpg) · [folder](styles/folded-diamond-perspective-type-poster-style)

---

### Gothic Cat Doodle Photo Collage

<a href="styles/gothic-cat-doodle-photo-collage-style"><img src="styles/gothic-cat-doodle-photo-collage-style/preview-16x9.jpg" width="720" alt="Gothic Cat Doodle Photo Collage preview"></a>

A playful photo-illustration collage style combining dramatic real architectural photography with oversized flat cartoon creature overlays, bubbly hand-drawn headline lettering, and loose marker doodles.

Files: [style.json](styles/gothic-cat-doodle-photo-collage-style/style.json) · [16:9 preview](styles/gothic-cat-doodle-photo-collage-style/preview-16x9.jpg) · [9:16 preview](styles/gothic-cat-doodle-photo-collage-style/preview-9x16.jpg) · [folder](styles/gothic-cat-doodle-photo-collage-style)

---

### K-pop Apocalypse Ransom Zine

<a href="styles/k-pop-apocalypse-ransom-zine-style"><img src="styles/k-pop-apocalypse-ransom-zine-style/preview-16x9.jpg" width="720" alt="K-pop Apocalypse Ransom Zine preview"></a>

A maximalist K-pop fashion zine collage style built from a central portrait cutout, crumpled monochrome paper texture, skewed ransom-note typography, loud sticker blocks, saturated lime/blue/red accents, and a bold bottom masthead band.

Files: [style.json](styles/k-pop-apocalypse-ransom-zine-style/style.json) · [16:9 preview](styles/k-pop-apocalypse-ransom-zine-style/preview-16x9.jpg) · [9:16 preview](styles/k-pop-apocalypse-ransom-zine-style/preview-9x16.jpg) · [folder](styles/k-pop-apocalypse-ransom-zine-style)

---

### Metro Doodle Snapshot Diary

<a href="styles/metro-doodle-snapshot-diary-style"><img src="styles/metro-doodle-snapshot-diary-style/preview-16x9.jpg" width="720" alt="Metro Doodle Snapshot Diary preview"></a>

A handheld urban transit photo-collage style combining realistic crowded metro, bus, tram, or station snapshots with expressive marker-like cartoon doodles, oversized foreground gestures, white handwritten diary notes, and saturated comic face overlays.

Files: [style.json](styles/metro-doodle-snapshot-diary-style/style.json) · [16:9 preview](styles/metro-doodle-snapshot-diary-style/preview-16x9.jpg) · [9:16 preview](styles/metro-doodle-snapshot-diary-style/preview-9x16.jpg) · [folder](styles/metro-doodle-snapshot-diary-style)

---

### Mountain Trail Monster Doodle Poster

<a href="styles/mountain-trail-monster-doodle-poster-style"><img src="styles/mountain-trail-monster-doodle-poster-style/preview-16x9.jpg" width="720" alt="Mountain Trail Monster Doodle Poster preview"></a>

A candid outdoor hiking photograph remixed with a flat hand-drawn monster companion, oversized Spanish comic lettering, and loose sketch annotations, creating a playful adventure-poster collage.

Files: [style.json](styles/mountain-trail-monster-doodle-poster-style/style.json) · [16:9 preview](styles/mountain-trail-monster-doodle-poster-style/preview-16x9.jpg) · [9:16 preview](styles/mountain-trail-monster-doodle-poster-style/preview-9x16.jpg) · [folder](styles/mountain-trail-monster-doodle-poster-style)

---

### Neon Doodle Gallery Snapshot

<a href="styles/neon-doodle-gallery-snapshot-style"><img src="styles/neon-doodle-gallery-snapshot-style/preview-16x9.jpg" width="720" alt="Neon Doodle Gallery Snapshot preview"></a>

A candid phone-photo style layered with chaotic neon digital marker doodles: hot-pink and cyan subject outlines, yellow monster spikes, rough handwritten captions, stars, paw prints, spiderweb corners, scribble bars, halos, plants, and student diary energy.

Files: [style.json](styles/neon-doodle-gallery-snapshot-style/style.json) · [16:9 preview](styles/neon-doodle-gallery-snapshot-style/preview-16x9.jpg) · [9:16 preview](styles/neon-doodle-gallery-snapshot-style/preview-9x16.jpg) · [folder](styles/neon-doodle-gallery-snapshot-style)

---

### Neon Kinetic Typographic Poster

<a href="styles/neon-kinetic-typographic-poster-style"><img src="styles/neon-kinetic-typographic-poster-style/preview-16x9.jpg" width="720" alt="Neon Kinetic Typographic Poster preview"></a>

A dramatic outdoor editorial poster style combining low-angle lifestyle photography, oversized warped neon typography, film grain, and high-energy youth-culture campaign design.

Files: [style.json](styles/neon-kinetic-typographic-poster-style/style.json) · [16:9 preview](styles/neon-kinetic-typographic-poster-style/preview-16x9.jpg) · [9:16 preview](styles/neon-kinetic-typographic-poster-style/preview-9x16.jpg) · [folder](styles/neon-kinetic-typographic-poster-style)

---

### Orange Brush Mascot Action Poster

<a href="styles/orange-brush-mascot-action-poster-style"><img src="styles/orange-brush-mascot-action-poster-style/preview-16x9.jpg" width="720" alt="Orange Brush Mascot Action Poster preview"></a>

A sparse orange-white-black flat illustration system with a white mascot figure, oversized prop, rough black dry-brush linework, orange cheek circles, and screen-printed paper grain.

Files: [style.json](styles/orange-brush-mascot-action-poster-style/style.json) · [16:9 preview](styles/orange-brush-mascot-action-poster-style/preview-16x9.jpg) · [9:16 preview](styles/orange-brush-mascot-action-poster-style/preview-9x16.jpg) · [folder](styles/orange-brush-mascot-action-poster-style)

---

### Photo Illustration Overlay Poster

<a href="styles/photo-illustration-overlay-poster-style"><img src="styles/photo-illustration-overlay-poster-style/preview-16x9.jpg" width="720" alt="Photo Illustration Overlay Poster preview"></a>

A realistic city photograph with an oversized, high-saturation, flat 2D cartoon figure composited on top, plus hand-drawn stars, sparks, arrows, and comic marks.

Files: [style.json](styles/photo-illustration-overlay-poster-style/style.json) · [16:9 preview](styles/photo-illustration-overlay-poster-style/preview-16x9.jpg) · [9:16 preview](styles/photo-illustration-overlay-poster-style/preview-9x16.jpg) · [folder](styles/photo-illustration-overlay-poster-style)

---

### Plush City Festival Mobile Poster

<a href="styles/plush-city-festival-mobile-poster-style"><img src="styles/plush-city-festival-mobile-poster-style/preview-16x9.jpg" width="720" alt="Plush City Festival Mobile Poster preview"></a>

A bright mobile event poster style combining real city landmarks, soft fuzzy mascot characters, rounded app-card UI framing, bold white festival typography, date/location text, and friendly tourism-campaign energy.

Files: [style.json](styles/plush-city-festival-mobile-poster-style/style.json) · [16:9 preview](styles/plush-city-festival-mobile-poster-style/preview-16x9.jpg) · [9:16 preview](styles/plush-city-festival-mobile-poster-style/preview-9x16.jpg) · [folder](styles/plush-city-festival-mobile-poster-style)

---

### Pop Bubble Letter Photo Poster

<a href="styles/pop-bubble-letter-photo-poster-style"><img src="styles/pop-bubble-letter-photo-poster-style/preview-16x9.jpg" width="720" alt="Pop Bubble Letter Photo Poster preview"></a>

A punchy photo-and-illustration poster style built around a central low-angle fashion portrait framed by oversized flat bubble-letter shapes, saturated candy colors, thick black outlines, oval highlights, and crisp sparkle marks.

Files: [style.json](styles/pop-bubble-letter-photo-poster-style/style.json) · [16:9 preview](styles/pop-bubble-letter-photo-poster-style/preview-16x9.jpg) · [9:16 preview](styles/pop-bubble-letter-photo-poster-style/preview-9x16.jpg) · [folder](styles/pop-bubble-letter-photo-poster-style)

---

### Soft Analog Future Editorial Poster

<a href="styles/soft-analog-future-editorial-poster-style"><img src="styles/soft-analog-future-editorial-poster-style/preview-16x9.jpg" width="720" alt="Soft Analog Future Editorial Poster preview"></a>

A quiet analog-future editorial poster style using warm cream paper, oversized black neo-grotesk typography, strict grid rules, retro technology still life, pale-blue translucent interface panels, botanical foreground accents, and tiny bilingual information design.

Files: [style.json](styles/soft-analog-future-editorial-poster-style/style.json) · [16:9 preview](styles/soft-analog-future-editorial-poster-style/preview-16x9.jpg) · [9:16 preview](styles/soft-analog-future-editorial-poster-style/preview-9x16.jpg) · [folder](styles/soft-analog-future-editorial-poster-style)

---

### Subway Doodle Photo Hybrid

<a href="styles/subway-doodle-photo-hybrid-style"><img src="styles/subway-doodle-photo-hybrid-style/preview-16x9.jpg" width="720" alt="Subway Doodle Photo Hybrid preview"></a>

A phone-shot urban transit poster style combining documentary subway or street transport photography with expressive hand-drawn cartoon overlays, doodled character faces, oversized foreground gestures, handwritten notes, and social media screenshot texture.

Files: [style.json](styles/subway-doodle-photo-hybrid-style/style.json) · [16:9 preview](styles/subway-doodle-photo-hybrid-style/preview-16x9.jpg) · [9:16 preview](styles/subway-doodle-photo-hybrid-style/preview-9x16.jpg) · [folder](styles/subway-doodle-photo-hybrid-style)

---

### Tokyo Kawaii Travel Collage Poster

<a href="styles/tokyo-kawaii-travel-collage-poster-style"><img src="styles/tokyo-kawaii-travel-collage-poster-style/preview-16x9.jpg" width="720" alt="Tokyo Kawaii Travel Collage Poster preview"></a>

A maximalist Japanese city-travel collage style with bold destination typography, cute sticker elements, manga speech bubbles, cutout fashion photography, halftone urban backgrounds, and scrapbook editorial layout.

Files: [style.json](styles/tokyo-kawaii-travel-collage-poster-style/style.json) · [16:9 preview](styles/tokyo-kawaii-travel-collage-poster-style/preview-16x9.jpg) · [9:16 preview](styles/tokyo-kawaii-travel-collage-poster-style/preview-9x16.jpg) · [folder](styles/tokyo-kawaii-travel-collage-poster-style)

---

### Urban Transit Doodle Diary

<a href="styles/urban-transit-doodle-diary-style"><img src="styles/urban-transit-doodle-diary-style/preview-16x9.jpg" width="720" alt="Urban Transit Doodle Diary preview"></a>

A raw urban snapshot treated like a personal visual diary, combining real public-space photography with bold hand-drawn comic overlays, handwritten travel notes, saturated cartoon faces, and a large foreground gesture.

Files: [style.json](styles/urban-transit-doodle-diary-style/style.json) · [16:9 preview](styles/urban-transit-doodle-diary-style/preview-16x9.jpg) · [9:16 preview](styles/urban-transit-doodle-diary-style/preview-9x16.jpg) · [folder](styles/urban-transit-doodle-diary-style)

---

### Y2K Grunge Hip-hop Cutout Poster

<a href="styles/y2k-grunge-hiphop-cutout-poster-style"><img src="styles/y2k-grunge-hiphop-cutout-poster-style/preview-16x9.jpg" width="720" alt="Y2K Grunge Hip-hop Cutout Poster preview"></a>

A Y2K grunge hip-hop magazine collage poster style built from oversized photo cutouts, acid yellow retro typography, rough black-and-white wall textures, dense editorial footer panels, and photocopied print noise.

Files: [style.json](styles/y2k-grunge-hiphop-cutout-poster-style/style.json) · [16:9 preview](styles/y2k-grunge-hiphop-cutout-poster-style/preview-16x9.jpg) · [9:16 preview](styles/y2k-grunge-hiphop-cutout-poster-style/preview-9x16.jpg) · [folder](styles/y2k-grunge-hiphop-cutout-poster-style)

## Publishing Model

- One directory = one style
- New styles appear first in Featured Styles and Style Index
- Main branch contains only `style.json` plus two preview JPGs per style
- Full galleries are not included in this repository
- Do not publish original reference images, watermarks, platform identifiers, QR codes, account handles, private prompts, or brand-owned assets without permission

## License

The repository structure and documentation are MIT licensed. Individual `style.json` files declare their own license. Preview images are included as visual references.
