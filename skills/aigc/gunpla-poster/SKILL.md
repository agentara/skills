---
name: gunpla-poster
description: Create premium collectible Gunpla model-photography posters through a guided, language-aware interview and image-generation workflow. Use this skill whenever a user asks for a Gundam, Gunpla, mobile-suit model, MG, RG, PG, MGEX, or collector-catalog poster, portrait, showcase image, or studio photograph. Ask for the mobile suit, crop, pose, environment, and aspect ratio one at a time, then generate a faithful, polished poster with restrained technical typography.
compatibility: Requires an image-generation tool. Web access is helpful when exact official mobile-suit specifications need verification.
---

# Gunpla Collector Poster

Create a premium Gunpla model-photography poster that feels like an official high-end Gundam collector catalog page.

## Bundled visual references

The four bundled images are composition references, not mobile-suit identity references. Give each image a stable ID so the orchestration model can select it before calling the image model:

| Reference ID | File | Use for | Composition cues |
| --- | --- | --- | --- |
| `BUST-01` | `references/bust-portrait.png` | Bust or half-body portrait | Tight head-and-chest crop, three-quarter face, subject on the left, technical panel on the right |
| `FULL-01` | `references/full-body-weapon-showcase.png` | Grounded full-body pose with a lean or angular silhouette, especially with a long weapon | Entire figure visible, slight three-quarter stance, weapon clearly separated from the body, generous studio space |
| `ACTION-01` | `references/support-stand-combat-pose.png` | Airborne or support-stand combat pose | Visible transparent base and support arm, dynamic articulated silhouette, all remote equipment and weapons kept in frame |
| `FULL-02` | `references/full-body-neutral-showcase.png` | Grounded full-body pose with a bulky, stocky, shield-heavy, or strongly symmetrical silhouette | Entire figure visible, weighty frontal stance, large armor and shield remain readable |

### Reference-selection procedure

After `framing` and `pose` are known, derive one internal field named `visual_reference`. Do not ask the user to choose a reference ID. Apply this decision tree in order and stop at the first match:

1. If `framing` is Bust portrait or Half body, select `BUST-01`.
2. If the pose is Support-stand combat pose, or the user explicitly requests airborne, flying, jumping, lunging, funnel deployment, a visible support arm, or a display base holding the model off the ground, select `ACTION-01`.
3. For a grounded Full body pose, select `FULL-02` when the selected mobile suit is bulky or stocky, has very large armor, a dominant shield, or a mostly frontal symmetrical presentation.
4. For every other grounded Full body pose, select `FULL-01`. This is the default full-body reference when the silhouette does not clearly favor `FULL-02`.

The word “combat” alone does not imply `ACTION-01`: use `ACTION-01` only when the pose is airborne or visibly supported. A grounded ready or combat stance still routes to `FULL-01` or `FULL-02`.

Routing examples:

- Bust portrait + any pose → `BUST-01` → `references/bust-portrait.png`
- Full body + grounded ready stance + Gundam Barbatos with its long mace → `FULL-01` → `references/full-body-weapon-showcase.png`
- Full body + neutral standing + Sazabi with its bulky armor and shield → `FULL-02` → `references/full-body-neutral-showcase.png`
- Full body + airborne funnel-deployment pose on a clear arm → `ACTION-01` → `references/support-stand-combat-pose.png`

Select exactly one bundled composition reference. Using one image makes the intended crop and pose unambiguous to the image model. Resolve its path relative to the directory containing this `SKILL.md`, then pass the resolved absolute path to the image-generation tool as the only bundled item in `referenced_image_paths`.

If the user also supplied an image that must define the mobile suit's identity, pass the user image first and the selected bundled composition reference second. In that case, label them explicitly in the prompt as `Image 1 — identity` and `Image 2 — composition`. Otherwise, label the single bundled image as `Image 1 — composition`.

Use the selected reference only for framing, pose family, studio spacing, lighting hierarchy, and technical-panel placement. Preserve the user's selected mobile suit and never transfer the reference image's armor, colors, weapons, markings, logos, text, or specifications.

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

After the five user-facing fields are complete, derive `visual_reference` using the reference-selection procedure above. This is internal state, not a sixth interview question.

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
- Support-stand combat pose — airborne articulated action on a visible transparent display stand
- Angled showcase — subtle torso and shoulder rotation designed for model photography
- Custom pose — let the user describe it

Keep the pose physically plausible for a premium articulated scale model. A support-stand combat pose may be dynamic, but it should still look like a photographed articulated kit: show a plausible clear base/support arm, preserve joint limits, and keep the silhouette readable. Avoid unsupported floating or cinematic action-scene effects unless the user explicitly requests them.

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
- For a support-stand combat pose, keep the clear display base and support arm visibly connected, frame all major equipment without edge collisions, and retain enough negative space for the technical-information panel.

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

REFERENCE USAGE
[REFERENCE LABEL AND ID]. Use the selected composition reference only for [CROP / POSE FAMILY / STUDIO SPACING / LIGHTING / RIGHT-SIDE INFORMATION-PANEL PLACEMENT]. Do not copy the depicted mobile suit's identity, armor, colors, weapons, markings, text, logos, or specifications. The subject must remain [MOBILE SUIT AND VARIANT].

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

Fill `REFERENCE USAGE` with the selected ID and its intended role. For example, when `ACTION-01` is selected and no user identity image is present:

```text
REFERENCE USAGE
Image 1 — composition reference ACTION-01. Use it for the airborne articulated pose, visible transparent support base and arm, equipment spacing, neutral-gray studio lighting, and right-side information-panel placement only. Do not copy the depicted Nu Gundam identity, armor, colors, weapons, markings, text, logos, or specifications. The subject must remain MG Gundam Barbatos.
```

## Generation and delivery

Use the available image-generation tool once the prompt is ready. Include the selected reference according to the `referenced_image_paths` contract above; do not silently generate without it when local-image referencing is available. If the tool supports an explicit aspect ratio parameter, set it to the user's selection; otherwise state the ratio prominently at the start and end of the prompt.

Return the generated image with a short caption in the user's current language. Mention the chosen mobile suit, framing, pose, environment, and aspect ratio. Do not expose the entire internal prompt unless the user asks for it.

If image generation fails, explain the failure briefly in the user's language and offer to retry with the same saved selections. Do not restart the interview.
