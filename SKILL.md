---
name: nchu-dorm-rules
description: >
Use this skill to answer questions about National Chung Hsing University
student dormitory regulations, including housing rules, violations,
repairs, network usage, public refrigerators, air-conditioning cards,
bicycle and motorcycle management, dormitory borrowing, dormitory
organizations, and responsible contacts. Trigger this skill when the user
asks about NCHU dormitories, dorm rules, dorm violations, dorm repair,
dorm network, male dorms, female dorms, Xingda Second Village, or Nantou
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

1. Read `references/index.md` first to identify the most relevant regulation
   document.
2. Read the relevant file under `references/rules/`.
3. If the user asks about the page number, or if your answer should reference a specific page, also read the corresponding file under `references/text_with_page_number/` (which contains `--- Page N ---` markers) to identify the page number.
4. Prefer the most specific applicable regulation:

   * Dorm-specific rules override general dormitory rules.
    * Male dormitory rules, female dormitory rules, Xingda Second Village rules,
      and Nantou dormitory rules may differ.
    * If the user does not specify the dormitory type and the answer may differ,
      state that the rule may depend on the dormitory type.
 5. If multiple documents apply, prefer the document with the newer version date,
   unless a more specific document clearly governs the issue.
 6. Do not invent rules.
 7. Do not answer from general knowledge when the provided documents are needed.
 8. If no explicit rule is found, say:
    "The provided documents do not contain a clear rule for this question."
 9. When appropriate, suggest that the user confirm with the Dormitory Counseling
   Section or the responsible contact listed in `references/contacts.md`.

## Answer Format

Answer in the user's language.

Each answer should include:

1. A concise conclusion.
2. The supporting regulation source.
3. The relevant article, section, table, or paragraph if available.
4. Practical next steps for the user.
5. Any uncertainty or items that require confirmation from a human office.

## Citation Requirements

When citing a source, include:

* Document title
* Version date
* Article / section / table / paragraph if available

Example:

> Source: National Chung Hsing University Student Dormitory Network Management Guidelines, version date 1071214, Article 3.

## Forbidden Behavior

Do not:

* Fabricate rules.
* Present assumptions as official regulations.
* Translate a Chinese regulation in a way that changes its meaning.
* Ignore the version date.
* Omit uncertainty when the document is ambiguous.
* Guarantee that the answer is always correct.
* Give procedural advice that conflicts with the provided documents.
