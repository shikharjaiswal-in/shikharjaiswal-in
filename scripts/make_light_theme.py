"""
Generate light-theme variants of the animated profile SVGs.

Reads each dark asset and rewrites its color tokens to light-mode equivalents,
producing assets/<name>-light.svg. The README serves them via <picture> +
prefers-color-scheme so GitHub picks the right one per theme.

terminal.svg is intentionally excluded -- a terminal stays dark in both themes.

Run after any edit to the dark assets:
    python scripts/make_light_theme.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")

FILES = ["hero.svg", "capabilities.svg", "beyond.svg", "footer.svg"]

# dark -> light token map. Machines become "line art": light fills, medium
# strokes. Scene backgrounds fade to white so the borderless mask melts into
# GitHub's light page exactly like the dark one does on #0d1117.
COLOR_MAP = {
    # scene backgrounds
    "#0d1420": "#e9eff7",
    "#0a0e14": "#f8fafc",
    "#080b10": "#ffffff",
    "#11202e": "#dde6ef",
    # structure / chrome
    "#1f6feb": "#5b8dd9",
    "#30363d": "#6e7c8a",
    "#3d4b5c": "#5f6f80",
    "#4b5563": "#5a636d",
    "#1f2d3d": "#b3c0cd",
    # machine bodies -> light fills
    "#161b22": "#eef1f5",
    "#1c2430": "#e3e9ef",
    "#0f1826": "#e8edf2",
    "#0a1a2a": "#d9e5f1",
    "#0e3a5c": "#b9d4ee",
    "#0a2540": "#cfe2f3",
    # text
    "#c9d1d9": "#2a323c",
    "#e6edf3": "#1f2833",
    "#7d8590": "#57606a",
    # stars
    "#9fb4d8": "#8496b3",
    # accents (darkened for contrast on white)
    "#22d3ee": "#0e93ad",
    "#58a6ff": "#2b6fdb",
    "#818cf8": "#5b62d9",
    "#39d353": "#188038",
    "#f2cc60": "#b08800",
}

for name in FILES:
    src = os.path.join(ASSETS, name)
    dst = os.path.join(ASSETS, name.replace(".svg", "-light.svg"))
    svg = open(src, encoding="utf-8").read()
    for dark, light in COLOR_MAP.items():
        svg = svg.replace(dark, light)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", dst, len(svg), "bytes")
