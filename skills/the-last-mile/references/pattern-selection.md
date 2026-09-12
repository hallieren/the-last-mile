# Picking the pattern for a step where AI intervenes

**Load this reference when:** the room is debating agent vs RAG vs fine-tune, "it already runs" is the argument for taking a demo into production, the proposer outranks you, or a generated number, date or fact is flowing straight into a calculation, a filing or an outbound message.

Source: chapter 10 (`docs/chapters/ch10-pattern-selection.md`); template 10 (`docs/appendices/template-10-pattern-decision.md`).

## Contents

Decisions (the criterion, the spectrum, the table, three rules of use, three preconditions, the maintainability cell, stopping rules) · Procedures (fill the table; a smarter pattern is proposed; the proposer outranks you; two internal levers; the anti-pattern vote) · Detectors · Key judgments · Templates · Vendor seat

## Decisions

**Rule on the shape of the error, never on the capability ceiling.** A demo shows the ceiling. Production needs an error that can be caught, attributed and rolled back. Test the shape on the spot, can the ways it fails be listed in full in advance, and once it has failed can you locate which step failed and who backstops it. The higher a pattern's ceiling, the harder its error shape is to draw, so the hottest pattern is the one with the narrowest applicability.

**Read the spectrum in this order, dumbest to smartest by how clear the error shape is.**

| # | Pattern | Error shape | The most typical misuse |
|---|---|---|---|
| 1 | Rules | Ways it fails listed in full in advance; when it fails you know which rule matched wrongly | Hardcoding a tacit judgment that will drift |
| 2 | Structured extraction + rules | Error fenced into the extraction step; a bad format caught by schema validation on the spot | No schema validation, the extraction output goes into the store as fact |
| 3 | RAG | Open-ended; a missed retrieval and a wrong retrieval both leave no visible trace; the only check is verifying citations one by one | Nobody maintains the corpus, or it answers exact-field questions |
| 4 | Single-step LLM | Every call can be wrong; the shape depends on how tightly the output format is pinned | Output with no format limit and no reason, leaving the reviewer nothing to review |
| 5 | Agentic workflow | Errors compound and amplify across steps (95% on one step leaves 77% over five, illustrative); the failing step is hard to locate and may not reproduce | Put into a step where errors go outside and nobody backstops them |
| 6 | Fine-tuning | Errors set into the weights, invisible, no way to strike out one on its own | Used on a problem a prompt could solve |

**Rule with the decision table, six patterns × five criteria, a judgment in every cell and no scores.** Scores get averaged. A judgment can only be rebutted. Read top down; all five cells in a row must pass.

| Pattern | Error tolerance | Verifiability | Data requirements | Latency and cost | Maintainability by the receiving side |
|---|---|---|---|---|---|
| Rules | Ways it fails are enumerable, the default for zero-tolerance steps | Reproducible, explainable rule by rule, exhaustively testable | "Fields only need to be interpretable" | "Milliseconds, near zero" | "The business line's IT can change it themselves" |
| Structured extraction + rules | Error fenced into the extraction step; schema validation intercepts format errors, spot checks watch semantic ones; usable near zero tolerance only if the validation layer really exists | Extraction output validated against the schema and spot-checked by sample | Unstructured source accessible, plus a spot-check sample set; extraction output is derived data, trustworthy only once validated | One call per case, batchable, cacheable | "Rules go to the business side; schema and prompts need a handoff." For as long as the spot-check owner is you, this row is your own permanent liability |
| RAG | Open-ended (missed retrieval, wrong retrieval), needs a human backstop; only for steps where a person checks the citations | Verified by checking citations; "should have been retrieved and was not" is hard to verify; "a rotten corpus rots everything" | One genuinely trustworthy corpus with a named maintenance owner | Two hops, retrieval plus generation; maintaining the corpus is a long-term hidden cost | "What gets maintained is really the corpus, and decay is hidden" |
| Single-step LLM | Wrong on any call; only for steps where a person reviews row by row | Cannot be verified exhaustively; pinning the output format and requiring a reason brings it down to "a person checks the reason" | "No training data needed, but no eval means no threshold," which means no acceptance | One hop, controllable and budgetable | "Prompt drift goes unnoticed"; prompts go into version control |
| Agentic workflow | Errors compound and amplify across steps; if any step sends an action outside, the whole chain is reviewed as zero tolerance | "Path varies, failures are hard to locate and hard to reproduce"; the same input may take a different path | Every step passes fitness and eval on its own; cost multiplies by the number of steps | Multiplied by hops, the number of steps settled at run time, latency and spend unpredictable | Hardest to hand off; "debugging often needs the builder himself," and inside a company that builder is your own team |
| Fine-tuning | Errors set into the weights; a new way of failing means retraining, it cannot be patched | Behavior changes globally, every retrain needs a full regression eval | "Hundreds to thousands of annotations (as of writing, the bar is still falling)" (illustrative), and they drift out of date | Training cost paid up front and paid again with every update | "The receiving side can hardly take it over at all." A retraining pipeline, an annotation team, a regression eval, none optional |

**Keep the three rules of use.**

1. Pick per step, not per project. "Does this project use agents" is a fake question. Tolerance differs from step to step and the pattern follows the step. An intervention point is one decision or one conversion, not one feature module.
2. Read top down and stop at the first pattern that passes all five criteria. A cell passes when its judgment still holds once dropped into your step, and the risk left over has a backstop you can name or a checkpoint. Name neither and the cell does not pass. If rules can solve it, no LLM. If a single step is enough, no agent.
3. An upgrade has exactly one legitimate channel, eval data showing that the dumber pattern cannot clear the threshold. "It does not feel smart enough" is not a reason to upgrade, and "I want to learn this framework" is even less of one. The table holds in reverse, if the evidence says upgrade, "never use agents" is just as much a dogma.

**Write three preconditions per step before you look at the table.**

| Precondition | Write down | Ruling it forces |
|---|---|---|
| Error tolerance | How many times may it be wrong, who sees it when it is, how fast, can it be recalled | Tolerance is a property of the step, not of the system |
| Data fitness | The real rung of the data the step consumes, cited from the fitness scorecard | A step that acts on the face value of a distorted field fails the data cell; unknown rung = fail |
| Decision rights layer | sense / advise / act / decide | At the act layer and above, tolerance is preset to zero tolerance |

**Fill the maintainability cell last and hardest.** It is the cell most likely to be filled in as "should be fine," because inside a company its cost never settles on one day, it spreads into two extra alerts a week and three extra days of regression per model generation (illustrative). Before you fill it, name the receiving side. If you cannot name one, the receiving side is you. Three receiving sides, three arguments: the business line's own IT (protect their ownership as co-builders), a Group-wide ops team (they can hold only something that runs, has a manual and an action for every alert), your own team (the argument is your own calendar). In place of the handoff physical, run this test: suppose this step is being debugged at midnight three years from now (illustrative) by a colleague who has not been hired yet. Could he handle it alone? No answer, and this cell does not pass. The sentence for the meeting, "Every extra notch of complexity we pick is another slice of ops headcount this system takes next year, and that headcount comes out of our team's capacity for new projects." The complexity you choose is your own night shift.

**Stop at the first cell that does not pass.** One cell failing puts the design out, and the rest need not be filled in. Record which cell it stopped at, so the conclusion points at that cell's evidence and not at the proposer.

**A generated number about to enter a deterministic step** → a layer of validation or a person in between, always. A generated amount into a payout calculation or a generated date into a regulatory filing runs the whole system to the standard of its loosest step.

**"It already runs"** → the demo's pattern goes through the table again before production. Build the demo with whatever pattern you like; demo assets are reused piece by piece (prompts, schema), the architecture is not inherited.

**A premise changes (data fitness improves, the eval goes live, the decision rights boundary moves up)** → fill the table again. Selection is a state, not a property; date every conclusion with its premises.

## Procedures

**Fill the table for a system.**
1. Get the sponsor's endorsement of "ruling by the table" as a procedure, once, before any design is on the table. Not his backing for one design. The rule he endorses: every step where AI intervenes is filled in row by row against the same table, it stops at the first cell that does not pass, and it treats every proposal alike, including the ones you make yourself.
2. List the AI intervention points, one line per step.
3. Per step, write the three preconditions.
4. Work down from Rules and stop at the first pattern whose five cells pass. Where the Rules row fails (free text, no fields), the table's first conclusion is an upgrade to extraction + rules; confine the output to a fixed schema and reject anything outside it. Put the LLM where its output can be checked.
5. Mark the tolerance and the backstop at every intervention point on the architecture diagram.
6. A rejected proposal goes into the scope log with the reason for refusal and a revival condition written as an event, standard form "The eval shows the current pattern cannot clear the threshold."
7. Date the conclusion and its premises.

**A smarter pattern is proposed, at any rank.**
1. Rule on nothing at the standup. Book two hours (rule). Say "Not judging the design good or bad, filling it in row by row against the criteria. You fill it in."
2. The proposer fills the table. You ask questions on the first row only, "The action goes straight out. Out to whom? What is the consequence of one wrong output, who sees it, can it be recalled?"
3. Stop at the first failing cell. Say "The design is not wrong. The layer is." Let the AI's suggestions earn a record of being accepted before anyone talks about letting it act; on that day, whether to use agents is for the eval to say.
4. Point the proposer at the hardest engineering that survives (the extraction pipeline; the prompt inside his agent, stripped of the agent shell, is version one of the extractor) and let him claim it. The enthusiasm lands somewhere else, it is not doused.
5. Scope log row: the proposal, the proposer, the reason for refusal (errors go outside and cannot be recalled, are hard to locate, and the data does not support it), the revival event.

**The proposer outranks you (your manager, the architecture committee).**
1. Before the meeting, take "ruling by the table" to the sponsor as a procedure, once. Endorsed, the meeting is a proposal against a table, not you against him.
2. You are not the facilitator. The business-side owner or the proposer chairs. You only ask questions; you do not rule.
3. The conclusion goes into the scope log with the reason and the revival event, and not a word about whose judgment is faulty.

**Two internal levers.**
- Cite the technology stack standard or the architecture committee's whitelist, with restraint. It counts as a red line only if you can name which standard it is. A "the company does not allow it" that cannot name the clause is only a shield.
- Find the corpses. How the company's previous agent project really died, who wrote it, who maintains it, whether anyone still uses it, what criteria it was picked on. Its causes of death go into the anti-pattern list as this company's own entries.

**Before a design review, run the anti-pattern vote.** Send the list to the whole team; each person ticks anonymously "which of these we are committing right now." Any entry with two or more votes (rule) goes on the review agenda. The value of an anti-pattern is in making it unsayable beforehand, not in naming it afterwards.

| # | Anti-pattern | The words you hear | Corrective action |
|---|---|---|---|
| 1 | Resume-driven architecture | "This project is a good chance to get fluent in the agent framework"; internally, "can this go in the promotion package," "the annual report needs a line that says we shipped agents" | Through the table; the criteria recognize neither learning value nor the wording of a report. Schedule the learning separately, off the critical path |
| 2 | The demo's pattern straight into production | "The demo already runs, do not tear it down" | Through the table again before production; reuse assets, not the architecture |
| 3 | Uncertainty into a step that cannot be wrong | "Just let the model work out this amount while it is in there" | Tolerance and backstop marked at every intervention point; validation or a person before a deterministic step |
| 4 | Reverse dogma | "We had an incident last time, so no LLM goes to production" | Replace the ban with the table; if eval evidence says upgrade, upgrade one layer at a time |
| 5 | Generalizing into a platform, agents ahead of time | "Build it general-purpose and it will run any process later" | Back to the thin slice; into the scope log with revival "after the second slice lands" |
| 6 | Fine-tuning a prompt problem | "The results are unstable, a bit of fine-tuning will fix it" | Exhaust prompts and schema constraints against the eval first; fine-tuning answers "where the annotated data comes from, and who retrains when it drifts" before it is heard |
| 7 | Using RAG as a database | "Ask it how much this claim paid out and it can answer" | Exact fields go through queries and rules; RAG answers only questions whose answer lives in a document, always with citations. A retrieval hit is not a correct fact |
| 8 | Chained LLMs in place of deterministic logic that works | "Have an agent judge whether these two records are the same claim" | What can be joined is not generated, what can be looked up is not inferred; repair the join key |
| 9 | Talking about upgrades with no eval | "Users say it is not smart enough, let us go multi-step" | Freeze the upgrade and build the eval; a proposal must cite which class of cases fails the threshold |
| 10 | A backstop in name only | "There is human review anyway" | Accept it against the three oversight questions, time, ability, authority; the reason column and the daily volume are design parameters, not footnotes |

## Detectors

- If the criterion for "upgrading" is written nowhere you can produce, you do not have an eval yet, and the loudest feeling wins the next upgrade.
- If you cannot say with evidence why a step is not one notch dumber, you are over-built at that step; drop a notch and try it for a week.
- If a generated number or fact lands in a calculation, a filing or an outbound message with nothing in between, the system runs to the standard of its loosest step.
- If "it already runs" is the argument for production, you are carrying a demo's selection criterion (impressive) into a place that needs a backstop, and "sunk cost" is an illusion the demo manufactured.
- If you cannot name the receiving side of a step, the receiving side is you, and the maintainability cell is being filled as "should be fine."
- If "no agent" was said in your own name instead of a table's, the meeting was you against the proposer, and whichever cell you won counts for nothing.
- If the whitelist you cited has no clause number, it is a shield, and the other side knows it.
- If "am I falling behind, building a spreadsheet with suggestions on it" is steering the choice, remember that enterprises have no demand for "occasionally impressive."

## Key judgments

- "Enterprises have no demand for 'occasionally impressive.' They have a hard requirement for 'when it is wrong, it can be caught, attributed, and rolled back.'"
- "Start with the dumbest thing, and let the evidence force the upgrade. The only legitimate reason to upgrade is eval data showing that the dumber pattern cannot clear the threshold."
- "A pattern's popularity and its applicability are badly decoupled. The hottest is precisely the one with the narrowest applicability."
- "Put the LLM where its output can be checked."
- "The complexity you choose is your own night shift."
- "One cell failing puts the design out."

## Templates

- Decision cards, filling-in checklist, anti-pattern list: `docs/appendices/template-10-pattern-decision.md` §10.2–10.4.
- Scope log row for a rejected proposal: `templates/scope-decision-log.md`; `docs/appendices/template-08-thin-slice.md`.
- The upgrade criterion lives in `templates/eval-spec.md`.

## Vendor seat

The engineers proposing the design are the client's engineers, and the receiving side is whatever the contract's handoff clause names; the crosswalk says apply the table as is. A handoff clause naming a receiving side is one line, and the maintainability cell passes only when that side has changed one thing and the change went through. A line in a contract is not a working mechanism.
