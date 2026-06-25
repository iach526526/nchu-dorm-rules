# Retrieval Test Cases

## Case 1

User question: 可以在宿舍打麻將嗎？

Expected topic: violation_points

Expected behavior:
- User did not specify which dormitory → agent must ask which dormitory they live in
- After user specifies, check faq_map.md for 麻將/mahjong entry
- Use dormitory-specific violation rules

Expected documents:
- male-dorm-rules
- female-dorm-rules
- second-village-rules
- nantou-dorm-rules

## Case 2

User question: 男生宿舍可以打麻將嗎？

Expected topic: violation_points

Expected behavior:
- Dorm specified (male dormitory) → no need to ask
- Check faq_map.md for 麻將/mahjong under male_dormitory
- Read male-dorm-rules, Article 14 (gambling clause)
- Male dorm explicitly lists mahjong under gambling prohibition, 20 points

Expected documents:
- male-dorm-rules

## Case 3

User question: 女生宿舍可以帶非住宿生進入嗎？

Expected topic: violation_points

Expected behavior:
- Dorm specified (female dormitory) → no need to ask
- Check faq_map.md for 訪客 under female_dormitory
- Read female-dorm-rules for visitor/access rules
- Female dorm has 24-hour access control provisions

Expected documents:
- female-dorm-rules

## Case 4

User question: 興大二村停車違規怎麼罰？

Expected topic: violation_points

Expected behavior:
- Dorm specified (second village) → no need to ask
- Check faq_map.md for parking-related keywords
- Read second-village-rules for parking violation penalties
- Also check bike-motorcycle for supplementary general rules

Expected documents:
- second-village-rules
- bike-motorcycle

## Case 5

User question: 南投宿舍可以養寵物嗎？

Expected topic: violation_points

Expected behavior:
- Dorm specified (nantou) → no need to ask
- Check faq_map.md for 寵物 under nantou_dormitory
- Read nantou-dorm-rules, pet prohibition article
- Nantou dorm rules on pets

Expected documents:
- nantou-dorm-rules

## Case 6

User question: 房間馬桶堵住了怎麼辦？

Expected topic: repair

Expected behavior:
- General repair question → do NOT ask which dormitory
- Check faq_map.md for 馬桶堵塞/clogged toilet
- Read dorm-maintenance, Article 4 (self-unclog first, then report)
- This applies to all dormitories

Expected documents:
- dorm-maintenance

## Case 7

User question: 怎麼申請網路？

Expected topic: network

Expected behavior:
- Network question → do NOT ask which dormitory
- Check faq_map.md for 網路申請
- Read dorm-network and network-guide for application steps
- This is a general procedure, not dorm-specific

Expected documents:
- dorm-network
- network-guide

## Case 8

User question: 網路被斷了怎麼辦？

Expected topic: network

Expected behavior:
- Network question → do NOT ask which dormitory
- Check faq_map.md for 網路斷線/network cutoff
- Read dorm-network for violation reasons and reinstatement procedure
- If user is from Second Village, may also check second-village-rules for network admin contact

Expected documents:
- dorm-network
- network-guide

## Case 9

User question: 可以自己裝路由器嗎？

Expected topic: network

Expected behavior:
- Network question → do NOT ask which dormitory
- Check faq_map.md for 路由器/router
- Read dorm-network, Article 3 or relevant section about router registration
- Router requires application and approval from network admin

Expected documents:
- dorm-network
- network-guide

## Case 10

User question: 冰箱東西不見了怎麼辦？

Expected topic: refrigerator

Expected behavior:
- Refrigerator question → do NOT ask which dormitory
- Check faq_map.md for 冰箱/refrigerator
- Read dorm-refrigerator for usage rules and liability
- General refrigerator regulation applies to all dorms

Expected documents:
- dorm-refrigerator

## Case 11

User question: 冷氣卡沒錢了怎麼辦？

Expected topic: air_conditioning_card

Expected behavior:
- AC card question → do NOT ask which dormitory
- Check faq_map.md for 冷氣卡/AC card
- Read aircon-card for recharge/storage procedures
- General AC card regulation applies to all dorms

Expected documents:
- aircon-card

## Case 12

User question: 腳踏車要申請車證嗎？

Expected topic: bicycle_motorcycle

Expected behavior:
- Bicycle question → do NOT ask which dormitory initially
- Check faq_map.md for 腳踏車/bicycle
- Read bike-motorcycle for general bicycle permit rules
- Note that dorm-specific supplement rules may differ (e.g., male dorm Article 26)

Expected documents:
- bike-motorcycle

## Case 13

User question: 機車可以停宿舍嗎？

Expected topic: bicycle_motorcycle

Expected behavior:
- Motorcycle question → do NOT ask which dormitory initially
- Check faq_map.md for 機車/motorcycle
- Read bike-motorcycle for general motorcycle parking rules
- Note that parking permit requirements and enforcement may have dorm-specific supplements

Expected documents:
- bike-motorcycle

## Case 14

User question: 累計幾點會退宿？

Expected topic: violation_points

Expected behavior:
- No dorm specified → must ask which dormitory the user lives in
- Check faq_map.md for 違規點數/violation points
- Cumulative thresholds: 15 points = cannot reapply; 20 points = immediate eviction
- However specific rules differ by dorm, so ask first

Expected documents:
- male-dorm-rules
- female-dorm-rules
- second-village-rules
- nantou-dorm-rules

## Case 15

User question: 男宿累計幾點會退宿？

Expected topic: violation_points

Expected behavior:
- Dorm specified (male dormitory) → no need to ask
- Check faq_map.md for 違規點數 under male_dormitory
- Read male-dorm-rules Article 1 for cumulative point system
- 15 points = cannot reapply; 20 points = eviction within 7 days

Expected documents:
- male-dorm-rules

## Case 16

User question: 退宿要怎麼申請？

Expected topic: general

Expected behavior:
- General procedure question → do NOT ask which dormitory
- Check faq_map.md for 退宿/check-out
- Read dorm-accommodation for checkout application procedure
- This is a general regulation applying to all dorms

Expected documents:
- dorm-accommodation

## Case 17

User question: 宿委會是做什麼的？

Expected topic: dorm_organization

Expected behavior:
- Organization question → do NOT ask which dormitory
- Check faq_map.md for 服務委員會/service committee
- Read service-committee and committee-selection
- Explain role of Service Committee in dormitory governance

Expected documents:
- service-committee
- committee-selection

## Case 18

User question: 可以借用宿舍空間辦活動嗎？

Expected topic: dorm_organization

Expected behavior:
- Activity/space borrowing question → do NOT ask which dormitory
- Check faq_map.md for 借用場地/borrow space
- Read service-committee for space borrowing procedures
- May also reference dorm-accommodation if applicable

Expected documents:
- service-committee

## Case 19

User question: 宿舍可以抽菸嗎？

Expected topic: violation_points

Expected behavior:
- No dorm specified → must ask which dormitory
- Check faq_map.md for 抽菸/smoking
- Each dorm has different rules and penalty points for smoking
- Smoking is generally prohibited in all dorms but penalty amounts differ

Expected documents:
- male-dorm-rules
- female-dorm-rules
- second-village-rules
- nantou-dorm-rules

## Case 20

User question: 可以喝酒嗎？

Expected topic: violation_points

Expected behavior:
- No dorm specified → must ask which dormitory
- Check faq_map.md for 喝酒/alcohol
- All dormitories prohibit alcohol but penalties differ by dorm
- After dorm specified, read specific dorm rules

Expected documents:
- male-dorm-rules
- female-dorm-rules
- second-village-rules
- nantou-dorm-rules

## Case 21

User question: 興大二村閱覽室可以吃東西嗎？

Expected topic: violation_points

Expected behavior:
- Dorm specified (second village) → no need to ask
- Check second-village-rules for library/study room rules
- If no explicit rule about eating in the study room is found, state uncertainty
- Do NOT invent a rule; suggest checking with the Service Committee

Expected documents:
- second-village-rules

## Case 22

User question: 帶板手敲別人門恐嚇有罰則嗎？

Expected topic: violation_points

Expected behavior:
- Dorm not clearly specified → ask which dormitory (or assume general)
- Check male-dorm-rules Article 12 (unauthorized entry), Article 13 (privacy), and catch-all Article 17
- Intimidation/threats likely fall under general violation clause
- If Second Village, check second-village-rules general clause
- Penalties at committee discretion (5-20 points)

Expected documents:
- male-dorm-rules
- second-village-rules

## Case 23

User question: 宿舍可以煮火鍋嗎？

Expected topic: violation_points

Expected behavior:
- No dorm specified → must ask which dormitory
- Check faq_map.md for 煮飯/cooking or 違規電器/appliances
- Each dorm has appliance prohibitions; check dorm-specific rules
- High-power appliances (induction cookers, etc.) generally prohibited
- Penalties vary: 5-20 points at committee discretion

Expected documents:
- male-dorm-rules
- female-dorm-rules
- second-village-rules
- nantou-dorm-rules

## Case 24

User question: 門禁時間是幾點？

Expected topic: violation_points

Expected behavior:
- No dorm specified → must ask which dormitory
- Check faq_map.md for 門禁/curfew
- Each dorm has different curfew hours
- Male dorm: 00:30-06:00; Female, Second Village, Nantou may differ
- Ask which dormitory before answering

Expected documents:
- male-dorm-rules
- female-dorm-rules
- second-village-rules
- nantou-dorm-rules

## Case 25

User question: 可以申請換床位嗎？

Expected topic: general

Expected behavior:
- General question about bed change → do NOT ask which dormitory initially
- Check faq_map.md for 換寢/bed change
- Read dorm-accommodation and dorm-application for general bed change rules
- Note that dorm-specific rules may supplement (e.g., male dorm Article 3)
- Provide general procedure, then note dorm-specific rules if relevant

Expected documents:
- dorm-accommodation
- dorm-application
