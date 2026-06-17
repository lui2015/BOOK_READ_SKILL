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
  flashcards: [...],
  classicStories: [...]   // NEW — see Template 8
};
```

---

## Template 8: Classic Stories Extraction (经典故事)

Extract 5-8 representative stories, anecdotes, parables, or case studies from the book for the "经典故事" tab.

### Story Selection Criteria

Select stories that are ALL of the following:
- **Concrete** — has a specific protagonist, setting, or event (not a general statement)
- **Illustrative** — directly supports one of the book's core arguments
- **Memorable** — vivid enough to stick in the reader's mind
- **Self-contained** — can be understood without reading the entire book

Prioritize: stories the author explicitly uses to make a point > case studies with data > personal anecdotes > historical examples.

### Story Types

| Type ID | Chinese Label | Description |
|---------|--------------|-------------|
| `anecdote` | 寓言 | Fable, parable, or illustrative metaphor |
| `case` | 案例 | Real-world business / scientific / social case study |
| `personal` | 亲身经历 | Author's or protagonist's personal experience |
| `history` | 历史典故 | Historical event or famous historical figure's story |

### Extraction Format

For each story, produce:

```markdown
### 故事{N}：{故事标题}

**来源章节**：第{N}章
**故事类型**：{寓言|案例|亲身经历|历史典故}
**论点相关度排名**：{1-8，1=最强佐证}
**关联核心论点**：{论点标题}

**故事梗概**（100-200字）：
{叙事性段落，用生动语言描述故事的起因、经过和结果。
包含关键细节：人物、时间、地点、具体事件。
不要用列表，要写成连贯叙事。}

**作者观点解读**（150-250字）：
{分析这个故事如何佐证作者的核心论点。
必须引用书中的具体主张或数据。
解释故事与论点之间的因果逻辑链。
指出作者通过这个故事要读者得出的结论。}

**读者启示**（1-2句）：
{将故事的智慧迁移到读者自己的生活或工作场景中。
必须是可执行的行动，而不是抽象感悟。}
```

### Quality Requirements

- **梗概**：叙事连贯，有细节，禁用"他强调了X的重要性"等空话
- **解读**：必须引用书中论点，不能只是故事复述
- **启示**：具体可行，避免"要保持积极心态"等套话
- **数量**：至少5个，最多8个；少于5个说明提取不足，超过8个说明过度提取

### JSON Format for HTML Embedding

```json
{
  "classicStories": [
    {
      "id": "story_1",
      "title": "{故事标题}",
      "chapter": 3,
      "relevance": 1,
      "type": "case",
      "typeCN": "案例",
      "summary": "{故事梗概，100-200字}",
      "interpretation": "{作者观点解读，150-250字}",
      "linkedArgument": "{关联核心论点标题}",
      "insight": "{读者启示，1-2句话}"
    }
  ]
}
```
