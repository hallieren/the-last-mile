# Queue columns and decision trail

Source: `docs/appendices/template-17-action-queue.md` §17.1–17.3 (and `repo/templates/action-queue/schema.sql`, `repo/templates/action-queue/reason-codes.json`; the repo wins on conflict).

| Header field | Fill in |
|---|---|
| System / workflow claim | `This system will change <role and name>'s <next action>` REQUIRED |
| Layer where AI stops | advise (sense and advise get AI columns; act gets people columns; decide gets no column) REQUIRED |
| Daily volume cap | <rows entering human view per day>, derived backward from <review minutes per day ÷ minutes per row> REQUIRED |
| Weekly override review | <owner name>, hung on <existing business-side meeting>, <weekday> REQUIRED |
| Version / date | <date>; reason code values version <n> |

## Column structure (§17.1)

| Layer | Column | Who writes | Who consumes | Design point |
|---|---|---|---|---|
| Sense | <business primary key> | System | Everyone | Matches the source system's key, traceable back |
| Sense | Reason stuck / missing item | AI extraction | Handler | Output can be checked |
| Sense | Days waiting / aging flag | System | Handler, escalation rules | Counted in business days, not calendar days |
| Sense | Risk signal | Rules + AI | Handler | Traces to a source rule or model version |
| Sense | Status-in-doubt flag | Reconciliation logic | Handler, owner | Lights up when the source system and the source of truth disagree |
| Advise | Suggested priority | Rules + AI | Handler | Ranking eats the front line's real trade-offs; chase ≠ risk |
| Advise | Suggested next action | Rules + AI | Handler | Starts with a verb, executable; outbound sending actions produce a draft only |
| Advise | Reason | Rules + AI | Handler | The "ability" of the three oversight questions, in the same row |
| Act | Owner | Pick up / assign | Everyone | <owner name>, never blank; basis written as one of SOP clause / job responsibility / supervisor assignment |
| Act | Human Call | Handler | Trail, downstream actions | The "authority"; without this column the system takes no action |
| Decide | (no column) | / | / | The physical form of the red line; <the decision the system never touches> has no place on the table |

Companion pieces: a rollup view (numbers by team / category / aging, every number clicks through to the queue; an entrance, never a parallel big screen); exception escalation rules (set how many rows the recipient will look at per day first, derive thresholds backward, ≤ 3 signal categories (rule)).

## Trail schema (§17.2, `schema.sql`)

Two tables. `suggestions` is written only by the AI; `decisions` only by people. Both are INSERT only, never UPDATE or DELETE; a revised call appends a new decision row. The AI never writes one character back to the source system.

| Table | Field | Content | Aligns with |
|---|---|---|---|
| suggestions | input_snapshot | Fingerprint or snapshot reference of the input at suggestion time | Based on what |
| suggestions | rule_model_version | Rule version hit, model and prompt version | Based on what |
| suggestions | suggestion | Priority + next action | What it said |
| suggestions | reason | The reason sentence shown to the handler, stored as is | What it said |
| suggestions | category | Suggestion category; the override rate is split by this column | Review cadence |
| suggestions | created_at | Suggestion time | When |
| decisions | decision | accept / override (Human Call) | Who made the call |
| decisions | decided_by | Real name, inherited from the source system identity | Who made the call |
| decisions | decided_at | Decision time, kept apart from suggestion time | When |
| decisions | reason_code + reason_note | Required on override, enforced at the database layer; note required when the code is other | Loop entrance |

Reason code rules: ≤ 7 values plus other (rule), rewritten in the front line's own language; sample set risk judgment differs (the word repeating in the notes is the name of the next rule) / priority judgment differs / information outdated (feeds the fitness retest) / already handled offline (a workflow escape signal) / suggested action not feasible / other; other above 30% (rule) = revise the values. Review cadence: split the override rate by category once a week (rule), trace back the rule implementation for the highest category, add rows with the wrong shape to the golden cases.

## Before/after workflow map (§17.3)

| # | Real step (before) | Where it goes | After form | Notes (red line / dependency) |
|---|---|---|---|---|
| 1 | <step from field archaeology> | Absorbed / Transformed / Kept | <queue column or "the system does not touch"> | <red line, platform dependency> |

Absorbed = pure information hauling (find, copy, move, watch). Transformed = hauling + human confirmation, the system does the first half. Kept = judgment and relationships (persuade, coordinate, decide).

**Rules**
- Layers AI owns get columns, layers people own get columns, and the red line layer gets no column.
- Must be a named person, with the basis for assignment written down, one of SOP clause / job responsibility / supervisor assignment. Blank equals failure mode 2 (suggestions left hanging, a suggestion with no responsible person is not a suggestion).
- Suggestions and facts are stored separately. The fact table records only the world and what people did. The suggestion table is append-only, never updated, and not one word of AI output is written back to the source.
- Is everything absorbed pure information hauling? A judgment absorbed = the decision rights boundary is drawn wrong.
- Does the "person does the second half" of each transformed step land on a queue column (Human Call / review), not in another system?
- Are the kept steps written down explicitly? "What the system does not touch" matters as much as "what the system does." It is the boundary promise to the front line.

Filled in → goes to: the decision memo (the decision rights boundary pasted into the trade-off section) and the weekly override review; wrong-shape rows flow into the golden cases of the eval spec.
