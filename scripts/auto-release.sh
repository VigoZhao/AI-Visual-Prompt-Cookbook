#!/usr/bin/env bash
#
# auto-release.sh — cut a dated, source-only GitHub release for every style
# added since the previous release.
#
# Run by .github/workflows/release.yml after the Validate workflow succeeds on
# main, so a release is created automatically no matter who pushed the style
# (a local publish, another session, or an automated flow). Keying off "styles
# added since the last release" — rather than the contents of a single push —
# makes it self-healing (it catches styles from pushes that never got a
# release) and idempotent (nothing new since the last release ⇒ no-op).
#
# Usage:
#   scripts/auto-release.sh                 # real run (needs gh auth / GH_TOKEN)
#   scripts/auto-release.sh --dry-run       # print tag/title/notes, create nothing
#   scripts/auto-release.sh --since <ref>   # override "last release" (testing)
#   scripts/auto-release.sh --head  <ref>   # override HEAD (testing; default HEAD)
#
set -euo pipefail

DRY_RUN=0
SINCE_OVERRIDE=""
HEAD_REF="HEAD"
while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run) DRY_RUN=1 ;;
    --since)   SINCE_OVERRIDE="${2:-}"; shift ;;
    --head)    HEAD_REF="${2:-}"; shift ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
  shift
done

HEAD_SHA=$(git rev-parse "$HEAD_REF")

# --- Determine the previous release's tag ---------------------------------
# Resolve the nearest release tag reachable from HEAD (topologically the
# previous release on main) from git alone — no gh/network call. So a transient
# API failure can never be mistaken for "first release", a draft release's
# phantom tag can't hijack it, and it is naturally idempotent: if HEAD is
# already tagged, the tag resolves to HEAD and the diff below is empty (no-op).
if [ -n "$SINCE_OVERRIDE" ]; then
  LAST_TAG="$SINCE_OVERRIDE"
else
  LAST_TAG=$(git describe --tags --abbrev=0 --match 'v[0-9]*' "$HEAD_SHA" 2>/dev/null || true)
fi

# A non-empty tag MUST resolve to a commit. Empty = genuine first release; a
# set-but-unresolvable tag (bad --since, or a stale/draft ref) is an error, not
# a cue to re-release every style. Checked here in the main shell so `exit`
# actually aborts (an exit inside the process substitution below would not).
if [ -n "$LAST_TAG" ] && ! git rev-parse -q --verify "refs/tags/${LAST_TAG}^{commit}" >/dev/null 2>&1; then
  echo "previous release tag '${LAST_TAG}' does not resolve to a commit; aborting" >&2
  exit 1
fi

# --- Collect style.json files added since that tag ------------------------
# A new style folder always introduces a styles/<slug>/style.json, so the set of
# Added style.json files is exactly the set of newly published styles. Rename
# detection is disabled (--no-renames) so a new style is never reclassified as a
# rename of a concurrently-removed style — which --diff-filter=A would drop,
# silently missing the release.
added_paths() {
  if [ -z "$LAST_TAG" ]; then
    # No release tag reachable from HEAD: first release ever — every style is new.
    git ls-tree -r --name-only "$HEAD_SHA" -- styles
  else
    git diff --no-renames --name-status --diff-filter=A "$LAST_TAG" "$HEAD_SHA" -- styles \
      | awk '$1 ~ /^A/ {print $2}'
  fi | grep -E '^styles/[^/]+/style\.json$' | sort || true
}

ADDED=()
while IFS= read -r line; do
  [ -n "$line" ] && ADDED+=("$line")
done < <(added_paths)

if [ "${#ADDED[@]}" -eq 0 ]; then
  echo "No new styles since ${LAST_TAG:-<none>} (HEAD ${HEAD_SHA:0:7}); nothing to release."
  exit 0
fi

# --- Build the release notes ----------------------------------------------
TOTAL=$(git ls-tree -d --name-only "$HEAD_SHA" styles/ | wc -l | tr -d ' ')
PREVIEWS=$((TOTAL * 2))
N=${#ADDED[@]}
case "$N" in
  1) COUNT_WORD="One" ;;
  2) COUNT_WORD="Two" ;;
  3) COUNT_WORD="Three" ;;
  *) COUNT_WORD="$N" ;;
esac
NOUN="style"; [ "$N" -gt 1 ] && NOUN="styles"

bullets=""
for f in "${ADDED[@]}"; do
  slug=$(basename "$(dirname "$f")")
  name=$(git show "$HEAD_SHA:$f" | python3 -c "import json,sys;print(json.load(sys.stdin)['style_name'])")
  bullets+="- **${name}** — \`styles/${slug}/\`"$'\n'
done

NOTES="${COUNT_WORD} new visual ${NOUN}:

${bullets}
The library now includes ${TOTAL} styles and ${PREVIEWS} preview images. All six READMEs, \`docs/CATALOG.md\`, the copy-prompt library, gallery thumbnails, and the GitHub Pages data were refreshed."

# --- Pick a fresh, non-colliding dated tag --------------------------------
BASE="v$(date +%Y.%m.%d)"   # honors $TZ (workflow sets Asia/Shanghai to match prior tags)
TAG="$BASE"; i=1
while gh release view "$TAG" >/dev/null 2>&1 || git rev-parse -q --verify "refs/tags/${TAG}" >/dev/null 2>&1; do
  i=$((i + 1)); TAG="${BASE}-${i}"
done
TITLE="${TAG#v} Style Drop"

# --- Create (or preview) the release --------------------------------------
echo "Tag:   $TAG"
echo "Title: $TITLE"
echo "Target commit: $HEAD_SHA"
echo "New styles ($N):"; printf '  %s\n' "${ADDED[@]}"
echo "----- notes -----"
printf '%s\n' "$NOTES"
echo "-----------------"

if [ "$DRY_RUN" -eq 1 ]; then
  echo "[dry-run] no release created."
  exit 0
fi

gh release create "$TAG" --target "$HEAD_SHA" --title "$TITLE" --notes "$NOTES"
echo "Created release $TAG at ${HEAD_SHA:0:7}."
