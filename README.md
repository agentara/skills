# ✨ Agent Tara Skills

![banner](https://github.com/user-attachments/assets/d7843a4e-9b67-4494-b3c7-1f0092e41a15)


A personal library of Claude Code skills — installable prompt extensions that give Claude Code new capabilities.

## Reference

### AIGC

AI-generated content tools for video planning, visual continuity, storyboards, and key art.

- **[video-character-design](skills/aigc/video-character-design/SKILL.md)** — Create reusable character design specs and character sheets for video, storyboard, advertising, animation, or AI video-generation workflows.
- **[video-plan](skills/aigc/video-plan/SKILL.md)** — Plan short-form videos by choosing a story arc, visual style, duration, and scene-by-scene structure.
- **[video-poster-design](skills/aigc/video-poster-design/SKILL.md)** — Create cinematic poster concepts and final key art from a brief, video plan, storyboard, or character design.
- **[video-storyboard](skills/aigc/video-storyboard/SKILL.md)** — Generate storyboard image boards and matching video-generation prompt scripts for specific scenes.

### Health

Health and wellness tools for triage and report interpretation.

- **[emergency-triage](skills/health/emergency-triage/SKILL.md)** — Help users triage urgent or semi-urgent symptoms, narrow possible causes, and prepare department and examination suggestions.
- **[lab-interpreter](skills/health/lab-interpreter/SKILL.md)** — Interpret medical lab reports from images, PDFs, or text, explaining abnormal values and practical next steps.

### Productivity

General workflow tools, not code-specific.

- **[doctor-strange](skills/productivity/doctor-strange/SKILL.md)** — Simulate how future scenarios might unfold, store the projections as memory, and recall them later as soft priors.

## Installing a Skill

### Install via NPX (Recommended)

This installs one skill at a time. For example, to install `doctor-strange`:

```bash
npx skills add https://github.com/agentara/skills/blob/main/skills/productivity/doctor-strange/ -y -g
```

To install a different skill, replace the path with that skill's directory URL.

### Install Manually

Clone this repo to your local machine.

```bash
git clone https://github.com/agentara/skills.git
```

Then symlink or copy the specific skill directory you want to install into `~/.agents/skills/<skill-name>/` and `~/.claude/skills/<skill-name>/` so the Claude Code and other agents can discover it. For example, to install `doctor-strange` manually:

```bash
ln -s /path/to/skills/skills/productivity/doctor-strange ~/.agents/skills/doctor-strange
ln -s /path/to/skills/skills/productivity/doctor-strange ~/.claude/skills/doctor-strange
```
