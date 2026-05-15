---
name: soviet-storybook-grotesque
description: Transform a user-provided photo or image into a strange vintage Soviet or Eastern European children's book illustration with grotesque humorous cartoon energy, shaky ink, faded watercolor, dirty paper texture, awkward anatomy, nervous absurd expressions, sparse composition, and an absurd handwritten English rhyme. Use this skill when the user asks to turn a photo into an unsettling old children's book illustration, 1980s Eastern European illustration, weird Soviet cartoon book art, grotesque watercolor storybook art, or clumsy absurd illustrated caption style. Do NOT trigger for polished fantasy art, cute children's illustration, modern vector art, realistic portraits, anime, clean editorial illustration, or generic vintage filters.
---

# Soviet Storybook Grotesque

Transform the user's photo into a deliberately awkward, funny, slightly unsettling old-print children's book illustration.

## Workflow

1. Check for a source photo or image. If none is present, ask the user to provide one.
2. Identify only the visual anchors needed from the photo: subject count, broad pose, main action, key clothing, props, and obvious setting.
3. Use an image-generation or image-editing model with the photo as the visual reference. Preserve the source's basic subject roles and composition, but stylize aggressively.
4. Add a short absurd English caption inside the image unless the user explicitly asks for no text. Make it clumsy, handwritten, confusingly rhymed, and only loosely related to the image.
5. Review the result against the negative constraints. If it looks polished, cute, modern, realistic, decorative, or too detailed, regenerate or revise toward roughness and emptier space.

## Style Recipe

Use these ingredients directly in the image prompt:

- Thin shaky black ink lines, careless sketchy linework, uneven contours, and old-print roughness.
- Awkward anatomy, elongated limbs, weird proportions, stiff hands, uncomfortable facial expressions, and nervous absurd body language.
- Grotesque humorous cartoon energy: ridiculous rather than adorable, tense rather than cozy.
- Pale faded watercolor washes, washed-out muted colors, uneven coloring, dirty paper texture, and slightly misregistered print texture.
- Sparse composition with lots of empty paper space.
- Minimal random background details: small strange doodles, crooked objects, loose marks, stray patterns, or irrelevant tiny props.
- An authentically old Eastern European children's book illustration feeling from the 1980s, without referencing a specific living artist.

## Caption Direction

Write one or two short lines of absurd English. It should rhyme imperfectly, feel confused, and be slightly related to the image without explaining it.

Examples of caption logic:

```text
The uncle ate thunder, the teapot said soon,
my left shoe saluted a boiled little moon.
```

```text
Three knees for breakfast, one hat for the rain,
the window forgot how to whisper again.
```

Render the caption as part of the illustration: clumsy handwritten letters, uneven baseline, shaky spacing, imperfect ink, and no clean digital typography. If exact text is important and the image model cannot render it reliably, generate the artwork with a blank caption area, then add the caption afterward with an image-editing tool while matching the rough handwritten style.

## Negative Constraints

Avoid:

- Cute, charming, polished, cozy, pretty, glossy, aesthetic, or modern results.
- Realistic rendering, photographic texture, cinematic lighting, high detail, smooth anatomy, clean faces, or professional character-design polish.
- Slick vector art, anime, Pixar-like style, clean children's book cuteness, clean poster design, decorative maximalism, or saturated modern palettes.
- Dense backgrounds. Keep the environment minimal, strange, and loose.
- Faithful beauty retouching. The transformation should be strange, absurd, nervous, and intentionally clumsy.

## Prompt Template

```text
Transform the attached photo into a strange vintage Soviet / Eastern European children's book illustration from the 1980s. Preserve the basic subject count, pose, action, and key props from the photo, but redraw everything as an intentionally clumsy grotesque cartoon.

Use thin shaky black ink lines, awkward anatomy, elongated limbs, weird proportions, stiff hands, nervous uncomfortable facial expressions, chaotic movement, and ridiculous absurd energy. Make it funny and slightly unsettling rather than cute. Use pale faded watercolor washes, dirty yellowed paper texture, uneven coloring, washed-out muted colors, rough old-print texture, careless sketchy linework, and lots of empty space.

Keep the background minimal and random, with a few small strange doodles or crooked irrelevant details. Do not make it polished, aesthetic, modern, cute, detailed, realistic, glossy, cinematic, anime, vector, or clean.

Add a clumsy handwritten English caption inside the illustration: "[ABSURD RHYMING CAPTION]". The lettering should look shaky, uneven, and hand-drawn as part of the old illustration.
```
