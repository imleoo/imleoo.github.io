# 项目架构文档

## 1. 项目概述
本项目是一个基于 Jekyll 的静态网站，主要用于个人博客、项目展示和联系方式等功能。通过 Jekyll 的模板引擎和 Markdown 支持，实现了内容的快速生成和发布。

## 2. 架构图
![项目架构图](/assets/images/project-architecture.svg)

## 3. 模块说明
### 核心配置文件
- `_config.yml`：定义了网站的基本设置，如标题、描述、插件等。
- `Gemfile` 和 `Gemfile.lock`：管理 Ruby 依赖。

### 内容管理
- `_posts/`：存放博客文章，格式为 Markdown。
- `_layouts/`：定义页面布局模板。
- `_includes/`：包含可复用的 HTML 片段。

### 静态资源
- `assets/`：存放 CSS、JavaScript 和图片资源。
- `pics/` 和 `docs/`：存放额外的图片和文档。

### 生成站点
- `_site/`：Jekyll 生成的静态站点文件，可直接部署到服务器。

## 4. 关键设计决策
- **使用 Jekyll**：选择 Jekyll 是因为其简单易用，适合静态网站的快速生成。
- **目录结构**：遵循 Jekyll 的默认目录结构，便于维护和扩展。

## 5. 依赖关系
- **Ruby**：Jekyll 的运行环境。
- **Jekyll**：核心静态网站生成工具。

## 6. 扩展点
- **插件支持**：未来可以添加更多 Jekyll 插件以增强功能。
- **优化构建流程**：通过 CI/CD 工具自动化构建和部署。
