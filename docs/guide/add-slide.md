# スライドの追加方法

## 手順

### 1. テンプレートをコピー

```bash
cp -r slides/src/slides/_template slides/src/slides/<フォルダ名>
```

フォルダ名はスライドの識別子になります（英数字・ハイフン推奨）。

### 2. content.md を編集

`slides/src/slides/<フォルダ名>/content.md` を開いて編集します。

**frontmatter の必須項目:**

```yaml
---
marp: true
theme: blue-theme
class: lead
paginate: true
title: スライドのタイトル   # ドキュメントサイトの一覧に表示される
date: 2026-01-01           # ドキュメントサイトの一覧に表示される
---
```

`title` と `date` が欠けると一覧ページに正しく表示されません。

### 3. スライドを区切る

ページの区切りは `---` で行います：

```markdown
# 1ページ目

---

# 2ページ目
```

### 4. ビルドして確認

```bash
bash slides/scripts/build-local.sh
uv run mkdocs serve
```

## 画像の使い方

画像は `slides/src/slides/<フォルダ名>/images/` に置きます。

```markdown
# インライン画像
![説明](./images/example.png)

# 右側に背景として表示（テキストと並べる）
![bg right:40% contain](./images/example.png)

# drawio ファイルをそのまま使う
![bg right:60% contain](./images/diagram.drawio.svg)
```

drawio ファイルは VS Code の Draw.io Integration 拡張でそのまま編集できます。

## テーマの変更

`content.md` の frontmatter で `theme:` を変更します：

```yaml
theme: blue-theme   # slides/src/themes/ 以下の CSS ファイル名（拡張子なし）
```

新しいテーマを追加する場合は `slides/src/themes/` に CSS ファイルを追加します。
