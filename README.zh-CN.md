<h1 align="center">AI Visual Prompt Cookbook</h1>

<p align="center">
  <img src="assets/hero-collage.jpg" alt="AI Visual Prompt Cookbook 风格展示">
</p>

<p align="center">
  <a href="README.md">English</a> |
  简体中文 |
  <a href="README.zh-TW.md">繁體中文</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.ko.md">한국어</a> |
  <a href="README.id.md">Bahasa Indonesia</a>
</p>

<p align="center">
  <img alt="风格数量" src="https://img.shields.io/badge/styles-36-ff5a7a?style=flat-square">
  <img alt="预览图" src="https://img.shields.io/badge/previews-72-4cc9f0?style=flat-square">
  <img alt="格式" src="https://img.shields.io/badge/format-style.json-111111?style=flat-square">
  <img alt="语言" src="https://img.shields.io/badge/languages-6-f7b801?style=flat-square">
</p>

<p align="center">
  <strong>复制一个 JSON，得到一种风格。</strong> 把一个 <code>style.json</code> 放进 ChatGPT、Claude、Nano Banana Pro、即梦或其他 LLM 图像工作流，替换变量，保留完整视觉系统。
</p>

<p align="center">
  这是一个面向 AI 图像生成的可复用视觉提示词风格库：每个风格都被整理成可直接使用的 <code>style.json</code>，并配套横竖两张预览图，方便浏览、复制和二次生成。
</p>

<p align="center">
  由 <a href="https://x.com/VigoCreativeAI">@VigoCreativeAI</a> 策划整理，并在 OpenAI Codex 的协助下结构化。Star 这个仓库可以持续关注新的风格更新。
</p>

## 快速入口

| 分类 | 适合做什么 | 先看这些 |
| --- | --- | --- |
| 照片 + 涂鸦 | 社交随拍、生活方式场景、轻快贴纸覆盖层 | [Playful Mascot Doodle Snapshot](#playful-mascot-doodle-snapshot), [Subway Doodle Photo Hybrid](#subway-doodle-photo-hybrid) |
| Zine + 拼贴 | 时尚海报、音乐视觉、极繁编辑排版 | [K-pop Apocalypse Ransom Zine](#k-pop-apocalypse-ransom-zine), [Y2K Grunge Hip-hop Cutout Poster](#y2k-grunge-hiphop-cutout-poster) |
| 字体海报 | 大标题系统、高冲击广告图、视觉冲击 | [Impact Burst Halftone Comic Poster](#impact-burst-halftone-comic-poster), [Neon Kinetic Typographic Poster](#neon-kinetic-typographic-poster) |
| 旅行 + 城市 | 目的地海报、街头场景、城市视觉日记 | [Clean Triptych Travel Vlog Thumbnail](#clean-triptych-travel-vlog-thumbnail), [Tokyo Kawaii Travel Collage Poster](#tokyo-kawaii-travel-collage-poster) |
| 编辑 + 极简 | 更干净的构图、结构化版式、安静的艺术指导 | [Tri Color Hardcut Portrait Poster](#tri-color-hardcut-portrait-poster), [Soft Analog Future Editorial Poster](#soft-analog-future-editorial-poster) |

## 为什么做这个项目

大多数 AI 图像提示词都是一次性的文本块：难复用、难比较，也难稳定迭代。这个项目采用另一种方式：把每一种视觉风格拆解成结构化的 `style.json`，你可以把它放进 ChatGPT、Claude 或其他 LLM 图像生成流程里。换主题时，风格结构仍然保持稳定。

## 快速开始

1. 浏览下面的 [精选风格](#精选风格)、[快速入口](#快速入口) 或 [风格索引](#风格索引)。
2. 打开某个风格目录，复制里面的 `style.json`。
3. 把完整 JSON 放进 ChatGPT、Claude、Nano Banana Pro、即梦或其他 LLM 图像工作流。
4. 根据 `environment_variables` 里的变量说明填写你的变量值，或直接修改 `examples[*].values` 里的案例值。
5. 生成最终图像提示词，再发送给你的图像模型。

示例指令：

```text
把这个 style.json 当作锁定的视觉风格。
使用这些变量值：
SUBJECT = 一位街头服装产品摄影师
LOCATION = 雨夜霓虹小巷
MAIN_TEXT = NIGHT DROP
ASPECT_RATIO = 16:9
```

## 精选风格

先看这 6 个，就能快速理解这个风格库的视觉跨度。每个风格都保持轻量：一个 JSON 加两张预览图。

<table>
<tr>
<td width="33%" valign="top">
<a href="styles/blue-hud-macro-product-poster"><img src="styles/blue-hud-macro-product-poster/preview-16x9.jpg" alt="Blue HUD Macro Creator Tech Poster preview"></a>
<h3>Blue HUD Macro Creator Tech Poster</h3>
<p>一种蓝色 HUD 创作者科技发布海报风格：微距 3D 硬件主视觉、超大的罗纹手套、电蓝色玻璃界面面板、巨大压缩白色标题字、密集功能卡片层级，以及一个暖金色性能徽章。</p>
<p><a href="styles/blue-hud-macro-product-poster/style.json"><strong>打开 style.json</strong></a> · <a href="styles/blue-hud-macro-product-poster">目录</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/warm-fisheye-product-impact-ad-style"><img src="styles/warm-fisheye-product-impact-ad-style/preview-16x9.jpg" alt="Warm Fisheye Product Impact Ad preview"></a>
<h3>Warm Fisheye Product Impact Ad</h3>
<p>一种密集的中文社交电商产品广告风格：微距鱼眼产品隧道、贴近镜头的主产品、巨大斜切白色中文标题、暖焦糖棕灯光、蓝色标注条、底部产品信息条和高光泽质感。</p>
<p><a href="styles/warm-fisheye-product-impact-ad-style/style.json"><strong>打开 style.json</strong></a> · <a href="styles/warm-fisheye-product-impact-ad-style">目录</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/olive-scribble-sports-poster-style"><img src="styles/olive-scribble-sports-poster-style/preview-16x9.jpg" alt="Olive Scribble Sports Poster preview"></a>
<h3>Olive Scribble Sports Poster</h3>
<p>一种动感手工体育海报风格：米白纸底、不规则橄榄绿块、超大斜向动作人物、粗黑墨线、红色马克笔运动弧、黄绿色干刷笔触和丝网印刷质感。</p>
<p><a href="styles/olive-scribble-sports-poster-style/style.json"><strong>打开 style.json</strong></a> · <a href="styles/olive-scribble-sports-poster-style">目录</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a href="styles/bold-anime-reaction-thumbnail-style"><img src="styles/bold-anime-reaction-thumbnail-style/preview-16x9.jpg" alt="Bold Anime Reaction Thumbnail preview"></a>
<h3>Bold Anime Reaction Thumbnail</h3>
<p>一种高冲击动漫网页缩略图风格：超大反应角色、巨大的黄黑标题字、分屏构图、青蓝发光揭示区和干净赛璐璐插画。</p>
<p><a href="styles/bold-anime-reaction-thumbnail-style/style.json"><strong>打开 style.json</strong></a> · <a href="styles/bold-anime-reaction-thumbnail-style">目录</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/turquoise-red-techno-manga-poster-style"><img src="styles/turquoise-red-techno-manga-poster-style/preview-16x9.jpg" alt="Turquoise Red Techno Manga Poster preview"></a>
<h3>Turquoise Red Techno Manga Poster</h3>
<p>一种复古科技漫画海报风格：奶油色纸张底、巨大红橙展示字、青绿色技术服装或硬件、密集机械线稿、标注面板、平面赛璐璐阴影和微微褪色的印刷颗粒。</p>
<p><a href="styles/turquoise-red-techno-manga-poster-style/style.json"><strong>打开 style.json</strong></a> · <a href="styles/turquoise-red-techno-manga-poster-style">目录</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/chromatic-fisheye-orbit-pop-poster-style"><img src="styles/chromatic-fisheye-orbit-pop-poster-style/preview-16x9.jpg" alt="Chromatic Fisheye Orbit Pop Poster preview"></a>
<h3>Chromatic Fisheye Orbit Pop Poster</h3>
<p>一种高调流行文化海报风格：凸面鱼眼照片圆顶、巨大环绕式红橙洋红字体、水蓝折射弧线、暖白留白和模拟印刷颗粒。</p>
<p><a href="styles/chromatic-fisheye-orbit-pop-poster-style/style.json"><strong>打开 style.json</strong></a> · <a href="styles/chromatic-fisheye-orbit-pop-poster-style">目录</a></p>
</td>
</tr>
</table>

## 文件结构

```text
styles/<style-slug>/
  style.json          # 机器可读的提示词风格模板
  preview-16x9.jpg    # 横屏预览图
  preview-9x16.jpg    # 竖屏预览图
```

## style.json v2.1

每个 `style.json` 都是自包含的：把完整文件复制给 LLM，然后根据 `environment_variables` 的变量说明填写新值，或直接改写某个 `examples[*].values` 案例。

- `prompt_template` 是带 `{VARIABLE}` 占位符的可复用风格提示词。
- `environment_variables` 声明模板里可使用的所有变量。
- `examples` 提供可直接改写的案例；每个案例只包含 `case_name` 和 `values`。
- `style_fidelity_anchors` 和 `source_content_to_avoid` 分别说明要保留的风格锚点，以及不能复制的源内容。
- `negative_prompt` 用来排除水印、Logo、直接复刻源图和偏离风格的输出。

仓库不会保存 `prompt_9x16`、`prompt_16x9` 或 `full_prompt` 这类渲染后的完整提示词。它们可以在生成时由 `prompt_template` 和变量值临时推导出来，这样 JSON 更轻，也不容易过期。

校验命令：

```bash
python3 scripts/validate-style-json.py .
```

## 风格索引

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

## 风格目录

### Blue HUD Macro Creator Tech Poster

<a href="styles/blue-hud-macro-product-poster"><img src="styles/blue-hud-macro-product-poster/preview-16x9.jpg" width="720" alt="Blue HUD Macro Creator Tech Poster preview"></a>

一种蓝色 HUD 创作者科技发布海报风格：微距 3D 硬件主视觉、超大的罗纹手套、电蓝色玻璃界面面板、巨大压缩白色标题字、密集功能卡片层级，以及一个暖金色性能徽章。

文件： [style.json](styles/blue-hud-macro-product-poster/style.json) · [16:9 预览](styles/blue-hud-macro-product-poster/preview-16x9.jpg) · [9:16 预览](styles/blue-hud-macro-product-poster/preview-9x16.jpg) · [目录](styles/blue-hud-macro-product-poster)

---

### Warm Fisheye Product Impact Ad

<a href="styles/warm-fisheye-product-impact-ad-style"><img src="styles/warm-fisheye-product-impact-ad-style/preview-16x9.jpg" width="720" alt="Warm Fisheye Product Impact Ad preview"></a>

一种密集的中文社交电商产品广告风格：微距鱼眼产品隧道、贴近镜头的主产品、巨大斜切白色中文标题、暖焦糖棕灯光、蓝色标注条、底部产品信息条和高光泽质感。

文件：[style.json](styles/warm-fisheye-product-impact-ad-style/style.json) · [16:9 预览](styles/warm-fisheye-product-impact-ad-style/preview-16x9.jpg) · [9:16 预览](styles/warm-fisheye-product-impact-ad-style/preview-9x16.jpg) · [目录](styles/warm-fisheye-product-impact-ad-style)

---

### Olive Scribble Sports Poster

<a href="styles/olive-scribble-sports-poster-style"><img src="styles/olive-scribble-sports-poster-style/preview-16x9.jpg" width="720" alt="Olive Scribble Sports Poster preview"></a>

一种动感手工体育海报风格：米白纸底、不规则橄榄绿块、超大斜向动作人物、粗黑墨线、红色马克笔运动弧、黄绿色干刷笔触和丝网印刷质感。

文件：[style.json](styles/olive-scribble-sports-poster-style/style.json) · [16:9 预览](styles/olive-scribble-sports-poster-style/preview-16x9.jpg) · [9:16 预览](styles/olive-scribble-sports-poster-style/preview-9x16.jpg) · [目录](styles/olive-scribble-sports-poster-style)

---

### Bold Anime Reaction Thumbnail

<a href="styles/bold-anime-reaction-thumbnail-style"><img src="styles/bold-anime-reaction-thumbnail-style/preview-16x9.jpg" width="720" alt="Bold Anime Reaction Thumbnail preview"></a>

一种高冲击动漫网页缩略图系统：超大反应角色、带硬黑阴影的醒目黄色标题字、分屏构图、较小的发光动作揭示区、冷蓝/青蓝背景，以及干净的赛璐璐插画质感。

文件：[style.json](styles/bold-anime-reaction-thumbnail-style/style.json) · [16:9 预览](styles/bold-anime-reaction-thumbnail-style/preview-16x9.jpg) · [9:16 预览](styles/bold-anime-reaction-thumbnail-style/preview-9x16.jpg) · [目录](styles/bold-anime-reaction-thumbnail-style)

---

### Turquoise Red Techno Manga Poster

<a href="styles/turquoise-red-techno-manga-poster-style"><img src="styles/turquoise-red-techno-manga-poster-style/preview-16x9.jpg" width="720" alt="Turquoise Red Techno Manga Poster preview"></a>

一种复古科技漫画海报系统：奶油色纸张底、巨大红色展示字、青绿色技术服装或硬件、密集机械线稿、标注面板、赛璐璐阴影人物绘制和微微褪色的印刷质感。

文件：[style.json](styles/turquoise-red-techno-manga-poster-style/style.json) · [16:9 预览](styles/turquoise-red-techno-manga-poster-style/preview-16x9.jpg) · [9:16 预览](styles/turquoise-red-techno-manga-poster-style/preview-9x16.jpg) · [目录](styles/turquoise-red-techno-manga-poster-style)

---

### Chromatic Fisheye Orbit Pop Poster

<a href="styles/chromatic-fisheye-orbit-pop-poster-style"><img src="styles/chromatic-fisheye-orbit-pop-poster-style/preview-16x9.jpg" width="720" alt="Chromatic Fisheye Orbit Pop Poster preview"></a>

一种高调流行文化海报系统：极端鱼眼摄影、中央凸面玻璃圆顶、超大环绕字体、红橙洋红字面、水蓝色折射光弧、暖白留白和轻微模拟印刷质感，像通过扭曲圆形镜头看到的当代音乐、时尚或文化活动主视觉。

文件：[style.json](styles/chromatic-fisheye-orbit-pop-poster-style/style.json) · [16:9 预览](styles/chromatic-fisheye-orbit-pop-poster-style/preview-16x9.jpg) · [9:16 预览](styles/chromatic-fisheye-orbit-pop-poster-style/preview-9x16.jpg) · [目录](styles/chromatic-fisheye-orbit-pop-poster-style)

---

### Naive Marker PSA Poster

<a href="styles/naive-marker-psa-poster-style"><img src="styles/naive-marker-psa-poster-style/preview-16x9.jpg" width="720" alt="Naive Marker PSA Poster preview"></a>

一种友好的手绘公共服务海报风格：粗糙马克笔线条、巨大蓝框对话牌标题、简化卡通人物、扁平公共场景道具、柔和纸张背景、警示符号和有意天真的透视。

文件：[style.json](styles/naive-marker-psa-poster-style/style.json) · [16:9 预览](styles/naive-marker-psa-poster-style/preview-16x9.jpg) · [9:16 预览](styles/naive-marker-psa-poster-style/preview-9x16.jpg) · [目录](styles/naive-marker-psa-poster-style)

---

### Blue Bubble Fisheye Action Poster

<a href="styles/blue-bubble-fisheye-action-poster-style"><img src="styles/blue-bubble-fisheye-action-poster-style/preview-16x9.jpg" width="720" alt="Blue Bubble Fisheye Action Poster preview"></a>

一种清爽白底青年文化动作海报风格：中央鱼眼动作照片、超大圆润皇家蓝字体、破框前景尺度、小号蓝色编辑文字，以及一个红色手绘圈注。

文件：[style.json](styles/blue-bubble-fisheye-action-poster-style/style.json) · [16:9 预览](styles/blue-bubble-fisheye-action-poster-style/preview-16x9.jpg) · [9:16 预览](styles/blue-bubble-fisheye-action-poster-style/preview-9x16.jpg) · [目录](styles/blue-bubble-fisheye-action-poster-style)

---

### Cozy Bedroom Doodle Companion Snapshot

<a href="styles/cozy-bedroom-doodle-companion-snapshot-style"><img src="styles/cozy-bedroom-doodle-companion-snapshot-style/preview-16x9.jpg" width="720" alt="Cozy Bedroom Doodle Companion Snapshot preview"></a>

一种温暖低光的居家随拍风格：在真实卧室、沙发或桌面照片前景叠加一个大型平面 2D 抱枕玩偶伙伴，形成安静的深夜创作日记氛围，并保留房间纹理、屏幕微光和少量手写涂鸦符号。

文件：[style.json](styles/cozy-bedroom-doodle-companion-snapshot-style/style.json) · [16:9 预览](styles/cozy-bedroom-doodle-companion-snapshot-style/preview-16x9.jpg) · [9:16 预览](styles/cozy-bedroom-doodle-companion-snapshot-style/preview-9x16.jpg) · [目录](styles/cozy-bedroom-doodle-companion-snapshot-style)

---

### Surreal Fish Doodle Landmark Photo Collage

<a href="styles/surreal-fish-doodle-landmark-photo-collage-style"><img src="styles/surreal-fish-doodle-landmark-photo-collage-style/preview-16x9.jpg" width="720" alt="Surreal Fish Doodle Landmark Photo Collage preview"></a>

一种明亮的旅行照片拼贴风格：在真实地标摄影上叠加巨大的平面 2D 卡通旅人、奇幻民俗鱼、黑色马克笔环线、飞溅符号和漫画星爆。

文件：[style.json](styles/surreal-fish-doodle-landmark-photo-collage-style/style.json) · [16:9 预览](styles/surreal-fish-doodle-landmark-photo-collage-style/preview-16x9.jpg) · [9:16 预览](styles/surreal-fish-doodle-landmark-photo-collage-style/preview-9x16.jpg) · [目录](styles/surreal-fish-doodle-landmark-photo-collage-style)

---

### Plush Comic Toy Product Poster

<a href="styles/plush-comic-toy-product-poster-style"><img src="styles/plush-comic-toy-product-poster-style/preview-16x9.jpg" width="720" alt="Plush Comic Toy Product Poster preview"></a>

一种高能玩具产品海报风格：以毛绒质感产品为主角，搭配复古奶油色海报纸、青蓝色圆形背景、超大倾斜漫画字体、厚重黑色阴影、涂鸦批注、贴纸标签和广告微文案。

文件：[style.json](styles/plush-comic-toy-product-poster-style/style.json) · [16:9 预览](styles/plush-comic-toy-product-poster-style/preview-16x9.jpg) · [9:16 预览](styles/plush-comic-toy-product-poster-style/preview-9x16.jpg) · [目录](styles/plush-comic-toy-product-poster-style)

---

### Rough Animation Pet Sketch Storyboard

<a href="styles/rough-animation-pet-sketch-storyboard-style"><img src="styles/rough-animation-pet-sketch-storyboard-style/preview-16x9.jpg" width="720" alt="Rough Animation Pet Sketch Storyboard preview"></a>

一种粗线动画宠物喜剧分镜草图风格：暖米色纸感、红棕色结构线、深酒红粗糙轮廓、半透明色洗、轻描室内背景和夸张动物表情。

文件：[style.json](styles/rough-animation-pet-sketch-storyboard-style/style.json) · [16:9 预览](styles/rough-animation-pet-sketch-storyboard-style/preview-16x9.jpg) · [9:16 预览](styles/rough-animation-pet-sketch-storyboard-style/preview-9x16.jpg) · [目录](styles/rough-animation-pet-sketch-storyboard-style)

---

### Tri Color Hardcut Portrait Poster

<a href="styles/tri-color-hardcut-portrait-poster-style"><img src="styles/tri-color-hardcut-portrait-poster-style/preview-16x9.jpg" width="720" alt="Tri Color Hardcut Portrait Poster preview"></a>

一种干净的三色硬切肖像海报风格：平面青绿色背景、珊瑚红主体色块、近黑色剪影与阴影，把所有细节压缩成大块、硬边、类矢量的剪影形状。

文件：[style.json](styles/tri-color-hardcut-portrait-poster-style/style.json) · [16:9 预览](styles/tri-color-hardcut-portrait-poster-style/preview-16x9.jpg) · [9:16 预览](styles/tri-color-hardcut-portrait-poster-style/preview-9x16.jpg) · [目录](styles/tri-color-hardcut-portrait-poster-style)

---

### Clean Triptych Travel Vlog Thumbnail

<a href="styles/clean-triptych-travel-vlog-thumbnail-style"><img src="styles/clean-triptych-travel-vlog-thumbnail-style/preview-16x9.jpg" width="720" alt="Clean Triptych Travel Vlog Thumbnail preview"></a>

一种干净的旅行 vlog 缩略图系统：三栏竖向摄影拼接、超大的小写白色目的地标题、小号斜体旅行批注、少量手绘白色符号，以及柔和的手机摄影编辑质感。

文件：[style.json](styles/clean-triptych-travel-vlog-thumbnail-style/style.json) · [16:9 预览](styles/clean-triptych-travel-vlog-thumbnail-style/preview-16x9.jpg) · [9:16 预览](styles/clean-triptych-travel-vlog-thumbnail-style/preview-9x16.jpg) · [目录](styles/clean-triptych-travel-vlog-thumbnail-style)

---

### Playful Mascot Doodle Snapshot

<a href="styles/playful-mascot-doodle-snapshot-style"><img src="styles/playful-mascot-doodle-snapshot-style/preview-16x9.jpg" width="720" alt="Playful Mascot Doodle Snapshot preview"></a>

一种把真实生活社交照片转成轻快贴纸拼贴海报的风格：在摄影场景上叠加原创卡通吉祥物贴纸、手绘描边、丝带标题牌、闪光、螺旋和草稿感装饰符号。

文件：[style.json](styles/playful-mascot-doodle-snapshot-style/style.json) · [16:9 预览](styles/playful-mascot-doodle-snapshot-style/preview-16x9.jpg) · [9:16 预览](styles/playful-mascot-doodle-snapshot-style/preview-9x16.jpg) · [目录](styles/playful-mascot-doodle-snapshot-style)

---

### Teenage Skate Scribble Screenprint Poster

<a href="styles/teenage-skate-scribble-screenprint-poster-style"><img src="styles/teenage-skate-scribble-screenprint-poster-style/preview-16x9.jpg" width="720" alt="Teenage Skate Scribble Screenprint Poster preview"></a>

一种复古滑板 zine 海报风格：扭曲的中央滑板人物剪贴、奶油纸张底、松散红色手写边框字、粗粝双色丝网印刷质感，以及海军蓝、灰、绿、赭色的有限街头配色。

文件：[style.json](styles/teenage-skate-scribble-screenprint-poster-style/style.json) · [16:9 预览](styles/teenage-skate-scribble-screenprint-poster-style/preview-16x9.jpg) · [9:16 预览](styles/teenage-skate-scribble-screenprint-poster-style/preview-9x16.jpg) · [目录](styles/teenage-skate-scribble-screenprint-poster-style)

---

### Impact Burst Halftone Comic Poster

<a href="styles/impact-burst-halftone-comic-poster-style"><img src="styles/impact-burst-halftone-comic-poster-style/preview-16x9.jpg" width="720" alt="Impact Burst Halftone Comic Poster preview"></a>

一种响亮的复古漫画海报系统：厚重黑色墨线、扁平高饱和色块、超大冲击字体、夸张插画主体、对角道具、对话爆裂形、烟雾团、半色调网点和做旧丝网印刷颗粒。

文件：[style.json](styles/impact-burst-halftone-comic-poster-style/style.json) · [16:9 预览](styles/impact-burst-halftone-comic-poster-style/preview-16x9.jpg) · [9:16 预览](styles/impact-burst-halftone-comic-poster-style/preview-9x16.jpg) · [目录](styles/impact-burst-halftone-comic-poster-style)

---

### Sunburst Fisheye Bubble Type Poster

<a href="styles/sunburst-fisheye-bubble-type-poster-style"><img src="styles/sunburst-fisheye-bubble-type-poster-style/preview-16x9.jpg" width="720" alt="Sunburst Fisheye Bubble Type Poster preview"></a>

一种超低机位鱼眼夏日生活方式海报风格：近距离摄影主体、饱和钴蓝天空、巨大的拱形柠檬黄色泡泡字体、暖橙色文字阴影、Y2K 配饰和明显的模拟胶片颗粒。

文件：[style.json](styles/sunburst-fisheye-bubble-type-poster-style/style.json) · [16:9 预览](styles/sunburst-fisheye-bubble-type-poster-style/preview-16x9.jpg) · [9:16 预览](styles/sunburst-fisheye-bubble-type-poster-style/preview-9x16.jpg) · [目录](styles/sunburst-fisheye-bubble-type-poster-style)

---

### Backseat Transit Doodle Letter Poster

<a href="styles/backseat-transit-doodle-letter-poster-style"><img src="styles/backseat-transit-doodle-letter-poster-style/preview-16x9.jpg" width="720" alt="Backseat Transit Doodle Letter Poster preview"></a>

一种把真实乘客视角交通照片转化为高能旅行海报的风格：后视中央人物、电光黄色剪影光晕、巨大的黄橙色手绘字母、漫画放射线、紫色音乐符号、贴纸图标和青白色云朵涂鸦。

文件：[style.json](styles/backseat-transit-doodle-letter-poster-style/style.json) · [16:9 预览](styles/backseat-transit-doodle-letter-poster-style/preview-16x9.jpg) · [9:16 预览](styles/backseat-transit-doodle-letter-poster-style/preview-9x16.jpg) · [目录](styles/backseat-transit-doodle-letter-poster-style)

---

### Analog Sticker Diary Portrait Poster

<a href="styles/analog-sticker-diary-portrait-poster-style"><img src="styles/analog-sticker-diary-portrait-poster-style/preview-16x9.jpg" width="720" alt="Analog Sticker Diary Portrait Poster preview"></a>

一种怀旧模拟日记拼贴肖像系统：大型侧脸插画人物、奶油色方格纸背景、贴纸化的私人小物、磨损橙色手写字和厚重的扫描印刷质感。

文件：[style.json](styles/analog-sticker-diary-portrait-poster-style/style.json) · [16:9 预览](styles/analog-sticker-diary-portrait-poster-style/preview-16x9.jpg) · [9:16 预览](styles/analog-sticker-diary-portrait-poster-style/preview-9x16.jpg) · [目录](styles/analog-sticker-diary-portrait-poster-style)

---

### Folded Diamond Perspective Type Poster

<a href="styles/folded-diamond-perspective-type-poster-style"><img src="styles/folded-diamond-perspective-type-poster-style/preview-16x9.jpg" width="720" alt="Folded Diamond Perspective Type Poster preview"></a>

一种大胆的极简编辑海报风格：低机位英雄摄影嵌入菱形开口，折叠的棕褐色纸张或帆布平面，以及印在下方平面上的巨大白色透视字体。

文件：[style.json](styles/folded-diamond-perspective-type-poster-style/style.json) · [16:9 预览](styles/folded-diamond-perspective-type-poster-style/preview-16x9.jpg) · [9:16 预览](styles/folded-diamond-perspective-type-poster-style/preview-9x16.jpg) · [目录](styles/folded-diamond-perspective-type-poster-style)

---

### Gothic Cat Doodle Photo Collage

<a href="styles/gothic-cat-doodle-photo-collage-style"><img src="styles/gothic-cat-doodle-photo-collage-style/preview-16x9.jpg" width="720" alt="Gothic Cat Doodle Photo Collage preview"></a>

一种玩趣的摄影插画拼贴风格：戏剧化真实建筑摄影、超大扁平卡通生物叠加、圆润手绘标题字和松散马克笔涂鸦。

文件：[style.json](styles/gothic-cat-doodle-photo-collage-style/style.json) · [16:9 预览](styles/gothic-cat-doodle-photo-collage-style/preview-16x9.jpg) · [9:16 预览](styles/gothic-cat-doodle-photo-collage-style/preview-9x16.jpg) · [目录](styles/gothic-cat-doodle-photo-collage-style)

---

### K-pop Apocalypse Ransom Zine

<a href="styles/k-pop-apocalypse-ransom-zine-style"><img src="styles/k-pop-apocalypse-ransom-zine-style/preview-16x9.jpg" width="720" alt="K-pop Apocalypse Ransom Zine preview"></a>

一种极繁 K-pop 时尚 zine 拼贴风格：中央人物剪贴、揉皱黑白纸张质感、倾斜勒索信式排版、响亮贴纸块、饱和青柠/蓝/红点缀，以及醒目的底部刊头色带。

文件：[style.json](styles/k-pop-apocalypse-ransom-zine-style/style.json) · [16:9 预览](styles/k-pop-apocalypse-ransom-zine-style/preview-16x9.jpg) · [9:16 预览](styles/k-pop-apocalypse-ransom-zine-style/preview-9x16.jpg) · [目录](styles/k-pop-apocalypse-ransom-zine-style)

---

### Metro Doodle Snapshot Diary

<a href="styles/metro-doodle-snapshot-diary-style"><img src="styles/metro-doodle-snapshot-diary-style/preview-16x9.jpg" width="720" alt="Metro Doodle Snapshot Diary preview"></a>

一种手持城市交通照片拼贴风格：真实拥挤的地铁、公交、电车或车站快照，叠加马克笔感卡通涂鸦、超大前景手势、白色手写日记文字和高饱和漫画脸。

文件：[style.json](styles/metro-doodle-snapshot-diary-style/style.json) · [16:9 预览](styles/metro-doodle-snapshot-diary-style/preview-16x9.jpg) · [9:16 预览](styles/metro-doodle-snapshot-diary-style/preview-9x16.jpg) · [目录](styles/metro-doodle-snapshot-diary-style)

---

### Mountain Trail Monster Doodle Poster

<a href="styles/mountain-trail-monster-doodle-poster-style"><img src="styles/mountain-trail-monster-doodle-poster-style/preview-16x9.jpg" width="720" alt="Mountain Trail Monster Doodle Poster preview"></a>

一种把户外徒步随手拍改造成冒险海报的拼贴风格：真实山路照片、扁平手绘怪物伙伴、超大西班牙语漫画字和松散草图标注。

文件：[style.json](styles/mountain-trail-monster-doodle-poster-style/style.json) · [16:9 预览](styles/mountain-trail-monster-doodle-poster-style/preview-16x9.jpg) · [9:16 预览](styles/mountain-trail-monster-doodle-poster-style/preview-9x16.jpg) · [目录](styles/mountain-trail-monster-doodle-poster-style)

---

### Neon Doodle Gallery Snapshot

<a href="styles/neon-doodle-gallery-snapshot-style"><img src="styles/neon-doodle-gallery-snapshot-style/preview-16x9.jpg" width="720" alt="Neon Doodle Gallery Snapshot preview"></a>

一种手机随拍叠加霓虹数字马克笔涂鸦的风格：热粉和青色人物描边、黄色怪物尖刺、粗糙手写标题、星星、爪印、蛛网角标、涂抹条、光环、植物和学生日记感。

文件：[style.json](styles/neon-doodle-gallery-snapshot-style/style.json) · [16:9 预览](styles/neon-doodle-gallery-snapshot-style/preview-16x9.jpg) · [9:16 预览](styles/neon-doodle-gallery-snapshot-style/preview-9x16.jpg) · [目录](styles/neon-doodle-gallery-snapshot-style)

---

### Neon Kinetic Typographic Poster

<a href="styles/neon-kinetic-typographic-poster-style"><img src="styles/neon-kinetic-typographic-poster-style/preview-16x9.jpg" width="720" alt="Neon Kinetic Typographic Poster preview"></a>

一种戏剧化户外编辑海报风格：低机位生活方式摄影、巨大的变形霓虹字体、胶片颗粒，以及高能青年文化广告视觉。

文件：[style.json](styles/neon-kinetic-typographic-poster-style/style.json) · [16:9 预览](styles/neon-kinetic-typographic-poster-style/preview-16x9.jpg) · [9:16 预览](styles/neon-kinetic-typographic-poster-style/preview-9x16.jpg) · [目录](styles/neon-kinetic-typographic-poster-style)

---

### Orange Brush Mascot Action Poster

<a href="styles/orange-brush-mascot-action-poster-style"><img src="styles/orange-brush-mascot-action-poster-style/preview-16x9.jpg" width="720" alt="Orange Brush Mascot Action Poster preview"></a>

一种稀疏的橙白黑扁平插画系统：白色吉祥物人物、超大道具、粗糙黑色干刷线条、橙色脸颊圆点和丝网印刷纸张颗粒。

文件：[style.json](styles/orange-brush-mascot-action-poster-style/style.json) · [16:9 预览](styles/orange-brush-mascot-action-poster-style/preview-16x9.jpg) · [9:16 预览](styles/orange-brush-mascot-action-poster-style/preview-9x16.jpg) · [目录](styles/orange-brush-mascot-action-poster-style)

---

### Photo Illustration Overlay Poster

<a href="styles/photo-illustration-overlay-poster-style"><img src="styles/photo-illustration-overlay-poster-style/preview-16x9.jpg" width="720" alt="Photo Illustration Overlay Poster preview"></a>

一种真实城市照片叠加高饱和扁平 2D 卡通人物的海报风格，并加入手绘星星、火花、箭头和漫画符号。

文件：[style.json](styles/photo-illustration-overlay-poster-style/style.json) · [16:9 预览](styles/photo-illustration-overlay-poster-style/preview-16x9.jpg) · [9:16 预览](styles/photo-illustration-overlay-poster-style/preview-9x16.jpg) · [目录](styles/photo-illustration-overlay-poster-style)

---

### Plush City Festival Mobile Poster

<a href="styles/plush-city-festival-mobile-poster-style"><img src="styles/plush-city-festival-mobile-poster-style/preview-16x9.jpg" width="720" alt="Plush City Festival Mobile Poster preview"></a>

一种明亮的移动端活动海报风格：真实城市地标、柔软毛绒吉祥物、圆角 App 卡片式框架、醒目的白色节日字体、日期地点信息和友好的旅游推广气质。

文件：[style.json](styles/plush-city-festival-mobile-poster-style/style.json) · [16:9 预览](styles/plush-city-festival-mobile-poster-style/preview-16x9.jpg) · [9:16 预览](styles/plush-city-festival-mobile-poster-style/preview-9x16.jpg) · [目录](styles/plush-city-festival-mobile-poster-style)

---

### Pop Bubble Letter Photo Poster

<a href="styles/pop-bubble-letter-photo-poster-style"><img src="styles/pop-bubble-letter-photo-poster-style/preview-16x9.jpg" width="720" alt="Pop Bubble Letter Photo Poster preview"></a>

一种有冲击力的摄影插画海报风格：低机位时尚肖像位于中心，周围是超大扁平泡泡字形、糖果色、高对比黑色描边、椭圆高光和清脆闪光符号。

文件：[style.json](styles/pop-bubble-letter-photo-poster-style/style.json) · [16:9 预览](styles/pop-bubble-letter-photo-poster-style/preview-16x9.jpg) · [9:16 预览](styles/pop-bubble-letter-photo-poster-style/preview-9x16.jpg) · [目录](styles/pop-bubble-letter-photo-poster-style)

---

### Soft Analog Future Editorial Poster

<a href="styles/soft-analog-future-editorial-poster-style"><img src="styles/soft-analog-future-editorial-poster-style/preview-16x9.jpg" width="720" alt="Soft Analog Future Editorial Poster preview"></a>

一种安静的模拟未来编辑海报风格：暖奶油纸张、超大黑色 neo-grotesk 字体、严格网格规则、复古科技静物、浅蓝半透明界面面板、植物前景点缀和细小双语信息设计。

文件：[style.json](styles/soft-analog-future-editorial-poster-style/style.json) · [16:9 预览](styles/soft-analog-future-editorial-poster-style/preview-16x9.jpg) · [9:16 预览](styles/soft-analog-future-editorial-poster-style/preview-9x16.jpg) · [目录](styles/soft-analog-future-editorial-poster-style)

---

### Subway Doodle Photo Hybrid

<a href="styles/subway-doodle-photo-hybrid-style"><img src="styles/subway-doodle-photo-hybrid-style/preview-16x9.jpg" width="720" alt="Subway Doodle Photo Hybrid preview"></a>

一种手机拍摄的城市交通海报风格：纪实地铁或街头交通摄影，叠加表现性手绘卡通覆盖层、涂鸦人物脸、超大前景手势、手写笔记和社交媒体截图质感。

文件：[style.json](styles/subway-doodle-photo-hybrid-style/style.json) · [16:9 预览](styles/subway-doodle-photo-hybrid-style/preview-16x9.jpg) · [9:16 预览](styles/subway-doodle-photo-hybrid-style/preview-9x16.jpg) · [目录](styles/subway-doodle-photo-hybrid-style)

---

### Tokyo Kawaii Travel Collage Poster

<a href="styles/tokyo-kawaii-travel-collage-poster-style"><img src="styles/tokyo-kawaii-travel-collage-poster-style/preview-16x9.jpg" width="720" alt="Tokyo Kawaii Travel Collage Poster preview"></a>

一种极繁日式城市旅行拼贴风格：醒目的目的地字体、可爱贴纸元素、漫画对话框、剪贴时尚摄影、半色调城市背景和 scrapbook 编辑版式。

文件：[style.json](styles/tokyo-kawaii-travel-collage-poster-style/style.json) · [16:9 预览](styles/tokyo-kawaii-travel-collage-poster-style/preview-16x9.jpg) · [9:16 预览](styles/tokyo-kawaii-travel-collage-poster-style/preview-9x16.jpg) · [目录](styles/tokyo-kawaii-travel-collage-poster-style)

---

### Urban Transit Doodle Diary

<a href="styles/urban-transit-doodle-diary-style"><img src="styles/urban-transit-doodle-diary-style/preview-16x9.jpg" width="720" alt="Urban Transit Doodle Diary preview"></a>

一种把原始城市公共空间快照处理成私人视觉日记的风格：真实照片、粗重手绘漫画覆盖层、手写旅行笔记、饱和卡通脸和大面积前景手势。

文件：[style.json](styles/urban-transit-doodle-diary-style/style.json) · [16:9 预览](styles/urban-transit-doodle-diary-style/preview-16x9.jpg) · [9:16 预览](styles/urban-transit-doodle-diary-style/preview-9x16.jpg) · [目录](styles/urban-transit-doodle-diary-style)

---

### Y2K Grunge Hip-hop Cutout Poster

<a href="styles/y2k-grunge-hiphop-cutout-poster-style"><img src="styles/y2k-grunge-hiphop-cutout-poster-style/preview-16x9.jpg" width="720" alt="Y2K Grunge Hip-hop Cutout Poster preview"></a>

一种 Y2K grunge hip-hop 杂志拼贴海报风格：超大照片剪贴、酸黄色复古字体、粗糙黑白墙面质感、密集编辑页脚信息区和复印机印刷噪点。

文件：[style.json](styles/y2k-grunge-hiphop-cutout-poster-style/style.json) · [16:9 预览](styles/y2k-grunge-hiphop-cutout-poster-style/preview-16x9.jpg) · [9:16 预览](styles/y2k-grunge-hiphop-cutout-poster-style/preview-9x16.jpg) · [目录](styles/y2k-grunge-hiphop-cutout-poster-style)

## 发布规则

- 一个目录 = 一个风格
- 新风格优先出现在精选风格和风格索引顶部
- 主分支只放 `style.json` 和两张预览 JPG
- 完整图库不放在这个仓库里
- 不发布原始参考图、水印图、平台标识、二维码、账号信息、私有提示词，或未经授权的品牌素材

## 许可证

仓库结构和文档采用 MIT。每个 `style.json` 会声明自己的授权方式。预览图仅作为视觉参考随仓库展示。
