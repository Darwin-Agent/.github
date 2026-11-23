# Darwin Agent Organization Profile

`profile/README.md` is the public introduction displayed on the
[Darwin-Agent organization page](https://github.com/Darwin-Agent).

The official team website is <https://darwin-agent.github.io/>. Website code and
GitHub Pages configuration live in
[Darwin-Agent/darwin-agent.github.io](https://github.com/Darwin-Agent/darwin-agent.github.io),
not in a member's personal account.

## Brand assets

- `assets/darwin-mark-da-orange.png`: reviewed softer third-candidate DA monogram, orange `#FF6900`.
- `assets/darwin-agent-banner.png`: shared banner composed from the current monogram.
- `scripts/build_banner.py`: Pillow-based banner generator using the bundled M PLUS Rounded 1c and Inter fonts.
- `assets/fonts/`: bundled font files and their original license notices.

Rebuild the banner with `python scripts/build_banner.py` after installing Pillow.
M PLUS Rounded 1c provides a medium-weight rounded title. The layout uses a single
orange divider, with no title shadow or added effects. Inter provides the tagline
and supporting text. Typography is rendered at 3× resolution before downsampling.
The DA monogram asset, placement, size, background, and banner dimensions remain unchanged.

Font sources: [M PLUS Rounded 1c](https://github.com/google/fonts/tree/main/ofl/roundedmplus1c)
and [Inter](https://github.com/google/fonts/tree/main/ofl/inter) from Google Fonts.

The original website and initial logo were prepared by Shaokun. Their source
history is preserved in the website repository. The current logo is a reviewed
image-generated revision; earlier assets remain recoverable through history.
No new license is assigned here.

The organization avatar is a separate GitHub setting. If it does not yet use
the new identity, upload `assets/darwin-mark-da-orange.png` in the organization's
profile settings. Keep the monogram's existing clear space and aspect ratio.
