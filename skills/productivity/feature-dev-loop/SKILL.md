---
name: feature-dev-loop
description: End-to-end orchestration for non-trivial software feature development. Use this skill whenever the user asks to implement a PR-sized feature, break down a plan, have subagents review a plan, run a plan-review-development-acceptance loop, coordinate multiple review perspectives, produce an acceptance report, or generate an HTML PR summary. Prefer this skill for multi-step code changes even if the user only says "build this feature" and the task is not a tiny one-file edit.
---

# Feature Dev Loop

Orchestrate a full software feature loop by composing local development skills instead of rewriting them: requirements baseline, plan breakdown, multi-perspective plan review, safe serial implementation, dynamic acceptance review, and an HTML PR summary.

This is a controller skill. It decides when to move between stages, how feedback is classified, when loops exit, what gets written to disk, and when to involve the user. It should call or follow existing local skills for the lower-level work when they are available, especially:

- `superpowers:writing-plans` for implementation plans
- `superpowers:subagent-driven-development` for task execution with implementer/reviewer agents
- `superpowers:test-driven-development` for feature and bugfix implementation
- `superpowers:requesting-code-review` for code review dispatch
- `superpowers:verification-before-completion` before claiming completion
- Frontend/browser verification skills when UI behavior changes

## Operating Defaults

- Use this for non-trivial feature work, multi-step changes, PR-sized tasks, or explicit requests for plan review, subagent review, acceptance testing, code review, or PR summary generation.
- For tiny edits, use a lightweight version unless the user explicitly asks for the full loop.
- Default to safe serial implementation. Only run implementation workers in parallel when file/module ownership is disjoint and shared contracts are already fixed.
- Default to human gates at the end of plan review and before final release. If the user asks for full auto mode, proceed automatically when exit criteria are met and record all assumptions.
- Save process artifacts in the target repo under `docs/dev-loop-runs/YYYY-MM-DD-feature-slug/`.
- Be git-aware, but do not commit, push, or open PRs unless the user explicitly asks.
- Never loop forever. Each review loop has a default limit of 3 rounds.
- Respect the active tool policy for subagents. If the user explicitly asked for subagents, delegation, plan review by agents, the full feature-dev-loop, or this skill by name, proceed with subagent dispatch when available. If not, ask before the first subagent dispatch or perform the review inline and record the limitation.

## Dependency Gate

Before starting a full loop, check whether the local prerequisite skills are available in the active session. This skill depends on Superpowers-style development workflows; it should not silently degrade into an ad-hoc process when those skills are missing.

Check dependencies from the active skill list when it is available. If the active skill list is unavailable, inspect likely local skill/plugin locations such as `.agents/skills/superpowers`, `.codex/superpowers/skills`, or the harness plugin list. Do not assume a dependency exists just because this skill mentions it.

### Required skills

These are required for the intended workflow:

- `superpowers:writing-plans` - implementation plan breakdown
- `superpowers:subagent-driven-development` - serial task execution with implementer/reviewer agents
- `superpowers:test-driven-development` - red/green/refactor discipline for behavior changes
- `superpowers:requesting-code-review` - structured code review dispatch
- `superpowers:verification-before-completion` - evidence before completion claims

### Recommended skills

These are not always required, but should be used when relevant:

- `superpowers:brainstorming` - when the request is still rough or product/design intent is unclear
- `superpowers:systematic-debugging` - when implementation or tests expose a bug
- `superpowers:receiving-code-review` - when applying reviewer feedback
- `superpowers:finishing-a-development-branch` - when the user wants merge/PR/branch cleanup guidance
- `superpowers:using-git-worktrees` - when the user wants isolated branch/worktree execution
- Frontend/browser automation skills - when UI behavior must be visually verified

### Missing dependency behavior

If any required skill is missing:

1. Stop before creating the full run directory or starting implementation.
2. Tell the user exactly which prerequisite skills are missing.
3. Recommend installing Superpowers, because these required skills are provided by the Superpowers workflow.
4. If a plugin-install tool for Superpowers is available in the current harness, use it or ask the user to approve it according to the active tool policy. Otherwise provide the appropriate install hint for the harness when known:
   - Codex App: open Plugins in the sidebar, find `Superpowers` in the Coding section, click `+`, and follow the prompts.
   - Codex CLI: run `/plugins`, search for `superpowers`, and select `Install Plugin`.
   - Claude Code: run `/plugin install superpowers@claude-plugins-official`, or register the Superpowers marketplace with `/plugin marketplace add obra/superpowers-marketplace` and then run `/plugin install superpowers@superpowers-marketplace`.
5. After the user installs it, restart the dependency check before proceeding.

If installation is not possible in the current harness, offer a reduced inline mode only after making the limitation explicit. Reduced inline mode must still create the run artifacts and record that subagent/Superpowers dependencies were unavailable.

Reference for installation and workflow names: `https://github.com/obra/superpowers`.

## Feedback Severity

All reviewer comments must use these severities:

- `BLOCKER`: Must be resolved before the loop can exit.
- `IMPORTANT`: Should be resolved before exit. The controller may adjudicate and close it only with written rationale.
- `QUESTION`: Must be answered or converted into a concrete change before exit.
- `NIT`: Non-blocking improvement. Record it, but do not let it block progress.

A phase may exit only when there are no unresolved `BLOCKER`, `IMPORTANT`, or `QUESTION` items. Remaining `NIT` items become follow-ups.

## Run Directory

At the start of a run:

1. Locate the repo root with `git rev-parse --show-toplevel` when available.
2. Check `git status -sb`.
3. Record `base_sha`, current branch, dirty-state summary, user request, and mode.
4. Create:

```text
docs/dev-loop-runs/YYYY-MM-DD-feature-slug/
  00-requirements.md
  01-plan.md
  02-plan-review-rounds.md
  03-implementation-log.md
  04-acceptance-report.md
  05-pr-summary.html
  artifacts/
    screenshots/
    test-outputs/
```

If the working tree is dirty, do not revert anything. Decide whether existing changes are related to the requested task. If ambiguous and risky, ask the user before editing.

## Phase 1: Requirements Baseline

Create `00-requirements.md` before planning.

Use this structure:

```markdown
# Requirements Baseline

## Goal
## Non-goals
## User-visible Behavior
## Acceptance Criteria
## Constraints
## Assumptions
## Open Questions
## Source Request
## Repo Context
```

Ask the user only for open questions that materially affect architecture, data model, security, user experience, compatibility, or test strategy. Infer ordinary implementation details from repo conventions and record them as assumptions.

Do not enter plan breakdown while blocking open questions remain.

## Phase 2: Plan Breakdown

Explore the codebase before writing the plan. Prefer `rg` and existing project docs/tests. Let the repo teach the implementation style.

Create `01-plan.md`. When available, follow `superpowers:writing-plans`.

The plan must include:

- Exact goal and architecture summary
- Files/modules expected to change
- Task order and dependencies
- Test strategy and exact verification commands
- Ownership boundaries for any worker subagents
- Acceptance criteria mapped back to `00-requirements.md`
- Known risks and assumptions

Tasks should be small enough to implement and review independently. If a shared contract is needed, put it before dependent tasks.

## Phase 3: Multi-perspective Plan Review Loop

Dispatch multiple plan-review subagents from different perspectives when subagents are available and permitted. Give each reviewer precise context: the requirements file, plan file, relevant repo conventions, and the requested output schema. Do not hand them the whole conversation history.

Default reviewer perspectives:

- Architecture reviewer: decomposition, boundaries, dependency order, extensibility, integration risk
- Test strategy reviewer: acceptance criteria, regression coverage, failure paths, verification commands
- Product/spec reviewer: user-visible behavior, requirement gaps, non-goals, ambiguous semantics
- Risk/complexity reviewer: hidden complexity, migration risk, rollout concerns, maintainability traps

Each reviewer must return:

```markdown
## Verdict
APPROVED | COMMENTS

## Comments
- id:
  severity: BLOCKER | IMPORTANT | QUESTION | NIT
  area:
  target:
  comment:
  required_change:

## Approval Conditions
```

Aggregate all feedback into `02-plan-review-rounds.md`.

For each round:

1. Fix the plan for all valid `BLOCKER`, `IMPORTANT`, and `QUESTION` feedback.
2. If rejecting a comment, write the adjudication and rationale.
3. Re-run the reviewers on the whole revised plan, not just the diff.
4. Stop after 3 rounds and escalate unresolved blocking disagreement to the user with a concrete recommendation.

Plan review exits when all reviewers approve or only `NIT` items remain.

### Plan Gate

Unless the user requested auto mode, show a concise plan summary and ask for approval before implementation:

- Goal
- Major files/modules
- Task sequence
- Main risks
- Verification strategy

## Phase 4: Safe Serial Implementation

Implement one task at a time in plan order. Use `superpowers:subagent-driven-development` when the plan is well-specified and worker subagents are appropriate. Use `superpowers:test-driven-development` for behavior changes.

For each task:

1. Assign clear file/module ownership.
2. Tell workers they are not alone in the codebase, must not revert others' edits, and must adapt to existing changes.
3. Prefer TDD: write/verify failing tests before implementation where practical.
4. Run task-specific verification commands.
5. Record changes, commands, results, and concerns in `03-implementation-log.md`.
6. Run task-level spec compliance and code-quality review when the task has meaningful behavior or risk.
7. Resolve review findings using the shared severity rules.

Default to serial implementation. Parallel implementation is allowed only when:

- Tasks touch disjoint files/modules
- Shared contracts are already committed or otherwise stable
- Each worker has explicit ownership
- The controller can safely integrate and review the outputs

Do not create checkpoint commits unless the user explicitly requested commits or PR mode.

## Phase 5: Dynamic Acceptance Matrix

After implementation, choose reviewers based on the actual change surface.

Always run:

- Requirements acceptance reviewer: verifies the delivered behavior against `00-requirements.md` and `01-plan.md`
- Test coverage reviewer: checks tests, missing cases, regression risk, and whether verification commands are credible
- Code quality reviewer: checks correctness, maintainability, integration, edge cases, and hidden regressions

Run conditionally:

- Frontend UX reviewer: for UI, interaction, layout, accessibility, or visual changes; require browser/screenshot evidence
- Security reviewer: for auth, permissions, secrets, uploads, external input, payments, or data exposure
- Performance reviewer: for queries, rendering loops, concurrency, caching, batching, or large data paths
- Docs/migration reviewer: for configuration, migration, API behavior, setup instructions, or user-facing behavior changes
- Compatibility reviewer: for public APIs, schemas, serialized data, plugins, or integration contracts

Each acceptance reviewer receives:

- Requirements baseline
- Final plan
- Implementation log
- `base_sha` and current `HEAD` or working-tree diff
- Relevant test outputs and screenshots
- Their specific review mandate

Each reviewer returns:

```markdown
## Verdict
PASS | PASS_WITH_NOTES | FAIL

## Scope Checked
## Evidence
## Findings
- id:
  severity: BLOCKER | IMPORTANT | MINOR
  target:
  finding:
  suggested_fix:
  evidence:

## Residual Risks
```

Aggregate results into `04-acceptance-report.md`:

```markdown
# Acceptance Report

## Verdict
PASS | PASS_WITH_NOTES | FAIL

## Scope Checked
## Reviewers Run
## Tests Run
## Requirement Coverage
## Findings
## Fixes Applied
## Residual Risks
## Follow-ups
```

Acceptance exits only when:

- No `BLOCKER` remains
- No unresolved `IMPORTANT` remains
- Verification commands pass, or unavailable commands are clearly explained
- The controller can honestly assign `PASS` or `PASS_WITH_NOTES`

If acceptance fails, fix the issues and re-run the relevant reviewers. Stop after 3 rounds and escalate with a blocker report.

## Phase 6: HTML PR Summary

Generate `05-pr-summary.html` as a self-contained, summary-first HTML report. It should help a PR reviewer understand the change quickly, while preserving expandable audit detail.

The first screen should answer:

- What problem this PR solves
- What changed
- User-visible behavior changes
- Validation and acceptance verdict
- Residual risks and follow-ups

Include expandable detail sections for:

- Requirements baseline
- Plan review summary
- Implementation log
- Acceptance matrix
- Tests run and key outputs
- Code review findings
- Screenshots or artifacts, when applicable
- Main diff or changed-file summary

Use plain, readable HTML and CSS with no external network dependencies. Link local artifacts with relative paths where possible.

## Git Policy

- Always inspect and record current branch and `base_sha`.
- Never run destructive git commands.
- Never revert user changes unless explicitly requested.
- Do not commit, push, or open a PR unless the user explicitly asks.
- If commits are requested, use non-interactive git commands and keep commits scoped to completed, verified units.
- If no commits exist, generate summaries from `git diff` and `git status`.

## User Escalation Rules

Ask the user only when:

- Requirements ambiguity changes architecture, UX, data model, security, compatibility, or acceptance criteria
- Existing workspace changes make safe editing ambiguous
- Review loops hit the 3-round limit with unresolved blocking disagreement
- The requested behavior conflicts with repo constraints or safety requirements

When asking, ask one concrete question at a time and provide a recommended answer.

## Completion Checklist

Before final response:

- `00-requirements.md` exists
- `01-plan.md` exists and passed plan review or has documented adjudications
- `03-implementation-log.md` records tasks, changed files, and verification evidence
- `04-acceptance-report.md` has a clear verdict
- `05-pr-summary.html` exists
- Required tests or checks were run, or the reason they could not run is recorded
- No unresolved `BLOCKER`, `IMPORTANT`, or `QUESTION` remains

Then summarize the outcome concisely for the user, including the report path and verification status.
