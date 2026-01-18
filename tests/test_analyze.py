#!/usr/bin/env python3
"""
测试页面分析功能
"""
import asyncio
import sys
from pathlib import Path

# 添加src到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.config import Config


async def test_single_url():
    """测试单个URL分析"""
    print("=" * 60)
    print("🧪 测试页面分析功能")
    print("=" * 60)
    
    Config.ensure_dirs()
    
    # 验证配置
    errors = Config.validate()
    if errors:
        print("\n❌ 配置错误:")
        for error in errors:
            print(f"   - {error}")
        print("\n请在 .env 文件中设置相关配置")
        return
    
    # 导入分析函数
    from scripts.analyze import analyze_page
    
    # 测试URL
    test_url = "https://georgeconstructions.com/products/"
    
    print(f"\n📋 测试URL: {test_url}")
    print(f"📁 输出目录: {Config.OUTPUT_DIR}")
    print(f"🤖 视觉模型: {Config.VISION_MODEL}")
    print()
    
    try:
        result = await analyze_page(test_url, "test_products")
        
        print("\n" + "=" * 60)
        print("✅ 测试成功!")
        print("=" * 60)
        print(f"\n📊 分析结果:")
        print(f"   - 分块方法: {result.get('method', 'unknown')}")
        print(f"   - 分块数量: {len(result.get('screenshots', []))}")
        print(f"   - 分析完成: {len(result.get('chunks', []))} 个")
        
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_single_url())
