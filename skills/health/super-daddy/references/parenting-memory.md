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

## First-Time Interview

If there is no usable profile, do not produce a full plan immediately unless the user's request is urgent. Ask one focused question at a time.

For urgent requests, ask only safety-critical questions and do not delay emergency care to complete the profile.

Start with the question that most changes the answer:

1. Child's age/month age or birth date; whether premature and corrected age.
2. Current concern and duration.
3. Current state: eating/drinking, sleep, activity, urine/stool, fever/rash/vomiting/pain/breathing if relevant.
4. Feeding pattern: breastfeeding, formula, complementary foods, appetite, allergies or suspected reactions.
5. Growth/development context: recent height/weight/head circumference if relevant; milestones or caregiver concern.
6. Medical context: known diagnoses, medications, allergies, vaccines, recent clinician instructions.
7. Family routine: primary caregivers, daycare/kindergarten, sleep setup, screen exposure, family disagreement if relevant.
8. Caregiver goal: what outcome would feel useful this week.

Ask only the missing questions that materially affect the current advice. Do not interrogate the user with a long checklist.

Minimum baseline before a full non-urgent plan:

- age/month age and corrected age if premature;
- current concern and duration;
- current state: activity, sleep, eating/drinking, urine/stool, and any fever/rash/vomiting/pain/breathing issue relevant to the question;
- topic-specific context from the profile or one focused follow-up question.

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
