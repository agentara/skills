# Visual Plan Output

Use this reference when Super Daddy produces a non-urgent caregiver action plan. The visual plan is not required for profile-only updates, archive-only work, urgent/emergency cases, or clinician-referral-only responses.

## Required Workflow

1. Confirm the Baby Profile completeness gate in `parenting-memory.md` is satisfied. If incomplete, do not generate an image; continue profile-building instead.
2. Confirm the Visit Clarification Gate in `family-doctor-workflow.md` is satisfied. If incomplete, do not generate an image; continue visit questioning and update the draft case.
3. Read the relevant topic references before planning. Always read `core-principles.md`, then add the topic files needed for the user's concern.
4. Read or create/update `~/.super_daddy/parenting.md` using `parenting-memory.md` so the plan reflects the actual child.
5. Draft a detailed plan in text first so the image has accurate content.
6. Convert the plan into a concise visual layout.
7. Invoke the `imagegen` skill/tool to generate a raster image only if the case is non-urgent and the plan contains caregiver actions.
8. Save or move the final image under `~/.super_daddy/images/YYYY-MM-DD_<topic>_plan.png` when a local file path is available, and record the path in the case file. If no local image path is available, record `Visual plan: generated in conversation, not saved locally`.
9. After generation, give only a short note: what the image contains, whether/where it was saved, any urgent-care caveat, and that the plan is educational rather than diagnosis.

Exceptions: if the request contains urgent red flags or the boundary is emergency care, use `emergency-bridge.md` first and do not generate a routine plan image. If the answer is only building/updating `parenting.md`, organizing files, preparing a clinician visit, or archiving a case, skip image generation unless the user explicitly asks for a visual summary.

## Visual Content

The image should usually include:

- title with child age/context, e.g. `18个月宝宝吃饭计划`;
- one short context line from `~/.super_daddy/parenting.md`, such as age, routine constraint, or current goal;
- boundary badge: `日常调整`, `居家观察`, or `需要医生参与`;
- 3-5 key principles from the loaded references;
- action timeline: `今天`, `3-7天`, `2-4周`;
- observation checklist;
- caregiver teamwork row: father/mother/grandparents or primary caregivers;
- medical escalation box when relevant.
- small footer with the case date or case topic; do not include private filesystem paths in the image itself.

Keep text short enough to be legible in an image. Use Chinese labels. Avoid dense paragraphs.

## Image Prompt Pattern

When calling imagegen, provide a prompt like:

```text
Create a polished Chinese parenting-plan infographic for caregivers.
Format: vertical A4 poster or square share-card, clean editorial infographic, warm but not childish, readable Chinese text, clear sections, icon-like visual hierarchy.
Topic: <child age and concern>.
Reference-grounded principles: <3-5 concise principles from loaded references>.
Plan sections:
- 今天: <3 concise actions>
- 3-7天: <3 concise actions>
- 2-4周: <2-3 concise actions if relevant>
- 观察记录: <checklist>
- 何时就医: <clear escalation threshold, if relevant>
- 家庭协作: <caregiver division of labor>
Style: calm professional pediatric education poster, soft neutral background, accent colors in teal, coral, and warm yellow, simple line icons, no cartoons of doctors making diagnoses, no medicine bottles unless medication was prescribed by a clinician.
Safety note in small footer: 教育建议，不能替代医生诊断；出现红旗信号请及时就医。
No brand logos, no copyrighted characters, no source logos.
```

If imagegen cannot be used in the runtime, provide the complete final image prompt as a fallback and state that image generation was unavailable.

## Safety Constraints

- Do not include medication names, doses, or vaccine schedules in the image unless the user provided an existing clinician instruction and the wording is only "遵医嘱".
- Do not make the poster look like an official hospital or government document.
- Do not present uncertain medical judgments as diagnosis labels.
- Use escalation language such as `联系儿科医生`, `当地急救电话`, `儿科急诊`, or `毒物咨询`, not "不用去医院".
