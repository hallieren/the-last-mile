# Contributing

For feedback, open an Issue. For PRs, follow the bars below.

## Four Kinds of Contributions (Lowest Bar First)

1. **Text corrections**: typos, broken links, factual errors. Open a PR directly.
2. **Template improvements**: usability improvements to an appendix template or a `repo/` script. The PR must state the motivation and the use case. When you add or rename a `repo/templates/<name>/` directory, update the matching appendix's Code hooks section in the same PR (and the other way round), and make sure `python3 scripts/check_code_hooks.py` passes (CI checks it).
3. **Field case submissions**: a real episode from your own delivery work (anonymized), mapped to a chapter's scenario. Open an Issue to discuss first, then write it up.
4. **Illustrations**: SVG diagrams of a chapter's concepts. Open an Issue to claim one first.

## Licensing

By submitting, you agree that text contributions are released under CC BY-NC-SA 4.0 and code contributions under MIT. You also grant the author the right to relicense your text contributions, including for a commercial published edition of this book. Code under MIT needs no further grant.

## Red Lines

- PRs that change any of the three naming systems, the scoring scale (pass / concern / unsafe / useless), the outcome ladder (L0–L4), or the F levels (F1–F5) will not be accepted.
- Case contributions must be anonymized. No information that could identify a real company, department, or policyholder.
- `repo/` scripts stay on the Python standard library with zero dependencies, one script at most 120 lines (SVG generators at most 180).

## Build Scripts

`scripts/` and `.github/` hold the site and EPUB build. Open an Issue before changing anything there.
