# Handoff — Publishing styles to AI Visual Prompt Cookbook

A one-page mental model for whoever (a person, Cursor, another agent) takes over the "add a new visual style and publish it" job. For the exact command-by-command runbook, see **`AGENTS.md`** at the repo root. This doc is the *why* and the *gotchas*; `AGENTS.md` is the *how*.

> **The one rule that matters most:** the GitHub Release is cut **automatically by CI**. Never run `gh release create` or make a release in the web UI — you only ever **commit + push**, then verify. (See "How releases work" below.)

## What the task is

Someone hands you a **style package folder** (under `Save_prompt/…`) containing `style-spec.json`, a `README.md`, and 8 preview PNGs (4 subjects × 2 orientations). You:

1. Add it to the library as `styles/<slug>/` (one `style.json` + two preview JPGs).
2. Regenerate the derived files (thumbnail, copy-prompt, Pages data).
3. Hand-edit the six READMEs + the catalog so the new style is listed (this is the real work — scripts don't do it).
4. Commit and push to `main`.
5. **Verify** the automatic release appeared. Done.

## Current state (as of this handoff)

- **120 styles / 240 previews.** Counts live in the `styles-`/`previews-` badges at the top of every README (previews = 2 × styles).
- Branch `main`, latest commit `def5745`. Latest release `v2026.08.24`.
- Author email for commits: `128469840+VigoZhao@users.noreply.github.com`.
- Origin: `git@github.com:VigoZhao/AI-Visual-Prompt-Cookbook.git`.
- Release automation is **live** (added Aug 2026) and self-healing.

## How releases work (the important mental model)

```
push to main ──▶ [Validate workflow] ──success──▶ [Release workflow]
                  validate.yml                     release.yml (workflow_run)
                                                        │
                                                        ▼
                                                  scripts/auto-release.sh
                                                        │
                        "which styles were added since the last release?"
                        (git describe → previous tag; git diff --no-renames -A)
                                                        │
                              ≥1 new ──▶ cut ONE dated source-only release
                              0 new  ──▶ no-op (nothing to release)
```

Consequences you must internalize:

- **Do not cut releases manually.** CI does it. A manual release races the workflow and can duplicate.
- It keys off *"styles added since the last release,"* not *"this push"* — so it is **self-healing** (if several pushes pile up with no release, the next run bundles them all) and **idempotent** (a push with no new style is a harmless no-op).
- Releases are **source-only** — never attach preview images or any binary.
- Tag is `vYYYY.MM.DD` (Asia/Shanghai date), with `-2`, `-3` suffixes if two land the same day.
- After pushing, confirm with `gh release list` (or the repo's Releases page). If the Release workflow *failed* to produce a release, read its logs and fix the cause — don't paper over it with a manual release.

## The procedure, in brief

Full commands are in `AGENTS.md`. The shape:

1. **Preconditions** — on `main`, clean tree, `git fetch`, and confirm the slug isn't already published (`git cat-file -e origin/main:styles/<slug>/style.json` must fail). Read current count `N` from the README badge.
2. **Package** — `styles/<slug>/` gets `style.json` (copied from `style-spec.json`) + `preview-16x9.jpg` + `preview-9x16.jpg`. The folder must contain **exactly** those three files.
3. **Derived files** — `scripts/generate-thumbnails.py` (thumbnail), `scripts/generate-copy-prompts.py .` (copy-prompt), and later `scripts/build-pages-mvp.py` (Pages data). Then `scripts/validate-style-json.py .` must PASS.
4. **Hand-edit 6 READMEs + `docs/CATALOG.md`** — badges, count sentences, the **Featured** grid (newest first, drop the oldest to stay at 6), and the **All Styles** gallery (newest first, rows of 3). `AGENTS.md` ships a small, tested Python reflow script for this — use it.
5. **Commit + push** — never stage `.DS_Store`. Then verify the release.

## Gotchas / lessons learned (these bit us before)

- **Releases used to be skipped.** The whole automation exists because earlier sessions/flows committed styles but forgot the manual release step, leaving styles pushed-but-unreleased. That's why it's now server-side. → Trust the automation; don't reintroduce a manual release.
- **Preview aspect ratios vary.** Sources come as `*-5x4.png`/`*-4x5.png` *or* `*-16x9.png`/`*-9x16.png`. Either way: **landscape → `preview-16x9.jpg`, portrait → `preview-9x16.jpg`.** Default to the first sorted subject (`01-…`) unless told otherwise. (Note: when the source is 5:4/4:5, the README's "16:9 / 9:16" link text is not literally exact, but that's the established convention — the slots are named `preview-16x9`/`preview-9x16` regardless.)
- **Names & descriptions stay English in all six READMEs.** Only the Featured action line (`Open style.json · Copy Prompt · Folder`) and the count sentences are localized. All Styles cells are identical English across all languages.
- **Featured header is translated** in the five localized READMEs — locate the grid as the first `<table>`, not by grepping `## Featured Styles` (that string is English-only in `README.md`).
- **Never commit `.DS_Store`** (macOS litters these; two sit untracked in the tree — leave them).
- **Dedup before you start.** Some handed-over paths were already published in a prior drop — always run the not-already-published check first and skip duplicates.
- **`generate-thumbnails.py` is macOS-only** (`sips`). On a non-mac agent it crashes; use the Pillow fallback in `AGENTS.md` (must downscale to 640px wide at quality 72 — Validate only checks the thumb *exists*, so a full-res thumb would silently ship).

## File & tooling map

| Thing | Where |
|---|---|
| Style packages | `styles/<slug>/{style.json,preview-16x9.jpg,preview-9x16.jpg}` |
| Gallery thumbs | `assets/thumbs/<slug>-16x9.jpg` (generated) |
| Copy-prompts | `docs/copy-prompts/<slug>.md` (generated) |
| Catalog | `docs/CATALOG.md` (hand-edited) |
| Homepages | `README.md` + `README.{zh-CN,zh-TW,ja,ko,id}.md` (hand-edited) |
| Pages data | `site/styles-data.js` (generated from README order) |
| Scripts | `scripts/{generate-thumbnails,generate-copy-prompts,build-pages-mvp,validate-style-json}.py`, `scripts/auto-release.sh` |
| CI | `.github/workflows/validate.yml`, `.github/workflows/release.yml` |
| Agent runbook | `AGENTS.md` (repo root) |
| Schema | `schemas/style-v2.1.schema.json` |

## Using this with Cursor

Cursor reads repo files as context. Two caveats:

1. **`AGENTS.md` is currently local-only** — it's excluded via `.git/info/exclude` and is **not on GitHub**. Cursor sees it only if it's working on this exact local checkout. If Cursor works from a fresh clone or a cloud environment, it will not have `AGENTS.md` — commit `AGENTS.md` (and this file) to the repo, or paste the runbook into Cursor, so it actually has the instructions.
2. Then a single instruction suffices, e.g.:
   > *Follow `AGENTS.md`: add the style package at `Save_prompt/<folder>` and push. Default to the `01-` subject for previews. Do not cut a release — CI does it automatically; just confirm it appears afterward.*

Everything else — the reflow, the counts, the release — follows from `AGENTS.md`.
