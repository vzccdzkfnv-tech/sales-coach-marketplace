# 语音回复 Skill（Edge-TTS）

基于 Microsoft Edge 在线 TTS 的语音合成工具，**免费、无需 API Key、无需 GPU**。

## 快速使用

```bash
# 基础用法（默认男声教练）
python3 edge_tts_reply.py "你好，这段汇报整体不错，有三个地方可以优化" -o reply.mp3

# 慢速讲解（适合详细分析）
python3 edge_tts_reply.py "接下来我逐句给你分析这段汇报" -o analysis.mp3 --rate "-15%"

# 温暖鼓励风格
python3 edge_tts_reply.py "你做得很好，继续保持" -o encourage.mp3 -v zh-CN-YunyangNeural

# 女声专业风格
python3 edge_tts_reply.py "我来帮你梳理一下思路" -o reply.mp3 -v zh-CN-XiaoxiaoNeural
```

> **前置依赖**：需安装 edge-tts 包（`pip install edge-tts`）

## 推荐音色

| 别名 | 实际 Voice ID | 风格 | 适用场景 |
|------|-------------|------|---------|
| `coach-pro`（默认） | `zh-CN-YunyangNeural` | 男声，成熟、新闻主播风 | 教练点评、正式反馈（默认） |
| `coach-warm` | `zh-CN-YunxiNeural` | 男声，年轻、现代感 | 鼓励性反馈、轻松对话 |
| `coach-young` | `zh-CN-YunjianNeural` | 男声，年轻、活力 | 轻松对话、日常咨询 |
| `female-pro` | `zh-CN-XiaoxiaoNeural` | 女声，专业、清晰 | 专业分析 |
| `female-warm` | `zh-CN-XiaohanNeural` | 女声，温暖、柔和 | 温暖鼓励 |

## 参数

| 参数 | 必填 | 默认值 | 说明 |
|------|------|--------|------|
| `text` | ✅ | - | 要合成的文字 |
| `-o/--output` | ✅ | - | 输出文件路径 (.mp3) |
| `-v/--voice` | ❌ | `zh-CN-YunyangNeural` | 音色（支持别名或完整 Voice ID） |
| `--rate` | ❌ | `+0%` | 语速调整，如 `-10%` 慢，`+10%` 快 |
| `--list-voices` | ❌ | - | 列出推荐音色 |

## 语音推送方式

生成 mp3 后，**唯一正确的推送方式**是 `open_result_view`：

```
open_result_view({
  target_file: "/path/to/voice_reply_01.mp3",
  explanation: "角色名·第N轮·简短描述"
})
```

这会在用户右侧面板显示内置音频播放器，可直接点击播放。

**❌ 以下方式均不可用**（已验证失败）：
- `deliver_attachments` → 界面无法直接播放
- `preview_url` + CloudStudio → 不稳定
- HTML 内嵌 base64 → 文件太大
- 本地 HTTP 服务器 → 客户端访问不到
- `preview_url` + HTML → 缓存不刷新

## 输出路径规范

所有语音文件输出到当前工作目录（相对路径），不要硬编码绝对路径：
```
voice_reply_01.mp3
```
序号递增，每次生成前先删掉旧文件保持干净。

## 优势

- ✅ 完全免费，无需 API Key
- ✅ 无需 GPU/本地模型，在线服务
- ✅ 中文语音质量优秀
- ✅ 支持语速调节
