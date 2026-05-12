# Inline SVG Figures — five typical skeletons

Every SVG sits inside a `<figure>`, has a `<figcaption>`, and references no external assets. Hex palette in `components.md`.

Font is consistent across all figures:
```
font-family="ui-monospace, Menlo, monospace" font-size="12"
```

---

## 1) Architecture · nodes + arrows (left → right)

Good for: service topology, module dependency, data flow.

```html
<figure>
  <svg viewBox="0 0 760 360" xmlns="http://www.w3.org/2000/svg"
       font-family="ui-monospace, Menlo, monospace" font-size="12">
    <rect width="760" height="360" fill="#fff"/>

    <!-- node A -->
    <g>
      <rect x="60" y="140" width="160" height="80" fill="#eef4f8" stroke="#6f9bb8" stroke-width="1.4"/>
      <text x="70" y="160" fill="#6f9bb8" font-weight="600" letter-spacing="0.1em" font-size="11">NODE A</text>
      <text x="70" y="180" fill="#7a7a7a" font-size="10.5" font-style="italic">→ Description</text>
      <text x="70" y="200" fill="#4a4a4a">One line of content</text>
    </g>

    <!-- node B -->
    <g>
      <rect x="300" y="140" width="160" height="80" fill="#fff" stroke="#6f9bb8" stroke-width="1.4"/>
      <text x="310" y="160" fill="#6f9bb8" font-weight="600" letter-spacing="0.1em" font-size="11">NODE B</text>
      <text x="310" y="200" fill="#4a4a4a">One line of content</text>
    </g>

    <!-- node C -->
    <g>
      <rect x="540" y="140" width="160" height="80" fill="#f5ecdc" stroke="#b88a4a" stroke-width="1.4"/>
      <text x="550" y="160" fill="#7a6420" font-weight="600" letter-spacing="0.1em" font-size="11">NODE C</text>
      <text x="550" y="200" fill="#4a4a4a">One line of content</text>
    </g>

    <!-- arrows -->
    <defs>
      <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5"
              markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#6f9bb8"/>
      </marker>
    </defs>
    <g fill="none" stroke="#6f9bb8" stroke-width="1.4">
      <path d="M 220 180 L 298 180" marker-end="url(#arr)"/>
      <path d="M 460 180 L 538 180" marker-end="url(#arr)"/>
    </g>

    <text x="259" y="170" fill="#7a7a7a" font-size="10" text-anchor="middle">request</text>
    <text x="499" y="170" fill="#7a7a7a" font-size="10" text-anchor="middle">tool call</text>
  </svg>
  <figcaption><span class="fig-num">FIG 1</span>Architecture diagram</figcaption>
</figure>
```

---

## 2) Timing comparison · two parallel timelines

Good for: before/after migration, old vs new flow, A/B comparison.

```html
<figure>
  <svg viewBox="0 0 760 320" xmlns="http://www.w3.org/2000/svg"
       font-family="ui-monospace, Menlo, monospace" font-size="11">
    <rect width="760" height="320" fill="#fff"/>

    <!-- time axis -->
    <line x1="180" y1="280" x2="720" y2="280" stroke="#7a7a7a"/>
    <g fill="#7a7a7a" font-size="10">
      <text x="180" y="300" text-anchor="middle">0s</text>
      <text x="396" y="300" text-anchor="middle">60s</text>
      <text x="612" y="300" text-anchor="middle">120s</text>
      <text x="720" y="300" text-anchor="middle">3min</text>
    </g>
    <g stroke="#e8e8e2" stroke-width="1" stroke-dasharray="2 4">
      <line x1="396" y1="60" x2="396" y2="280"/>
      <line x1="612" y1="60" x2="612" y2="280"/>
    </g>

    <!-- row A -->
    <text x="160" y="100" text-anchor="end" fill="#7a6420" font-weight="600" font-size="11">Old</text>
    <rect x="180" y="88" width="50" height="22" fill="#f0ede5" stroke="#c0baa0"/>
    <text x="205" y="103" text-anchor="middle" fill="#4a4a4a">step 1</text>
    <rect x="230" y="88" width="180" height="22" fill="#ecdfb8" stroke="#b88a4a"/>
    <text x="320" y="103" text-anchor="middle" fill="#7a6420">blocking wait</text>

    <!-- row B -->
    <text x="160" y="200" text-anchor="end" fill="#6f9bb8" font-weight="600" font-size="11">New</text>
    <rect x="180" y="188" width="50" height="22" fill="#eef4f8" stroke="#a5c0d8"/>
    <text x="205" y="203" text-anchor="middle" fill="#4a4a4a">step 1</text>
    <rect x="230" y="188" width="180" height="22" fill="#eef4f8" stroke="#a5c0d8"/>
    <text x="320" y="203" text-anchor="middle" fill="#4a4a4a">parallel</text>
  </svg>
  <figcaption><span class="fig-num">FIG 2</span>Timing comparison</figcaption>
</figure>
```

---

## 3) Bar comparison chart

Good for: cost comparison, performance comparison, multi-candidate scoring.

```html
<figure>
  <svg viewBox="0 0 760 280" xmlns="http://www.w3.org/2000/svg"
       font-family="ui-monospace, Menlo, monospace" font-size="11">
    <rect width="760" height="280" fill="#fff"/>

    <!-- axes -->
    <line x1="180" y1="240" x2="700" y2="240" stroke="#7a7a7a"/>
    <line x1="180" y1="40" x2="180" y2="240" stroke="#7a7a7a"/>
    <g fill="#7a7a7a" font-size="10" text-anchor="end">
      <text x="170" y="244">$0</text>
      <text x="170" y="144">$4</text>
      <text x="170" y="44">$8</text>
    </g>
    <g stroke="#e8e8e2" stroke-width="1" stroke-dasharray="2 4">
      <line x1="180" y1="144" x2="700" y2="144"/>
      <line x1="180" y1="44" x2="700" y2="44"/>
    </g>

    <!-- group: old vs new for category 1 -->
    <rect x="220" y="44" width="40" height="196" fill="#ecdfb8" stroke="#b88a4a"/>
    <text x="240" y="35" text-anchor="middle" fill="#7a6420" font-weight="600">$8</text>
    <rect x="265" y="238" width="40" height="2" fill="#a5c0d8" stroke="#6f9bb8"/>
    <text x="285" y="232" text-anchor="middle" fill="#6f9bb8" font-weight="600">$0</text>
    <text x="262" y="262" text-anchor="middle" fill="#4a4a4a">Category 1</text>

    <!-- legend -->
    <g transform="translate(40, 50)" font-size="10" fill="#7a7a7a">
      <rect x="0" y="0" width="14" height="10" fill="#ecdfb8" stroke="#b88a4a"/>
      <text x="20" y="9">Old</text>
      <rect x="0" y="20" width="14" height="10" fill="#a5c0d8" stroke="#6f9bb8"/>
      <text x="20" y="29">New</text>
    </g>
  </svg>
  <figcaption><span class="fig-num">FIG 3</span>Bar comparison</figcaption>
</figure>
```

---

## 4) Stacked layers (three or N tiers)

Good for: layered architecture (frontend / service / storage), layered data flow.

```html
<figure>
  <svg viewBox="0 0 760 360" xmlns="http://www.w3.org/2000/svg"
       font-family="ui-monospace, Menlo, monospace" font-size="12">
    <rect width="760" height="360" fill="#fff"/>

    <!-- layer 1 -->
    <rect x="80" y="40" width="600" height="80" fill="#eef4f8" stroke="#6f9bb8" stroke-width="1.4"/>
    <text x="92" y="60" fill="#6f9bb8" font-weight="600" letter-spacing="0.1em" font-size="11">LAYER 1 · Frontend</text>
    <text x="92" y="80" fill="#7a7a7a" font-size="10.5" font-style="italic">→ Deploy target</text>
    <text x="92" y="102" fill="#4a4a4a">Description</text>

    <!-- layer 2 -->
    <rect x="80" y="140" width="600" height="80" fill="#f5ecdc" stroke="#b88a4a" stroke-width="1.4"/>
    <text x="92" y="160" fill="#7a6420" font-weight="600" letter-spacing="0.1em" font-size="11">LAYER 2 · Service</text>
    <text x="92" y="180" fill="#7a7a7a" font-size="10.5" font-style="italic">→ Deploy target</text>
    <text x="92" y="202" fill="#4a4a4a">Description</text>

    <!-- layer 3 -->
    <rect x="80" y="240" width="600" height="80" fill="#ecede5" stroke="#6b7560" stroke-width="1.4"/>
    <text x="92" y="260" fill="#5a5a3a" font-weight="600" letter-spacing="0.1em" font-size="11">LAYER 3 · Storage</text>
    <text x="92" y="280" fill="#7a7a7a" font-size="10.5" font-style="italic">→ Deploy target</text>
    <text x="92" y="302" fill="#4a4a4a">Description</text>
  </svg>
  <figcaption><span class="fig-num">FIG 4</span>Stacked architecture</figcaption>
</figure>
```

---

## 5) Lifecycle · timeline with events + a branch point

Good for: state transitions, user journey, phase switches.

```html
<figure>
  <svg viewBox="0 0 760 280" xmlns="http://www.w3.org/2000/svg"
       font-family="ui-monospace, Menlo, monospace" font-size="11">
    <rect width="760" height="280" fill="#fff"/>

    <!-- time axis -->
    <line x1="180" y1="240" x2="720" y2="240" stroke="#7a7a7a"/>
    <g fill="#7a7a7a" font-size="10">
      <text x="180" y="260" text-anchor="middle">Start</text>
      <text x="360" y="260" text-anchor="middle">Phase 1</text>
      <text x="540" y="260" text-anchor="middle">Phase 2</text>
      <text x="720" y="260" text-anchor="middle">End state</text>
    </g>
    <line x1="540" y1="40" x2="540" y2="240" stroke="#a05050" stroke-width="1" stroke-dasharray="3 3"/>
    <text x="540" y="30" text-anchor="middle" fill="#a05050" font-weight="600">Switch point</text>

    <!-- discrete events -->
    <rect x="200" y="85" width="40" height="20" fill="#a5c0d8" stroke="#6f9bb8"/>
    <rect x="340" y="85" width="40" height="20" fill="#a5c0d8" stroke="#6f9bb8"/>
    <rect x="450" y="85" width="40" height="20" fill="#a5c0d8" stroke="#6f9bb8"/>

    <!-- continuous after switch -->
    <rect x="540" y="180" width="180" height="24" fill="#a5c0d8" stroke="#6f9bb8" stroke-width="1.5"/>
    <text x="630" y="196" text-anchor="middle" fill="#4a4a4a">Persistent state</text>
  </svg>
  <figcaption><span class="fig-num">FIG 5</span>Lifecycle</figcaption>
</figure>
```

---

## SVG general tips

- **Always start with `<rect width=... height=... fill="#fff"/>`** as a background. Otherwise the figure border and the SVG leak paper color between them.
- **Node rectangles:** `stroke-width="1.2"` is thin, `1.4-1.5` is medium, `2` is emphatic.
- **Dash rhythm:** auxiliary lines `stroke-dasharray="2 4"`, weak dependencies `stroke-dasharray="3 3"`.
- **text-anchor:** `start` (default) / `middle` / `end`.
- **Legend:** top-left or top-right via `<g transform="translate(40, 30)">`, with 14×10 swatches and labels.
- **Arrows:** define one `<defs><marker>...` per figure, then every `<path marker-end="url(#arr)">` reuses it.
- **No more than 5 distinct colors.** The more restrained the palette, the better the "paper" feel.
