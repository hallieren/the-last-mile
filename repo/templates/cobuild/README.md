# cobuild

- **Corresponding template**: Template 15 (Co-build Agreement and Knowledge Transfer Cadence) ([full appendix](../../../docs/appendices/template-15-cobuild.md))
- **One-sentence purpose**: Turn Clause One (code ownership), Clause Two (backward staffing), and Clause Three (the three explain-it questions) of the co-build agreement into three configs and templates you can drop straight into a repo.
- **File list**:

| File | What it is | How to use |
|------|--------|--------|
| `ownership-checklist.md` | Code-ownership-to-the-receiving-side checklist + the module backward staffing table (with performance accountability, gatekeeper, and handoff condition) | Fill in when signing the agreement; fill "who maintains it after handoff" first, then work backward to "who leads the writing" |
| `collaborator-access.yaml` | Sample cross-org collaborator access config (platform-neutral, comments give a mapping for each platform) | Implement item by item against whatever platform you use; your team members exit after handoff |
| `pull-request-template.md` | PR template: the three explain-it questions column + AI-generated share and explainer signature | Drop into your platform's PR template slot; the gatekeeper checks all three questions before merging |
