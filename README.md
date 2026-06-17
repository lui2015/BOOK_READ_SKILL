# 📖 Book Read Skill

> 把任何一本书变成精美的交互式 HTML 读书报告

## 功能特点

- 🎨 **精美 HTML 报告** — 自包含单文件，无需外部依赖，现代 UI 设计
- 🧠 **知识脑图** — SVG 渲染的交互式思维导图，一眼看透全书逻辑
- 🎴 **知识卡片** — SVG 公式图/结构图，可视化核心知识模型
- 🏆 **TOP3 精华论点** — 可展开卡片，含推理链、实践案例和行动指南
- 📝 **9 大交互 Tab** — 概览、核心论点、知识脑图、知识卡片、章节摘要、关键概念、实践清单、闪卡、评价推荐
- 🌓 **深色/浅色模式** — 自动检测系统偏好，支持手动切换
- 📱 **响应式设计** — 适配桌面端和移动端
- 💾 **本地持久化** — 实践清单进度保存到 localStorage

## 目录结构

```
book_read_skill/
├── SKILL.md                          # 技能主定义文件
├── README.md                         # 本文件
├── .gitignore
├── assets/                           # 静态资源
├── library/                          # 书籍知识库
│   ├── index.json                    # 书库索引
│   └── almanack-of-naval-ravikant/   # 示例：《纳瓦尔宝典》
│       ├── summary.md
│       └── knowledge.json
├── references/                       # 参考文档
│   ├── html_template.md              # HTML 模板与设计规范（核心）
│   ├── extraction_templates.md       # 知识提取模板
│   ├── domain_adapters.md            # 领域适配器
│   ├── flashcard_patterns.md         # 闪卡生成模式
│   └── sub_skill_template.md         # 子技能模板
└── scripts/
    └── parse_book.py                 # PDF/EPUB 文本提取脚本
```

## 使用方式

### 在 WorkBuddy 中使用

```
@skill:book_read_skill 《纳瓦尔宝典》
```

### 支持的输入

- 📄 PDF/EPUB 文件路径
- 📝 直接粘贴文本
- 📖 仅提供书名（降级模式，通过 Web 搜索补充内容）

## 设计规范

- **主色**：`#0052D9`（腾讯企业蓝）
- **辅助色**：`#36CFC9`（青绿）
- **字体**：系统字体栈（苹方/微软雅黑/Segoe UI）
- **布局**：最大宽度 1200px 居中，响应式栅格
- **卡片**：12px 圆角，微阴影，悬停动画
- **动画**：0.3s ease 过渡，IntersectionObserver 滚动触发

## 输出示例

生成《纳瓦尔宝典》读书报告的示例效果：

- 9 个交互式 Tab 页
- SVG 知识脑图（中心→分支→章节→关键概念）
- 5 张 SVG 公式知识卡片（轮播切换）
- TOP3 可展开精华论点
- 知识卡片式章节摘要（高亮关键词 + pill 标签）
- 闪卡翻转交互
- localStorage 持久化的实践清单

## License

MIT
