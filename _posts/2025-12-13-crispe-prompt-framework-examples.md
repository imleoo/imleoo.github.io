---
layout: post
title: "CRISPE Prompt框架实战指南：代码审查、Bug修复与APP开发完整示例"
date: 2025-12-13 10:00:00 +0800
categories: [AI, Prompt工程, 开发实践]
tags: [CRISPE, Prompt框架, 代码审查, Bug修复, Flutter, AI编程]
author_profile: true
header:
  image: /assets/images/avatar.png
  caption: "CRISPE Prompt框架实战"
toc: true
toc_sticky: true
excerpt: "深入解析CRISPE Prompt框架的实战应用，通过代码审查、Bug修复和Flutter天气APP开发三个完整示例，展示如何用结构化提示词获得高质量AI输出。"
---

> CRISPE是一个强大的Prompt结构化框架，包含六个核心要素：**C**apacity（角色）、**R**equest（任务）、**I**nput（输入）、**S**teps（步骤）、**P**arameters（参数）、**E**xamples（示例）。本文通过三个实战案例，展示如何运用CRISPE框架获得高质量的AI输出。

## CRISPE框架概述

CRISPE框架通过六个维度构建完整的提示词，让AI能够准确理解需求并生成高质量输出：

| 要素 | 含义 | 作用 |
|------|------|------|
| **C** - Capacity | 角色设定 | 定义AI扮演的专业角色 |
| **R** - Request | 具体任务 | 明确要完成的核心任务 |
| **I** - Input | 输入信息 | 提供必要的上下文和数据 |
| **S** - Steps | 执行步骤 | 规定任务的执行流程 |
| **P** - Parameters | 参数约束 | 设定输出格式和质量标准 |
| **E** - Examples | 示例参考 | 提供期望输出的样例 |

---

## 示例一：代码审查场景

### 场景背景
需要对一个登录API进行安全审查，识别潜在漏洞并提供修复建议。

### CRISPE提示词

#### 【C】角色
```
你是一位资深代码审查专家，专注于识别OWASP Top 10安全漏洞、性能问题和代码规范违规
```

#### 【R】任务
```
审查以下登录API代码，识别安全漏洞、性能问题和规范违规，并提供修复建议
```

#### 【I】输入
**待审查代码：**
```javascript
router.post('/login', async (req, res) => {
  const { email, password } = req.body;
  const user = await User.findOne({ email });
  if (user && user.password === password) {
    res.json({ token: generateToken(user) });
  } else {
    res.json({ error: '登录失败' });
  }
});
```

**技术栈：** Node.js + Express + MongoDB

#### 【S】步骤
1. 检查SQL注入/NoSQL注入风险
2. 检查密码存储安全性
3. 检查错误处理是否完善
4. 检查是否缺少输入验证
5. 检查性能问题(N+1查询、索引等)
6. 对每个问题提供具体的修复代码示例

#### 【P】参数
- 按严重程度分级：🔴严重 🟡中等 🟢轻微
- 每个问题包含：问题描述 + 风险说明 + 修复代码
- 修复代码需完整可直接使用
- 输出格式为Markdown表格

#### 【E】示例
期望输出格式：

| 问题 | 严重度 | 修复建议 |
|------|--------|----------|
| 密码明文存储 | 🔴 | 使用bcrypt加密... |
| 缺少错误处理 | 🟡 | 添加try-catch... |

### 应用要点
- **C-角色**：定义为代码审查专家，关注安全和性能
- **R-任务**：审查代码，识别问题并提供修复建议
- **I-输入**：提供待审查的代码和技术栈
- **S-步骤**：按照6个检查点逐一审查
- **P-参数**：要求按严重度分级，输出Markdown表格
- **E-示例**：展示期望的表格格式

CRISPE框架让代码审查**系统化、标准化**，确保不遗漏关键检查点。

---

## 示例二：Bug修复场景

### 场景背景
诊断API性能问题，响应时间从50ms突然增加到5000ms。

### CRISPE提示词

#### 【C】角色
```
你是一位Debug专家，擅长问题诊断、根因分析和性能调优
```

#### 【R】任务
```
诊断并修复以下性能问题：API响应时间从50ms突然增加到5000ms
```

#### 【I】输入
**问题代码：**
```javascript
router.get('/users/:id/posts', async (req, res) => {
  const user = await User.findById(req.params.id);
  const posts = await Post.find({ userId: user.id });

  for (let post of posts) {
    post.author = await User.findById(post.userId);
    post.comments = await Comment.find({ postId: post.id });
  }

  res.json(posts);
});
```

**环境信息：**
- 数据库：MongoDB (远程服务器，延迟30ms)
- 用户posts数量：平均100条
- 每个post的comments：平均10条

#### 【S】步骤
1. 分析当前代码的执行流程
2. 计算数据库查询次数和总耗时
3. 识别N+1查询问题
4. 提供优化方案(使用聚合/populate/join)
5. 计算优化后的查询次数和性能提升
6. 给出完整的修复代码

#### 【P】参数
- 输出包含：问题分析 + 性能计算 + 优化方案 + 修复代码
- 使用Markdown格式，代码块使用语法高亮
- 必须说明性能提升倍数

#### 【E】示例
期望输出格式：

```markdown
## 问题分析
N+1查询问题：循环中执行201次数据库查询

## 性能计算
当前：201次 × 30ms = 6030ms
优化后：3次 × 30ms = 90ms
提升：67倍

## 修复代码
// 优化后的代码...
```

### 应用要点
- **C-角色**：Debug专家，擅长问题诊断
- **R-任务**：诊断性能问题，从50ms降到5000ms
- **I-输入**：提供问题代码和环境信息(延迟、数据量)
- **S-步骤**：分析流程 → 计算耗时 → 识别问题 → 提供方案 → 修复代码
- **P-参数**：要求说明性能提升倍数，使用Markdown格式

这个示例展示了CRISPE在**复杂问题诊断**中的威力。

---

## 示例三：Flutter天气APP开发

### 场景背景
开发一个完整的Flutter天气预报应用，调用公开API获取天气数据。

### CRISPE提示词

#### 【C - Capacity 角色设定】
```
你是一位拥有8年经验的Flutter高级开发工程师，精通Dart语言、Flutter框架和Material Design设计。
你擅长状态管理、网络请求、UI/UX优化和编写高质量、可维护的移动应用代码。
```

#### 【R - Request 具体任务】
```
实现一个Flutter天气预报APP，通过调用 https://wttr.in/beijing API获取天气数据。
需要实现精美的卡片式UI界面，支持下拉刷新、温度单位切换、天气图标展示。
```

#### 【I - Input 输入信息】
**技术栈：**
- Flutter 3.16
- Dart 3.2
- http 1.1.0 (网络请求)
- provider 6.1.0 (状态管理)

**API接口：**
- 天气数据：https://wttr.in/beijing?format=j1
- 返回JSON格式的天气信息

**设计要求：**
- 卡片式布局，渐变背景
- 显示当前温度、天气状况、湿度、风速
- 未来3天天气预报

**现有代码框架：**
```dart
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() => runApp(WeatherApp());

class WeatherApp extends StatelessWidget {
  // TODO: 实现天气APP
}
```

#### 【S - Steps 执行步骤】
1. 创建WeatherModel数据模型，解析API返回的JSON数据
2. 实现WeatherService服务类，封装HTTP请求逻辑
3. 使用Provider创建WeatherProvider状态管理
4. 设计主页面WeatherHomePage：
   - 顶部显示城市名称和当前时间
   - 中部大号显示当前温度和天气图标
   - 底部卡片展示湿度、风速、体感温度等详细信息
5. 实现下拉刷新功能，重新获取天气数据
6. 添加加载状态和错误处理UI
7. 实现温度单位切换(摄氏度/华氏度)
8. 实现渐变背景和卡片阴影效果

#### 【P - Parameters 参数约束】
**代码规范：**
- 遵循Dart官方代码规范
- 使用Material Design 3设计语言
- 所有网络请求使用async/await

**错误处理：**
- 网络请求包裹在try-catch中
- 网络异常时显示友好的错误提示
- 添加超时处理(10秒)

**UI要求：**
- 使用渐变背景(蓝色系)
- 卡片使用圆角和阴影效果
- 图标使用Material Icons或天气图标
- 字体大小层次分明(温度>标题>详情)

**注释要求：**
- 关键Widget添加中文注释
- Model类属性注释说明

**输出格式：**
- 生成完整的单文件main.dart代码
- 包含所有必要的import语句
- 代码长度控制在300行以内

#### 【E - Examples 示例参考】
**API返回数据示例：**
```json
{
  "current_condition": [{
    "temp_C": "15",
    "weatherDesc": [{"value": "Sunny"}],
    "humidity": "45",
    "windspeedKmph": "12"
  }],
  "weather": [{
    "date": "2024-01-15",
    "maxtempC": "18",
    "mintempC": "8"
  }]
}
```

**期望的UI规范：**
- 渐变背景：从深蓝 #1E3C72 到浅蓝 #2A5298
- 大温度显示：72px，粗体，白色
- 天气图标：48x48，居中
- 信息卡片：白色半透明，圆角16px，阴影8px

### 应用要点
- **C-角色**：定义为8年经验的Flutter高级开发工程师，精通Dart和Material Design
- **R-任务**：开发天气预报APP，调用wttr.in API，实现精美的卡片式UI
- **I-输入**：提供Flutter技术栈、API接口、设计参考和代码框架
- **S-步骤**：定义了8个清晰步骤，从数据模型、网络服务、状态管理到UI实现，逻辑完整
- **P-参数**：约束Dart规范、Material Design 3、错误处理、UI要求(渐变、圆角、阴影)
- **E-示例**：提供API数据格式和UI设计规范(颜色、字体、布局)的具体参考

这个完整的**移动端CRISPE Prompt**，六要素完整，AI能生成可直接运行的Flutter应用，展示了CRISPE框架的**跨领域适用性**。

---

## 总结

通过以上三个实战案例，我们可以看到CRISPE框架的强大之处：

| 场景 | 核心价值 | 输出质量 |
|------|----------|----------|
| 代码审查 | 系统化检查，不遗漏关键点 | 结构化问题清单 + 修复代码 |
| Bug修复 | 根因分析，量化性能提升 | 完整诊断报告 + 优化方案 |
| APP开发 | 端到端实现，完整可运行 | 生产级代码 + 最佳实践 |

### CRISPE使用建议

1. **角色要专业**：定义具体的专业背景和技能领域
2. **任务要明确**：清晰描述期望的最终成果
3. **输入要充分**：提供足够的上下文和约束条件
4. **步骤要具体**：拆解任务为可执行的检查点
5. **参数要量化**：用具体数值约束输出质量
6. **示例要典型**：展示期望的输出格式和内容

掌握CRISPE框架，让你的AI对话从"试探性提问"升级为"精准任务下达"，显著提升AI输出质量和工作效率。

---

## 📎 附件下载

**CRISPE框架完整模板** - 包含详细的角色定义、任务描述、输入示例、执行步骤、参数约束和参考模板。

[🔗 下载 CRISPE Prompt框架模板](/downloads/crispe-prompt-framework-template.md)

该模板文件包含了本文中所有示例的完整版本，以及更多实用的CRISPE提示词模板，可以直接复制使用并根据具体需求进行修改。
