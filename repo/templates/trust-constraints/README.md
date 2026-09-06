# trust-constraints

- Corresponding template: Template 12, Trust Constraint Matrix and Security Review Packet (companion: Chapter 12) ([full appendix](../../../docs/appendices/template-12-trust-matrix.md))
- Purpose: a ready-to-adapt mechanism sample for the matrix's "audit" row and "privacy" row, an audit log schema and a field-level redaction rule set plus a demo script
- File list:

| File | What it is | How to use |
|------|--------|--------|
| `audit-log-schema.sql` | Audit log schema sample (SQLite DDL, the trail fields from Matrix §4) | Cite directly in the security review packet's §4 "trail notes"; can also serve as a read-only view derived from the §2.1 trail tables |
| `redaction-rules.json` | Redaction rule config sample, the de-identification rules of Chapter 12 under the file's own name | Field → strategy: placeholder / hash (truncated hash) / drop; fields not listed pass through unchanged |
| `redact.py` | Redaction demo script | `python3 redact.py` (no arguments, runs on the sample); `--rules --input --out` to customize |
| `sample/claims.jsonl` | Pre-redaction record sample (sample from the book's Anchor & Helm case, all plaintext values are fictional demo values) | Default input for the demo script |

Notes:
- The audit schema follows the same conventions as CONVENTIONS §2.1's two trail tables (suggestions / decisions), but this is an **audit-view** sample (one row per suggestion, the decision folded in for readability); it need not be the same table. The DDL includes a read-only view derived from the two tables.
- The hash strategy produces a stable pseudonym, so cross-claim linkage still works (for example, a phone number's third appearance is itself a high-risk signal, the cost that 12.1.2's privacy row is paying for); a real deployment should add salt so low-entropy fields cannot be enumerated back.
- Verify redaction per 12.2 §5, sample N redacted records for a re-identification test and record the result; the `../pattern-selection/spot-check/` sampling script works for this.
