<!--
  Lipford-Dutch org profile. Sections between goc:* markers are rewritten
  weekly by .github/workflows/goc-profile-refresh.yml (scripts/render_profile.py).
-->

<p align="center">
  <a href="https://cbgoc-cloud.top">
    <img src="./assets/goc-header.svg" alt="Generals of Chaos — Order the chaos. Build. Observe. Iterate." width="100%">
  </a>
</p>

<p align="center">
  <a href="https://cbgoc-cloud.top"><img alt="cbgoc-cloud.top" src="https://img.shields.io/badge/HQ-cbgoc--cloud.top-e65f00?style=for-the-badge&labelColor=07090a"></a>
  <a href="https://github.com/Lipford-Dutch/GOC-Base-Repo-Template"><img alt="Repo template" src="https://img.shields.io/badge/kickoff-GOC_Base_Template-3ee6a2?style=for-the-badge&labelColor=07090a"></a>
  <a href="https://lipford-dutch.github.io/goc-guide-library/"><img alt="Guide library" src="https://img.shields.io/badge/field_guides-library-f4f5f3?style=for-the-badge&labelColor=07090a"></a>
  <img alt="Base" src="https://img.shields.io/badge/base-Carolina_Beach,_NC-afb4b6?style=for-the-badge&labelColor=07090a">
</p>

<h3 align="center">A proving ground for infrastructure, observability, commerce, civic systems,<br>and the ideas we refuse to leave on paper.</h3>

<img src="./assets/goc-divider.svg" width="100%" alt="">

## ⚔️ Active theaters

<!-- goc:theaters:start -->
<table>
<tr>
<td width="33%" valign="top">

**01 · Wireless Cellular SoT**<br>
<sub>Nautobot app for wireless and cellular routers, SIM cards and carrier source-of-truth workflows.</sub><br>
[repo](https://github.com/Lipford-Dutch/nautobot-wireless-cellular-sot-app) · [launch page](https://lipford-dutch.github.io/nautobot-wireless-cellular-sot-app/cellular.html)

</td>
<td width="33%" valign="top">

**02 · Nautobot Custom Metrics**<br>
<sub>Alpha Nautobot app for ROI, activity and platform telemetry metrics.</sub><br>
[repo](https://github.com/Lipford-Dutch/nautobot-app-custom-metrics) · [launch page](https://lipford-dutch.github.io/nautobot-app-custom-metrics/)

</td>
<td width="33%" valign="top">

**03 · F5 Staging Precheck**<br>
<sub>Parallel SSH and iControl REST audit framework for F5 BIG-IP change-window readiness.</sub><br>
[repo](https://github.com/Lipford-Dutch/f5-staging-precheck) · [docs](https://lipford-dutch.github.io/f5-staging-precheck/)

</td>
</tr>
<tr>
<td valign="top">

**04 · Citizen Karen**<br>
<sub>Consent-first civic complaint intake and tracking demo with accessible workflows and observability. Not a government service.</sub><br>
[repo](https://github.com/Lipford-Dutch/citizen-karen-platform) · [demo](https://lipford-dutch.github.io/citizen-karen-platform/)

</td>
<td valign="top">

**05 · Carolina Beach 411**<br>
<sub>Mobile-first guide to Carolina Beach vendors, Town News, beach-day planning and seasonal themes.</sub><br>
[repo](https://github.com/Lipford-Dutch/carolina-beach-local-411) · [live guide](https://lipford-dutch.github.io/carolina-beach-local-411/)

</td>
<td valign="top">

**06 · GOC Base Repo Template**<br>
<sub>Day-zero kickoff for every new repo: docs, CI/CD, security, triage, Pages and release governance.</sub><br>
[template](https://github.com/Lipford-Dutch/GOC-Base-Repo-Template) · [docs](https://lipford-dutch.github.io/GOC-Base-Repo-Template/)

</td>
</tr>
</table>
<!-- goc:theaters:end -->

## 🛰️ What we're shipping

<!-- goc:feed:start -->
| When | Repo | Signal |
| --- | --- | --- |
| 2026-11-24 | [.github](https://github.com/Lipford-Dutch/.github) | Public org profile for Generals of Chaos (Lipford-Dutch): animated header, active theaters |
| 2026-11-24 | [goc-guide-library](https://github.com/Lipford-Dutch/goc-guide-library) | GoC step-by-step guide library. |
| 2026-11-24 | [Hannah-Huffman-Wealth-Horizon](https://github.com/Lipford-Dutch/Hannah-Huffman-Wealth-Horizon) | Hannah's Wealth Horizon: an interactive 10-year family roadmap for financial independence, |
| 2026-11-24 | [GOC-DEMO-ASSETS-1](https://github.com/Lipford-Dutch/GOC-DEMO-ASSETS-1) | Various Generals of Chaos Demo Assets |
| 2026-11-24 | [f5-staging-precheck](https://github.com/Lipford-Dutch/f5-staging-precheck) | check_multi 2.0 + bigip-precheck: parallel SSH and iControl REST audit framework for F5 BI |
| 2026-11-24 | [citizen-karen-platform](https://github.com/Lipford-Dutch/citizen-karen-platform) | Consent-first civic complaint intake and tracking demo with plugin-driven agency simulatio |
<!-- goc:feed:end -->

<p align="center">
  <!-- goc:stats:start -->
  <img src="./assets/goc-stats.svg" alt="Org pulse: active repos, commits in the last 90 days, Pages sites live" width="100%">
  <!-- goc:stats:end -->
</p>

## 🧭 Workstreams

| Lane | What lives here |
| --- | --- |
| **Network source of truth** | Nautobot apps for cellular SoT and custom metrics; [OpenNMS MCP](https://github.com/Lipford-Dutch/opennms-mcp) exposes alarms, nodes and events to MCP clients. |
| **Upgrade readiness** | F5 BIG-IP prechecks and zero-touch TMOS upgrade automation. |
| **Observability fabric** | Nautobot → Prometheus + OTEL → Grafana, with OpenNMS + Kafka planned upstream. |
| **Civic & local** | Citizen Karen civic intake demo and the Carolina Beach 411 local guide. |
| **Commerce & brand** | [Pleasure Island Design](https://www.pleasureislanddesign.com), Nollies and Hoplite on [cbgoc-cloud.top](https://cbgoc-cloud.top). |
| **Field manuals** | [WTFManuals](https://github.com/Lipford-Dutch/wtfmanuals), the [guide library](https://lipford-dutch.github.io/goc-guide-library/) and the base repo template. |
| **Contractor tech** | Keith's Contractor Takeoff and Ködade ADE lanes (see [@ContractorKeith](https://github.com/ContractorKeith)). |

```mermaid
flowchart LR
  SoT["Nautobot + apps<br/>inventory · compliance · cellular"] --> Collect["Prometheus + OTEL<br/>(planned)"]
  Collect --> Grafana["Grafana<br/>dashboards"]
  NMS["OpenNMS + Kafka<br/>(planned)"] --> Grafana
  SoT -. MCP .-> Agents["AI agents / operators"]
  NMS -. MCP .-> Agents
```

## 🎖️ The Generals

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/willyd61"><img src="https://github.com/willyd61.png" width="64" align="left" alt="Will Lipford"></a>

**[Will Lipford](https://github.com/willyd61)** · Carolina Beach<br>
<sub>Network automation, DevOps and field systems. Turns messy operating reality into Nautobot apps, CI pipelines and launch pages.</sub>
</td>
<td width="50%" valign="top">
<a href="https://github.com/ContractorKeith"><img src="https://github.com/ContractorKeith.png" width="64" align="left" alt="Keith Bloemendaal"></a>

**[Keith Bloemendaal](https://github.com/ContractorKeith)** · [contractorkeith.com](http://contractorkeith.com)<br>
<sub>37 years in the trades, now an agentic engineer. Building Ködade ADE (open source) and Contractor Takeoff.</sub>
</td>
</tr>
</table>

## 🧰 Stack

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-07090a?style=flat-square&logo=python&logoColor=3ee6a2">
  <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-07090a?style=flat-square&logo=typescript&logoColor=3ee6a2">
  <img alt="Rust" src="https://img.shields.io/badge/Rust-07090a?style=flat-square&logo=rust&logoColor=e65f00">
  <img alt="Go" src="https://img.shields.io/badge/Go-07090a?style=flat-square&logo=go&logoColor=3ee6a2">
  <img alt="Nautobot" src="https://img.shields.io/badge/Nautobot-07090a?style=flat-square&logoColor=e65f00">
  <img alt="Django" src="https://img.shields.io/badge/Django-07090a?style=flat-square&logo=django&logoColor=3ee6a2">
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-07090a?style=flat-square&logo=fastapi&logoColor=3ee6a2">
  <img alt="Ansible" src="https://img.shields.io/badge/Ansible-07090a?style=flat-square&logo=ansible&logoColor=e65f00">
  <img alt="Grafana" src="https://img.shields.io/badge/Grafana-07090a?style=flat-square&logo=grafana&logoColor=e65f00">
  <img alt="Prometheus" src="https://img.shields.io/badge/Prometheus-07090a?style=flat-square&logo=prometheus&logoColor=e65f00">
  <img alt="OpenTelemetry" src="https://img.shields.io/badge/OpenTelemetry-07090a?style=flat-square&logo=opentelemetry&logoColor=3ee6a2">
  <img alt="MCP" src="https://img.shields.io/badge/Model_Context_Protocol-07090a?style=flat-square&logoColor=e65f00">
  <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub_Actions-07090a?style=flat-square&logo=githubactions&logoColor=3ee6a2">
  <img alt="GitHub Pages" src="https://img.shields.io/badge/GitHub_Pages-07090a?style=flat-square&logo=github&logoColor=f4f5f3">
</p>

## 📡 Rules of engagement

- Every repo is **active**, **reference** or **archived**. No silent clutter.
- New repos start from the [GOC Base Repo Template](https://github.com/Lipford-Dutch/GOC-Base-Repo-Template).
- Proof lives next to the code: CI, docs and a launch page for anything we call shipped.
- Client and product lanes stay private until cleared.

<img src="./assets/goc-divider.svg" width="100%" alt="">

<p align="center"><sub><b>GENERALS OF CHAOS</b> / Build. Observe. Iterate. · <a href="https://cbgoc-cloud.top">cbgoc-cloud.top</a></sub></p>
