# the-last-mile

A Claude Skill distilled from *The Last Mile: A Field Guide to Deploying AI Systems That Survive the Enterprise* (this repository). It is for the person inside an organization who is accountable for taking an AI initiative from a vague ask, a prototype or a stuck pilot into production and daily use, and who has to rule on what happens next: take it or not, start the pilot or not, roll out or not, step out or not.

It is not a summary of the book. `SKILL.md` carries the judgment the book repeats across chapters (a named owner and a fixed moment its numbers are read; evidence is something that already happened; unsafe is counted in cases; events, never dates; drafted by you, issued by the one with the power to violate it), a router by situation, the decision procedures for the moments where projects live or die, the output contracts for the artifacts, a table of the sentences people say when a project is dying and what it would take instead, and a review mode with a closed tag set. `references/` holds one file per moment; `templates/` holds the book's main delivery chain as 13 fill-in files; `scripts/` holds four stdlib tools.

It is not for eval statistics, judges and sample sizes, model training or prompt technique, writing the application code, or project management with no AI component.

## Install

In Claude Code, add this repo as a plugin marketplace and install:

```
/plugin marketplace add hallieren/the-last-mile
/plugin install the-last-mile@the-last-mile
```

Or install by hand with a symlink into wherever your agent loads skills from:

```bash
ln -s "$(pwd)/skills/the-last-mile" ~/.claude/skills/the-last-mile
```

Nothing to build; the scripts need Python 3.9+ and the standard library only.

## Layout

- `SKILL.md`: the router, rules, procedures, contracts, review mode. Read this first.
- `references/`: one file per moment in the delivery cycle (Field MVP, saying not now, charter, discovery, thin slice, data fitness, pattern selection, eval as spec, trust constraints, executive memos, stage changes, build and run, launch / adopt / handoff, closeout and platform, stuck-project diagnosis). Each opens with "Load this reference when".
- `templates/`: the main chain in order, workflow claim → charter and pre-mortem → Five Ones and scope log → data fitness → eval spec → gates and kill criteria → queue and trail → memos → handoff plan. The other field templates are in `docs/appendices/`.
- `scripts/`: `gate_check.py`, `run_chart.py`, `screen.py`, `override_report.py`. Each has `--help` and `--selftest`.
- `evals/`: the test prompts, fixtures and assertions used to check the skill against a no-skill baseline.

## Source and license

The book is the source of truth; when this skill and a chapter disagree, the chapter wins. Chapters and templates are CC BY-NC-SA 4.0; the scripts and the code in `repo/` are MIT. See `LICENSE.md` at the repository root.
