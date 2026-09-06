#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
"""Reads several five-question scorecard CSVs, rolls them up under the seven hard rules in 7.2, and prints the reporting one-pager (an elimination table in Markdown). Template 7."""
import argparse
import csv
import pathlib

QUESTIONS = ["Pain", "Data", "Decision", "Risk", "ROI"]


def load_card(path):
    with open(path, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    card = {"candidate": rows[0]["candidate"], "proposed_by": rows[0]["proposed_by"],
            "condition": "", "score": {}, "evidence": {}, "capped": set()}
    for r in rows:
        q = r["question"].strip()
        assert q in QUESTIONS, f"{path}: unknown question '{q}'"
        score = int(r["score"])
        assert 1 <= score <= 5, f"{path}: {q} score {score} is not between 1 and 5"
        if not r["evidence"].strip():  # Rule 4 (7.2): a blank evidence cell always scores 2
            if score > 2:
                card["capped"].add(q)
            score = min(score, 2)
        card["score"][q], card["evidence"][q] = score, r["evidence"].strip()
        cond = (r.get("condition_or_reevaluation_condition") or "").strip()
        card["condition"] = card["condition"] or cond
    assert set(card["score"]) == set(QUESTIONS), f"{path}: missing one of the five questions"
    return card


def verdict(card):
    lo = min(card["score"].values())
    at = " / ".join(q for q in QUESTIONS if card["score"][q] == lo)
    # Rule 1 (7.2): any question scoring 2 or below eliminates the candidate outright, no weighting, no averaging. Rule 2: a score of 3 is a conditional pass
    concl = "Eliminated" if lo <= 2 else ("Winner (conditional)" if lo == 3 else "Winner")
    return lo, at, concl


parser = argparse.ArgumentParser(description="Five-question scorecards → reporting one-pager (elimination table in Markdown), Template 7.2/7.3")
parser.add_argument("files", nargs="*", help="Scorecard CSVs, one per candidate (defaults to the sample/ examples)")
parser.add_argument("-o", "--out", help="Output file (defaults to printing to the terminal)")
args = parser.parse_args()

files = args.files or sorted(str(p) for p in (pathlib.Path(__file__).parent / "sample").glob("*.csv"))
cards = [load_card(f) for f in files]

winners = [c for c in cards if verdict(c)[2] != "Eliminated"]
losers = [c for c in cards if verdict(c)[2] == "Eliminated"]

lines = ["# Five-Question Screen One-Pager (Template 7.3 Format)", ""]
if winners:
    lines += [f"**Conclusion**: {', '.join(c['candidate'] for c in winners)} moves into charter negotiation / discovery.",
              "One-sentence reason + one number: ____ (pick the hardest evidence from the winning candidates' evidence columns)", ""]
else:
    lines += ["**Conclusion**: every candidate is eliminated. Go back to discovery and find a new opportunity, not loosen the standard and screen again (Rule 5, 7.2).", ""]

lines += ["## Candidates and Results (Elimination Table)", "",
          "| Candidate | Proposed By | Pain | Data | Decision | Risk | ROI | Lowest Score (Question) | Conclusion | Condition / Re-evaluation Condition |",
          "|------|--------|------|------|----------|------|-----|------------------|------|------------------|"]
for c in cards:
    lo, at, concl = verdict(c)
    scores = " | ".join(f"{c['score'][q]}{'*' if q in c['capped'] else ''}" for q in QUESTIONS)
    tail = ", conditional" if concl == "Winner (conditional)" else ""
    lines.append(f"| {c['candidate']} | {c['proposed_by']} | {scores} | {lo} ({at}{tail}) | {concl} | {c['condition'] or '____'} |")
if any(c["capped"] for c in cards):
    lines.append("\n* Original score voided: evidence cell is blank, scored as 2 (Rule 4, 7.2).")

if losers:
    lines += ["", "## Eliminated Candidates (Three Lines Each)"]
for c in losers:
    lo, at, _ = verdict(c)
    ev = next((c["evidence"][q] for q in QUESTIONS if c["score"][q] == lo and c["evidence"][q]),
              "[evidence cell is blank, an imagined score, scored as 2]")
    lines += ["", f"**{c['candidate']}**",
              f"- Cause of death: the {at} question, scoring {lo}.",
              f"- Evidence: {ev}",
              f"- Re-evaluation condition: {c['condition'] or '____ (required: what evidence would trigger another pass at the five questions)'}"]

lines += ["", "## Next Steps"]
for c in winners:
    lines.append(f"- {c['candidate']}: condition, {c['condition'] or '____'}; time box, data access, and staffing: ____ (input to the charter negotiation, see Chapter 4)")
if not winners:
    lines.append("- Go back to discovery. Archive this table. When the idea resurfaces in three months, check the evidence and the re-evaluation condition, not your memory.")

out = "\n".join(lines) + "\n"
if args.out:
    pathlib.Path(args.out).write_text(out, encoding="utf-8")
    print(f"Wrote {args.out}")
else:
    print(out)
