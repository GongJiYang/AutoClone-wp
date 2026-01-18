#!/usr/bin/env python3
"""
清理输出文件

用法:
  python scripts/cleanup.py           # 清理所有输出
  python scripts/cleanup.py --keep N  # 保留最近N天的文件
"""
import shutil
import sys
import time
from pathlib import Path

# 添加src到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.config import Config


def cleanup(keep_days: int = 0):
    """清理输出目录"""
    print("=" * 60)
    print("🧹 清理输出文件")
    print("=" * 60)
    
    dirs_to_clean = [
        Config.SCREENSHOT_DIR,
        Config.ANALYSIS_DIR,
        Config.GENERATED_DIR,
    ]
    
    total_size = 0
    total_files = 0
    
    now = time.time()
    keep_seconds = keep_days * 24 * 3600
    
    for dir_path in dirs_to_clean:
        if not dir_path.exists():
            print(f"⏭️  跳过（不存在）: {dir_path}")
            continue
        
        if keep_days > 0:
            # 只删除旧文件
            for file in dir_path.rglob("*"):
                if file.is_file():
                    file_age = now - file.stat().st_mtime
                    if file_age > keep_seconds:
                        total_size += file.stat().st_size
                        total_files += 1
                        file.unlink()
            print(f"✅ 清理旧文件: {dir_path}")
        else:
            # 删除整个目录
            for file in dir_path.rglob("*"):
                if file.is_file():
                    total_size += file.stat().st_size
                    total_files += 1
            
            shutil.rmtree(dir_path)
            print(f"✅ 删除目录: {dir_path}")
    
    # 重新创建目录
    Config.ensure_dirs()
    
    print("\n" + "=" * 60)
    print(f"✅ 清理完成!")
    print(f"   删除文件: {total_files} 个")
    print(f"   释放空间: {total_size / (1024*1024):.1f} MB")
    print("=" * 60)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='清理输出文件')
    parser.add_argument('--keep', type=int, default=0, help='保留最近N天的文件（0=全部删除）')
    args = parser.parse_args()
    
    cleanup(args.keep)


if __name__ == "__main__":
    main()
