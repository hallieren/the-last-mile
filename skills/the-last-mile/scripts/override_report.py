#!/usr/bin/env python3
# Companion tool from The Last Mile. Modify freely and use at work, no attribution needed.
"""Weekly override report over two decision-trail exports: override rate by category, reason codes, other share, daily actives.

suggestions.csv columns: suggestion_id,claim_id,input_snapshot,rule_model_version,suggestion,reason,category,created_at
decisions.csv columns: decision_id,suggestion_id,decision,reason_code,reason_note,decided_by,decided_at
  (decision is accept/override; a reason_code is required on every override).
The window is the last --days days counted back from the latest decided_at in the file, so an old export still reports.
Exit 0 always.
"""
import argparse
import csv
from collections import Counter
from datetime import datetime, timedelta


def report(suggestions, decisions, days):
    """Return the report lines; both inputs are lists of dicts with the CSV columns."""
    category = {s["suggestion_id"]: s["category"] for s in suggestions}
    unknown = {d["suggestion_id"] for d in decisions} - set(category)
    assert not unknown, f"decisions point at unknown suggestion_id: {sorted(unknown)}"
    bad = {d["decision"] for d in decisions} - {"accept", "override"}
    assert not bad, f"decision must be accept/override, got {sorted(bad)}"
    at = {d["decision_id"]: datetime.fromisoformat(d["decided_at"].strip()) for d in decisions}
    latest = max(at.values())
    start = latest - timedelta(days=days)
    window = [d for d in decisions if at[d["decision_id"]] >= start]
    overrides = [d for d in window if d["decision"] == "override"]

    lines = [f"Window: last {days} days ending {latest:%Y-%m-%d} (from {start:%Y-%m-%d}), "
             f"{len(window)} of {len(decisions)} decisions",
             f"Overall override rate: {len(overrides)}/{len(window)} = {len(overrides) / len(window):.0%}", "",
             "| Category | Decisions | Overrides | Override rate |", "|---|---|---|---|"]
    per_cat = Counter(category[d["suggestion_id"]] for d in window)
    per_cat_ov = Counter(category[d["suggestion_id"]] for d in overrides)
    for c in sorted(per_cat, key=lambda c: per_cat_ov[c] / per_cat[c], reverse=True):
        lines.append(f"| {c} | {per_cat[c]} | {per_cat_ov[c]} | {per_cat_ov[c] / per_cat[c]:.0%} |")
    lines += ["trace the rule implementation for the highest category first", ""]

    codes = Counter(d["reason_code"].strip() or "(missing)" for d in overrides)
    lines.append("Reason codes among overrides:")
    lines += [f"  {code}: {n}" for code, n in codes.most_common()]
    if codes["(missing)"]:
        lines.append(f"ALARM: {codes['(missing)']} override(s) without a reason_code; every override needs one")
    if overrides:
        other = codes["other"] / len(overrides)
        lines.append(f"Share of other: {codes['other']}/{len(overrides)} = {other:.0%}")
        if other > 0.3:
            lines.append("ALARM: reason codes need a revision, above 30% other")

    lines += ["", "Daily actives (distinct decided_by per day):"]
    actives = {}
    for d in window:
        actives.setdefault(at[d["decision_id"]].date(), set()).add(d["decided_by"].strip())
    lines += [f"  {day}: {len(actives[day])}" for day in sorted(actives)]
    return lines


def selftest():
    sug = [{"suggestion_id": f"s{i}", "category": c} for i, c in enumerate("aabbb")]
    dec = [{"decision_id": f"d{i}", "suggestion_id": f"s{i}", "decision": v, "reason_code": rc,
            "decided_by": who, "decided_at": t}
           for i, (v, rc, who, t) in enumerate([("accept", "", "x", "2026-01-01T09:00:00"),
                                                 ("override", "other", "y", "2026-01-02T09:00:00"),
                                                 ("override", "", "x", "2026-01-02T10:00:00"),
                                                 ("accept", "", "y", "2026-01-03T09:00:00"),
                                                 ("override", "other", "x", "2026-01-10T09:00:00")])]
    lines = report(sug, dec, 3650)
    assert "Overall override rate: 3/5 = 60%" in lines
    assert lines.index("| b | 3 | 2 | 67% |") < lines.index("| a | 2 | 1 | 50% |"), "sorted by rate descending"
    assert "ALARM: reason codes need a revision, above 30% other" in lines
    assert any(ln.startswith("ALARM: 1 override(s) without a reason_code") for ln in lines)
    assert "  2026-01-02: 2" in lines and "  2026-01-10: 1" in lines
    lines = report(sug, dec, 7)
    assert "Overall override rate: 1/2 = 50%" in lines, "the window counts back from the latest decided_at"
    print("selftest ok")


def main():
    p = argparse.ArgumentParser(description="Override report over suggestions.csv and decisions.csv exports: "
                                "rate by category, reason codes, other share, daily actives (exit 0)")
    p.add_argument("suggestions", nargs="?", help="suggestions CSV export")
    p.add_argument("decisions", nargs="?", help="decisions CSV export")
    p.add_argument("--days", type=int, default=7, help="window length in days, counted back from the latest decided_at (default 7)")
    p.add_argument("--selftest", action="store_true", help="run inline checks and exit")
    a = p.parse_args()
    if a.selftest:
        return selftest()
    if not (a.suggestions and a.decisions):
        p.error("both suggestions.csv and decisions.csv are required")

    with open(a.suggestions, newline="", encoding="utf-8-sig") as fh:
        suggestions = list(csv.DictReader(fh))
    with open(a.decisions, newline="", encoding="utf-8-sig") as fh:
        decisions = list(csv.DictReader(fh))
    assert suggestions and {"suggestion_id", "category"} <= set(suggestions[0]), \
        "suggestions CSV needs at least suggestion_id and category"
    assert decisions and {"decision_id", "suggestion_id", "decision", "reason_code", "decided_by", "decided_at"} \
        <= set(decisions[0]), "decisions CSV needs decision_id,suggestion_id,decision,reason_code,decided_by,decided_at"
    print("\n".join(report(suggestions, decisions, a.days)))


if __name__ == "__main__":
    main()
