---
name: torn-paper-collage-poster
description: Create AI image-generation prompts and image-generation workflows for torn-paper editorial collage style posters with layered ripped paper, rough typography, stamps, tape, stickers, cutout subjects, photocopy grain, and collectible evidence-board energy. Use when the user asks to generate, redesign, or prompt an Image Generator for this specific torn-paper collage poster style, especially when they provide a theme plus optional reference image, person photo, news/event data, launch data, product/object photo, cultural moment, technology milestone, or mood/style references.
---

# Torn-Paper Collage Poster

## Core Workflow

1. Collect the required theme and any optional inputs:
   - Theme or occasion, such as a product launch, tech news, public announcement, cultural moment, music poster, exhibition poster, founder story, team portrait, city memory, film/book release, or object-focused collectible.
   - Main subject, if any: person, group, pet, product, object, vehicle, landmark, venue, device, artwork, or place.
   - Data to show: title, name, event, date, location, stats, role, edition number, product details, quote snippets supplied by the user, or user-supplied notes.
   - Reference images, if supplied: treat person photos as identity/subject references; treat mood boards as loose direction only.
2. If the user omits important poster data, proceed with a strong poster using only the theme. Do not invent specific facts, dates, roles, rankings, brands, official claims, quotes, statistics, UI details, or provenance details.
3. Read `references/style-dna.md` before writing the final image prompt.
4. Generate a single clear Image Generator prompt that includes:
   - Subject and theme.
   - The torn-paper editorial collage material language.
   - Composition rules: paper layers dominate; subject breaks through or is embedded in layers; no clean rectangular main photo.
   - Typography and data treatment: huge type, oversized numbers, stamps, stickers, rough labels, readable cards.
   - Color direction selected from the style DNA. Default to energetic mid-bright poster contrast; avoid overly dark or harsh high-contrast posters unless the user explicitly asks for that mood.
   - Reference discipline and exclusions.
5. Call the image-generation tool directly when available and the user asked for an image. If only a prompt is requested, return the prompt.
6. Inspect the generated result against the reject checklist in `references/style-dna.md`. If it fails materially, regenerate with a stricter prompt that names the failure.

## Prompt Pattern

Use this structure and adapt it to the user's inputs:

```text
Create a premium collectible torn-paper editorial collage poster about [THEME].
Main subject: [SUBJECT OR "no specific person"].
Use the supplied reference image only for [identity / pose / mood / camera energy / texture density], not for copying layout, text, logos, or unrelated subjects.

Visual language: torn-paper editorial collage, layered paper construction, old newspaper texture, certificate or archive scraps when relevant, torn black paper fields, cream paper slabs with rough fiber edges, colored tape strips, crooked overlapping labels, drop shadows, ripped photo windows, stickers, stamps, barcode, safety pins, paper tape, splashes or scuffs, halftone dots, photocopy grain, risograph texture, handwriting marks, contour lines, and scene fragments that match the theme.

Composition: paper layers must dominate structurally. The person/subject should be a cutout breaking through paper layers or embedded between torn sheets. Avoid a clean rectangular photo frame. Use huge type, oversized numbers, rough stamps, tape, and readable evidence-data stickers/cards distributed across the poster.

Data to include only if provided: [USER DATA]. Keep important text large and legible; do not hide main data in microtext.

Color direction: [DEFAULT OR SELECTED ALTERNATIVE]. Unless explicitly requested, keep the poster energetic, tactile, and mid-bright rather than dark, severe, or extremely high-contrast.

Avoid: generic event flyer, clean certificate, corporate dashboard, one large rectangular main photo, thin decorative torn border, fake sponsor logos, fake maps/evidence, impossible props, watermarks, copied slogans, visible brand logos, Chinese text copied from references, changing the identity of a supplied person, and dark high-contrast poster treatment unless requested.
```

## Handling References

- Treat user-supplied person photos as identity and subject references. Preserve the person, approximate pose/energy, and relevant context.
- Treat mood/style references as loose direction for texture, camera angle, color energy, and typography density.
- Never copy exact layouts, slogans, watermarks, visible brands/logos, unrelated subjects, or Chinese text from references.

## Output

- For image requests, generate the image and briefly state what theme/data was used.
- For prompt-only requests, output one ready-to-use prompt and, when helpful, one short negative prompt.
- For missing data, do not ask unless the user's request depends on it. Use placeholders only if the user explicitly wants a reusable template.
