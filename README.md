# Skills

A personal library of Claude Code skills — installable prompt extensions that give Claude Code new capabilities.

## Categories

- **[AIGC](skills/aigc/README.md)** — AI-generated content tools.
- **[Health](skills/health/README.md)** — Health and wellness tools.
- **[Productivity](skills/productivity/README.md)** — General workflow tools, not code-specific.

## Installing a skill

Symlink or copy a skill's directory into `~/.claude/skills/<skill-name>/` so the Claude Code harness can discover it.

```bash
ln -s /path/to/skills/skills/productivity/doctor-strange ~/.claude/skills/doctor-strange
```
