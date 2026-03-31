#!/bin/bash
# ローカルでスライドをビルドして docs/slides/ に配置するスクリプト
# 実行後に `uv run mkdocs serve` でプレビューできる
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

for dir in "$PROJECT_ROOT/slides/src/slides/"/*/; do
  name=$(basename "$dir")
  echo "Building $name..."
  npx marp "$dir/content.md" \
    --theme-set "$PROJECT_ROOT/slides/src/themes/"*.css \
    -o "$PROJECT_ROOT/docs/slides/$name/index.html" \
    --allow-local-files

  if [ -d "$dir/images" ]; then
    mkdir -p "$PROJECT_ROOT/docs/slides/$name/images"
    cp -r "$dir/images/"* "$PROJECT_ROOT/docs/slides/$name/images/"
  fi
done

echo "✅ Done. Run 'uv run mkdocs serve' to preview."
