# References

Regulation documents sourced from [NCHU Office of Student Affairs - Dormitory Section](https://www.osa.nchu.edu.tw/osa/dorm/rules.html).

## Directory Structure

| Directory | Format | Description |
|-----------|--------|-------------|
| `pdf-original/` | PDF | Original PDFs downloaded from the website, renamed by English title |
| `rules/` | Markdown | Plain text converted via `pdftotext` or manually written, consumed by the skill |
| `appendix/` | PDF | Original PDFs for practical guides (e.g., network application guide with screenshots) |
| `text_with_page_number/` | Text | Alternative conversion via PyMuPDF (fitz) with `[IMAGE]` placeholders and `--- Page N ---` markers |

## Regulatory Documents

### Dormitory Regulations (住宿法規)

| # | Document | Version |
|---|----------|---------|
| 1 | [Regulations for Dormitory Accommodation](rules/Regulations-for-Dormitory-Accommodation-1131129.md) | 1131129 |
| 2 | [Application for Student Dormitory Maintenance Regulation](rules/Application-for-Student-Dormitory-Maintenance-Regulation-1131017.md) | 1131017 |
| 3 | [Directives Governing the Management of Bicycles and Motorbikes at Student Dormitories](rules/Directives-Governing-the-Management-of-Bicycles-and-Motorbikes-at-Student-Dormitories-1101203.md) | 1101203 |
| 4 | [Dormitory Public Property Management Regulation](rules/Dormitory-Public-Property-Management-Regulation-1040413.md) | 1040413 |
| 5 | [Directives Governing the Application for and Management of Student Dormitories](rules/Directives-Governing-the-Application-for-and-Management-of-Student-Dormitories-1131129.md) | 1131129 |
| 6 | [Guidelines on Rules and Punishment for Male Dormitory](rules/Guidelines-on-Rules-and-Punishment-for-Male-Dormitory-1140517.md) | 1140517 |
| 7 | [Female Dormitory Codes and Directives Governing the Handling of Violations](rules/Female-Dormitory-Codes-and-Directives-Governing-the-Handling-of-Violations-1140820.md) | 1140820 |
| 8 | [Guidelines or Rules and Punishment for Second-Village Dormitory](rules/Guidelines-or-Rules-and-Punishment-for-Second-Village-Dormitory-1140507.md) | 1140507 |
| 9 | [Guidelines on Rules and Punishment for Nantou Dormitory](rules/Guidelines-on-Rules-and-Punishment-for-Nantou-Dormitory-1121025.md) | 1121025 |
| 10 | [Guidelines for the Network Management of Student Dormitories](rules/Guidelines-for-the-Network-Management-of-Student-Dormitories-1071214.md) | 1071214 |
| 11 | [Directives Governing the Use and Management of Student Dormitory Refrigerators](rules/Directives-Governing-the-Use-and-Management-of-Student-Dormitory-Refrigerators-1141211.md) | 1141211 |
| 12 | [Guidelines for the Management of Air Conditioning Cards in Student Dormitories](rules/Guidelines-for-the-Management-of-Air-Conditioning-Cards-in-Student-Dormitories-1131217.md) | 1131217 |

### Dormitory Organization (宿舍組織)

| # | Document | Version |
|---|----------|---------|
| 13 | [Articles of Association of Student Dormitory Service Committee](rules/Articles-of-Association-of-Student-Dormitory-Service-Committee-1060913.md) | 1060913 |
| 14 | [Selection and Evaluation Measures of Student Dormitory Service Committee](rules/Selection-and-Evaluation-Measures-of-Student-Dormitory-Service-Committee-1130313.md) | 1130313 |
| 15 | [Articles of Association for Resident Student Representative Committee](rules/Articles-of-Association-for-Resident-Student-Representative-Committee-1121024.md) | 1121024 |
| 16 | [Measures of Resident Student Representatives Selection](rules/Measures-of-Resident-Student-Representatives-Selection-1121024.md) | 1121024 |
| 17 | [Implementation Measures of Voluntary Services by Student Dormitories](rules/Implementation-Measures-of-Voluntary-Services-by-Student-Dormitories-1061110.md) | 1061110 |

### Practical Guides (實用指南)

| # | Document | Description |
|---|----------|-------------|
| 18 | [Dormitory Network Application Guide](rules/Dormitory-Network-Application-Guide.md) | Step-by-step network application procedure, includes equipment preparation, IP configuration (Windows/Mac), web portal application, troubleshooting, and MAC address lookup |

## Update Workflow

When the school publishes new versions:

### Step 1 — Download new PDFs

```bash
wget -q -O /tmp/rules.html "https://www.osa.nchu.edu.tw/osa/dorm/rules.html"
grep -oP 'https://[^"]+\.pdf' /tmp/rules.html | sort -u | wget -i - -P /tmp/nchu-pdfs/
```

### Step 2 — Extract English titles and rename

```bash
mkdir -p references/pdf-original
python3 -c "
import fitz, os, re, glob, shutil

src = '/tmp/nchu-pdfs'
dst = 'references/pdf-original'

for pdf_path in sorted(glob.glob(os.path.join(src, '*.pdf'))):
    doc = fitz.open(pdf_path)
    text = doc[0].get_text()
    doc.close()

    # First English line after Chinese title
    eng = ''
    for line in text.split('\n'):
        if re.match(r'^[A-Z]', line.strip()) and 'Chung Hsing' in line:
            eng = line.strip()
            break

    # Remove 'National Chung Hsing University ' prefix
    eng = re.sub(r'^National Chung Hsing University ', '', eng)
    # Remove ' at National Chung Hsing University' suffix
    eng = re.sub(r'\s+at\s+National\s+Chung\s+Hsing\s+University$', '', eng)
    # Extract date from server filename
    date_match = re.search(r'(\d{7})', os.path.basename(pdf_path))
    date = date_match.group(1) if date_match else '0000000'
    safe = re.sub(r'\s+', '-', eng.strip())
    safe = re.sub(r'[^\w-]', '', safe).strip('-')

    shutil.copy2(pdf_path, os.path.join(dst, f'{safe}-{date}.pdf'))
    print(f'{safe}-{date}.pdf')
"
```

### Step 3 — Convert to Markdown (rules/)

```bash
# pdftotext method (for the skill)
for pdf in references/pdf-original/*.pdf; do
  base=$(basename "$pdf" .pdf)
  pdftotext "$pdf" "references/rules/${base}.md"
done
```

### Step 4 — Convert to plain text with page numbers (text_with_page_number/)

```bash
python scripts/pdf-to-text.py references/pdf-original -o references/text_with_page_number
```

### Step 5 — Convert appendix PDFs to Markdown manually

PDFs in `appendix/` contain image-heavy practical guides that `pdftotext` cannot fully capture.
Convert them manually to `rules/` with complete textual descriptions of each image/step.

### Step 6 — Update this index

Bump version dates in the tables above to match the newly downloaded files.

## Query Process

When a user asks about dormitory rules:

1. **Ask which dormitory** — Dorm-specific rules (male, female, Second Village, Nantou) may differ. If the user does not specify, ask before answering.
2. Read `index.md` to identify the most relevant regulation document.
3. Read the relevant file under `references/rules/`.
4. Prefer the most specific applicable regulation (dorm-specific rules override general rules).

## Usage Notes

* For general information retrieval, use `rules/` (Markdown, higher semantic density).
* For page-number references, use `text_with_page_number/` (includes `--- Page N ---` markers).
