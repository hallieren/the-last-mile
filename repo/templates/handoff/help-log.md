> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.

# Response-Window Help Log (Template 22.3)

Window rule: only two kinds of requests get logged here, P1 incidents (an unsafe case reaching human attention) and exceptions the escalation tree's end point could not catch. Routine ops and everyday requests are outside the window; taking one on is a return to stage 3. Log every request during the window; review once before the window closes.

- Project / system: ____
- Response window: ____ to ____ (3 months suggested)

| Date | Request (one line) | Category (P1 / exception / outside window, declined) | Which capability it points to (run/configure/exceptions/evolve/teach) | Handling and outcome | Added a targeted drill? |
|------|------------------|--------------------------------|------------------------------------------|------------|--------------------|
| [...] | ____ | ____ | ____ | ____ | ____ |

**Two questions before the window closes**: Which capability do the requests cluster on? What it needs is a targeted drill, not a document. Was the expiry action done? Drop write access to read-only, and remove the person from the oncall rotation and the standing review-meeting attendee list (this is where co-build clause one gets honored).
