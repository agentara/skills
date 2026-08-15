# ✨ Agentara's Skills

![banner](https://github.com/user-attachments/assets/d7843a4e-9b67-4494-b3c7-1f0092e41a15)


A personal library of Claude Code skills — installable prompt extensions that give Claude Code new capabilities.

## Reference

### AIGC

AI-generated content tools for image stylization, video planning, visual continuity, storyboards, and key art.

- **[presentation-design](skills/aigc/presentation-design/SKILL.md)** — Plan and generate a premium 6-slide presentation design board as one single composite image, with a named layout library and light/dark style modes.
- **[gunpla-poster](skills/aigc/gunpla-poster/SKILL.md)** — Create premium collectible Gunpla model-photography posters through a guided interview, with deterministic reference routing for bust, grounded full-body, and support-stand combat compositions.
- **[soviet-storybook-grotesque](skills/aigc/soviet-storybook-grotesque/SKILL.md)** — Transform photos into strange, rough, faded Eastern European children's book illustrations with absurd handwritten rhymes.
- **[torn-paper-collage-poster](skills/aigc/torn-paper-collage-poster/SKILL.md)** — Create torn-paper editorial collage poster prompts and image workflows with layered ripped paper, rough typography, stamps, tape, stickers, and photocopy texture.
- **[video-character-design](skills/aigc/video-character-design/SKILL.md)** — Create reusable character design specs and character sheets for video, storyboard, advertising, animation, or AI video-generation workflows.
- **[video-plan](skills/aigc/video-plan/SKILL.md)** — Plan short-form videos by choosing a story arc, visual style, duration, and scene-by-scene structure.
- **[video-poster-design](skills/aigc/video-poster-design/SKILL.md)** — Create cinematic poster concepts and final key art from a brief, video plan, storyboard, or character design.
- **[video-storyboard](skills/aigc/video-storyboard/SKILL.md)** — Generate storyboard image boards and matching video-generation prompt scripts for specific scenes.

### Entertainment

Sports forecasting and other fun, interactive prediction tools.

- **[world-cup-predictor](skills/entertainment/world-cup-predictor/SKILL.md)** — Predict FIFA World Cup matches, full tournament paths, and champion probabilities through agent-native subagents that analyze live news, weather, injuries, markets, Polymarket, tactics, and tournament context while updating a real-time web dashboard.

### Health

Health, child development, parenting, triage, and report interpretation tools.

- **[emergency-triage](skills/health/emergency-triage/SKILL.md)** — Help users triage urgent or semi-urgent symptoms, narrow possible causes, and prepare department and examination suggestions.
- **[lab-interpreter](skills/health/lab-interpreter/SKILL.md)** — Interpret medical lab reports from images, PDFs, or text, explaining abnormal values and practical next steps.
- **[super-daddy](skills/health/super-daddy/SKILL.md)** — Act as a family-doctor-style Chinese parenting assistant that maintains `~/.super_daddy/`, builds child profiles, runs structured visits, creates reference-grounded plans, generates visual plan images, and archives cases.

### Engineering

Practical software engineering workflows for code review, small change planning, PR communication, reviewer feedback, and emergency changes.

- **[engineering-code-review](skills/engineering/engineering-code-review/SKILL.md)** — Review code changes for code health, design, functionality, complexity, tests, maintainability, and approval risk.
- **[engineering-review-comments](skills/engineering/engineering-review-comments/SKILL.md)** — Write clear, respectful, severity-labeled code review comments that explain reasoning and drive better code.
- **[engineering-small-prs](skills/engineering/engineering-small-prs/SKILL.md)** — Split large features, refactors, and migrations into reviewable, testable PR or CL sequences.
- **[engineering-change-descriptions](skills/engineering/engineering-change-descriptions/SKILL.md)** — Draft or improve PR, CL, and commit descriptions so reviewers and future maintainers understand what changed and why.
- **[engineering-review-feedback](skills/engineering/engineering-review-feedback/SKILL.md)** — Handle reviewer comments as the change author by clarifying code, applying fixes, and resolving disagreements constructively.
- **[engineering-emergency-changes](skills/engineering/engineering-emergency-changes/SKILL.md)** — Decide whether a hotfix is a true emergency and run expedited review without losing follow-up code health.

### Productivity

General workflow tools, not code-specific.

- **[feature-dev-loop](skills/productivity/feature-dev-loop/SKILL.md)** — End-to-end orchestration for PR-sized feature development: requirements baseline, multi-perspective plan review, safe serial implementation, dynamic acceptance matrix, and HTML PR summary.
- **[article-to-html](skills/productivity/article-to-html/SKILL.md)** — Render markdown drafts or conversation documents into self-contained paper-style HTML pages with inline CSS, SVG figures, callouts, tables, and optional interactivity.
- **[doctor-strange](skills/productivity/doctor-strange/SKILL.md)** — Run causal sand-table simulations of future scenarios through parallel universe subagents, then store and recall the projections as soft priors.
- **[mega-goal-prompt](skills/productivity/mega-goal-prompt/SKILL.md)** — Interview the user about a long-horizon task and output a filled-in `/goal` mega prompt ready to paste into Claude Code or Codex CLI.
- **[publish-research-site](skills/productivity/publish-research-site/SKILL.md)** — Turn a thesis, proposition, trend, question, or explainer topic into a citation-backed, image-rich, interactive website and deploy it with Vercel CLI.

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

## License

Most original content in this repository is licensed under [MIT](LICENSE).

The engineering skills are adapted from [Google Engineering Practices](https://google.github.io/eng-practices/) under [CC-BY 3.0](https://creativecommons.org/licenses/by/3.0/). They include source attribution in each `SKILL.md`; wording and structure were changed for this skill library.
