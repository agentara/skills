---
name: meta-goal-prompt
description: Generate a /goal mega prompt for Claude Code or Codex CLI by interviewing the user about their task. Use when the user wants to define a long-horizon autonomous goal — migration, refactor, feature build, optimization loop, test fixing, research project, learning system, or any task where the agent should run end-to-end without hand-holding. Trigger on: "help me write a goal", "I want Claude to keep working until...", "run this autonomously", "set a /goal", or any request that implies sustained agentic execution toward a non-trivial outcome. The skill conducts a structured interview (one question at a time) to extract outcome, context, success criteria, constraints, and quality bar — then outputs a filled-in mega prompt ready to paste into Claude Code or Codex.
---

# Meta-Goal Prompt Generator

Interview the user about their task, one question at a time, until you have everything needed to fill in the `/goal` mega prompt template. Then output the completed prompt.

## The Mega Prompt Template

Read `references/mega-prompt-template.md` to internalize the full template structure before starting. You will fill this in at the end.

## Interview Protocol

Ask **one question at a time**. Wait for the answer before continuing. For each question, offer your own recommended answer based on what you know so far — the user can accept, tweak, or override it.

Work through these branches in order, but skip questions that are already answered from context:

### Branch 1 — The Outcome
What is the single final outcome? What does "done" look like in one sentence?

This becomes the `/goal` line. It must be falsifiable — something the evaluator model can confirm from the transcript.

### Branch 2 — Context
Fill in the CONTEXT block:
- **Project**: what are you building?
- **Stack**: languages, frameworks, infra?
- **Current state**: what exists today — is this greenfield, or modifying existing code?
- **Working dir**: path or repo name?
- **Constraints**: anything off-limits, budget or time constraints?
- **Audience**: who is this for?

Ask about context fields that are missing or ambiguous. If the user has described the project already, confirm rather than re-ask.

### Branch 3 — Success Criteria
What are the 3–5 measurable conditions that must ALL be true for the goal to be met?

Each criterion must map to something the agent can produce as proof in the transcript (command output, file count, test result, URL). Push back on vague criteria like "it works" — ask what command proves it.

### Branch 4 — Constraints and Off-Limits
What must the agent NOT do or touch?
- Files or directories that must stay unchanged
- Actions that require human approval (commits, deploys, etc.)
- Any tool restrictions (no internet, no DB writes, etc.)

### Branch 5 — Quality Bar
Adjust the quality bar to fit the task:
- Is there a UI? (if no, drop the design line)
- What coding conventions matter?
- Is this internal tooling or production-facing?

### Branch 6 — Final Deliverable Proof
What should the agent produce at the end to confirm completion?
- Default: test output + file list + how to run
- Ask if a screenshot, URL, or specific artifact is needed

## NEVER

- NEVER ask multiple questions in one turn — one question, then wait.
- NEVER accept "I'll figure that out later" — require a decision or explicitly mark it as an open question before moving on.
- NEVER let the user redirect to implementation details before all branches are resolved.
- NEVER output the mega prompt until all blocking branches (1, 2, 3) are resolved. Branches 4–6 can use sensible defaults if the user wants to move fast.

## When to Stop Interviewing

Stop and output the prompt when:
- Branches 1–3 are fully resolved, AND
- The user says "go" / "looks good" / "that's enough", OR
- You've asked about all branches and have reasonable answers for everything

## Output

Once done interviewing, output the completed mega prompt as a code block, ready to paste directly into Claude Code or Codex CLI.

After the code block, add a one-line summary of any open questions or assumptions you made.

---

## References

- `references/mega-prompt-template.md` — the full template to fill in