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
  <img alt="Styles" src="https://img.shields.io/badge/styles-22-ff5a7a?style=flat-square">
  <img alt="Previews" src="https://img.shields.io/badge/previews-44-4cc9f0?style=flat-square">
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
| Travel + City | Destination posters, street scenes, urban diaries | [Tokyo Kawaii Travel Collage Poster](#tokyo-kawaii-travel-collage-poster), [Urban Transit Doodle Diary](#urban-transit-doodle-diary) |
| Editorial + Minimal | Cleaner compositions, structured layouts, quieter art direction | [Soft Analog Future Editorial Poster](#soft-analog-future-editorial-poster), [Folded Diamond Perspective Type Poster](#folded-diamond-perspective-type-poster) |

## Why This Exists

Most AI image prompts are one-off text blobs: hard to reuse, hard to compare, and hard to iterate on. This repo takes a different approach: each visual style is distilled into a structured `style.json` you can drop into any LLM-based image generation workflow. Same JSON, more consistent style direction across generations.

## Quick Start

1. Browse the [Featured Styles](#featured-styles), [Quick Links](#quick-links), or [Style Index](#style-index).
2. Open a style folder and copy the `style.json`.
3. Paste the full JSON into ChatGPT, Claude, Nano Banana Pro, or any LLM-based image workflow.
4. Change only the `variables` values for your own subject, scene, text, and aspect ratio.
5. Generate the final image prompt and send it to your image model.

Example instruction:

```text
Use this style.json as the locked visual style.
Replace only the variables:
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
<a href="styles/k-pop-apocalypse-ransom-zine-style"><img src="styles/k-pop-apocalypse-ransom-zine-style/preview-16x9.jpg" alt="K-pop Apocalypse Ransom Zine preview"></a>
<h3>K-pop Apocalypse Ransom Zine</h3>
<p>Maximalist fashion zine collage with cutout portraits, ransom-note typography, crumpled paper, sticker blocks, and loud accent color.</p>
<p><a href="styles/k-pop-apocalypse-ransom-zine-style/style.json"><strong>Open style.json</strong></a> · <a href="styles/k-pop-apocalypse-ransom-zine-style">Folder</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/impact-burst-halftone-comic-poster-style"><img src="styles/impact-burst-halftone-comic-poster-style/preview-16x9.jpg" alt="Impact Burst Halftone Comic Poster preview"></a>
<h3>Impact Burst Halftone Comic Poster</h3>
<p>A loud retro comic poster system with thick ink, high-saturation color, oversized impact typography, speech bursts, and screen-print grain.</p>
<p><a href="styles/impact-burst-halftone-comic-poster-style/style.json"><strong>Open style.json</strong></a> · <a href="styles/impact-burst-halftone-comic-poster-style">Folder</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/playful-mascot-doodle-snapshot-style"><img src="styles/playful-mascot-doodle-snapshot-style/preview-16x9.jpg" alt="Playful Mascot Doodle Snapshot preview"></a>
<h3>Playful Mascot Doodle Snapshot</h3>
<p>A casual real-life social photo transformed into a playful poster by layering original cartoon mascot stickers, hand-drawn outlines, ribbon headline panels, sparkles, spirals, and sketchy decorative marks over the photographic scene.</p>
<p><a href="styles/playful-mascot-doodle-snapshot-style/style.json"><strong>Open style.json</strong></a> · <a href="styles/playful-mascot-doodle-snapshot-style">Folder</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a href="styles/teenage-skate-scribble-screenprint-poster-style"><img src="styles/teenage-skate-scribble-screenprint-poster-style/preview-16x9.jpg" alt="Teenage Skate Scribble Screenprint Poster preview"></a>
<h3>Teenage Skate Scribble Screenprint Poster</h3>
<p>A retro skate zine poster style with a distorted central skateboarder cutout, cream paper field, loose red hand-lettered border typography, rough duotone screen-print texture, and a limited navy-gray-green-ochre palette.</p>
<p><a href="styles/teenage-skate-scribble-screenprint-poster-style/style.json"><strong>Open style.json</strong></a> · <a href="styles/teenage-skate-scribble-screenprint-poster-style">Folder</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/neon-kinetic-typographic-poster-style"><img src="styles/neon-kinetic-typographic-poster-style/preview-16x9.jpg" alt="Neon Kinetic Typographic Poster preview"></a>
<h3>Neon Kinetic Typographic Poster</h3>
<p>Dramatic outdoor editorial design with low-angle photography, warped neon type, film grain, and youth-culture campaign energy.</p>
<p><a href="styles/neon-kinetic-typographic-poster-style/style.json"><strong>Open style.json</strong></a> · <a href="styles/neon-kinetic-typographic-poster-style">Folder</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/tokyo-kawaii-travel-collage-poster-style"><img src="styles/tokyo-kawaii-travel-collage-poster-style/preview-16x9.jpg" alt="Tokyo Kawaii Travel Collage Poster preview"></a>
<h3>Tokyo Kawaii Travel Collage Poster</h3>
<p>A maximalist city-travel collage with destination type, stickers, speech bubbles, cutout photography, and scrapbook editorial layout.</p>
<p><a href="styles/tokyo-kawaii-travel-collage-poster-style/style.json"><strong>Open style.json</strong></a> · <a href="styles/tokyo-kawaii-travel-collage-poster-style">Folder</a></p>
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

## Style Index

1. [Playful Mascot Doodle Snapshot](#playful-mascot-doodle-snapshot)
2. [Teenage Skate Scribble Screenprint Poster](#teenage-skate-scribble-screenprint-poster)
3. [Impact Burst Halftone Comic Poster](#impact-burst-halftone-comic-poster)
4. [Sunburst Fisheye Bubble Type Poster](#sunburst-fisheye-bubble-type-poster)
5. [Backseat Transit Doodle Letter Poster](#backseat-transit-doodle-letter-poster)
6. [Analog Sticker Diary Portrait Poster](#analog-sticker-diary-portrait-poster)
7. [Folded Diamond Perspective Type Poster](#folded-diamond-perspective-type-poster)
8. [Gothic Cat Doodle Photo Collage](#gothic-cat-doodle-photo-collage)
9. [K-pop Apocalypse Ransom Zine](#k-pop-apocalypse-ransom-zine)
10. [Metro Doodle Snapshot Diary](#metro-doodle-snapshot-diary)
11. [Mountain Trail Monster Doodle Poster](#mountain-trail-monster-doodle-poster)
12. [Neon Doodle Gallery Snapshot](#neon-doodle-gallery-snapshot)
13. [Neon Kinetic Typographic Poster](#neon-kinetic-typographic-poster)
14. [Orange Brush Mascot Action Poster](#orange-brush-mascot-action-poster)
15. [Photo Illustration Overlay Poster](#photo-illustration-overlay-poster)
16. [Plush City Festival Mobile Poster](#plush-city-festival-mobile-poster)
17. [Pop Bubble Letter Photo Poster](#pop-bubble-letter-photo-poster)
18. [Soft Analog Future Editorial Poster](#soft-analog-future-editorial-poster)
19. [Subway Doodle Photo Hybrid](#subway-doodle-photo-hybrid)
20. [Tokyo Kawaii Travel Collage Poster](#tokyo-kawaii-travel-collage-poster)
21. [Urban Transit Doodle Diary](#urban-transit-doodle-diary)
22. [Y2K Grunge Hip-hop Cutout Poster](#y2k-grunge-hiphop-cutout-poster)

## Style Catalog

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
