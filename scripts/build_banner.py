"""Compose the team banner from the existing DA brand asset."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
FONT_ROOT = Path("/usr/share/fonts/truetype/dejavu")


def build():
    banner = Image.new("RGB", (1600, 480), "#f2f0e9")
    mark = Image.open(ASSETS / "darwin-mark-da-orange.png").convert("RGBA")
    mark.thumbnail((360, 360), Image.Resampling.LANCZOS)
    banner.paste(mark, (70, 60), mark)
    draw = ImageDraw.Draw(banner)
    title_font = ImageFont.truetype(str(FONT_ROOT / "DejaVuSans-Bold.ttf"), 82)
    body_font = ImageFont.truetype(str(FONT_ROOT / "DejaVuSans.ttf"), 28)
    tagline_font = ImageFont.truetype(str(FONT_ROOT / "DejaVuSans-Bold.ttf"), 30)
    draw.text((470, 124), "Darwin Agent", font=title_font, fill="#151714")
    draw.line((474, 245, 1440, 245), fill="#ff6900", width=4)
    draw.text((474, 272), "EXPERIENCE  →  ACTION  →  EVOLUTION", font=tagline_font, fill="#151714")
    draw.text((474, 337), "Continuously learning. System-level evolution.", font=body_font, fill="#676962")
    banner.save(ASSETS / "darwin-agent-banner.png", optimize=True)


if __name__ == "__main__":
    build()
