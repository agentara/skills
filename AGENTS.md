This file provides guidance to agents when working with code in this repository.

## Repository Purpose

This is a personal library of **skills** — installable prompt extensions that give agent new capabilities. Each skill is a `SKILL.md` file containing a frontmatter block and a detailed instruction body.

## Structure

```text
skills/
  <category>/
    <skill-name>/
      SKILL.md
```

Current categories: `productivity`

## Skill Format

Every `SKILL.md` must start with a YAML frontmatter block:

```yaml
---
name: <kebab-case-slug>
description: >
  One or more sentences describing what the skill does and when it triggers.
  Include explicit TRIGGER conditions (keywords, user intents) and DO NOT TRIGGER
  conditions to help the model route correctly.
---
```

The body after the frontmatter is the full instruction set the model will follow when the skill is invoked.

## Skill Reference Maintenance

Whenever adding or modifying a skill, update both reference lists that expose the skill:

- Root `README.md`
- Category README at `skills/{category_name}/README.md`

Keep each reference's link, name, and short description aligned with the skill's current behavior.

## Key Design Patterns (from existing skills)

- **Multi-agent orchestration**: Skills can spawn parallel subagents via the `Agent` tool. The main agent coordinates; subagents each inhabit a separate branch/task and report back.
- **Trigger conditions**: The `description` field doubles as routing logic — be explicit about what user messages should and shouldn't activate the skill.
- **Memory integration**: Skills that produce persistent outputs write to the project memory directory (`/Users/danielwalnut/.claude/projects/*/memory/`) using the standard frontmatter format and update `MEMORY.md`.
- **Mode switching**: Complex skills define multiple modes (e.g., SIMULATE / RECALL / MANAGE) with explicit command words that switch between them.

## Installing a Skill

Skills in this repo are meant to be symlinked or copied into `~/.claude/skills/<skill-name>/SKILL.md` and `~/.agents/skills/<skill-name>/SKILL.md` so the Claude Code and other agents can discover and load them.
