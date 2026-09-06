# The Last Mile

[![smoke](https://github.com/hallieren/the-last-mile/actions/workflows/smoke.yml/badge.svg)](https://github.com/hallieren/the-last-mile/actions/workflows/smoke.yml) [![docs](https://github.com/hallieren/the-last-mile/actions/workflows/docs.yml/badge.svg)](https://github.com/hallieren/the-last-mile/actions/workflows/docs.yml) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22543658.svg)](https://doi.org/10.5281/zenodo.22543658)

> **A demo is L0. Delivery is L4. Enterprise AI dies in the last mile, not in the model.**

Written for the people inside a company who are accountable for taking an AI project to production and into daily use, whatever their title. Two assumptions: you can build the system yourself or have someone next to you who can, and the project has a sponsor who can commit people and schedule, even if that is only your own manager. The vendor-side FDE is where this method comes from; the [Vendor Crosswalk](docs/appendices/internal-fde-mapping.md) maps every chapter to that seat. 27 chapters, 24 field templates, and 22 zero-dependency scripts, following one delivery cycle from a vague one-line ask to the day you step out of the daily. The guide (reading paths, the fire index, the template main chain) is in [docs/index.md](docs/index.md).

*Anchor & Helm Insurance and Swiftway Logistics are fictional composites assembled from common enterprise scenarios; they correspond to no real company, and every character is fictional.*

## How to read

- **Online**: <https://hallieren.github.io/the-last-mile/> (full-text search, dark mode, previous and next chapter).
- **On GitHub**: the chapter links below go straight to the text.
- **Offline**: [EPUB](https://hallieren.github.io/the-last-mile/the-last-mile.epub), or build your own locally with `./scripts/build_epub.sh` (requires pandoc).
- **Locally**: `uvx --from mkdocs-material mkdocs serve`, then open <http://127.0.0.1:8000>.

## Hand it to your agent

Every chapter's "Next Monday" section is followed by a block you can paste straight into Claude Code, Codex, or any coding agent. It copies the chapter's templates into your working directory, runs the companion scripts on their sample data, asks you field by field instead of making things up, and stops where the call is yours to make. The one-time setup block is in [Start Here](docs/index.md). An agent can also read the whole book: [llms.txt](https://hallieren.github.io/the-last-mile/llms.txt) (index) and [llms-full.txt](https://hallieren.github.io/the-last-mile/llms-full.txt) (full text).

## Chapters

| # | Chapter | Templates |
|---|---|---|
| **Part 0** | | |
| 0 | [The Opening 48 Hours](docs/chapters/ch00-field-mvp.md) | [Template 0](docs/appendices/template-00-field-mvp-pack.md) |
| **Part I · Position and Mindset** | | |
| 1 | [The Last Mile Problem](docs/chapters/ch01-last-mile.md) | / |
| 2 | [The Internal Deliverer's Position](docs/chapters/ch02-inheritance.md) | [Template 2](docs/appendices/template-02-role-charter.md) |
| 3 | [Four Identities](docs/chapters/ch03-four-identities.md) | [Template 3](docs/appendices/template-03-capability.md) |
| **Part II · Discovery** | | |
| 4 | [Opening and Agreement](docs/chapters/ch04-charter.md) | [Template 4](docs/appendices/template-04-deployment-charter.md) |
| 5 | [Trust Ships First](docs/chapters/ch05-trust.md) | [Template 5](docs/appendices/template-05-stakeholder-map.md) |
| 6 | [Field Archaeology](docs/chapters/ch06-field-archaeology.md) | [Template 6](docs/appendices/template-06-field-archaeology.md) |
| 7 | [The Opportunity Screen](docs/chapters/ch07-opportunity.md) | [Template 7](docs/appendices/template-07-five-questions.md) |
| **Part III · Design** | | |
| 8 | [From Use Case to Boundary](docs/chapters/ch08-thin-slice.md) | [Template 8](docs/appendices/template-08-thin-slice.md) |
| 9 | [Data Reality](docs/chapters/ch09-data-fitness.md) | [Template 9](docs/appendices/template-09-data-fitness.md) |
| 10 | [Pick the Pattern](docs/chapters/ch10-pattern-selection.md) | [Template 10](docs/appendices/template-10-pattern-decision.md) |
| 11 | [Eval as Spec](docs/chapters/ch11-eval-as-spec.md) | [Template 11](docs/appendices/template-11-eval-spec.md) |
| 12 | [Trust Constraints](docs/chapters/ch12-trust-constraints.md) | [Template 12](docs/appendices/template-12-trust-matrix.md) |
| 13 | [The Trade-off Story](docs/chapters/ch13-tradeoff-narrative.md) | / |
| **Part IV · Build and Run** | | |
| 14 | [Prototype, Pilot, Production](docs/chapters/ch14-prototype-pilot-production.md) | [Template 14](docs/appendices/template-14-stage-gates.md) |
| 15 | [Co-build with the Engineers Who Will Take Over](docs/chapters/ch15-cobuild.md) | [Template 15](docs/appendices/template-15-cobuild.md) |
| 16 | [Production Engineering](docs/chapters/ch16-production-engineering.md) | [Template 16](docs/appendices/template-16-production-readiness.md) |
| 17 | [From Dashboard to Action Queue](docs/chapters/ch17-dashboard-to-queue.md) | [Template 17](docs/appendices/template-17-action-queue.md) |
| 18 | [Launch and Measure](docs/chapters/ch18-launch-and-metrics.md) | [Template 18](docs/appendices/template-18-metric-tree.md) |
| **Part V · Adoption and Transfer** | | |
| 19 | [Talking to Executives](docs/chapters/ch19-executive-memos.md) | [Template 19](docs/appendices/template-19-memo-suite.md) |
| 20 | [Resistance Is a Signal](docs/chapters/ch20-resistance-as-signal.md) | [Template 20](docs/appendices/template-20-resistance-decoder.md) |
| 21 | [Adoption Engineering](docs/chapters/ch21-adoption-engineering.md) | [Template 21](docs/appendices/template-21-adoption-plan.md) |
| 22 | [Make the Business Side Self-Sufficient](docs/chapters/ch22-handoff.md) | [Template 22](docs/appendices/template-22-handoff.md) |
| **Part VI · Reuse and Growth** | | |
| 23 | [The Pattern Library](docs/chapters/ch23-pattern-library.md) | [Template 23](docs/appendices/template-23-pattern-extraction.md) |
| 24 | [From the Field to the Platform](docs/chapters/ch24-field-to-product.md) | [Template 24](docs/appendices/template-24-f2p-memo.md) |
| 25 | [When to Say No](docs/chapters/ch25-saying-no.md) | [Template 25](docs/appendices/template-25-intake-redlines.md) |
| 26 | [The Deliverer's Career Path](docs/chapters/ch26-career-path.md) | / |

**Templates**: [Field Template Library (24 templates)](docs/appendices/template-library-index.md) · **Appendix**: [Vendor Crosswalk](docs/appendices/internal-fde-mapping.md) · **Companion scaffold**: [repo/](repo/README.md)

Prose CC BY-NC-SA 4.0 · code MIT ([LICENSE.md](LICENSE.md)) · [Contributing](CONTRIBUTING.md) · [How to cite](CITATION.cff)
