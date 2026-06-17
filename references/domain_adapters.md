# Domain Adapters

Domain-specific extraction rules that supplement the standard templates. After identifying the book's domain, apply the corresponding adapter's additional extraction dimensions.

## Domain Detection

Analyze the book's content to classify it into one of the following domains. Use these signals:

| Domain | Detection Signals |
|--------|------------------|
| `investment` | 股票、基金、交易、投资组合、风险、收益率、估值、市场、对冲 |
| `business` | 战略、管理、组织、领导力、竞争优势、商业模式、增长、营销 |
| `technology` | 代码、算法、架构、API、数据结构、系统设计、性能、编程 |
| `psychology` | 认知、行为、实验、偏误、神经科学、情绪、动机、潜意识 |
| `philosophy` | 论证、伦理、存在、认识论、形而上学、逻辑、真理、自由意志 |
| `self_help` | 习惯、目标、效率、自律、正念、成长、生产力、时间管理 |
| `history` | 事件、年代、人物、因果、文明、演变、战争、王朝 |
| `science` | 假说、实验、证据、模型、理论、数据、物理、化学、生物 |
| `economics` | GDP、通胀、货币政策、供需、博弈论、制度、市场失灵 |
| `literature` | 小说、叙事、人物、象征、主题、隐喻、文学批评 |
| `education` | 教学、学习理论、课程、认知发展、教育心理学 |
| `health` | 医学、营养、运动、疾病、健康管理、生理学、临床 |
| `sociology` | 社会结构、文化、阶层、制度、群体行为、社会变迁 |
| `design` | 用户体验、交互设计、产品设计、设计思维、美学、原型 |
| `law` | 法律条文、判例、法理学、合规、知识产权、合同 |
| `communication` | 演讲、写作、谈判、说服、非暴力沟通、媒体素养 |
| `parenting` | 儿童发展、亲子关系、教育方法、情感培养 |
| `biography` | 人物经历、成就、时代背景、决策过程、人格特质 |
| `general` | 无法明确归类时使用 |

If a book spans multiple domains (e.g., behavioral finance = psychology + investment), pick the PRIMARY domain and note secondary domains in the metadata.

---

## Adapter: Investment / Trading / Finance (`investment`)

### Additional Extraction Dimensions

1. **Strategy Rules**
   - Entry conditions (买入条件)
   - Exit conditions (卖出条件)
   - Position sizing rules (仓位管理)
   - Risk management rules (止损/止盈)

2. **Market Models**
   - Author's market view (有效市场/行为金融/技术分析...)
   - Applicable market conditions (牛市/熊市/震荡)
   - Time horizon (短线/中线/长线)

3. **Quantifiable Parameters**
   - Any specific numbers mentioned (PE阈值、回撤容忍度、仓位比例等)
   - Historical backtesting results cited by author

4. **Risk Warnings**
   - Author's stated limitations
   - Survivorship bias considerations
   - Market regime dependencies

### Sub-Skill Emphasis
Focus on: decision checklists, position sizing logic, risk assessment frameworks

---

## Adapter: Business / Management / Strategy (`business`)

### Additional Extraction Dimensions

1. **Frameworks & Models**
   - Named frameworks (e.g., Porter's Five Forces, Jobs-to-be-Done)
   - Decision matrices, process models

2. **Case Studies**
   | Company | Situation | Action | Result | Lesson |

3. **Organizational Principles**
   - Culture/values prescriptions, team structure, leadership behaviors

4. **Metrics & KPIs**
   - Recommended measurement systems, benchmarks

### Sub-Skill Emphasis
Focus on: decision frameworks as step-by-step procedures, analysis templates, strategic checklists

---

## Adapter: Technology / Programming (`technology`)

### Additional Extraction Dimensions

1. **Design Patterns & Architecture**
   - Named patterns with problem/solution structure
   - Architecture diagrams (reproduce as Mermaid)
   - Trade-off analysis

2. **Code Patterns**
   - Pattern name, problem, solution (pseudocode), when to use, anti-patterns

3. **System Design Principles**
   - Scalability, reliability, performance optimization strategies

4. **Technology Comparisons**
   | Technology | Strengths | Weaknesses | Best For |

### Sub-Skill Emphasis
Focus on: design decision guides, code review checklists, architecture evaluation frameworks

---

## Adapter: Psychology / Cognitive Science (`psychology`)

### Additional Extraction Dimensions

1. **Cognitive Biases & Heuristics**
   | Bias/Heuristic | Definition | Example | Mitigation |

2. **Key Experiments**
   | Experiment | Researchers | Finding | Replication Status |

3. **Behavioral Models**
   - Stimulus → Process → Response chains
   - Intervention strategies

4. **Practical Applications**
   - Nudge techniques, debiasing strategies, persuasion tactics

### Sub-Skill Emphasis
Focus on: bias detection checklists, decision debiasing procedures, behavioral intervention templates

---

## Adapter: Philosophy / Thought (`philosophy`)

### Additional Extraction Dimensions

1. **Argument Structure**
   - Premise 1 → Premise 2 → Conclusion (validity + soundness)

2. **Thought Experiments**
   - Setup, question, competing intuitions, author's resolution

3. **Intellectual Lineage**
   - Who the author builds on / argues against / where this fits in tradition

4. **Core Distinctions**
   - Key conceptual distinctions, terms defined differently from common usage

### Sub-Skill Emphasis
Focus on: argument evaluation frameworks, conceptual analysis templates, ethical reasoning procedures

---

## Adapter: Self-Help / Personal Growth (`self_help`)

### Additional Extraction Dimensions

1. **Habit/Practice Prescriptions**
   | Habit | Frequency | Duration | Expected Outcome | Evidence Quality |

2. **Transformation Model**
   - Before state → Intervention → After state, timeline expectations

3. **Daily/Weekly Routines**
   - Morning/evening routines, weekly review processes

4. **Progress Tracking**
   - Metrics, milestones, accountability structures

### Sub-Skill Emphasis
Focus on: daily practice checklists, progress tracking templates, obstacle-solution lookup tables

---

## Adapter: History (`history`)

### Additional Extraction Dimensions

1. **Timeline & Chronology**
   | Period | Key Events | Key Figures | Consequences |

2. **Causal Analysis**
   - What caused X? What were the consequences? Counterfactual: what if X hadn't happened?

3. **Pattern Recognition**
   - Recurring patterns across different eras/civilizations
   - Author's theory of historical change (cyclical/progressive/contingent)

4. **Primary Sources & Evidence**
   - What evidence does the author rely on? How reliable?
   - Competing historical interpretations

### Sub-Skill Emphasis
Focus on: historical pattern recognition frameworks, causal analysis templates, era comparison methods

---

## Adapter: Science / Natural Sciences (`science`)

### Additional Extraction Dimensions

1. **Core Theories & Laws**
   | Theory/Law | Statement | Evidence | Limitations | Applicable Scale |

2. **Experimental Method**
   - Hypothesis → Method → Results → Interpretation chain
   - Key experiments that changed the field

3. **Unresolved Questions**
   - Open problems, competing hypotheses, frontiers of research

4. **Practical Implications**
   - How this science affects daily life / technology / policy

### Sub-Skill Emphasis
Focus on: scientific reasoning frameworks, experiment design templates, evidence evaluation methods

---

## Adapter: Economics (`economics`)

### Additional Extraction Dimensions

1. **Models & Theories**
   | Model | Assumptions | Predictions | Empirical Support | Limitations |

2. **Policy Implications**
   - What does the author recommend? What trade-offs?

3. **Data & Evidence**
   - Key datasets, natural experiments, cross-country comparisons

4. **Schools of Thought**
   - Where does the author sit? (Keynesian/monetarist/Austrian/behavioral/institutional)
   - How does this differ from mainstream?

### Sub-Skill Emphasis
Focus on: economic analysis frameworks, policy evaluation templates, market mechanism models

---

## Adapter: Literature / Fiction (`literature`)

### Additional Extraction Dimensions

1. **Narrative Structure**
   - Plot arc (exposition → rising action → climax → resolution)
   - Narrative technique (POV, timeline, unreliable narrator)

2. **Character Analysis**
   | Character | Role | Motivation | Arc | Symbolic Function |

3. **Themes & Symbols**
   | Theme/Symbol | Manifestation | Interpretation |

4. **Literary Context**
   - Literary movement, influences, reception, cultural significance

5. **Philosophical/Intellectual Content** (for idea-rich fiction like Sophie's World)
   - Core ideas presented through the narrative
   - How fiction form serves the intellectual content

### Sub-Skill Emphasis
Focus on: literary analysis frameworks, thematic comparison methods. For idea-rich fiction, also extract the intellectual content as if it were a non-fiction book.

---

## Adapter: Education / Learning (`education`)

### Additional Extraction Dimensions

1. **Learning Theories**
   | Theory | Proponent | Core Claim | Evidence | Application |

2. **Pedagogical Methods**
   - Teaching techniques, assessment approaches, curriculum design principles

3. **Cognitive Development Stages**
   - Age-appropriate learning, scaffolding, zone of proximal development

4. **Practical Classroom Strategies**
   - Specific activities, discussion formats, feedback methods

### Sub-Skill Emphasis
Focus on: teaching method templates, lesson design frameworks, learning assessment checklists

---

## Adapter: Health / Medicine / Nutrition (`health`)

### Additional Extraction Dimensions

1. **Evidence Quality Assessment**
   | Claim | Evidence Type | Quality (RCT/observational/anecdotal) | Consensus Level |

2. **Protocols & Recommendations**
   - Dosage, frequency, duration, contraindications

3. **Mechanisms**
   - Biological pathways, physiological explanations

4. **Risk-Benefit Analysis**
   - Benefits vs side effects, individual variation factors

### Sub-Skill Emphasis
Focus on: health protocol checklists, evidence evaluation frameworks, risk assessment templates. Always note evidence quality — distinguish RCTs from anecdotes.

---

## Adapter: Sociology / Culture (`sociology`)

### Additional Extraction Dimensions

1. **Social Structures & Systems**
   - Institutions, power dynamics, class/gender/race analysis

2. **Research Methods**
   - Ethnography, surveys, statistical analysis, case studies

3. **Theoretical Frameworks**
   - Functionalism, conflict theory, symbolic interactionism, etc.

4. **Contemporary Relevance**
   - How findings apply to current social issues

### Sub-Skill Emphasis
Focus on: social analysis frameworks, institutional evaluation templates

---

## Adapter: Design / UX / Product (`design`)

### Additional Extraction Dimensions

1. **Design Principles**
   | Principle | Definition | Example | Anti-pattern |

2. **Process & Methods**
   - Design thinking stages, user research methods, prototyping approaches

3. **Evaluation Criteria**
   - Usability heuristics, accessibility standards, aesthetic principles

4. **Case Studies**
   | Product | Problem | Design Solution | Outcome |

### Sub-Skill Emphasis
Focus on: design evaluation checklists, UX research frameworks, design critique templates

---

## Adapter: Communication / Writing / Rhetoric (`communication`)

### Additional Extraction Dimensions

1. **Persuasion Techniques**
   | Technique | How It Works | Example | When to Use |

2. **Structure Templates**
   - Speech structures, essay frameworks, storytelling arcs

3. **Audience Analysis**
   - How to adapt message to different audiences

4. **Practice Exercises**
   - Drills, templates, feedback methods

### Sub-Skill Emphasis
Focus on: communication templates, persuasion checklists, writing frameworks

---

## Adapter: Biography / Memoir (`biography`)

### Additional Extraction Dimensions

1. **Life Timeline**
   | Period | Age | Key Events | Decisions | Outcomes |

2. **Decision Analysis**
   - Critical crossroads: what options existed, what was chosen, what resulted

3. **Character Traits & Mental Models**
   - Recurring patterns in the subject's thinking and behavior

4. **Lessons Extracted**
   - What can be learned from this person's life? What is context-dependent vs universal?

5. **Historical Context**
   - How the era shaped the person, how the person shaped the era

### Sub-Skill Emphasis
Focus on: decision-making frameworks derived from the subject's life, mental model catalogs, leadership principle extractions

---

## Adapter: Parenting / Child Development (`parenting`)

### Additional Extraction Dimensions

1. **Development Stages**
   | Age Range | Key Developments | Parenting Focus | Common Challenges |

2. **Parenting Strategies**
   | Strategy | When to Use | How to Implement | Evidence Quality |

3. **Communication Patterns**
   - Effective vs harmful communication examples

4. **Long-term Outcomes**
   - What research says about long-term effects of parenting approaches

### Sub-Skill Emphasis
Focus on: age-appropriate strategy checklists, communication templates, developmental milestone trackers

---

## Adapter: Law / Legal (`law`)

### Additional Extraction Dimensions

1. **Legal Principles & Doctrines**
   | Principle | Source | Application | Exceptions |

2. **Case Analysis**
   | Case | Facts | Legal Issue | Holding | Significance |

3. **Regulatory Framework**
   - Relevant statutes, regulations, enforcement mechanisms

4. **Practical Compliance**
   - Checklists, risk areas, best practices

### Sub-Skill Emphasis
Focus on: compliance checklists, legal risk assessment frameworks, contract review templates

---

## Adapter: General (Fallback)

When no specific domain matches, use only the standard extraction templates without additional dimensions. Note in the metadata that no domain adapter was applied.
