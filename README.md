# Dev Monorepo Template

ドキュメント・スライド・ソースコードを一体管理する Monorepo テンプレートです。
Markdown でスライドとドキュメントを書き、GitHub Pages に自動デプロイします。

## 技術スタック

- **ドキュメント**: [MkDocs](https://www.mkdocs.org/) + [Material テーマ](https://squidfunk.github.io/mkdocs-material/)
- **スライド**: [Marp](https://marp.app/)（Markdown → HTML スライド）
- **CI/CD**: GitHub Actions（main push → GitHub Pages 自動デプロイ）
- **パッケージ管理**: [uv](https://docs.astral.sh/uv/)（Python）、npm（Node.js）

## 前提条件

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- Node.js 20+

## セットアップ

```bash
# 1. リポジトリをクローン
git clone <your-repo-url>
cd <repo-name>

# 2. 依存関係をインストール
uv sync
npm ci

# 3. スライドをビルドしてドキュメントをプレビュー
bash slides/scripts/build-local.sh
uv run mkdocs serve
```

ブラウザで `http://localhost:8000` を開くとドキュメントサイトが確認できます。

## ディレクトリ構成

```
.
├── docs/          # MkDocs ドキュメント（slides/ は自動生成）
├── slides/
│   ├── src/       # スライドのソース（Markdown + テーマ CSS）
│   └── scripts/   # ローカルビルドスクリプト
├── hooks/         # MkDocs フック（スライド一覧の自動生成）
├── mkdocs.yml     # MkDocs 設定
└── pyproject.toml # Python 依存関係
```

## スライドの追加

```bash
# テンプレートをコピー
cp -r slides/src/slides/_template slides/src/slides/<新しい名前>

# content.md を編集してビルド
bash slides/scripts/build-local.sh
```

スライドは MkDocs のドキュメントサイトに自動的に一覧表示されます。

## GitHub Pages の設定

1. GitHub リポジトリの Settings → Pages → Source を `gh-pages` ブランチに設定
2. main ブランチに push すると自動デプロイされます

## Claude Code での開発

このリポジトリは Claude Code での開発を想定しています。
`CLAUDE.md` にプロジェクト固有の指示が記載されています。
