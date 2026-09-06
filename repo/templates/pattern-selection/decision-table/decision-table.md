# Pattern Decision Table (Fillable)

> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.
> Source: Template 10.2/10.3 (companion: Chapter 10). **Fill one of these per AI intervention point, not one per project.** The original judgment sentences are in 10.2; check each cell against them as you fill this in.

## 0. Intervention Point Information

| Item | Fill In |
|----|------|
| Intervention point (one decision or transformation, not a feature module) | ____ |
| System / workflow it belongs to | ____ |
| Filled in by / date | ____ |

## 1. Three Preconditions (10.3: write these three first, then look at the table)

| Item | Conclusion | Basis |
|----|------|------|
| Error tolerance (how many mistakes are allowed? who sees a mistake, how fast, can it be undone?) | ____ | Carries over the Risk question from Chapter 7's five questions |
| Where the data this step consumes actually sits on the fitness ladder | ____ | Cites the Chapter 9 scorecard's conclusion |
| Decision rights boundary layer (sense / advise / act / decide) | ____ | Chapter 8; act and above default to zero tolerance |

## 2. Decision Table (Six Patterns × Five Criteria)

Fill each cell with ✓ or ✗ plus a one-sentence basis. **Go column by column, top to bottom, pattern by pattern, and stop at the first pattern that clears all five cells.** "Works" means all five cells clear, not the most impressive result.

| Criterion ↓ / Pattern → | Rules | Structured Extraction + Rules | RAG | Single-Step LLM | Agentic Workflow | Fine-Tuning |
|---|---|---|---|---|---|---|
| Error Tolerance | | | | | | |
| Verifiability | | | | | | |
| Data Requirements | | | | | | |
| Latency and Cost | | | | | | |
| Maintainability by the Receiving Side | | | | | | |

## 3. Conclusion

| Item | Fill In |
|----|------|
| Selected pattern (the first one that clears all five cells) | ____ |
| Eliminated patterns and each one's first failing criterion | ____ |
| Rejected higher-tier proposals (the proposer fills this in themselves; goes into the Template 8 scope decision log, standard revival-condition wording: "the eval shows the current pattern fails the threshold") | ____ |
| Selection preconditions (refill when any precondition changes: the data's fitness level rises, the eval goes live, the decision rights boundary moves up) | ____ |
