"""Build the transparent, light/dark SVG used by the profile README."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2] / "profile-3d-contrib"


def chart(name, background):
    source = (ROOT / name).read_text(encoding="utf-8")
    source = re.sub(r'^<svg[^>]*>', '', source, count=1)
    source = re.sub(r'</svg>\\s*$', '', source, count=1)
    source = re.sub(r'^<style>[\\s\\S]*?</style>', '', source, count=1)
    pattern = rf'^<rect x="0" y="0" width="1280" height="850" fill="{background}"></rect>'
    if not re.match(pattern, source):
        raise ValueError(f"Unexpected background for {name}; review the generator output")
    return re.sub(pattern, '', source, count=1)


css = "* {font-family:\"Ubuntu\",\"Helvetica\",\"Arial\",sans-serif}\n.day{display:inline}\n.night{display:none}\n@media (prefers-color-scheme:dark){.day{display:none}.night{display:inline}}\n.day text{paint-order:stroke fill;stroke:#fff;stroke-width:2px;stroke-linejoin:round}\n.night text{paint-order:stroke fill;stroke:#00000f;stroke-width:2px;stroke-linejoin:round}"
day = chart("profile-green-animate.svg", "#ffffff")
night = chart("profile-night-green.svg", "#00000f")
output = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="850" '
    'viewBox="0 0 1280 850"><style>' + css + '</style>'
    '<g class="day">' + day + '</g>'
    '<g class="night">' + night + '</g></svg>\\n'
)
(ROOT / "profile-adaptive.svg").write_text(output, encoding="utf-8")
