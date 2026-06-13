#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Edge-TTS CLI — Microsoft Edge Online TTS (免费，无需 API Key)

用法:
  python edge_tts_reply.py "你好，这是语音回复" -o reply.mp3
  python edge_tts_reply.py "专业反馈" -o feedback.mp3 -v zh-CN-YunxiNeural --rate "-10%"
"""

import argparse
import asyncio
import edge_tts

# 销售教练场景推荐音色
VOICES = {
    "coach-pro": "zh-CN-YunyangNeural",    # 男声，成熟、新闻主播风（默认）
    "coach-young": "zh-CN-YunxiNeural",     # 男声，年轻、现代感
    "coach-energy": "zh-CN-YunjianNeural",  # 男声，活力、激情
    "coach-calm": "zh-CN-YunxiaNeural",     # 男声，沉稳、叙述
    "female-pro": "zh-CN-XiaoxiaoNeural",    # 女声，专业、清晰
    "female-warm": "zh-CN-XiaohanNeural",   # 女声，温暖、柔和
}

DEFAULT_VOICE = "zh-CN-YunyangNeural"


async def synthesize(text: str, voice: str, rate: str, output: str):
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save(output)
    print(f"OK: {output}")


def main():
    p = argparse.ArgumentParser(description="Edge-TTS 语音合成（免费）")
    p.add_argument("text", help="要合成的文字")
    p.add_argument("-o", "--output", required=True, help="输出文件路径 (.mp3)")
    p.add_argument("-v", "--voice", default=DEFAULT_VOICE,
                   help=f"音色 (默认: {DEFAULT_VOICE})")
    p.add_argument("--rate", default="+0%", help="语速调整 (如 '-10%' 慢, '+10%' 快)")
    p.add_argument("--list-voices", action="store_true", help="列出推荐音色")
    args = p.parse_args()

    if args.list_voices:
        print("推荐音色（销售教练场景）：")
        for k, v in VOICES.items():
            print(f"  {k:15s} → {v}")
        return

    # 支持别名
    voice = VOICES.get(args.voice, args.voice)
    asyncio.run(synthesize(args.text, voice, args.rate, args.output))


if __name__ == "__main__":
    main()
