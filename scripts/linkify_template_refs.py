#!/usr/bin/env python3
"""Turn "<template word> N" / "N.M" prose citations into links to the template appendix.

The template word (模板 / Template) comes from book.json. Authoring tool, not run in CI:
run it only once every template appendix exists, or it links to missing files."""
import json
import re
from pathlib import Path

BOOK = json.loads(Path("book.json").read_text(encoding="utf-8"))

TPL = {0: "template-00-field-mvp-pack", 2: "template-02-role-charter", 3: "template-03-capability",
       4: "template-04-deployment-charter", 5: "template-05-stakeholder-map", 6: "template-06-field-archaeology",
       7: "template-07-five-questions", 8: "template-08-thin-slice", 9: "template-09-data-fitness",
       10: "template-10-pattern-decision", 11: "template-11-eval-spec", 12: "template-12-trust-matrix",
       14: "template-14-stage-gates", 15: "template-15-cobuild", 16: "template-16-production-readiness",
       17: "template-17-action-queue", 18: "template-18-metric-tree", 19: "template-19-memo-suite",
       20: "template-20-resistance-decoder", 21: "template-21-adoption-plan", 22: "template-22-handoff",
       23: "template-23-pattern-extraction", 24: "template-24-f2p-memo", 25: "template-25-intake-redlines"}

PAT = re.compile(r"(?<!\[)" + re.escape(BOOK["template_word"]) + r" (\d+)(\.\d+)?")
skipped = set()
linked = 0


def repl(m):
    global linked
    n = int(m.group(1))
    if n not in TPL:
        skipped.add(m.group(0))
        return m.group(0)
    linked += 1
    return f"[{m.group(0)}](../appendices/{TPL[n]}.md)"


for f in sorted(Path("docs/chapters").glob("ch*.md")):
    out, fenced = [], False
    for line in f.read_text(encoding="utf-8").splitlines(keepends=True):
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
        out.append(line if fenced else PAT.sub(repl, line))
    f.write_text("".join(out), encoding="utf-8")

print("linked:", linked)
print("skipped (no template file):", sorted(skipped) or "none")
