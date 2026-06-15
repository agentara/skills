const FLAGS = {
  Algeria: "🇩🇿",
  Argentina: "🇦🇷",
  Australia: "🇦🇺",
  Austria: "🇦🇹",
  Belgium: "🇧🇪",
  "Bosnia and Herzegovina": "🇧🇦",
  Brazil: "🇧🇷",
  Canada: "🇨🇦",
  "Cape Verde": "🇨🇻",
  Colombia: "🇨🇴",
  "Congo DR": "🇨🇩",
  "DR Congo": "🇨🇩",
  Croatia: "🇭🇷",
  Curacao: "🇨🇼",
  "Czech Republic": "🇨🇿",
  Ecuador: "🇪🇨",
  Egypt: "🇪🇬",
  England: "\u{1F3F4}\u{E0067}\u{E0062}\u{E0065}\u{E006E}\u{E0067}\u{E007F}",
  France: "🇫🇷",
  Germany: "🇩🇪",
  Ghana: "🇬🇭",
  Haiti: "🇭🇹",
  Iran: "🇮🇷",
  Iraq: "🇮🇶",
  "Ivory Coast": "🇨🇮",
  Japan: "🇯🇵",
  Jordan: "🇯🇴",
  Mali: "🇲🇱",
  Mexico: "🇲🇽",
  Morocco: "🇲🇦",
  Netherlands: "🇳🇱",
  "New Zealand": "🇳🇿",
  Norway: "🇳🇴",
  Panama: "🇵🇦",
  Paraguay: "🇵🇾",
  Portugal: "🇵🇹",
  Qatar: "🇶🇦",
  "Saudi Arabia": "🇸🇦",
  Scotland: "\u{1F3F4}\u{E0067}\u{E0062}\u{E0073}\u{E0063}\u{E0074}\u{E007F}",
  Senegal: "🇸🇳",
  "South Africa": "🇿🇦",
  "South Korea": "🇰🇷",
  Spain: "🇪🇸",
  Switzerland: "🇨🇭",
  Sweden: "🇸🇪",
  Tunisia: "🇹🇳",
  Turkey: "🇹🇷",
  "United States": "🇺🇸",
  Uruguay: "🇺🇾",
  Uzbekistan: "🇺🇿"
};

let lastPredictionStamp = "";
let lastSourceStamp = "";
let lastLiveStamp = "";
let lastReplayStamp = "";
let replayFrames = [];
let replayIndex = -1;
let replayMode = "live";
let replayTimer = null;
let liveNeedsRender = true;
let groupsData = [];
let activeGroup = "all";
let currentPredictions = { matches: [] };
let currentLiveState = {};
let selectedMatchKey = "";

async function readJson(path, fallback) {
  try {
    const joiner = path.includes("?") ? "&" : "?";
    const response = await fetch(`${path}${joiner}t=${Date.now()}`, { cache: "no-store" });
    if (!response.ok) throw new Error(response.statusText);
    return await response.json();
  } catch {
    return fallback;
  }
}

function safeText(value) {
  return String(value ?? "").replace(/[&<>"']/g, (char) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    "\"": "&quot;",
    "'": "&#039;"
  })[char]);
}

function flagFor(team) {
  return FLAGS[team] || "🏳";
}

function pct(value) {
  return Math.round((Number(value) || 0) * 1000) / 10;
}

function americanOdds(probability) {
  const p = Math.max(0.01, Math.min(0.99, Number(probability) || 0.5));
  if (p >= 0.5) return `-${Math.round((p / (1 - p)) * 100)}`;
  return `+${Math.round(((1 - p) / p) * 100)}`;
}

function progressPercent(state) {
  return Math.max(0, Math.min(100, Math.round((state?.progress || 0) * 100)));
}

function latestMatchCount(state = currentLiveState) {
  return Number(state.featured?.matches || currentPredictions.matches?.length || 0);
}

function latestChampion(state = currentLiveState) {
  return state.featured?.champion || currentPredictions.predicted_champion || "";
}

function forecastStatusLabel(state = currentLiveState) {
  if (state.error) return "Attention";
  if (state.complete || progressPercent(state) >= 100) return "Published";
  if (progressPercent(state) > 0) return "Building";
  return "Waiting";
}

function forecastHeadline(state = currentLiveState) {
  if (state.error) return "Forecast run needs attention";
  if (state.complete || progressPercent(state) >= 100) return "Final forecast published";
  if (progressPercent(state) > 0) return "Forecast run in progress";
  return "Forecast run waiting";
}

function runStatRows(state = currentLiveState) {
  const rows = [{ label: "Status", value: forecastStatusLabel(state) }];
  const matchCount = latestMatchCount(state);
  const champion = latestChampion(state);

  if (matchCount) rows.push({ label: "Markets", value: String(matchCount) });
  if (champion) rows.push({ label: "Champion", value: champion });
  if (!state.complete && progressPercent(state) < 100) {
    rows.push({ label: "Progress", value: `${progressPercent(state)}%` });
  }

  return rows;
}

function liveMetaRows() {
  return runStatRows(currentLiveState).map((row) => `
    <span><em>${safeText(row.label)}</em>${safeText(row.value)}</span>
  `).join("");
}

function emptyPanel(title, copy, showLiveMeta = false) {
  const liveMeta = showLiveMeta ? `<div class="empty-meta">${liveMetaRows()}</div>` : "";
  return `<article class="empty-panel"><strong>${safeText(title)}</strong><p>${safeText(copy)}</p>${liveMeta}</article>`;
}

function renderGroups(data) {
  groupsData = data.groups || [];
  const target = document.querySelector("#bracket");
  target.innerHTML = "";
  for (const group of groupsData) {
    const teams = (group.teams || []).map((team) => `
      <li>
        <span>${flagFor(team)}</span>
        <strong>${safeText(team)}</strong>
      </li>
    `).join("");
    target.insertAdjacentHTML("beforeend", `
      <article class="group-card">
        <header>Group ${safeText(group.group)}</header>
        <ul>${teams}</ul>
      </article>
    `);
  }
}

function renderLiveState(data) {
  currentLiveState = data || {};
  const stage = document.querySelector("#live-stage");
  const message = document.querySelector("#live-message");
  const stats = document.querySelector("#run-stats");
  const ticker = document.querySelector(".market-ticker");
  const isComplete = Boolean(data.complete || progressPercent(data) >= 100);

  stage.textContent = forecastHeadline(data);
  message.textContent = data.message || (isComplete
    ? "Latest forecast snapshot is available below."
    : "Run status updates here; forecast lines change when a snapshot is published.");
  if (stats) {
    stats.innerHTML = runStatRows(data).map((row) => `
      <span><em>${safeText(row.label)}</em>${safeText(row.value)}</span>
    `).join("");
  }
  ticker?.classList.toggle("is-error", Boolean(data.error));
  ticker?.classList.toggle("is-complete", isComplete && !data.error);
  ticker?.classList.toggle("is-building", !isComplete && !data.error && progressPercent(data) > 0);
}

function normalizeGroup(group) {
  return String(group || "").trim().toUpperCase();
}

function groupLabel(group) {
  const normalized = normalizeGroup(group);
  return normalized ? `Group ${normalized}` : "Group";
}

function matchesActiveGroup(match) {
  return activeGroup === "all" || normalizeGroup(match.group) === activeGroup;
}

function renderGroupFilters(data) {
  const target = document.querySelector("#group-filter");
  if (!target) return;

  const matches = data.matches || [];
  if (matches.length === 0) {
    target.innerHTML = "";
    return;
  }

  const counts = new Map();
  for (const match of matches) {
    const group = normalizeGroup(match.group);
    if (group) counts.set(group, (counts.get(group) || 0) + 1);
  }

  const groupOrder = groupsData.length
    ? groupsData.map((group) => normalizeGroup(group.group)).filter(Boolean)
    : [...counts.keys()].sort();
  const visibleGroups = groupOrder.filter((group) => counts.has(group));
  const buttons = [
    { group: "all", label: "All", count: matches.length },
    ...visibleGroups.map((group) => ({ group, label: groupLabel(group), count: counts.get(group) || 0 }))
  ];

  target.innerHTML = buttons.map((button) => `
    <button
      class="group-filter-button ${activeGroup === button.group ? "is-active" : ""}"
      type="button"
      data-group="${safeText(button.group)}"
      aria-pressed="${activeGroup === button.group ? "true" : "false"}"
      title="${safeText(button.label)} markets"
    >
      <span>${safeText(button.label)}</span>
      <strong>${button.count}</strong>
    </button>
  `).join("");
}

function marketProbabilities(match) {
  const teams = match.teams || [];
  const probabilities = match.probabilities || {};
  const home = teams[0] || "Home";
  const away = teams[1] || "Away";
  return [
    { label: home, value: probabilities[home] ?? probabilities.Home ?? 0 },
    { label: "Draw", value: probabilities.Draw ?? probabilities.draw ?? 0 },
    { label: away, value: probabilities[away] ?? probabilities.Away ?? 0 }
  ];
}

function matchDescriptor(match) {
  const parts = [];
  if (match.round) parts.push(match.round);
  if (match.group) parts.push(groupLabel(match.group));
  if (match.match_id) parts.push(match.match_id);
  if (match.market_type) parts.push(String(match.market_type).toUpperCase());
  return parts.join(" · ");
}

function matchKey(match, index = 0) {
  return match.match_id || `${match.round || "match"}:${match.group || ""}:${(match.teams || []).join("-")}:${index}`;
}

function findMatchByKey(data, key) {
  return (data.matches || []).find((match, index) => matchKey(match, index) === key);
}

function ensureSelectedMatch(matches) {
  if (matches.length === 0) {
    selectedMatchKey = "";
    return null;
  }
  const selected = matches.find((match, index) => matchKey(match, index) === selectedMatchKey);
  if (selected) return selected;
  selectedMatchKey = matchKey(matches[0], 0);
  return matches[0];
}

function scoreFor(match) {
  return match.status === "finished" ? match.final_score : match.simulation?.predicted_score;
}

function scoreTextFor(match) {
  const score = scoreFor(match);
  return score ? `${score.home}-${score.away}` : "--";
}

function emptyMatchDetailMarkup() {
  return `
    <div class="detail-top">
      <p class="eyebrow">Match detail</p>
      <h2>No Line Selected</h2>
    </div>
    <p class="detail-copy">Details print after forecast lines arrive.</p>
  `;
}

function matchDetailMarkup(match) {
  const teams = match.teams || [];
  const markets = marketProbabilities(match);
  const scoreLabel = match.status === "finished" ? "Final score" : "Projected score";
  const timeline = match.simulation?.timeline || [];
  const evidence = match.evidence || [];
  const risks = match.risks || [];
  const factors = match.environmental_factors || [];
  const odds = match.status === "finished" ? `
    <div class="detail-odd"><span>Settled</span><strong>${safeText(scoreTextFor(match))}</strong><em>final</em></div>
  ` : markets.map((market) => `
    <div class="detail-odd">
      <span>${safeText(market.label)}</span>
      <strong>${americanOdds(market.value)}</strong>
      <em>${pct(market.value)}% ${market.label === "Draw" ? "draw" : "win"} prob</em>
    </div>
  `).join("");
  const timelineRows = timeline.slice(0, 5).map((event) => `
    <li>
      <time>${safeText(event.minute)}</time>
      <div>
        <strong>${safeText(event.type || "event")}${event.team ? ` · ${safeText(event.team)}` : ""}</strong>
        <p>${safeText(event.description)}</p>
      </div>
      <span>${pct(event.probability)}%</span>
    </li>
  `).join("");
  const riskRows = risks.slice(0, 3).map((risk) => `<li>${safeText(risk)}</li>`).join("");
  const factorRows = factors.slice(0, 2).map((factor) => `<li><strong>${safeText(factor.factor)}</strong><span>${safeText(factor.impact)}</span></li>`).join("");
  const evidenceRows = evidence.slice(0, 2).map((item) => `<li>${safeText(item.claim || item.source || "")}</li>`).join("");

  return `
    <div class="detail-top">
      <div>
        <p class="eyebrow">Match detail</p>
        <h2>${safeText(teams[0] || "Home")} vs ${safeText(teams[1] || "Away")}</h2>
      </div>
      <span>${safeText(matchDescriptor(match))}</span>
    </div>
    <div class="detail-score">
      <span>${scoreLabel}</span>
      <strong>${safeText(scoreTextFor(match))}</strong>
      <em>${safeText(match.confidence || match.status || "open")} confidence</em>
    </div>
    <div class="detail-odds">${odds}</div>
    <section class="detail-section">
      <h3>Simulation Timeline</h3>
      ${timelineRows ? `<ul class="detail-timeline">${timelineRows}</ul>` : `<p class="detail-copy">No timeline events published yet.</p>`}
    </section>
    ${factorRows ? `<section class="detail-section"><h3>Context Factors</h3><ul class="detail-factors">${factorRows}</ul></section>` : ""}
    ${riskRows ? `<section class="detail-section"><h3>Risk Flags</h3><ul class="detail-list">${riskRows}</ul></section>` : ""}
    ${evidenceRows ? `<section class="detail-section"><h3>Evidence</h3><ul class="detail-list">${evidenceRows}</ul></section>` : ""}
  `;
}

function renderFeatured(data) {
  const target = document.querySelector("#featured-market");
  const match = (data.matches || [])[0];
  if (!match) {
    target.innerHTML = emptyPanel("Board warming up", "Forecast cards will appear here as soon as the first prediction ticket lands.", true);
    return;
  }
  const teams = match.teams || [];
  const score = match.status === "finished" ? match.final_score : match.simulation?.predicted_score || { home: "-", away: "-" };
  const scoreLabel = match.status === "finished" ? "Final score" : "Projected score";
  const markets = match.status === "finished" ? `
    <div class="featured-odd settled-odd">
      <span>Settled</span>
      <strong>Final</strong>
      <em>No market</em>
    </div>
  ` : marketProbabilities(match).map((market) => `
    <div class="featured-odd">
      <span>${safeText(market.label)}</span>
      <strong>${americanOdds(market.value)}</strong>
      <em>${pct(market.value)}% ${market.label === "Draw" ? "draw" : "win"} prob</em>
    </div>
  `).join("");
  target.innerHTML = `
    <article class="hero-ticket">
      <div class="hero-context">
        <div>
          <div class="ticket-ribbon">${match.status === "finished" ? "Settled Result" : "Featured Market"}</div>
          <strong>${safeText(teams[0] || "Home")} vs ${safeText(teams[1] || "Away")}</strong>
        </div>
        <span>${safeText(matchDescriptor(match))}</span>
      </div>
      <div class="hero-teams">
        <div><span>${flagFor(teams[0])}</span><strong>${safeText(teams[0] || "Home")}</strong></div>
        <div class="hero-score"><span>${scoreLabel}</span><p>${score.home}<i>-</i>${score.away}</p></div>
        <div><span>${flagFor(teams[1])}</span><strong>${safeText(teams[1] || "Away")}</strong></div>
      </div>
      <div class="odds-explainer">90m 1X2 · American odds · model probability</div>
      <div class="featured-odds">${markets}</div>
    </article>
  `;
}

function renderMatches(data) {
  const target = document.querySelector("#matches");
  const marketCount = document.querySelector("#market-count");
  target.innerHTML = "";
  document.querySelector("#updated").textContent = data.updated_at || "No tickets yet";
  renderGroupFilters(data);

  const allMatches = data.matches || [];
  const matches = allMatches.filter(matchesActiveGroup);
  ensureSelectedMatch(matches.length ? matches : allMatches);
  if (marketCount) {
    marketCount.textContent = allMatches.length
      ? `${matches.length} / ${allMatches.length} markets`
      : "No markets";
  }

  if (allMatches.length === 0) {
    target.innerHTML = emptyPanel("No open lines", "Forecast lines will populate as prediction tickets return.", true);
    return;
  }
  if (matches.length === 0) {
    target.innerHTML = emptyPanel("No lines in this group", "Pick another group or return to All markets.");
    return;
  }
  for (const match of matches) {
    const key = matchKey(match, allMatches.indexOf(match));
    const teams = match.teams || [];
    const markets = marketProbabilities(match);
    const odds = match.status === "finished" ? `
      <div class="settled-cell">
        <span>Settled</span>
        <strong>${safeText(match.final_score ? `${match.final_score.home}-${match.final_score.away}` : "Final")}</strong>
      </div>
    ` : markets.map((market) => `
      <div class="odd-cell" title="${safeText(market.label)} ${pct(market.value)}%">
        <span>${safeText(market.label)}</span>
        <strong>${americanOdds(market.value)}</strong>
        <em>${pct(market.value)}% ${market.label === "Draw" ? "draw" : "win"} prob</em>
      </div>
    `).join("");
    const scoreText = scoreTextFor(match);
    target.insertAdjacentHTML("beforeend", `
      <button class="market-row ${match.status === "finished" ? "is-settled" : ""} ${key === selectedMatchKey ? "is-selected" : ""}" type="button" data-match-key="${safeText(key)}" aria-pressed="${key === selectedMatchKey ? "true" : "false"}">
        <div class="market-meta">
          <span>${safeText(match.round || "Market")}${match.group ? ` / Group ${safeText(match.group)}` : ""}</span>
          <strong>${flagFor(teams[0])} ${safeText(teams[0] || "Home")} <em>vs</em> ${flagFor(teams[1])} ${safeText(teams[1] || "Away")}</strong>
          <small>${match.status === "finished" ? "Final" : "Projected"} ${safeText(scoreText)} · ${match.status === "finished" ? "settled" : safeText(match.confidence || "open")}</small>
        </div>
        <div class="odds-grid">${odds}</div>
        <span class="row-cue">Detail</span>
      </button>
    `);
    if (key === selectedMatchKey) {
      target.insertAdjacentHTML("beforeend", `
        <article class="inline-match-detail">${matchDetailMarkup(match)}</article>
      `);
    }
  }
}

function renderMatchDetail(data) {
  const target = document.querySelector("#match-detail");
  if (!target) return;

  const match = findMatchByKey(data, selectedMatchKey) || ensureSelectedMatch(data.matches || []);
  if (!match) {
    target.innerHTML = emptyMatchDetailMarkup();
    return;
  }

  target.innerHTML = matchDetailMarkup(match);
}

function revealMatchDetailOnMobile() {
  if (window.innerWidth > 820) return;
  const scrollToDetail = () => {
    const detail = document.querySelector("#matches .inline-match-detail") || document.querySelector("#match-detail");
    detail?.scrollIntoView({ behavior: "auto", block: "start" });
  };
  scrollToDetail();
  requestAnimationFrame(scrollToDetail);
  setTimeout(scrollToDetail, 80);
}

function renderOutrights(data) {
  const target = document.querySelector("#outrights");
  target.innerHTML = "";
  const outrights = data.outrights || [];
  if (outrights.length === 0) {
    target.innerHTML = emptyPanel("Futures pending", "Champion prices open after the tournament synthesis ticket returns.");
    return;
  }
  const rows = outrights.slice(0, 10).map((row, index) => `
    <li>
      <span>${index + 1}</span>
      <strong>${flagFor(row.team)} ${safeText(row.team)}</strong>
      <em><strong>${americanOdds(row.probability)}</strong><small>${pct(row.probability)}% title</small></em>
    </li>
  `).join("");
  const favorite = outrights[0] || {};
  target.innerHTML = `
    <div class="champion-banner">
      <span>${flagFor(data.predicted_champion || outrights[0]?.team)}</span>
      <div>
        <p>Board favorite</p>
        <strong>${safeText(data.predicted_champion || outrights[0]?.team)}</strong>
        <em>${pct(favorite.probability)}% title chance</em>
      </div>
    </div>
    <div class="futures-heading"><span>Team</span><span>American odds / title chance</span></div>
    <ul class="futures-list">${rows}</ul>
  `;
}

function renderNarrative(data) {
  const target = document.querySelector("#narrative");
  const lines = data.narrative || [];
  if (lines.length === 0) {
    target.innerHTML = `
      <div class="slip-line"><span>1</span><p>Waiting for tournament synthesis.</p></div>
      <div class="slip-line"><span>2</span><p>Champion futures will lock after all markets are priced.</p></div>
    `;
    return;
  }
  target.innerHTML = lines.slice(0, 5).map((line, index) => `
    <div class="slip-line"><span>${index + 1}</span><p>${safeText(line)}</p></div>
  `).join("");
}

function renderSources(data) {
  const target = document.querySelector("#sources");
  target.innerHTML = "";
  for (const source of data.sources || []) {
    target.insertAdjacentHTML("beforeend", `
      <article class="source-chip">
        <strong>${safeText(source.name)}</strong>
        <span>${safeText(source.status)}</span>
      </article>
    `);
  }
}

function renderDashboardSnapshot(predictions, sources, live, force = false) {
  currentPredictions = predictions || { matches: [] };
  if (force || live.updated_at !== lastLiveStamp) {
    renderLiveState(live);
    lastLiveStamp = live.updated_at;
  }
  if (force || predictions.updated_at !== lastPredictionStamp) {
    renderFeatured(predictions);
    renderMatches(predictions);
    renderMatchDetail(predictions);
    renderOutrights(predictions);
    renderNarrative(predictions);
    lastPredictionStamp = predictions.updated_at;
  }
  if (force || sources.generated_at !== lastSourceStamp) {
    renderSources(sources);
    lastSourceStamp = sources.generated_at;
  }
}

function normalizeReplayFrames(data) {
  return (data.frames || [])
    .filter((frame) => frame && frame.predictions && frame.live)
    .sort((a, b) => {
      const progressA = replayProgress(a);
      const progressB = replayProgress(b);
      if (progressA !== progressB) return progressA - progressB;
      const matchesA = replayMatchCount(a);
      const matchesB = replayMatchCount(b);
      if (matchesA !== matchesB) return matchesA - matchesB;
      return String(a.captured_at || "").localeCompare(String(b.captured_at || ""));
    });
}

function replayProgress(frame) {
  const progress = Number(frame.live?.progress ?? frame.summary?.progress ?? 0);
  const completeBonus = frame.live?.complete || frame.live?.stage === "complete" ? 1 : 0;
  return Math.max(0, Math.min(1, Math.max(progress, completeBonus)));
}

function replayMatchCount(frame) {
  return Number(frame.summary?.matches ?? frame.predictions?.matches?.length ?? 0);
}

function replayControl(id) {
  return document.querySelector(`#${id}`);
}

function stopReplayTimer() {
  if (replayTimer) {
    clearInterval(replayTimer);
    replayTimer = null;
  }
}

function updateReplayControls() {
  const hasFrames = replayFrames.length > 0;
  const deck = replayControl("replay-deck");
  const live = replayControl("replay-live");
  const prev = replayControl("replay-prev");
  const next = replayControl("replay-next");
  const toggle = replayControl("replay-toggle");
  const scrub = replayControl("replay-scrub");
  const status = replayControl("replay-status");
  const activeIndex = Math.max(0, replayIndex);

  deck?.classList.toggle("is-replay", replayMode === "replay");
  if (live) {
    live.disabled = replayMode === "live";
    live.textContent = "Latest";
    live.title = "Show latest published forecast";
    live.setAttribute("aria-label", "Show latest published forecast");
  }
  if (prev) prev.disabled = !hasFrames || activeIndex <= 0;
  if (next) next.disabled = !hasFrames || activeIndex >= replayFrames.length - 1;
  if (toggle) {
    toggle.disabled = !hasFrames;
    toggle.textContent = replayTimer ? "⏸" : "▶";
    toggle.title = replayTimer ? "Pause snapshots" : "Play snapshots";
    toggle.setAttribute("aria-label", replayTimer ? "Pause snapshots" : "Play snapshots");
  }
  if (scrub) {
    scrub.disabled = !hasFrames;
    scrub.max = String(Math.max(0, replayFrames.length - 1));
    scrub.value = String(hasFrames ? activeIndex : 0);
  }
  if (status) {
    const frame = replayFrames[activeIndex];
    status.textContent = hasFrames
      ? replayMode === "replay"
        ? `Snapshot ${activeIndex + 1}/${replayFrames.length}`
        : `${replayFrames.length} snapshots`
      : "No snapshots";
    status.title = frame?.label || "";
  }
}

function showReplayFrame(index) {
  if (!replayFrames.length) return;
  replayMode = "replay";
  replayIndex = Math.max(0, Math.min(replayFrames.length - 1, index));
  const frame = replayFrames[replayIndex];
  renderDashboardSnapshot(
    frame.predictions || { matches: [], outrights: [] },
    frame.sources || { sources: [] },
    frame.live || { stage: "snapshot", message: "", progress: 0 },
    true
  );
  updateReplayControls();
}

function exitReplay() {
  replayMode = "live";
  stopReplayTimer();
  liveNeedsRender = true;
  updateReplayControls();
  refreshDynamic();
}

function startReplay() {
  if (!replayFrames.length) return;
  stopReplayTimer();
  if (replayMode !== "replay") {
    showReplayFrame(0);
  }
  replayTimer = setInterval(() => {
    if (replayIndex >= replayFrames.length - 1) {
      stopReplayTimer();
      updateReplayControls();
      return;
    }
    showReplayFrame(replayIndex + 1);
  }, 1400);
  updateReplayControls();
}

function toggleReplay() {
  if (replayTimer) {
    stopReplayTimer();
    updateReplayControls();
    return;
  }
  startReplay();
}

function refreshReplayData(data) {
  const previousId = replayFrames[replayIndex]?.id;
  const nextFrames = normalizeReplayFrames(data);
  replayFrames = nextFrames;
  if (replayMode === "replay") {
    const sameIndex = replayFrames.findIndex((frame) => frame.id === previousId);
    replayIndex = sameIndex >= 0 ? sameIndex : Math.min(replayIndex, replayFrames.length - 1);
  } else {
    replayIndex = replayFrames.length ? replayFrames.length - 1 : -1;
  }
  updateReplayControls();
}

function setupReplayControls() {
  document.querySelector("#group-filter")?.addEventListener("click", (event) => {
    const button = event.target.closest("[data-group]");
    if (!button) return;
    activeGroup = button.dataset.group || "all";
    renderMatches(currentPredictions);
    renderMatchDetail(currentPredictions);
  });
  document.querySelector("#matches")?.addEventListener("click", (event) => {
    const row = event.target.closest("[data-match-key]");
    if (!row) return;
    selectedMatchKey = row.dataset.matchKey || "";
    renderMatches(currentPredictions);
    renderMatchDetail(currentPredictions);
    revealMatchDetailOnMobile();
  });
  replayControl("replay-live")?.addEventListener("click", exitReplay);
  replayControl("replay-toggle")?.addEventListener("click", toggleReplay);
  replayControl("replay-prev")?.addEventListener("click", () => {
    stopReplayTimer();
    showReplayFrame(replayIndex - 1);
  });
  replayControl("replay-next")?.addEventListener("click", () => {
    stopReplayTimer();
    showReplayFrame(replayIndex + 1);
  });
  replayControl("replay-scrub")?.addEventListener("input", (event) => {
    stopReplayTimer();
    showReplayFrame(Number(event.target.value));
  });
  updateReplayControls();
}

async function main() {
  setupReplayControls();
  const groups = await readJson("data/groups.json", { groups: [] });
  renderGroups(groups);
  await refreshDynamic();
}

async function refreshDynamic() {
  const [predictions, sources, live, replay] = await Promise.all([
    readJson("data/predictions.json", { matches: [] }),
    readJson("data/source-log.json", { sources: [] }),
    readJson("data/live-state.json", { stage: "waiting", message: "Waiting for forecast run.", progress: 0 }),
    readJson("data/replay.json", { frames: [] })
  ]);

  const replayStamp = `${replay.generated_at || ""}:${(replay.frames || []).length}`;
  if (replayStamp !== lastReplayStamp) {
    refreshReplayData(replay);
    lastReplayStamp = replayStamp;
  }
  if (replayMode !== "live") return;

  renderDashboardSnapshot(predictions, sources, live, liveNeedsRender);
  liveNeedsRender = false;
}

main();
setInterval(refreshDynamic, 1000);
