# Lipford-Dutch / .github

Public home of the **Generals of Chaos** GitHub organization profile.

GitHub renders the org landing page at <https://github.com/Lipford-Dutch> from
[`profile/README.md`](profile/README.md).

| Path | Purpose |
| --- | --- |
| `profile/README.md` | The org profile |
| `profile/assets/` | Animated header, divider and the generated pulse card (SVG, GoC palette) |
| `scripts/render_profile.py` | Rebuilds the pulse card and the "What we're shipping" feed from public, non-fork repos |
| `.github/workflows/goc-profile-refresh.yml` | Runs the script every Monday and on manual dispatch |

## Rules

- Only public, non-fork, non-archived repos appear in generated sections.
- No private repo names, internal hostnames, IPs or credentials in this repo.
- Run locally with `GITHUB_TOKEN=<read-only token> python scripts/render_profile.py`.

Palette: `#07090a` background, `#f4f5f3` text, `#e65f00` amber, `#3ee6a2` green,
matching <https://cbgoc-cloud.top>.

## Discussions

Org conversation lives in [Discussions](https://github.com/Lipford-Dutch/.github/discussions): Announcements, Show and tell, Q&A, Ideas, and General (used for the public roadmap until a Roadmap category is added in the repo settings).
