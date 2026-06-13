---
name: torn-paper-collage-poster
description: Create style-selectable AI poster prompts and image-generation workflows, defaulting to torn-paper editorial collage but supporting a poster style selector with core keywords, typography, readable poster text, and refactored style effects. Use when the user asks to generate, redesign, or prompt an Image Generator for a poster, style-show poster, campaign poster, torn-paper collage poster, creator economy poster, launch poster, event poster, product poster, or editorial visual with optional reference images, person photos, product/object photos, news/event data, cultural moments, technology milestones, or mood/style references. Do NOT trigger for cinematic video key art when the user specifically wants the video-poster-design workflow.
---

# Torn-Paper Collage Poster

This skill is a poster workflow with selectable styles. The default style is the repo's existing `torn-paper-editorial-collage`; other styles are optional poster-ready directions.

## Core Workflow

1. Collect the required theme and any optional inputs:
   - Theme or occasion, such as a product launch, tech news, public announcement, cultural moment, music poster, exhibition poster, founder story, team portrait, city memory, film/book release, style-show image, campaign visual, or object-focused collectible.
   - Main subject, if any: person, group, pet, product, object, vehicle, landmark, venue, device, artwork, or place.
   - Data to show: title, name, event, date, location, stats, role, edition number, product details, quote snippets supplied by the user, or user-supplied notes.
   - Reference images, if supplied: treat person photos as identity/subject references; treat mood boards as loose direction only.
2. Read `references/poster-styles.md` and choose the closest style category file:
   - If the user names a style or supplies style cues, open the relevant file under `references/styles/` and choose the closest poster style.
   - If the user asks for options, propose 3 to 5 matching style IDs with their core keywords from the category files.
   - If the style is unspecified, use `torn-paper-editorial-collage` as the default.
   - Open the referenced file under `references/styles/` for the chosen style's prompt add-on and effects.
   - Always carry the selected style ID and its core keywords into the final prompt or style selector output.
3. If the selected style is `torn-paper-editorial-collage`, or if the user explicitly wants torn-paper treatment, also read `references/style-dna.md` before writing the final image prompt.
   - For non-default styles, do not force torn-paper motifs unless the user asks for a hybrid.
4. If the user omits important poster data, proceed with a strong poster using only the theme. Do not invent specific facts, dates, roles, rankings, brands, official claims, quotes, statistics, UI details, or provenance details.
5. Generate a single clear Image Generator prompt that includes:
   - Selected style ID and core style keywords from the selector.
   - Style prompt add-on from the referenced style file.
   - Subject and theme.
   - The selected style effects: composition, typography, color, image treatment, and texture.
   - Typography and data treatment: title, subtitle, date, label, quote, number, or supplied data as readable poster elements.
   - Reference discipline and exclusions.
6. Call the image-generation tool directly when available and the user asked for an image. If only a prompt is requested, return the prompt plus the chosen style selector line.
7. Inspect the generated result against the selected style effects and, for the default torn-paper style, the reject checklist in `references/style-dna.md`. If it fails materially, regenerate with a stricter prompt that names the failure.

## Text and Fact Policy

This is a poster skill, not a no-text aesthetic study. Do not add a blanket `no text`, `no readable text`, or `no letters` restriction unless the user explicitly asks for a textless poster.

- Use readable display typography when the user supplies a title, phrase, date, location, edition number, quote, or label.
- If no exact copy is supplied, use the theme itself as the main title when that is natural; otherwise leave deliberate title space or use generic non-factual labels such as "FIELD NOTE", "LAUNCH", "ISSUE 01", or "POSTER STUDY".
- Do not invent official facts, claims, dates, awards, brand names, sponsor names, logos, quotes, charts, stats, UI screens, or provenance details.
- Avoid random extra text, filler microtext, fake sponsor logos, watermarks, unreadable letter noise, or copied text from references.
- If exact text is critical and the image model cannot render it cleanly, generate the poster with planned text areas and recommend a deterministic typography overlay pass.

## Style Selector Contract

When a style decision is part of the output, use this compact selector format:

```text
Style: [style-id]
Core keywords: [copy the core keywords from the selected file under references/styles/]
Style file: [references/styles/category-file.md]
Poster effect: [one sentence explaining composition + typography + color/image treatment]
```

The `Core keywords` line is mandatory because it makes the style selectable and reusable.

## Prompt Pattern

Use this structure and adapt it to the user's inputs:

```text
Create a premium collectible poster about [THEME].
Selected style: [STYLE ID].
Core style keywords: [CORE KEYWORDS FROM THE STYLE SELECTOR].
Main subject: [SUBJECT OR "no specific person"].
Use the supplied reference image only for [identity / pose / mood / camera energy / texture density], not for copying layout, text, logos, or unrelated subjects.

Style prompt add-on: [COPY OR ADAPT THE PROMPT ADD-ON FROM THE REFERENCED STYLE FILE].

Style effect: [COMPOSITION, MATERIALS, IMAGE TREATMENT, TYPOGRAPHY, COLOR FROM THE SELECTED STYLE FILE].

Typography and text plan: include [USER-SUPPLIED TITLE / THEME TITLE / SUPPLIED DATA]. Make important text large, intentional, and readable. Do not add random slogans, fake credits, fake sponsors, or invented facts.

Composition: [STYLE-SPECIFIC COMPOSITION]. The subject should feel integrated into the poster system, not pasted into a clean template.

Visual language: [STYLE-SPECIFIC VISUAL MATERIALS AND TEXTURES].

Data to include only if provided: [USER DATA]. Keep important text large and legible; do not hide main data in microtext.

Color direction: [STYLE-SPECIFIC PALETTE]. Keep the style coherent and poster-like rather than generic, corporate, or dashboard-like.

Avoid: generic event flyer, clean corporate dashboard, fake sponsor logos, fake maps/evidence, fake product evidence, fake UI, fake quotes, fake statistics, impossible props, watermarks, copied slogans, visible brand logos unless provided and requested, copied Chinese text from references, changing the identity of a supplied person, random extra text, and no-text/no-readable-text constraints unless the user explicitly requested a textless poster.
```

For the default `torn-paper-editorial-collage` style, use the more specific material language below:

```text
Visual language: torn-paper editorial collage, layered paper construction, old newspaper texture, certificate or archive scraps when relevant, torn black paper fields, cream paper slabs with rough fiber edges, colored tape strips, crooked overlapping labels, drop shadows, ripped photo windows, stickers, stamps, barcode, safety pins, paper tape, splashes or scuffs, halftone dots, photocopy grain, risograph texture, handwriting marks, contour lines, and scene fragments that match the theme.

Composition: paper layers must dominate structurally. The person/subject should be a cutout breaking through paper layers or embedded between torn sheets. Avoid a clean rectangular photo frame. Use huge type, oversized numbers, rough stamps, tape, and readable evidence-data stickers/cards distributed across the poster.
```

## Handling References

- Treat user-supplied person photos as identity and subject references. Preserve the person, approximate pose/energy, and relevant context.
- Treat product/object/place photos as subject references. Preserve recognizable shape, material, key details, and product/place identity when the user asks for it.
- Treat mood/style references as loose direction for texture, camera angle, color energy, typography density, and composition.
- Never copy exact layouts, slogans, watermarks, visible brands/logos, unrelated subjects, or Chinese text from references.

## Output

- For image requests, generate the image and briefly state the selected style ID, core keywords, and what theme/data was used.
- For prompt-only requests, output one ready-to-use prompt, the style selector line, and, when helpful, one short negative prompt.
- For style-selection requests, list the matching style IDs with core keywords and one-line poster effects.
- For missing data, do not ask unless the user's request depends on it. Use placeholders only if the user explicitly wants a reusable template.

## References

- `references/poster-styles.md`: compact category selector and references to detailed style files. Read this for every run.
- `references/styles/*.md`: detailed style IDs, core keywords, prompt add-ons, effects, and avoid notes grouped by category. Read only the file needed for the selected style.
- `references/style-dna.md`: default torn-paper editorial collage details and reject checklist. Read this when the selected style is `torn-paper-editorial-collage` or when the user asks for torn-paper treatment.
