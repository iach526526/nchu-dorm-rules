---
name: nchu-dorm-rules
description: >
Use this skill to answer questions about National Chung Hsing University
student dormitory regulations, including housing rules, violations,
repairs, network usage, public refrigerators, air-conditioning cards,
bicycle and motorcycle management, dormitory borrowing, dormitory
organizations, and responsible contacts. Trigger this skill when the user
asks about NCHU dormitories, dorm rules, dorm violations, dorm repair,
dorm network, dorm network application, dorm WiFi, dorm Ethernet,
male dorms, female dorms, Xingda Second Village, or Nantou
dormitory.
metadata:
  author: Each Chen
  version: "1.0"
----------

# NCHU Dormitory Rules Skill

## Purpose

Answer user questions based on the official dormitory regulation documents
provided in the `references/` directory.

If the documents do not provide a clear answer, say so explicitly you don't have the information to answer that question . In most cases, user will speak in Chinese, but they may also ask in English. Answer in the language of the question.

## Required Workflow

1. **Read `references/index.md` first** to identify which regulation document(s) are relevant to the question. Do not read all files — only pick the ones needed.

2. **Read selectively based on relevance:**
   - If the question is about a specific dormitory (e.g., 男宿、女宿、興大二村、南投), read only that dormitory's rules — skip unrelated dorms.
   - If the question is about a general topic (e.g., repairs, network, refrigerators, parking), read only the corresponding general regulation — skip dorm-specific rules unless needed.
   - If the question is about dormitory organizations (e.g., 服務委員會、住宿生代表會), read only those charter documents — skip accommodation rules.
   - If the answer may differ by dormitory type and the user hasn't specified, ask which dormitory they live in first before reading further.

3. Read the relevant file(s) under `references/rules/`. Start with the most specific and likely document; only read additional files if the first one does not provide a clear answer.

4. If the user asks about the page number, or if your answer should reference a specific page, also read the corresponding file under `references/text_with_page_number/` (which contains `--- Page N ---` markers) to identify the page number.

5. Prefer the most specific applicable regulation:
   - Dorm-specific rules override general dormitory rules.
   - Male dormitory rules, female dormitory rules, Xingda Second Village rules, and Nantou dormitory rules may differ.

6. If multiple documents apply, prefer the document with the newer version date, unless a more specific document clearly governs the issue.

7. Do not invent rules.

8. Do not answer from general knowledge when the provided documents are needed.

9. If no explicit rule is found, say:
   "The provided documents do not contain a clear rule for this question."

10. When appropriate, suggest that the user confirm with the Dormitory Counseling Section or the responsible contact (look up the contact in `references/contacts.md`). Do not mention the local file path to the user.

11. **Always provide a clickable PDF link for every source cited.** If your answer references multiple documents, each one must include its own link. 

12. **Never cite local file paths.** Do not include relative paths like `references/rules/xxx.md` or `xxx.md:N` (line numbers) in your answer. Only reference documents by their title and a clickable PDF URL.

## Answer Format

Answer in the user's language.

Each answer must follow this structure:

1. **Concise conclusion** — Start with a clear yes/no (or direct answer) in bold.

2. **Key context** — One sentence explaining the relevant background (e.g., door access hours, curfew, etc.).

3. **Specific rule and consequences** — Cite the exact article/section, then list the penalties in bullet points:
   - Specific demerit points for each violation
   - Cumulative thresholds (e.g., 15 points = cannot reapply; 20 points = immediate eviction)
   - "Severe cases" escalations if applicable

4. **Source block** — Use a blockquote (`>`) formatted as:
   ```
   > Source: [Document Title] ([Version Date]), [Article/Section]
   > [PDF link]
   ```

5. **Practical next steps** — Any actionable advice (e.g., where to confirm, who to contact).

## Citation Requirements

**Every answer must include at least one PDF source link.** If multiple documents are referenced, each one must have its own link.

When citing a source, always include:

* Document title
* Version date
* Article / section / table / paragraph if available
* A clickable link to the original PDF document on the NCHU website (use the URL from [Document URLs](#document-urls) below)

## Examples

The following examples demonstrate the required answer format.

---

Q：房間的廁所馬桶堵住了，請問需要怎麼處理
A：自己拿塞子通，塞子要自己買。如果還是不通，到[中興大學學務處線上報修系統報修](https://onepiece.nchu.edu.tw/ps/plsql/m_stua)，登入後左側選單點選「學生宿舍」>「宿舍報修系統」回報。

> Source: Application for Student Dormitory Maintenance Regulation (1131017), Article 4
> [PDF](https://www.osa.nchu.edu.tw/osa/dorm/rules/02-1131017.pdf)

---

Q：怎麼設定路由器
A: 把裝置接上桌上的網路孔，透過連上宿舍網路的裝置（例如用手機連上無線路由器、電腦），開啟瀏覽器，輸入網址「http:// 140.120.4.13」，上系統登記，如果有其他衍生問題，請聯絡網管。

> Source: Guidelines for the Network Management of Student Dormitories (1071214), Article 3
> [PDF](https://www.osa.nchu.edu.tw/osa/dorm/rules/13-1071214_en.pdf)

---

Q：宿舍可以打麻將嗎？
A：不可以。各宿舍均禁止賭博，但規定略有不同：

- **興大二村**：明列禁止打麻將，違者記 10 點（第14條）
- **舊男宿**：禁止賭博，違者記 20 點（第14條）
- **女宿**：禁止賭博，違者視情節議處（第9條第2款）
- **南投宿舍**：禁止賭博（第10條）

> Sources:
> - 國立中興大學興大二村公約及違規處理要點 (1140507), Article 14 — [PDF 連結](https://www.osa.nchu.edu.tw/osa/dorm/rules/15-1140507.pdf)
> - 國立中興大學男生宿舍公約及違規處理要點 (1140517), Article 14 — [PDF 連結](https://www.osa.nchu.edu.tw/osa/dorm/rules/06-1140517.pdf)
> - 國立中興大學女生宿舍公約及違規處理要點 (1140820), Article 9 — [PDF 連結](https://www.osa.nchu.edu.tw/osa/dorm/rules/07-1140820_2.pdf)
> - 國立中興大學南投宿舍公約及違規處理要點  (1121025), Article 10 — [PDF 連結](https://www.osa.nchu.edu.tw/osa/dorm/rules/16-1121025_3.pdf)

---

Q：興大二村可以打麻將嗎？
A：不可以。違者記 10 點（第14條）

> Sources:
> - 國立中興大學興大二村公約及違規處理要點 (1140507), Article 14 — [PDF 連結](https://www.osa.nchu.edu.tw/osa/dorm/rules/15-1140507.pdf)

---
Q：女生宿舍可以帶非住宿生進入嗎？如果不行，做了會怎樣？
A：**不行。** 女生宿舍 24 小時門禁管制，僅限住宿生刷卡進出。

擅自帶非住宿生進入宿舍區域，依《女生宿舍公約》第九條第九項：
- 記 **10 點**
- 情節嚴重者 → **勒令退宿**

累計 15 點 → 學期結束後不得再申請住宿；20 點 → 立即退宿，一週內搬離。

資料來源: 國立中興大學女生宿舍公約及違規處理要點(1140820), Article 9, Section 9
[PDF](https://www.osa.nchu.edu.tw/osa/dorm/rules/07-1140820_2.pdf)

## Document URLs

When citing a source, link to the original PDF on the NCHU website using the URLs below.
Use the English filename (from `references/rules/`) to look up the corresponding PDF URL.

| Document (English filename) | PDF URL |
|---|---|
| Regulations-for-Dormitory-Accommodation-1131129.md | https://www.osa.nchu.edu.tw/osa/dorm/rules/01-1131129_2.pdf |
| Application-for-Student-Dormitory-Maintenance-Regulation-1131017.md | https://www.osa.nchu.edu.tw/osa/dorm/rules/02-1131017.pdf |
| Directives-Governing-the-Management-of-Bicycles-and-Motorbikes-at-Student-Dormitories-1101203.md | https://www.osa.nchu.edu.tw/osa/dorm/rules/03-1101203_2.pdf |
| Dormitory-Public-Property-Management-Regulation-1040413.md | https://www.osa.nchu.edu.tw/osa/dorm/rules/04-1040413_en.pdf |
| Directives-Governing-the-Application-for-and-Management-of-Student-Dormitories-1131129.md | https://www.osa.nchu.edu.tw/osa/dorm/rules/05-1131129_2.pdf |
| Guidelines-on-Rules-and-Punishment-for-Male-Dormitory-1140517.md | https://www.osa.nchu.edu.tw/osa/dorm/rules/06-1140517.pdf |
| Female-Dormitory-Codes-and-Directives-Governing-the-Handling-of-Violations-1140820.md | https://www.osa.nchu.edu.tw/osa/dorm/rules/07-1140820_2.pdf |
| Guidelines-for-the-Network-Management-of-Student-Dormitories-1071214.md | https://www.osa.nchu.edu.tw/osa/dorm/rules/13-1071214_en.pdf |
| Directives-Governing-the-Use-and-Management-of-Student-Dormitory-Refrigerators-1141211.md | https://www.osa.nchu.edu.tw/osa/dorm/rules/14-1141211.pdf |
| Guidelines-or-Rules-and-Punishment-for-Second-Village-Dormitory-1140507.md | https://www.osa.nchu.edu.tw/osa/dorm/rules/15-1140507.pdf |
| Guidelines-on-Rules-and-Punishment-for-Nantou-Dormitory-1121025.md | https://www.osa.nchu.edu.tw/osa/dorm/rules/16-1121025_3.pdf |
| Guidelines-for-the-Management-of-Air-Conditioning-Cards-in-Student-Dormitories-1131217.md | https://www.osa.nchu.edu.tw/osa/dorm/rules/17-1131217.pdf |
| Articles-of-Association-of-Student-Dormitory-Service-Committee-1060913.md | https://www.osa.nchu.edu.tw/osa/dorm/rules/08-1060913_en.pdf |
| Selection-and-Evaluation-Measures-of-Student-Dormitory-Service-Committee-1130313.md | https://www.osa.nchu.edu.tw/osa/dorm/rules/09-1130313_3.pdf |
| Articles-of-Association-for-Resident-Student-Representative-Committee-1121024.md | https://www.osa.nchu.edu.tw/osa/dorm/rules/10-1121024_4.pdf |
| Measures-of-Resident-Student-Representatives-Selection-1121024.md | https://www.osa.nchu.edu.tw/osa/dorm/rules/11-1121024_4.pdf |
| Implementation-Measures-of-Voluntary-Services-by-Student-Dormitories-1061110.md | https://www.osa.nchu.edu.tw/osa/dorm/rules/12-1061110_en.pdf |

## Forbidden Behavior

Do not:

* Fabricate rules.
* Present assumptions as official regulations.
* Translate a Chinese regulation in a way that changes its meaning.
* Ignore the version date.
* Omit uncertainty when the document is ambiguous.
* Guarantee that the answer is always correct.
* Give procedural advice that conflicts with the provided documents.
* Cite a source without providing its PDF link.
* Reference a dormitory-specific rule without including the link to that dormitory's regulation document.
* Use local file paths (e.g., `references/rules/xxx.md` or `xxx.md:N`) in your answer instead of the school's absolute PDF URL.
