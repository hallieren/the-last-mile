# Template 12 · Trust Constraint Matrix and Security Review Packet

> Companion chapter(s): Chapter 12. The two tools are used in time order. The matrix (12.1) starts being filled after the week 2 constraint interview and updates all the way through the design, a living document of the design period. The packet (12.2) is assembled from the matrix and the design documents in the week before the review, a snapshot of the matrix at review time. Chapter 18's launch gate reuses the packet (updated to a launch version).
> License: Every template in this book may be modified freely and used in your work, no attribution needed.

---

## 12.1 Trust Constraint Matrix

### 12.1.0 Constraint Interview (Do This Before Filling the Matrix)

Who, the risk owner (the name in that cell of the stakeholder map, Template 5). When, week 2 of the opening, before the design takes shape. Everything can still be changed at that point. Go with questions, not with a design. Three must-asks:

- [ ] **What has gone wrong before?** Real incidents this company has had with data or systems. The answer marks out his actual minefield.
- [ ] **What are you afraid of?** How responsibility lands on him when something goes wrong. The answer fills the "What They Fear / What They Win" columns (Template 5), and it also explains every reaction he has later.
- [ ] **What evidence do you want to see at the review?** The review checklist in his head. The answer generates the table of contents of the 12.2 packet directly.

Interview output, a first draft of the matrix's first column plus an open questions list. Rows you cannot fill stay as open questions, not deleted, not hidden.

### 12.1.1 Blank Template (Six Constraints × Three Columns)

| Constraint | The Specific Requirement for This Project | How the Design Satisfies It (Write the Cost on the Last Line) | Who Signs Off |
|------|------------------|------------------------------|-----------|
| Privacy | | | |
| Security | | | |
| Audit | | | |
| Human oversight | | | |
| Fairness | | | |
| Maintainability | | | |

**Rules for filling the three columns**:

- **Column one**. Specific to this project, taken from the constraint interview. "Complies with the company data standard" does not count as filled in. "Customer-identifiable information may not leave the claims domain" does.
- **Column two**. A mechanism, not a promise. "We will be careful" does not count. Being able to write "at which layer, by what means, and how an error gets caught" does. **One line at the end of every cell, "Cost,"** who spends how much extra time under this way of satisfying it, and what information or capability is given up. Costs that never reach the table let constraints accumulate in one direction only (Chapter 12, failure mode 4).
- **Column three**. Real names. The day a name goes on, the reviewer turns from judge into co-author. Blank = this row has no owner yet, handle it as an open question.

**Row-by-row filling guide** (the mechanism material is long, moved into numbered notes below the table):

| Constraint | Ask Yourself for Column One | Common Qualifying Mechanisms | Anti-formality Check |
|------|-----------|--------------|----------------|
| **Privacy** | Whose information, and how far may it flow before the boundary stops it? | Note 1 | Spot-check whether de-identified data can re-identify a person; whether the right side of the line really has no plaintext |
| **Security** | Who can access what, and change what? What attack surface is new? | Note 2 | Whether the new system's permissions exceed what the same person has in the source system |
| **Audit** | When something goes wrong, can you reconstruct who did what, when, and on what basis? | Note 3 | Take one historical suggestion and actually rehearse a trace |
| **Human oversight** | At which step is a person present, and in what way is that presence real? | Note 4 | **Three questions. Is there time to look? The ability to judge? The authority to stop it?** Daily volume × review time per row, do the division in front of the reviewer |
| **Fairness** | Will the system systematically treat one class of subject worse? | Note 5 | It counts as a mechanism only if you can say "what data would reveal unfair treatment" |
| **Maintainability** | After you are reassigned, leave, or the system enters its third year with nobody watching, who can safely change it? | Note 6 | Have the future maintainer (the co-build counterpart of Chapter 15) try one change |

**Common qualifying mechanisms (material for column two, numbered by constraint)**:

1. **Privacy**. De-identification and placeholder substitution at the extraction layer; the de-identification boundary drawn on the data flow diagram; the minimum-fields principle.
2. **Security**. Permissions inherit existing system roles (no separate account system); externally writable content (emails, attachments) is handled as data, never as instructions.
3. **Audit**. A trail the whole way, including input snapshot, rule and model version, suggestion, reason, Human Call, timestamp; derived views purely read-only, AI output not written back to the source (Chapter 9's trail form).
4. **Human oversight**. The Human Call column carries a real name; every suggestion carries its reason; risk ranking with a daily volume cap.
5. **Fairness**. Ranking and suggestion logic use no identity attribute; the override distribution is spot-checked by customer segment (Chapter 18 monitoring).
6. **Maintainability**. Rules, de-identification config and thresholds become configuration items the claims-ops IT engineers can change; changes go through the existing release process; a model upgrade runs the regression eval (Chapter 11).

### 12.1.2 Anchor & Helm Example (Excerpt from the Week 8 Review Version)

| Constraint | The Specific Requirement for This Project | How the Design Satisfies It | Who Signs Off |
|------|------------------|--------------|-----------|
| Privacy | Customer-identifiable information may not enter the queue or any model call | Name / ID number / plate number / phone are replaced with placeholders at the extraction layer, no plaintext to the right of the line. Cost, same-name customers across claims are checked by hand, about 1 extra minute per claim in review | Victor Reyes |
| Security | The queue may not enlarge anyone's existing permissions | Permissions inherit core system roles, no separate accounts; email content is handled as data, not parsed as instructions. Cost, new members depend on the core system process for access, up to 3 days | Victor Reyes + the IT data team |
| Audit | Every suggestion is fully traceable | The six end-to-end decision trail fields; the merged view is purely derived, purely read-only, no write-back. Cost, log storage and the hours for the quarterly spot check | Victor Reyes |
| Human oversight | No action without human confirmation | Risk ranking with a daily volume cap (time); suggestions carry their reason (ability); the Human Call column names a person (authority). Cost, a cap on daily throughput, with the backlog going through the old manual process | Kevin Doyle |
| Fairness | Ranking may not systematically treat a customer segment worse | Priority logic carries no identity attribute; the override distribution is spot-checked by customer segment each quarter. Cost, half a day per quarter for the spot-check report | The head of compliance |
| Maintainability | After handoff, claims-ops IT can make changes on its own | Rules and de-identification config are configuration items claims-ops IT can change; a model upgrade passes the regression eval. Cost, about one extra week of development to make it configurable | Kevin Doyle + claims-ops IT |

---

## 12.2 Security Review Packet Template

**Organizing principle. Organize by the reviewer's point of view. Whatever answer he wants, write it in advance.** Open every section with one line naming which of the reviewer's questions this section answers. Send it a week ahead. Confirm section by section at the meeting, and debate only the open questions (§8).

### §0 Cover

- The system in one sentence (precise to workflow claim level) + the review scope (which components are under review, which are explicitly not)
- **Byline, two lines. Solution design (the deliverer) / constraint design (the risk owner and the other signers)**, and everyone named in column three appears here. The review conclusion memo goes out from these two jointly, recipients see two senders, and it is not downgraded to one approver's signature
- **Rule for the maintainability row's signer**. The signer may not come from this project's delivery team. Either it is signed by the business line's IT or ops, or it is left blank and handled as an open question. Self-signing does not count, that is signing yourself an ops commitment with no end date
- Nature of the review, a confirmation meeting (every row of the matrix is signed) / a ruling meeting (open questions exist, list them)

### §1 Answers-First Page (One Page)

The reviewer's top questions × a one-line answer × the section with the detail. The third question of the constraint interview decides what goes on this page. For example:

| The Reviewer's Question | One-Line Answer | See |
|--------------|----------|------|
| Does customer data leave the boundary? | No. Identifiable information is de-identified at the extraction layer, boundary shown as the red line on the data flow diagram | §2/§5 |
| Who audits the model's output? | Every suggestion carries a trail the whole way, schema and query permissions in the trail notes | §4 |
| Who is responsible when it is wrong? | No action without human confirmation; the Human Call carries a real name | §3/§6 |

### §2 Data Flow Diagram (Figure Slot)

[Figure slot: source systems → extraction and de-identification layer → merged view → queue → Human Call]. Must be labeled. The **de-identification boundary** (one solid line, plaintext on the left, none on the right); the **read-only / writable** attribute of every arrow; the **external call points** (model calls, outbound notices); and where data does not flow (draw "does not leave the boundary" explicitly).

### §3 Permission Model

| Role | What They Can Do in the Queue | Inherits From (Source System Role) | Exceptions and Why |
|------|----------------|----------------------|------------|

One line of principle. The new system enlarges nobody's existing permissions, and every exception must be listed item by item and signed.

### §4 Trail Notes

- Audit log schema (sample in Code Hooks at the end), suggestion ID / input snapshot / rule and model version / suggestion content / reason / Human Call + the decider / timestamp
- One line of declaration. AI output is written back to no source field and exists in trail form (Chapter 9)
- Retention period, query permissions, spot-check cadence

### §5 De-identification Boundary

| Field | Treatment (De-identify / Substitute / Keep) | Where It Happens | Reason for Keeping (If Kept) |
|------|---------------------------|----------|---------------------|

Attach the verification method. Take N de-identified records, run a re-identification test, and record the result.

### §6 Human Oversight Design

One line each for question × mechanism × evidence (time, the arithmetic of daily volume divided by the review time budget; ability, a sample of the reason column; authority, a demonstration of the stop path).

### §7 Rollback Path

Trigger conditions (which signal sends it back) / the rollback action and how long it takes / which old process runs after a rollback / the owner / the rehearsal record (Chapter 18 requires one real rehearsal before launch).

### §8 Open Questions

Unsettled item × suggested handling × what this meeting has to rule on. **Open questions are not hidden.** It is the blank row you hid that blows up at the review, and an open question you list yourself is a deposit into credibility (Chapter 5).

### §9 Attachments

The full trust constraint matrix (12.1) + the signature page.

**Assembly discipline**. The packet writes nothing new. Every section should be a rearrangement of material already in the matrix and the design documents. A section you cannot write while assembling means the design has a hole. Fix it at the design layer, do not paper over it at the document layer.

---

## Code Hooks

The companion repo provides (this repository's `repo/` directory):

- [`templates/trust-constraints/`](https://github.com/hallieren/the-last-mile/tree/main/repo/templates/trust-constraints/): audit log schema sample and redaction rule config sample
