# ドキュメントの追加方法

## 手順

### 1. Markdown ファイルを作成

`docs/` 以下の任意の場所に Markdown ファイルを作成します。

```bash
# 例：新しいガイドページ
touch docs/guide/my-page.md
```

### 2. mkdocs.yml の nav に追加

`mkdocs.yml` の `nav` セクションにページを追加します：

```yaml
nav:
  - Home: index.md
  - ガイド:
    - セットアップ: guide/setup.md
    - 新しいページ: guide/my-page.md  # ← 追加
  - Slides: slides/index.md
```

### 3. ローカルで確認

```bash
uv run mkdocs serve
```

## 注意事項

### 編集禁止のファイル

以下のファイルは自動生成されるため直接編集しないでください：

| ファイル | 生成元 |
|---|---|
| `docs/slides/index.md` | `hooks/slides_index.py` |
| `docs/slides/<name>/index.html` | `slides/scripts/build-local.sh` / CI |

### 絵文字の使い方

Unicode 絵文字をそのまま書くことができます：

```markdown
# 🚀 タイトル

内容 🎉
```

Markdown 拡張の twemoji も利用できます（`mkdocs.yml` で設定済み）：

```markdown
:rocket: タイトル
```

## Material テーマの機能

このサイトは MkDocs Material テーマを使用しています。
以下の記法が使用できます：

```markdown
!!! note "メモ"
    注釈ボックスが表示されます。

!!! warning "警告"
    警告ボックスが表示されます。
```
