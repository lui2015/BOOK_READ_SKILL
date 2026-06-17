# Sub-Skill Generation Template

Guide for identifying, presenting, and generating self-contained sub-skills from books.

---

## Phase 1: Candidate Identification

Scan the book's extracted content for items that are ALL of:
- **Independently executable** — can be applied to a new situation without the rest of the book
- **Has clear inputs/outputs** — user gives X, the framework produces Y
- **Structured** — has steps, criteria, thresholds, or decision logic (not just a vague principle)
- **Non-trivial** — more than a single rule (single rules → memory, not sub-skill)

### What qualifies as a sub-skill candidate

| Type | Example | Qualifies? |
|------|---------|-----------|
| Named methodology with steps | "经济利润评估法" (5步流程) | ✅ Yes |
| Decision framework with criteria | "五分位回测验证法" (5条标准) | ✅ Yes |
| Evaluation rubric with thresholds | "危险信号排查" (4个阈值) | ✅ Yes |
| Strategy with parameters | "估值+动量催化策略" (双因子组合) | ✅ Yes |
| Collection of executable models | "双因子选股模型库" (10+模型) | ✅ Yes |
| Single principle | "买低卖高" | ❌ → memory |
| Preference/opinion | "Beta不如P/S衡量风险" | ❌ → memory |
| Historical fact | "1999年泡沫期价值策略失效" | ❌ → knowledge.json |
| Vague concept without steps | "投资者情绪很重要" | ❌ → summary.md |

---

## Phase 2: Present Candidate Menu to User

**NEVER auto-generate sub-skills without user approval.**

Present the following table and wait for user selection:

```markdown
📋 可蒸馏的子Skill候选（共{N}个）

从《{书名}》中识别出以下可独立调用的方法论/策略/框架：

| # | 候选名称 | 来源章节 | 类型 | 调用场景示例 |
|---|---------|---------|------|------------|
| 1 | {name} | 第{X}章 | 框架/策略/清单/评估模型/模型库 | "{用户会怎么说}" |
| 2 | {name} | 第{Y}章 | ... | "..." |
| ... | ... | ... | ... | ... |

💡 你可以：
- 全选：回复"全部生成"
- 部分选择：回复编号，如"1, 3, 5"
- 跳过：回复"不需要子Skill"

📝 内容较简单的条目建议写入记忆而非生成子Skill（已标注在表中）
```

---

## Phase 3: Generate Selected Sub-Skills

For each user-selected candidate, generate a **self-contained** Markdown file.

### Self-Contained Requirement (CRITICAL)

Each sub-skill file MUST contain ALL information needed to execute the methodology. After loading this ONE file, the AI must be able to:
- Understand what the methodology is
- Execute every step with specific parameters
- Know the thresholds and decision criteria
- Identify failure cases and edge conditions
- Walk through at least one concrete example

**Test**: If the book and all other files were deleted, could someone still execute this methodology using only this file? If not, add more detail.

### Sub-Skill File Template

Save to: `library/{book-slug}/sub-skills/{sub-skill-id}.md`

```markdown
# {Sub-Skill Name}

> **来源**：《{book_title}》第{N}章 | **作者**：{author}
> **类型**：{框架/策略/清单/评估模型}
> **一句话**：{一句话说明这个方法论做什么}

## 适用场景

- {场景1：什么时候用}
- {场景2}
- {场景3}

## 前置条件

- {需要什么数据/信息才能执行}

## 完整步骤

### Step 1: {步骤名称}
**做什么**：{具体操作}
**输入**：{需要什么}
**输出**：{产出什么}
**判断标准**：{具体阈值/公式，不能用"较高""显著"等模糊词}
**注意事项**：{常见错误/陷阱}

### Step 2: {步骤名称}
...

### Step N: {步骤名称}
...

## 关键公式与阈值

| 指标 | 公式 | 阈值 | 含义 |
|------|------|------|------|
| {指标名} | {完整计算公式} | {具体数值} | {超过/低于阈值意味着什么} |

## 决策矩阵（如适用）

| 条件组合 | 结论 | 建议行动 |
|---------|------|---------|
| {条件A + 条件B} | {判断} | {做什么} |

## 失效场景

- **{场景1}**：{什么情况下这个方法论不适用，为什么}
- **{场景2}**：...

## 实战示例

### 示例：{具体案例名称}
**背景**：{情境描述}
**Step 1**：{执行过程和中间结果}
**Step 2**：{...}
**结论**：{最终判断}

## 速查卡片

{把最核心的信息压缩到5行以内，供快速回顾}
```

### Quality Checklist

Before saving a sub-skill file, verify ALL of the following:

- [ ] File is self-contained — can be executed without any other file
- [ ] All formulas include complete calculation method (not just variable names)
- [ ] All thresholds are specific numbers (not "较高" "显著" "适中")
- [ ] At least one complete worked example with intermediate results
- [ ] Failure cases are documented with explanation
- [ ] Steps are ordered with clear inputs/outputs for each
- [ ] Trigger phrases cover both Chinese and English patterns

---

## Phase 4: Register in Index

After generating sub-skill files, update `library/index.json`:

```json
{
  "id": "{sub-skill-id}",
  "name": "{Sub-Skill Name}",
  "source_book": "{book-slug}",
  "file": "library/{book-slug}/sub-skills/{sub-skill-id}.md",
  "triggers": ["{trigger1}", "{trigger2}", "..."],
  "brief": "DO_NOT_USE_AS_CONTENT"
}
```

**IMPORTANT**: The `brief` field is intentionally set to `DO_NOT_USE_AS_CONTENT` to prevent the AI from using the index entry as a substitute for the full file. The index is for routing only.

---

## Sub-Skills vs Memory vs Summary

When deciding where to put extracted knowledge:

| Content Type | Where | Example |
|-------------|-------|---------|
| Complete methodology with steps | Sub-Skill file | "经济利润评估法：5步流程+公式+阈值" |
| Single principle or preference | Memory (MEMORY.md) | "用P/S代替Beta衡量风险更准确" |
| Historical fact or data point | knowledge.json | "1987-2006年ROIC最高分位年均超额2.3%" |
| Narrative understanding | summary.md | "第4章论证了盈利性作为选股因子的有效性" |
| Quick-reference thresholds | checklist.md | "ROIC>25%, FCF/Price>10%" |
