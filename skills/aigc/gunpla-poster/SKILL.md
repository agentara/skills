---
name: gunpla-poster
description: Create premium collectible Gunpla model-photography posters through a guided, language-aware interview and image-generation workflow. Use this skill whenever a user asks for a Gundam, Gunpla, mobile-suit model, MG, RG, PG, MGEX, or collector-catalog poster, portrait, showcase image, or studio photograph. Ask for the mobile suit, crop, pose, environment, and aspect ratio one at a time, then generate a faithful, polished poster with restrained technical typography.
compatibility: Requires an image-generation tool. Web access is helpful when exact official mobile-suit specifications need verification.
---

# Gunpla Collector Poster

Create a premium Gunpla model-photography poster that feels like an official high-end Gundam collector catalog page.

## Language behavior

Write this workflow's user-facing questions, option labels, brief explanations, and final response in the language the user is currently using. If the user changes language, follow the language used in their latest message. Keep proper nouns, model numbers, grades, and official product or mobile-suit names in their canonical form when appropriate.

The skill instructions and the image-generation prompt remain in English. Translate user answers into precise English prompt language internally when helpful, but do not force the user to answer in English.

## Conversation state

Collect these five fields in order:

1. `mobile_suit`
2. `framing`
3. `pose`
4. `environment`
5. `aspect_ratio`

Ask exactly one unanswered question per turn and wait for the user's answer before asking the next one. Briefly acknowledge the selection, then ask the next question. Do not show later questions early.

If the user supplies one or more answers before being asked, save them and do not ask for them again. Continue with the earliest unanswered field. Treat “default,” “recommended,” or its equivalent in the user's language as acceptance of the stated default for the current question.

After the fifth field is known, generate the poster immediately. Do not ask for confirmation unless an essential answer is genuinely ambiguous.

## Guided interview

### Question 1 — Mobile suit

Ask which Gunpla or Gundam the user wants. Offer at least five concrete candidates, all represented as MG-class or higher-end collector builds. Always allow the user to enter another mobile suit or an exact kit/grade.

Use a concise selection such as:

- RX-78-2 Gundam — MG 3.0
- Nu Gundam — MG Ver.Ka
- Sazabi — MG Ver.Ka
- Unicorn Gundam — MGEX
- Wing Gundam Zero EW — MG Ver.Ka
- Freedom Gundam — MG 2.0
- Gundam Barbatos — MG
- Strike Freedom Gundam — MGEX

State that the default assumption is MG or a higher-end build. When the user names only a mobile suit, choose the most suitable MG-or-higher collector interpretation without changing the canonical design. If the requested suit has no literal MG-or-higher retail kit, render it with premium master-grade model craftsmanship while preserving the official design; do not falsely claim that a nonexistent retail kit exists.

### Question 2 — Framing

Ask the user to choose one:

- Bust portrait — head, chest armor, and shoulders; recommended for maximum mechanical detail
- Half body — approximately waist-up, balancing detail and silhouette
- Full body — complete mobile-suit figure with a tighter collector showcase composition

Use `Bust portrait` when the user chooses the default without naming an option.

### Question 3 — Pose

Ask the user to choose one:

- Neutral standing — default; calm, authoritative museum-display stance
- Heroic standing — chest slightly lifted with a stronger three-quarter turn
- Ready stance — restrained combat readiness without an action-scene look
- Angled showcase — subtle torso and shoulder rotation designed for model photography
- Custom pose — let the user describe it

Keep the pose physically plausible for a premium articulated scale model. Avoid exaggerated animation, floating, or action-scene effects unless the user explicitly requests them.

### Question 4 — Environment

Ask the user to choose one:

- Studio Grey — default; seamless light neutral-gray premium photography studio
- Hangar / garage bay — clean, restrained maintenance architecture
- Maintenance gantry — precise technical support structures around the model
- Collector display stand — premium base or support arm, minimally visible
- Custom environment — let the user describe it

Studio Grey should remain the visual benchmark: light neutral gray, refined, coherent across a series, and neither pure white nor black. For other choices, keep the setting subordinate to the Gunpla and avoid clutter.

### Question 5 — Aspect ratio

Ask this last. Offer:

- 2:3 portrait — default and recommended collector-poster format
- 3:4 portrait — slightly broader editorial page
- 4:5 portrait — compact social and print format
- 9:16 portrait — tall mobile-first poster
- 1:1 square — catalog tile or cover
- Custom ratio — let the user specify it

Use `2:3 portrait` when the user chooses the default without naming an option.

## Design priorities

Build the final image around these priorities, in order:

1. Canonical mobile-suit identity and silhouette
2. Premium physical Gunpla realism
3. Strong model-photography composition
4. Clean technical catalog graphics
5. Series consistency

Adapt the composition to the selected framing:

- For a bust portrait, use a three-quarter facial angle and emphasize the head, V-fin or antenna, faceplate, eyes, chest armor, shoulder armor, panel separation, and mechanical detail.
- For a half-body portrait, preserve the head-and-torso emphasis while showing the waist and arm articulation clearly.
- For a full-body portrait, keep the entire model legible, preserve realistic model proportions, and avoid making it resemble a full-scale robot or a game render.

## Canonical accuracy

Faithfully reproduce the selected mobile suit's official head, antenna or V-fin, faceplate, eye shape, chest armor, shoulder armor, color blocking, vents, emblems, and signature structures. Do not redesign, kitbash, add original armor, invent weapons, or mix in parts from other mobile suits.

Use the requested kit or grade as a craftsmanship and detailing reference, but do not import features from a different variant. Distinguish variants carefully, such as Ver.Ka, EW, Destroy Mode, Full Armor, or specific color editions.

When exact model numbers, faction names, or technical specifications are uncertain, verify them using authoritative official sources if web access is available. If verification is unavailable, omit uncertain numeric specifications rather than inventing them.

## Material and photography direction

Render the subject as a real, meticulously assembled collectible plastic model photographed in a professional studio:

- Clean, even paint application with subtle material variation
- Crisp panel lines and part separation
- Fine, correctly scaled water-slide decals
- Realistic plastic, painted, metallic, and clear-part responses
- Controlled micro-surface detail without grime
- Convincing scale-model proportions and articulation
- Premium catalog-level finish
- Professional key, fill, and rim lighting that reveal armor layering
- Sharp focus on the face and major armor details, with restrained optical depth of field

Avoid battle damage, weathering, rust, dust, scratches, chipped paint, stains, heavy bloom, excessive lens flare, toy-like plastic, cheap product-shot styling, anime cel shading, video-game CGI, concept-art rendering, full-scale live-action robot scale, or a busy cinematic battlefield.

## Technical information layout

Place a restrained technical-information column on the right side when the composition permits. Include:

- Mobile-suit name
- Model number
- Faction or affiliation
- A small set of verified specifications or concise equipment facts

Use a low-saturation palette derived from the mobile suit's theme colors and faction identity. Keep typography, rules, insignia, and logo treatment elegant, minimal, and secondary to the model. Preserve generous negative space and a premium editorial grid.

Prefer short, legible labels. Image models may struggle with dense text, so do not fill the panel with paragraphs or unverified microcopy. Never invent an official logo. Use a restrained typographic wordmark or neutral technical insignia when a verified official mark is unavailable.

For a nonportrait or especially tight ratio, adapt the right-side column into the clearest available side panel without covering the mobile suit. Preserve the user's selected ratio rather than forcing a 2:3 crop.

## Image-generation prompt

After collecting all five answers, construct a self-contained English prompt using this structure:

```text
Create a premium collectible Gunpla model-photography poster of [MOBILE SUIT / EXACT KIT], in [ASPECT RATIO].

SUBJECT AND ACCURACY
Faithfully reproduce the canonical official design of [MOBILE SUIT AND VARIANT]: exact head, V-fin or antenna, faceplate, eyes, chest armor, shoulder armor, vents, color blocking, emblems, and signature mechanical structures. Do not redesign, kitbash, or mix elements from any other mobile suit. Present it as a meticulously assembled [GRADE / COLLECTOR INTERPRETATION] scale model, not a full-scale robot.

COMPOSITION
[FRAMING-SPECIFIC DESCRIPTION]. Use a three-quarter view where compatible with the selected pose. Pose: [POSE]. Prioritize facial identity, armor layering, panel separation, decals, and realistic model articulation.

MATERIAL AND LIGHTING
High-end physical Gunpla realism, clean precision paint, crisp panel lines, fine water-slide decals, subtle plastic and painted-material response, premium collector finish. Professional studio key, fill, and rim lighting, controlled highlights, sharp focus on the face and primary armor, restrained optical depth of field.

ENVIRONMENT
[ENVIRONMENT DESCRIPTION]. Keep the background coherent, refined, uncluttered, and secondary to the model.

GRAPHIC DESIGN
Add a restrained technical-information panel on the right with the verified mobile-suit name, model number, faction or affiliation, and a few concise verified specifications or equipment facts. Use elegant low-saturation typography and graphic accents derived from the suit's theme colors and faction style. Maintain generous negative space and an official premium collector-catalog layout. Keep text sparse and legible; do not invent official logos or specifications.

NEGATIVE CONSTRAINTS
No original redesign, no kitbash, no parts from other mobile suits, no incorrect signature geometry, no battle damage, no weathering, no rust, no dust, no scratches, no chipped paint, no grime, no cheap toy appearance, no anime cel shading, no video-game CGI, no concept-art look, no battlefield, no explosions, no heavy bloom, no excessive lens flare, no cluttered background, no illegible dense text, no pure-white or pure-black background unless explicitly requested.
```

Make the prompt concrete rather than leaving bracketed placeholders. Include only verified technical facts.

## Generation and delivery

Use the available image-generation tool once the prompt is ready. If the tool supports an explicit aspect ratio parameter, set it to the user's selection; otherwise state the ratio prominently at the start and end of the prompt.

Return the generated image with a short caption in the user's current language. Mention the chosen mobile suit, framing, pose, environment, and aspect ratio. Do not expose the entire internal prompt unless the user asks for it.

If image generation fails, explain the failure briefly in the user's language and offer to retry with the same saved selections. Do not restart the interview.
