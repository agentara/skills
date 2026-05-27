# Family Doctor Workflow

Use this reference for the end-to-end Super Daddy flow: build profile -> structured visit -> handling plan -> case archive.

Super Daddy uses a family-doctor-style continuity model, but it is not a licensed doctor. Records are caregiver-owned notes for continuity, observation, and clinician preparation.

## Directory Layout

All runtime files belong under `~/.super_daddy/` by default.

```text
~/.super_daddy/
  parenting.md                 # master baby profile and longitudinal summary
  cases/
    index.md                   # case index
    YYYY-MM-DD_<topic>.md      # one case per visit/concern
  plans/
    YYYY-MM-DD_<topic>_plan.md # detailed text plan
  images/
    YYYY-MM-DD_<topic>_plan.png # imagegen output or copied final image when locally available
  attachments/
    YYYY-MM-DD_<topic>/        # user-provided photos, screenshots, reports if any
  archive/
    YYYY/                      # old closed cases, if the user asks to archive
```

Create missing directories before writing. Do not put these files inside the skill package or a repository unless the user explicitly gives that path.

## Stage 1: 建档

Goal: know who the child is before giving advice.

Actions:

- read `~/.super_daddy/parenting.md` if it exists;
- create it from the template in `parenting-memory.md` if missing;
- ask one focused question at a time when essential facts are missing;
- update only user-provided or confirmed facts;
- use `未知` rather than guessing.

Minimum baseline:

- child age/month age and corrected age if premature;
- current concern and duration;
- current state: activity, eating/drinking, sleep, urine/stool, and symptom-specific state;
- relevant feeding/sleep/growth/allergy/medical/routine context.

## Stage 2: 看病

Run a structured visit before planning:

- chief concern in caregiver words;
- timeline: start, trend, triggers, what changed today;
- current state: activity, appetite/drinking, sleep, urine/stool, pain, rash, fever, vomiting, breathing when relevant;
- red-flag check;
- what caregivers already tried and whether a clinician has given instructions;
- family/routine context that affects execution.

If red flags are present, stop routine workflow and use `emergency-bridge.md`. Do not wait to finish file updates.

## Stage 3: 给处理办法

For non-urgent cases:

- load relevant topic references before planning;
- say the boundary: routine, home observation, clinician care, or emergency care;
- if the boundary is emergency care, stop routine workflow and use `emergency-bridge.md` instead of producing a visual plan;
- give a practical plan for now/today, 3-7 days, and 2-4 weeks when relevant;
- define what to observe and when to review;
- define escalation thresholds;
- include caregiver division of labor;
- generate a visual plan image with `imagegen` using `visual-plan-output.md` when there is a non-urgent caregiver action plan.

Do not diagnose, prescribe, dose medicines, create vaccine schedules, or recommend home oral food challenges.

## Stage 4: 病例&归档

After the plan:

1. Update `~/.super_daddy/parenting.md` with stable facts and a dated observation-log summary.
2. Write a case file under `~/.super_daddy/cases/YYYY-MM-DD_<topic>.md`.
3. Write the detailed text plan under `~/.super_daddy/plans/YYYY-MM-DD_<topic>_plan.md`.
4. Save or move the imagegen final image under `~/.super_daddy/images/YYYY-MM-DD_<topic>_plan.png` when possible. If the runtime only returns a conversation image with no local file path, record `Visual plan: generated in conversation, not saved locally` in the case file and do not claim a saved path.
5. Update `~/.super_daddy/cases/index.md` with case title, date, status, and file links.

Use ASCII slugs for filenames. Keep Chinese text inside files.

Fact handling:

- Stable profile facts belong in `parenting.md` under `Baby Profile`, `Baseline`, or `Family Routine`.
- Current caregiver observations and uncertain symptoms belong in the dated case file and `Observation Log`, not as permanent profile facts.
- Diagnosis labels belong in `parenting.md` only when the caregiver says a clinician diagnosed them.

## Case File Template

```markdown
# YYYY-MM-DD - <topic>

Status: open/follow-up/closed
Child: <nickname or unknown>, <age/month age>
Created: YYYY-MM-DD
Last updated: YYYY-MM-DD

## Chief Concern

-

## Timeline

-

## Current State

- Activity:
- Eating/drinking:
- Sleep:
- Urine/stool:
- Temperature/rash/vomiting/pain/breathing if relevant:

## Red-Flag Check

-

## Relevant Profile Context

-

## References Used

-

## Boundary Judgment

- Routine parenting / home observation / clinician care / emergency care:

## Handling Plan

- Now/today:
- 3-7 days:
- 2-4 weeks:
- Caregiver division:

## Observe And Review

- Observe:
- Review date:
- Escalation thresholds:

## Outputs

- Text plan:
- Visual plan:
- Attachments:

## Archive Notes

-
```

## Case Index Template

```markdown
# Super Daddy Case Index

| Date | Topic | Status | Case File | Plan | Image |
| --- | --- | --- | --- | --- | --- |
```
