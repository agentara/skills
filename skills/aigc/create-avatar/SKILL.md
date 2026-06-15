---
name: create-avatar
description: Generate a single 16:9 six-panel avatar contact-sheet prompt with exactly six labeled sections, each containing a 3 x 2 portrait grid. Use this skill when the user asks to create an avatar board, team avatar sheet, fictional cast contact sheet, collectible character grid, six-name portrait board, or multi-character avatar prompt with named sections. Do NOT trigger for a single-avatar portrait, ordinary headshot retouching, unrestricted character design sheets, or video storyboard work.
---

# Six-Panel Avatar Contact Sheet

## Purpose

Generate one clean 16:9 character contact-sheet image with six labeled sections. The structure is fixed: 3 columns x 2 rows of sections, and each section contains a 3 x 2 grid of portraits. This skill is designed for team/avatar boards, fictional collectible casts, or stylized identity sheets.

## Core behavior

When this skill is used, produce a single image prompt for an image-generation model. The prompt must preserve the six-section layout, the name tabs, the portrait grids, the thin black borders, and the light gray/off-white overall background.

The skill should treat the six-name count as locked. There must be exactly six section names, shown in this order: top row left-to-right, then bottom row left-to-right. Do not add a seventh section, remove a section, merge sections, or create extra labels.

## Inputs

| Input | Type | Default | Rules |
|---|---:|---|---|
| `names` | string[6] | `["Luna", "Peter", "Saul", "Robert", "Zayn", "Meus"]` | Required count is exactly 6. Order maps to top row L->R, then bottom row L->R. |
| `style` | string | `photorealistic studio portraits with a clean retro collectible-card contact-sheet aesthetic` | Can be changed, but must not override the fixed layout. |
| `special_characters` | string[] | `["alien", "zombie-like character", "AI/robot humanoid", "anthropomorphic panda", "monkey/ape character"]` | Include these somewhere across the full 36 portraits, not necessarily in every section. |
| `aspect_ratio` | string | `16:9` | Locked unless the user explicitly asks for another ratio. |
| `overall_background` | string | `light gray / off-white` | Background outside all cards. |
| `section_layout` | string | `3 columns x 2 rows` | Locked. |
| `portraits_per_section` | number | `6` | Locked. |
| `portrait_grid` | string | `3 columns x 2 rows` | Locked inside each section. |
| `section_border` | string | `thin black outline around each card section` | Use clean outlines and visible separation. |
| `name_tab_style` | string | `centered white tab at the top of each section, thin black outline, bold black text` | Text should appear only in the six name tabs. |
| `portrait_background_palette` | string[] | `["teal", "pink", "olive", "brown", "purple", "magenta", "mustard", "orange", "cyan", "lime", "navy", "red"]` | Each portrait tile should use a distinct solid color background when possible. |
| `accessory_mix` | string[] | `["crown", "cowboy hat", "fedora", "beanie", "round glasses", "sunglasses", "mohawk", "bald head", "colorful hair", "facial hair", "face tattoos", "small facial decorations"]` | Use for variety across the 36 portraits. |
| `diversity_direction` | string | `varied genders, ages, ethnicities, skin tones, facial expressions, and fashion styles` | Apply globally. |
| `mood` | string | `creative, polished, playful, organized` | Keep the board coherent and editorial. |
| `negative_constraints` | string[] | `["no extra sections", "no missing sections", "no duplicate name tabs", "no text except the six names", "do not crop off name tabs", "do not make portraits messy or low resolution"]` | Append these constraints to the prompt. |

## Minimal input surface

The intended minimal interface is:

```json
{
  "names": ["Luna", "Peter", "Saul", "Robert", "Zayn", "Meus"],
  "style": "photorealistic studio portraits with a clean retro collectible-card contact-sheet aesthetic",
  "special_characters": ["alien", "zombie-like character", "AI/robot humanoid", "anthropomorphic panda", "monkey/ape character"]
}
```

Everything else should use defaults unless the user asks to change it.

## Validation

Before generating the final prompt:

1. If `names` is omitted, use the default six names.
2. If `names` has fewer or more than six names, do not silently add or remove names. Ask for exactly six names, or use the default names when the user clearly wants the default version.
3. Preserve name spelling exactly as supplied.
4. Preserve the fixed order: `names[0]`, `names[1]`, `names[2]` on the top row; `names[3]`, `names[4]`, `names[5]` on the bottom row.
5. Ensure every section contains exactly six portrait tiles in a 3 x 2 internal grid.
6. Ensure the full image contains 36 portraits total.

## Prompt construction

Use this template after resolving inputs:

```text
Create a single wide 16:9 poster-style image with a clean, organized layout on a {overall_background} overall background.

The canvas is divided into exactly 6 bordered card sections arranged in 3 columns by 2 rows. Each card section has a thin black outline and a centered name tab at the top, also outlined in black. The section names are fixed and must appear exactly as follows: top row left to right: {names[0]}, {names[1]}, {names[2]}; bottom row left to right: {names[3]}, {names[4]}, {names[5]}.

Inside each of the 6 card sections, place a 3 by 2 grid of portrait images, for a total of 6 portraits per section and 36 portraits overall. Each portrait should be a tightly framed head-and-shoulders avatar portrait in this style: {style}.

Each portrait tile should have its own distinct solid color background. Use a varied palette such as {portrait_background_palette}. Ensure strong variety across the whole image.

Make the portrait subjects highly varied and creative. Apply this diversity direction: {diversity_direction}. Include the following special character types somewhere across the 36 portraits: {special_characters}. Also include a broad accessory and feature mix such as {accessory_mix}.

Keep the overall presentation neat and symmetrical, with clear spacing, clean black borders, centered name tabs, and a polished editorial contact-sheet feel. The image should be crisp, cohesive, and visually balanced.

Hard constraints: exactly 6 sections; exactly 6 name tabs; exactly 36 portraits; no extra text besides the six names; no missing or duplicated sections; no messy collage layout; no cropped-off labels.
```

## Style handling

If `style` is photorealistic, explicitly include: realistic studio lighting, detailed facial features, natural skin texture, realistic clothing materials, crisp lens-like detail, and no pixel art.

If `style` is pixel art, explicitly include: pixelated 24x24 avatar-like faces, hard-edged blocky forms, retro 8-bit look, limited shading, and clean sprite-like portraits.

If `style` is 3D/toy/illustration/anime/cyberpunk/etc., keep the style local to the portraits and overall rendering, but never let it change the six-section grid structure.

## Quality checklist

A good output should satisfy all of these:

- The image reads instantly as a 3 x 2 board of six named sections.
- The six names are visible, centered, and correctly ordered.
- Each section contains a clean 3 x 2 portrait grid.
- The full board has 36 portraits total.
- Every portrait has a distinct solid background color.
- Character variety is obvious at a glance.
- The special character list is represented somewhere in the image.
- Borders are thin, black, and clean.
- The overall background stays light gray/off-white.
- The final result feels organized, polished, and coherent.

## Example invocation

```json
{
  "names": ["Luna", "Peter", "Saul", "Robert", "Zayn", "Meus"],
  "style": "photorealistic studio portraits with a clean retro collectible-card contact-sheet aesthetic",
  "special_characters": ["alien", "zombie-like character", "AI/robot humanoid", "anthropomorphic panda", "monkey/ape character"]
}
```

## Example resolved prompt

```text
Create a single wide 16:9 poster-style image with a clean, organized layout on a light gray / off-white overall background. The canvas is divided into exactly 6 bordered card sections arranged in 3 columns by 2 rows. Each card section has a thin black outline and a centered white name tab at the top, also outlined in black, with bold black text.

The section names are fixed and must appear exactly as follows: top row left to right: Luna, Peter, Saul; bottom row left to right: Robert, Zayn, Meus.

Inside each of the 6 card sections, place a 3 by 2 grid of portrait images, for a total of 6 portraits per section and 36 portraits overall. Each portrait should be a tightly framed head-and-shoulders avatar portrait in a photorealistic studio portrait style with a clean retro collectible-card contact-sheet aesthetic. Use realistic studio lighting, detailed facial features, natural skin texture, realistic clothing materials, crisp lens-like detail, and no pixel art.

Each portrait tile should have its own distinct solid color background. Use a varied palette such as teal, pink, olive, brown, purple, magenta, mustard, orange, cyan, lime, navy, and red. Ensure strong variety across the whole image.

Make the portrait subjects highly varied and creative: varied genders, ages, ethnicities, skin tones, facial expressions, and fashion styles. Include an alien, a zombie-like character, an AI/robot humanoid, an anthropomorphic panda, and a monkey/ape character somewhere across the 36 portraits. Also include a broad accessory and feature mix: crown, cowboy hat, fedora, beanie, round glasses, sunglasses, mohawk, bald head, colorful hair, facial hair, face tattoos, and small facial decorations.

Keep the overall presentation neat and symmetrical, with clear spacing, clean black borders, centered name tabs, and a polished editorial contact-sheet feel. The image should be crisp, cohesive, and visually balanced.

Hard constraints: exactly 6 sections; exactly 6 name tabs; exactly 36 portraits; no extra text besides the six names; no missing or duplicated sections; no messy collage layout; no cropped-off labels.
```
