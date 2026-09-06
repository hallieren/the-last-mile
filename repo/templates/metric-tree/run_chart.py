#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
"""Run chart SVG generator: baseline median + automatic special cause flagging (six points on one side, Template 18.1).

CSV format follows the repo's CONVENTIONS §2.2: header row period,value.
Sample data illustrates the book's Anchor & Helm North Star (first-touch handling time for auto exceptions, hours, the -18% to -22% segment).
"""
import argparse
import csv
import pathlib
from statistics import median
from xml.sax.saxutils import escape

HERE = pathlib.Path(__file__).parent


def six_point_runs(values, med):
    """The six-points-on-one-side rule comes from The Health Care Data Guide (as
    paraphrased in Template 18.1.3): six or more consecutive points on the same
    side of the baseline median is a special cause signal. A point that lands
    exactly on the median neither counts nor breaks the run."""
    runs, cur, side = [], [], 0
    for i, v in enumerate(values):
        s = 1 if v > med else (-1 if v < med else 0)
        if s == 0:
            continue
        if s == side:
            cur.append(i)
        else:
            if len(cur) >= 6:
                runs.append((cur, side))
            cur, side = [i], s
    if len(cur) >= 6:
        runs.append((cur, side))
    return runs


def main():
    ap = argparse.ArgumentParser(
        description="Read a period,value CSV and draw a run chart SVG, auto-flagging special cause (Template 18)")
    ap.add_argument("csv", nargs="?", default=str(HERE / "sample" / "run-chart.csv"),
                    help="CSV path (defaults to the sample/ Anchor & Helm example)")
    ap.add_argument("--baseline", type=int, default=6,
                    help="Use the first N points to compute the baseline median (Template 18.1.3: the pre-launch baseline segment)")
    ap.add_argument("--title", default="first-touch handling time for auto exceptions (weekly median, hours)", help="Chart title")
    ap.add_argument("--out", help="Output SVG path (defaults to the CSV's name with a .svg extension)")
    args = ap.parse_args()

    with open(args.csv, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    assert rows and "period" in rows[0] and "value" in rows[0], \
        "CSV needs a period,value header row (CONVENTIONS §2.2)"
    periods = [r["period"] for r in rows]
    values = [float(r["value"]) for r in rows]
    n_base = min(args.baseline, len(values))
    med = median(values[:n_base])
    runs = six_point_runs(values, med)

    # Canvas and coordinates
    W, H, L, R, T, B = 760, 420, 64, 28, 56, 64
    pw, ph = W - L - R, H - T - B
    lo, hi = min(values + [med]), max(values + [med])
    pad = (hi - lo) * 0.15 or 1
    lo, hi = lo - pad, hi + pad
    xs = [L + pw * (i + 0.5) / len(values) for i in range(len(values))]
    ys = [T + ph * (hi - v) / (hi - lo) for v in values]
    y_med = T + ph * (hi - med) / (hi - lo)

    p = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
         'font-family="sans-serif">' % (W, H),
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
         f'<text x="{L}" y="26" font-size="15" fill="#1a1a1a">{escape(args.title)}</text>',
         f'<text x="{L}" y="44" font-size="11" fill="#707070">'
         f'Baseline = median of the first {n_base} points, {med:g}. Special cause rule: six points in a row on one side '
         '(The Health Care Data Guide)</text>']
    # Horizontal grid + y-axis ticks (recessive)
    for k in range(5):
        gy = T + ph * k / 4
        gv = hi - (hi - lo) * k / 4
        p.append(f'<line x1="{L}" y1="{gy:.1f}" x2="{W - R}" y2="{gy:.1f}" '
                 'stroke="#ececec" stroke-width="1"/>')
        p.append(f'<text x="{L - 8}" y="{gy + 4:.1f}" font-size="11" fill="#707070" '
                 f'text-anchor="end">{gv:.1f}</text>')
    # Special cause segment background + label (text label, not just color)
    for idx, side in runs:
        x0, x1 = xs[idx[0]] - 12, xs[idx[-1]] + 12
        word = "above" if side > 0 else "below"
        p.append(f'<rect x="{x0:.1f}" y="{T}" width="{x1 - x0:.1f}" height="{ph}" '
                 'fill="#c4461d" opacity="0.07"/>')
        p.append(f'<text x="{x0:.1f}" y="{T + 14}" font-size="11" fill="#c4461d">'
                 f'special cause: {len(idx)} points in a row {word} the median</text>')
    # Median line (dashed) + right-side label
    p.append(f'<line x1="{L}" y1="{y_med:.1f}" x2="{W - R}" y2="{y_med:.1f}" '
             'stroke="#8a8a8a" stroke-width="1.5" stroke-dasharray="6 4"/>')
    p.append(f'<text x="{W - R}" y="{y_med - 6:.1f}" font-size="11" fill="#555555" '
             f'text-anchor="end">baseline median {med:g}</text>')
    # Data line + points (points inside a special cause segment change color)
    flagged = {i for idx, _ in runs for i in idx}
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in zip(xs, ys))
    p.append(f'<polyline points="{pts}" fill="none" stroke="#4269d0" stroke-width="2"/>')
    for i, (x, y) in enumerate(zip(xs, ys)):
        color = "#c4461d" if i in flagged else "#4269d0"
        p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#ffffff" '
                 f'stroke="{color}" stroke-width="2"/>')
    # x-axis labels (every point shown, no cherry-picking weeks, Template 18.1.3)
    for x, label in zip(xs, periods):
        p.append(f'<text x="{x:.1f}" y="{H - B + 20}" font-size="11" fill="#707070" '
                 f'text-anchor="middle">{escape(label)}</text>')
    p.append("</svg>")

    out = pathlib.Path(args.out or pathlib.Path(args.csv).with_suffix(".svg"))
    out.write_text("\n".join(p), encoding="utf-8")

    print(f"Points {len(values)}, baseline median (first {n_base} points) = {med:g}")
    for idx, side in runs:
        word = "above" if side > 0 else "below"
        print(f"special cause: {periods[idx[0]]}–{periods[idx[-1]]}, "
              f"{len(idx)} points in a row {word} the median")
    if not runs:
        print("No special cause signal detected (an improvement claim should not be made yet, Template 18.1.3)")
    print(f"SVG written to {out}")


if __name__ == "__main__":
    main()
