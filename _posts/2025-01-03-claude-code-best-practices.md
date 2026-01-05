---
layout: post
title: "Claude Code 最佳实践：来自创始人的使用心得"
date: 2025-01-03 12:00:00 +0800
categories: [开发工具, AI编程]
tags: [Claude Code, AI编程, 最佳实践, 工作流优化]
description: "Claude Code 创始人 Boris Cherny 分享了他如何高效使用 Claude Code 的13个最佳实践技巧"
---

## 前言

最近，Claude Code 的创始人 Boris Cherny (@bcherny) 在 Twitter 上分享了他使用 Claude Code 的工作流程和最佳实践。这些实践来自 Claude Code 的核心开发者，具有很高的参考价值。本文将基于他的分享，整理和总结出这些最佳实践，帮助大家更高效地使用 Claude Code。

Boris 强调："没有一种正确使用 Claude Code 的方式。我们有意将其构建成可以让每个人以自己的方式使用、定制和改造的工具。甚至 Claude Code 团队中的每个人使用方式都不同。"

## 核心实践

### 1. 并行多任务处理

**实践内容**：
- 同时运行 **5 个本地 Claude 终端会话**
- 在终端标签页编号 1-5，使用系统通知了解何时需要输入
- 同时在 **claude.ai/code** 运行 5-10 个 Web 会话
- 在本地和 Web 会话之间切换（使用 `&` 手动移交）
- 从手机（Claude iOS 应用）启动会话，稍后查看

**价值**：
充分利用并行处理能力，最大化生产力。不同会话可以处理不同的任务，互不干扰。

### 2. 始终使用最强模型

**实践内容**：
- 使用 **Opus 4.5 with thinking** 处理所有任务
- 虽然 Opus 更大、更慢，但因为它需要的引导更少、工具使用更好，最终反而更快

**价值**：
"这是我用过最好的编码模型。" —— 投资更好的模型可以节省大量引导和迭代的时间。

### 3. 团队知识库 - CLAUDE.md

**实践内容**：
- 团队共享一个 `CLAUDE.md` 文件
- 文件纳入 git 版本控制
- 每周多次更新
- 每当发现 Claude 做错什么，就添加到 `CLAUDE.md`
- 每个团队维护自己的 `CLAUDE.md`

**价值**：
持续积累团队知识，让 Claude 越用越聪明。这是"复合工程"（Compounding Engineering）的实践。

**示例内容**：
```markdown
# CLAUDE.md

## 项目规范
- 使用 TypeScript strict 模式
- 所有函数必须有类型注解
- 遵循 ESLint 规则

## 常见错误
- 不要在 useEffect 中直接使用 async
- API 调用必须包含错误处理
```

### 4. 代码审查集成

**实践内容**：
- 在 PR 审查中标记 `@.claude` 让 Claude 添加内容到 `CLAUDE.md`
- 使用 Claude Code GitHub Action：`/install-github-action`

**价值**：
自动化知识积累，将代码审查中的学习固化为团队资产。

### 5. 计划优先模式

**实践内容**：
- 大多数会话从 **Plan 模式**开始（按 `Shift+Tab` 两次）
- 如果目标是写 PR，先和 Claude 来回讨论计划
- 计划满意后，切换到**自动接受编辑模式**
- Claude 通常可以一次性完成

**价值**：
"好的计划非常重要！" - 充分的规划可以大幅减少返工。

**工作流程**：
```
用户需求 → Plan 模式（讨论计划）
         ↓
    确认计划
         ↓
Auto-accept 模式 → 一键完成实现
```

### 6. Slash Commands 自动化

**实践内容**：
- 为每天重复多次的"内循环"工作流创建 slash commands
- 命令纳入 git 管理，存放在 `.claude/commands/`
- 使用 inline bash 预计算信息（如 git status），避免反复交互

**价值**：
避免重复提示词，提高效率。Claude 也可以使用这些工作流。

**示例**：
```bash
# .claude/commands/commit-push-pr.md
Commit current changes, push to remote, and create PR

Uses inline bash to pre-compute:
- git status
- current branch
- changed files summary

bash: |
  git status --short
  git branch --show-current
```

### 7. Subagents 常规任务

**实践内容**：
- 创建 subagents 处理常见任务
- 示例：
  - `code-simplifier`：简化 Claude 完成的代码
  - `verify-app`：端到端测试 Claude Code

**价值**：
自动化大多数 PR 的常见工作流。

### 8. PostToolUse Hook - 代码格式化

**实践内容**：
- 使用 PostToolUse hook 格式化 Claude 的代码
- Claude 通常生成格式良好的代码
- Hook 处理最后 10%，避免 CI 中的格式错误

**价值**：
确保代码风格一致性，减少 CI 失败。

### 9. 权限管理策略

**实践内容**：
- **不使用** `--dangerously-skip-permissions`
- 使用 `/permissions` 预先允许已知安全的 bash 命令
- 大部分权限配置纳入 `.claude/settings.json` 并与团队共享

**价值**：
在安全性和便利性之间取得平衡。

### 10. MCP 工具集成

**实践内容**：
- 让 Claude 使用各种工具：
  - **Slack MCP**：搜索和发布消息
  - **BigQuery**：运行分析查询（使用 bq CLI）
  - **Sentry**：获取错误日志
- MCP 配置纳入 `.mcp.json` 并与团队共享

**价值**：
扩展 Claude 能力，让它成为真正的全能助手。

**示例配置**：
```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"]
    }
  }
}
```

### 11. 长时间任务策略

**实践内容**：
对于长时间运行的任务，使用以下方法之一：
- **(a)** 提示 Claude 完成后用 background agent 验证
- **(b)** 使用 **agent Stop hook** 更确定性地验证
- **(c)** 使用 **ralph-wiggum plugin**
- 在沙箱中使用 `--permission-mode=dontAsk` 或 `--dangerously-skip-permissions`，避免权限提示阻塞

**价值**：
让 Claude 能够自主工作，不需要持续人工干预。

### 12. 验证反馈循环（最重要！）

**实践内容**：
- **最重要的是给 Claude 一种验证其工作的方法**
- 如果有反馈循环，最终结果质量可以提高 2-3 倍
- Claude 使用 Chrome 扩展测试每个改动
- 验证方式因领域而异：
  - 运行 bash 命令
  - 运行测试套件
  - 在浏览器或手机模拟器中测试应用

**价值**：
"确保投入精力让这个验证机制坚如磐石。" —— 这是获得高质量结果的关键。

**示例验证流程**：
```markdown
# 测试验证

## 后端 API
1. 运行单元测试：`npm test`
2. 检查类型检查：`npm run type-check`
3. 运行集成测试：`npm run test:integration`

## 前端 UI
1. 启动开发服务器：`npm run dev`
2. 打开浏览器访问 http://localhost:3000
3. 测试用户流程：登录 → 操作 → 登出
4. 检查控制台错误
5. 验证响应式设计
```

## 个人化定制建议

Boris 的配置可能"出奇地简单"（vanilla），因为 Claude Code 开箱即用非常好用。但每个人的工作方式不同：

### 初学者建议
1. **从简单开始**：不要过度配置，先熟悉基本功能
2. **建立 CLAUDE.md**：这是最重要的长期投资
3. **学习 Plan 模式**：好的计划是成功的一半

### 进阶用户建议
1. **创建 Slash Commands**：识别重复性任务并自动化
2. **配置 MCP 工具**：扩展 Claude 的能力边界
3. **设置验证流程**：让 Claude 能够自检和改进

### 团队协作建议
1. **共享 CLAUDE.md**：建立团队知识库
2. **标准化配置**：`.claude/settings.json` 纳入版本控制
3. **GitHub 集成**：使用 Action 自动化代码审查

## 工具配置示例

### 1. 终端配置（iTerm2）
```
启用系统通知：
Preferences > Profiles > Advanced >
Semantic History > "Run silently..."
```

### 2. Slash Commands 结构
```
.claude/
├── commands/
│   ├── commit.md
│   ├── test.md
│   ├── deploy.md
│   └── review.md
└── settings.json
```

### 3. MCP 配置
```json
{
  "mcpServers": {
    "slack": {...},
    "filesystem": {...},
    "brave-search": {...}
  }
}
```

## 总结

Boris Cherny 的分享揭示了一个核心原则：**没有唯一正确的方式，但有一些通用的高效实践**。

### 关键要点回顾

1. **并行工作**：充分利用多会话能力
2. **投资最佳模型**：Opus 4.5 worth it
3. **知识积累**：CLAUDE.md 是最重要的资产
4. **计划优先**：Plan 模式减少返工
5. **自动化重复任务**：Slash commands 和 subagents
6. **工具集成**：MCP 服务器扩展能力
7. **验证循环**：给 Claude 自我验证的能力

### 下一步行动

想要更好地使用 Claude Code？从这里开始：

1. ✅ 为你的项目创建 `CLAUDE.md`
2. ✅ 尝试 Plan 模式进行下一个功能开发
3. ✅ 识别重复性任务并创建 slash command
4. ✅ 设置验证流程让 Claude 自检
5. ✅ 探索 MCP 工具集成

## 资源链接

- [Claude Code 官方文档](https://code.claude.com/docs)
- [Terminal 配置指南](https://code.claude.com/docs/en/terminal-config)
- [Slash Commands 文档](https://code.claude.com/docs/en/slash-commands)
- [Sub Agents 文档](https://code.claude.com/docs/en/sub-agents)
- [Hooks 指南](https://code.claude.com/docs/en/hooks-guide)
- [Chrome 扩展](https://code.claude.com/docs/en/chrome)
- [GitHub Action](https://github.com/anthropics/claude-code-action)

## 结语

正如 Boris 所说："我希望这些对你有帮助！你使用 Claude Code 有什么技巧？想听什么内容？"

Claude Code 的强大在于它的灵活性和可定制性。无论你是个人开发者还是团队成员，都可以根据自己的需求定制工作流程。最重要的是持续学习和改进，就像 Claude 一样。

---

**参考来源**：[Twitter Thread by Boris Cherny](https://twitter-thread.com/t/2007179832300581177)

**作者**：Boris Cherny (@bcherny) - Claude Code 创始人
**整理**：基于 Twitter thread 内容整理翻译
