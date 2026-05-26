"""Generate Open Graph preview images for social sharing.

Creates 1200x630 dark-themed cards with page title and subtitle.
Matches the site's #0d1117 background with monospace typography.
"""
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

DOCS_DIR = Path(__file__).resolve().parent.parent.parent / "docs" / "og"
WIDTH, HEIGHT = 1200, 630
BG = (13, 17, 23)
ACCENT = (88, 166, 255)
TEXT = (240, 246, 252)
MUTED = (139, 148, 158)
BORDER = (48, 54, 61)

PAGES = {
    "index": {"title": "F1 2026 Season", "subtitle": "Championship standings, race results, and 23 analysis pages", "accent": (0, 210, 190)},
    "coherence": {"title": "Δ.72 Coherence", "subtitle": "First application of the coherence framework to F1", "accent": (187, 154, 247)},
    "montecarlo": {"title": "Monte Carlo Projection", "subtitle": "10,000 simulated seasons — championship probability", "accent": (63, 185, 80)},
    "elo": {"title": "Elo Ratings", "subtitle": "Pairwise skill ratings separating driver from car", "accent": (88, 166, 255)},
    "entropy": {"title": "Championship Entropy", "subtitle": "Shannon entropy — measuring competitiveness", "accent": (210, 153, 34)},
    "nonlinear": {"title": "Nonlinear Dynamics", "subtitle": "Gini, HHI, Lorenz, Zipf — 16-season comparison", "accent": (187, 154, 247)},
    "prediction": {"title": "Next Race Prediction", "subtitle": "Bayesian model — form, momentum, consistency", "accent": (63, 185, 80)},
    "markets": {"title": "Prediction Markets", "subtitle": "Model vs Polymarket — edge detection, Kelly sizing", "accent": (210, 153, 34)},
    "profiles": {"title": "Driver Profiles", "subtitle": "Big Five, radar charts, 22 psychological archetypes", "accent": (187, 154, 247)},
    "physics": {"title": "The Physics of F1", "subtitle": "Forces, energy, thermodynamics, tire friction", "accent": (248, 81, 73)},
    "technology": {"title": "F1 Technology", "subtitle": "Power unit architecture, active aero, sensors", "accent": (88, 166, 255)},
    "hft": {"title": "High-Frequency Trading", "subtitle": "1969–2026: firms, timeline, market venues", "accent": (63, 185, 80)},
    "hft-tech": {"title": "HFT Latency Stack", "subtitle": "2,000,000× improvement — fiber to ASIC", "accent": (210, 153, 34)},
    "hft-routes": {"title": "Microwave Routes", "subtitle": "Tower by tower — the arb math of light speed", "accent": (248, 81, 73)},
}


def generate_og_image(page_id: str, title: str, subtitle: str, accent: tuple, output_dir: Path) -> Path:
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, WIDTH - 1, HEIGHT - 1], outline=BORDER, width=2)
    draw.rectangle([0, 0, WIDTH, 4], fill=accent)

    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 48)
        sub_font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 24)
        brand_font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 16)
    except (OSError, IOError):
        try:
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 48)
            sub_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 24)
            brand_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 16)
        except (OSError, IOError):
            title_font = ImageFont.load_default()
            sub_font = ImageFont.load_default()
            brand_font = ImageFont.load_default()

    draw.text((60, 200), title, fill=TEXT, font=title_font)
    draw.text((60, 270), subtitle, fill=MUTED, font=sub_font)
    draw.text((60, HEIGHT - 60), "jthorvaldur.github.io", fill=(*accent, 180), font=brand_font)
    draw.text((WIDTH - 200, HEIGHT - 60), "Thorarinson", fill=MUTED, font=brand_font)

    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / f"{page_id}.png"
    img.save(out_path, "PNG", optimize=True)
    return out_path


def generate_all():
    if not HAS_PIL:
        print("  SKIP og images (Pillow not installed)")
        return

    count = 0
    for page_id, info in PAGES.items():
        try:
            generate_og_image(page_id, info["title"], info["subtitle"], info["accent"], DOCS_DIR)
            count += 1
        except Exception as e:
            print(f"  WARN og/{page_id}.png: {e}")
    print(f"  OK   og/ ({count} images)")
