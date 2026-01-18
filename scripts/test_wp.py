#!/usr/bin/env python3
"""
测试WordPress连接

用法:
  python scripts/test_wp.py
"""
import sys
from pathlib import Path

# 添加src到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.config import Config
from src.core.wordpress import WordPressClient


def main():
    print("=" * 60)
    print("🔌 测试WordPress连接")
    print("=" * 60)
    
    if not Config.WP_SITE_URL:
        print("❌ WP_SITE_URL 未设置")
        sys.exit(1)
    
    print(f"\n📋 WordPress配置:")
    print(f"   URL: {Config.WP_SITE_URL}")
    print(f"   用户: {Config.WP_USERNAME}")
    print()
    
    client = WordPressClient()
    
    print("🔍 测试连接...")
    if client.test_connection():
        print("✅ WordPress连接成功!")
        print("\n可以使用以下功能:")
        print("  - client.create_page(title, content)")
        print("  - client.create_post(title, content)")
    else:
        print("❌ WordPress连接失败")
        print("\n请检查:")
        print("  1. WP_SITE_URL 是否正确（包含http/https）")
        print("  2. WP_USERNAME 是否正确")
        print("  3. WP_APP_PASSWORD 是否正确（包含空格）")
        print("  4. WordPress REST API 是否启用")
        sys.exit(1)


if __name__ == "__main__":
    main()
