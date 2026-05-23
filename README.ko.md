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
  <img alt="Styles" src="https://img.shields.io/badge/styles-36-ff5a7a?style=flat-square">
  <img alt="Previews" src="https://img.shields.io/badge/previews-72-4cc9f0?style=flat-square">
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

## 빠른 링크

| 카테고리 | 적합한 용도 | 먼저 볼 스타일 |
| --- | --- | --- |
| 사진 + 드로잉 | 소셜 스냅, 라이프스타일 장면, 장난스러운 스티커 오버레이 | [Playful Mascot Doodle Snapshot](styles/playful-mascot-doodle-snapshot-style), [Subway Doodle Photo Hybrid](styles/subway-doodle-photo-hybrid-style) |
| Zine + 콜라주 | 패션 포스터, 음악 비주얼, 맥시멀 에디토리얼 레이아웃 | [K-pop Apocalypse Ransom Zine](styles/k-pop-apocalypse-ransom-zine-style), [Y2K Grunge Hip-hop Cutout Poster](styles/y2k-grunge-hiphop-cutout-poster-style) |
| 타이포그래피 포스터 | 큰 헤드라인, 강한 캠페인 그래픽, 시각적 임팩트 | [Impact Burst Halftone Comic Poster](styles/impact-burst-halftone-comic-poster-style), [Neon Kinetic Typographic Poster](styles/neon-kinetic-typographic-poster-style) |
| 여행 + 도시 | 여행지 포스터, 거리 장면, 도시 비주얼 다이어리 | [Tokyo Kawaii Travel Collage Poster](styles/tokyo-kawaii-travel-collage-poster-style), [Urban Transit Doodle Diary](styles/urban-transit-doodle-diary-style) |
| 에디토리얼 + 미니멀 | 깔끔한 구성, 구조적인 레이아웃, 차분한 아트 디렉션 | [Soft Analog Future Editorial Poster](styles/soft-analog-future-editorial-poster-style), [Folded Diamond Perspective Type Poster](styles/folded-diamond-perspective-type-poster-style) |

## 이 프로젝트를 만든 이유

대부분의 AI 이미지 프롬프트는 한 번 쓰고 버리는 텍스트 덩어리라 재사용, 비교, 반복 개선이 어렵습니다. 이 저장소는 각 비주얼 스타일을 구조화된 `style.json` 으로 분해합니다. 주제는 바꿔도 스타일 구조는 유지할 수 있습니다.

## 빠른 시작

1. [추천 스타일](#추천-스타일), [빠른 링크](#빠른-링크), [스타일 인덱스](#스타일-인덱스)를 둘러봅니다.
2. 원하는 스타일 폴더를 열고 `style.json` 을 복사합니다.
3. 전체 JSON 을 ChatGPT, Claude, Nano Banana Pro 또는 원하는 LLM 이미지 워크플로에 붙여 넣습니다.
4. `environment_variables` 에 선언된 변수에 값을 지정하거나 `examples[*].values` 의 사례 값을 수정합니다.
5. 최종 이미지 프롬프트를 생성해 이미지 모델로 보냅니다.

예시 지시문:

```text
이 style.json 을 고정된 비주얼 스타일로 사용하세요.
아래 변수 값을 사용하세요:
SUBJECT = 스트리트웨어 제품 사진가
LOCATION = 비 오는 네온 골목
MAIN_TEXT = NIGHT DROP
ASPECT_RATIO = 16:9
```

## 추천 스타일

이 6가지만 보면 라이브러리의 시각적 범위를 빠르게 이해할 수 있습니다. 모든 스타일은 JSON 하나와 미리보기 이미지 두 장으로 구성됩니다.

<table>
<tr>
<td width="33%" valign="top">
<a href="styles/blue-hud-macro-product-poster"><img src="styles/blue-hud-macro-product-poster/preview-16x9.jpg" alt="Blue HUD Macro Creator Tech Poster preview"></a>
<h3>Blue HUD Macro Creator Tech Poster</h3>
<p>매크로 3D 하드웨어 히어로, 큼직한 리브 장갑, 전기빛 시안 HUD 글래스 패널, 거대한 압축형 흰색 타이포그래피, 촘촘한 기능 카드 레이어, 하나의 따뜻한 골드 성능 배지로 구성한 블루 크리에이터 테크 런칭 포스터 스타일.</p>
<p><a href="styles/blue-hud-macro-product-poster/style.json"><strong>style.json 열기</strong></a> · <a href="styles/blue-hud-macro-product-poster">폴더</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/warm-fisheye-product-impact-ad-style"><img src="styles/warm-fisheye-product-impact-ad-style/preview-16x9.jpg" alt="Warm Fisheye Product Impact Ad preview"></a>
<h3>Warm Fisheye Product Impact Ad</h3>
<p>매크로 어안 제품 터널, 렌즈 가까이 잘린 히어로 제품, 거대한 기울어진 흰색 중국어 헤드라인, 따뜻한 캐러멜 브라운 조명, 파란 콜아웃 탭, 하단 제품 정보 스트립, 광택 있는 질감으로 구성된 고밀도 중국 소셜커머스 광고 스타일입니다.</p>
<p><a href="styles/warm-fisheye-product-impact-ad-style/style.json"><strong>style.json 열기</strong></a> · <a href="styles/warm-fisheye-product-impact-ad-style">폴더</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/olive-scribble-sports-poster-style"><img src="styles/olive-scribble-sports-poster-style/preview-16x9.jpg" alt="Olive Scribble Sports Poster preview"></a>
<h3>Olive Scribble Sports Poster</h3>
<p>오프화이트 종이 바탕, 불규칙한 올리브 블록, 크게 배치된 대각선 액션 인물, 거친 검정 잉크 윤곽, 빨간 마커 모션 아크, 노랑빛 그린 드라이브러시, 스크린프린트 질감으로 구성된 수작업 스포츠 포스터 스타일입니다.</p>
<p><a href="styles/olive-scribble-sports-poster-style/style.json"><strong>style.json 열기</strong></a> · <a href="styles/olive-scribble-sports-poster-style">폴더</a></p>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a href="styles/bold-anime-reaction-thumbnail-style"><img src="styles/bold-anime-reaction-thumbnail-style/preview-16x9.jpg" alt="Bold Anime Reaction Thumbnail preview"></a>
<h3>Bold Anime Reaction Thumbnail</h3>
<p>대형 리액션 캐릭터, 거대한 노랑-검정 헤드라인, 분할 화면 구성, 시안 글로우 리빌, 깔끔한 셀 셰이딩 일러스트를 결합한 고임팩트 애니메이션 웹 썸네일 스타일.</p>
<p><a href="styles/bold-anime-reaction-thumbnail-style/style.json"><strong>style.json 열기</strong></a> · <a href="styles/bold-anime-reaction-thumbnail-style">폴더</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/turquoise-red-techno-manga-poster-style"><img src="styles/turquoise-red-techno-manga-poster-style/preview-16x9.jpg" alt="Turquoise Red Techno Manga Poster preview"></a>
<h3>Turquoise Red Techno Manga Poster</h3>
<p>크림색 종이 바탕, 거대한 레드오렌지 디스플레이 글자, 터쿼이즈 기술 의상이나 하드웨어, 촘촘한 기계 선화, 주석 패널, 평면 셀 셰이딩, 살짝 바랜 인쇄 입자를 결합한 레트로 테크노 만화 포스터 스타일.</p>
<p><a href="styles/turquoise-red-techno-manga-poster-style/style.json"><strong>style.json 열기</strong></a> · <a href="styles/turquoise-red-techno-manga-poster-style">폴더</a></p>
</td>
<td width="33%" valign="top">
<a href="styles/chromatic-fisheye-orbit-pop-poster-style"><img src="styles/chromatic-fisheye-orbit-pop-poster-style/preview-16x9.jpg" alt="Chromatic Fisheye Orbit Pop Poster preview"></a>
<h3>Chromatic Fisheye Orbit Pop Poster</h3>
<p>볼록한 피시아이 포토 돔, 거대한 궤도형 타이포그래피, 레드/오렌지/마젠타 글자, 아쿠아 굴절 아크, 따뜻한 흰 여백, 아날로그 인쇄 입자를 결합한 하이키 팝 컬처 포스터 스타일.</p>
<p><a href="styles/chromatic-fisheye-orbit-pop-poster-style/style.json"><strong>style.json 열기</strong></a> · <a href="styles/chromatic-fisheye-orbit-pop-poster-style">폴더</a></p>
</td>
</tr>
</table>

## 패키지 구조

```text
styles/<style-slug>/
  style.json          # 기계가 읽을 수 있는 프롬프트 스타일 템플릿
  preview-16x9.jpg    # 가로 미리보기
  preview-9x16.jpg    # 세로 미리보기
```

## style.json v2.1

각 `style.json` 은 자체 완결형입니다. 파일 전체를 LLM 에 복사한 뒤 `environment_variables` 에 선언된 변수에 값을 지정하거나 `examples[*].values` 의 사례 값을 수정하면 됩니다.

- `prompt_template` 은 `{VARIABLE}` 플레이스홀더가 있는 재사용 가능한 스타일 프롬프트입니다.
- `environment_variables` 는 템플릿에서 사용할 수 있는 모든 변수를 선언합니다.
- `examples` 는 바로 수정할 수 있는 사례이며, 각 사례는 `case_name` 과 `values` 만 저장합니다.
- `style_fidelity_anchors` 와 `source_content_to_avoid` 는 유지해야 할 스타일 요소와 복사하면 안 되는 원본 요소를 구분합니다.
- `negative_prompt` 는 워터마크, 로고, 원본 직접 재현, 스타일 이탈을 줄입니다.

`prompt_9x16`, `prompt_16x9`, `full_prompt` 같은 렌더링된 전체 프롬프트는 저장하지 않습니다. 생성 시점에 `prompt_template` 과 선택한 값으로 만들기 때문에 JSON 이 가볍고 오래 유지됩니다.

검증 명령:

```bash
python3 scripts/validate-style-json.py .
```

## 스타일 인덱스

| # | 스타일 | 파일 |
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

## 게시 모델

- 하나의 디렉터리 = 하나의 스타일
- 새 스타일은 추천 스타일과 스타일 인덱스 상단에 추가
- main 브랜치에는 `style.json` 과 두 장의 JPG 미리보기만 포함
- 전체 갤러리는 이 저장소에 포함하지 않습니다
- 원본 레퍼런스 이미지, 워터마크, 플랫폼 식별자, QR 코드, 계정 핸들, 비공개 프롬프트, 허가되지 않은 브랜드 자산은 게시하지 않습니다

## 라이선스

저장소 구조와 문서는 MIT 라이선스입니다. 각 `style.json` 파일은 자체 라이선스를 명시합니다. 미리보기 이미지는 시각 참고용으로 포함되어 있습니다.
