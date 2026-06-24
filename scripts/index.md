# Scripts

## Overview

This directory contains utility scripts for the NCHU dormitory rules skill. The main tool converts PDF regulations into plain text suitable for LLM reading.

## pdf-to-text.py

Converts PDF to text with image placeholders using PyMuPDF (fitz). Preserves text blocks in reading order and marks image regions with bounding box info.

### Dependencies

```bash
pip install pymupdf
```

### Single file

```bash
python scripts/pdf-to-text.py input.pdf -o output.txt
```

### Batch (directory)

```bash
python scripts/pdf-to-text.py references/pdf-original -o references/text_with_page_number
```

Omitting arguments defaults to `input.pdf` → `output.txt`.

## Data Flow

```
Web (osa.nchu.edu.tw)
  ↓ download
references/pdf-original/    ← original PDFs renamed by English title
  ↓ pdftotext
references/rules/           ← Markdown used by the skill
  ↓ PyMuPDF (fitz)
references/text_with_page_number/       ← plain text with [IMAGE] placeholders and --- Page N --- markers
```

## PDF Naming Convention

English title extracted from the PDF, stripped of "National Chung Hsing University" prefix/suffix, spaces replaced with `-`, version date appended.

Example: `National Chung Hsing University Regulations for Dormitory Accommodation` → `Regulations-for-Dormitory-Accommodation-1131129.pdf`
