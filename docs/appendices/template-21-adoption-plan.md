# Template 21 · Adoption Plan, Super-user Agreement, Operating Cadence Sheet

> Companion chapter(s): Chapter 21. The three tools are in order of use. Do the plan first (21.1), then sign the agreement with your first super-user (21.2), and last lay the cadence into the calendar (21.3).
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

## 21.1 Adoption Plan Template (One Row Per Mechanism)

**Usage**: fill it in before launch, and none of the four rows may be blank. Every mechanism needs a named owner and a moment in time. A mechanism with no owner is not a mechanism, it is a wish. If you cannot fill in the "goal" column, go back and reread that mechanism in Chapter 21.

| Mechanism | Goal (Verifiable) | Action | Owner | When |
|------|---------------|------|-------|------|
| Super-user network | | | | |
| Operating cadence | | | | |
| Short-term win announcement | | | | |
| Institutional anchoring | | | | |

**Anchor & Helm worked example**:

| Mechanism | Goal (Verifiable) | Action | Owner | When |
|------|---------------|------|-------|------|
| Super-user network | ≥1 named super-user before the expansion; ≥1 contact point per team after it | Linda Marsh named "queue co-builder", credited by name on the five published rules, lead instructor for the expansion training; the survey team lead in an observation period | Kevin Doyle (naming rights sit with the business, not with the project side) | Week 19, the day the expansion starts |
| Operating cadence | 100% attendance at the weekly retrospective (team lead level) | Embedded in the last 30 minutes of Kevin's weekly, reason code distribution / top aging claims / status-in-doubt list / one improvement; chairing handed to Linda | Linda Marsh (chairing), Kevin Doyle (attendance discipline) | From pilot week 2; chairing handed over in week 19 |
| Short-term win announcement | One business win worth telling inside the first month | Team two's backlog cleared, announced at the monthly business review, the date it hit zero plus the drop in first-touch handling time, with team two as the subject | Kevin Doyle (the announcer must be the business owner) | The week 23 monthly meeting |
| Institutional anchoring | New reviewer onboarding material covers queue operation; the exception claim SOP references the system | Onboarding gets a one-page queue operation section plus the five rules; the SOP's exception claim section rewritten to "claim it from the queue" | Kevin Doyle (SOP), Linda Marsh (content of the operation page) | Weeks 23 to 24, settled as the expansion goes |

**Three checks**: how many times does your own team appear among the four owners? More than once and adoption is still growing on you, and the handoff will go wrong. Which of the four already has a hook in the business side's existing institutions? If not one of them does, do not launch yet. What do you check first when daily actives drop? The order is fixed, unsafe trail → manager's attendance → features.

## 21.2 Super-user Agreement

**Usage**: one page, walked through face to face with every super-user, with the business owner in the room. This is not an employment document. It makes identity and reward explicit, and it guards against the hidden exploitation of "take the feeding, give nothing back."

### Selection Criteria (All Must Hold to Be a Candidate)

- [ ] **Influence test**: a hard claim comes in and he is the one colleagues get up to go ask. Pick by that question, not by rank
- [ ] **Actual user**: the person whose daily work the system changes, not his supervisor
- [ ] **Dares to say unsafe**: has a record of rejecting the system's output to its face (Anchor & Helm: Linda Marsh's three unsafe marks in Chapter 0; the survey team lead's challenge in week 20). Someone who only says nice things cannot feed a good system
- [ ] **Voluntary**: an appointed champion is not a champion

### Privileges (What You Give)

| Privilege | What It Is |
|------|------|
| First use | New features and new rule versions two weeks before everyone else, and his view can veto the release cadence |
| Direct channel | Improvement suggestions go straight to the development board, skipping the ticket process; every one gets a reply inside two weeks; reserve a fixed response capacity allowance in your own schedule before you say this privilege out loud |
| Chairing | The queue retrospective is chaired by the super-user, not by the project side |

### Identity (What Is Made Public)

- A formal name (Anchor & Helm: "queue co-builder"), granted by the business owner in front of everyone. Naming rights sit with the business side, not with the project side
- Personal contributions credited by name in public (Anchor & Helm: the five rules signed by Linda Marsh). The self-esteem loop has to close. Promoting the system = promoting your own work
- The super-user takes the training instructor role. A peer's testimony beats the project side's pitch

### Obligations (What You Get Back)

- The feeding-period commitment. Keep using the system at its dumbest, fill in reason codes seriously. Trail quality is how the system gets paid back
- The time spent chairing the retrospective and answering new teams' questions goes into his workload, on the precedent of the business-side commitment line in the project approval memo or the charter (Anchor & Helm: "2 hours a week"); his supervisor confirms in writing how many hours a week, or it goes into the super-user's OKRs for the quarter. No free rides

### Exit Conditions (Written Down in Advance)

- Voluntary exit, at any time, no reason required. The identity is an honor, not a shackle. Ask once for him to stay, and apply no pressure
- Four straight weeks of not using the system or not attending the retrospective voids the status automatically (against a title running empty)
- Red line. Using data visibility to appraise or pressure colleagues means immediate removal. The three visibility pledges (Template 20.3) apply to super-users too

## 21.3 Operating Cadence Sheet

**Usage**: one row per tier of ritual, laid into the calendar. The "Embedded in an Existing Meeting" column is the soul of this sheet. Embed wherever you can, and creating a new ritual takes a written explanation of why no existing ritual can hold it.

| Frequency | Ritual | Agenda (Time-boxed) | Chair | Embedded in an Existing Meeting |
|------|------|-------------|------|-------------|
| Weekly | Queue retrospective (30 minutes) | Reason code distribution / top aging claims / status-in-doubt list / settle one improvement | Super-user | ✓ Embedded in the tail of the business owner's existing weekly (Anchor & Helm: Kevin's weekly) |
| Biweekly | Rotating release (Chapter 15) | The claims-ops IT engineers demonstrate progress to the owner, the three explain-it questions | Co-build engineers | ✓ Aligned to the same week as the retrospective, the heavier of the two alternating week by week (Anchor & Helm went weekly after the expansion, Chapter 22) |
| Monthly | Metrics and win announcement | Run chart of the North Star plus balancing metrics (Chapter 18) / short-term win announced (business language) / per-team review of the adoption curves | Business owner | ✓ Embedded in the one-page slot of the monthly business review |

**Two red lines**: the retrospective crowded out twice in a row by "something more important" = an adoption warning, handled the same way as a drop in daily actives; the subject of the monthly announcement must be the business team. The project side has no name on this page.

**Handoff marker** (used in Chapter 22): the day all three tiers of ritual are chaired by the business side is the day the operating cadence handoff is complete.

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/adoption/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/adoption/): sample weekly query for per-team daily actives and depth of use (daily actives = the share of users who took a Human Call action that day; depth = override rate, reason code fill rate, share of "other" codes, the last two being the detector for failure mode 2's going-through-the-motions compliance)
- [`templates/adoption/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/adoption/): sample script that generates the retrospective one-pager automatically (reason code distribution plus top aging claims, taken from the trail table in Template 17.2)
