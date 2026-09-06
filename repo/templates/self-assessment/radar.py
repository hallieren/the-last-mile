#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
import argparse
import csv
import math
import pathlib
from xml.sax.saxutils import escape

# Dimension names match Template 3 word for word (CONVENTIONS §2.3)
DIMENSIONS = ["engineering depth", "AI engineering", "business grasp", "narrative", "field judgment"]
CX, CY, R = 230, 230, 160


def load_scores(path):
    with open(path, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    assert [r["dimension"] for r in rows] == DIMENSIONS, (
        f"{path}: must be five rows, with dimension names and order matching Template 3 word for word: {DIMENSIONS}")
    scores = [float(r["score"]) for r in rows]
    assert all(1 <= s <= 5 for s in scores), f"{path}: score must be between 1 and 5"
    return scores


def point(i, r):
    angle = math.radians(-90 + i * 72)
    return CX + r * math.cos(angle), CY + r * math.sin(angle)


def polygon(radii, style):
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in (point(i, r) for i, r in enumerate(radii)))
    return f'<polygon points="{pts}" {style}/>'


def render(scores, title):
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="460" height="460" '
        'font-family="sans-serif" font-size="13">',
        '<rect width="460" height="460" fill="white"/>',
        f'<text x="{CX}" y="26" text-anchor="middle" font-size="15">{escape(title)}</text>',
    ]
    for level in range(1, 6):
        parts.append(polygon([R * level / 5] * 5, 'fill="none" stroke="#cccccc"'))
        parts.append(f'<text x="{CX + 5}" y="{CY - R * level / 5 + 4}" '
                     f'fill="#999999" font-size="10">{level}</text>')
    for i, (dim, score) in enumerate(zip(DIMENSIONS, scores)):
        ax, ay = point(i, R)
        parts.append(f'<line x1="{CX}" y1="{CY}" x2="{ax:.1f}" y2="{ay:.1f}" stroke="#cccccc"/>')
        cos = math.cos(math.radians(-90 + i * 72))
        anchor = "middle" if abs(cos) < 0.3 else ("start" if cos > 0 else "end")
        lx, ly = point(i, R + 22)
        parts.append(f'<text x="{lx:.1f}" y="{ly + 5:.1f}" text-anchor="{anchor}">{dim} {score:g}</text>')
    parts.append(polygon([R * s / 5 for s in scores],
                         'fill="#4472c4" fill-opacity="0.35" stroke="#4472c4" stroke-width="2"'))
    for i, score in enumerate(scores):
        x, y = point(i, R * score / 5)
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="#4472c4"/>')
    parts.append("</svg>")
    return "\n".join(parts)


def main():
    p = argparse.ArgumentParser(
        description="Five-axis radar chart generator (Template 3): reads a dimension,score CSV (CONVENTIONS §2.3), writes SVG.")
    p.add_argument("csv", nargs="?",
                   default=str(pathlib.Path(__file__).parent / "sample" / "radar.csv"),
                   help="radar data CSV (default: demos on sample/radar.csv)")
    p.add_argument("-o", "--out", help="output SVG path (default: same name as the input, .svg)")
    p.add_argument("--title", help="chart title (default: the input file name)")
    args = p.parse_args()
    scores = load_scores(args.csv)
    out = args.out or str(pathlib.Path(args.csv).with_suffix(".svg"))
    pathlib.Path(out).write_text(render(scores, args.title or pathlib.Path(args.csv).stem),
                                 encoding="utf-8")
    low = min(scores)
    print(f"Wrote {out}")
    print(", ".join(f"{d} {s:g}" for d, s in zip(DIMENSIONS, scores)))
    print(f"Lowest axis: {DIMENSIONS[scores.index(low)]} ({low:g}). The lowest axis sets how big a project you can "
          f"own on your own. Spend your next 30 days strengthening only that axis (Template 3.6).")


if __name__ == "__main__":
    main()
