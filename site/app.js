const data = window.COOKBOOK_STYLES || { styles: [], categories: [], styleCount: 0 };

const RESERVED_HASHES = new Set(["", "curator", "featuredTitle", "galleryTitle"]);
const PORTRAIT_RATIOS = new Set(["9:16", "4:5"]);
const LANDSCAPE_RATIOS = new Set(["16:9", "5:4"]);

function categoryFromUrl() {
  try {
    const category = new URLSearchParams(location.search).get("category");
    if (category === "All" || data.categories.includes(category)) return category;
  } catch {
    // Ignore malformed query strings and fall back to All.
  }
  return "All";
}

const state = {
  query: "",
  category: categoryFromUrl(),
};

const detailState = {
  slug: "",
  exampleIndex: 0,
  ratio: "16:9",
};

const searchInput = document.querySelector("#searchInput");
const categoryStrip = document.querySelector("#categoryStrip");
const featuredGrid = document.querySelector("#featuredGrid");
const styleGrid = document.querySelector("#styleGrid");
const resultCount = document.querySelector("#resultCount");
const activeFilter = document.querySelector("#activeFilter");
const emptyState = document.querySelector("#emptyState");
const detailPanel = document.querySelector("#detailPanel");
const detailSheet = document.querySelector(".detail-sheet");
const detailContent = document.querySelector("#detailContent");
const toast = document.querySelector("#toast");
const pullSwitch = document.querySelector("#themePullSwitch");
let isPullAnimating = false;
let ignoreUrlSync = false;

function setTheme(theme) {
  const nextTheme = theme === "light" ? "light" : "dark";
  document.documentElement.dataset.theme = nextTheme;
  try {
    localStorage.setItem("cookbook-theme", nextTheme);
  } catch {
    // The theme still updates for this page load if storage is unavailable.
  }
  if (pullSwitch) {
    const targetTheme = nextTheme === "light" ? "dark" : "light";
    pullSwitch.setAttribute("aria-pressed", String(nextTheme === "light"));
    pullSwitch.setAttribute("aria-label", `Pull to switch to ${targetTheme} theme`);
    pullSwitch.title = `Pull to switch to ${targetTheme} theme`;
  }
}

function toggleThemeWithPull() {
  if (isPullAnimating) return;
  isPullAnimating = true;
  const currentTheme = document.documentElement.dataset.theme === "light" ? "light" : "dark";
  const nextTheme = currentTheme === "light" ? "dark" : "light";
  if (pullSwitch) {
    pullSwitch.classList.add("lamp-pull--pulling");
    window.setTimeout(() => {
      setTheme(nextTheme);
    }, 150);
    window.setTimeout(() => {
      pullSwitch.classList.remove("lamp-pull--pulling");
      pullSwitch.style.removeProperty("--pull-scale");
      pullSwitch.style.removeProperty("--bead-offset");
      isPullAnimating = false;
    }, 400);
    return;
  }
  setTheme(nextTheme);
  isPullAnimating = false;
}

function setupPullSwitch() {
  if (!pullSwitch) return;
  let startY = 0;
  let pullDistance = 0;
  let isDragging = false;
  let suppressClick = false;
  let activePointerId = null;

  function beginPull(clientY) {
    if (isPullAnimating) return false;
    isDragging = true;
    suppressClick = false;
    pullDistance = 0;
    startY = clientY;
    return true;
  }

  function updatePull(clientY) {
    if (!isDragging) return;
    pullDistance = Math.max(0, Math.min(42, clientY - startY));
    if (pullDistance > 2) suppressClick = true;
    pullSwitch.style.setProperty("--pull-scale", String(1 + pullDistance / 80));
    pullSwitch.style.setProperty("--bead-offset", `${pullDistance}px`);
  }

  function finishPull() {
    if (!isDragging) return;
    isDragging = false;
    activePointerId = null;
    const shouldToggle = pullDistance >= 22;
    pullSwitch.style.removeProperty("--pull-scale");
    pullSwitch.style.removeProperty("--bead-offset");
    if (shouldToggle) toggleThemeWithPull();
  }

  pullSwitch.addEventListener("pointerdown", (event) => {
    if (!beginPull(event.clientY)) return;
    activePointerId = event.pointerId;
    pullSwitch.setPointerCapture(event.pointerId);
  });

  pullSwitch.addEventListener("pointermove", (event) => {
    if (activePointerId !== event.pointerId) return;
    updatePull(event.clientY);
  });

  pullSwitch.addEventListener("pointerup", finishPull);
  pullSwitch.addEventListener("pointercancel", finishPull);

  pullSwitch.addEventListener("mousedown", (event) => {
    if (activePointerId !== null || event.button !== 0) return;
    beginPull(event.clientY);
  });

  document.addEventListener("mousemove", (event) => {
    if (activePointerId !== null) return;
    updatePull(event.clientY);
  });

  document.addEventListener("mouseup", () => {
    if (activePointerId !== null) return;
    finishPull();
  });

  pullSwitch.addEventListener(
    "touchstart",
    (event) => {
      if (activePointerId !== null || event.touches.length === 0) return;
      beginPull(event.touches[0].clientY);
    },
    { passive: true },
  );

  pullSwitch.addEventListener(
    "touchmove",
    (event) => {
      if (activePointerId !== null || event.touches.length === 0) return;
      updatePull(event.touches[0].clientY);
    },
    { passive: true },
  );

  pullSwitch.addEventListener("touchend", () => {
    if (activePointerId !== null) return;
    finishPull();
  });

  pullSwitch.addEventListener("click", (event) => {
    event.stopPropagation();
    if (suppressClick) {
      suppressClick = false;
      return;
    }
    toggleThemeWithPull();
  });
}

function textIncludes(style, query) {
  if (!query) return true;
  const haystack = [
    style.name,
    style.slug,
    style.category,
    style.description,
    style.summary,
    style.anchors.join(" "),
    style.variables.join(" "),
  ]
    .join(" ")
    .toLowerCase();
  return haystack.includes(query.toLowerCase());
}

function visibleStyles() {
  return data.styles.filter((style) => {
    const categoryMatch = state.category === "All" || style.category === state.category;
    return categoryMatch && textIncludes(style, state.query.trim());
  });
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function labelFor(key) {
  return key
    .toLowerCase()
    .split("_")
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(" ");
}

function findStyle(slug) {
  return data.styles.find((style) => style.slug === slug);
}

function hydrate(style) {
  if (!style || style.hydrated) return style;
  const parsed = JSON.parse(style.jsonText);
  const examples = Array.isArray(parsed.examples) ? parsed.examples : [];
  style.promptTemplate = typeof parsed.prompt_template === "string" ? parsed.prompt_template : "";
  style.env = parsed.environment_variables && typeof parsed.environment_variables === "object"
    ? parsed.environment_variables
    : {};
  style.examples = examples.map((item, index) => {
    const values = item && typeof item.values === "object" && item.values ? item.values : {};
    const cleanValues = {};
    for (const [key, value] of Object.entries(values)) {
      if (typeof value === "string") cleanValues[key] = value;
    }
    return {
      name: typeof item?.case_name === "string" && item.case_name.trim()
        ? item.case_name.trim()
        : `Example ${index + 1}`,
      values: cleanValues,
    };
  });
  if (!style.examples.length) {
    style.examples = [{ name: "Custom example", values: {} }];
  }
  style.fidelityAnchors = Array.isArray(parsed.style_fidelity_anchors)
    ? parsed.style_fidelity_anchors.filter((item) => typeof item === "string")
    : style.anchors || [];
  style.sourceAvoid = Array.isArray(parsed.source_content_to_avoid)
    ? parsed.source_content_to_avoid.filter((item) => typeof item === "string")
    : [];
  style.negativePrompt = typeof parsed.negative_prompt === "string" ? parsed.negative_prompt : "";
  style.hydrated = true;
  return style;
}

function defaultRatio(style) {
  const ratios = style.aspectRatios || [];
  for (const ratio of ["16:9", "9:16", "4:5", "5:4"]) {
    if (ratios.includes(ratio)) return ratio;
  }
  return ratios[0] || "16:9";
}

function exampleAt(style, index) {
  hydrate(style);
  const examples = style.examples;
  return examples[Math.max(0, Math.min(index, examples.length - 1))];
}

function fillValues(style, example, ratio) {
  hydrate(style);
  const values = { ...(example?.values || {}) };
  values.ASPECT_RATIO = ratio;
  if (!values.STYLE_FIDELITY_ANCHORS && style.fidelityAnchors.length) {
    values.STYLE_FIDELITY_ANCHORS = style.fidelityAnchors.join(" ");
  }
  if (!values.SOURCE_CONTENT_TO_AVOID && style.sourceAvoid.length) {
    values.SOURCE_CONTENT_TO_AVOID = style.sourceAvoid.join("; ");
  }
  if (!values.NEGATIVE_PROMPT && style.negativePrompt) {
    values.NEGATIVE_PROMPT = style.negativePrompt;
  }
  return values;
}

function filledPrompt(style, example, ratio) {
  hydrate(style);
  const values = fillValues(style, example, ratio);
  const template = style.promptTemplate;
  if (!template) return shortCopyPrompt(style, example, ratio);
  return template.replace(/\{([A-Z][A-Z0-9_]*)\}/g, (match, key) => {
    if (!Object.prototype.hasOwnProperty.call(values, key)) return match;
    const value = values[key];
    return value === undefined || value === null || value === "" ? match : String(value);
  });
}

function shortCopyPrompt(style, example, ratio) {
  hydrate(style);
  const values = fillValues(style, example, ratio);
  const skip = new Set(["STYLE_FIDELITY_ANCHORS", "SOURCE_CONTENT_TO_AVOID", "NEGATIVE_PROMPT"]);
  const keys = [];
  for (const key of style.variables || []) {
    if (!skip.has(key) && values[key]) keys.push(key);
  }
  for (const key of Object.keys(values)) {
    if (!skip.has(key) && values[key] && !keys.includes(key)) keys.push(key);
  }

  const lines = [
    `Use the "${style.name}" visual style as the locked visual system.`,
    "",
    `Create a ${ratio} image.`,
    "",
  ];
  for (const key of keys) {
    lines.push(`${labelFor(key)}: ${values[key]}`);
  }
  if (style.summary) {
    lines.push("", "Style direction:", style.summary);
  }
  const anchors = (style.anchors || []).slice(0, 5);
  if (anchors.length) {
    lines.push("", "Keep visible:");
    for (const anchor of anchors) lines.push(`- ${anchor}`);
  }
  if (style.negativePrompt) {
    lines.push("", "Avoid:", style.negativePrompt);
  }
  lines.push(
    "",
    "Do not copy source content, real logos, watermarks, platform UI, QR codes, or exact",
    "reference layouts. Keep the visual system, but change the subject, text, and scene.",
  );
  return lines.join("\n").trim();
}

function selectionFor(slug) {
  const style = hydrate(findStyle(slug));
  if (!style) return null;
  if (detailState.slug === slug) {
    return {
      style,
      example: exampleAt(style, detailState.exampleIndex),
      ratio: detailState.ratio,
    };
  }
  return {
    style,
    example: exampleAt(style, 0),
    ratio: defaultRatio(style),
  };
}

function cardTemplate(style, featured = false) {
  const cardClass = featured ? "style-card featured" : "style-card";
  return `
    <article class="${cardClass}" data-slug="${escapeHtml(style.slug)}">
      <button class="preview-button" type="button" data-open-detail="${escapeHtml(style.slug)}">
        <img src="${escapeHtml(style.preview16)}" alt="${escapeHtml(style.name)} preview" loading="lazy">
      </button>
      <div class="card-body">
        <span class="category-label">${escapeHtml(style.category)}</span>
        <h3>${escapeHtml(style.name)}</h3>
        <p class="card-description">${escapeHtml(style.description)}</p>
        <div class="card-actions">
          <button class="action-button primary" type="button" data-copy-json="${escapeHtml(style.slug)}" title="Copy the full style.json for ChatGPT, Gemini, or Claude">Copy JSON</button>
          <button class="action-button" type="button" data-open-detail="${escapeHtml(style.slug)}">Details</button>
          <button class="action-button" type="button" data-copy-prompt="${escapeHtml(style.slug)}" title="Short chat paste">Copy Prompt</button>
        </div>
      </div>
    </article>
  `;
}

function renderCategories() {
  const categories = ["All", ...data.categories];
  categoryStrip.innerHTML = categories
    .map((category) => {
      const active = category === state.category ? " is-active" : "";
      return `<button class="category-button${active}" type="button" data-category="${escapeHtml(category)}">${escapeHtml(category)}</button>`;
    })
    .join("");
}

function renderFeatured() {
  featuredGrid.innerHTML = data.styles.slice(0, 6).map((style) => cardTemplate(style, true)).join("");
}

function renderGrid() {
  const styles = visibleStyles();
  styleGrid.innerHTML = styles.map((style) => cardTemplate(style)).join("");
  resultCount.textContent = `${styles.length} of ${data.styleCount} styles`;
  activeFilter.textContent = state.category === "All" ? "All categories" : state.category;
  emptyState.hidden = styles.length > 0;
}

function choiceButtons(items, selected, attrName) {
  return items
    .map((item, index) => {
      const value = typeof item === "string" ? item : String(index);
      const label = typeof item === "string" ? item : item.name;
      const active = value === String(selected) ? " is-active" : "";
      return `<button class="choice-button${active}" type="button" data-${attrName}="${escapeHtml(value)}" aria-pressed="${active ? "true" : "false"}">${escapeHtml(label)}</button>`;
    })
    .join("");
}

function variableRows(style, values) {
  const keys = [...(style.variables || [])];
  for (const key of Object.keys(values)) {
    if (!keys.includes(key)) keys.push(key);
  }
  if (!keys.length) return `<p class="empty-note">No variables declared.</p>`;
  return `
    <dl class="variable-table">
      ${keys
        .map((key) => {
          const description = typeof style.env[key] === "string" ? style.env[key] : "";
          const value = values[key];
          const valueHtml = value
            ? escapeHtml(value)
            : `<span class="empty-value">not in this example</span>`;
          return `
            <div class="variable-row">
              <dt>
                <code>${escapeHtml(key)}</code>
                ${description ? `<span>${escapeHtml(description)}</span>` : ""}
              </dt>
              <dd>${valueHtml}</dd>
            </div>
          `;
        })
        .join("")}
    </dl>
  `;
}

function detailTemplate(style) {
  hydrate(style);
  const example = exampleAt(style, detailState.exampleIndex);
  const ratio = detailState.ratio;
  const values = fillValues(style, example, ratio);
  const landscapeOn = LANDSCAPE_RATIOS.has(ratio);
  const portraitOn = PORTRAIT_RATIOS.has(ratio);
  const landscapeCaption = ratio === "5:4" ? "16:9 preview · stand-in for 5:4" : "16:9";
  const portraitCaption = ratio === "4:5" ? "9:16 preview · stand-in for 4:5" : "9:16";
  const filled = filledPrompt(style, example, ratio);

  return `
    <div class="detail-content">
      <span class="category-label">${escapeHtml(style.category)}</span>
      <h2>${escapeHtml(style.name)}</h2>
      <p>${escapeHtml(style.summary || style.description)}</p>
      <p class="copy-legend">Copy JSON for ChatGPT / Gemini / Claude workflows. Copy filled prompt to paste <code>prompt_template</code> with this example and ratio. Copy Prompt is a short chat paste.</p>

      <div class="detail-controls">
        <div class="control-block">
          <h3>Example case</h3>
          <div class="choice-strip" role="group" aria-label="Example case">
            ${choiceButtons(style.examples, detailState.exampleIndex, "example-index")}
          </div>
        </div>
        <div class="control-block">
          <h3>Aspect ratio</h3>
          <div class="choice-strip" role="group" aria-label="Aspect ratio">
            ${choiceButtons(style.aspectRatios, ratio, "aspect-ratio")}
          </div>
        </div>
      </div>

      <div class="detail-images">
        <figure class="preview-frame${landscapeOn ? " is-emphasized" : ""}">
          <img src="${escapeHtml(style.preview16)}" alt="${escapeHtml(style.name)} 16:9 preview">
          <figcaption>${escapeHtml(landscapeCaption)}</figcaption>
        </figure>
        <figure class="preview-frame preview-frame--portrait${portraitOn ? " is-emphasized" : ""}">
          <img src="${escapeHtml(style.preview9)}" alt="${escapeHtml(style.name)} 9:16 preview">
          <figcaption>${escapeHtml(portraitCaption)}</figcaption>
        </figure>
      </div>

      <h3>Style Anchors</h3>
      <ul class="anchor-list">
        ${style.anchors.map((anchor) => `<li>${escapeHtml(anchor)}</li>`).join("")}
      </ul>

      <h3>Variables</h3>
      ${variableRows(style, values)}

      <h3>Filled prompt</h3>
      <pre class="filled-prompt" id="filledPromptPreview">${escapeHtml(filled)}</pre>

      <div class="detail-actions">
        <button class="action-button primary" type="button" data-copy-json="${escapeHtml(style.slug)}">Copy JSON</button>
        <button class="action-button" type="button" data-copy-filled="${escapeHtml(style.slug)}">Copy filled prompt</button>
        <button class="action-button" type="button" data-copy-prompt="${escapeHtml(style.slug)}">Copy Prompt</button>
        <a class="card-link" href="${escapeHtml(style.styleJson)}">Open style.json</a>
        <a class="card-link" href="styles/${escapeHtml(style.slug)}/">Style page</a>
        <a class="card-link" href="${escapeHtml(style.copyPromptDoc)}">Prompt doc</a>
        <a class="card-link" href="${escapeHtml(style.folder)}">Folder</a>
      </div>
    </div>
  `;
}

function hashFragment() {
  try {
    return decodeURIComponent(location.hash.replace(/^#/, ""));
  } catch {
    return null;
  }
}

function slugFromUrl() {
  const params = new URLSearchParams(location.search);
  const querySlug = params.get("style");
  if (querySlug && findStyle(querySlug)) return querySlug;
  const hash = hashFragment();
  if (hash === null || RESERVED_HASHES.has(hash)) return null;
  const fromPrefix = hash.startsWith("style/") ? hash.slice(6) : hash;
  return findStyle(fromPrefix) ? fromPrefix : null;
}

function writeStyleUrl(slug, replace = false) {
  const url = new URL(location.href);
  url.searchParams.delete("style");
  url.hash = slug ? encodeURIComponent(slug) : "";
  ignoreUrlSync = true;
  history[replace ? "replaceState" : "pushState"]({ style: slug || "" }, "", url);
  window.setTimeout(() => {
    ignoreUrlSync = false;
  }, 0);
}

function syncCategoryUrl() {
  const url = new URL(location.href);
  if (state.category === "All") url.searchParams.delete("category");
  else url.searchParams.set("category", state.category);
  ignoreUrlSync = true;
  history.replaceState(history.state, "", url);
  window.setTimeout(() => {
    ignoreUrlSync = false;
  }, 0);
}

function setDetailOpen(open) {
  detailPanel.classList.toggle("is-open", open);
  detailPanel.setAttribute("aria-hidden", open ? "false" : "true");
  document.body.classList.toggle("detail-open", open);
}

function renderDetail() {
  const style = findStyle(detailState.slug);
  if (!style) return;
  const scroll = detailSheet ? detailSheet.scrollTop : 0;
  detailContent.innerHTML = detailTemplate(style);
  if (detailSheet) detailSheet.scrollTop = scroll;
}

function openDetail(slug, options = {}) {
  const style = findStyle(slug);
  if (!style) return;
  hydrate(style);
  const sameStyle = detailState.slug === slug && detailPanel.classList.contains("is-open");
  detailState.slug = slug;
  if (!sameStyle) {
    detailState.exampleIndex = 0;
    detailState.ratio = defaultRatio(style);
  }
  if (style.aspectRatios.length && !style.aspectRatios.includes(detailState.ratio)) {
    detailState.ratio = defaultRatio(style);
  }
  renderDetail();
  setDetailOpen(true);
  if (!options.fromUrl) writeStyleUrl(slug, options.replace);
}

function closeDetail(options = {}) {
  setDetailOpen(false);
  detailState.slug = "";
  if (!options.fromUrl) writeStyleUrl("", options.replace);
}

function showToast(message) {
  toast.textContent = message;
  toast.classList.add("is-visible");
  window.clearTimeout(showToast.timer);
  showToast.timer = window.setTimeout(() => {
    toast.classList.remove("is-visible");
  }, 2600);
}

function fallbackCopy(text) {
  const area = document.createElement("textarea");
  area.value = text;
  area.setAttribute("readonly", "");
  area.style.position = "fixed";
  area.style.opacity = "0";
  document.body.append(area);
  try {
    area.select();
    return document.execCommand("copy");
  } finally {
    area.remove();
  }
}

async function copyText(text, message) {
  let copied = false;
  if (navigator.clipboard && window.isSecureContext) {
    try {
      await Promise.race([
        navigator.clipboard.writeText(text),
        new Promise((_, reject) => {
          window.setTimeout(() => reject(new Error("clipboard timeout")), 400);
        }),
      ]);
      copied = true;
    } catch {
      copied = false;
    }
  }
  if (!copied) {
    try {
      copied = fallbackCopy(text);
    } catch {
      copied = false;
    }
  }
  showToast(copied ? message : "Copy failed. Please copy the text manually.");
}

async function copyJson(slug) {
  const style = findStyle(slug);
  if (!style) return;
  await copyText(style.jsonText, `Copied ${style.name} style.json`);
}

async function copyFilled(slug) {
  const selection = selectionFor(slug);
  if (!selection) return;
  await copyText(
    filledPrompt(selection.style, selection.example, selection.ratio),
    `Copied filled ${selection.ratio} prompt`,
  );
}

async function copyPrompt(slug) {
  const selection = selectionFor(slug);
  if (!selection) return;
  await copyText(
    shortCopyPrompt(selection.style, selection.example, selection.ratio),
    `Copied short prompt for ${selection.style.name}`,
  );
}

function syncDetailFromUrl() {
  if (ignoreUrlSync) return;
  const slug = slugFromUrl();
  if (slug) {
    openDetail(slug, { fromUrl: true });
    const params = new URLSearchParams(location.search);
    const hash = hashFragment();
    if (params.has("style") || (hash && hash.startsWith("style/"))) {
      writeStyleUrl(slug, true);
    }
  } else if (detailPanel.classList.contains("is-open")) {
    closeDetail({ fromUrl: true });
  }
}

document.addEventListener("click", (event) => {
  const categoryButton = event.target.closest("[data-category]");
  if (categoryButton) {
    state.category = categoryButton.dataset.category;
    syncCategoryUrl();
    renderCategories();
    renderGrid();
    return;
  }

  const exampleButton = event.target.closest("[data-example-index]");
  if (exampleButton && detailState.slug) {
    detailState.exampleIndex = Number(exampleButton.dataset.exampleIndex);
    renderDetail();
    return;
  }

  const ratioButton = event.target.closest("[data-aspect-ratio]");
  if (ratioButton && detailState.slug) {
    detailState.ratio = ratioButton.dataset.aspectRatio;
    renderDetail();
    return;
  }

  const detailButton = event.target.closest("[data-open-detail]");
  if (detailButton) {
    openDetail(detailButton.dataset.openDetail);
    return;
  }

  const jsonButton = event.target.closest("[data-copy-json]");
  if (jsonButton) {
    copyJson(jsonButton.dataset.copyJson);
    return;
  }

  const filledButton = event.target.closest("[data-copy-filled]");
  if (filledButton) {
    copyFilled(filledButton.dataset.copyFilled);
    return;
  }

  const copyButton = event.target.closest("[data-copy-prompt]");
  if (copyButton) {
    copyPrompt(copyButton.dataset.copyPrompt);
    return;
  }

  if (event.target.closest("[data-close-detail]")) {
    closeDetail();
  }
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") closeDetail();
});

window.addEventListener("hashchange", syncDetailFromUrl);
window.addEventListener("popstate", syncDetailFromUrl);

searchInput.addEventListener("input", () => {
  state.query = searchInput.value;
  renderGrid();
});

setupPullSwitch();
setTheme(document.documentElement.dataset.theme);
renderCategories();
renderFeatured();
renderGrid();
syncDetailFromUrl();
