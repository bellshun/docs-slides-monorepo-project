# セットアップガイド

## 前提条件

| ツール | バージョン | インストール方法 |
|---|---|---|
| Python | 3.12+ | [python.org](https://www.python.org/) |
| uv | 最新 | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Node.js | 20+ | [nodejs.org](https://nodejs.org/) |
| Git | 任意 | [git-scm.com](https://git-scm.com/) |

VS Code を使う場合は以下の拡張機能もインストールしてください：

- **Marp for VS Code** (`marp-team.marp-vscode`) - スライドのプレビュー
- **Draw.io Integration** (`hediet.vscode-drawio`) - drawio 図の編集

リポジトリを開くと VS Code が自動的に推奨拡張機能として提案します。

## インストール手順

```bash
# 1. リポジトリをクローン
git clone <your-repo-url>
cd <repo-name>

# 2. Python 依存関係をインストール（MkDocs など）
uv sync

# 3. Node.js 依存関係をインストール（Marp CLI）
npm ci
```

## ローカルプレビュー

```bash
# スライドをビルドして docs/slides/ に配置
bash slides/scripts/build-local.sh

# ドキュメントサイトを起動
uv run mkdocs serve
```

`http://localhost:8000` でサイトが確認できます。
ファイルを保存すると自動でリロードされます。

## GitHub Pages へのデプロイ設定

1. GitHub リポジトリの **Settings** → **Pages** を開く
2. **Source** を `Deploy from a branch` に設定
3. ブランチを `gh-pages`、フォルダを `/ (root)` に設定して保存

設定後は `main` ブランチへの push で自動デプロイされます。
