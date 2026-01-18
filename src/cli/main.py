#!/usr/bin/env python3
"""
AutoClone 主入口
"""
import asyncio
import sys
from pathlib import Path

# 添加src到路径
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.core.config import Config
from src.core.screenshot import ScreenshotCapture
from src.core.analyzer import VisionAnalyzer


async def main():
    """主函数"""
    Config.ensure_dirs()
    
    errors = Config.validate()
    if errors:
        print("❌ 配置错误:")
        for error in errors:
            print(f"   - {error}")
        print("\n请在 .env 文件中设置相关配置")
        return
    
    print("=" * 60)
    print("🚀 AutoClone - 网页克隆到WordPress")
    print("=" * 60)
    print("\n请使用具体命令:")
    print("  python -m src.cli.analyze <url>")
    print("  python -m src.cli.batch <csv_file>")


if __name__ == "__main__":
    asyncio.run(main())
