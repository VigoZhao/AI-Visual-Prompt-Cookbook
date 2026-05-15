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
  <img alt="風格數量" src="https://img.shields.io/badge/styles-25-ff5a7a?style=flat-square">
  <img alt="預覽圖" src="https://img.shields.io/badge/previews-50-4cc9f0?style=flat-square">
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

## 快速入口

| 分類 | 適合做什麼 | 先看這些 |
| --- | --- | --- |
| 照片 + 塗鴉 | 社交隨拍、生活方式場景、輕快貼紙覆蓋層 | [Playful Mascot Doodle Snapshot](styles/playful-mascot-doodle-snapshot-style), [Subway Doodle Photo Hybrid](styles/subway-doodle-photo-hybrid-style) |
| Zine + 拼貼 | 時尚海報、音樂視覺、極繁編輯版式 | [K-pop Apocalypse Ransom Zine](styles/k-pop-apocalypse-ransom-zine-style), [Y2K Grunge Hip-hop Cutout Poster](styles/y2k-grunge-hiphop-cutout-poster-style) |
| 字體海報 | 大標題系統、高衝擊廣告圖、強烈視覺識別 | [Impact Burst Halftone Comic Poster](styles/impact-burst-halftone-comic-poster-style), [Neon Kinetic Typographic Poster](styles/neon-kinetic-typographic-poster-style) |
| 旅行 + 城市 | 目的地海報、街頭場景、城市視覺日記 | [Tokyo Kawaii Travel Collage Poster](styles/tokyo-kawaii-travel-collage-poster-style), [Urban Transit Doodle Diary](styles/urban-transit-doodle-diary-style) |
| 編輯 + 極簡 | 更乾淨的構圖、結構化版面、安靜的藝術指導 | [Soft Analog Future Editorial Poster](styles/soft-analog-future-editorial-poster-style), [Folded Diamond Perspective Type Poster](styles/folded-diamond-perspective-type-poster-style) |

## 為什麼做這個項目

多數 AI 圖像提示詞都是一次性的文字塊：難以重用、難以比較，也難以穩定迭代。這個項目採用另一種方式：把每一種視覺風格拆解成結構化的 `style.json`，你可以把它放進 ChatGPT、Claude 或其他 LLM 圖像生成流程中。換主題時，風格結構仍然保持穩定。

## 快速開始

1. 瀏覽 [精選風格](#精選風格)、[快速入口](#快速入口) 或 [風格索引](#風格索引)。
2. 打開某個風格目錄，複製裡面的 `style.json`。
3. 把完整 JSON 放進 ChatGPT、Claude、Nano Banana Pro、即夢或其他 LLM 圖像工作流。
4. 只修改 `variables` 裡的主體、場景、文字和比例。
5. 生成最終圖像提示詞，再送到你的圖像模型。

示例指令：

```text
把這個 style.json 當作鎖定的視覺風格。
只替換 variables：
SUBJECT = 一位街頭服裝產品攝影師
LOCATION = 雨夜霓虹小巷
MAIN_TEXT = NIGHT DROP
ASPECT_RATIO = 16:9
```

## 精選風格

先看這 6 個，就能快速理解這個風格庫的視覺跨度。每個風格都保持輕量：一個 JSON 加兩張預覽圖。

<table>
<tr>
<td width="33%" valign="top">
<a href="styles/k-pop-apocalypse-ransom-zine-style"><img src="styles/k-pop-apocalypse-ransom-zine-style/preview-16x9.jpg" alt="K-pop Apocalypse Ransom Zine preview"></a>
<h3>K-pop Apocalypse Ransom Zine</h3>
<p>極繁時尚 zine 拼貼：人物剪貼、勒索信式排版、揉皺紙張、貼紙色塊和高飽和強調色。</p>
<p><a href="styles/k-pop-apocalypse-ransom-zine-style/style.json"><strong>打開 style.json</strong></a> · <a href="styles/k-pop-apocalypse-ransom-zine-style">目錄</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/impact-burst-halftone-comic-poster-style"><img src="styles/impact-burst-halftone-comic-poster-style/preview-16x9.jpg" alt="Impact Burst Halftone Comic Poster preview"></a>
<h3>Impact Burst Halftone Comic Poster</h3>
<p>響亮復古漫畫海報：厚重墨線、高飽和色塊、超大衝擊字體、爆裂對話形和絲網印刷顆粒。</p>
<p><a href="styles/impact-burst-halftone-comic-poster-style/style.json"><strong>打開 style.json</strong></a> · <a href="styles/impact-burst-halftone-comic-poster-style">目錄</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/playful-mascot-doodle-snapshot-style"><img src="styles/playful-mascot-doodle-snapshot-style/preview-16x9.jpg" alt="Playful Mascot Doodle Snapshot preview"></a>
<h3>Playful Mascot Doodle Snapshot</h3>
<p>把真實生活社交照片轉成輕快貼紙拼貼海報，在攝影場景上疊加原創卡通吉祥物、手繪描邊和草稿感裝飾。</p>
<p><a href="styles/playful-mascot-doodle-snapshot-style/style.json"><strong>打開 style.json</strong></a> · <a href="styles/playful-mascot-doodle-snapshot-style">目錄</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a href="styles/teenage-skate-scribble-screenprint-poster-style"><img src="styles/teenage-skate-scribble-screenprint-poster-style/preview-16x9.jpg" alt="Teenage Skate Scribble Screenprint Poster preview"></a>
<h3>Teenage Skate Scribble Screenprint Poster</h3>
<p>復古滑板 zine 海報：扭曲人物剪貼、奶油紙張、鬆散手寫邊框字、粗糲雙色絲網質感。</p>
<p><a href="styles/teenage-skate-scribble-screenprint-poster-style/style.json"><strong>打開 style.json</strong></a> · <a href="styles/teenage-skate-scribble-screenprint-poster-style">目錄</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/neon-kinetic-typographic-poster-style"><img src="styles/neon-kinetic-typographic-poster-style/preview-16x9.jpg" alt="Neon Kinetic Typographic Poster preview"></a>
<h3>Neon Kinetic Typographic Poster</h3>
<p>戲劇化戶外編輯海報：低機位攝影、變形霓虹字體、膠片顆粒和青年文化廣告氣質。</p>
<p><a href="styles/neon-kinetic-typographic-poster-style/style.json"><strong>打開 style.json</strong></a> · <a href="styles/neon-kinetic-typographic-poster-style">目錄</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/tokyo-kawaii-travel-collage-poster-style"><img src="styles/tokyo-kawaii-travel-collage-poster-style/preview-16x9.jpg" alt="Tokyo Kawaii Travel Collage Poster preview"></a>
<h3>Tokyo Kawaii Travel Collage Poster</h3>
<p>極繁城市旅行拼貼：目的地大字、可愛貼紙、漫畫對話框、剪貼攝影和 scrapbook 編輯版式。</p>
<p><a href="styles/tokyo-kawaii-travel-collage-poster-style/style.json"><strong>打開 style.json</strong></a> · <a href="styles/tokyo-kawaii-travel-collage-poster-style">目錄</a></p>
</td>
</tr>
</table>

## 文件結構

```text
styles/<style-slug>/
  style.json          # 機器可讀的提示詞風格模板
  preview-16x9.jpg    # 橫向預覽圖
  preview-9x16.jpg    # 直向預覽圖
```

## 風格索引

| # | 風格 | 文件 |
| --- | --- | --- |
| 1 | [Rough Animation Pet Sketch Storyboard](styles/rough-animation-pet-sketch-storyboard-style) | [style.json](styles/rough-animation-pet-sketch-storyboard-style/style.json) |
| 2 | [Tri Color Hardcut Portrait Poster](styles/tri-color-hardcut-portrait-poster-style) | [style.json](styles/tri-color-hardcut-portrait-poster-style/style.json) |
| 3 | [Clean Triptych Travel Vlog Thumbnail](styles/clean-triptych-travel-vlog-thumbnail-style) | [style.json](styles/clean-triptych-travel-vlog-thumbnail-style/style.json) |
| 4 | [Playful Mascot Doodle Snapshot](styles/playful-mascot-doodle-snapshot-style) | [style.json](styles/playful-mascot-doodle-snapshot-style/style.json) |
| 5 | [Teenage Skate Scribble Screenprint Poster](styles/teenage-skate-scribble-screenprint-poster-style) | [style.json](styles/teenage-skate-scribble-screenprint-poster-style/style.json) |
| 6 | [Impact Burst Halftone Comic Poster](styles/impact-burst-halftone-comic-poster-style) | [style.json](styles/impact-burst-halftone-comic-poster-style/style.json) |
| 7 | [Sunburst Fisheye Bubble Type Poster](styles/sunburst-fisheye-bubble-type-poster-style) | [style.json](styles/sunburst-fisheye-bubble-type-poster-style/style.json) |
| 8 | [Backseat Transit Doodle Letter Poster](styles/backseat-transit-doodle-letter-poster-style) | [style.json](styles/backseat-transit-doodle-letter-poster-style/style.json) |
| 9 | [Analog Sticker Diary Portrait Poster](styles/analog-sticker-diary-portrait-poster-style) | [style.json](styles/analog-sticker-diary-portrait-poster-style/style.json) |
| 10 | [Folded Diamond Perspective Type Poster](styles/folded-diamond-perspective-type-poster-style) | [style.json](styles/folded-diamond-perspective-type-poster-style/style.json) |
| 11 | [Gothic Cat Doodle Photo Collage](styles/gothic-cat-doodle-photo-collage-style) | [style.json](styles/gothic-cat-doodle-photo-collage-style/style.json) |
| 12 | [K-pop Apocalypse Ransom Zine](styles/k-pop-apocalypse-ransom-zine-style) | [style.json](styles/k-pop-apocalypse-ransom-zine-style/style.json) |
| 13 | [Metro Doodle Snapshot Diary](styles/metro-doodle-snapshot-diary-style) | [style.json](styles/metro-doodle-snapshot-diary-style/style.json) |
| 14 | [Mountain Trail Monster Doodle Poster](styles/mountain-trail-monster-doodle-poster-style) | [style.json](styles/mountain-trail-monster-doodle-poster-style/style.json) |
| 15 | [Neon Doodle Gallery Snapshot](styles/neon-doodle-gallery-snapshot-style) | [style.json](styles/neon-doodle-gallery-snapshot-style/style.json) |
| 16 | [Neon Kinetic Typographic Poster](styles/neon-kinetic-typographic-poster-style) | [style.json](styles/neon-kinetic-typographic-poster-style/style.json) |
| 17 | [Orange Brush Mascot Action Poster](styles/orange-brush-mascot-action-poster-style) | [style.json](styles/orange-brush-mascot-action-poster-style/style.json) |
| 18 | [Photo Illustration Overlay Poster](styles/photo-illustration-overlay-poster-style) | [style.json](styles/photo-illustration-overlay-poster-style/style.json) |
| 19 | [Plush City Festival Mobile Poster](styles/plush-city-festival-mobile-poster-style) | [style.json](styles/plush-city-festival-mobile-poster-style/style.json) |
| 20 | [Pop Bubble Letter Photo Poster](styles/pop-bubble-letter-photo-poster-style) | [style.json](styles/pop-bubble-letter-photo-poster-style/style.json) |
| 21 | [Soft Analog Future Editorial Poster](styles/soft-analog-future-editorial-poster-style) | [style.json](styles/soft-analog-future-editorial-poster-style/style.json) |
| 22 | [Subway Doodle Photo Hybrid](styles/subway-doodle-photo-hybrid-style) | [style.json](styles/subway-doodle-photo-hybrid-style/style.json) |
| 23 | [Tokyo Kawaii Travel Collage Poster](styles/tokyo-kawaii-travel-collage-poster-style) | [style.json](styles/tokyo-kawaii-travel-collage-poster-style/style.json) |
| 24 | [Urban Transit Doodle Diary](styles/urban-transit-doodle-diary-style) | [style.json](styles/urban-transit-doodle-diary-style/style.json) |
| 25 | [Y2K Grunge Hip-hop Cutout Poster](styles/y2k-grunge-hiphop-cutout-poster-style) | [style.json](styles/y2k-grunge-hiphop-cutout-poster-style/style.json) |

## 發布規則

- 一個目錄 = 一種風格
- 新風格優先出現在精選風格和風格索引頂部
- 主分支只放 `style.json` 和兩張預覽 JPG
- 完整圖庫不放在這個倉庫中
- 不發布原始參考圖、水印圖、平台標識、QR code、帳號資訊、私有提示詞，或未經授權的品牌素材

## 授權

倉庫結構和文件採用 MIT。每個 `style.json` 會聲明自己的授權方式。預覽圖僅作為視覺參考隨倉庫展示。
