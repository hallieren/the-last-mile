> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.

# Applicability Boundary: The Decision Trail Schema (read this file first, then asset.md)

## Applies When

- The system is shaped "AI suggests, a person decides": decision rights stop at the advise layer, a person makes the call, and a decision trail is a structural requirement for this kind of system, not an industry-specific one.
- The scene needs to answer "who made the call, and on what basis": audit, retrospective, override analysis, adoption measurement.

## Does Not Apply When (stop and do not use it if any of these hit)

- Decision rights have already moved up to an automated-execution step: there is no "human decision" fact, the decisions table has no subject. Go back and redesign the decision rights boundary first, do not force the schema onto it.
- A pure display scenario where the suggestion is never persisted and is discarded immediately (no retrospective need): the cost of the trail buys no future review, do not keep a trail for the trail's sake.
- A compliance environment that requires amending historical records after the fact (such as record-keeping rules built on correction, not append): this component's append-only invariant conflicts with that, get a legal ruling first.
