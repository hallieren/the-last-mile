> Companion template from The Last Mile. Modify freely and use at work, no attribution needed.

# Component Packing Sample (Template 23 Code Hooks: "Asset Body + Applicability Boundary + Verification Record Travel Together")

Pack a component-category asset into this directory structure before feeding it to a coding agent. All three files are required, and **the boundary comes before the body**: the agent (or a person) must read `boundaries.md` first before reusing it, and stops the moment a does-not-apply-when condition is hit.

```
<asset-name>/
├── asset.md          # Asset body: structure, schema, judgment sentences, the parts you can copy directly
├── boundaries.md     # Applicability boundary: applies-when + does-not-apply-when (scenarios where it backfires)
└── verification.md   # Verification record: how many times, where, who was there; fillable only by someone who was on site
```

The `trace-schema/` example is the packing of Anchor & Helm's "decision trail schema" component (sample data comes from the book's Anchor & Helm case). Two packing rules: a component with a verified count of 1 is weighted down at packing time and marked "awaiting a second live test"; `verification.md` may never be filled in by AI, AI does the grunt work, people make the calls.
