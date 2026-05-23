import click
from .generate import generate_all


@click.group()
def main():
    pass


@main.command()
@click.option("--year", type=int, default=None, help="Season year (default: current)")
def generate(year):
    """Fetch F1 data and regenerate all HTML pages."""
    generate_all(year)


@main.command()
@click.option("--year", type=int, default=None)
def fetch(year):
    """Fetch data only (write data.json, skip HTML)."""
    from . import api
    import json
    from pathlib import Path

    data = api.get_season_data(year)
    out = Path("docs/data.json")
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(data, indent=2))
    click.echo(f"Wrote {out} ({len(data['drivers'])} drivers, {len(data['races'])} races)")
