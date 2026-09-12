#!/usr/bin/env python3
# Companion tool from The Last Mile. Modify freely and use at work, no attribution needed.
"""Screen one candidate: red lines first (any one vetoes), then a five-question scorecard on weakest-link logic.

Scorecard CSV columns: question,score,evidence,condition,deadline.
  question is Pain/Data/Decision/Risk/ROI, or the intake rubric's
  Strategic value/Data readiness/Owner in place/Production path/Reuse potential (case-insensitive).
  score is an integer 1 to 5; condition and deadline are required when score is 3.
Red-lines CSV (optional, --red-lines) columns: red_line,touched,test_question with touched yes/no.
Exit 0 take it, 2 take it with conditions, 1 eliminated or vetoed.
"""
import argparse
import csv
import sys

RUBRICS = ({"pain", "data", "decision", "risk", "roi"},
           {"strategic value", "data readiness", "owner in place", "production path", "reuse potential"})
REFERRAL = ("write the referral route and the re-evaluation condition as an event, "
            "and name who rechecks it at which standing meeting")


def veto(red_lines):
    """Lines for the touched red lines; empty when none is touched."""
    touched = [r for r in red_lines if r["touched"].strip().lower() == "yes"]
    lines = [f"Red line touched: {r['red_line'].strip()}. Test question: {r['test_question'].strip()}" for r in touched]
    if lines:
        lines += ["Verdict: do not take it",
                  "the veto comes before the scoring; scoring anyway only shows which dimensions "
                  "an alternative path must rebuild"]
    return lines


def score(rows):
    """Return (lines, exit code) for one scorecard."""
    names = {r["question"].strip().lower() for r in rows}
    assert len(rows) == 5 and names in RUBRICS, f"the sheet must hold exactly one five-question rubric, got {sorted(names)}"
    lines, scores, conditions = [], {}, []
    for r in rows:
        q, s = r["question"].strip(), int(r["score"])
        assert 1 <= s <= 5, f"{q}: score {s} is not between 1 and 5"
        if not r["evidence"].strip():
            lines.append(f"{q}: blank evidence is treated as 2")
            s = min(s, 2)
        if s == 3:
            if r["condition"].strip() and r["deadline"].strip():
                conditions.append(f"{q}: {r['condition'].strip()}, by {r['deadline'].strip()}")
            else:
                lines.append(f"error: {q} scores 3 without a condition and a deadline, treated as 2")
                s = 2
        scores[q] = s
    lo = min(scores.values())
    weakest = " / ".join(q for q in scores if scores[q] == lo)
    lines.append(f"Lowest score: {weakest} {lo}")
    if lo <= 2:
        lines += [f"Verdict: eliminated on {weakest}", "no weighted total exists on this sheet", REFERRAL]
        return lines, 1
    if lo == 3:
        return lines + ["Verdict: take it with conditions"] + [f"  - {c}" for c in conditions], 2
    return lines + ["Verdict: take it"], 0


def selftest():
    def card(scores, evidence="x", condition="c", deadline="d"):
        return [{"question": q, "score": str(s), "evidence": evidence, "condition": condition, "deadline": deadline}
                for q, s in zip(["Pain", "Data", "Decision", "Risk", "ROI"], scores)]
    assert score(card([5, 4, 4, 4, 4]))[1] == 0
    lines, code = score(card([5, 3, 4, 4, 4]))
    assert code == 2 and "  - Data: c, by d" in lines
    lines, code = score(card([5, 3, 4, 4, 4], deadline=""))
    assert code == 1 and "Verdict: eliminated on Data" in lines, "a 3 without a deadline drops to 2"
    lines, code = score(card([5, 5, 5, 5, 5], evidence=""))
    assert code == 1 and "Lowest score: Pain / Data / Decision / Risk / ROI 2" in lines
    assert score(card([5, 4, 4, 1, 4]))[1] == 1
    red = [{"red_line": "irreversible harm", "touched": "no", "test_question": "q1"},
           {"red_line": "grey zone", "touched": "Yes", "test_question": "q2"}]
    assert veto(red)[0] == "Red line touched: grey zone. Test question: q2" and veto(red[:1]) == []
    print("selftest ok")


def main():
    p = argparse.ArgumentParser(description="Screen one candidate: red-line veto first, then the five-question "
                                "scorecard on weakest-link logic (exit 0 take, 2 conditional, 1 eliminated or vetoed)")
    p.add_argument("scorecard", nargs="?", help="scorecard CSV (question,score,evidence,condition,deadline)")
    p.add_argument("--red-lines", help="red-lines CSV (red_line,touched,test_question)")
    p.add_argument("--selftest", action="store_true", help="run inline checks and exit")
    a = p.parse_args()
    if a.selftest:
        return selftest()
    if not a.scorecard:
        p.error("scorecard CSV path is required")

    if a.red_lines:
        with open(a.red_lines, newline="", encoding="utf-8-sig") as fh:
            red = list(csv.DictReader(fh))
        assert red and {"red_line", "touched", "test_question"} <= set(red[0]), \
            "red-lines CSV needs columns red_line,touched,test_question"
        lines = veto(red)
        if lines:
            print("\n".join(lines))
            sys.exit(1)
        print(f"Red lines: none of {len(red)} touched, on to the scoring")
    with open(a.scorecard, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    assert rows and {"question", "score", "evidence", "condition", "deadline"} <= set(rows[0]), \
        "scorecard CSV needs columns question,score,evidence,condition,deadline"
    lines, code = score(rows)
    print("\n".join(lines))
    sys.exit(code)


if __name__ == "__main__":
    main()
