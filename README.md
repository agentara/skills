# Agentara's Skills

A personal library of Claude Code skills — installable prompt extensions that give Claude Code new capabilities.

## Categories

- **[AIGC](skills/aigc/README.md)** — AI-generated content tools.
- **[Health](skills/health/README.md)** — Health and wellness tools.
- **[Productivity](skills/productivity/README.md)** — General workflow tools, not code-specific.

## Installing a skill

### Install via NPX (Recommended)

```sh
npx skills add https://github.com/agentara/skills/blob/main/skills/productivity/doctor-strange/ -y -g
```

### Install Manually

Clone this repo to your local machine.

```bash
git clone https://github.com/agentara/skills.git
```

Then symlink or copy a skill's directory into `~/.agents/skills/<skill-name>/` and `~/.claude/skills/<skill-name>/` so the Claude Code and other agents can discover it.

```bash
ln -s /path/to/skills/skills/productivity/doctor-strange ~/.agents/skills/doctor-strange
ln -s /path/to/skills/skills/productivity/doctor-strange ~/.claude/skills/doctor-strange
```
