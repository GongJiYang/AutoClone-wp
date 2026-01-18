#!/usr/bin/env python3
"""
批量分析脚本

用法:
  python scripts/batch.py [csv_file] [--limit N] [--start N]

示例:
  python scripts/batch.py                          # 处理所有URL
  python scripts/batch.py data/urls.csv --limit 5  # 只处理前5个
  python scripts/batch.py --start 10 --limit 10    # 从第10个开始处理10个
"""
import asyncio
import csv
import sys
import time
from pathlib import Path

# 添加src到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.config import Config


def load_urls(csv_path: Path, start: int = 0, limit: int = None) -> list:
    """从CSV加载URL列表"""
    urls = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            urls.append({
                'id': row.get('id'),
                'url': row.get('source_url'),
                'status': row.get('status', 'pending')
            })
    
    # 应用start和limit
    if start > 0:
        urls = urls[start:]
    if limit:
        urls = urls[:limit]
    
    return urls


def get_output_name(url: str, url_id: str = None) -> str:
    """从URL生成输出名称"""
    slug = url.rstrip('/').split('/')[-1] or 'homepage'
    if url_id:
        return f"{url_id}_{slug}"
    return slug


async def process_url(url_data: dict, index: int, total: int):
    """处理单个URL"""
    from scripts.analyze import analyze_page
    
    url = url_data['url']
    url_id = url_data.get('id', '')
    output_name = get_output_name(url, url_id)
    
    print(f"\n{'='*60}")
    print(f"📋 [{index+1}/{total}] 处理: {url}")
    print(f"{'='*60}")
    
    # 检查是否已处理（使用带模型后缀的文件名）
    model_suffix = Config.get_model_suffix()
    json_path = Config.ANALYSIS_DIR / f"{output_name}_{model_suffix}.json"
    if json_path.exists():
        print(f"   ⏭️  跳过（已存在）: {output_name}_{model_suffix}")
        return True
    
    try:
        await analyze_page(url, output_name)
        return True
    except Exception as e:
        print(f"   ❌ 处理失败: {e}")
        return False


async def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='批量分析页面')
    parser.add_argument('csv_file', nargs='?', default='data/urls.csv', help='CSV文件路径')
    parser.add_argument('--start', type=int, default=0, help='从第N个开始')
    parser.add_argument('--limit', type=int, default=None, help='只处理N个')
    args = parser.parse_args()
    
    csv_path = Path(args.csv_file)
    if not csv_path.is_absolute():
        csv_path = Config.BASE_DIR / args.csv_file
    
    if not csv_path.exists():
        print(f"❌ CSV文件不存在: {csv_path}")
        sys.exit(1)
    
    # 验证配置
    errors = Config.validate()
    if errors:
        print("\n❌ 配置错误:")
        for error in errors:
            print(f"   - {error}")
        sys.exit(1)
    
    Config.ensure_dirs()
    
    # 加载URL
    urls = load_urls(csv_path, args.start, args.limit)
    
    print("=" * 60)
    print("🚀 批量分析")
    print("=" * 60)
    print(f"📁 CSV文件: {csv_path}")
    print(f"📋 待处理: {len(urls)} 个URL")
    print(f"🤖 视觉模型: {Config.VISION_MODEL}")
    print("=" * 60)
    
    success_count = 0
    fail_count = 0
    
    for i, url_data in enumerate(urls):
        try:
            success = await process_url(url_data, i, len(urls))
            if success:
                success_count += 1
            else:
                fail_count += 1
        except Exception as e:
            print(f"   ❌ 异常: {e}")
            fail_count += 1
        
        # 每处理5个休息一下
        if (i + 1) % 5 == 0 and i < len(urls) - 1:
            print(f"\n⏸️  休息10秒...")
            time.sleep(10)
    
    print("\n" + "=" * 60)
    print("📊 批量处理完成!")
    print(f"   ✅ 成功: {success_count}")
    print(f"   ❌ 失败: {fail_count}")
    print(f"   📁 输出目录: {Config.OUTPUT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
