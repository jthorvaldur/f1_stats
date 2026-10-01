# F1 2026 Season Statistics

Live site: **[jthorvaldur.github.io/f1_stats](https://jthorvaldur.github.io/f1_stats/)**

Static site tracking the 2026 Formula 1 season. Data sourced from the [Jolpica/Ergast F1 API](https://github.com/jolpica/jolpica-f1).

## Pages

- **Championship Standings** — driver and constructor points tables
- **Race Results** — round-by-round finishing order
- **Age Distribution** — driver age analysis across the grid
- **Weight Distribution** — driver weight analysis across the grid

## Stack

- Python (click, httpx, tqdm) for data fetching
- Static HTML/CSS/JS served via GitHub Pages (`docs/`)

## Setup

```bash
uv sync --locked
uv run --locked f1stats generate
```

Generation fetches live API data and writes all pages, JSON, sitemap, and preview images to `docs/`.
Use `uv run --locked f1stats generate --year 2026` to select a season explicitly.

## Validation and publishing

Python 3.12+ and Node.js 22+ are required for validation:

```bash
bash scripts/test.sh
uv run --locked python scripts/check_pages.py
```

The regression tests render mixed, unknown, and empty age datasets and execute the
page's JavaScript. The page checker verifies all expected generated pages, compiles
their inline JavaScript, and parses the generated JSON and sitemap.

Pull requests run validation with read-only permissions. The weekly workflow runs
tests, generates pages, validates them, then commits `docs/` on `main`. Manual runs
on other branches are skipped. Commit dates are calendar dates, not F1 round numbers.

GitHub Pages serves `main:/docs`. After successful regeneration the workflow explicitly
[requests a Pages build](https://docs.github.com/en/rest/pages/pages#request-a-github-pages-build),
because [pushes using `GITHUB_TOKEN` do not trigger Pages builds](https://docs.github.com/en/actions/concepts/security/github_token).
The request queues a separate Pages build; check its result in Actions to confirm publication.

---

Managed by [policy-orchestrator](https://github.com/jthorvaldur/policy-orchestrator).
