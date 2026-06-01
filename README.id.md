<h1 align="center">AI Visual Prompt Cookbook</h1>

<p align="center">
  <img src="assets/hero-collage.jpg" alt="AI Visual Prompt Cookbook showcase">
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.zh-TW.md">繁體中文</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.ko.md">한국어</a> |
  Bahasa Indonesia
</p>

<p align="center">
  <img alt="Styles" src="https://img.shields.io/badge/styles-49-ff5a7a?style=flat-square">
  <img alt="Previews" src="https://img.shields.io/badge/previews-98-4cc9f0?style=flat-square">
  <img alt="Format" src="https://img.shields.io/badge/format-style.json-111111?style=flat-square">
  <img alt="Languages" src="https://img.shields.io/badge/languages-6-f7b801?style=flat-square">
</p>

<p align="center">
  <strong>Salin satu JSON, dapatkan satu gaya.</strong> Masukkan <code>style.json</code> ke ChatGPT, Claude, Nano Banana Pro, atau workflow gambar berbasis LLM lain. Ganti variabelnya, pertahankan sistem visualnya.
</p>

<p align="center">
  Ini adalah pustaka gaya prompt visual siap pakai untuk generasi gambar AI. Setiap gaya disusun sebagai <code>style.json</code> yang mudah digunakan ulang, lengkap dengan preview landscape dan portrait.
</p>

<p align="center">
  Curated by <a href="https://x.com/VigoCreativeAI">@VigoCreativeAI</a>, structured with assistance from OpenAI Codex. Star repo ini untuk mengikuti rilis gaya baru.
</p>

<p align="center">
  Jelajahi <a href="#all-styles">galeri All Styles</a> atau buka <a href="docs/CATALOG.md">katalog lengkap</a>.
</p>

## Tautan Cepat

| Kategori | Cocok untuk | Mulai dari |
| --- | --- | --- |
| Foto + Doodle | Foto sosial, adegan lifestyle, overlay stiker yang playful | [Playful Mascot Doodle Snapshot](#playful-mascot-doodle-snapshot-style), [Subway Doodle Photo Hybrid](#subway-doodle-photo-hybrid-style) |
| Zine + Kolase | Poster fashion, visual musik, layout editorial maksimalis | [K-pop Apocalypse Ransom Zine](#k-pop-apocalypse-ransom-zine-style), [Y2K Grunge Hip-hop Cutout Poster](#y2k-grunge-hiphop-cutout-poster-style) |
| Poster Tipografi | Headline besar, grafik kampanye yang keras, visual impact | [Impact Burst Halftone Comic Poster](#impact-burst-halftone-comic-poster-style), [Neon Kinetic Typographic Poster](#neon-kinetic-typographic-poster-style) |
| Travel + Kota | Poster destinasi, scene jalanan, diary visual perkotaan | [Clean Triptych Travel Vlog Thumbnail](#clean-triptych-travel-vlog-thumbnail-style), [Tokyo Kawaii Travel Collage Poster](#tokyo-kawaii-travel-collage-poster-style) |
| Editorial + Minimal | Komposisi bersih, layout terstruktur, arahan visual yang lebih tenang | [Tri Color Hardcut Portrait Poster](#tri-color-hardcut-portrait-poster-style), [Soft Analog Future Editorial Poster](#soft-analog-future-editorial-poster-style) |

## Kenapa Proyek Ini Ada

Banyak prompt gambar AI hanya berupa teks sekali pakai: sulit digunakan ulang, sulit dibandingkan, dan sulit diiterasi secara stabil. Repo ini memakai pendekatan berbeda: setiap gaya visual dipecah menjadi `style.json` yang terstruktur. Saat subjek berubah, struktur visualnya tetap konsisten.

## Mulai Cepat

1. Jelajahi [Gaya Unggulan](#gaya-unggulan), [Tautan Cepat](#tautan-cepat), atau [All Styles](#all-styles).
2. Buka folder gaya yang kamu suka, lalu salin `style.json`.
3. Tempel seluruh JSON ke ChatGPT Images 2, Nano Banana Pro, atau model gambar multimodal end-to-end lain.
4. Isi nilai untuk variabel yang dideklarasikan di `environment_variables`, atau edit salah satu case di `examples[*].values`.
5. Buat gambar final.

Lihat [Complete Example](#complete-example) di bawah untuk walkthrough input-ke-output penuh.

### Recommended Image Models

Workflow ini paling cocok dengan model gambar multimodal end-to-end yang bisa membaca prompt JSON terstruktur yang panjang dan menghasilkan gambar final dalam satu langkah.

- ChatGPT Images 2 (OpenAI, gpt-image-2) — rendering teks kuat, output 2K/4K, reasoning sebelum generasi
- Nano Banana Pro (Google, Gemini 3 Pro Image) — output 4K, akurasi teks multibahasa, konsistensi subjek kuat

LLM multimodal lain yang menerima prompt JSON panjang mungkin juga bisa dipakai, tetapi bukan rekomendasi utama.

## Complete Example

### Walkthrough Input → Output

Contoh ini memakai [Mono Noir Type Portrait Poster Style](styles/mono-noir-type-portrait-poster-style/).

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

Ingin mencoba versi singkat dulu? Buka [Copy Prompt Library](docs/copy-prompts/README.md) untuk prompt siap salin per gaya. Sistem gaya lengkap yang reusable tetap berada di setiap `style.json`.

## Gaya Unggulan

Enam sistem visual ini cocok untuk memulai. Setiap gaya berisi satu JSON dan dua gambar preview. Jelajahi 49 gaya lengkap di galeri [All Styles](#all-styles) di bawah.

<!-- HTML table used for rich image+link cells -->

<table>
<tr>
<td width="33%" valign="top">
<a href="styles/yellow-black-manga-food-zine-ad-style"><img src="styles/yellow-black-manga-food-zine-ad-style/preview-16x9.jpg" alt="Yellow Black Manga Food Zine Ad Style preview"></a>
<h3>Yellow Black Manga Food Zine Ad Style</h3>
<p>Gaya iklan zine makanan dan produk yang terinspirasi manga Jepang, dengan linework tinta hitam, blok iklan kuning, bidang kertas krem, panel reaksi terpotong dramatis, objek utama ilustratif glossy, tipografi display melengkung besar, copy editorial Tionghoa kecil, dan tekstur cetak kasar.</p>
<p><a href="styles/yellow-black-manga-food-zine-ad-style/style.json"><strong>Buka style.json</strong></a> · <a href="docs/copy-prompts/yellow-black-manga-food-zine-ad-style.md">Copy Prompt</a> · <a href="styles/yellow-black-manga-food-zine-ad-style">Folder</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/neon-outdoor-diary-longform-collage-style"><img src="styles/neon-outdoor-diary-longform-collage-style/preview-16x9.jpg" alt="Neon Outdoor Diary Longform Collage Style preview"></a>
<h3>Neon Outdoor Diary Longform Collage Style</h3>
<p>Gaya kolase longform diary outdoor yang mobile-first, dengan kanvas hitam arang, cutout foto aksi dokumenter, headline kinetic acid-green, panel kertas robek, panah gambar tangan, label stiker, bagian bernomor, dan ritme catatan sosial yang padat.</p>
<p><a href="styles/neon-outdoor-diary-longform-collage-style/style.json"><strong>Buka style.json</strong></a> · <a href="docs/copy-prompts/neon-outdoor-diary-longform-collage-style.md">Copy Prompt</a> · <a href="styles/neon-outdoor-diary-longform-collage-style">Folder</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/acid-lime-3d-streetwear-type-poster-style"><img src="styles/acid-lime-3d-streetwear-type-poster-style/preview-16x9.jpg" alt="Acid Lime 3D Streetwear Type Poster Style preview"></a>
<h3>Acid Lime 3D Streetwear Type Poster Style</h3>
<p>Gaya poster kampanye streetwear C4D glossy dengan ruang studio pucat, tipografi blok hitam besar, coretan marker acid-lime, badge stiker, properti alat fashion, staging karakter wide-angle rendah, dan pencahayaan produk sintetis yang bersih.</p>
<p><a href="styles/acid-lime-3d-streetwear-type-poster-style/style.json"><strong>Buka style.json</strong></a> · <a href="docs/copy-prompts/acid-lime-3d-streetwear-type-poster-style.md">Copy Prompt</a> · <a href="styles/acid-lime-3d-streetwear-type-poster-style">Folder</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a href="styles/electric-blue-silhouette-product-launch-style"><img src="styles/electric-blue-silhouette-product-launch-style/preview-16x9.jpg" alt="Electric Blue Silhouette Product Launch Style preview"></a>
<h3>Electric Blue Silhouette Product Launch Style</h3>
<p>Gaya poster peluncuran teknologi premium yang renggang dengan ruang hitam, siluet produk di tengah, rim light biru elektrik, platform bercahaya, tipografi latar terpotong besar, dan copy putih bersih.</p>
<p><a href="styles/electric-blue-silhouette-product-launch-style/style.json"><strong>Buka style.json</strong></a> · <a href="docs/copy-prompts/electric-blue-silhouette-product-launch-style.md">Copy Prompt</a> · <a href="styles/electric-blue-silhouette-product-launch-style">Folder</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/luxury-perspective-checkerboard-editorial"><img src="styles/luxury-perspective-checkerboard-editorial/preview-16x9.jpg" alt="Luxury Perspective Checkerboard Editorial preview"></a>
<h3>Luxury Perspective Checkerboard Editorial</h3>
<p>Gaya editorial high-fashion dengan fotografi mewah low-angle, bidang perspektif checkerboard merah-putih, ruang putih luas, tipografi script besar, dan aksen emerald atau teal yang tertahan.</p>
<p><a href="styles/luxury-perspective-checkerboard-editorial/style.json"><strong>Buka style.json</strong></a> · <a href="docs/copy-prompts/luxury-perspective-checkerboard-editorial.md">Copy Prompt</a> · <a href="styles/luxury-perspective-checkerboard-editorial">Folder</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/sunny-3d-avatar-campaign-style"><img src="styles/sunny-3d-avatar-campaign-style/preview-16x9.jpg" alt="Sunny 3D Avatar Campaign Style preview"></a>
<h3>Sunny 3D Avatar Campaign Style</h3>
<p>Gaya kampanye sosial 3D yang cerah dengan avatar seperti mainan mengilap, cahaya langit biru, perspektif wide-angle, headline miring besar, garis neon, dan label stiker membulat.</p>
<p><a href="styles/sunny-3d-avatar-campaign-style/style.json"><strong>Buka style.json</strong></a> · <a href="docs/copy-prompts/sunny-3d-avatar-campaign-style.md">Copy Prompt</a> · <a href="styles/sunny-3d-avatar-campaign-style">Folder</a></p>
</td>
</tr>
</table>

## Struktur Paket

```text
styles/<style-slug>/
  style.json          # Template gaya prompt yang dapat dibaca mesin
  preview-16x9.jpg    # Preview landscape
  preview-9x16.jpg    # Preview portrait
```

## style.json v2.1

Setiap `style.json` bersifat mandiri: salin seluruh file ke LLM, lalu isi nilai untuk variabel yang dideklarasikan di `environment_variables` atau edit salah satu case di `examples[*].values`.

- `prompt_template` adalah prompt gaya reusable dengan placeholder `{VARIABLE}`.
- `environment_variables` mendeklarasikan semua placeholder yang dapat dipakai template.
- `examples` berisi kasus siap edit; setiap kasus hanya menyimpan `case_name` dan `values`.
- `style_fidelity_anchors` dan `source_content_to_avoid` menjelaskan apa yang harus dipertahankan dan apa yang tidak boleh disalin.
- `negative_prompt` membantu menghindari watermark, logo, rekreasi sumber langsung, dan output yang keluar dari gaya.

Prompt final seperti `prompt_9x16`, `prompt_16x9`, atau `full_prompt` sengaja tidak disimpan. Prompt itu dibuat saat generasi dari `prompt_template` dan nilai yang dipilih, sehingga JSON tetap ringkas dan tidak mudah basi.

Validasi pustaka dengan:

```bash
python3 scripts/validate-style-json.py .
```

## All Styles

Jelajahi semua 49 gaya di bawah ini.

Library lengkap ini mencakup gaya unggulan di atas. Untuk deskripsi penuh dan semua tautan file per gaya, lihat [docs/CATALOG.md](docs/CATALOG.md).

<!-- HTML table used for rich image+link cells -->

<table>
<tr>
<td width="33%" valign="top">
<a id="yellow-black-manga-food-zine-ad-style"></a>
<a href="styles/yellow-black-manga-food-zine-ad-style"><img src="styles/yellow-black-manga-food-zine-ad-style/preview-16x9.jpg" alt="Yellow Black Manga Food Zine Ad Style preview"></a>
<p><strong><a href="styles/yellow-black-manga-food-zine-ad-style">Yellow Black Manga Food Zine Ad Style</a></strong><br>
<em>Iklan zine makanan manga hitam-kuning dengan type melengkung dan objek glossy.</em><br>
<a href="styles/yellow-black-manga-food-zine-ad-style/style.json">style.json</a> · <a href="docs/copy-prompts/yellow-black-manga-food-zine-ad-style.md">prompt</a> · <a href="styles/yellow-black-manga-food-zine-ad-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="neon-outdoor-diary-longform-collage-style"></a>
<a href="styles/neon-outdoor-diary-longform-collage-style"><img src="styles/neon-outdoor-diary-longform-collage-style/preview-16x9.jpg" alt="Neon Outdoor Diary Longform Collage Style preview"></a>
<p><strong><a href="styles/neon-outdoor-diary-longform-collage-style">Neon Outdoor Diary Longform Collage Style</a></strong><br>
<em>Kolase diary outdoor longform dengan type acid-green, panel kertas robek, dan cutout foto.</em><br>
<a href="styles/neon-outdoor-diary-longform-collage-style/style.json">style.json</a> · <a href="docs/copy-prompts/neon-outdoor-diary-longform-collage-style.md">prompt</a> · <a href="styles/neon-outdoor-diary-longform-collage-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="acid-lime-3d-streetwear-type-poster-style"></a>
<a href="styles/acid-lime-3d-streetwear-type-poster-style"><img src="styles/acid-lime-3d-streetwear-type-poster-style/preview-16x9.jpg" alt="Acid Lime 3D Streetwear Type Poster Style preview"></a>
<p><strong><a href="styles/acid-lime-3d-streetwear-type-poster-style">Acid Lime 3D Streetwear Type Poster Style</a></strong><br>
<em>Kampanye streetwear C4D glossy dengan type blok hitam dan aksen acid-lime.</em><br>
<a href="styles/acid-lime-3d-streetwear-type-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/acid-lime-3d-streetwear-type-poster-style.md">prompt</a> · <a href="styles/acid-lime-3d-streetwear-type-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="electric-blue-silhouette-product-launch-style"></a>
<a href="styles/electric-blue-silhouette-product-launch-style"><img src="styles/electric-blue-silhouette-product-launch-style/preview-16x9.jpg" alt="Electric Blue Silhouette Product Launch Style preview"></a>
<p><strong><a href="styles/electric-blue-silhouette-product-launch-style">Electric Blue Silhouette Product Launch Style</a></strong><br>
<em>Peluncuran produk hitam-biru premium dengan siluet bercahaya dan tipografi terpotong.</em><br>
<a href="styles/electric-blue-silhouette-product-launch-style/style.json">style.json</a> · <a href="docs/copy-prompts/electric-blue-silhouette-product-launch-style.md">prompt</a> · <a href="styles/electric-blue-silhouette-product-launch-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="luxury-perspective-checkerboard-editorial"></a>
<a href="styles/luxury-perspective-checkerboard-editorial"><img src="styles/luxury-perspective-checkerboard-editorial/preview-16x9.jpg" alt="Luxury Perspective Checkerboard Editorial preview"></a>
<p><strong><a href="styles/luxury-perspective-checkerboard-editorial">Luxury Perspective Checkerboard Editorial</a></strong><br>
<em>Editorial mewah dengan perspektif checkerboard, script besar, dan ruang putih halus.</em><br>
<a href="styles/luxury-perspective-checkerboard-editorial/style.json">style.json</a> · <a href="docs/copy-prompts/luxury-perspective-checkerboard-editorial.md">prompt</a> · <a href="styles/luxury-perspective-checkerboard-editorial/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="sunny-3d-avatar-campaign-style"></a>
<a href="styles/sunny-3d-avatar-campaign-style"><img src="styles/sunny-3d-avatar-campaign-style/preview-16x9.jpg" alt="Sunny 3D Avatar Campaign Style preview"></a>
<p><strong><a href="styles/sunny-3d-avatar-campaign-style">Sunny 3D Avatar Campaign Style</a></strong><br>
<em>Avatar 3D kampanye cerah dengan langit biru, tipografi miring besar, dan garis neon.</em><br>
<a href="styles/sunny-3d-avatar-campaign-style/style.json">style.json</a> · <a href="docs/copy-prompts/sunny-3d-avatar-campaign-style.md">prompt</a> · <a href="styles/sunny-3d-avatar-campaign-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="y2k-mirror-ui-scribble-collage-style"></a>
<a href="styles/y2k-mirror-ui-scribble-collage-style"><img src="styles/y2k-mirror-ui-scribble-collage-style/preview-16x9.jpg" alt="Y2K Mirror UI Scribble Collage Style preview"></a>
<p><strong><a href="styles/y2k-mirror-ui-scribble-collage-style">Y2K Mirror UI Scribble Collage Style</a></strong><br>
<em>Kolase foto flash Y2K dengan panel UI cermin, coretan biru elektrik, dan noise kasar.</em><br>
<a href="styles/y2k-mirror-ui-scribble-collage-style/style.json">style.json</a> · <a href="docs/copy-prompts/y2k-mirror-ui-scribble-collage-style.md">prompt</a> · <a href="styles/y2k-mirror-ui-scribble-collage-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="neon-plush-gadget-pop-3d-style"></a>
<a href="styles/neon-plush-gadget-pop-3d-style"><img src="styles/neon-plush-gadget-pop-3d-style/preview-16x9.jpg" alt="Neon Plush Gadget Pop 3D Style preview"></a>
<p><strong><a href="styles/neon-plush-gadget-pop-3d-style">Neon Plush Gadget Pop 3D Style</a></strong><br>
<em>Render 3D produk mainan neon dengan maskot plush dan gadget chunky.</em><br>
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
<a href="styles/warm-fisheye-product-impact-ad-style"><img src="styles/warm-fisheye-product-impact-ad-style/preview-16x9.jpg" alt="Warm Fisheye Product Impact Ad preview"></a>
<p><strong><a href="styles/warm-fisheye-product-impact-ad-style">Warm Fisheye Product Impact Ad</a></strong><br>
<em>Warm fisheye product ads with bold Chinese social-commerce type.</em><br>
<a href="styles/warm-fisheye-product-impact-ad-style/style.json">style.json</a> · <a href="docs/copy-prompts/warm-fisheye-product-impact-ad-style.md">prompt</a> · <a href="styles/warm-fisheye-product-impact-ad-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="olive-scribble-sports-poster-style"></a>
<a href="styles/olive-scribble-sports-poster-style"><img src="styles/olive-scribble-sports-poster-style/preview-16x9.jpg" alt="Olive Scribble Sports Poster preview"></a>
<p><strong><a href="styles/olive-scribble-sports-poster-style">Olive Scribble Sports Poster</a></strong><br>
<em>Handmade sports posters with olive blocks and kinetic scribbles.</em><br>
<a href="styles/olive-scribble-sports-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/olive-scribble-sports-poster-style.md">prompt</a> · <a href="styles/olive-scribble-sports-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="bold-anime-reaction-thumbnail-style"></a>
<a href="styles/bold-anime-reaction-thumbnail-style"><img src="styles/bold-anime-reaction-thumbnail-style/preview-16x9.jpg" alt="Bold Anime Reaction Thumbnail preview"></a>
<p><strong><a href="styles/bold-anime-reaction-thumbnail-style">Bold Anime Reaction Thumbnail</a></strong><br>
<em>High-impact anime thumbnails with bold yellow reaction typography.</em><br>
<a href="styles/bold-anime-reaction-thumbnail-style/style.json">style.json</a> · <a href="docs/copy-prompts/bold-anime-reaction-thumbnail-style.md">prompt</a> · <a href="styles/bold-anime-reaction-thumbnail-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="turquoise-red-techno-manga-poster-style"></a>
<a href="styles/turquoise-red-techno-manga-poster-style"><img src="styles/turquoise-red-techno-manga-poster-style/preview-16x9.jpg" alt="Turquoise Red Techno Manga Poster preview"></a>
<p><strong><a href="styles/turquoise-red-techno-manga-poster-style">Turquoise Red Techno Manga Poster</a></strong><br>
<em>Retro techno-manga posters with turquoise hardware and red lettering.</em><br>
<a href="styles/turquoise-red-techno-manga-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/turquoise-red-techno-manga-poster-style.md">prompt</a> · <a href="styles/turquoise-red-techno-manga-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="chromatic-fisheye-orbit-pop-poster-style"></a>
<a href="styles/chromatic-fisheye-orbit-pop-poster-style"><img src="styles/chromatic-fisheye-orbit-pop-poster-style/preview-16x9.jpg" alt="Chromatic Fisheye Orbit Pop Poster preview"></a>
<p><strong><a href="styles/chromatic-fisheye-orbit-pop-poster-style">Chromatic Fisheye Orbit Pop Poster</a></strong><br>
<em>Pop fisheye posters with orbiting type and chromatic arcs.</em><br>
<a href="styles/chromatic-fisheye-orbit-pop-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/chromatic-fisheye-orbit-pop-poster-style.md">prompt</a> · <a href="styles/chromatic-fisheye-orbit-pop-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="naive-marker-psa-poster-style"></a>
<a href="styles/naive-marker-psa-poster-style"><img src="styles/naive-marker-psa-poster-style/preview-16x9.jpg" alt="Naive Marker PSA Poster preview"></a>
<p><strong><a href="styles/naive-marker-psa-poster-style">Naive Marker PSA Poster</a></strong><br>
<em>Friendly civic PSA posters with naive marker drawings.</em><br>
<a href="styles/naive-marker-psa-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/naive-marker-psa-poster-style.md">prompt</a> · <a href="styles/naive-marker-psa-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="blue-bubble-fisheye-action-poster-style"></a>
<a href="styles/blue-bubble-fisheye-action-poster-style"><img src="styles/blue-bubble-fisheye-action-poster-style/preview-16x9.jpg" alt="Blue Bubble Fisheye Action Poster preview"></a>
<p><strong><a href="styles/blue-bubble-fisheye-action-poster-style">Blue Bubble Fisheye Action Poster</a></strong><br>
<em>Youth action posters with blue bubble type and fisheye photos.</em><br>
<a href="styles/blue-bubble-fisheye-action-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/blue-bubble-fisheye-action-poster-style.md">prompt</a> · <a href="styles/blue-bubble-fisheye-action-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="cozy-bedroom-doodle-companion-snapshot-style"></a>
<a href="styles/cozy-bedroom-doodle-companion-snapshot-style"><img src="styles/cozy-bedroom-doodle-companion-snapshot-style/preview-16x9.jpg" alt="Cozy Bedroom Doodle Companion Snapshot preview"></a>
<p><strong><a href="styles/cozy-bedroom-doodle-companion-snapshot-style">Cozy Bedroom Doodle Companion Snapshot</a></strong><br>
<em>Low-light bedroom snapshots with quiet doodle companion energy.</em><br>
<a href="styles/cozy-bedroom-doodle-companion-snapshot-style/style.json">style.json</a> · <a href="docs/copy-prompts/cozy-bedroom-doodle-companion-snapshot-style.md">prompt</a> · <a href="styles/cozy-bedroom-doodle-companion-snapshot-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="surreal-fish-doodle-landmark-photo-collage-style"></a>
<a href="styles/surreal-fish-doodle-landmark-photo-collage-style"><img src="styles/surreal-fish-doodle-landmark-photo-collage-style/preview-16x9.jpg" alt="Surreal Fish Doodle Landmark Photo Collage preview"></a>
<p><strong><a href="styles/surreal-fish-doodle-landmark-photo-collage-style">Surreal Fish Doodle Landmark Photo Collage</a></strong><br>
<em>Landmark travel photos remixed with folk-art fish doodles.</em><br>
<a href="styles/surreal-fish-doodle-landmark-photo-collage-style/style.json">style.json</a> · <a href="docs/copy-prompts/surreal-fish-doodle-landmark-photo-collage-style.md">prompt</a> · <a href="styles/surreal-fish-doodle-landmark-photo-collage-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="plush-comic-toy-product-poster-style"></a>
<a href="styles/plush-comic-toy-product-poster-style"><img src="styles/plush-comic-toy-product-poster-style/preview-16x9.jpg" alt="Plush Comic Toy Product Poster preview"></a>
<p><strong><a href="styles/plush-comic-toy-product-poster-style">Plush Comic Toy Product Poster</a></strong><br>
<em>Toy-product posters with fuzzy plush heroes and comic typography.</em><br>
<a href="styles/plush-comic-toy-product-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/plush-comic-toy-product-poster-style.md">prompt</a> · <a href="styles/plush-comic-toy-product-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="rough-animation-pet-sketch-storyboard-style"></a>
<a href="styles/rough-animation-pet-sketch-storyboard-style"><img src="styles/rough-animation-pet-sketch-storyboard-style/preview-16x9.jpg" alt="Rough Animation Pet Sketch Storyboard preview"></a>
<p><strong><a href="styles/rough-animation-pet-sketch-storyboard-style">Rough Animation Pet Sketch Storyboard</a></strong><br>
<em>Loose pet-comedy storyboard frames with warm sketch texture.</em><br>
<a href="styles/rough-animation-pet-sketch-storyboard-style/style.json">style.json</a> · <a href="docs/copy-prompts/rough-animation-pet-sketch-storyboard-style.md">prompt</a> · <a href="styles/rough-animation-pet-sketch-storyboard-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="tri-color-hardcut-portrait-poster-style"></a>
<a href="styles/tri-color-hardcut-portrait-poster-style"><img src="styles/tri-color-hardcut-portrait-poster-style/preview-16x9.jpg" alt="Tri Color Hardcut Portrait Poster preview"></a>
<p><strong><a href="styles/tri-color-hardcut-portrait-poster-style">Tri Color Hardcut Portrait Poster</a></strong><br>
<em>Three-color portrait posters built from hard-edged cutout planes.</em><br>
<a href="styles/tri-color-hardcut-portrait-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/tri-color-hardcut-portrait-poster-style.md">prompt</a> · <a href="styles/tri-color-hardcut-portrait-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="clean-triptych-travel-vlog-thumbnail-style"></a>
<a href="styles/clean-triptych-travel-vlog-thumbnail-style"><img src="styles/clean-triptych-travel-vlog-thumbnail-style/preview-16x9.jpg" alt="Clean Triptych Travel Vlog Thumbnail preview"></a>
<p><strong><a href="styles/clean-triptych-travel-vlog-thumbnail-style">Clean Triptych Travel Vlog Thumbnail</a></strong><br>
<em>Clean travel thumbnails with three photo panels and soft notes.</em><br>
<a href="styles/clean-triptych-travel-vlog-thumbnail-style/style.json">style.json</a> · <a href="docs/copy-prompts/clean-triptych-travel-vlog-thumbnail-style.md">prompt</a> · <a href="styles/clean-triptych-travel-vlog-thumbnail-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="playful-mascot-doodle-snapshot-style"></a>
<a href="styles/playful-mascot-doodle-snapshot-style"><img src="styles/playful-mascot-doodle-snapshot-style/preview-16x9.jpg" alt="Playful Mascot Doodle Snapshot preview"></a>
<p><strong><a href="styles/playful-mascot-doodle-snapshot-style">Playful Mascot Doodle Snapshot</a></strong><br>
<em>Real-life snapshots layered with mascot stickers and doodles.</em><br>
<a href="styles/playful-mascot-doodle-snapshot-style/style.json">style.json</a> · <a href="docs/copy-prompts/playful-mascot-doodle-snapshot-style.md">prompt</a> · <a href="styles/playful-mascot-doodle-snapshot-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="teenage-skate-scribble-screenprint-poster-style"></a>
<a href="styles/teenage-skate-scribble-screenprint-poster-style"><img src="styles/teenage-skate-scribble-screenprint-poster-style/preview-16x9.jpg" alt="Teenage Skate Scribble Screenprint Poster preview"></a>
<p><strong><a href="styles/teenage-skate-scribble-screenprint-poster-style">Teenage Skate Scribble Screenprint Poster</a></strong><br>
<em>Retro skate posters with scribbled borders and screenprint grit.</em><br>
<a href="styles/teenage-skate-scribble-screenprint-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/teenage-skate-scribble-screenprint-poster-style.md">prompt</a> · <a href="styles/teenage-skate-scribble-screenprint-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="impact-burst-halftone-comic-poster-style"></a>
<a href="styles/impact-burst-halftone-comic-poster-style"><img src="styles/impact-burst-halftone-comic-poster-style/preview-16x9.jpg" alt="Impact Burst Halftone Comic Poster preview"></a>
<p><strong><a href="styles/impact-burst-halftone-comic-poster-style">Impact Burst Halftone Comic Poster</a></strong><br>
<em>Loud comic posters with impact type and halftone bursts.</em><br>
<a href="styles/impact-burst-halftone-comic-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/impact-burst-halftone-comic-poster-style.md">prompt</a> · <a href="styles/impact-burst-halftone-comic-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="sunburst-fisheye-bubble-type-poster-style"></a>
<a href="styles/sunburst-fisheye-bubble-type-poster-style"><img src="styles/sunburst-fisheye-bubble-type-poster-style/preview-16x9.jpg" alt="Sunburst Fisheye Bubble Type Poster preview"></a>
<p><strong><a href="styles/sunburst-fisheye-bubble-type-poster-style">Sunburst Fisheye Bubble Type Poster</a></strong><br>
<em>Summer fisheye posters with sunny bubble typography.</em><br>
<a href="styles/sunburst-fisheye-bubble-type-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/sunburst-fisheye-bubble-type-poster-style.md">prompt</a> · <a href="styles/sunburst-fisheye-bubble-type-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="backseat-transit-doodle-letter-poster-style"></a>
<a href="styles/backseat-transit-doodle-letter-poster-style"><img src="styles/backseat-transit-doodle-letter-poster-style/preview-16x9.jpg" alt="Backseat Transit Doodle Letter Poster preview"></a>
<p><strong><a href="styles/backseat-transit-doodle-letter-poster-style">Backseat Transit Doodle Letter Poster</a></strong><br>
<em>Transit photos turned into energetic hand-lettered travel posters.</em><br>
<a href="styles/backseat-transit-doodle-letter-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/backseat-transit-doodle-letter-poster-style.md">prompt</a> · <a href="styles/backseat-transit-doodle-letter-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="analog-sticker-diary-portrait-poster-style"></a>
<a href="styles/analog-sticker-diary-portrait-poster-style"><img src="styles/analog-sticker-diary-portrait-poster-style/preview-16x9.jpg" alt="Analog Sticker Diary Portrait Poster preview"></a>
<p><strong><a href="styles/analog-sticker-diary-portrait-poster-style">Analog Sticker Diary Portrait Poster</a></strong><br>
<em>Nostalgic diary portraits with stickers and distressed lettering.</em><br>
<a href="styles/analog-sticker-diary-portrait-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/analog-sticker-diary-portrait-poster-style.md">prompt</a> · <a href="styles/analog-sticker-diary-portrait-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="folded-diamond-perspective-type-poster-style"></a>
<a href="styles/folded-diamond-perspective-type-poster-style"><img src="styles/folded-diamond-perspective-type-poster-style/preview-16x9.jpg" alt="Folded Diamond Perspective Type Poster preview"></a>
<p><strong><a href="styles/folded-diamond-perspective-type-poster-style">Folded Diamond Perspective Type Poster</a></strong><br>
<em>Minimal diamond-aperture posters with folded perspective typography.</em><br>
<a href="styles/folded-diamond-perspective-type-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/folded-diamond-perspective-type-poster-style.md">prompt</a> · <a href="styles/folded-diamond-perspective-type-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="gothic-cat-doodle-photo-collage-style"></a>
<a href="styles/gothic-cat-doodle-photo-collage-style"><img src="styles/gothic-cat-doodle-photo-collage-style/preview-16x9.jpg" alt="Gothic Cat Doodle Photo Collage preview"></a>
<p><strong><a href="styles/gothic-cat-doodle-photo-collage-style">Gothic Cat Doodle Photo Collage</a></strong><br>
<em>Dramatic architecture photos with playful cartoon creature overlays.</em><br>
<a href="styles/gothic-cat-doodle-photo-collage-style/style.json">style.json</a> · <a href="docs/copy-prompts/gothic-cat-doodle-photo-collage-style.md">prompt</a> · <a href="styles/gothic-cat-doodle-photo-collage-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top">
<a id="k-pop-apocalypse-ransom-zine-style"></a>
<a href="styles/k-pop-apocalypse-ransom-zine-style"><img src="styles/k-pop-apocalypse-ransom-zine-style/preview-16x9.jpg" alt="K-pop Apocalypse Ransom Zine preview"></a>
<p><strong><a href="styles/k-pop-apocalypse-ransom-zine-style">K-pop Apocalypse Ransom Zine</a></strong><br>
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
<a href="styles/mountain-trail-monster-doodle-poster-style"><img src="styles/mountain-trail-monster-doodle-poster-style/preview-16x9.jpg" alt="Mountain Trail Monster Doodle Poster preview"></a>
<p><strong><a href="styles/mountain-trail-monster-doodle-poster-style">Mountain Trail Monster Doodle Poster</a></strong><br>
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
<a href="styles/orange-brush-mascot-action-poster-style"><img src="styles/orange-brush-mascot-action-poster-style/preview-16x9.jpg" alt="Orange Brush Mascot Action Poster preview"></a>
<p><strong><a href="styles/orange-brush-mascot-action-poster-style">Orange Brush Mascot Action Poster</a></strong><br>
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
<a href="styles/pop-bubble-letter-photo-poster-style"><img src="styles/pop-bubble-letter-photo-poster-style/preview-16x9.jpg" alt="Pop Bubble Letter Photo Poster preview"></a>
<p><strong><a href="styles/pop-bubble-letter-photo-poster-style">Pop Bubble Letter Photo Poster</a></strong><br>
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
<a href="styles/urban-transit-doodle-diary-style"><img src="styles/urban-transit-doodle-diary-style/preview-16x9.jpg" alt="Urban Transit Doodle Diary preview"></a>
<p><strong><a href="styles/urban-transit-doodle-diary-style">Urban Transit Doodle Diary</a></strong><br>
<em>Public-space photos remixed with bold foreground gestures and travel diary notes.</em><br>
<a href="styles/urban-transit-doodle-diary-style/style.json">style.json</a> · <a href="docs/copy-prompts/urban-transit-doodle-diary-style.md">prompt</a> · <a href="styles/urban-transit-doodle-diary-style/preview-9x16.jpg">9:16</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a id="y2k-grunge-hiphop-cutout-poster-style"></a>
<a href="styles/y2k-grunge-hiphop-cutout-poster-style"><img src="styles/y2k-grunge-hiphop-cutout-poster-style/preview-16x9.jpg" alt="Y2K Grunge Hip-hop Cutout Poster preview"></a>
<p><strong><a href="styles/y2k-grunge-hiphop-cutout-poster-style">Y2K Grunge Hip-hop Cutout Poster</a></strong><br>
<em>Y2K hip-hop collage posters with acid type and photocopy grit.</em><br>
<a href="styles/y2k-grunge-hiphop-cutout-poster-style/style.json">style.json</a> · <a href="docs/copy-prompts/y2k-grunge-hiphop-cutout-poster-style.md">prompt</a> · <a href="styles/y2k-grunge-hiphop-cutout-poster-style/preview-9x16.jpg">9:16</a></p>
</td>
<td width="33%" valign="top"></td>
<td width="33%" valign="top"></td>
</tr>
</table>

## Model Publikasi

- Satu direktori = satu gaya
- Gaya baru muncul lebih dulu di Gaya Unggulan dan galeri All Styles, dengan deskripsi lengkap ditambahkan ke [docs/CATALOG.md](docs/CATALOG.md)
- Branch main hanya berisi `style.json` dan dua preview JPG per gaya
- Galeri lengkap tidak disertakan di repo ini
- Jangan memublikasikan gambar referensi asli, watermark, identitas platform, QR code, handle akun, prompt privat, atau aset brand tanpa izin

## Contributing

Pengiriman gaya baru harus mengikuti struktur paket publik, aturan validasi, dan PR checklist di [CONTRIBUTING.md](CONTRIBUTING.md).

## Lisensi

Struktur repo dan dokumentasi menggunakan lisensi MIT. Setiap file `style.json` menyatakan lisensinya sendiri. Gambar preview disertakan sebagai referensi visual.
