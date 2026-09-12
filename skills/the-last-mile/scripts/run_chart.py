#!/usr/bin/env python3
# Companion tool from The Last Mile. Modify freely and use at work, no attribution needed.
"""Run chart signal and SVG: baseline median, latest same-side streak, and a short-notice draft when the rule holds.

CSV columns: period,value (period is "Week N" or a date string, value a number).
--baseline N: the first N points form the baseline, their median is the reference line.
--run R: the R in "R points on one side" (default 6, the rule comes from The Health Care Data Guide).
--svg out.svg: also draw the run chart, every point in time order, median line, baseline segment shaded, no trend line.
Exit 0 always.
"""
import argparse
import csv
import pathlib
import statistics
from xml.sax.saxutils import escape


def streak(values, median, baseline):
    """Consecutive same-side points counted back from the latest one, stopping at the baseline.
    Returns (count, side, index of the earliest point in the streak).
    A point sitting on the median neither counts nor breaks the streak (run chart rule)."""
    n, side, start = 0, None, len(values)
    for i in range(len(values) - 1, baseline - 1, -1):
        if values[i] == median:
            continue
        s = "below" if values[i] < median else "above"
        side = side or s
        if s != side:
            break
        n, start = n + 1, i
    return n, side, start


def svg(periods, values, median, baseline, shift_from):
    """shift_from is the index where the signalled streak begins, or None when the rule does not hold."""
    W, H, L, R, T, B = 760, 420, 64, 28, 56, 64
    pw, ph = W - L - R, H - T - B
    lo, hi = min(values + [median]), max(values + [median])
    pad = (hi - lo) * 0.15 or 1
    lo, hi = lo - pad, hi + pad
    step = pw / len(values)
    xs = [L + step * (i + 0.5) for i in range(len(values))]
    ys = [T + ph * (hi - v) / (hi - lo) for v in values]
    y_med = T + ph * (hi - median) / (hi - lo)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" font-family="sans-serif">',
           f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
           f'<text x="{L}" y="26" font-size="15" fill="#1a1a1a">Run chart, {len(values)} points</text>',
           f'<text x="{L}" y="44" font-size="11" fill="#707070">Baseline = first {baseline} points, median {median:g}. '
           'No trend line: a shift is a run of points on one side, not a slope.</text>']
    for k in range(5):
        gy = T + ph * k / 4
        out.append(f'<line x1="{L}" y1="{gy:.1f}" x2="{W - R}" y2="{gy:.1f}" stroke="#ececec"/>')
        out.append(f'<text x="{L - 8}" y="{gy + 4:.1f}" font-size="11" fill="#707070" text-anchor="end">'
                   f'{hi - (hi - lo) * k / 4:.1f}</text>')
    out.append(f'<rect x="{L}" y="{T}" width="{step * baseline:.1f}" height="{ph}" fill="#8a8a8a" opacity="0.08"/>')
    out.append(f'<text x="{L + 4}" y="{T + 14}" font-size="11" fill="#555555">baseline</text>')
    if shift_from is not None:
        x0 = xs[shift_from] - 12
        out.append(f'<rect x="{x0:.1f}" y="{T}" width="{xs[-1] + 12 - x0:.1f}" height="{ph}" fill="#c4461d" opacity="0.07"/>')
        out.append(f'<text x="{x0:.1f}" y="{T + 14}" font-size="11" fill="#c4461d">shift: points on one side of the median</text>')
    out.append(f'<line x1="{L}" y1="{y_med:.1f}" x2="{W - R}" y2="{y_med:.1f}" stroke="#8a8a8a" '
               'stroke-width="1.5" stroke-dasharray="6 4"/>')
    out.append(f'<text x="{W - R}" y="{y_med - 6:.1f}" font-size="11" fill="#555555" text-anchor="end">'
               f'baseline median {median:g}</text>')
    out.append('<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in zip(xs, ys))
               + '" fill="none" stroke="#4269d0" stroke-width="2"/>')
    for i, (x, y) in enumerate(zip(xs, ys)):
        color = "#c4461d" if shift_from is not None and i >= shift_from and values[i] != median else "#4269d0"
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#ffffff" stroke="{color}" stroke-width="2"/>')
        out.append(f'<text x="{x:.1f}" y="{H - B + 20}" font-size="11" fill="#707070" text-anchor="middle">'
                   f'{escape(periods[i])}</text>')
    out.append("</svg>")
    return "\n".join(out)


def selftest():
    vals = [10, 12, 9, 11, 10, 13, 8, 12, 7, 6, 5, 4, 3, 2]
    med = statistics.median(vals[:8])
    assert med == 10.5
    assert streak(vals, med, 8) == (6, "below", 8)
    assert streak(vals[:9] + [10.5, 6], med, 8) == (2, "below", 8), "an on-median point neither counts nor breaks"
    assert streak(vals[:10] + [15], med, 8) == (1, "above", 10)
    assert streak(vals[:8], med, 8) == (0, None, 8)
    doc = svg([f"p{i}" for i in range(len(vals))], vals, med, 8, 8)
    assert doc.count("<circle") == len(vals) and "stroke-dasharray" in doc and "shift:" in doc
    assert "shift:" not in svg(["a", "b"], [1.0, 2.0], 1.5, 1, None)
    print("selftest ok")


def main():
    p = argparse.ArgumentParser(description="Run chart signal: baseline median, same-side streak, short-notice draft "
                                "when the rule holds, optional SVG (exit 0 always)")
    p.add_argument("csv_path", nargs="?", help="CSV with columns period,value")
    p.add_argument("--baseline", type=int, default=8, help="baseline is the first N points (default 8)")
    p.add_argument("--run", type=int, default=6, help='R in "R points on one side" (default 6)')
    p.add_argument("--svg", help="write the run chart to this SVG path")
    p.add_argument("--selftest", action="store_true", help="run inline checks and exit")
    a = p.parse_args()
    if a.selftest:
        return selftest()
    if not a.csv_path:
        p.error("CSV path is required")

    with open(a.csv_path, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    assert rows and {"period", "value"} <= set(rows[0]), "CSV needs columns period,value"
    assert len(rows) > a.baseline, "need more points than the baseline"
    periods = [r["period"] for r in rows]
    values = [float(r["value"]) for r in rows]
    median = statistics.median(values[:a.baseline])
    n, side, start = streak(values, median, a.baseline)
    holds = n >= a.run

    print(f"Baseline: first {a.baseline} points ({periods[0]} to {periods[a.baseline - 1]}), median {median:g}")
    if holds:
        print(f"[Short notice draft] Point {len(values)} ({periods[-1]}): the latest {n} consecutive points sit "
              f'{side} the baseline median {median:g}, "{a.run} points on one side" holds. This is a shift, '
              "not fluctuation. Send discipline: one line plus one chart, no request attached.")
    else:
        print(f"Latest same-side streak: {n} points (threshold {a.run}), no special cause yet; "
              "keep watching, do not draw a trend between two points.")
    if a.svg:
        pathlib.Path(a.svg).write_text(svg(periods, values, median, a.baseline, start if holds else None), encoding="utf-8")
        print(f"SVG written to {a.svg}")


if __name__ == "__main__":
    main()
