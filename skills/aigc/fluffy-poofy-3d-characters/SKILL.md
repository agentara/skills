---
name: fluffy-poofy-3d-characters
description: Generate original fluffy, poofy 3D animation characters in a cohesive collectible-avatar family: monolithic plush body, inset smooth face, tiny limbs, restrained expression, tactile materials, strong silhouettes, and high variation without losing the shared design language.
---

# Fluffy & Poofy 3D Characters

Use this skill whenever the user asks to create, vary, expand, or art-direct characters in this avatar family.

## Core Design Language

**One-line rule:** monolithic poofy body + smooth inset face + tiny limbs + restrained expression + tactile plush material + unmistakable silhouette.

### 1. Silhouette
- One dominant rounded body mass; head and torso often merge into one shape.
- Short, heavy, simplified limbs; no anatomical fingers or toes unless specifically requested.
- A character must remain recognizable as a solid silhouette.
- Proportions should feel toy-like and huggable rather than human or mascot-costume realistic.

### 2. Face Architecture
- Face is a clean, smooth, matte panel embedded inside the fuzzy body, like a small opening in a plush shell.
- Keep the face visually quieter than the body.
- Default features: two small black dot eyes, tiny curved mouth, subtle blush, no visible nose.
- Expressions are calm and low-amplitude; avoid exaggerated emoji faces.

### 3. Material Contrast
- Body: dense short fur, fleece, velvet, boucle, shag, or another tactile soft surface.
- Face: smooth matte material with warm skin/ivory tone.
- The contrast between fuzzy shell and clean face is a defining feature.
- Avoid glossy plastic CGI, hard rubber, or metallic toy surfaces unless explicitly requested.

### 4. Shape Language
- Rounded, continuous, low-detail geometry.
- No sharp mechanical segmentation.
- Ears, horns, tails, fins, antennae, sprouts, wings, etc. should be simplified into soft toy-like primitives.
- Species inspiration is allowed, but the result should feel like its own creature rather than a literal animal costume.

### 5. Color
- Soft, coherent palettes: cream, oatmeal, muted brown, dusty pink, sage, pale blue, lavender, warm yellow, charcoal, muted terracotta.
- Stronger colors are allowed as accents, not as neon lighting.
- Keep the face slightly warmer and smoother than the body.

### 6. Rendering
- Premium 3D animation / collectible-plush quality.
- Soft diffused studio light, subtle ambient occlusion, gentle floor shadow.
- Clean white or very light neutral background by default.
- Front-facing or small natural pose variation; avoid dramatic camera distortion.
- No text unless requested.

## Variation Rules

When generating multiple characters, make **each character structurally different**, not just recolored.

Vary across these axes:
- silhouette: tall, squat, pear-shaped, egg-shaped, wide, narrow, top-heavy, bottom-heavy
- fur: short plush, long fluffy, shaggy, boucle, velour, curly wool
- face opening: rounded rectangle, oval, arch, bean, shallow trapezoid, asymmetric soft cutout
- appendages: rounded ears, floppy ears, horns, antennae, fins, tiny wings, tail, sprout, mane
- proportions: face-to-body ratio, limb length, shoulder width, belly size, leg spacing
- motifs: stripes, spots, belly patch, gradient, seasonal detail, tiny scarf, bow, hood nub
- expression: neutral smile, sleepy, curious, shy, content, surprised-but-subtle

Do **not** create 36 near-identical bodies with different animal ears. Change the underlying body architecture too.

## Generation Workflow

1. Read the user's requested count, aspect ratio, grid, subject, and variation constraints.
2. Use `assets/reference-avatar.png` as the primary design-language reference.
3. If available, use `assets/character-grid.png` only as a diversity reference, not as a set to copy.
4. Build a variation plan before generation so neighboring characters do not repeat silhouette, species cue, color, or accessory.
5. Generate with image generation using the reference image(s).
6. Inspect the result for:
   - correct number of characters
   - unique silhouettes
   - consistent face architecture
   - fuzzy-shell / smooth-face contrast
   - no duplicated characters
   - no malformed limbs or accessories
   - no text artifacts
   - cohesive lighting and scale
7. If diversity is weak, regenerate with stronger structural variation rather than adding random accessories.

## Default Prompt Block

Use this wording as the base and adapt it to the user's request:

> Create original premium 3D animation characters in one coherent collectible family. Each character has a monolithic rounded plush body, a small smooth matte face panel embedded inside the fuzzy shell, tiny simplified limbs, restrained dot-eye facial features, subtle blush, tactile soft materials, and a strong readable silhouette. Keep geometry low-detail, rounded, and huggable. Every character must be structurally unique through silhouette, proportions, fur treatment, face-opening shape, appendages, motifs, and color—not merely recolored. Preserve a consistent design language across the entire set. Use soft diffused studio lighting, subtle contact shadows, and a clean white or very light neutral background. Avoid glossy CGI, literal mascot costumes, over-detailed anatomy, exaggerated emoji expressions, generic kawaii duplication, neon gradients, text, and AI-slop artifacts.

## Grid Defaults

For character-sheet requests:
- default to a strict equal-cell grid
- exactly one character per cell
- full body visible
- consistent visual scale
- generous breathing room
- light or invisible separators
- no labels unless requested

For 36 characters, use a strict **6 × 6** grid.

## Negative Direction

Avoid:
- generic Funko-like vinyl heads
- chibi human proportions
- literal furry animal suits
- big anime eyes
- oversized mouths
- glossy plastic or clay-only look
- hard-surface mecha details
- random accessories used as the only source of uniqueness
- repeated identical body meshes
- excessive rainbow/neon palettes
- fake text, watermarks, or UI
- over-rendered cinematic backgrounds unless requested
