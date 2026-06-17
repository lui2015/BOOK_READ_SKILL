---
name: book_read_skill
agent_created: true
description: "Book reading skill that generates beautiful HTML report. Use when user wants to read/digest a book and produce a visually stunning HTML file. Triggers: 读书、读这本书、生成读书报告、精美读书笔记、book read、book html、读书HTML、书籍精读、book reading report、可视化读书笔记、生成精美HTML读书报告、阅读报告、reading report HTML"
---

# 📖 Book Read Skill — 把书变成精美的 HTML 读书报告

## Purpose

Transform any book into a **visually stunning, self-contained HTML reading report**. All knowledge is extracted, structured, and rendered as a beautiful interactive HTML file with modern UI design.

## When to Use

- User provides a book (PDF/EPUB/text/name) and wants a beautiful reading report
- User asks for a visual/HTML book summary or reading note
- User says "生成精美读书报告", "读书HTML", "读这本书生成报告" etc.

## Skill Base Directory

All paths in this skill are relative to: `~/.workbuddy/skills/book_read_skill/`

The book library is stored at: `~/.workbuddy/skills/book_read_skill/library/`

---

## Anti-Hallucination Rules (CRITICAL — READ FIRST)

1. **NEVER answer questions about a book based on index entries alone.** ALWAYS read the full content file before responding.
2. **NEVER paraphrase or reconstruct content from file names/descriptions.** If the content file cannot be loaded, respond: "该内容文件未找到" and STOP.
3. **NEVER mix content from different books** unless explicitly asked for cross-book analysis.
4. **When referencing the book, QUOTE specific data, thresholds, and steps from the loaded content.** Never invent values.
5. **Every file in the library must be self-contained.** Loading a single file must provide enough context to execute without requiring other files.

---

## Workflows

### Workflow 1: Book Read & HTML Report Generation (Main Flow)

Triggered when user provides a book and wants a reading report.

#### Phase 1: Input Processing

**If PDF/EPUB file provided:**
1. Run `scripts/parse_book.py` to extract text and chapter structure
2. The script outputs JSON with `{ "title", "chapters": [{"number", "title", "content"}] }`

**If text pasted:**
1. Accept the text directly
2. Attempt to identify chapter boundaries from headings/numbering

**If only book name provided (degraded mode):**
1. Use web search to gather comprehensive information about the book
2. Warn user: "仅通过书名搜索，内容覆盖度可能不如直接提供原文"
3. Proceed with available information

#### Phase 2: Core Extraction

Read `references/extraction_templates.md` for the mandatory six-part output structure.
Read `references/domain_adapters.md` to identify the book's domain and apply domain-specific extraction rules.

Extract the following six parts:
1. **一句话总结** — 全书核心主张
2. **核心论点** — 3-5个论点（主张/论据/推理链/评价），评分用十分制
3. **章节框架** — 思维导图数据（JSON结构，供HTML渲染）
4. **章节摘要** — 每章含叙事性总结 + 标签展开
5. **关键概念索引** — 每个概念3-5句完整定义
6. **评价及关联推荐** — 十分制评分 + 适合人群 + 不足 + 推荐书目

#### Phase 3: Deep Processing (run immediately, DO NOT pause)

**3a. Practice Checklist**
- Extract all actionable advice from the book
- Organize into categorized, prioritized checklist

**3b. Flashcard Generation**
- Read `references/flashcard_patterns.md` for card generation patterns
- Generate cards covering: key concepts, core arguments, frameworks, vocabulary

**3c. Classic Stories Extraction**
- Read `references/extraction_templates.md` (Template 8) for the story extraction format
- Scan the book for 5-8 representative stories, anecdotes, parables, or case studies
- For each story, extract: title, source chapter, narrative summary (100-200 words), author's viewpoint interpretation (tied to core arguments), reader insight (actionable takeaway)
- Prioritize stories that best illustrate the book's core thesis

**3d. Book Review**
- Generate structured review: overview, strengths, weaknesses, audience fit, key takeaways

#### Phase 4: HTML Report Generation (CORE OUTPUT)

Read `references/html_template.md` for the complete HTML template specification.

Generate a **single, self-contained HTML file** with:
- Embedded CSS (no external dependencies)
- Embedded JavaScript for interactivity
- Modern, beautiful UI design

The HTML report MUST include ALL of the following sections rendered as interactive tabs:

**Tab 1: 概览** (Overview)
- Hero section with book cover placeholder, title, author, domain badge
- One-sentence summary in a highlighted card
- Overall rating with visual star display
- TOP3 精华论点：3 张可展开卡片，每张含核心主张/推理链/实践案例/行动指南

**Tab 2: 核心论点** (Core Arguments)
- Card-based layout for each argument
- Each card shows: claim, evidence list, reasoning chain, evaluation score
- Visual score bar for each argument's persuasion rating

**Tab 3: 知识脑图** (Knowledge Mind Map)
- SVG 交互式知识脑图，展示书籍完整逻辑结构
- 中心节点→一级分支→二级章节→三级关键概念
- 颜色编码区分不同部分，跨域关联用橙色虚线
- 底部核心洞察横幅

**Tab 4: 知识卡片** (Knowledge Cards) ★
- 多张 SVG 公式图/结构图呈现书中核心知识模型
- 左右箭头+底部圆点导航切换（支持键盘方向键）
- 参考公式树形图风格：米黄背景、彩色关键词、箭头指向子公式

**Tab 5: 经典故事** (Classic Stories) ★★
- 提取书中 5-8 个最具代表性的小故事、案例或寓言
- 每个故事含：故事标题、章节来源徽章、故事梗概（叙事性 100-200字）、折叠式"作者观点解读"（结合书中核心论点展开）、读者启示（可操作领悟）
- 故事卡片左侧有彩色竖线标签区分不同故事类型（寓言/案例/亲身经历/历史典故）
- 顶部提供排序切换：按"章节顺序"或"论点相关度"排列
- 移动端：单列全宽卡片；桌面端：双列卡片布局

**Tab 6: 章节摘要** (Chapter Summaries)
- 知识卡片式展示（非手风琴）
- 每章含颜色高亮关键词、pill 标签、渐变引用块
- 叙事性总结 + 标签展开

**Tab 7: 关键概念** (Key Concepts)
- Searchable concept index
- Card grid layout
- Click to expand full definition

**Tab 8: 实践清单** (Action Checklist)
- Categorized actionable items with priority indicators
- Interactive checkboxes (localStorage persistence)

**Tab 9: 闪卡** (Flashcards)
- Flip-card interaction
- Progress tracking
- Spaced repetition indicator

**Tab 10: 评价推荐** (Review & Recommendations)
- Radar chart for multi-dimensional ratings
- Audience fit analysis
- Related book recommendations

**HTML Design Requirements:**
- **Color scheme**: Primary `#0052D9` (腾讯企业蓝), accent `#36CFC9`, gradient backgrounds
- **Typography**: System font stack, proper hierarchy with `font-weight` variations
- **Layout**: Max-width 1200px centered, responsive grid
- **Cards**: Rounded corners (12px), subtle shadows, hover animations (仅桌面端)
- **Tabs**: Pill-style tab navigation with active indicator
- **Animations**: Smooth transitions (0.3s ease), scroll-triggered reveals
- **Dark/Light mode**: Auto-detect system preference, toggle switch
- **Print-friendly**: Proper `@media print` styles
- **Mobile-first responsive** (⚠️ 关键要求，必须严格遵守):
  - 移动优先：所有 CSS 从小屏写起，768px/1024px 逐步增强
  - Tab 导航：横向可滚动，隐藏滚动条，点击自动居中，最小触控区 44px
  - 知识脑图：横向滚动 + 滚动提示文案（移动端显示）
  - 知识卡片：全宽展示，触控友好导航箭头 44px
  - 经典故事：单列全宽卡片，768px 起双列
  - 章节摘要：单列卡片，768px 起双列
  - 概念网格：单列→双列→三列
  - 闪卡：最小高度 240px，触控友好按钮 44px
  - 实践清单：放大 checkbox 至 22px，行高 48px
  - 全局防溢出：`overflow-wrap: break-word`、`max-width: 100vw`、SVG/图片 `max-width: 100%`
  - iOS 安全区域：`env(safe-area-inset-*)` 刘海屏适配
  - 触控设备：去掉 hover 上浮效果，消除 300ms 点击延迟
  - 字号降级：480px 以下 h1=1.5rem，body=15px
- **Accessibility**: Proper ARIA labels, keyboard navigation, focus styles

**Output file:** `{workspace}/{book-slug}-reading-report.html`

Also save structured data:
- `library/{book-slug}/knowledge.json` — Structured knowledge base
- `library/{book-slug}/summary.md` — Markdown fallback (六部分标准)

#### Phase 5: Registration & Completion

1. Update `library/index.json` with the new book entry
2. Present the HTML file to the user via `present_files`
3. Show completion summary with:
   - 产出文件路径
   - 闪卡复习引导
   - 可蒸馏子Skill候选菜单（如需）

---

### Workflow 2: Book Chat

Triggered when user says "聊聊某本书", "关于某书中的Y概念".

1. Look up the book in `library/index.json`
2. Read the book's `summary.md` or `knowledge.json`
3. Answer questions grounded in the loaded content
4. If book not found, suggest reading it first

---

### Workflow 3: Library Management

Triggered when user says "我的书库", "书单", "library".

1. Read `library/index.json`
2. Display formatted book catalog
3. Support: browse, search, re-read, delete

---

### Workflow 4: Sub-Skill Invocation

Triggered when user says something matching a sub-skill's triggers.

1. Read `library/index.json` to find the matching sub-skill entry
2. Read the full sub-skill file
3. Execute the methodology, quoting specific values from the file
4. If file not found, say "该子Skill文件未找到" and STOP

---

## Domain Detection

Automatically detect the book's domain from content analysis. See `references/domain_adapters.md` for supported domains:
investment, business, technology, psychology, philosophy, self_help, history, science, economics, literature, education, health, sociology, design, law, communication, biography, parenting, general

---

## Error Handling

- **PDF parsing fails**: Suggest EPUB or paste text directly
- **Book too large**: Process chapter by chapter, then synthesize
- **Book name search yields thin results**: Warn about coverage limitations
- **Book already in library**: Ask whether to re-read (overwrite) or skip
- **Sub-skill file not found**: Say "该子Skill文件未找到" and STOP

---

## File Reference Quick Index

| File | Purpose | When to Read |
|------|---------|-------------|
| `references/extraction_templates.md` | Core extraction templates (六部分标准) | Workflow 1 Phase 2 |
| `references/html_template.md` | HTML report template & design spec | Workflow 1 Phase 4 |
| `references/domain_adapters.md` | Domain-specific extraction rules | Workflow 1 Phase 2 |
| `references/flashcard_patterns.md` | Flashcard generation patterns | Workflow 1 Phase 3b |
| `references/sub_skill_template.md` | Sub-skill generation template | Sub-skill creation |
| `scripts/parse_book.py` | PDF/EPUB text extraction | Workflow 1 Phase 1 |
