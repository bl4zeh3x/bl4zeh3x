"""Build the transparent light/dark chart used by the profile README."""

from pathlib import Path
import re

CHARTS = Path(__file__).resolve().parents[2] / "profile-3d-contrib"

CSS = """* {font-family:"Ubuntu","Helvetica","Arial",sans-serif}
.day{display:inline}
.night{display:none}
@media (prefers-color-scheme:dark){.day{display:none}.night{display:inline}}
.day text{paint-order:stroke fill;stroke:#fff;stroke-width:2px;stroke-linejoin:round}
.night text{paint-order:stroke fill;stroke:#00000f;stroke-width:2px;stroke-linejoin:round}"""


def chart(filename, background):
    svg = (CHARTS / filename).read_text(encoding="utf-8")
    if not svg.startswith("<svg ") or "</svg>" not in svg:
        raise ValueError(f"Unexpected SVG source: {filename}")
    inner = svg.split(">", 1)[1].rsplit("</svg>", 1)[0]
    inner = re.sub(r"^<style>.*?</style>", "", inner, count=1, flags=re.S)
    bg = f'<rect x="0" y="0" width="1280" height="850" fill="{background}"></rect>'
    if not inner.startswith(bg):
        raise ValueError(f"Unexpected SVG background: {filename}")
    return inner[len(bg):]


day = chart("profile-green-animate.svg", "#ffffff")
night = chart("profile-night-green.svg", "#00000f")
output = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="850" '
    'viewBox="0 0 1280 850">'
    f"<style>{CSS}</style>"
    f'<g class="day">{day}</g>'
    f'<g class="night">{night}</g>'
    "</svg>\n"
)
(CHARTS / "profile-adaptive.svg").write_text(output, encoding="utf-8")
