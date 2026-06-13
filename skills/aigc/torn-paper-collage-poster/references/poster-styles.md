# Poster Style Selector

Use this compact selector first, then open the relevant file in `references/styles/` for specific style IDs, core keywords, prompt add-ons, and avoid notes.

Default style: `torn-paper-editorial-collage` in `styles/editorial-print.md`.

## Selection Rules

- Preserve the caller's aspect ratio behavior. Do not add, remove, or default an aspect ratio.
- Text is allowed. Never add a no-readable-text restriction unless the user explicitly asks for a textless poster.
- Exclude pure wallpaper, texture tests, icon packs, character sheets, UI dashboards, and styles that cannot support poster hierarchy.
- If the user asks for options, open the most relevant category file and return 3 to 5 style IDs with core keywords.
- If several category files fit, open only the smallest useful set.

## Category Index

- `styles/editorial-print.md`: editorial, magazine, newspaper, zine, type-led, documentary, report, and print-production posters.
- `styles/brand-product-tech.md`: brand campaign, product launch, commercial, SaaS, AI, hardware, fintech, retail, and service posters.
- `styles/culture-event-sports.md`: entertainment, film, music, sports, festival, performance, travel, market, and public event posters.
- `styles/art-historical-craft.md`: art movements, historical design languages, regional visual traditions, craft, printmaking, textile, and material posters.
- `styles/social-data-internet.md`: social media, internet culture, meme, live moment, data storytelling, public information, explainer, and attention-map posters.

## Porting Goal

All poster-ready aesthetic ports should live under `references/styles/`. Keep this selector as a small category router; place concrete style prompts inside the category files.
