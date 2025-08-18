---
layout: post
title: "使用Claude Router搭建本地Claude Code服务，借助GPT-OSS:20B模型每月节省200美金"
date: 2025-08-18 10:00:00 +0800
categories: [AI, 技术实践]
tags: [Claude, GPT-OSS, 成本优化, 本地部署]
author_profile: true
header:
  image: /assets/images/run-claude-code-use-gpt-oss-20b/cpuusage.png
  caption: "系统CPU使用率监控"
toc: true
toc_sticky: true
---

## 背景与动机

作为一名AI技术从业者，我每天都需要大量使用Claude Code进行编程和代码审查。然而，随着使用频率的增加，API费用也水涨船高——每月约200美金的支出成为了不可忽视的成本负担。

为了解决这个问题，我决定探索本地化部署方案，通过Claude Router结合开源大模型来替代部分API调用。

## 技术方案选择

### 为什么选择Claude Router？

Claude Router是一个强大的工具，它能够：
- **智能路由**：根据请求类型自动选择最优模型
- **成本优化**：在本地模型和云端API之间智能切换
- **无缝集成**：与现有Claude Code工作流完美兼容

### 为什么选择GPT-OSS:20B？

经过对比测试，GPT-OSS:20B模型在以下方面表现出色：
- **代码理解能力强**：20B参数规模足够处理复杂的编程任务
- **本地部署友好**：显存占用合理，消费级GPU可运行
- **响应速度快**：本地推理延迟低，提升开发效率

## 系统架构设计

```
Claude Code → Claude Router → GPT-OSS:20B (本地)
                        → Claude API (云端，备用)
```

### 硬件配置
- **芯片**: Apple M2 Max
- **统一内存**: 32GB (与GPU共享)
- **存储**: 1TB SSD
- **操作系统**: macOS Sonoma 14.0+

### 软件环境
- **操作系统**: macOS Sonoma 14.0+
- **包管理器**: Homebrew
- **Python**: 3.11 (通过pyenv管理)
- **Ollama**: 最新版本
- **Claude Code Router**: 最新版本
- **GPT-OSS**: 20B量化版本 (通过Ollama)

## 部署步骤

### 1. 环境准备

```bash
# 安装Homebrew (如果没有)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安装Ollama
brew install ollama

# 安装Python和依赖
brew install python
pip install torch torchvision torchaudio
pip install transformers accelerate

# 安装Claude Code Router
npm install -g @saoudrizwan/claude-code-router
```

### 2. 模型下载与配置

```bash
# 启动Ollama服务
ollama serve

# 下载GPT-OSS:20B模型 (注意：需要32GB以上内存)
ollama pull gpt-oss:20b

# 验证模型下载
ollama list
```

### 3. Claude Router配置

对于Mac环境，我们使用Claude Code Router (ccr) 配合Ollama，配置更加简单：

创建配置文件 `~/.claude-code-router/config.json`：

```json
{
  "Providers": [
    {
      "name": "ollama",
      "api_base_url": "http://127.0.0.1:11434/v1/chat/completions",
      "api_key": "ollama-local",
      "models": ["gpt-oss:20b"]
    }
  ],
  "Router": {
    "default": "ollama,gpt-oss:20b"
  }
}
```

**配置说明：**
- **api_base_url**: Ollama服务的本地地址
- **api_key**: 自定义的API密钥，可以是任意值
- **models**: 指定使用的Ollama模型
- **Router.default**: 默认路由到本地的GPT-OSS:20B模型

### 4. 启动服务

#### Mac一键部署脚本

为了简化Mac用户的部署流程，我创建了一个自动化脚本 `setup-claude-router.sh`：

```shell
#!/bin/zsh
set -e

# === 配置参数 ===
MODEL="gpt-oss:20b"
API_KEY="ollama-local"
OLLAMA_HOST="127.0.0.1:11434"
CONFIG_FILE="$HOME/.claude-code-router/config.json"

echo "🔍 检查 Homebrew 安装..."
if ! command -v brew >/dev/null 2>&1; then
  echo "❌ Homebrew 未安装，请先执行："
  echo '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
  exit 1
fi

echo "🔍 检查 Ollama..."
if ! command -v ollama >/dev/null 2>&1; then
  echo "📥 安装 Ollama..."
  brew install ollama
fi

echo "🔍 检查 Claude Code Router..."
if ! command -v ccr >/dev/null 2>&1; then
  echo "❌ 未检测到 ccr，请先安装 Claude Code Router"
  echo "👉 参考文档: https://github.com/saoudrizwan/claude-code-router"
  exit 1
fi

# === 启动 Ollama 服务 (默认 32k context) ===
echo "🚀 启动 Ollama 服务 (context_length=32768)..."
pkill ollama || true
OLLAMA_CONTEXT_LENGTH=32768 OLLAMA_API_KEY=$API_KEY ollama serve > /tmp/ollama.log 2>&1 &
sleep 2

# === 检查模型是否已拉取 ===
if ! ollama list | grep -q "$MODEL"; then
  echo "📥 拉取模型: $MODEL ..."
  ollama pull $MODEL
fi

# === 写入 Claude Code Router 配置 ===
echo "⚙️ 配置 Claude Code Router..."
mkdir -p "$(dirname $CONFIG_FILE)"
cat > $CONFIG_FILE <<EOF
{
  "Providers": [
    {
      "name": "ollama",
      "api_base_url": "http://$OLLAMA_HOST/v1/chat/completions",
      "api_key": "$API_KEY",
      "models": ["$MODEL"]
    }
  ],
  "Router": {
    "default": "ollama,$MODEL"
  }
}
EOF

# === 测试 Ollama API ===
echo "🧪 测试 Ollama API..."
curl -s http://$OLLAMA_HOST/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d "{
    \"model\": \"$MODEL\",
    \"messages\": [{\"role\":\"user\",\"content\":\"hello with 32k context\"}]
  }" | jq '.choices[0].message.content'

# === 启动 Claude Code Router ===
echo "✅ 启动 Claude Code Router..."
exec ccr code
```

**使用方法：**

```bash
# 下载脚本
curl -o setup-claude-router.sh https://raw.githubusercontent.com/your-repo/setup-claude-router.sh

# 赋予执行权限
chmod +x setup-claude-router.sh

# 运行脚本
./setup-claude-router.sh
```

**脚本功能说明：**

1. **环境检查** - 自动检测Homebrew、Ollama和Claude Code Router
2. **依赖安装** - 自动安装缺失的依赖
3. **服务配置** - 配置32k上下文长度的Ollama服务
4. **模型管理** - 自动拉取GPT-OSS:20B模型
5. **API测试** - 验证服务是否正常工作
6. **一键启动** - 自动启动Claude Code Router

## 性能监控与优化

### 系统资源使用情况

![CPU使用率](/assets/images/run-claude-code-use-gpt-oss-20b/cpuusage.png)

从监控数据可以看出，系统CPU使用率在正常负载下保持在40-60%之间，完全在可控范围内。

![内存使用情况](/assets/images/run-claude-code-use-gpt-oss-20b/memeryuasage.png)

内存使用稳定在32GB左右，其中大部分被GPT-OSS模型占用，剩余空间充足。

![系统负载和CPU风扇](/assets/images/run-claude-code-use-gpt-oss-20b/sysloadingandcpufans.png)

系统负载和CPU风扇转速都在正常范围内，说明硬件配置合理。

### 性能优化策略

1. **统一内存优化**：利用M2 Max的统一内存架构，GPU和CPU共享32GB内存
2. **模型量化**：使用4bit量化，内存占用从~40GB降至~12GB
3. **Metal加速**：启用Apple Metal框架，充分利用M2 Max的GPU性能
4. **批处理优化**：合理设置batch_size，平衡吞吐量和延迟
5. **缓存机制**：对常见查询结果进行缓存，减少重复计算
6. **动态路由**：根据任务复杂度智能选择模型

#### M2 Max特定优化

```bash
# 设置Metal后端加速
export PYTORCH_ENABLE_MPS_FALLBACK=1

# 优化内存使用
export OLLAMA_NUM_PARALLEL=1
export OLLAMA_MAX_LOADED_MODELS=1

# 启用Metal优化
ollama serve --metal
```

## 成本效益分析

### 费用对比

| 项目 | Claude API | 本地部署 | 节省 |
|------|-----------|----------|------|
| 月均费用 | $200 | $15 | $185 |
| 年均费用 | $2,400 | $180 | $2,220 |

### 投资回报

- **硬件投资**: ~$2,499 (MacBook Pro 14" M2 Max, 32GB内存, 1TB SSD)
- **投资回收期**: ~13.5个月
- **长期收益**: 每年节省超过$2,200
- **额外价值**: 获得一台高性能移动工作站，可用于其他开发和日常任务

## 实际使用体验

### 优势

1. **成本大幅降低**：从每月$200降至$15
2. **响应速度提升**：本地推理延迟更低
3. **数据隐私保护**：敏感代码无需上传云端
4. **完全可控**：可根据需求调整模型参数

### 挑战

1. **硬件要求较高**：需要高端GPU支持
2. **模型质量差异**：在某些复杂任务上略逊于Claude
3. **维护成本**：需要定期更新模型和依赖
4. **系统负载较高**：本地推理会持续占用大量系统资源，影响其他应用的性能
5. **响应速度较慢**：相比云端API，本地模型推理速度较慢，特别是在处理复杂任务时

## 路由策略优化

### 智能分流规则

```python
def route_request(request_text):
    # 简单的编程任务使用本地模型
    if is_simple_coding_task(request_text):
        return "local_gpt"
    
    # 复杂的推理任务使用Claude API
    if is_complex_reasoning(request_text):
        return "claude_api"
    
    # 默认使用本地模型
    return "local_gpt"
```

### 质量监控机制

- **准确率监控**：定期对比本地模型和API的输出质量
- **用户反馈**：收集开发者对代码质量的反馈
- **自动切换**：质量低于阈值时自动切换到API

## 部署建议

### 适合场景

1. **个人开发者**：高频代码生成需求
2. **小型团队**：预算有限但有AI编程需求
3. **企业内部**：对代码隐私有要求的场景

### 不适合场景

1. **硬件资源有限**：无法满足GPU要求
2. **对模型质量要求极高**：需要最先进的推理能力
3. **临时性需求**：短期使用无法覆盖硬件成本

## 未来展望

1. **模型持续优化**：随着开源模型不断进步，本地部署的质量会进一步提升
2. **硬件成本下降**：GPU价格持续下降，部署门槛降低
3. **工具链完善**：更多本地化工具出现，使用更加便捷
4. **混合部署模式**：本地+云端的混合模式成为主流

## 结论

通过Claude Router + GPT-OSS:20B的本地化部署方案，我成功将每日AI编程成本从$30降至几乎为零，同时保持了良好的使用体验。虽然前期有一定硬件投入，但从长期来看具有显著的经济效益。

对于有类似需求的开发者，我强烈推荐考虑这种本地化部署方案。它不仅能够大幅降低成本，还能提供更好的数据隐私保护和响应速度。

---

*如果你对这个方案有任何问题或建议，欢迎在评论区交流。*

## 相关资源

- [Claude Router GitHub仓库](https://github.com/claude-router/claude-router)
- [GPT-OSS模型页面](https://huggingface.co/gpt-oss)
- [Claude Code官方文档](https://docs.anthropic.com/claude-code)