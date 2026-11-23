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
    title = "Darwin Agent"
    title_font = load_font("MPLUSRounded1c-Medium-Latin.ttf", 128)
    title_width = title_font.getlength(title)
    if title_width > 955 * TEXT_SCALE:
        title_font = load_font("MPLUSRounded1c-Medium-Latin.ttf", int(128 * 955 * TEXT_SCALE / title_width))
    body_font = load_font("Inter-Variable.ttf", 26, 450)
    tagline_font = load_font("Inter-Variable.ttf", 26, 700)
    draw.text(
        (4 * TEXT_SCALE, 215 * TEXT_SCALE),
        title,
        font=title_font,
        fill="#151714",
        anchor="ls",
    )
    draw.line(
        (4 * TEXT_SCALE, 255 * TEXT_SCALE, 970 * TEXT_SCALE, 255 * TEXT_SCALE),
        fill="#ff6900",
        width=2 * TEXT_SCALE,
    )
    draw_tracked_text(
        draw,
        (4 * TEXT_SCALE, 310 * TEXT_SCALE),
        "EXPERIENCE  →  ACTION  →  EVOLUTION",
        tagline_font,
        "#151714",
        tracking=0,
    )
    draw.text(
        (4 * TEXT_SCALE, 365 * TEXT_SCALE),
        "Continuously learning. System-level evolution.",
        font=body_font,
        fill="#676962",
        anchor="ls",
    )
    banner.paste(typography.resize((1130, 480), Image.Resampling.LANCZOS), (470, 0))
    banner.save(ASSETS / "darwin-agent-banner.png", optimize=True)


if __name__ == "__main__":
    build()
