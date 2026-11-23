"""Compose the team banner from the existing DA brand asset."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
FONT_ROOT = ASSETS / "fonts"
TEXT_SCALE = 3


def load_font(filename, size, weight=None):
    font = ImageFont.truetype(str(FONT_ROOT / filename), size * TEXT_SCALE)
    if weight is not None:
        font.set_variation_by_axes([min(32, max(14, size)), weight])
    return font


def draw_tracked_text(draw, position, text, font, fill, tracking):
    cursor, baseline = position
    for index, character in enumerate(text):
        draw.text((cursor, baseline), character, font=font, fill=fill, anchor="ls")
        if index + 1 < len(text):
            following = text[index + 1]
            cursor += font.getlength(character + following) - font.getlength(following)
            cursor += tracking * TEXT_SCALE


def build():
    banner = Image.new("RGB", (1600, 480), "#f2f0e9")
    mark = Image.open(ASSETS / "darwin-mark-da-orange.png").convert("RGBA")
    mark.thumbnail((360, 360), Image.Resampling.LANCZOS)
    banner.paste(mark, (70, 60), mark)
    typography = Image.new("RGB", (1130 * TEXT_SCALE, 480 * TEXT_SCALE), "#f2f0e9")
    draw = ImageDraw.Draw(typography)
    title = "DARWIN AGENT"
    title_font = load_font("LuckiestGuy-Regular.ttf", 132)
    title_width = title_font.getlength(title)
    if title_width > 955 * TEXT_SCALE:
        title_font = load_font("LuckiestGuy-Regular.ttf", int(132 * 955 * TEXT_SCALE / title_width))
    body_font = load_font("Inter-Variable.ttf", 27, 450)
    tagline_font = load_font("Inter-Variable.ttf", 28, 750)
    draw.text(
        (10 * TEXT_SCALE, 222 * TEXT_SCALE),
        title,
        font=title_font,
        fill="#ff6900",
        anchor="ls",
    )
    draw.text(
        (4 * TEXT_SCALE, 216 * TEXT_SCALE),
        title,
        font=title_font,
        fill="#151714",
        anchor="ls",
    )
    draw.line(
        (4 * TEXT_SCALE, 260 * TEXT_SCALE, 970 * TEXT_SCALE, 260 * TEXT_SCALE),
        fill="#ff6900",
        width=3 * TEXT_SCALE,
    )
    draw_tracked_text(
        draw,
        (4 * TEXT_SCALE, 318 * TEXT_SCALE),
        "EXPERIENCE  →  ACTION  →  EVOLUTION",
        tagline_font,
        "#151714",
        tracking=0.8,
    )
    draw.text(
        (4 * TEXT_SCALE, 373 * TEXT_SCALE),
        "Continuously learning. System-level evolution.",
        font=body_font,
        fill="#676962",
        anchor="ls",
    )
    banner.paste(typography.resize((1130, 480), Image.Resampling.LANCZOS), (470, 0))
    banner.save(ASSETS / "darwin-agent-banner.png", optimize=True)


if __name__ == "__main__":
    build()
