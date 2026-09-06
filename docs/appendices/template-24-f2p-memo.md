# Template 24 · Field-to-Product Memo and Closeout Asset Recovery Checklist

> Companion chapter(s): Chapter 24. The two tools are arranged in the direction the signal flows. At the asset inventory, run the recovery checklist (24.2) first to count the assets, then take the platform-level candidates it turns up across the river with the memo template (24.1). A signal that trips the three filters mid-project can go straight to 24.1.
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

## 24.1 Field-to-Product Memo Template

**Self-check before sending (the three filters)**, fail any row and it does not go out:

- [ ] **n≥2**: at least two business departments or projects have hit it, and n is verifiable. n=1 → into the candidate register (24.1.3), do not send.
- [ ] **Judgment structure**: what you describe is a transferable judgment structure, not one department's interface habit ("waiting attributed across steps" passes, "a Gantt chart" does not).
- [ ] **The give-up line**: name what you are willing to give up or yield for it. Cannot write it → you do not much believe in it yourself.

**Format rules**: obey the four one-page rules of Chapter 19, one page of body text, lead with the conclusion, an ask at the end, delivered 48 hours before the meeting. The reader changes from an executive on the business side to the Group platform lead. The rules do not.

### 24.1.1 The Four Sections

> **F2P Memo #[number]: [the capability name in one line].** To: [the platform lead], From: [you], [date]
>
> **Phenomenon**: which field, at what frequency, on what evidence. Quote the actual words, the decision trail data, the engineering effort records, not impressions.
>
> **The generalization case**: which other departments or scenes will hit this, and on what grounds. Write backward from the side with the need (the *Working Backwards* discipline), not forward from "what I built." State **what n is**, the name behind each n, and whether the nth implementation needed any industry adaptation.
>
> **The product recommendation (a capability, not a feature)**: what **capability** you are asking the platform to provide. Self-check, rewrite it as "add a [button / page] for [Claims Operations]" and see whether it still holds. If it does, it is a feature. Rewrite it.
>
> **The cost of not doing it**: the small bill (the engineering effort every project repeats) + the big bill (what is lost structurally, consistency, aggregation analysis, response speed).
>
> **Willing to give up for it**: one sentence.
> **What I need from you**: an ask with a date on it (a scheduling review / 30 minutes in person / a written reply).

### 24.1.2 A Worked Example (Anchor & Helm, the Decision Trail Component)

> **F2P Memo #1: the decision trail component.** To: the platform lead, From: [you], week 32
>
> **Phenomenon**: projects at two subsidiaries, Anchor & Helm (insurance claims) and Swiftway (logistics dispatch), hand-wrote the same trail layer one after the other. Suggestions and facts stored in separate tables, the suggestion table append-only, the six end-to-end decision trail fields, override reason codes (an enumeration plus an optional note). About one week of engineering each time, and the structures are near identical.
>
> **The generalization case**: the decision trail is a structural requirement of any "AI suggests, a person decides" system, and it has nothing to do with the industry. As long as decision rights stop at the advise layer, the system has to answer "who made the call and on what grounds." n=2 (the two subsidiaries Anchor & Helm and Swiftway), and the second implementation needed no industry adaptation at all.
>
> **The product recommendation (a capability)**: a decision trail component (the trail schema + reason code configuration + a review query that splits overrides by category), available to any project out of the box. (Counterexample self-check, "add a decision trail export button for Claims Operations" is a feature, not this proposal.)
>
> **The cost of not doing it**: the small bill, about a week of rewriting on every new project. The big bill, project schemas diverge and cross-department override aggregation analysis cannot be built at all. Both subsidiaries' decision trails sit in the Group warehouse. An outside team can never do this, we could have, and it is the only source of platform-level eval insight.
>
> **Willing to give up for it**: if the schedule conflicts, this team sends one person into the platform repo to co-build, and withdraws its request this quarter for custom columns in the queue interface.
> **What I need from you**: a written reply before the next platform scheduling meeting ([date]), on the roadmap / refused (with the reason, which this team records in the register).

### 24.1.3 The Candidate Register (Where n=1 and Refused Memos Are Kept)

| Signal | Source (Department / Proposer / Date) | n | Status | Trigger / Revival Condition |
|------|--------------------------|---|------|----------------|
| Repair shop response time as a metric | Anchor & Helm / the survey team lead / week 23 | 1 | candidate | Any second project that raises an "outside party response time" need promotes this to a memo |
| The queue scaffold | Anchor & Helm + Swiftway / you / after week 32 (memo #3) | 2 | refused, recorded (conflicts with the existing roadmap) | Raise it again when the platform roadmap touches a rework of queue shape |

Three rules. n=1 is registered, not reported. A refused memo goes into the table together with the reason for refusal, and its revival condition is written as events, not dates (the same form as Chapter 8's scope decision log). Go through the table once a quarter. **A memo that was refused but recorded is still an asset**.

## 24.2 Closeout Asset Recovery Checklist

**Three triggers**, the fixed retrospective N weeks after launch / before anyone moves posts / the quarterly asset inventory. Hang it on any one of them and recovery has a date, and past that window it does not happen by default. **Guiding principle**, the code may sit in the same git, but structure that was never declared is the same as structure that does not exist. Code files belong to the business line repo (Chapter 15). Schema design, the error taxonomy, and the key judgments belong to no repo at all. The four classes correspond to Chapter 23's four asset classes (component / template / judgment rule / metric model), ordered here the way an asset inventory counts them.

**Three questions per item**. Is it general (does it still hold in another industry)? What is n (how many projects have hit it)? Destination, **admit** (through Chapter 23's admission review, registered into the Template 23 asset register, must have an owner) / **send a memo** (n≥2 and at platform capability level, through 24.1) / **leave it in the business line repo** (business-line-specific, with one line on why it is not recovered). **The first two exits are not mutually exclusive.** A component at platform capability level usually goes into the library and gets reported as well (a refused report still stays in the library), and only "leave it in the business line repo" is an exclusive exit.

| Class | What Goes Through, Item by Item | General? | n= | Destination | owner |
|----|--------------|--------|----|------|-------|
| **Code** | Decision trail schema / eval harness / queue skeleton / extraction pipeline structure / configuration patterns | | | | |
| **Documents** | charter / review packet / the three memos / runbook / annotation guide **framework** (the content does not transfer) | | | | |
| **Judgment** | Key judgments / failure modes and incident retrospectives / annotation disagreement rulings as precedent | | | | |
| **Metrics** | Metric definition tree / thresholds and acceptance lines / reason code enumeration / balancing metrics | | | | |

**Anchor & Helm's sample rows** (what actually happened in Chapter 24, including the note added after the asset inventory, memo #1 went out in week 32):

| Asset | Class | General? | n= | Destination |
|------|----|--------|----|------|
| Decision trail schema | Code | Yes (a structural requirement) | 2 | Admit + send a memo (#1) |
| eval harness | Code | Yes | 2 | Send a memo (#2) |
| Queue skeleton | Code | Yes | 2 | Send a memo (#3, refused → the register). Admitted at the same time (Template 23) |
| The five rules of thumb | Judgment | No. Tacit knowledge does not transfer. The method for mining it transfers (Chapter 23) | 1 | Stays with the business side. The three-layer probing method is admitted |
| "Chase priority ≠ risk priority" | Judgment | Yes (a key judgment transfers) | 1 | Admitted (Template 23. Validation count 1 at the asset inventory, marked "awaiting a second field test." Raised to 2 after the week 31 re-verification at Swiftway) |
| Reason code enumeration (the Anchor & Helm version) | Metrics | The structure is general, the vocabulary is business-line-specific | 2 | The structure rides along with memo #1. The vocabulary stays with the business side |

**Three closing checks**:

- [ ] Every item has a destination, and "leave it for now" is not allowed. A count with no exits is the same as no count.
- [ ] Every admitted item has an owner (Chapter 23, an asset with no owner rots in six months).
- [ ] Every n=1 candidate has its trigger condition written down (24.1.3).

**Field mapping, the 24.2 recovery checklist ↔ the 23.2 asset register** (the bridge across the river for the "admit" exit. The counting finishes in this sheet and the registration lands in Template 23.2, which keeps two registration systems from growing apart):

| 24.2 Recovery Checklist Field | 23.2 Asset Register Field | How It Maps |
|------------------|--------------------|----------|
| Class (code / documents / judgment / metrics) | Class (component / template / judgment rule / metric model) | One to one (Chapter 23's four asset classes), code → component, documents → template, judgment → judgment rule, metrics → metric model |
| What goes through, item by item | Name + in one line | The one-line description is filled in at the admission review (23.3) |
| General? | / (not in the register) | A test field. Answer "no" and it takes the "leave it in the business line repo" exit, producing no register row |
| n= | Validation count | The same count. After registration it keeps accumulating with reuse. n=1 is marked "awaiting a second field test" |
| Destination | / (not in the register) | "Admit" generates one register row. "Send a memo" goes through 24.1 separately, and the two exits are not mutually exclusive |
| owner | owner | The same person. Claimed at the recovery count, confirmed at the admission review as knowing and agreeing (assignment in absentia does not count) |
| / (the recovery checklist has no such three columns) | Source project / Last updated / Status | Filled in at admission. Source = the project the asset inventory sits in. Last updated = the admission date. Status defaults to active |

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/f2p-memo/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/f2p-memo/): the f2p memo Markdown template plus the candidate register CSV structure
- [`templates/asset-recovery/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/asset-recovery/): the closeout asset recovery checklist tables plus the field alignment notes for the Template 23 register
- [`templates/f2p-memo/override-compare.sql`](https://github.com/hallieren/the-last-mile/blob/main/repo/templates/f2p-memo/override-compare.sql): sample query comparing override reason code distributions across departments (the minimal implementation of platform-level eval insight)
