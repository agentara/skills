---
name: publish-research-site
description: Turn a thesis, proposition, trend, question, or explainer topic into a citation-backed, image-rich, interactive website and deploy it with Vercel CLI. Use when the user asks to research a claim deeply, generate visuals, build a shareable web experience, publish a microsite, create an interactive story/report, or deploy a researched site to Vercel.
---

# Publish Research Site

## Overview

Use this skill to orchestrate a four-stage pipeline: deep research, generated bitmap assets, production-grade interactive website creation, and Vercel CLI deployment. Treat the final artifact as a public-facing, shareable microsite: rigorous enough to cite, visual enough to travel, and fast enough to open on mobile.

## Workflow

### 0. Preflight dependencies

Before research or implementation, check that the required skills and CLIs are available. Prefer the user's Codex-local toolchain paths when commands are not on the default PATH:

```bash
export PATH="$HOME/.agent-reach-venv/bin:$HOME/.codex/toolchains/node-current/bin:$HOME/.codex/toolchains/gh-current/bin:$PATH"

for cmd in node npm npx vercel agent-reach mcporter yt-dlp gh; do
  command -v "$cmd" >/dev/null || {
    echo "Missing required dependency: $cmd"
    exit 1
  }
done

agent-reach doctor
```

Also confirm the skill files are present when the environment exposes the local skills folders:

```bash
test -f "$HOME/.agents/skills/deep-research/SKILL.md" || echo "Missing skill: deep-research"
test -f "$HOME/.agents/skills/agent-reach/SKILL.md" || echo "Missing skill: agent-reach"
test -f "$HOME/.agents/skills/frontend-design/SKILL.md" || echo "Missing skill: frontend-design"
test -f "$HOME/.codex/skills/.system/imagegen/SKILL.md" || echo "Missing skill: imagegen"
```

If a required dependency is missing, stop before starting the project and ask the user to install or authorize installing the missing prerequisite. Do not discover missing deployment tools after the site is already built.

### 1. Scope the proposition

Restate the user's thesis or topic as a working brief:

- Core proposition or question
- Intended audience and desired tone
- What the site should make the audience believe, understand, compare, or explore
- Any required language, region, timeframe, or deployment preference

Proceed autonomously when the intent is clear. Ask only when the proposition, audience, or deployment target is too ambiguous to act safely.

### 2. Run deep research

Invoke the existing `$deep-research` skill when available. Use standard mode by default; use deep or ultradeep when the site supports a consequential decision, controversial claim, investment argument, technical architecture judgment, or public-facing factual report.

Research output must include:

- Executive thesis with confidence level
- Key claims with citation IDs
- Contradictions, counterarguments, and uncertainty
- Source list with URLs, publication dates where relevant, and credibility notes
- 5-10 material facts that should appear in the website
- 3-5 visual opportunities suggested by the evidence

Do not build the site until the evidence base is strong enough for the claim. For current topics, verify facts with recent sources and label dates explicitly.

### 3. Convert research into a site brief

Create a concise site brief before coding. Use `references/site-brief-template.md` when the project has multiple sections, many claims, or several generated assets.

The brief must define:

- Narrative arc: hook, evidence path, tension/counterpoint, synthesis, action or takeaway
- Sections and interactions
- Claim-to-source map
- Visual asset list and image prompts
- Framework choice and project directory
- Verification and deployment checklist

Keep website copy tight. Turn research into scannable public communication rather than pasting a full report into the UI.

### 4. Generate images

Invoke the existing `$imagegen` skill for raster images that materially improve the site: hero art, editorial illustrations, product/scene imagery, explainers, posters, thumbnails, or social share visuals.

Image workflow:

- Generate only assets that the site will actually use.
- Write prompts from the research brief, including subject, composition, style, aspect ratio, avoid list, and whether text should be absent.
- Avoid putting factual claims or small text inside generated images unless the user explicitly wants typographic art.
- Inspect outputs, iterate once or twice when needed, and keep only usable finals.
- Move or copy final project-bound assets into the website workspace, usually under `public/assets/` or the framework equivalent.
- Record final prompts and saved paths in the site brief or final report.

### 5. Build the interactive website

Invoke `$frontend-design` when available, then implement the actual experience, not a marketing placeholder.

Default implementation guidance:

- Prefer Vite/React, Next.js, or a static HTML/CSS/JS site according to the workspace and deployment needs.
- Make the first viewport communicate the proposition immediately.
- Include at least one meaningful interaction: scrollytelling, timeline, comparison slider, evidence cards, filterable claim map, scenario toggle, chart interaction, annotated diagram, quiz, or calculator.
- Show citations close to the claims they support.
- Include a source drawer, notes section, or reference panel for readers who want to verify.
- Make it responsive, fast, accessible, and visually memorable.
- Use generated images as real assets, not decoration that could be removed without changing the communication.

Avoid generic placeholder sections, uncited claims, dummy charts, stock-like visuals, or interaction that does not teach the user anything.

### 6. Verify locally

Before deployment:

- Install dependencies only as needed and preserve the existing package manager style.
- Run lint/typecheck/tests when present.
- Run a production build.
- Start the local server when needed.
- Use browser verification on desktop and mobile widths.
- Confirm generated images load from project-local paths.
- Confirm external links and citations are reachable when practical.
- Fix visible layout problems, overlapping text, blank canvases, console errors, and broken routes.

Do not claim the site is ready until the build and visual checks have actually run, or clearly report what could not be verified.

### 7. Deploy with Vercel CLI

Use Vercel CLI for deployment.

Preferred sequence:

```bash
export PATH="$HOME/.codex/toolchains/node-current/bin:$PATH"
vercel --version
npm run build
vercel --yes
```

Use `vercel --prod --yes` only when the user asks for production or the task clearly requires a production deployment. If an existing Vercel project/domain could be overwritten, ask before production deployment.

If the local `vercel` command is unavailable after adding the Codex-local Node toolchain to PATH, use `npx vercel@latest`. If Vercel authentication is missing, ask the user to log in or confirm an alternative deploy path; do not silently switch to a non-CLI deployment service.

Capture the deployment URL from CLI output and test it in a browser. If deployment succeeds but remote verification fails, report both the URL and the failure.

## Final Response

Report only the useful handoff details:

- Deployed URL
- Local project path
- Research scope and source count
- Generated image asset paths
- Verification commands run
- Known limitations or unverified items

Keep the final answer concise and include links or file paths the user can open immediately.
