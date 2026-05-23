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
uv sync
python main.py
```

---

Managed by [policy-orchestrator](https://github.com/jthorvaldur/policy-orchestrator).
