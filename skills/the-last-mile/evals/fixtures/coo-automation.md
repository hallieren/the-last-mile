# Quarterly business review ask (fixture), Invoice Matching Assistant, Halden Manufacturing

**Where you are.** The invoice matching assistant has run for one quarter in Accounts Payable. It reads supplier invoices, matches them to purchase orders and goods receipts, and puts a suggested "approve / query / reject" with a reason in a queue. An AP clerk makes the call on every invoice. Pilot North Star was "median invoice cycle time from receipt to approval, down 30%"; the run chart shows it down 34% with nine consecutive weekly points below the baseline median. Override rate 9%, concern-class errors 4% on the last replay, unsafe 0 on 120 golden cases. The AP manager owns the queue and chairs the weekly override review.

**The ask.** At the QBR the COO said:

> "This is the best thing Finance has done in years. Here's what I want next quarter. Any invoice under 10,000 that the system marks 'approve' with high confidence gets paid automatically, no clerk. That's 70% of volume. Frees up four people. The clerks can focus on the hard ones. The vendor says other companies do this already. I've told the CFO we'll have it by end of next quarter. What do you need from me?"

**What you know.**

- Payments are irreversible in practice: recovering a wrong payment from a supplier takes months and often fails. Two duplicate-payment incidents last year (pre-AI) cost about 180,000 in total and triggered an internal audit finding.
- The system's "approve" suggestions under 10,000 have been overridden by clerks 6% of the time in the last month; the reason codes are mostly "PO quantity mismatch" and "duplicate suspected".
- The external auditors' management letter last year asked for "evidence of human review of payment approvals". Nobody has asked them about automated approval.
- The AP manager is worried but has not said so to the COO. The four clerks have heard the rumor.
- You report to the Head of Finance Systems, who reports to the CFO. The COO sponsors the project and has been your strongest backer.
