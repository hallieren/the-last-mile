# Template 10 · Pattern Decision Table and Anti-pattern List

> Companion chapter(s): Chapter 10. The three tools are in the order you use them. Learn the spectrum first (10.1), then take every step where AI intervenes through the criteria card by card (10.2/10.3), and last, give the design a physical with the anti-pattern list (10.4).
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

---

## 10.1 The Pattern Spectrum at a Glance

The six patterns are ordered from dumbest to smartest by how clear the error shape is. The further down, the higher the capability ceiling and the harder it is to draw a shape for the error.

| Pattern | In One Line | The Most Typical Misuse |
|------|-----------|--------------|
| **Rules** | Deterministic logic. Same input, necessarily the same output | Hardcoding a tacit judgment that will drift (Chapter 6, failure mode 4) |
| **Structured extraction + rules** | The LLM does only the unstructured → fixed schema conversion, and everything downstream is deterministic logic | No schema validation, and the extraction output goes into the store as fact |
| **RAG** | Retrieval over a trustworthy corpus + generation of an answer with citations | Nobody maintains the corpus itself, or it is used to answer exact-field questions (query the store when a query is what is called for) |
| **Single-step LLM** | One call completes one judgment or conversion, and the output goes into a human review step | Output with no format limit and no reason attached, leaving the reviewer nothing to review |
| **Agentic workflow** | Multi-step autonomous planning and execution, path decided at run time | Put into a step where the errors go outside and nobody backstops them |
| **Fine-tuning** | Changing model weights with annotated data | Using it on a problem a prompt could solve |

---

## 10.2 Pattern Decision Cards (Six Patterns × Five Criteria, Full Version, Ready to Copy)

**Usage**. This section re-lays Chapter 10's decision table as cards (one card per pattern, the five criteria as labels, judgments identical to the chapter's decision table, so the full content fits). Run it once per AI intervention step, not once per project. Read the judgments card by card in the 10.1 spectrum order and hold them against the reality of your step. Where a judgment plainly does not hold (the step's tolerance is zero, say, while the pattern's ways of failing are open-ended), that pattern is out for this step.

### Card One · Rules

- **Error tolerance**. Ways it fails are enumerable and foreseeable. When it is wrong it stays wrong, but one fix ends it. The default choice for zero-tolerance steps.
- **Verifiability**. Fully reproducible, explainable rule by rule, exhaustively testable.
- **Data requirements**. Fields only need to be interpretable.
- **Latency and cost**. Milliseconds, near zero cost.
- **Maintainability by the receiving side**. The business-side IT or Group ops can read it, change it, and test it themselves, and the handoff cost is the lowest there is.

### Card Two · Structured Extraction + Rules

- **Error tolerance**. The error is fenced tight inside the extraction step. Schema validation intercepts format errors, and spot checks watch for semantic errors. Usable in near-zero-tolerance steps, provided the validation layer really exists.
- **Verifiability**. The extraction output can be validated against the schema and spot-checked by sample. The rules part is the same as the "Rules" card.
- **Data requirements**. The unstructured source has to be accessible. Keep a separate sample set for manual spot checks. The extraction output is derived data, and it is trustworthy only once it climbs to validated (Chapter 9).
- **Latency and cost**. One call per claim, batchable and cacheable.
- **Maintainability by the receiving side**. The rules go to the receiving side. The schema and the prompts need handoff training. The spot-check process needs an owner on the receiving side, and for as long as the spot-check owner is you, this row is your own permanent liability.

### Card Three · RAG

- **Error tolerance**. Missed retrieval and wrong retrieval both happen, and the ways it fails are open-ended. Only for steps where a person checks the citations.
- **Verifiability**. Verified by "checking the citations." Whether a citation is real can be checked, but "should have been retrieved and was not" is hard to verify. A rotten corpus rots everything.
- **Data requirements**. It needs a corpus that is genuinely trustworthy and has someone responsible for maintaining it. The corpus's fitness decides everything.
- **Latency and cost**. Two hops, retrieval plus generation. Maintaining the corpus is a long-term hidden cost.
- **Maintainability by the receiving side**. What the receiving side maintains is really the corpus. The corpus decays slowly and out of sight, so it needs a named maintenance owner and a cadence.

### Card Four · Single-Step LLM

- **Error tolerance**. Every call can be wrong and the ways it fails are open-ended. Only for steps where a person reviews row by row.
- **Verifiability**. The output cannot be verified exhaustively. Pinning the output format + requiring a reason brings verification down to "a person checks the reason."
- **Data requirements**. No training data needed. But no eval set means no threshold, which means no acceptance.
- **Latency and cost**. One hop, latency and spend both controllable and budgetable.
- **Maintainability by the receiving side**. Prompt drift (model updates, quiet edits to the wording) going unnoticed is the biggest hazard. Prompts go into version control.

### Card Five · Agentic Workflow

- **Error tolerance**. Errors compound and amplify across steps (95% on one step leaves 77% over five). If any step sends an action outside, the whole chain is reviewed as zero tolerance.
- **Verifiability**. Many intermediate states and the path varies. Failures are hard to locate and hard to reproduce, and the same input may take a different path.
- **Data requirements**. The data each step consumes has to pass fitness on its own, each step's output needs its own eval, and the cost multiplies by the number of steps.
- **Latency and cost**. Multiplied by hops, and the number of steps is settled only at run time, so latency and spend are both unpredictable (Chapter 16 does this arithmetic).
- **Maintainability by the receiving side**. The hardest to hand off. Debugging requires understanding every agent's intent and interactions, and "only the builder can fix it" means, inside a company, that you are locked in, because the maintainer is often your own team.

### Card Six · Fine-Tuning

- **Error tolerance**. Errors set into the weights. A newly found way of failing means retraining, and it cannot be patched.
- **Verifiability**. Behavior changes globally and cannot be explained locally. Every retrain requires a full regression eval.
- **Data requirements**. Thousands of high-quality annotations and up. Most sites cannot accumulate them, and once accumulated they drift out of date.
- **Latency and cost**. Training cost comes up front and recurs with every update. Inference may be cheaper, but ask first whether that training bill is worth it.
- **Maintainability by the receiving side**. The receiving side can hardly take it over at all. A retraining pipeline, an annotation team, a regression eval, and not one of them is optional.

### Three Rules for Using It (Same as the Chapter)

1. **Pick per step, not per project.** Inside one system, tolerance differs from step to step, and the pattern follows the step.
2. **Read top down and stop at the first pattern that passes all five criteria.** "Works" = all five judgments pass, not the most impressive result.
3. **An upgrade has exactly one legitimate channel, eval data showing that the dumber pattern cannot clear the threshold (Chapter 11).** The criteria cards hold in reverse too. If the evidence says upgrade, "never use agents" is just as much a dogma.

---

## 10.3 Filling-In Process Checklist

- [ ] **Get the sponsor's endorsement of "ruling by the table" as a procedure first**, not his endorsement of one design. With the procedure endorsed, every step from then on goes row by row through the same table, all proposals are treated alike, including the ones you make yourself, and what is argued at the review is a proposal against a table, not you against the proposer.
- [ ] List the AI intervention points first. Which steps in this system does AI intervene in? One line per step (an intervention point = one decision or one conversion, not one feature module).
- [ ] For every step, write down three things before you look at the cards:
  - The step's **error tolerance** (how many times may it be wrong? who sees it when it is, how fast, and can it be recalled?), carrying on from Risk, one of Chapter 7's five questions.
  - The **real position** on the fitness ladder of the data the step consumes (cite the conclusion of the Template 9.2 scorecard directly).
  - Which layer of the **decision rights boundary** the step sits in (sense / advise / act / decide, Template 8.2). For steps at the act layer and above, tolerance is preset to zero tolerance.
- [ ] Work down from the "Rules" card, taking each pattern through the five criteria, and stop at the first pattern that passes all five.
- [ ] When somebody proposes jumping to a pattern further down, **have the proposer fill in the table himself** (what Anchor & Helm did in Chapter 10). A judgment can only be rebutted. It cannot be overruled by rank.
- [ ] A rejected pattern proposal goes into the scope decision log (Template 8), and the revival condition is written as an event. "The eval shows the current pattern cannot clear the threshold" is the standard form.
- [ ] Mark the selection conclusion with its date and its premises. Fill it in again when a premise changes (data fitness improves, the eval goes live, the decision rights boundary moves up). Pattern selection, like fitness, is a state, not a property.

---

## 10.4 Anti-pattern List

Matched to Chapter 10's failure modes and extended. Each entry gives a warning signal (the actual words you can hear at a review) and a corrective action.

| # | Anti-pattern | Warning Signal (Actual Words) | Structural Root Cause | Corrective Action |
|---|--------|------------------|-----------|----------|
| 1 | **Resume-driven architecture** | "This project is a good chance to get fluent in the agent framework" | How new the stack is calibrates an engineer's market value. The project account settles in three months, the resume account settles the same day. The department's annual report also needs a line that says "we shipped agents," and that pressure runs top down, onto the line that runs your schedule and your review, which is harder to push back on than a resume | Proposals go through the decision table, and the criteria recognize neither learning value nor the wording of a report. Schedule the learning separately, off the critical path |
| 2 | **The demo's pattern straight into production** | "The demo already runs, do not tear it down" | A demo selects on how impressive it is, production on whether it can be backstopped. "It already runs" manufactures the illusion of a sunk cost | Go through the table again before production. Demo assets can be reused piece by piece (prompts, schema). The architecture is not inherited |
| 3 | **Uncertainty into a step that cannot be wrong** | "Just let the model work out this amount while it is in there" | Probabilistic behavior is invisible on an architecture diagram. Tolerance is a property of the step, and if it is not drawn nobody aligns on it | Mark the tolerance and the backstop at every AI intervention point on the architecture diagram. Before a generated number enters a deterministic step there has to be a layer of validation or a person in between |
| 4 | **Reverse dogma** | "We had an incident last time, so no LLM goes to production" | An incident sets into a ban, and a ban is cheaper than judging case by case | Replace the ban with the decision table. If eval evidence says upgrade, upgrade, one layer at a time |
| 5 | **Generalizing into a platform, agents ahead of time** | "Build it general-purpose and it will run any process later" | The legitimate raw material for abstraction is repetition (Chapter 8). The generality of LLMs made a platform demo cheap, and production cost did not move | Go back to the thin slice. Platform proposals go into the scope decision log, with the revival condition "after the second slice lands" |
| 6 | **Fine-tuning a prompt problem** | "The results are unstable, a bit of fine-tuning will fix it" | Fine-tuning sounds "more engineering" than editing a prompt, and it justifies a budget | Exhaust prompts and schema constraints first, comparing with the eval. Fine-tuning has to answer "where the annotated data comes from, and who retrains when it drifts" first |
| 7 | **Using RAG as a database** | "Ask it how much this claim paid out and it can answer" | The generative interface hides the fact that an exact field calls for an exact query. A retrieval hit is not the same as a correct fact | Exact fields go through queries and rules. RAG answers only questions whose answer lives in a document, and always with citations |
| 8 | **Chained LLMs in place of deterministic logic that works** | "Have an agent judge whether these two records are the same claim" | Doing deterministic work with a probabilistic component feels "smarter." The right answer to a broken linkage is repairing the join key (Chapter 9) | What can be joined is not generated, what can be looked up is not inferred. Leave the LLM only the conversions deterministic logic genuinely cannot do |
| 9 | **Talking about upgrades with no eval** | "Users say it is not smart enough, let us go multi-step" | "Feelings" are cheap and cannot be rebutted. With no eval in place, the loudest feeling wins | Freeze the upgrade question and build the eval first (Chapter 11). An upgrade proposal has to cite which class of cases the current pattern fails the threshold on |
| 10 | **A backstop in name only** | "There is human review anyway" | Review is treated as a disclaimer rather than a design object. Review with no time, no ability, and no authority is review in name only | Accept it against Chapter 12's three oversight questions. Is there time to look? The ability to judge? The authority to stop it? The reason column and the daily volume are design parameters, not footnotes |

**How to use it**. Before a design review, send this table to the whole team and have each person tick anonymously "which of these we are committing right now." Any entry with two or more votes goes on the review agenda. The value of an anti-pattern is not in naming it afterwards. It is in making it unsayable beforehand.

---

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/pattern-selection/decision-table/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/pattern-selection/decision-table/): the decision table in electronic form and the script that generates the intervention point list
- [`templates/pattern-selection/schema-check/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/pattern-selection/schema-check/): schema validation scaffolding for extraction-type steps (field type / enum value / required field validation + a rejection log)
- [`templates/pattern-selection/spot-check/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/pattern-selection/spot-check/): the spot-check log (sampling, ruling, semantic error classification)
