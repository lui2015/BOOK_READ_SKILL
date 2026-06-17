# Extraction Templates

Standard templates for extracting knowledge from books. Apply the appropriate template based on the extraction phase.

---

## Template 1: One-Sentence Summary

Format:
```
《{书名}》的核心主张是：{用一句话概括全书论点，不超过50字}。
```

Requirements:
- Must capture the book's PRIMARY thesis, not a list of topics
- Must be specific enough to distinguish from other books in the same domain
- Avoid generic statements like "这本书探讨了..."

---

## Template 2: Core Arguments (3-5)

For each core argument, extract:

```markdown
### 论点 {N}：{论点标题}

**主张**：{一句话陈述}

**论据**：
- {支撑证据/数据/案例 1}
- {支撑证据/数据/案例 2}
- {支撑证据/数据/案例 3}

**推理链**：{前提A} → {推理步骤} → {结论}

**潜在反驳**：{最强的反对意见是什么}

**个人评价**：{X}/10 {一句话评价论证说服力}
```

---

## Template 3: Chapter Summary

For each chapter, produce a substantive narrative summary:

```markdown
### 第{N}章：{章节标题}

{叙事性总结：100-200字的连贯叙事，包含背景、核心事件/决策、关键数字、结果/影响}

【标签A】{展开说明}
【标签B】{展开说明}

> "{原文引用}" — {作者/来源}
```

**Requirements**:
1. Each chapter summary MUST be 300-600 words
2. Write connected prose, not skeleton-style bullet lists
3. Every chapter must include at least 2-3 specific data points
4. Show the reasoning chain, not just conclusions
5. Include failure cases where applicable
6. Cross-reference chapters

---

## Template 4: Knowledge Framework (Tree Data for HTML)

Generate chapter framework as JSON for HTML tree visualization:

```json
{
  "title": "{书名}",
  "children": [
    {
      "title": "第{N}部分: {部分标题}",
      "children": [
        {
          "title": "第{N}章: {章节标题}",
          "summary": "{一句话概括}",
          "concepts": ["{概念1}", "{概念2}"]
        }
      ]
    }
  ]
}
```

---

## Template 5: Summary.md Full Structure (六部分标准)

```markdown
# 《{书名}》读书笔记

作者：{作者名}　　领域：{领域}　　消化日期：{YYYY-MM-DD}

==========================================================
第一部分　一句话总结
==========================================================

{用一句话概括全书核心主张，不超过80字}

==========================================================
第二部分　核心论点
==========================================================

【论点N】{论点标题}

主张：{一句话陈述}

论据：
  - {支撑证据1}
  - {支撑证据2}
  - {支撑证据3}

推理链：{用通顺的中文句子描述因果链}

评价：{X}/10　{一句话评价}

==========================================================
第三部分　章节框架
==========================================================

{JSON格式的树状结构数据，供HTML渲染}

==========================================================
第四部分　章节摘要
==========================================================

{每章使用三层结构：总结段 + 标签展开 + 引用}

==========================================================
第五部分　关键概念索引
==========================================================

{概念名}　（首次出现章节）
  {完整定义，3-5句话}

==========================================================
第六部分　评价及关联推荐
==========================================================

【本书评价】
  - 阅读难度：{X}/10
  - 内容深度：{X}/10
  - 原创性：{X}/10
  - 实用性：{X}/10
  - 推荐指数：{X}/10

【适合人群】
【不足之处】
【关联推荐】
  同类入门 / 深度进阶 / 视角补充
```

---

## Template 6: Knowledge.json Structure

```json
{
  "meta": {
    "title": "",
    "author": "",
    "isbn": "",
    "domain": "",
    "sub_domain": "",
    "digest_date": "",
    "language": "",
    "tags": [],
    "page_count": null,
    "publication_year": null
  },
  "one_sentence_summary": "",
  "core_arguments": [
    {
      "id": "arg_1",
      "title": "",
      "claim": "",
      "evidence": [],
      "reasoning_chain": "",
      "counter_argument": "",
      "strength_rating": 0
    }
  ],
  "chapters": [
    {
      "number": 1,
      "title": "",
      "core_point": "",
      "concepts": [],
      "key_quotes": [],
      "actionable_items": [],
      "related_chapters": []
    }
  ],
  "concepts": {},
  "frameworks": [],
  "actionable_items": [],
  "cross_references": {}
}
```

---

## Template 7: HTML Data Embedding Format

For embedding into the HTML file, structure all data as:

```javascript
const BOOK_DATA = {
  meta: { title, author, domain, digestDate, year },
  oneSentenceSummary: "",
  coreArguments: [...],
  chapterFramework: { /* tree JSON */ },
  chapters: [...],
  concepts: [...],
  review: { ratings, audience, weaknesses, recommendations },
  checklist: [...],
  flashcards: [...]
};
```
