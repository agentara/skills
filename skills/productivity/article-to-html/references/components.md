# Components Cheat Sheet

Every snippet here is "paste directly into `template.html` inside `<article class="doc">`".

---

## Header

```html
<header class="doc-header">
  <div class="doc-eyebrow"><span class="mascot"></span>Team/Project · Doc type</div>
  <h1 class="doc-title">Main title</h1>
  <p class="doc-subtitle">Subtitle · one-sentence stance</p>
  <div class="doc-meta">
    <span>STATUS · DRAFT</span>
    <span>DATE · 2026-05-11</span>
    <span>AUTHOR · Team / Author</span>
  </div>
</header>
```

- `doc-eyebrow` is the breadcrumb / project name. `mascot` is the 8×8 color block.
- `doc-meta` accepts any number of `<span>`s — small monospace, with `·` separating label and value.

---

## TL;DR

```html
<div class="tldr">
  <div class="tldr-label">TL;DR</div>
  Body supports <strong>bold</strong>, <em>italic</em>, <code>code</code>, and links.
  Keep it to 3–4 sentences, ≤120 words.
</div>
```

If the source has no TL;DR, condense the first one or two paragraphs.

---

## Section (numbered)

```html
<section>
  <h2><span class="num">01</span>Section title</h2>
  <p>Body paragraph.</p>
  <h3>Subheading</h3>
  <ul>
    <li><strong>Keyword.</strong> Explanation.</li>
  </ul>
</section>
```

- Numbering `01 / 02 / 03` is small monospace, faint gray, auto-spaced 14px.
- Common list pattern: `<strong>Keyword.</strong> Explanation` — the bold lead acts as a visual anchor.

---

## Callout · three flavors

```html
<!-- Default (white background) -->
<div class="callout">
  <div class="callout-label">NOTE</div>
  A short note.
</div>

<!-- Warning / heads-up -->
<div class="callout warn">
  <div class="callout-label">CAUTION</div>
  Amber background — use for deferred decisions, risk, change windows.
</div>

<!-- Quotation -->
<div class="callout cite">
  "A quoted line."
  <div class="cite-source">— Author · Source</div>
</div>
```

Keep total callouts to 3–5. Decorative callouts are noise.

---

## Figure (with figcaption + inline SVG)

```html
<figure>
  <svg viewBox="0 0 760 360" xmlns="http://www.w3.org/2000/svg"
       font-family="ui-monospace, Menlo, monospace" font-size="12">
    <rect width="760" height="360" fill="#fff"/>
    <!-- your diagram -->
  </svg>
  <figcaption><span class="fig-num">FIG 1</span>Caption · subpoint</figcaption>
</figure>
```

- Use the CSS variable hex values directly in SVG (you cannot write `var(...)` inside SVG fills — hardcode the hex):
  - Ink: `#1a1a1a` (ink) / `#4a4a4a` (ink-soft) / `#7a7a7a` (ink-faint)
  - Rules: `#d8d8d2` (rule) / `#e8e8e2` (rule-soft)
  - Blue: `#6f9bb8` (accent) / `#eef4f8` (accent-faint) / `#a5c0d8`
  - Amber: `#b88a4a` (warn) / `#f5ecdc` (warn-soft) / `#ecdfb8`
  - Olive: `#6b7560` (session) / `#ecede5` (session-bg)
- All text uses `ui-monospace, Menlo, monospace`.
- Five typical skeletons live in `svg-figures.md`.

---

## N-column cards

```html
<div class="cards">
  <div class="card tone-a">
    <div class="card-icon">BRAIN</div>
    <div class="card-name">Agent</div>
    <div class="card-where">→ Centrally deployed</div>
    <div class="card-desc">One-line description.</div>
  </div>
  <div class="card tone-b">…</div>
  <div class="card tone-c">…</div>
</div>
```

Column count modifiers:

```html
<div class="cards cols-2">…</div>  <!-- two columns -->
<div class="cards cols-4">…</div>  <!-- four columns -->
```

`tone-a/b/c` controls the icon color (blue / amber / olive). Drop the tone class when you don't need color differentiation.

---

## Table

```html
<table>
  <thead>
    <tr>
      <th>Vendor</th>
      <th>Mechanism</th>
      <th>Startup</th>
      <th>Risk</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Option A</strong></td>
      <td>Notes</td>
      <td class="num">~90ms</td>
      <td class="accent">Shipped</td>
    </tr>
  </tbody>
</table>
```

- `<th>` is automatically uppercase + sans-serif small + gray.
- `<td class="num">` uses monospace (numbers, latencies, prices).
- `<td class="accent">` is blue + semibold (highlight a verdict).
- Pin column widths with `<th style="width: 70px;">`.

---

## Code block

```html
<pre><code>$ command --here
output
</code></pre>
```

- Inline: `<code>foo()</code>`
- No syntax highlighting (this is a document style, not a tutorial).

---

## Lists (bold-lead format)

```html
<ul>
  <li><strong>Keyword.</strong> Explanation, can run 1–2 full sentences.</li>
  <li><strong>Keyword.</strong> Explanation.</li>
</ul>
```

Open-questions / decision list — use ordered:

```html
<ol>
  <li><strong>Problem statement.</strong> Context / impact.</li>
</ol>
```

---

## Quote / blockquote

```html
<blockquote>
  A simple quoted line — faint gray, italic.
</blockquote>
```

If you have a source, switch to `.callout.cite`.

---

## Footer

```html
<footer>
  <h4>References</h4>
  <ul>
    <li>Author / Org · <a href="https://...">Link title</a></li>
    <li>Internal doc · <code>docs/path/to/file.md</code></li>
  </ul>
</footer>
```

You can add multiple `<h4>` groups (References / Acknowledgements / Changelog).

---

## Form (for interactive docs)

```html
<form id="feedback">
  <label for="reviewer">REVIEWER</label>
  <input type="text" id="reviewer" required />

  <label for="vote">VOTE</label>
  <select id="vote">
    <option value="approve">approve</option>
    <option value="reject">reject</option>
    <option value="abstain">abstain</option>
  </select>

  <label for="comment">COMMENT</label>
  <textarea id="comment" rows="3"></textarea>

  <button type="submit" class="btn primary">Submit</button>
</form>
```

Submit logic — see `interactive.md`.

---

## Buttons

```html
<button class="btn">Secondary</button>
<button class="btn primary">Primary</button>
```
