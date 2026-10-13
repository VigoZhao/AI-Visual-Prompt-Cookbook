# Contributing to AI Visual Prompt Cookbook

## How to Submit a New Style

1. Fork the repository and create a new branch.
2. Add a new directory under `styles/<slug>/`.
3. Add exactly one `style.json` file and two preview images.
4. Add the style to the top of `"styles"` in `data/catalog.json` with a one-line gallery `summary`, then run `python3 scripts/generate-readme.py` to update every README and `docs/CATALOG.md`.
5. Run the validation command.
6. Open a pull request with a short description of the visual system and sample use cases.

## Style Slug Naming

- Use lowercase English kebab-case.
- Keep the slug descriptive and no longer than 60 characters.
- Prefer concrete style words over generic labels.
- Match the folder name, `style_slug`, and copy-prompt filename.

## style.json Requirements

Each public style must include these fields:

- `prompt_template`
- `environment_variables`
- `examples`
- `style_fidelity_anchors`
- `source_content_to_avoid`
- `negative_prompt`
- `category` (`Photo + Doodle`, `Zine + Collage`, `Type Posters`, `Travel + City`, `Editorial + Minimal`, or `Product + Campaign`)

The template should preserve the reusable visual system while requiring new subject matter, text, and scene values.

## Preview Image Requirements

- Filenames must be exactly `preview-16x9.jpg` and `preview-9x16.jpg`.
- Recommended minimum resolution: 1280x720 for 16:9 and 720x1280 for 9:16.
- Use JPG format, preferably under 1MB and always under 5MB.
- Avoid visible watermarks, platform UI, QR codes, account handles, or brand-owned marks.

## README and Catalog

The Featured and All Styles galleries in all six READMEs, the badge counts, and `docs/CATALOG.md` are generated from `data/catalog.json` plus each `style.json`. Do not edit those sections by hand; CI regenerates them and fails if they differ.

- `styles`: gallery order, newest first. Each entry has `slug`, a short `summary`, and optional `summary_i18n` translations keyed by `zh-CN`, `zh-TW`, `ja`, `ko`, `id`.
- `featured`: exactly six styles. `description` is optional and defaults to the style's `style_summary`.

## Validation

Run this command from the repository root before submitting:

```bash
python3 scripts/validate-style-json.py .
```

## What Not to Include

Do not include original reference images, watermarks, platform identifiers, QR codes, account information, private prompts, or unauthorized brand assets.

## PR Checklist

- [ ] The new folder is under `styles/<slug>/`.
- [ ] The folder contains only `style.json`, `preview-16x9.jpg`, and `preview-9x16.jpg`.
- [ ] The slug is lowercase kebab-case and no longer than 60 characters.
- [ ] The preview images are JPGs and meet the naming requirements.
- [ ] The style is listed in `data/catalog.json` and `python3 scripts/generate-readme.py` has been run.
- [ ] `python3 scripts/validate-style-json.py .` passes.
- [ ] No source references, watermarks, QR codes, account handles, or unauthorized brand assets are included.
