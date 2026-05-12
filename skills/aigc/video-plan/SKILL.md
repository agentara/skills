---
name: video-plan
description: Plan short-form video, vlog, travel, lifestyle, documentary, or cinematic social video scripts by negotiating duration, choosing a story arc and visual style, then splitting the film into timed scenes of 4-15 seconds. Use this skill whenever the user asks for a video plan, short video plan, scene breakdown, montage plan, travel video script, TikTok/Reels/Shorts storyboard, or cinematic short-form narrative, even if they only describe a loose theme or destination.
---

# Video Plan

Use this skill to turn a user's short-film idea into a practical, scene-by-scene production plan. The plan should be useful for shooting, editing, AI video generation, or communicating with a photographer/editor.

The final plan should be written in the user's preferred local language. If the user writes in Chinese, output the plan in Chinese unless they explicitly ask for another language. Keep the skill instructions in English, but adapt the deliverable language to the user.

## Primary Goals

Create a complete short-video plan that:

- Negotiates or infers the total duration.
- Splits the video into scenes, where each scene is at least 4 seconds and no more than 15 seconds.
- Prefer scene durations of 4, 9, 12, or 15 seconds when practical.
- Uses a recognizable story arc, such as 起承转合, setup-conflict-turn-resolution, three-act structure, or hook-build-payoff.
- Recommends several style directions and chooses one based on the user's preference.
- Defines a coherent visual tone using references from photography styles, directors, films, or creator aesthetics.
- Includes shot type, scene description, character action, wardrobe suggestions, scenery/prop details, and editing rhythm for every scene.

## First Response Workflow

When a user asks for a video or short-film plan, first extract any constraints they already gave:

- Topic or title
- Intended platform and aspect ratio
- Total duration
- Destination or setting
- Characters
- Voiceover or dialogue
- Emotional goal
- Target audience
- Required locations, props, brands, or products
- Preferred language
- Available footage versus plan for future shooting

If essential details are missing, ask concise questions before writing the final plan. Do not over-interview. Ask only what materially changes the result.

Ask about total duration unless the user already provides one. Offer practical defaults:

- 30 seconds: fast, high-density social cut
- 45 seconds: compact narrative with breathing room
- 60 seconds: standard cinematic story arc
- 90 seconds: more reflective, travel-documentary pacing

If the user does not answer and wants you to proceed, choose 60 seconds by default.

## Duration Rules

Every scene must obey:

- Minimum scene duration: 4 seconds
- Maximum scene duration: 15 seconds
- Preferred durations: 4, 9, 12, 15 seconds

After choosing or confirming total duration:

1. Estimate the average scene length.
2. Calculate the approximate scene count.
3. Adjust scenes so the total duration exactly matches the target duration when possible.
4. If exact matching is awkward, explain the closest practical total and why.

Examples:

- 30 seconds: 5 scenes x 6 seconds, or 4 scenes using 9+9+8+4
- 45 seconds: 5 scenes x 9 seconds
- 60 seconds: 6-8 scenes, commonly 4+9+12+9+9+12+5 or 4 scenes x 15 seconds
- 90 seconds: 8-10 scenes, often built from 9, 12, and 15 second blocks

## Story Arc Planning

Use a clear narrative arc before writing scenes. Prefer 起承转合 when the user is Chinese-speaking or asks for an emotional/travel story:

- 起: Hook, premise, emotional question, or first visual image.
- 承: Expand the world, establish routine, relationship, place, or desire.
- 转: Contrast, complication, emotional turn, unexpected detail, fatigue, doubt, memory, or realization.
- 合: Resolution, return, answer, image of completion, or quiet aftertaste.

For more commercial or platform-native content, use:

## Style Consultation

Before the final plan, recommend 3-5 style directions unless the user already has a clear style. Keep them concrete and selectable.

Useful style directions:

- Cinematic travel essay: restrained, reflective, natural light, voiceover-led.
- Handheld diary vlog: intimate, imperfect, observational, close to the body.
- Editorial city montage: graphic compositions, faster cuts, architecture, street detail.
- Filmic romance travel: soft light, lingering gestures, warm human details.
- Outdoor documentary: wide landscapes, physical movement, weather, terrain, effort.
- Minimal luxury travel: clean compositions, slow pacing, texture, quiet service details.
- High-energy social cut: fast transitions, rhythmic inserts, bold location changes.

If the user has not chosen, recommend one and state the reason. Do not block progress unless the style choice is critical.

## Visual Tone References

Recommend visual tone using practical references. Do not imitate living artists too narrowly; use references as broad tonal anchors.

Possible photography references:

- Natural-light film photography
- Japanese street photography
- National Geographic-style environmental travel
- Fujifilm documentary color
- Kodak Portra warm skin tones
- Muted rainy-day city palette
- Golden-hour backlight
- Blue-hour urban neon

Possible director/film references:

- Wong Kar-wai: urban longing, saturated night color, reflective mood
- Hirokazu Kore-eda: quiet domestic realism, gentle observation
- Sofia Coppola: soft alienation, restrained luxury, drifting mood
- Terrence Malick: lyrical nature, backlight, movement through landscape
- Before Sunrise / Before Sunset: walking conversation, romantic naturalism
- Lost in Translation: foreign-city solitude, hotel interiors, neon melancholy
- Nomadland: open landscapes, human-scale realism, dusk light

Use references responsibly: describe the visual grammar rather than claiming to reproduce a person's exact style.

## Required Output Structure

Use this structure for the final plan. Translate headings into the user's preferred language when appropriate.

```markdown
# [Short Film / Video Title]

## Core Assumptions

- Total duration: [N seconds]
- Average scene duration: [N seconds]
- Number of scenes: [N]
- Platform/aspect ratio: [e.g. 16:9, 9:16, 1:1]
- Language: [plan language and voiceover language if relevant]
- Characters: [brief description]

## Style Direction

- Recommended style: [style name]
- Why it fits: [1-2 sentences]
- Visual tone references: [photography/director/film references]
- Color and light: [palette, contrast, time of day]
- Camera language: [handheld/stabilized/drone/static/long lens, etc.]

## Story Arc

Choose the right story arc for the user's story.

For example, the famous "起承转合" story arc is:

- 起: Hook, premise, emotional question, or first visual image.
- 承: Expand the world, establish routine, relationship, place, or desire.
- 转: Contrast, complication, emotional turn, unexpected detail, fatigue, doubt, memory, or realization.
- 合: Resolution, return, answer, image of completion, or quiet aftertaste.

## Scene Timeline

| Scene Index | Timecode | Duration | Arc Beat | Shot Type | Scene Description | Character Action | Wardrobe | Scenery & Props | Editing Rhythm |
| --- | --- | ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | 00:00-00:04 | 4s | Hook | [shot type] | [description] | [action] | [clothing] | [details] | [rhythm] |
| 2 | 00:04-00:09 | 5s | Build | [shot type] | [description] | [action] | [clothing] | [details] | [rhythm] |
| 3 | 00:09-00:15 | 6s | Turn | [shot type] | [description] | [action] | [clothing] | [details] | [rhythm] |
| 4 | 00:15-00:20 | 5s | Payoff | [shot type] | [description] | [action] | [clothing] | [details] | [rhythm] |

## Voiceover / On-screen Text Suggestions

[Optional. Include if useful. Provide lines matched to time ranges.]

## Shooting Notes

- [Practical advice for coverage, sound, transitions, weather, continuity, or pickups.]

## Edit Notes

- [Music, pacing, transition, sound design, color grade, and ending treatment.]
```

## Scene Detail Requirements

For every scene, include:

- Shot type: drone, telephoto, wide, super-wide, medium, close-up, insert, POV, tracking, static, handheld, gimbal, low angle, overhead, or macro.
- Scene description: what the viewer sees and where the scene happens.
- Character action: what each visible person does; avoid vague posing.
- Wardrobe suggestion: color, texture, layers, and practical reason.
- Scenery and prop details: background, weather, objects, vehicles, food, luggage, camera, phone, tickets, maps, local signs, etc.
- Editing rhythm: hold, slow push, match cut, quick inserts, sound bridge, jump cut, montage, crossfade, hard cut, slow motion, speed ramp, or natural sound pause.

Avoid generic filler such as "beautiful scenery" or "the character walks around." Replace it with specific observable details.

## Voiceover Guidance

If the user wants narration, draft concise voiceover lines that fit the timeline. Keep each line short enough to speak naturally within the scene duration.

For emotional travel videos:

- Start with a question or concrete image.
- Avoid overexplaining the moral.
- Let the final line land softly and specifically.

For commercial or product videos:

- Clarify the offer or transformation early.
- Make product/service moments visible, not only verbal.
- End with a concrete action or memorable image.

## Quality Checklist

Before finalizing, verify:

- Every scene is between 4 and 15 seconds.
- Preferred durations are used when practical.
- The scene durations add up to the stated total or the variance is explained.
- The story arc is explicit and coherent.
- The first scene contains a hook.
- Each scene has shot type, description, action, wardrobe, scenery/props, and editing rhythm.
- Visual tone references are practical and not merely name-dropping.
- The output language matches the user's preferred local language.
- The plan is actionable for shooting or editing, not only conceptual.

## File

Save your final plan to a file called `video-plan.md` in the `plans/` directory.
