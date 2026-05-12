# Interactive Snippets

Append these `<script>` blocks just before `</body>`. Every snippet is plain vanilla JS — no external library.

> Default to no interactivity. Only add it when the doc is long (≥3 sections) or is itself interaction-shaped (tutorial / decision / vendor selection).

---

## 1) Section collapse

Make every `<section>`'s `<h2>` clickable to collapse the section body.

**HTML change:** add `class="collapsible"` to the `section`.

**CSS** (append to the existing `<style>`):
```css
section.collapsible h2 { cursor: pointer; position: relative; padding-right: 28px; }
section.collapsible h2::after {
  content: "−";
  position: absolute; right: 8px; top: 0;
  font-family: ui-monospace, Menlo, monospace;
  color: var(--ink-faint);
}
section.collapsible.collapsed h2::after { content: "+"; }
section.collapsible.collapsed > *:not(h2) { display: none; }
```

**JS:**
```html
<script>
  document.querySelectorAll("section.collapsible h2").forEach(h => {
    h.addEventListener("click", () => h.parentElement.classList.toggle("collapsed"));
  });
</script>
```

---

## 2) Copy button on code blocks

```css
pre { position: relative; }
.copy-btn {
  position: absolute; top: 8px; right: 8px;
  font-family: ui-monospace, Menlo, monospace; font-size: 10px;
  letter-spacing: 0.1em; text-transform: uppercase;
  background: #fff; border: 1px solid var(--rule);
  padding: 4px 8px; cursor: pointer; color: var(--ink-faint);
}
.copy-btn:hover { color: var(--ink); }
```

```html
<script>
  document.querySelectorAll("pre").forEach(pre => {
    const btn = document.createElement("button");
    btn.className = "copy-btn";
    btn.textContent = "copy";
    btn.onclick = async () => {
      await navigator.clipboard.writeText(pre.innerText);
      btn.textContent = "copied";
      setTimeout(() => (btn.textContent = "copy"), 1500);
    };
    pre.appendChild(btn);
  });
</script>
```

---

## 3) Table filter + sort

Give the table an id: `<table id="vendors">`.

```html
<input type="text" id="vendors-filter" placeholder="filter…" style="max-width: 220px; margin-bottom: 12px;" />
<script>
  (function () {
    const t = document.getElementById("vendors");
    const input = document.getElementById("vendors-filter");
    if (!t || !input) return;
    const rows = [...t.tBodies[0].rows];

    input.addEventListener("input", e => {
      const q = e.target.value.toLowerCase();
      rows.forEach(r => {
        r.style.display = r.innerText.toLowerCase().includes(q) ? "" : "none";
      });
    });

    // sortable headers
    t.tHead.querySelectorAll("th").forEach((th, i) => {
      th.style.cursor = "pointer";
      let asc = true;
      th.addEventListener("click", () => {
        rows.sort((a, b) => {
          const av = a.cells[i].innerText.trim();
          const bv = b.cells[i].innerText.trim();
          const an = parseFloat(av), bn = parseFloat(bv);
          if (!isNaN(an) && !isNaN(bn)) return asc ? an - bn : bn - an;
          return asc ? av.localeCompare(bv) : bv.localeCompare(av);
        });
        asc = !asc;
        const tbody = t.tBodies[0];
        rows.forEach(r => tbody.appendChild(r));
      });
    });
  })();
</script>
```

---

## 4) TOC + scrollspy

Fixed left-side table of contents, auto-highlights the current section.

**CSS:**
```css
.toc {
  position: fixed; top: 64px; left: 24px;
  width: 200px;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 11px; line-height: 1.8;
}
.toc a { display: block; color: var(--ink-faint); border: none; }
.toc a.active { color: var(--accent); font-weight: 600; }
@media (max-width: 1180px) { .toc { display: none; } }
```

**HTML** (right after `<body>`):
```html
<nav class="toc" id="toc"></nav>
```

**JS:**
```html
<script>
  (function () {
    const toc = document.getElementById("toc");
    if (!toc) return;
    const sections = [...document.querySelectorAll("section > h2")];
    sections.forEach((h, i) => {
      const id = h.id || `sec-${i + 1}`;
      h.id = id;
      const a = document.createElement("a");
      a.href = `#${id}`;
      a.textContent = h.textContent.replace(/^\s*\d+\s*/, "");
      toc.appendChild(a);
    });
    const links = [...toc.querySelectorAll("a")];
    const obs = new IntersectionObserver(
      entries => {
        entries.forEach(e => {
          if (e.isIntersecting) {
            links.forEach(a => a.classList.toggle("active", a.getAttribute("href") === `#${e.target.id}`));
          }
        });
      },
      { rootMargin: "-40% 0px -50% 0px" }
    );
    sections.forEach(s => obs.observe(s));
  })();
</script>
```

---

## 5) Dark mode toggle (persisted)

**CSS** (append to the existing `<style>`):
```css
html.dark {
  --paper: #1a1a1a;
  --paper-edge: #222;
  --ink: #e8e8e2;
  --ink-soft: #b8b8b2;
  --ink-faint: #888;
  --rule: #333;
  --rule-soft: #2a2a2a;
  --code-bg: #262624;
  --accent-faint: #1c2a35;
  --warn-soft: #2c2418;
}
html.dark .callout, html.dark .card, html.dark figure { background: #1f1f1f; }
html.dark figcaption { background: #181818; }

.theme-toggle {
  position: fixed; top: 16px; right: 16px;
  font-family: ui-monospace, Menlo, monospace; font-size: 10px;
  letter-spacing: 0.1em; text-transform: uppercase;
  background: var(--paper-edge); color: var(--ink-faint);
  border: 1px solid var(--rule);
  padding: 6px 10px; cursor: pointer; z-index: 10;
}
```

**HTML:**
```html
<button class="theme-toggle" id="theme-toggle">dark</button>
```

**JS:**
```html
<script>
  (function () {
    const btn = document.getElementById("theme-toggle");
    const apply = mode => {
      document.documentElement.classList.toggle("dark", mode === "dark");
      btn.textContent = mode === "dark" ? "light" : "dark";
    };
    apply(localStorage.getItem("theme") || "light");
    btn.addEventListener("click", () => {
      const next = document.documentElement.classList.contains("dark") ? "light" : "dark";
      localStorage.setItem("theme", next);
      apply(next);
    });
  })();
</script>
```

---

## 6) Decision form → localStorage

Lets readers leave "approve/reject + comment" entries at the bottom of the doc, persisted locally (no network).

HTML is in the "Form" section of `components.md`.

```html
<div id="feedback-output" style="margin-top: 14px; font-family: ui-monospace, Menlo, monospace; font-size: 11px; color: var(--ink-faint);"></div>

<script>
  (function () {
    const form = document.getElementById("feedback");
    const out = document.getElementById("feedback-output");
    if (!form) return;
    const KEY = "feedback-" + location.pathname;

    const render = () => {
      const all = JSON.parse(localStorage.getItem(KEY) || "[]");
      if (!all.length) { out.textContent = ""; return; }
      out.innerHTML = "<strong>local responses:</strong><br/>" +
        all.map(r => `· ${r.reviewer} → ${r.vote}${r.comment ? " · " + r.comment : ""}`).join("<br/>");
    };
    render();

    form.addEventListener("submit", e => {
      e.preventDefault();
      const entry = {
        reviewer: form.reviewer.value.trim(),
        vote: form.vote.value,
        comment: form.comment.value.trim(),
        at: new Date().toISOString()
      };
      const all = JSON.parse(localStorage.getItem(KEY) || "[]");
      all.push(entry);
      localStorage.setItem(KEY, JSON.stringify(all));
      form.reset();
      render();
    });
  })();
</script>
```

---

## 7) Reading-progress bar

```css
.reading-progress {
  position: fixed; top: 0; left: 0;
  height: 2px; background: var(--accent);
  width: 0%; z-index: 10;
  transition: width 0.1s ease-out;
}
```

```html
<div class="reading-progress" id="progress"></div>
<script>
  const p = document.getElementById("progress");
  window.addEventListener("scroll", () => {
    const h = document.documentElement.scrollHeight - innerHeight;
    p.style.width = (scrollY / h) * 100 + "%";
  });
</script>
```

---

## 8) Click-to-zoom figures

```css
figure.zoomable { cursor: zoom-in; }
figure.zoomable.zoomed {
  position: fixed; inset: 0; z-index: 100;
  background: rgba(0,0,0,0.85); cursor: zoom-out;
  padding: 40px; margin: 0; border: none;
  display: flex; align-items: center; justify-content: center;
}
figure.zoomable.zoomed svg, figure.zoomable.zoomed img {
  max-width: 95vw; max-height: 90vh; width: auto;
}
figure.zoomable.zoomed figcaption { display: none; }
```

```html
<script>
  document.querySelectorAll("figure").forEach(fig => {
    fig.classList.add("zoomable");
    fig.addEventListener("click", () => fig.classList.toggle("zoomed"));
  });
</script>
```

---

## Recommended combos

| Doc type | Suggested mix |
|---|---|
| Short / TL;DR only | No interactivity |
| Proposal / RFC | Collapse + form + dark mode |
| Vendor / comparison | Table filter & sort + collapse |
| Tutorial / how-to | Code copy + TOC + reading progress |
| Long-form / report | TOC + dark mode + figure zoom |

Before adding any interaction, ask: **does it actually help comprehension?** If not, skip it.
