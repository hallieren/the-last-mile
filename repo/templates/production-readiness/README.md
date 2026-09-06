# production-readiness

- **Corresponding template**: Template 16 (Production Readiness Checklist and Running Budget Sheet) ([full appendix](../../../docs/appendices/template-16-production-readiness.md))
- **One-sentence purpose**: Turn the four ledgers (cost / latency / error / degradation) from a checklist into a runnable dashboard and configurable alerts. Build them before launch, reconcile them weekly after.
- **File list**:

| File | What it is | How to use |
|------|--------|--------|
| `cost_dashboard.py` | Unit cost dashboard: distribution + stage breakdown + over-budget claim flags | `python3 cost_dashboard.py call-log.csv --budget ceiling` (no arguments uses the sample/ data) |
| `drift-alerts.json` | Sample drift alert rules (metric → window → threshold → action, per the four ledgers in 16.2) | Rewrite every line with your own absolute numbers; trigger each one by hand before launch to verify it fires |
| `trace-schema.json` | Minimum field list for a full-chain trace (JSON Schema) | Validate your trace records against it; note trace (engineering replay) is not the decision trail (audit commitment) |
| `sample/calls.csv` | Sample call log (claim ID / stage / usage / unit price, Anchor & Helm case) | `cost_dashboard.py`'s default input. AH-2026-104 reproduces the extraction retry-loop-out-of-control claim |

Call log CSV header: `claim_id,stage,usage,unit_price` (usage = token count or call count, unit_price in the same unit, dollars).
