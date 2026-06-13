# 销售专业能力教练（Sales Coach）

AI 销售能力教练专家，支持**语音双向对话、客户模拟对练、录音逐句点评**，像真人教练一样帮你提升销售表达力。

## 功能特性

- 🎤 **语音双向交流**——发语音过去，教练用语音回应，像微信语音聊天一样自然
- 📊 **录音逐句分析**——上传销售汇报录音，逐句点评并给出提升建议
- 🎭 **客户角色扮演**——AI 扮演各类客户（预算敏感型、技术质疑型、竞品绑定型），进行模拟对练
- 📋 **结构化评分报告**——从内容逻辑、语言表达、客户价值传递、临场应变、结构完整性五个维度量化评分
- 🗺️ **个性化提升计划**——根据多次分析结果，识别短板并制定针对性训练计划

## 使用方法

安装后在 WorkBuddy 专家列表中找到「销售专业能力教练」，点击即可开始。

**三种核心用法**：

1. **语音对练**：直接发语音消息，教练自动语音回复
2. **录音分析**：说「帮我听这段销售汇报录音，逐句分析」，粘贴录音文字稿
3. **模拟训练**：说「开启模拟训练，你扮演一位预算有限的客户」

## 安装

### 方式一：从 GitHub 安装（推荐）

```bash
/plugin marketplace add vzccdzkfnv-tech/sales-coach-marketplace
/plugin install sales-coach@sales-coach-marketplace
```

### 方式二：本地安装

将本专家包放到 `~/.workbuddy/plugins/marketplaces/` 对应目录，然后运行：

```bash
python3 <WorkBuddy资源目录>/builtin-skills/expert-manager/scripts/register_expert.py \
  ~/.workbuddy/plugins/marketplaces/my-experts/plugins/sales-coach/
```

## 前置依赖

需要安装 Edge-TTS（免费，无需 API Key）：

```bash
pip install edge-tts
```

## 专家信息

| 项目 | 内容 |
|------|--------|
| 专家名 | sales-coach |
| 显示名 | 销售专业能力教练 |
| 类型 | Agent 型专家 |
| 作者 | Lorne |
| 版本 | 1.0.0 |
| 分类 | 销售与商务（07-SalesCommerce） |

## 许可证

MIT License
