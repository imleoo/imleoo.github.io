---
layout: post
title: "Anthropic 自曝：95% 数据分析交给 Claude 后，他们真正学到的不是“让 AI 写 SQL”"
date: 2026-06-05
article_id: 2683094
source: https://cloud.tencent.com/developer/article/2683094
---
# Anthropic 自曝：95% 数据分析交给 Claude 后，他们真正学到的不是“让 AI 写 SQL”

如果你在公司里做过数据分析，应该很熟悉这种场景：

业务同学在 Slack 里问一句：

> “上周活跃用户是多少？”

听起来很简单。

但数据同学脑子里马上开始冒出一串问题：

- 你说的“活跃”是哪种活跃？
- 是登录算活跃，还是完成一次关键动作算活跃？
- 要不要排除欺诈用户？
- 看自然周，还是过去 7 天？
- 用哪个表？哪个字段？哪个 dashboard？
- 这个口径是不是上个月刚改过？

这就是数据分析最痛苦的地方：**业务问题通常很短，但正确答案背后的上下文非常长。**

最近 Anthropic 发了一篇很值得读的文章：

> How Anthropic enables self-service data analytics with Claude

它讲的是 Anthropic 内部如何用 Claude 做自助式数据分析。

最抓人的一个数字是：

> 在 Anthropic，95% 的业务分析查询已经通过 Claude 自动化完成，整体准确率约 95%。

听起来像是“AI 分析师要来了”。

但这篇文章真正有价值的地方，不是炫耀 Claude 会写 SQL，而是 Anthropic 很诚实地说了一件事：

> 数据分析 Agent 的核心难点，从来不是代码生成，而是上下文、口径和验证。

换句话说，AI 数据分析不是“把 Claude 接到数仓上，让它自己跑”。

那样只会制造一种更危险的东西：**看起来很精确的错误答案。**

---

## 一、数据不是软件：AI 写 SQL 不等于 AI 懂数据

很多人会自然地把“AI 写代码”和“AI 写 SQL”放在一起看。

但 Anthropic 的观点很明确：

> Data is not software.

软件开发里，问题通常是开放的。

你让模型写一个函数、修一个 bug、搭一个组件，只要结果能跑、测试能过、逻辑清楚，很多时候就算成功。

代码世界里天然有一些护栏：

- 测试
- 类型
- 编译器
- lint
- 文档
- 运行结果

模型可以犯错，但很多错误会被系统发现。

数据分析不一样。

很多业务问题只有一个正确答案，而且通常只有一个正确来源。最糟糕的是：

> 错误 SQL 也能跑出一个看起来很合理的数字。

比如同样是“活跃用户”：

- A 表里的 active_user 是登录过的人
- B 表里的 active_user 是完成过核心行为的人
- C dashboard 里排除了 fraud user
- D 报表里按组织维度去重

Claude 可以非常熟练地写出 SQL。

但如果它选错了表、错了字段、错了过滤条件，最后出来的数字越精确，反而越危险。

这就是 Anthropic 文章里的第一性原理：

> 分析准确率不是代码生成问题，而是“问题如何映射到正确数据实体”的问题。

SQL 只是最后一步。

真正难的是：

```javascript
用户的问题→正确业务概念→正确指标定义→正确表/字段/过滤条件→正确查询
```

只要前面错了，SQL 写得再漂亮也没用。

---

## 二、AI 数据分析最常见的三个失败模式

Anthropic 总结了三个最主要的错误来源。

这三个点非常实用，几乎所有公司做数据 Agent 都会撞上。

### 1. 概念和数据实体对不上

这是最大的问题。

用户问的是一个自然语言概念：

> “收入” “活跃用户” “转化率” “留存” “增长”

但数仓里可能有几十个、几百个看起来都相关的字段和表。

模型的问题不是不会搜，而是搜到一堆都像答案的东西。

比如“收入”：

- gross revenue
- net revenue
- recognized revenue
- subscription revenue
- booked revenue
- refunded revenue
- product-specific revenue

每一个都“有道理”。

但业务真正要的是哪一个？

如果公司内部没有一个明确的 canonical metric，Agent 就会自己猜。

而 AI 最可怕的地方是：**它猜的时候很自信。**

### 2. 数据和文档会过期

业务定义会变。

表结构会变。

dashboard 会变。

某个字段今天还是标准口径，下个月可能就废弃了。

如果 Agent 读的是旧文档、旧 SQL、旧 dashboard，它就会产出一种很隐蔽的错误：

> 不是完全错，而是“细节上已经过期”。

这种错最难发现。

因为答案看起来合理，SQL 也能跑，甚至和旧报表还能对上。

但它已经不是公司现在认可的口径了。

### 3. 正确信息存在，但 Agent 找不到

很多团队以为，只要把所有 SQL、dashboard、notebook、文档都丢给模型，它就会自己找到答案。

Anthropic 做了一个很有意思的实验：

他们给 Agent 直接访问整个 dashboard、transform、analyst notebook SQL 语料库的能力，里面有成千上万份历史查询。

结果呢？

> 准确率提升不到 1 个百分点。

更关键的是，他们检查后发现：

> 在模型答错的问题里，大约 80% 的正确答案其实就在语料库中。

也就是说，问题不是“信息不存在”。

问题是：

> 信息太散，结构太差，Agent 不知道该相信谁。

这对很多团队是一个提醒：

别幻想“把所有文档塞进 RAG”就能解决数据分析。

RAG 不是魔法。

没有结构化的知识，检索越多，噪音越大。

---

## 三、Anthropic 的答案：不是一个 Agent，而是一套 Agentic Data Stack

Anthropic 内部不是简单地“Claude + 数仓”。

他们搭的是一套 Agentic Analytics Stack。

这套系统的核心目标只有三个：

```javascript
减少歧义
防止过期
避免找不到正确答案
```

它大致分成几层：

- Data foundations：数据基础设施
- Sources of truth：可信来源
- Skills：过程知识
- Validation：验证体系

这几个词听起来有点工程化，但翻译成人话就是：

> 先把正确答案定义清楚，再告诉 Claude 去哪里找，最后验证它有没有找对。

---

## 四、第一层：Canonical Dataset，比“大宽表”更重要

很多公司做自助分析，第一反应是做大宽表。

把字段铺开，让业务同学更容易查。

但 Anthropic 认为，这往往会带来另一个问题：

> 表更多了，口径也更多了。

一个指标出现多个版本，每个团队都有自己的 dashboard，每个 dashboard 都有一点点不同。

最后不是 self-service analytics，而是 self-service confusion。

Anthropic 的建议是：

> 少而精的 canonical datasets，比一堆看似方便的大宽表更重要。

也就是为关键业务概念建立明确的、受治理的、唯一可信的数据集。

比如收入，就应该让 Agent 能找到一个默认答案：

```javascript
Revenue→这个 canonical model →这个 metric definition →这个 owner
```

而不是让 Claude 在 40 个可能相关的数据集里猜。

这里有一个很重要的产品思路：

> 给 AI 用的数据模型，应该比给人用的数据模型更严格。

因为人类数据分析师看到奇怪字段时会怀疑、会问、会找同事确认。

Agent 不一定。

所以你要把选择空间提前收窄。

---

## 五、第二层：Semantic Layer 要优先于原始 SQL

Anthropic 很强调 semantic layer。

如果一个问题能映射到已经定义好的 metric 或 dimension，Agent 应该优先调用 semantic layer，而不是自己手写 SQL。

原因很简单：

> semantic layer 是公司指标口径的编译结果。

它包含了：

- 指标定义
- 维度定义
- join 逻辑
- grain
- 标准过滤条件
- 分群规则

如果 Agent 直接调用它，得到的数字就和 BI 工具、dashboard、公司标准报表一致。

这比让 Claude 每次重新发明一段 SQL 稳定得多。

但 Anthropic 也提到一个失败实验：

他们试过让 LLM 根据原始表和查询日志自动生成 metric definitions。

结果是负收益。

原因也很有意思：

> 模型生成了很多看起来合理的指标定义，但这些定义把原本的歧义也一起固化进去了。

所以他们的结论是：

> 可以让 Claude 帮你写文档、草拟指标说明，但指标定义必须由人类 owner 负责。

这是 AI 数据系统里一个很重要的边界：

```javascript
AI 可以降低维护成本
但不能替你承担治理责任
```

---

## 六、第三层：Skills 才是真正的“分析师经验”

这篇文章里最值得 OpenClaw / Claude Code 用户关注的，是 Anthropic 对 Skills 的使用。

他们说，在 Claude Code 里，Skill 是一个按需加载的 Markdown 文件夹。

但在数据分析场景里，它不是简单的“提示词”。

它更像是：

> 一个资深数据分析师写给 Agent 的操作手册。

它告诉 Claude：

- 这个领域的问题应该先查 semantic layer
- 如果 semantic layer 没覆盖，再看哪些 reference docs
- 哪些表是 canonical
- 哪些字段容易误用
- 哪些过滤条件必须加
- 哪些问题要先澄清
- 结果应该如何验证
- 什么时候不能回答，要升级给 owner

Anthropic 给了一个很夸张但重要的数字：

> 没有 Skills 时，Claude 在他们 eval 上的准确率不超过 21%。加入 Skills 后，整体稳定超过 95%，某些领域接近 99%。

这说明什么？

说明 Agent 的能力不是只来自模型本身。

真正的生产级 Agent，靠的是：

```javascript
模型能力+结构化上下文+程序化流程+持续维护
```

Skill 的本质，不是“写得更详细的 prompt”。

它是把组织里的隐性知识变成可调用的显性知识。

以前这些知识在资深分析师脑子里：

- “这个表别用，去年废弃了”
- “算增长要排除这类账户”
- “这个 dashboard 的口径和财务口径不一样”
- “实验 lift 不能用 raw event count”

现在要写进 Skill。

这就是 Agent 时代的数据治理。

---

## 七、Skill 也会腐烂，所以维护机制比初版更重要

Anthropic 提到一个非常现实的现象：

他们上线时离线准确率大约 95%。

但如果不维护，一个月后会漂到 65%。

为什么？

因为数据模型每天都在变。

业务定义每天都在变。

如果 Skill 文档不跟着变，它很快就会从“护栏”变成“误导”。

Anthropic 的做法是：

> 把 Skill Markdown 和数据模型放在同一个 repo 里。

如果一个 PR 改了 reporting model，却没有更新相关 Skill 文件，code review hook 会提醒。

他们说现在大约 90% 的数据模型 PR 都会同时包含 Skill 更新。

这点非常关键。

很多公司做 AI Agent 会失败，不是因为第一版不够聪明，而是因为没有维护机制。

初版 demo 很漂亮。

三个月后文档过期、指标改名、表废弃，Agent 开始稳定地产出错误答案。

所以真正的问题不是：

> 我能不能做一个数据分析 Agent？

而是：

> 我能不能让这个 Agent 的知识随着业务一起更新？

---

## 八、验证体系：别相信一次看起来对的回答

Anthropic 对 validation 的投入也很重。

他们分了 offline eval 和 online validation。

### Offline eval：上线前知道有没有明显漏洞

离线评测是 question / answer pairs。

有点像机器学习模型的测试集。

Anthropic 会用两类 eval：

- dashboard-based eval：基于常见 stakeholder 问题生成，再由人验证
- long tail eval：给 Claude 业务上下文，让它生成长尾问题，再纳入测试

他们还会把 stakeholder 在真实对话中纠正 Agent 的内容收集起来，变成新的 eval。

这就是一个闭环：

```javascript
线上纠错→变成离线测试→修Skill/文档→再上线
```

### Online validation：线上回答必须带出处

Anthropic 还提到几个线上验证机制。

其中我觉得最重要的是 provenance footer。

也就是每个回答最后带上：

- 来源层级：semantic layer / curated reference / raw table
- 数据新鲜度
- 模型 owner
- 是否经过 review
- confidence tier

这不会让答案自动正确。

但它会告诉用户：

> 这个答案应该有多可信。

比如：

```javascript
Source: raw table
Freshness: unknown
Owner: unknown
```

这就是一个明显信号：别直接拿去给老板汇报。

而如果是：

```javascript
Source: semantic layer
Freshness:2026-06-03
Owner:GrowthAnalytics
Reviewed: yes
```

信任级别就完全不一样。

---

## 九、最难解决的是“沉默的错误”

这篇文章最后有一句很清醒的话。

即使用了这么多机制，Anthropic 也承认有一种失败模式还没有完全解决：

> silent failure。

也就是答案是错的，但看起来很合理，而且没人质疑。

这才是 AI 数据分析最危险的部分。

因为传统错误往往会暴露：

- SQL 跑不通
- 字段不存在
- 数字离谱
- 用户指出“你用错表了”

但沉默的错误不会。

它会悄悄进入周报、dashboard、决策会议。

最后变成一个看起来很科学的错误决策。

Anthropic 现在的缓解方式包括：

- provenance footer
- leadership-bound 内容需要人工 sign-off
- 每个 domain 的 top KPI 每天和 blessed dashboard 做 sanity check

但他们也说：

> 还没有 robust solution。

这很真实。

AI 数据分析不是一个“全自动替代分析师”的问题。

它更像是把分析师从重复劳动里解放出来，同时用工程体系降低错误概率。

---

## 十、如果从零开始，应该怎么做？

Anthropic 给的建议其实很克制。

如果你从零开始，不需要一下子搭完整体系。

先做三件事就够了：

### 1. 建几个 canonical datasets

不要让 Agent 在几十个相似表里猜。

先把公司最核心的几个业务指标收敛成明确口径。

比如：

- 用户
- 收入
- 留存
- 转化
- 活跃
- 订阅
- 退款

每个指标都要有 owner、定义、grain、过滤条件和使用边界。

### 2. 做几十个 offline eval

别靠感觉判断 Agent 准不准。

用真实业务问题做测试集。

重点不是数量越多越好，而是覆盖那些最容易错、最常被问、最重要的指标。

### 3. 写一个 thin knowledge skill

先不要写一个百科全书式文档。

写一个薄的 router：

```javascript
如果问增长，看这些 reference docs
如果问收入，优先 semantic layer
如果问实验，不要用 raw event counts
如果问用户数，必须先确认活跃定义
```

这就能捕获大部分收益。

之后再逐步加：

- adversarial review
- correction harvesting
- provenance footer
- PR hook
- semantic layer enforcement
- cross-surface sync

---

## 最后：AI 数据分析的终点，不是“人人都会查数”

很多人理解 self-service analytics，会以为目标是：

> 让每个业务同学都能自己查数据。

但 Anthropic 这篇文章给了一个更准确的方向：

> 不是让每个人都变成数据分析师，而是让组织里的数据知识可以被 Agent 正确调用。

这件事的关键不是 SQL。

SQL 是表层。

真正重要的是：

- 哪个指标是标准口径
- 哪个表是可信来源
- 哪些字段不能用
- 哪些问题必须澄清
- 哪些答案需要人工确认
- 错误发生后如何回写到系统里

也就是说，AI 数据分析的竞争力，不在于“模型多会写查询”。

而在于公司有没有能力把自己的数据知识工程化。

Anthropic 内部 95% 的业务分析查询自动化，真正说明的不是 Claude 可以替代数据团队。

它说明的是：

> 当数据基础设施、语义层、Skill、评测和验证机制都搭起来之后，AI 才能稳定承担重复性分析工作。

这也是所有企业做 AI Agent 最容易忽略的一点：

**Agent 不是接上工具就能干活。**

它需要一套能让它“找对答案、知道边界、持续纠错”的系统。

如果没有这套系统，AI 数据分析只是更快地产生幻觉。

如果有了这套系统，它才有机会变成真正的组织生产力。

---

原文：Anthropic《How Anthropic enables self-service data analytics with Claude》

核心数字：Anthropic 内部约 95% 的业务分析查询通过 Claude 自动化完成，整体准确率约 95%。

一句话 takeaway：

> 数据分析 Agent 的关键不是让 AI 写 SQL，而是让 AI 永远先找到那个“被治理过的正确答案”。
