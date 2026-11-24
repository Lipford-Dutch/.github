#!/usr/bin/env python3
"""Regenerate GoC org profile stats card + shipping feed.

Reads public, non-fork, non-archived repos of ORG via the REST API and rewrites:
  profile/assets/goc-stats.svg            (animated pulse card, GoC palette)
  profile/README.md  <!-- goc:feed:* -->  (latest pushes / releases)
Private repo names are never written. Uses GITHUB_TOKEN (read-only is enough
for public data; contents:write is only needed by the workflow to commit).
"""
import datetime as dt, json, os, re, urllib.request

ORG = os.environ.get("ORG_LOGIN", "Lipford-Dutch")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
NOW = dt.datetime.now(dt.timezone.utc)
PAL = dict(bg="#07090a", surface="#0b0e10", text="#f4f5f3", muted="#afb4b6",
           amber="#e65f00", green="#3ee6a2", line="#f4f5f3")


def api(path):
    req = urllib.request.Request(f"https://api.github.com/{path}",
                                 headers={"Accept": "application/vnd.github+json",
                                          **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def repos():
    out, page = [], 1
    while True:
        batch = api(f"orgs/{ORG}/repos?type=public&per_page=100&page={page}")
        out += batch
        if len(batch) < 100:
            skip = set(filter(None, os.environ.get("GOC_EXCLUDE", "").split(",")))
            return [r for r in out if not r["fork"] and not r["archived"] and not r["private"]
                    and r["name"] not in skip]
        page += 1


def age(ts):
    return (NOW - dt.datetime.fromisoformat(ts.replace("Z", "+00:00"))).days


def stats_svg(owned):
    active = [r for r in owned if age(r["pushed_at"]) <= 90]
    pages = [r for r in owned if r.get("has_pages")]
    langs = {}
    for r in owned:
        if r.get("language"):
            langs[r["language"]] = langs.get(r["language"], 0) + 1
    top = sorted(langs.items(), key=lambda kv: -kv[1])[:4]
    tiles = [("ACTIVE THEATERS", len(active), PAL["green"]),
             ("PAGES LIVE", len(pages), PAL["amber"]),
             ("PUBLIC BUILDS", len(owned), PAL["text"])]
    # 12-week push sparkline (count of repos pushed per week)
    weeks = [0] * 12
    for r in owned:
        w = age(r["pushed_at"]) // 7
        if w < 12:
            weeks[11 - w] += 1
    mx = max(weeks) or 1
    pts = " ".join(f"{760 + i * 34},{150 - v / mx * 70:.1f}" for i, v in enumerate(weeks))
    t = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 200" width="1200" height="200" role="img" aria-label="Org pulse">',
         '<style>.k{font:800 12px Inter,Segoe UI,Arial,sans-serif;letter-spacing:.24em;fill:#afb4b6}'
         '.v{font:400 64px Impact,Haettenschweiler,Arial Narrow Bold,sans-serif}'
         '.m{font:600 12px ui-monospace,Menlo,Consolas,monospace;fill:#c5c9ca;letter-spacing:.1em}'
         '.draw{stroke-dasharray:600;stroke-dashoffset:600;animation:d 2.4s ease-out forwards}'
         '@keyframes d{to{stroke-dashoffset:0}}@media (prefers-reduced-motion:reduce){.draw{animation:none;stroke-dashoffset:0}}</style>',
         f'<rect width="1200" height="200" rx="14" fill="{PAL["bg"]}" stroke="{PAL["line"]}" stroke-opacity=".18"/>']
    for i, (k, v, c) in enumerate(tiles):
        x = 40 + i * 230
        t.append(f'<text x="{x}" y="58" class="k">{k}</text><text x="{x}" y="132" class="v" fill="{c}">{v}</text>')
    t.append(f'<text x="760" y="58" class="k">12-WEEK PUSH PULSE</text>')
    t.append(f'<polyline points="{pts}" fill="none" stroke="{PAL["amber"]}" stroke-width="3" class="draw"/>')
    t.append('<text x="40" y="176" class="m">' + "  ·  ".join(f"{l.upper()} {n}" for l, n in top) +
             f'  ·  UPDATED {NOW:%Y-%m-%d}</text></svg>')
    return "".join(t)


def feed(owned):
    rows = sorted(owned, key=lambda r: r["pushed_at"], reverse=True)[:6]
    lines = ["| When | Repo | Signal |", "| --- | --- | --- |"]
    for r in rows:
        sig = (r.get("description") or "Push to default branch").replace("|", "/")[:90]
        lines.append(f'| {r["pushed_at"][:10]} | [{r["name"]}]({r["html_url"]}) | {sig} |')
    return "\n".join(lines)


def main():
    owned = repos()
    os.makedirs("profile/assets", exist_ok=True)
    open("profile/assets/goc-stats.svg", "w").write(stats_svg(owned))
    p = "profile/README.md"
    s = open(p).read()
    s = re.sub(r"(<!-- goc:feed:start -->\n).*?(\n<!-- goc:feed:end -->)",
               lambda m: m.group(1) + feed(owned) + m.group(2), s, flags=re.S)
    open(p, "w").write(s)


if __name__ == "__main__":
    main()
