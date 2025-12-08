#!/usr/bin/env python3

"""
魔方对话服务入口
"""

import argparse
import os
import sys

# 添加 src 目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chat import ChatService
from chat.adb import AdbHelper


def print_banner():
    """显示 ASCII 艺术 banner"""
    GREEN = "\033[32m"  # 绿色
    RESET = "\033[0m"  # 重置颜色
    banner = """
▗▖  ▗▖▗▄▄▄▖ ▗▄▄▖▗▄▄▄▖ ▗▄▄▖     ▗▄▄▖▗▖ ▗▖▗▄▄▖ ▗▄▄▄▖
▐▛▚▞▜▌  █  ▐▌     █  ▐▌       ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌   
▐▌  ▐▌  █  ▐▌▝▜▌  █  ▐▌       ▐▌   ▐▌ ▐▌▐▛▀▚▖▐▛▀▀▘
▐▌  ▐▌▗▄█▄▖▝▚▄▞▘▗▄█▄▖▝▚▄▄▖    ▝▚▄▄▖▝▚▄▞▘▐▙▄▞▘▐▙▄▄▖
                                                                               
Made with ❤️ by https://del.wang   Version: 1.0.0                                           
    """
    print(f"{GREEN}{banner}{RESET}")


def main():
    parser = argparse.ArgumentParser(description="魔方对话服务")
    parser.add_argument(
        "--server",
        help="服务端设备 ID（用于监听语音指令）",
    )
    parser.add_argument(
        "--client",
        help="客户端设备 ID（用于拍照）",
    )
    parser.add_argument(
        "--tts",
        help="TTS 接口地址，比如 http://192.168.31.125:8080/tts.wav",
    )
    parser.add_argument(
        "--debug",
        help="是否为调试模式",
        action="store_true",
    )

    args = parser.parse_args()
    
    # 显示 ASCII banner
    print_banner()

    print("=" * 60)
    print("👓 小米 AI 眼镜 ｜ 看一看，解魔方")
    print("=" * 60)
    
    print("\n✅ 服务已启动...")

    adb = AdbHelper(
        server_device=args.server,
        client_device=args.client,
        tts_api=args.tts,
    )

    service = ChatService(
        adb_helper=adb,
        debug=args.debug,
    )

    service.start()


if __name__ == "__main__":
    main()
