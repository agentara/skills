# Parenting Memory

Use this reference at the start of every non-urgent Super Daddy session. The goal is to avoid generic advice by maintaining the master baby profile in `~/.super_daddy/parenting.md`. For case files, plans, images, and archiving, use `family-doctor-workflow.md`. If the opening message has obvious emergency red flags, do the emergency bridge first and return to profile updates only after the safety boundary is handled.

This pattern follows the same spirit as interview-first skills: ask until there is shared understanding, ask one question at a time, and do not ask questions that can be answered by reading existing context.

## File Location

Resolve the master profile path in this order:

1. If the user names a path outside `~/.super_daddy/`, require explicit confirmation before using it. Warn if it appears to be inside a repository, synced/cloud folder, public folder, or skill package.
2. Otherwise use `~/.super_daddy/parenting.md`.
3. If `~/.super_daddy/parenting.md` does not exist, create `~/.super_daddy/` and then create `parenting.md` there after telling the user the path.
4. If the user is migrating from an older setup and `parenting.md`, `memory/parenting.md`, `notes/parenting.md`, or `docs/parenting.md` exists in the current working directory, mention it and ask whether to import or ignore it instead of silently merging.

Do not store the profile inside a repository or project workspace by default; baby profile data is private user memory and should not be committed accidentally.

All other runtime files should be categorized under `~/.super_daddy/cases/`, `~/.super_daddy/plans/`, `~/.super_daddy/images/`, `~/.super_daddy/attachments/`, or `~/.super_daddy/archive/`.

## Baby Profile Completeness Gate

For non-urgent requests, the Baby Profile must be complete before Super Daddy starts the structured visit, handling plan, image generation, or routine case archive.

Complete means every required field below has either:

- a caregiver-provided or caregiver-confirmed value;
- `不适用`;
- or `未知（已询问 YYYY-MM-DD）` when the caregiver does not know or chooses not to answer.

Required fields:

- Name/nickname or preferred child label;
- birth date or age/month age;
- corrected age if premature, or `不适用`;
- region/time zone;
- primary caregivers;
- daycare/kindergarten status;
- feeding baseline;
- sleep baseline;
- stool/urine baseline;
- growth data baseline, even if only `未知（已询问 YYYY-MM-DD）`;
- development notes;
- allergies/suspected reactions;
- clinician-diagnosed medical history;
- medicines/supplements currently used;
- vaccination notes;
- main family routines;
- caregiver disagreements or constraints;
- parent goal.

If the profile is incomplete, ask exactly one focused profile question, update `~/.super_daddy/parenting.md`, then check the gate again. Do not move on to routine care planning until the gate is satisfied.

For urgent requests, ask only safety-critical questions and do not delay emergency care to complete the profile.

## First-Time Interview

If there is no usable profile, do not produce a full plan immediately unless the user's request is urgent. Ask one focused profile question at a time until the completeness gate is satisfied.

Start with the missing Baby Profile field that most changes future advice:

1. Child label, birth date or age/month age, and whether premature/corrected age applies.
2. Region/time zone, primary caregivers, and daycare/kindergarten status.
3. Feeding baseline.
4. Sleep baseline and stool/urine baseline.
5. Growth data and development notes.
6. Allergies/suspected reactions.
7. Clinician-diagnosed medical history, current medicines/supplements, and vaccination notes.
8. Main family routines, caregiver constraints/disagreements, and parent goal.

Ask only the missing questions that materially affect the current advice. Do not interrogate the user with a long checklist.

After the profile is complete, start the current visit interview: current concern, duration, current state, and topic-specific context.

## Update Rules

Before writing:

- Say what file will be created or updated.
- Store only facts the caregiver provided or explicitly confirmed.
- Use `未知` for unknown fields. Do not infer sensitive facts.
- Never store diagnosis labels unless the user says a clinician diagnosed it.
- Put stable profile facts in `Baby Profile`, `Baseline`, or `Family Routine`; put current unconfirmed symptoms only in `Observation Log` and the dated case file.
- For health events, write dated summaries, not long transcripts.

After the visit:

- Update baseline fields if new stable facts were provided.
- Add an entry under `## Observation Log` for current concerns, case file path, plan path, review date, and escalation thresholds.
- Add unresolved questions under `## Open Questions`.

## Template

```markdown
# Parenting

Last updated: YYYY-MM-DD

## Baby Profile

- Name/nickname: 未知
- Birth date or age/month age: 未知
- Corrected age if premature: 不适用/未知
- Region/time zone: 未知
- Primary caregivers: 未知
- Daycare/kindergarten: 未知

## Baseline

- Feeding: 未知
- Sleep: 未知
- Stool/urine: 未知
- Growth data: 未知
- Development notes: 未知
- Allergies/suspected reactions: 未知
- Medical history/diagnoses from clinician: 未知
- Medicines/supplements currently used: 未知
- Vaccination notes: 未知

## Family Routine

- Main routines: 未知
- Caregiver disagreements or constraints: 未知
- Parent goals: 未知

## Observation Log

### YYYY-MM-DD - <topic>

- Concern:
- Relevant facts:
- Reference files used:
- Plan summary:
- What to observe:
- Escalation threshold:
- Review date:

## Open Questions

- 
```

## Privacy And Portability

Treat `~/.super_daddy/parenting.md` as user-owned local memory. Do not include private source paths in generated images. If the user asks to share the skill publicly, keep `parenting.md` out of the skill package and out of commits unless the user explicitly wants to publish a redacted sample.
