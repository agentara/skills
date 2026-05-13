# The /goal Mega Prompt Template

For complex, long-running tasks where you want maximum autonomy and zero hand-holding.
Credit: @aiedge_

---

```
/goal [THE FINAL OUTCOME — what "done" looks like in one line]

— CONTEXT —
· Project: [what you're building]
· Stack: [languages, frameworks, infra]
· Current state: [what exists today]
· Working dir: [path or repo]
· Constraints: [budget, time, off-limits items]
· Audience: [who this is for]

— SUCCESS CRITERIA (ALL MUST BE TRUE) —
1. [Specific measurable outcome]
2. [Specific measurable outcome]
3. [Specific measurable outcome]
4. Final deliverable runs without errors
5. You can show proof (screenshot · test output · URL)

— OPERATING RULES — NON-NEGOTIABLE —
1. PLAN FIRST. Output a numbered task list before writing any code.
2. WORK AUTONOMOUSLY. Don't ask clarifying Qs unless genuinely blocked.
3. SELF-VERIFY. After every step: run tests, inspect output, confirm it worked.
4. DEBUG YOURSELF. If it fails, diagnose + fix. Don't hand it back.
5. USE EVERY TOOL. MCPs · terminal · web · code exec · pull real data.
6. NO PLACEHOLDERS. No TODOs · no stubs · real components + real states.
7. PROGRESS LOG. Track completed · in-flight · decisions · blockers.
8. STAY ON GOAL. Discoveries off-spec? Note + keep moving.
9. IF BLOCKED. Log the wall · continue everything parallelizable.
10. CHECK SUCCESS BEFORE STOPPING. Re-read criteria · confirm each is met.

— QUALITY BAR —
· Code: clean, typed, follows project conventions
· Design: looks like a well-funded startup shipped it
· Output: survives a senior code review
· Docs: every new pattern / env var / decision logged

— FINAL DELIVERABLE —
✅ Confirmation each criterion is satisfied
📋 Every file created / modified
🚀 How to run / test / deploy
📊 Proof (screenshot · test output · URL)
📝 Decisions made + anything to know
⚠️ Known limitations + follow-ups

Begin by outputting your plan. Then execute end-to-end without checking in
until done or genuinely blocked.
```

---

## Filling in the template

**`/goal` line** — one declarative sentence the evaluator can judge. Make it falsifiable.
```
# Weak:
/goal the app is working

# Strong:
/goal the FastAPI service passes all tests in tests/, serves /health with 200, and docker build succeeds
```

**CONTEXT** — paste what the agent needs to orient itself. Don't assume it knows your repo structure or conventions.

**SUCCESS CRITERIA** — write 3–5 conditions that are individually checkable. Each should map to a command output or visible artifact the agent can produce as proof.

**OPERATING RULES** — keep as-is for most tasks. Override only for specific constraints:
- "don't use the internet" → modify rule 5
- "always ask before committing" → add as rule 11
- backend-only task → drop the design line from QUALITY BAR

**FINAL DELIVERABLE** — the agent produces this checklist at the end. The evaluator uses it to confirm completion.
