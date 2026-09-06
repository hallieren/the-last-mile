# Metric Tree Three-Layer Structure, Fillable (Template 18.1.1)

> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.

One row per metric. **The owner and action-on-deviation columns may not be left blank.** If you cannot fill in an action, delete the metric. It is only scenery.

| Layer | Metric | Definition and Measurement | Data Source | Baseline | Owner (Real Name) | Action on Deviation (Who Does What) |
|----|------|-----------|----------|------|---------------|----------------------|
| North Star (outcome) | ____ | From the charter, the only one | ____ | ≥8 weeks before launch | ____ | ____ |
| Process (mechanism) | ____ | Can be changed directly by an action | ____ | ____ | ____ | ____ |
| Process (mechanism) | ____ | | ____ | ____ | ____ | ____ |
| Balancing (cost) | ____ | Whose cost the improvement might shift onto | ____ | ____ | ____ | ____ |
| Balancing (cost) | ____ | | ____ | ____ | ____ | ____ |
| Monitoring surface (fairness) | ____ | Override distribution spot-checked by customer segment, etc.; definition follows the eval spec (Template 11) | ____ | / | ____ | ____ |

See the Anchor & Helm example filled in at Template 18.1.2 (North Star = first-touch handling time for auto exceptions; process = queue aging / missing-document detection lead time / override rate / status-in-doubt list length; balancing = complaint rate / reviewer overtime hours).

## Checklist (Template 18.1.3)

- [ ] The North Star is unique and matches the charter's North Star word for word. No new metric gets created after launch.
- [ ] Every metric has an owner and an action on deviation. The owner is a real name, not a department.
- [ ] At least 2 balancing metrics, shown on the same page as the outcome metrics.
- [ ] Baseline: at least 8 weeks of data before launch, checked record by record for data trust.
- [ ] The run chart shows every point, no cherry-picking weeks. An improvement claim only gets made when a special cause signal shows up (auto-flagged by `run_chart.py`).
- [ ] The monitoring surface is kept on the same sheet as the metric tree (override alert thresholds are in `override-alert-config.json`).
