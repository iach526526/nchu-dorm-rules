# 中興大學宿舍法規知識包（NCHU Dormitory Rules Skill）

**免責聲明：** 這是一個 AI skill ，讓大型語言模型可以根據宿舍的實際狀況做出更貼近的回應。這個專案的開發者不會對任何 AI 回覆的錯誤答案付任何責任，請自行判斷什麼時候應該找真人協助。這**只是讓你更快速掌握學校規定的工具**。



## 這是什麼？

這是一套能讓 AI 正確回答國立中興大學學生宿舍法規問題的知識包 (skill) ，盡量讓 AI 依循文件產生更準確的答案。運作原理是把學校宿舍法規 PDF 轉換為結構化的機器可讀檔案，並提供檢索流程，讓大型語言模型可以不要瞎扯。

## 解決什麼問題？

讓你習慣使用的大語言模型服務告訴你正確的宿舍規定，你可以在不看任何規章的情況下丟一個問題，讓語言模型告訴你答案和應該確認的文件位置。

### 你可以透過這個 skill 知道
- 問到宿舍的規定
- 找到對應事務的負責人
  - ~~目前只能找到網管就是~~
- 帶板手敲別人房間的門會發生什麼事
- 熱心助人的你想給學姊一個家，帶她回宿舍會怎樣
- 室友養特殊寵物可以用哪條規定約束他

### 這個專案不能幹嘛？
- X 讓你的室友有良好的衛生習慣
- X 


## Repository 結構

```
.
├── README.md                      # 本文件（中文使用說明）
├── SKILL.md                       # AI agent 操作指引（英文）
├── references/
│   ├── index.md                   # 文件路由表（Document routing manifest）
│   ├── faq_map.md                 # FAQ 對應表（FAQ-to-document map）
│   ├── contacts.md                # 聯絡窗口
│   ├── source_priority.md         # 來源優先級規則
│   ├── rules/                     # 原始 / 輕度清理之法規 Markdown
│   ├── rules_structured/          # 逐條結構化法規
│   ├── text_with_page_number/     # 含頁碼標記之純文字
│   ├── pdf-original/              # 原始 PDF
│   └── appendix/                  # 補充 PDF 指南
├── scripts/
│   ├── pdf-to-text.py             # PDF 轉文字
│   ├── validate_skill.py          # 完整性驗證
│   ├── normalize_markdown.py      # Markdown 格式清理
│   └── build_index.py             # 索引產生輔助
└── tests/
    ├── retrieval_cases.md         # 檢索測試題目
    └── expected_behavior.md       # 預期 AI 行為
```

## 來源優先級

1. **官方宿舍法規**為權威來源。
2. **各宿舍自訂公約**優先於通用宿舍法規。
3. **官方指南**僅供操作流程參考。
4. **附錄文件**僅為輔助資料。
5. **產生式摘要與 FAQ 對應表**為路由輔助工具，非權威來源。
6. **原始中文文字**優先於英文翻譯。
7. 來源衝突時，應**回報衝突**而非默認擇一，除非優先級可明確解決。

完整說明請見 `references/source_priority.md`。

## 更新法規

理論上可以直接告訴 agent 去[學務處網站](https://www.osa.nchu.edu.tw/osa/dorm/rules.html)爬資料更新，不用自己做。大體來說是這樣的流程。

1. 至 https://www.osa.nchu.edu.tw/osa/dorm/rules.html 下載新版 PDF
2. 執行 `references/index.md` 中 Update Workflow 段落之 bash 指令
3. 更新 `references/index.md` 中的版本日期
4. 執行 `python scripts/validate_skill.py` 驗證完整性
5. 確認測試案例通過

### 如何執行驗證

```bash
pip install pyyaml
python scripts/validate_skill.py
```

### 新增文件

1. 將 PDF 放入 `references/pdf-original/`
2. 轉為 Markdown：`pdftotext <pdf> references/rules/<filename>.md`
3. 在 `references/rules_structured/` 下建立結構化版本
4. 在 `references/index.md` 路由表中新增條目
5. 在 `references/faq_map.md` 中新增 FAQ 對應（如適用）
6. 執行驗證

## 收錄文件

### 住宿輔導法規

- **學生宿舍住宿輔導辦法** (1131129) — 住宿通用規則
- **學生宿舍報修處理要點** (1131017) — 報修流程
- **學生宿舍自行車及機車管理要點** (1101203) — 停車與車輛管理
- **學生宿舍公有財產物品保管辦法** (1040413) — 公物損壞賠償
- **學生宿舍借用管理要點** (1131129) — 申請、分配、入住、退宿
- **學生宿舍公用冰箱使用管理要點** (1141211) — 冰箱使用規則
- **學生宿舍冷氣儲值卡管理要點** (1131217) — 冷氣卡購買與退費

### 各宿舍公約

- **男宿公約及違規處理要點** (1140517) — 男宿專屬規定與點數制
- **女宿公約及違規處理要點** (1140820) — 女宿專屬規定與點數制
- **興大二村公約及違規處理要點** (1140507) — 二村專屬規定與點數制
- **南投宿舍公約及違規處理要點** (1121025) — 南投宿舍專屬規定與點數制

### 網路相關

- **學生宿舍網路管理要點** (1071214) — 網路註冊與使用規則
- **宿舍網路申請指引** — 網路申請步驟

### 宿舍組織

- **學生宿舍服務委員會組織章程** (1060913) — 服委會章程
- **學生宿舍服務委員會選舉及評選辦法** (1130313) — 委員選舉與評鑑
- **學生宿舍住宿生代表會組織章程** (1121024) — 宿代會章程
- **學生宿舍住宿生代表選舉辦法** (1121024) — 宿代選舉程序
- **學生宿舍志願服務實施要點** (1061110) — 志願服務時數與流程

## 授權
本專案採用你他媽的想幹嘛就幹嘛授權條款 WTFPL（Do What The Fuck You Want To Public License），你他嗎的想幹嘛就幹嘛，對。


