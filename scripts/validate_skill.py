"""
validate_skill.py - Validate the NCHU Dormitory Rules skill structure.

Checks:
1. SKILL.md has valid YAML front matter
2. references/index.md exists with required manifest columns
3. references/faq_map.md exists
4. Local files in index.md exist (unless UNKNOWN)
5. Every faq_map.md document ID exists in index.md
6. No references/rules/ file has lines > 500 chars
7. No SKILL.md references files that don't exist
8. PDF URL fields are valid URLs or UNKNOWN
9. references/rules_structured/ exists and is non-empty
10. Each structured file has valid YAML front matter
11. Each structured file has required fields: id, title_zh, title_en,
   version_date, source_type, applies_to, topic_tags

Exit code 0 on success, non-zero on any failure.
"""

from __future__ import annotations

import os
import re
import sys
from typing import List, Optional, Tuple

import yaml

REQUIRED_COLUMNS = [
    "ID", "Title", "Source type", "Priority", "Applies to",
    "Topic tags", "Local structured file", "Local raw file",
    "Page text file", "Version date", "PDF URL"
]

REQUIRED_STRUCTURED_FIELDS = [
    "id", "title_zh", "title_en", "version_date",
    "source_type", "applies_to", "topic_tags"
]

errors: List[str] = []
warnings: List[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def die() -> None:
    if warnings:
        for w in warnings:
            print(f"[WARN] {w}")
    if errors:
        for e in errors:
            print(f"[FAIL] {e}", file=sys.stderr)
        sys.exit(1)
    sys.exit(0)


# ---------------------------------------------------------------------------
# 1. SKILL.md has valid YAML front matter
# ---------------------------------------------------------------------------
def check_skill_yaml(skill_path: str) -> None:
    if not os.path.isfile(skill_path):
        err(f"SKILL.md not found at {skill_path}")
        return
    content = _read_file(skill_path)
    if content is None:
        return
    fm = _parse_yaml_front_matter(content, skill_path)
    if fm is None:
        return
    # check referenced files exist — only match actual file paths, not examples
    refs = _extract_file_refs(content)
    for ref in refs:
        full = os.path.normpath(os.path.join(os.path.dirname(skill_path), ref))
        if not os.path.exists(full) and not os.path.isdir(full):
            err(f"SKILL.md references '{ref}' but the file does not exist")


# ---------------------------------------------------------------------------
# 2. references/index.md exists with correct columns
# ---------------------------------------------------------------------------
def check_index(index_path: str) -> List[dict]:
    if not os.path.isfile(index_path):
        err(f"references/index.md not found at {index_path}")
        return []
    content = _read_file(index_path)
    if content is None:
        return []
    rows = _parse_markdown_table(content)
    if not rows:
        err("references/index.md has no table rows or table is empty")
        return []
    # check columns
    header = list(rows[0].keys())
    for col in REQUIRED_COLUMNS:
        if col not in header:
            err(
                f"references/index.md table is missing required column "
                f"'{col}'"
            )
    return rows


# ---------------------------------------------------------------------------
# 3. references/faq_map.md exists
# ---------------------------------------------------------------------------
def check_faq_map(faq_path: str) -> List[dict]:
    if not os.path.isfile(faq_path):
        err(f"references/faq_map.md not found at {faq_path}")
        return []
    content = _read_file(faq_path)
    if content is None:
        return []
    rows = _parse_markdown_table(content)
    if not rows:
        err("references/faq_map.md has no table rows or table is empty")
        return []
    return rows


# ---------------------------------------------------------------------------
# 4. Local files in index.md exist (unless UNKNOWN)
# ---------------------------------------------------------------------------
def check_index_local_files(rows: List[dict], base_dir: str) -> None:
    file_cols = [
        "Local structured file", "Local raw file", "Page text file"
    ]
    # Paths in index.md are relative to the references/ directory
    ref_dir = os.path.join(base_dir, "references")
    for row in rows:
        doc_id = row.get("ID", "?")
        for col in file_cols:
            val = row.get(col, "").strip()
            if not val or val.upper() == "UNKNOWN":
                continue
            # Resolve relative to references/ directory
            full = os.path.normpath(os.path.join(ref_dir, val))
            if not os.path.exists(full):
                err(
                    f"index.md doc '{doc_id}', column '{col}': "
                    f"file '{val}' not found (resolved: {full})"
                )


# ---------------------------------------------------------------------------
# 5. Every document ID in faq_map.md exists in index.md
# ---------------------------------------------------------------------------
def check_faq_doc_ids(faq_rows: List[dict], index_rows: List[dict]) -> None:
    index_ids = {r.get("ID", "").strip() for r in index_rows}
    for i, row in enumerate(faq_rows):
        doc_field = row.get("Documents to check (use IDs from index)", "")
        ids = [x.strip() for x in doc_field.replace(",", " ").split()]
        for doc_id in ids:
            if doc_id and doc_id not in index_ids:
                err(
                    f"faq_map.md row {i + 2}: document ID '{doc_id}' "
                    f"not found in references/index.md"
                )


# ---------------------------------------------------------------------------
# 6. No references/rules/ file has lines > 500 chars
# ---------------------------------------------------------------------------
def check_long_lines(rules_dir: str) -> None:
    if not os.path.isdir(rules_dir):
        err(f"references/rules/ directory not found at {rules_dir}")
        return
    for fname in sorted(os.listdir(rules_dir)):
        fpath = os.path.join(rules_dir, fname)
        if not os.path.isfile(fpath):
            continue
        content = _read_file(fpath)
        if content is None:
            continue
        for lineno, line in enumerate(content.splitlines(), 1):
            if len(line) > 500:
                err(
                    f"references/rules/{fname}:{lineno} is {len(line)} chars "
                    f"(max 500)"
                )


# ---------------------------------------------------------------------------
# 7. SKILL.md file references already checked in check_skill_yaml
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 8. PDF URL fields are valid URLs or UNKNOWN
# ---------------------------------------------------------------------------
def check_pdf_urls(rows: List[dict]) -> None:
    for row in rows:
        doc_id = row.get("ID", "?")
        pdf = row.get("PDF URL", "").strip()
        if not pdf:
            err(f"index.md doc '{doc_id}' has empty PDF URL")
        elif pdf.upper() == "UNKNOWN":
            continue
        elif not re.match(r"^https?://", pdf):
            err(
                f"index.md doc '{doc_id}' PDF URL '{pdf}' does not start "
                f"with http:// or https://"
            )


# ---------------------------------------------------------------------------
# 9. references/rules_structured/ exists and has files
# ---------------------------------------------------------------------------
def check_rules_structured(structured_dir: str) -> None:
    if not os.path.isdir(structured_dir):
        err(f"references/rules_structured/ not found at {structured_dir}")
        return
    files = [
        f for f in os.listdir(structured_dir)
        if os.path.isfile(os.path.join(structured_dir, f))
    ]
    if not files:
        err("references/rules_structured/ is empty")


# ---------------------------------------------------------------------------
# 10. Each structured file has valid YAML front matter
# 11. Each structured file has required fields
# ---------------------------------------------------------------------------
def check_structured_files(structured_dir: str) -> None:
    if not os.path.isdir(structured_dir):
        # error already reported by check_rules_structured
        return
    for fname in sorted(os.listdir(structured_dir)):
        fpath = os.path.join(structured_dir, fname)
        if not os.path.isfile(fpath):
            continue
        content = _read_file(fpath)
        if content is None:
            continue
        fm = _parse_yaml_front_matter(content, fpath)
        if fm is None:
            continue
        for field in REQUIRED_STRUCTURED_FIELDS:
            if field not in fm:
                err(
                    f"references/rules_structured/{fname} is missing "
                    f"required front matter field '{field}'"
                )


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _read_file(path: str) -> str | None:
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return fh.read()
    except Exception as exc:
        err(f"Could not read {path}: {exc}")
        return None


def _parse_yaml_front_matter(content: str, label: str) -> dict | None:
    m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not m:
        err(f"{label} has no valid YAML front matter (--- delimiters)")
        return None
    try:
        return yaml.safe_load(m.group(1))
    except yaml.YAMLError as exc:
        err(f"{label} YAML front matter parse error: {exc}")
        return None


def _parse_markdown_table(content: str) -> List[dict]:
    """Return a list of dicts from the first Markdown table found."""
    lines = content.splitlines()
    table_start = None
    for i, line in enumerate(lines):
        if line.strip().startswith("|") and line.strip().endswith("|"):
            # check that next line is a separator row
            if i + 1 < len(lines) and re.match(
                r"^\|[-\s:|]+\|$", lines[i + 1]
            ):
                table_start = i
                break
    if table_start is None:
        return []
    header_line = lines[table_start]
    headers = _split_table_row(header_line)
    # skip separator row
    rows: List[dict] = []
    for line in lines[table_start + 2:]:
        if not line.strip().startswith("|"):
            break
        cells = _split_table_row(line)
        if len(cells) != len(headers):
            continue
        row = {}
        for h, c in zip(headers, cells):
            row[h.strip()] = c.strip()
        rows.append(row)
    return rows


def _split_table_row(line: str) -> List[str]:
    """Split a markdown table row, stripping leading/trailing pipes."""
    raw = line.strip()
    if raw.startswith("|"):
        raw = raw[1:]
    if raw.endswith("|"):
        raw = raw[:-1]
    return [cell.strip() for cell in raw.split("|")]


_FILE_REF_RE = re.compile(r"`(references/[\w./-]+)`")


def _extract_file_refs(content: str) -> List[str]:
    """Extract file references from SKILL.md content (backtick-wrapped paths)."""
    refs = set()
    for m in _FILE_REF_RE.finditer(content):
        path = m.group(1)
        # skip obvious placeholder/example patterns
        if "xxx" in path or "..." in path:
            continue
        refs.add(path)
    return sorted(refs)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skill_path = os.path.join(root, "SKILL.md")
    index_path = os.path.join(root, "references", "index.md")
    faq_path = os.path.join(root, "references", "faq_map.md")
    rules_dir = os.path.join(root, "references", "rules")
    structured_dir = os.path.join(root, "references", "rules_structured")

    # 1
    check_skill_yaml(skill_path)

    # 2
    index_rows = check_index(index_path)

    # 3
    faq_rows = check_faq_map(faq_path)

    # 4
    check_index_local_files(index_rows, root)

    # 5
    check_faq_doc_ids(faq_rows, index_rows)

    # 6
    check_long_lines(rules_dir)

    # 8
    check_pdf_urls(index_rows)

    # 9
    check_rules_structured(structured_dir)

    # 10 & 11
    check_structured_files(structured_dir)

    die()


if __name__ == "__main__":
    main()
