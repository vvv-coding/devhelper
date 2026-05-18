import html
import importlib
import re
from datetime import datetime
from pathlib import Path

from flask import Flask, abort, render_template


app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
LAB_DIR = BASE_DIR / "lab"
LAB_FILE_PATTERN = re.compile(r"^Lab(\d+)\.md$", re.IGNORECASE)
STEP_HEADING_PATTERN = re.compile(r"^##\s*Step\s+\d+", re.IGNORECASE)
LAB_TITLE_PATTERN = re.compile(r"^Lab\s+\d+\s*:\s*(.+)$", re.IGNORECASE)


def extract_title(markdown_text: str, fallback: str) -> str:
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            title = stripped[2:].strip()
            match = LAB_TITLE_PATTERN.match(title)
            if match:
                return match.group(1).strip()
            return title
    return fallback


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower())
    return slug.strip("-")


def extract_preview(markdown_text: str) -> str:
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        return stripped[:180]
    return "No content added yet."


def extract_step_count(markdown_text: str) -> int:
    return sum(1 for line in markdown_text.splitlines() if STEP_HEADING_PATTERN.match(line.strip()))


def format_modified_label(path: Path) -> str:
    modified = datetime.fromtimestamp(path.stat().st_mtime)
    return modified.strftime("%b %d, %Y")


def render_markdown(markdown_text: str) -> str:
    if not markdown_text.strip():
        return "<p>This file is empty.</p>"

    try:
        markdown_module = importlib.import_module("markdown")
    except ModuleNotFoundError:
        escaped = html.escape(markdown_text)
        return (
            "<div class='notice'>Install <code>markdown</code> for rich rendering: "
            "<code>pip install markdown</code>.</div>"
            f"<pre>{escaped}</pre>"
        )

    return markdown_module.markdown(
        markdown_text,
        extensions=["fenced_code", "tables", "sane_lists"],
    )


def load_labs() -> list[dict]:
    labs = []
    if not LAB_DIR.exists():
        return labs

    for path in sorted(LAB_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        match = LAB_FILE_PATTERN.match(path.name)

        if match:
            lab_id = match.group(1)
            default_title = f"Lab {lab_id}"
        else:
            lab_id = path.stem.lower().replace("_", "-")
            default_title = path.stem.replace("_", " ")

        labs.append(
            {
                "id": lab_id,
                "file_name": path.name,
                "title": extract_title(raw, default_title),
                "slug": slugify(extract_title(raw, default_title)),
                "preview": extract_preview(raw),
                "raw": raw,
                "html": render_markdown(raw),
                "step_count": extract_step_count(raw),
                "modified": format_modified_label(path),
                "status": "success",
            }
        )

    return labs


@app.route("/")
def home():
    return render_template("index.html", labs=load_labs())


@app.route("/labs/<lab_id>")
def lab_detail(lab_id: str):
    labs = load_labs()
    selected = next((lab for lab in labs if lab["id"] == lab_id), None)
    if selected is None:
        abort(404)
    return render_template("article.html", lab=selected, labs=labs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

