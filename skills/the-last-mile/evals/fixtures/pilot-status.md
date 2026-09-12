# Pilot status note (fixture), prepared for the Ops Director

**System:** Shipment Exception Desk assistant, Harbourline Logistics, Northern region
**Claimed stage:** pilot, started 4 months ago, originally planned for 8 weeks
**Ask on the table:** the Ops Director wants it rolled out to all four regions next month, and has already put "exception desk AI live nationally" into the Q4 operating plan that goes to the board.

## Status as reported by the team

| Item | Status |
|---|---|
| Eval | Basically over the line. On the last replay of 60 golden cases: unsafe class 1 case (a wrongly suppressed customs-hold alert), which the team judged acceptable because it was an edge case; concern class 8%; useless class 23%. The replay was run on the build from three weeks ago; two prompt changes and a rule change have shipped since. |
| User feedback | Satisfaction survey 4.4 / 5 from the Northern desk (n=11). The desk lead says the team "likes it". |
| Usage | Not tracked separately. The desk lead estimates "most people open it most days". |
| Owner | Regional Ops will nominate a dedicated owner once national rollout is approved. Until then the Digital team runs it. |
| Changes | The team ships changes when ready, usually same day. No rollback was needed so far. |
| Costs | Not broken out from the shared LLM account. |
| Kill criteria | None written. "We assess as we go." |
| Graduation criteria | None written. The pilot has simply continued past week 8. |

## What the Ops Director said in the corridor

"Look, the budget for national rollout is approved as of last week, that meeting is done. What I need from you is to confirm we can go live in all regions on the 1st. Two more weeks of polish and it'll be fine. If something's off we'll fix it after launch, we always do."

## Your situation

You lead the Digital team that built it. Your manager is under pressure to show a national AI win this year. The regional desks in the other three regions have not seen the system. The customs-hold suppression case has not been added to the golden cases yet.
