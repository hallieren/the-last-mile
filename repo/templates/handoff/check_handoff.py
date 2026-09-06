#!/usr/bin/env python3
# Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
"""Handoff checklist validation (Template 22). The checklist is flat key: value; the standard library has no YAML parser, so this hand-writes the parse."""
import argparse
import pathlib
import sys


def load(path):
    data = {}
    for raw in open(path, encoding="utf-8-sig"):
        line = raw.split(" #", 1)[0].strip()  # strip an inline comment
        if not line or line.startswith("#"):
            continue
        key, _, val = line.partition(":")
        data[key.strip()] = val.strip().strip('"').strip("'")
    return data


NAMES = {"system_owner": "the system owner", "maintenance_owner": "the maintenance owner",
         "eval_guardian": "the eval guardian", "ai_dependency_owner": "the AI dependency owner",
         "ai_eval_update": "AI: ongoing eval upkeep",
         "ai_model_revalidation": "AI: model/dependency change revalidation", "ai_trace_review": "AI: decision trail review"}
CAPS = {"run": "run", "config": "configure", "exception": "exceptions", "evolve": "evolve", "teach": "teach"}

p = argparse.ArgumentParser(
    description="Validate the handoff checklist: an empty name is an alarm; a failed capability must have a rework action and a retest date attached (Template 22)")
p.add_argument("yaml_path", nargs="?",
               default=str(pathlib.Path(__file__).parent / "sample" / "checklist.yaml"),
               help="Flat checklist.yaml; defaults to sample/checklist.yaml (which includes the alarm demo)")
a = p.parse_args()
d = load(a.yaml_path)

alarms = []
for k, label in NAMES.items():
    if not d.get(k):
        alarms.append(f'empty-name alarm: {label} ({k}) has no name filled in, "the team owns it" equals no one owns it')
for c, label in CAPS.items():
    st = d.get(f"cap_{c}_status", "")
    if st not in ("pending", "failed", "passed"):
        alarms.append(f"invalid status: the {label} capability = {st!r} (only pending/failed/passed allowed)")
    if st == "failed" and not (d.get(f"cap_{c}_rework") and d.get(f"cap_{c}_retest")):
        alarms.append(f"missing rework: the {label} capability failed, cap_{c}_rework and "
                      f"cap_{c}_retest must both be filled in, what it needs is a drill, not a document")

passed = sum(d.get(f"cap_{c}_status") == "passed" for c in CAPS)
print(f"Checklist: {a.yaml_path}")
print(f"Five capabilities: {passed}/5 passed; response window closes {d.get('window_end') or '(not filled in)'}")
if alarms:
    print(*alarms, sep="\n")
    sys.exit(1)
print("PASS: all four owners and the three AI items are named, and every failed item has a rework action and a retest date attached.")
