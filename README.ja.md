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
  <img alt="Styles" src="https://img.shields.io/badge/styles-36-ff5a7a?style=flat-square">
  <img alt="Previews" src="https://img.shields.io/badge/previews-72-4cc9f0?style=flat-square">
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

## クイックリンク

| カテゴリ | 向いている用途 | まず見るスタイル |
| --- | --- | --- |
| 写真 + ドゥードル | SNS風スナップ、ライフスタイル写真、遊びのあるステッカー表現 | [Playful Mascot Doodle Snapshot](styles/playful-mascot-doodle-snapshot-style), [Subway Doodle Photo Hybrid](styles/subway-doodle-photo-hybrid-style) |
| Zine + コラージュ | ファッションポスター、音楽ビジュアル、情報量の多いエディトリアル | [K-pop Apocalypse Ransom Zine](styles/k-pop-apocalypse-ransom-zine-style), [Y2K Grunge Hip-hop Cutout Poster](styles/y2k-grunge-hiphop-cutout-poster-style) |
| タイポグラフィポスター | 大きな見出し、強いキャンペーングラフィック、視覚インパクト | [Impact Burst Halftone Comic Poster](styles/impact-burst-halftone-comic-poster-style), [Neon Kinetic Typographic Poster](styles/neon-kinetic-typographic-poster-style) |
| 旅 + 都市 | 目的地ポスター、ストリートシーン、都市のビジュアル日記 | [Tokyo Kawaii Travel Collage Poster](styles/tokyo-kawaii-travel-collage-poster-style), [Urban Transit Doodle Diary](styles/urban-transit-doodle-diary-style) |
| エディトリアル + ミニマル | すっきりした構図、構造的なレイアウト、落ち着いたアートディレクション | [Soft Analog Future Editorial Poster](styles/soft-analog-future-editorial-poster-style), [Folded Diamond Perspective Type Poster](styles/folded-diamond-perspective-type-poster-style) |

## このプロジェクトについて

多くの AI 画像プロンプトは一回限りの文章になりがちで、再利用や比較、安定した改善が難しいものです。このリポジトリでは、各ビジュアルスタイルを構造化された `style.json` に分解しています。テーマを変えても、同じスタイル構造を保ったまま生成を続けられます。

## 使い方

1. [注目スタイル](#注目スタイル)、[クイックリンク](#クイックリンク)、または [スタイル索引](#スタイル索引) を見る。
2. 気になるスタイルのフォルダを開き、`style.json` をコピーする。
3. ChatGPT、Claude、Nano Banana Pro、または任意の LLM 画像生成ワークフローに JSON 全体を貼り付ける。
4. `environment_variables` で宣言された変数に自分の値を指定するか、`examples[*].values` のケースを編集する。
5. 最終プロンプトを生成し、画像モデルに送る。

入力例：

```text
この style.json を固定されたビジュアルスタイルとして使ってください。
次の変数値を使ってください：
SUBJECT = ストリートウェアのプロダクトフォトグラファー
LOCATION = 雨のネオン路地
MAIN_TEXT = NIGHT DROP
ASPECT_RATIO = 16:9
```

## 注目スタイル

この 6 つを見ると、ライブラリ全体の幅がすぐにわかります。すべてのスタイルは、1 つの JSON と 2 枚のプレビュー画像で構成されています。

<table>
<tr>
<td width="33%" valign="top">
<a href="styles/blue-hud-macro-product-poster"><img src="styles/blue-hud-macro-product-poster/preview-16x9.jpg" alt="Blue HUD Macro Creator Tech Poster preview"></a>
<h3>Blue HUD Macro Creator Tech Poster</h3>
<p>マクロ 3D ハードウェアの主役、巨大なリブ付きグローブ、エレクトリックシアンの HUD ガラスパネル、大きな白いコンデンス見出し、密な機能カード、暖色のゴールド性能バッジで構成する青いクリエイター向けテックローンチポスター。</p>
<p><a href="styles/blue-hud-macro-product-poster/style.json"><strong>style.json を開く</strong></a> · <a href="styles/blue-hud-macro-product-poster">フォルダ</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/warm-fisheye-product-impact-ad-style"><img src="styles/warm-fisheye-product-impact-ad-style/preview-16x9.jpg" alt="Warm Fisheye Product Impact Ad preview"></a>
<h3>Warm Fisheye Product Impact Ad</h3>
<p>マクロ魚眼の商品トンネル、レンズ近くに迫る主役商品、巨大で斜めの白い中国語見出し、暖かなキャラメルブラウン照明、青いコールアウトタブ、下部の商品情報帯、光沢のある質感で構成する高密度な中国系ソーシャルコマース広告スタイル。</p>
<p><a href="styles/warm-fisheye-product-impact-ad-style/style.json"><strong>style.json を開く</strong></a> · <a href="styles/warm-fisheye-product-impact-ad-style">フォルダ</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/olive-scribble-sports-poster-style"><img src="styles/olive-scribble-sports-poster-style/preview-16x9.jpg" alt="Olive Scribble Sports Poster preview"></a>
<h3>Olive Scribble Sports Poster</h3>
<p>オフホワイトの紙地、不規則なオリーブ色ブロック、大きな斜めのアクション人物、粗い黒インク線、赤いマーカーの動線、黄緑のドライブラシ、スクリーンプリント質感で構成する手描き感の強いスポーツポスタースタイル。</p>
<p><a href="styles/olive-scribble-sports-poster-style/style.json"><strong>style.json を開く</strong></a> · <a href="styles/olive-scribble-sports-poster-style">フォルダ</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a href="styles/bold-anime-reaction-thumbnail-style"><img src="styles/bold-anime-reaction-thumbnail-style/preview-16x9.jpg" alt="Bold Anime Reaction Thumbnail preview"></a>
<h3>Bold Anime Reaction Thumbnail</h3>
<p>巨大なリアクションキャラクター、黄黒の大見出し、分割画面、シアンの発光リビール、クリーンなセル調イラストで作る高インパクトなアニメ系ウェブサムネイル。</p>
<p><a href="styles/bold-anime-reaction-thumbnail-style/style.json"><strong>style.json を開く</strong></a> · <a href="styles/bold-anime-reaction-thumbnail-style">フォルダ</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/turquoise-red-techno-manga-poster-style"><img src="styles/turquoise-red-techno-manga-poster-style/preview-16x9.jpg" alt="Turquoise Red Techno Manga Poster preview"></a>
<h3>Turquoise Red Techno Manga Poster</h3>
<p>クリーム色の紙面、巨大な赤橙のディスプレイ文字、ターコイズの技術服やハードウェア、密なメカ線画、注釈パネル、フラットなセル調シェーディング、少し褪せた印刷粒子で作るレトロなテクノ漫画ポスター。</p>
<p><a href="styles/turquoise-red-techno-manga-poster-style/style.json"><strong>style.json を開く</strong></a> · <a href="styles/turquoise-red-techno-manga-poster-style">フォルダ</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/chromatic-fisheye-orbit-pop-poster-style"><img src="styles/chromatic-fisheye-orbit-pop-poster-style/preview-16x9.jpg" alt="Chromatic Fisheye Orbit Pop Poster preview"></a>
<h3>Chromatic Fisheye Orbit Pop Poster</h3>
<p>凸面魚眼フォトドーム、巨大な周回タイポグラフィ、赤・オレンジ・マゼンタの文字、アクアの屈折アーク、暖かい白の余白、アナログ印刷粒子で作るハイキーなポップカルチャーポスター。</p>
<p><a href="styles/chromatic-fisheye-orbit-pop-poster-style/style.json"><strong>style.json を開く</strong></a> · <a href="styles/chromatic-fisheye-orbit-pop-poster-style">フォルダ</a></p>
</td>
</tr>
</table>

## パッケージ構成

```text
styles/<style-slug>/
  style.json          # 機械可読のプロンプトスタイルテンプレート
  preview-16x9.jpg    # 横長プレビュー
  preview-9x16.jpg    # 縦長プレビュー
```

## style.json v2.1

各 `style.json` は自己完結しています。ファイル全体を LLM にコピーし、`environment_variables` で宣言された変数に値を指定するか、`examples[*].values` のケースを編集して使います。

- `prompt_template` は `{VARIABLE}` プレースホルダーを持つ再利用可能なスタイルプロンプトです。
- `environment_variables` はテンプレートで使えるすべての変数を宣言します。
- `examples` は編集しやすいケース集で、各ケースは `case_name` と `values` だけを持ちます。
- `style_fidelity_anchors` と `source_content_to_avoid` は、保つべきスタイル要素とコピーしてはいけない元内容を分けます。
- `negative_prompt` はウォーターマーク、ロゴ、元画像の直接再現、スタイル外れを避けるために使います。

`prompt_9x16`、`prompt_16x9`、`full_prompt` のようなレンダリング済みプロンプトは保存しません。生成時に `prompt_template` と選んだ値から作るため、JSON は軽く、古くなりにくくなります。

検証コマンド：

```bash
python3 scripts/validate-style-json.py .
```

## スタイル索引

| # | スタイル | ファイル |
| --- | --- | --- |
| 1 | [Blue HUD Macro Creator Tech Poster](styles/blue-hud-macro-product-poster) | [style.json](styles/blue-hud-macro-product-poster/style.json) |
| 2 | [Warm Fisheye Product Impact Ad](styles/warm-fisheye-product-impact-ad-style) | [style.json](styles/warm-fisheye-product-impact-ad-style/style.json) |
| 3 | [Olive Scribble Sports Poster](styles/olive-scribble-sports-poster-style) | [style.json](styles/olive-scribble-sports-poster-style/style.json) |
| 4 | [Bold Anime Reaction Thumbnail](styles/bold-anime-reaction-thumbnail-style) | [style.json](styles/bold-anime-reaction-thumbnail-style/style.json) |
| 5 | [Turquoise Red Techno Manga Poster](styles/turquoise-red-techno-manga-poster-style) | [style.json](styles/turquoise-red-techno-manga-poster-style/style.json) |
| 6 | [Chromatic Fisheye Orbit Pop Poster](styles/chromatic-fisheye-orbit-pop-poster-style) | [style.json](styles/chromatic-fisheye-orbit-pop-poster-style/style.json) |
| 7 | [Naive Marker PSA Poster](styles/naive-marker-psa-poster-style) | [style.json](styles/naive-marker-psa-poster-style/style.json) |
| 8 | [Blue Bubble Fisheye Action Poster](styles/blue-bubble-fisheye-action-poster-style) | [style.json](styles/blue-bubble-fisheye-action-poster-style/style.json) |
| 9 | [Cozy Bedroom Doodle Companion Snapshot](styles/cozy-bedroom-doodle-companion-snapshot-style) | [style.json](styles/cozy-bedroom-doodle-companion-snapshot-style/style.json) |
| 10 | [Surreal Fish Doodle Landmark Photo Collage](styles/surreal-fish-doodle-landmark-photo-collage-style) | [style.json](styles/surreal-fish-doodle-landmark-photo-collage-style/style.json) |
| 11 | [Plush Comic Toy Product Poster](styles/plush-comic-toy-product-poster-style) | [style.json](styles/plush-comic-toy-product-poster-style/style.json) |
| 12 | [Rough Animation Pet Sketch Storyboard](styles/rough-animation-pet-sketch-storyboard-style) | [style.json](styles/rough-animation-pet-sketch-storyboard-style/style.json) |
| 13 | [Tri Color Hardcut Portrait Poster](styles/tri-color-hardcut-portrait-poster-style) | [style.json](styles/tri-color-hardcut-portrait-poster-style/style.json) |
| 14 | [Clean Triptych Travel Vlog Thumbnail](styles/clean-triptych-travel-vlog-thumbnail-style) | [style.json](styles/clean-triptych-travel-vlog-thumbnail-style/style.json) |
| 15 | [Playful Mascot Doodle Snapshot](styles/playful-mascot-doodle-snapshot-style) | [style.json](styles/playful-mascot-doodle-snapshot-style/style.json) |
| 16 | [Teenage Skate Scribble Screenprint Poster](styles/teenage-skate-scribble-screenprint-poster-style) | [style.json](styles/teenage-skate-scribble-screenprint-poster-style/style.json) |
| 17 | [Impact Burst Halftone Comic Poster](styles/impact-burst-halftone-comic-poster-style) | [style.json](styles/impact-burst-halftone-comic-poster-style/style.json) |
| 18 | [Sunburst Fisheye Bubble Type Poster](styles/sunburst-fisheye-bubble-type-poster-style) | [style.json](styles/sunburst-fisheye-bubble-type-poster-style/style.json) |
| 19 | [Backseat Transit Doodle Letter Poster](styles/backseat-transit-doodle-letter-poster-style) | [style.json](styles/backseat-transit-doodle-letter-poster-style/style.json) |
| 20 | [Analog Sticker Diary Portrait Poster](styles/analog-sticker-diary-portrait-poster-style) | [style.json](styles/analog-sticker-diary-portrait-poster-style/style.json) |
| 21 | [Folded Diamond Perspective Type Poster](styles/folded-diamond-perspective-type-poster-style) | [style.json](styles/folded-diamond-perspective-type-poster-style/style.json) |
| 22 | [Gothic Cat Doodle Photo Collage](styles/gothic-cat-doodle-photo-collage-style) | [style.json](styles/gothic-cat-doodle-photo-collage-style/style.json) |
| 23 | [K-pop Apocalypse Ransom Zine](styles/k-pop-apocalypse-ransom-zine-style) | [style.json](styles/k-pop-apocalypse-ransom-zine-style/style.json) |
| 24 | [Metro Doodle Snapshot Diary](styles/metro-doodle-snapshot-diary-style) | [style.json](styles/metro-doodle-snapshot-diary-style/style.json) |
| 25 | [Mountain Trail Monster Doodle Poster](styles/mountain-trail-monster-doodle-poster-style) | [style.json](styles/mountain-trail-monster-doodle-poster-style/style.json) |
| 26 | [Neon Doodle Gallery Snapshot](styles/neon-doodle-gallery-snapshot-style) | [style.json](styles/neon-doodle-gallery-snapshot-style/style.json) |
| 27 | [Neon Kinetic Typographic Poster](styles/neon-kinetic-typographic-poster-style) | [style.json](styles/neon-kinetic-typographic-poster-style/style.json) |
| 28 | [Orange Brush Mascot Action Poster](styles/orange-brush-mascot-action-poster-style) | [style.json](styles/orange-brush-mascot-action-poster-style/style.json) |
| 29 | [Photo Illustration Overlay Poster](styles/photo-illustration-overlay-poster-style) | [style.json](styles/photo-illustration-overlay-poster-style/style.json) |
| 30 | [Plush City Festival Mobile Poster](styles/plush-city-festival-mobile-poster-style) | [style.json](styles/plush-city-festival-mobile-poster-style/style.json) |
| 31 | [Pop Bubble Letter Photo Poster](styles/pop-bubble-letter-photo-poster-style) | [style.json](styles/pop-bubble-letter-photo-poster-style/style.json) |
| 32 | [Soft Analog Future Editorial Poster](styles/soft-analog-future-editorial-poster-style) | [style.json](styles/soft-analog-future-editorial-poster-style/style.json) |
| 33 | [Subway Doodle Photo Hybrid](styles/subway-doodle-photo-hybrid-style) | [style.json](styles/subway-doodle-photo-hybrid-style/style.json) |
| 34 | [Tokyo Kawaii Travel Collage Poster](styles/tokyo-kawaii-travel-collage-poster-style) | [style.json](styles/tokyo-kawaii-travel-collage-poster-style/style.json) |
| 35 | [Urban Transit Doodle Diary](styles/urban-transit-doodle-diary-style) | [style.json](styles/urban-transit-doodle-diary-style/style.json) |
| 36 | [Y2K Grunge Hip-hop Cutout Poster](styles/y2k-grunge-hiphop-cutout-poster-style) | [style.json](styles/y2k-grunge-hiphop-cutout-poster-style/style.json) |

## 公開方針

- 1 つのディレクトリ = 1 つのスタイル
- 新しいスタイルは注目スタイルとスタイル索引の上部に追加
- main ブランチには `style.json` と 2 枚のプレビュー JPG のみを配置
- 完全なギャラリーはこのリポジトリには含めません
- 元の参考画像、透かし、プラットフォームロゴ、QR コード、アカウント情報、非公開プロンプト、未許可のブランド素材は公開しません

## ライセンス

リポジトリ構造とドキュメントは MIT ライセンスです。各 `style.json` には個別のライセンス表記があります。プレビュー画像は視覚参照として含まれています。
