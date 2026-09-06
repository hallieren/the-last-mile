# Template 17 · Action Queue Design Patterns, Decision Trail Schema, Before/After Workflow Map

> Companion chapter(s): Chapter 17. The three tools are in design order. Set the column structure first (17.1), then the trail schema (17.2), and last, check the embedding points with the workflow map template (17.3).
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

## 17.1 Action Queue Column Structure Checklist

**Design rule**: The column structure is the projection of the four layers of the decision rights boundary (Template 8.2). Layers AI owns get columns, layers people own get columns, and the red line layer **gets no column**. Go through column by column, and for each answer "which layer, who writes, who consumes." Longer design points move to numbered notes below the table, and the table keeps a phrase.

| Layer | Column | Who Writes | Who Consumes | Design Point |
|----|----|--------|--------|----------|
| Sense | Claim ID / business primary key | System | Everyone | Matches the source system's primary key, can be traced back |
| Sense | Reason stuck / missing item | AI extraction | Handler | Output can be checked (note 1) |
| Sense | Days waiting / aging flag | System | Handler, escalation rules | Counted in business days, not calendar days |
| Sense | Risk signal | Rules + AI | Handler | Signal traceable to its source (note 2) |
| Sense | Status-in-doubt flag | Reconciliation logic | Handler, owner | Lights up on mismatch (note 3) |
| Advise | Suggested priority | Rules + AI | Handler | Chase ≠ risk (note 4) |
| Advise | Suggested next action | Rules + AI | Handler | Starts with a verb, executable (note 5) |
| Advise | Reason | Rules + AI | Handler | The "ability" of the three questions (note 6) |
| Act | Owner | Pick up / assign | Everyone | Real name, never blank (note 7) |
| Act | Human Call | Handler | Trail, downstream actions | The "authority" of the three questions (note 8) |
| Decide | **(no column)** | / | / | The physical form of the red line (note 9) |

**Design point notes**:

1. Output can be checked. Put the LLM where its output can be checked (Chapter 10).
2. Every signal traces to a source rule or model version.
3. Lights up when the source system and the source of truth disagree (the in-row form of Chapter 9's status-in-doubt list).
4. The ranking logic eats the front line's real trade-offs. Chase ≠ risk.
5. Starts with a verb and can be executed directly. Outbound sending actions produce a draft only.
6. The "ability" of the three oversight questions. The information for judging right or wrong is in the same row.
7. Must be a named person, with the basis for assignment written down, one of SOP clause / job responsibility / supervisor assignment. Blank equals failure mode 2 (suggestions left hanging, a suggestion with no responsible person is not a suggestion).
8. The "authority" of the three oversight questions. Without this column the system takes no action.
9. The physical form of the red line. The payout decision has no place on the table.

**Two companion pieces** (Chapter 17, At Anchor & Helm):

- **Rollup view**: a page of numbers summed by team / category / aging, where every number clicks through to the queue itself. It is the entrance to the queue, not a parallel big screen.
- **Exception escalation rules**: set how many rows the recipient is willing to look at per day (the "time" of the three oversight questions), then derive the escalation thresholds backward. Keep signal categories to three or fewer, against alert fatigue.

## 17.2 Decision Trail Schema

**Guiding principle**: **Suggestions and facts are stored separately**. The fact table records only the world and what people did. The suggestion table is append-only, never updated, and not one word of AI output is written back to the source (Chapter 9's trail form, turned into a schema). Fields align item for item with Chapter 12's "six end-to-end decision trail fields."

| Field | Content | Aligns With |
|------|------|------|
| Input snapshot | Fingerprint / snapshot reference of the input data at the moment the suggestion was generated | Based on what |
| Rule / model version | Version number of the rule hit, model and prompt version | Based on what |
| Suggestion content | Priority + next action | What it said |
| Reason | The reason sentence shown to the handler, stored as is | What it said |
| Human Call | accept / override / hold | Who made the call |
| Decider | Real name, inherited from the source system identity | Who made the call |
| Timestamp | Suggestion time + decision time, both | When |
| **Reason code** | Required on override: enumerated value + optional note | Loop entrance |

**Sample reason code values** (Anchor & Helm's version, rewrite in the front line's own language for each project; no more than seven values):

1. Risk judgment differs (the word that keeps showing up in the notes is the name of the next rule)
2. Priority judgment differs
3. Information outdated (data lag, feeds into the fitness retest)
4. Already handled offline (workflow escape signal, the action happened outside the system)
5. Suggested action not feasible
6. Other (note required; "other" above thirty percent = the values need a revision)

**Review cadence** (the operating side of level six, closed loop, taken over by Chapter 18): split the override rate by suggestion category, look once a week; trace back the rule implementation for the category with the highest override rate; add claims with the wrong shape to the golden cases (Chapter 11).

## 17.3 Before/After Workflow Map Template

**Usage**: Before designing the embedding, rule on where every real step (field archaeology output, Template 6) goes. Three destinations, one line of test each:

| Where It Goes | Test | Example (Chapter 17's Fourteen Steps) |
|------|------|---------------------|
| **Absorbed** | Pure information hauling: find, copy, move, watch | Scan new claims, enter into the sheet, the Tuesday and Thursday manual filter of overdue claims |
| **Transformed** | Information hauling + human confirmation: the system does the first half, the person does the second | Pre-generated missing list reviewed by a person, drafted chase sent by a person |
| **Kept** | Judgment and relationships: persuade, coordinate, decide | Calling the surveyor, backing up Excel before leaving |

Template table:

| # | Real Step (Before) | Where It Goes | After Form | Notes (Red Line / Dependency) |
|---|--------------------|------|-----------|---------------------|
| 1 | | Absorbed / Transformed / Kept | | |

**Three checks**:

- [ ] Is everything absorbed pure information hauling? A judgment absorbed = the decision rights boundary is drawn wrong, go back to Chapter 8.
- [ ] Does the "person does the second half" of each transformed step land on a queue column (Human Call / review), not in another system? (Failure mode 3, five tools stitched into one workflow)
- [ ] Are the kept steps written down explicitly? "What the system does not touch" matters as much as "what the system does." It is the boundary promise to the front line.

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/action-queue/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/action-queue/): trail table DDL (fact table / suggestion table split) + sample reason code enumeration config
- [`templates/action-queue/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/action-queue/): sample weekly report query splitting the override rate by category
- [`templates/action-queue/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/action-queue/): sample config for the rollup view and escalation rules (thresholds, recipients, signal categories)
