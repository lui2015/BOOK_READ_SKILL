# Flashcard Generation Patterns

Guide for generating effective flashcards from book content. Cards should follow evidence-based learning principles: active recall, spaced repetition, and interleaving.

---

## Card Types

### Type 1: Concept Definition
```markdown
**Q**: 什么是{概念名}？
**A**: {定义}。来源：《{书名}》第{N}章
```
Use for: Key terms and concepts the reader must internalize.

### Type 2: Core Argument
```markdown
**Q**: 《{书名}》中，作者关于{主题}的核心主张是什么？
**A**: {核心论点}。论据：{关键证据}
```
Use for: The book's 3-5 main arguments.

### Type 3: Application / Scenario
```markdown
**Q**: 根据《{书名}》的{框架名}，面对{场景描述}应该怎么做？
**A**: 应该{行动建议}。因为{原理}。注意{常见错误}。
```
Use for: Practical application of the book's frameworks.

### Type 4: Compare & Contrast
```markdown
**Q**: {概念A}和{概念B}的关键区别是什么？
**A**: 
- {概念A}：{核心特征}
- {概念B}：{核心特征}
- 关键区别：{差异点}
```
Use for: Concepts that are easily confused.

### Type 5: Cause & Effect
```markdown
**Q**: 根据《{书名}》，{原因}会导致什么结果？
**A**: 会导致{结果}。作者的推理：{因果链}。
```
Use for: Causal relationships the author argues for.

### Type 6: Quote Completion
```markdown
**Q**: 补全这句话（《{书名}》）："_______{后半句}"
**A**: "{前半句}{后半句}" — {作者名}
```
Use for: Memorable, pithy quotes that encapsulate key ideas.

### Type 7: Framework Steps
```markdown
**Q**: {框架名}的第{N}步是什么？（前一步是{N-1步名}）
**A**: 第{N}步：{步骤名} — {具体做什么}
```
Use for: Multi-step frameworks that need to be memorized in order.

---

## Generation Rules

1. **Target count**: Generate 20-40 cards per book (adjust based on book density)
   - 5-8 Concept Definition cards
   - 3-5 Core Argument cards
   - 5-10 Application/Scenario cards
   - 3-5 Compare & Contrast cards
   - 2-4 Cause & Effect cards
   - 2-3 Quote Completion cards
   - Variable Framework Steps cards

2. **Difficulty distribution**:
   - 30% Easy (recognition/recall of basic facts)
   - 50% Medium (understanding and application)
   - 20% Hard (analysis, synthesis, evaluation)

3. **Card quality rules**:
   - One fact per card (no compound questions)
   - Question should be answerable in 1-3 sentences
   - Avoid yes/no questions — prefer open-ended recall
   - Include source reference (chapter number) for each card
   - Use the book's own terminology

4. **Organization**: Group cards by chapter, then by card type within each chapter

---

## Output Format

```markdown
# 🃏 《{书名}》闪卡

> {总卡片数} 张卡片 | 难度分布：🟢 Easy {N} | 🟡 Medium {N} | 🔴 Hard {N}

## 第1章：{章节标题}

### 🟢 Easy

**Q1**: {问题}
**A1**: {答案}

---

**Q2**: {问题}
**A2**: {答案}

---

### 🟡 Medium

**Q3**: {问题}
**A3**: {答案}

---

### 🔴 Hard

**Q4**: {问题}
**A4**: {答案}

---

## 第2章：{章节标题}
...
```

---

## Future Anki Export

When Anki export is needed, convert the Markdown cards to tab-separated format:
```
{question}\t{answer}\t{tags}
```

Tags should include: `book:{book-slug}`, `chapter:{N}`, `type:{card-type}`, `difficulty:{level}`
