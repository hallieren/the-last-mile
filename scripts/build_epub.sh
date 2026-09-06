#!/usr/bin/env bash
# Build the whole-book EPUB (27 chapters + 25 template pages + 1 appendix) for offline reading. Requires pandoc.
# Title, language and output name come from book.json.
set -euo pipefail
cd "$(dirname "$0")/.."
meta() { python3 -c 'import json,sys;print(json.load(open("book.json"))[sys.argv[1]])' "$1"; }
mkdir -p build
files=(docs/chapters/ch*.md docs/appendices/template-library-index.md)
for f in docs/appendices/template-[0-9]*.md; do
  files+=("$f")
done
files+=(docs/appendices/internal-fde-mapping.md)
out="build/$(meta slug).epub"
pandoc "${files[@]}" \
  --metadata title="$(meta epub_title)" \
  --metadata author="$(meta author)" --metadata lang="$(meta epub_lang)" \
  --toc --toc-depth=2 --resource-path=docs:docs/chapters:docs/appendices \
  -o "$out"
echo "OK: $out"
