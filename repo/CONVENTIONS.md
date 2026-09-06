# Repo Conventions (Binding on Every Template Directory)

> This file is the contract for the code pass. Each `templates/<name>/` directory is built by its own batch, and this file governs every cross-directory interface. Where it conflicts with an appendix page, the appendix wins. Report the conflict, never edit the appendix on your own.

## 1. General Rules

- **Language and dependencies**: every script is Python 3.9+, **standard library only, zero third-party dependencies** (the book practices the dependency discipline it preaches). Charts (radar, run chart) write SVG files directly, no matplotlib.
- **Document language**: English, with the book's technical terms unchanged (charter, eval, override, and the rest), consistent with the book.
- **Script shape**: every script is a self-contained runnable CLI. `python3 script.py --help` works; with no arguments it runs on the sample data in the sibling `sample/` directory and prints the result. argparse always carries a `description` (one sentence plus the matching template number).
- **Every directory has a `README.md`**: the first three lines are the matching template, a one-sentence purpose, and a file table (File | What it is | How to use).
- **License header**: one comment or lead line at the top of every template and script file: `Companion template from The Last Mile. Modify freely and use at work, no attribution needed.`
- **Sample data**: always the Anchor & Helm case (labeled "Sample data comes from the book's Anchor & Helm case.") or a placeholder (`[name]`, `____`). Never invent a third case.
- **Prompt files**: `prompt-*.md`, with three fixed sections: `## Your Role`, `## Input`, `## Output Requirements`. Prompts name no specific model or vendor (the book does not bind itself to any model or vendor).

## 1.5 Code Style (Mandatory)

- **Spare and plain**: write the smallest code that solves the problem in front of you, never code written "in case we need it later". Target one script at 120 lines or fewer (blank lines included; SVG generators may go to 180). Over the line, ask what to cut, not how to split the file.
- **No preventive abstraction**: a function called once gets inlined; no parameter without a second caller; hardcode until there is a real reason to configure.
- **Handle only the errors that can happen**: a missing CLI input file just raises Python's own FileNotFoundError, no try/except wrapper; a malformed data file gets a one-line assert with a message. No logging framework, no retries.
- **No class worship**: if functions plus dicts solve it, do not write a class.
- **Comments**: write only the constraint the code itself cannot state (such as "the six-points-on-one-side rule comes from the Health Care Data Guide"), never "what the next line does".

## 2. Shared Data Formats (Cross-Directory Interfaces, Do Not Reinvent)

### 2.1 Decision Trail Tables (defined by action-queue, reused by adoption / f2p-memo queries)

SQLite dialect. Two tables kept apart (suggestion / decision), append-only:

```sql
-- suggestions (suggestion table, written by the AI)
suggestion_id TEXT PRIMARY KEY, claim_id TEXT NOT NULL, input_snapshot TEXT NOT NULL,
rule_model_version TEXT NOT NULL, suggestion TEXT NOT NULL, reason TEXT NOT NULL,
category TEXT NOT NULL, created_at TEXT NOT NULL
-- decisions (human decision table, written by people)
decision_id TEXT PRIMARY KEY, suggestion_id TEXT NOT NULL REFERENCES suggestions,
decision TEXT NOT NULL CHECK(decision IN ('accept','override')),
reason_code TEXT, reason_note TEXT, decided_by TEXT NOT NULL, decided_at TEXT NOT NULL
```

The reason code enum holds 7 values or fewer plus `other`; when `decision='override'`, `reason_code` is required (Template 17).

### 2.2 Run Chart Data (defined by metric-tree, reused by memo-suite)

CSV with a header row: `period,value` (period = "Week N" or a date string; value = a number). The baseline median and special cause ("six points on one side") are computed by the script, and `--baseline N` sets the baseline to the first N points.

### 2.3 Five-Axis Radar Data (defined by self-assessment, reused by f-levels)

CSV with a header row: `dimension,score`, five rows, dimension names word for word from Template 3, score from 1 to 5 (one decimal allowed).

### 2.4 Eval Replay Report (defined by eval-spec, reused by stage-gates)

CSV with a header row: `case_id,category,verdict`; verdict is one of pass/concern/unsafe/useless; threshold table JSON: `{"unsafe": 0, "concern": 0.10, "useless": 0.20}` (each number is a ceiling on the share; unsafe stays 0).

### 2.5 Asset Register (defined by pattern-library, aligned with f2p-memo / asset-recovery)

CSV with a header row: `category,name,description,origin,verified_count,owner,updated,status`; status is one of active/pending-reverify/retired; category is one of template/component/judgment-rule/metric-model.

## 3. Directory List (26, sourced from the Code hooks note on each template)

templates/field-mvp, premortem, role-charter, self-assessment, f-levels, deployment-charter, stakeholder-map, field-archaeology, five-questions, thin-slice, data-fitness, pattern-selection (with the three subdirectories decision-table/ schema-check/ spot-check/), eval-spec, trust-constraints, stage-gates, cobuild, production-readiness, action-queue, metric-tree, memo-suite, adoption, handoff, pattern-library, f2p-memo, asset-recovery, intake

(Template 20 has no code companion.)
