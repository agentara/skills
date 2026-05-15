# Slide Layout Library

A named, composable pattern pool for 16:9 slide tiles. Pick **6 layouts** that together form a coherent narrative arc — mix layouts, do not repeat the same one across all 6.

## Composition Heuristics

- Always open with `hero-title` (slide 01) and close with `closer` (slide 06) unless the topic demands otherwise.
- Vary the middle four (slides 02–05). Avoid two `3-card`s back-to-back. Avoid four text-heavy slides in a row.
- Balance information types: pair text-heavy layouts with visual-dominant layouts.
- Accent color usage must stay consistent across all 6 — choose where it appears (titles, dividers, numbers, chart highlights) and apply uniformly.
- If the topic is data-heavy, include at least one `chart-dominant` or `big-number`.
- If the topic is person-driven (athlete, founder, leader), include `portrait-feature`.
- If the topic is argumentative or contrastive, include `comparison`.
- If the topic is chronological (history, roadmap, season recap), include `timeline`.

## Layouts

### `hero-title`

**When to use.** Opening slide. Sets the tone, theme, and visual identity for the whole deck.

**Anatomy.** Oversized title dominates. Optional subtitle, deck date, or section number. Single hero visual or full-bleed background image. Slide number `01` in a corner.

**Content slots.** `title`, optional `subtitle`, optional `eyebrow` (one-line context).

**Do.** Use the biggest type on the board. Let the background image or graphic carry mood. Give the title a clear vertical anchor (top-left, lower-left, or centered).

**Don't.** Add bullet points. Crowd with multiple visuals. Use the same composition as `closer`.

```text
┌────────────────────────────────┐
│ 01                             │
│                                │
│   BIG TITLE                    │
│   subtitle line                │
│                                │
│   [hero visual / full bleed]   │
└────────────────────────────────┘
```

---

### `split-2col`

**When to use.** The workhorse layout. Any slide that needs text + supporting visual side-by-side.

**Anatomy.** Two columns. One side carries text (title + 3–5 short points). The other side carries a single image, chart, map, portrait, or product shot. Either side can be left or right.

**Content slots.** `title`, `bullets` (3–5), `visual`.

**Do.** Keep the text column tight — short bullets, generous line spacing. Let the visual breathe.

**Don't.** Fill the visual column with multiple stacked images. Let the text column wrap into essay paragraphs.

```text
┌────────────────────────────────┐
│ 02   TITLE                     │
│      • point one    │          │
│      • point two    │ [visual] │
│      • point three  │          │
│      • point four   │          │
└────────────────────────────────┘
```

---

### `3-card`

**When to use.** Three equally weighted concepts, pillars, principles, or themes.

**Anatomy.** Three vertical cards across the slide. Each card: small icon or number + short label + 1-line description. Optional shared section title above.

**Content slots.** `section_title` (optional), 3 × (`card_title`, `card_body`).

**Do.** Keep card titles parallel in form (all nouns, or all verbs). Use consistent card heights.

**Don't.** Pack each card with a paragraph. Use mismatched icon styles. Stack two `3-card`s in the same deck — once is enough.

```text
┌────────────────────────────────┐
│ 03   Section Title             │
│   ┌─────┐ ┌─────┐ ┌─────┐      │
│   │ 01  │ │ 02  │ │ 03  │      │
│   │ ttl │ │ ttl │ │ ttl │      │
│   │ ··· │ │ ··· │ │ ··· │      │
│   └─────┘ └─────┘ └─────┘      │
└────────────────────────────────┘
```

---

### `big-number`

**When to use.** A single metric, percentage, ratio, or score is the entire point of the slide.

**Anatomy.** One huge number occupies 40–60% of the tile. One short caption above or below explains what the number means. Optional source line in small type.

**Content slots.** `metric` (the number/value), `caption` (≤ 12 words), optional `source`.

**Do.** Use the accent color on the number. Pair with a quiet background.

**Don't.** Add multiple secondary metrics — that's a `chart-dominant` slide. Add bullets.

```text
┌────────────────────────────────┐
│ 04                             │
│                                │
│         87%                    │
│      caption line              │
│                                │
│      source: ...               │
└────────────────────────────────┘
```

---

### `chart-dominant`

**When to use.** A chart, map, table, or data visualization is the slide.

**Anatomy.** The chart fills 60–70% of the tile. Title sits compact above the chart. 1–2 short annotations or callouts highlight what to look at. Legend kept minimal.

**Content slots.** `title`, `chart_description` (what the chart shows), 1–2 `annotations`.

**Do.** Use the accent color to highlight the single most important data point or line. Strip away gridlines and legends to the minimum.

**Don't.** Show four charts on one tile. Use rainbow palettes. Add unrelated bullets.

```text
┌────────────────────────────────┐
│ 05   Chart Title               │
│                                │
│    [chart / map fills 60–70%]  │
│           ↑ annotation         │
│                                │
└────────────────────────────────┘
```

---

### `quote-frame`

**When to use.** A single pull-quote carries the slide — a key insight, mission statement, customer voice, or thesis.

**Anatomy.** Large quoted text centered or left-anchored. Attribution line below (name, role, source). Quiet textured or gradient background; optional small portrait or logo.

**Content slots.** `quote`, `attribution`, optional `portrait`.

**Do.** Use generous whitespace. Let typography do the work — bold serif or modern sans depending on the style mode.

**Don't.** Add bullets. Stretch the quote into a paragraph. Compete with a loud background image.

```text
┌────────────────────────────────┐
│ 02                             │
│                                │
│   " A short, sharp quote       │
│     that lands the slide. "    │
│                                │
│     — Name, Role               │
└────────────────────────────────┘
```

---

### `timeline`

**When to use.** Chronological sequence — a history, roadmap, season recap, product evolution, project phases.

**Anatomy.** Horizontal or vertical line with 3–5 nodes. Each node has a date/marker + short label. Optional small illustration at one or two nodes.

**Content slots.** `title`, 3–5 × (`date`, `label`, optional `note`).

**Do.** Keep node spacing even. Use the accent color on the line and on the current/featured node.

**Don't.** Cram 8+ nodes. Mix horizontal and vertical timelines in the same deck.

```text
┌────────────────────────────────┐
│ 03   Timeline Title            │
│                                │
│   ●─────●─────●─────●─────●    │
│   2019  2020  2022  2024  now  │
│   ttl   ttl   ttl   ttl   ttl  │
└────────────────────────────────┘
```

---

### `portrait-feature`

**When to use.** A person is the subject of the slide — athlete, founder, expert, character, customer.

**Anatomy.** Portrait cropped to roughly half the tile (often left side, often slightly bleeding off-frame). Title (the person's name) + role / one-line description on the other side. Optional 2–3 stats or facts in small type.

**Content slots.** `portrait`, `name`, `role`, optional `stats` (2–3 short facts).

**Do.** Crop tight. Use cinematic lighting consistent with the style mode. Keep typography quiet so the portrait dominates.

**Don't.** Use stock-photo headshots that clash with the deck's mood. Add long paragraphs.

```text
┌────────────────────────────────┐
│ 04                             │
│ ┌────────┐                     │
│ │        │   NAME              │
│ │portrait│   Role / Title      │
│ │        │   • stat one        │
│ │        │   • stat two        │
│ └────────┘                     │
└────────────────────────────────┘
```

---

### `comparison`

**When to use.** Two things must be contrasted side-by-side with parallel structure — before vs after, A vs B, us vs them, plan vs result.

**Anatomy.** Tile split into two equal halves. Each half: label at top + 3–4 short parallel bullets or one supporting visual. Optional center divider with a comparison verb (`vs`, `→`).

**Content slots.** `title`, `left_label`, `left_points`, `right_label`, `right_points`.

**Do.** Make the two sides visually symmetric and grammatically parallel. Use the accent color to mark the "winning" or focal side.

**Don't.** Make one side dense and the other sparse. Use three-way comparisons here — that's a `3-card`.

```text
┌────────────────────────────────┐
│ 05   Comparison Title          │
│   BEFORE      │      AFTER     │
│   • point     │   • point      │
│   • point     │   • point      │
│   • point     │   • point      │
└────────────────────────────────┘
```

---

### `closer`

**When to use.** Final slide. Takeaway, CTA, signature, or thank-you.

**Anatomy.** Calmer composition than `hero-title`. One short takeaway line (the deck's "so what"), optional CTA, optional signature / logo / contact. Slide number `06` in a corner.

**Content slots.** `takeaway` (one line), optional `cta`, optional `signature`.

**Do.** Echo the visual language of `hero-title` but at lower intensity — same palette, same typography, calmer composition. Leave whitespace.

**Don't.** Reintroduce content the deck already covered. Make it as loud as the opener.

```text
┌────────────────────────────────┐
│ 06                             │
│                                │
│   Takeaway line.               │
│                                │
│   → CTA                        │
│   signature / logo             │
└────────────────────────────────┘
```
