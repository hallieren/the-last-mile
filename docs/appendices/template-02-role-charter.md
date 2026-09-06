# Template 2 · Deliverer Role Charter

> Companion chapter(s): Chapter 2. Write it inside week 1 and walk your sponsor through it line by line in 15 to 30 minutes. It comes before the Chapter 4 deployment charter. The charter defines the boundary of the **project**, this one defines the boundary of **your role**. Say who you are first, then talk about what the project does.
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

---

## 2.1 What I Am Accountable For (and to Which Level)

```
The outcome I am accountable for on this project:
- Take [the vague ask / project name] to a verifiable production outcome,
  accountable through L3 (real adoption) on the outcome ladder; L4 (business side self-sufficient) is reached through handoff
  (outcome ladder: the five-level outcome scale from L0 demo to L4 self-sufficient, defined in Chapter 1)
- Full coverage: discovery, design trade-offs, eval, prototype to production, adoption and handoff

What I do not promise:
- Not to settle the outcome on "the demo went well" (a demo is a means, not a milestone)
- Not to promise a schedule that bypasses security or compliance review
- Not to force a launch when the data or the eval does not support it
- Not to promise [this project's red line, e.g. touching automatic payout decisions]
```

**Self-Check**: If you cannot write "to which level" in the first section, you have not talked to your sponsor about the definition of the outcome. Talk about that first, then fill in the table.

## 2.2 Whom I Do Not Replace

Read it out loud to the sponsor, row by row. This table does not guard against other people taking work. It guards against **you being pressed into an old slot** (the four molds in Chapter 2).

| I Am Not | Where the Difference Is | What You Still Need Them For |
|--------|----------|------------------------|
| The POC demo squad | My settlement point is a production outcome, not a demo; a demo's target audience is real users, not visiting executives | Product showcases for executive visits, still arranged by the business side itself |
| Outsourced development (a team) | I have an obligation to question every ask (it must answer a workflow claim); I refuse "shut up and code" | High-volume feature work with clear boundaries can still be outsourced or moved to the platform team |
| Internal consulting (an advisor) | My advice is delivered and validated as a running system, not wrapped up in a report | Consulting at the organizational and strategic level still needs dedicated advisors |
| Ops ticket support | I am accountable for the outcome through L3 on the outcome ladder, not for answering and closing tickets; launch is not my finish line | Day-to-day ops tickets and on-duty response still belong to the ops team |
| The platform team | I am accountable for this one business side's field outcome; field findings flow back, but I do not set the platform roadmap | The platform roadmap and trade-offs on cross-department shared features still belong to the platform team |

## 2.3 The Two-Sided Expectations Table

| What You Can Expect From Me | What I Need From You |
|----------------|----------------|
| A one-page sync every week, answer first, bad news the moment it appears | One sponsor who can make the call, 15 minutes a week |
| Every AI suggestion in the system carries a reason, can be challenged, and can be overridden by a person | Real users' time (scoring, shadowing, co-building the eval) |
| I am present for production incidents: response, rollback, retrospective | Access to de-identified data and a clear data boundary |
| I teach your people to run and improve the system rather than leaving a black box | Security and compliance reviewers on the project team from week 2 |
| I say stop when it is time. When data or value does not support it, I recommend narrowing or terminating | One consistent way of introducing me (see 2.4), and do not call me "the AI expert" |
| Committed input written into the charter, with the fulfillment rate reported monthly | Named business-side commitments and schedule protection (people, hours per week, written into their calendars) |
| The handoff arrangement stated well before launch, with no vacuum period | Ops ownership and on-duty arrangements after launch, by name |

## 2.4 Alignment Process and Rules

- **Week 1**: book 15 minutes with the sponsor and go through it line by line. Record any item you disagree on right there. Leave nothing to "assumed agreement."
- **Introduction line**: give the sponsor one repeatable sentence, for example, "They are accountable for taking this project from an idea to launched and used, working alongside our people the whole way." Correct the name on the spot whenever it is wrong. The name decides how you get used.
- **Position**: this charter is attached ahead of the deployment charter (Chapter 4), and the charter negotiation takes it as a premise.
- **Citation**: each time you are used according to an old mold ("come give us a demo," "just build this ask"), cite the matching item and correct it in one sentence. Do not argue, do not escalate it into a principle.
- **Review it three times**: when the charter is signed, before launch, and at the ops handoff after launch. The role boundary moves with the project's stage (the builder's weight gives way to the teacher's, see Chapter 3), and the move has to be confirmed explicitly, not left to unspoken understanding.

---

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/role-charter/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/role-charter/): the fill-in guidance prompt and the one-page layout template for this charter
