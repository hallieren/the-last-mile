# Scope decision log

Source: `docs/appendices/template-08-thin-slice.md` §8.3 (and `repo/templates/thin-slice/thin-slice.md`, `repo/templates/thin-slice/scope_log.py`; the repo wins on conflict).

| Field | Value |
|---|---|
| Project | <project> |
| Log owner | <owner name> REQUIRED |
| Where the log lives | <the team's shared location, not a personal folder> REQUIRED |
| Sponsor cc'd on rows from other departments | <sponsor name> |
| Last reread at | <milestone retrospective, date> |

One row per refused extension proposal. Log it on the spot.

| Date | Expansion | Proposed by (name, relation to you) | Reason for refusal (the cost, one sentence) | Revival condition (a checkable event) | Status |
|---|---|---|---|---|---|
| <date> | <what was proposed> | <proposer name>, <pilot owner / sponsor / co-build engineer / peer department> | <what doubles or slips, e.g. "eval doubles, pilot slips six weeks"> | <event, e.g. "the first extension after the pilot North Star hits target" (exclusive)> | shelved / revived / abandoned |
| <date> | <favor over half a day> | <proposer name>, <relation> | <which item of this phase it crowds out> | <event> | shelved / revived / abandoned |

**Rules**
- Log it on the spot, send it back to the proposer within 48 hours. The log itself is the proposer's answer. Most proposals want not a "yes" but an answer they can repeat. For a proposal from another department, cc the sponsor when you send it back. The cc is not tattling. It sends a lateral request into the hands of the person with the authority to rank it.
- Write the reason for refusal as a cost, not an attitude ("not for now" and "not a priority" are attitudes; "eval doubles, pilot slips six weeks" is a cost).
- Write revival conditions as events, not dates. "Look again in Q3" and nothing happens when Q3 comes. "After the pilot hits target" and when the event happens the proposer comes to open this page himself.
- Once the system enters the operating period, pilot events like "hits target" no longer occur, and revival conditions switch to operating-period anchors: "ranked with the others at next quarter's resource review", or "revisit after <operating metric> holds within threshold for <N> consecutive weeks". An entry that cannot be given either anchor is really a new project already and should go through project approval.
- The charter's "not this phase" list is this log's first batch of entries. After signing, add the cost and revival condition to each.
- The half-day rule: any "favor" over half a day (scattered support that goes through no project approval and no charter) also goes in this log. The proposer writes their name and their relation to you, and the refusal reason column states which item of this phase it crowds out.
- Reread the revival list at every milestone retrospective. Entries whose revival condition is met either start or get their condition explicitly rewritten. Renege once and this log loses its credibility. On the day the pilot hits target, this log is the ready-made phase-two roadmap.
- Platform proposals all get the same revival condition, "after the second slice lands." A good abstraction grows out of the second case. It is not guessed from the first.
- If the proposer insists, do not recompute the cost. Write both roads with the same tally on one page, quote them verbatim in that week's project report cc the sponsor, and if the second road is taken, the delay attribution column reads "scope change, <X> added this phase."

Filled in → goes to: the proposer, within 48 hours; the weekly project report (rows pasted at the end); the milestone retrospective (revival list reread); the impact memo's options (revival list items stated by their revival condition); the phase-two roadmap on the day the pilot hits target.
