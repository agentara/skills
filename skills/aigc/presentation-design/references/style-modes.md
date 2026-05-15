# Style Modes

Concrete palettes and typography directions for each style sub-mode. The user has already chosen **light** or **dark** at workflow step 2 — pick a sub-mode from the matching section based on the topic.

Each entry specifies: **background**, **primary accent**, **secondary accent**, **typography direction**, **image treatment**, **good for**.

---

## Dark Modes

### `dark cinematic` *(default)*

- **HRD.** High contrast, high detail. Make the major content bright and stand out.
  > For some reason, GPT images tends to generate darker content, so we need to explicitly ask for high contrast, high detail.
- **Background.** Deep navy or charcoal black with a soft gradient toward near-black at the edges. Subtle film grain.
- **Primary accent.** Electric blue (#3B82F6 family) or warm gold (#D4A24A family).
- **Secondary accent.** Off-white / ivory for body text. One accent only per deck — pick blue or gold, not both.
- **Typography.** Bold modern sans-serif titles (e.g. Inter Display, Söhne, GT America). Large slide numbers. Clear section headers. High contrast for TV readability.
- **Image treatment.** Gradient masks over hero images, dark overlays, glow edges, depth layering. Cropped hero imagery embedded into the slide — never pasted-on rectangles.
- **Good for.** Strategy decks, premium brand stories, editorial features, executive presentations when the topic is ambiguous.

### `dark sports broadcast`

- **Background.** Near-black with stadium-light gradients, slight vignette. Optional faint scanline or screen-shimmer texture.
- **Primary accent.** Red (#EF4444 family) or team-color red equivalent.
- **Secondary accent.** Cyan (#22D3EE family) for data highlights and chart annotations.
- **Typography.** Bold condensed sans (e.g. Druk Wide, Compressa), high-impact italic for energy. Large numbers. Stat-heavy treatments — jersey-style numerals welcome.
- **Image treatment.** High-contrast action photography. Stadium lighting blown out as glow. Player portraits cropped tight.
- **Good for.** Sports recaps, match analyses, season previews, athlete features, esports.

### `dark geopolitical intelligence`

- **Background.** Charcoal with subtle map textures or coordinate-grid overlays. Faint topographic or satellite imagery as background.
- **Primary accent.** Amber (#F59E0B family).
- **Secondary accent.** Cyan (#06B6D4 family) for data, routes, and connections.
- **Typography.** Editorial sans with a mono accent for data labels and coordinates (e.g. Söhne + JetBrains Mono). Quiet, restrained.
- **Image treatment.** Maps embedded full-bleed with dark overlays. Satellite imagery, infographic-style connectors, route lines.
- **Good for.** News analysis, geopolitical briefings, defense / intel content, supply-chain or logistics stories.

### `dark editorial`

- **Background.** Near-black with a single warm accent — no gradients, flat and confident.
- **Primary accent.** Warm gold (#D4A24A) **or** coral (#F87171) — one only.
- **Secondary accent.** Ivory / cream for body text.
- **Typography.** Serif headlines (e.g. GT Sectra, Tiempos Headline) paired with a quiet sans for body. Long-form-magazine feel.
- **Image treatment.** Single hero image per slide, beautifully cropped. Restrained overlays — let the photo speak.
- **Good for.** Long-form journalism style, magazine-style decks, premium brand storytelling, documentary topics.

### `dark glassmorphism`

- **Background.** Vivid blurred backdrop (gradient mesh, blurred photo, or abstract color cloud).
- **Primary accent.** Translucent white panels with subtle borders. Pick one vivid hue for the underlying gradient (violet, cyan, or magenta).
- **Secondary accent.** Soft white glow on edges.
- **Typography.** Geometric sans (e.g. Geist, Inter) at medium weight. Avoid heavy bold — let the glass do the work.
- **Image treatment.** Layered translucent cards floating over the colorful blurred background. Each "card" is a slide element.
- **Good for.** Modern SaaS product launches, AI / tech keynotes, creative agency decks.

### `dark cyberpunk`

- **Background.** Deep violet or near-black with vivid neon glows along edges.
- **Primary accent.** Neon magenta (#EC4899 family).
- **Secondary accent.** Cyan (#22D3EE family). Optional third: acid green for chart highlights.
- **Typography.** Sharp geometric sans, occasionally stretched. Slight glitch / chromatic-aberration treatment on titles is okay — but sparingly.
- **Image treatment.** Neon rim lighting, high contrast, deep shadows. Avoid kitsch — keep it disciplined.
- **Good for.** Gaming, esports, web3, AI-edge topics, futuristic product reveals.

### `dark luxury keynote`

- **Background.** Pure black or near-black, perfectly flat.
- **Primary accent.** Gold leaf (#C9A961) — sparingly applied.
- **Secondary accent.** Muted ivory (#F5F1E8) for text.
- **Typography.** High-contrast serif titles (e.g. Bodoni, Didot) paired with a clean sans for body. Generous tracking.
- **Image treatment.** Minimal. Black-and-white or duotone photography. Single hero element per slide.
- **Good for.** Luxury brands, watch / fashion / fine-jewelry, private banking, premium investment stories.

---

## Light Modes

### `light minimal keynote`

- **Background.** Off-white (#FAFAF8 or pure #FFFFFF). Generous whitespace.
- **Primary accent.** One color only — choose based on the brand or topic (Apple-blue, deep green, terracotta, etc.). Use sparingly: titles, dividers, and one highlight per slide.
- **Secondary accent.** Soft gray (#9CA3AF family) for secondary text and dividers.
- **Typography.** Serif headlines (e.g. New York, Tiempos) **or** geometric sans (e.g. Inter, Geist) — pick one direction, stay consistent. Large type, ample line-height.
- **Image treatment.** Clean cropped hero photography. No overlays. Photos sit confidently inside the slide with proportional whitespace.
- **Good for.** B2B SaaS, design-led brands, thought leadership, founder talks, conference keynotes.

### `bright commercial keynote`

- **Background.** Pure white or saturated brand-color blocks. Sections of the slide can be full-bleed brand color.
- **Primary accent.** A bold, saturated brand color (cobalt, scarlet, electric green — match the product/brand).
- **Secondary accent.** Black for type. Optional bright second accent for chart highlights.
- **Typography.** Bold sans titles (e.g. GT Walsheim, Söhne Breit), heavy weight. Punchy and product-forward.
- **Image treatment.** Product photography front and center. High-key lighting, clean shadows. Color blocks behind products. Charts and data viz use the brand color directly.
- **Good for.** Consumer product launches, retail / e-commerce, mass-market campaigns, FMCG, ad agency pitches.

---

## Selection Heuristics

- **Sports / news / geopolitics / action** → `dark sports broadcast` or `dark geopolitical intelligence`.
- **Strategy / editorial / premium brand / documentary** → `dark cinematic`, `dark editorial`, or `dark luxury keynote`.
- **AI / SaaS / modern tech / creative agency** → `dark glassmorphism` or `dark cyberpunk` (cyberpunk only when the topic genuinely calls for it).
- **B2B SaaS / thought leadership / design-led** → `light minimal keynote`.
- **Consumer products / retail / commercial campaigns** → `bright commercial keynote`.
- **Topic unclear** → `dark cinematic`.

After selecting a sub-mode, briefly tell the user which one was chosen and why, so they can override if needed before the deck plan is written.
