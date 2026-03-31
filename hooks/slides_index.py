"""
MkDocs hook: slides/src/slides/ 配下のスライドを読み取り、
docs/slides/index.md にカード一覧ページを自動生成する。
"""
import re
from pathlib import Path


def on_pre_build(config):
    slides_src = Path("slides/src/slides")
    docs_slides = Path("docs/slides")

    if not slides_src.exists():
        return

    docs_slides.mkdir(parents=True, exist_ok=True)

    slides = []
    for slide_dir in sorted(slides_src.iterdir()):
        if not slide_dir.is_dir():
            continue
        content_md = slide_dir / "content.md"
        if not content_md.exists():
            continue

        title = slide_dir.name
        date = ""
        text = content_md.read_text(encoding="utf-8")

        title_match = re.search(r"^title:\s*(.+)$", text, re.MULTILINE)
        date_match = re.search(r"^date:\s*(.+)$", text, re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip()
        if date_match:
            date = date_match.group(1).strip()

        slides.append({"name": slide_dir.name, "title": title, "date": date})

    lines = [
        "# スライド一覧\n\n",
        '<div class="grid cards" markdown>\n\n',
    ]

    for slide in slides:
        lines.append(f'- :material-presentation: **[{slide["title"]}](./{slide["name"]}/)**\n\n')
        if slide["date"]:
            lines.append(f'    📅 {slide["date"]}\n\n')

    lines.append("</div>\n")

    (docs_slides / "index.md").write_text("".join(lines), encoding="utf-8")
