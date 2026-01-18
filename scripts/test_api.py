#!/usr/bin/env python3
"""
API请求测试脚本 - 测试视觉模型API并处理速率限制

用法:
  python scripts/test_api.py [--model MODEL] [--count N] [--delay SECONDS]

示例:
  python scripts/test_api.py --model glm-4.6v --count 5
  python scripts/test_api.py --model glm-4v-flash --count 10 --delay 2
"""
import asyncio
import argparse
import base64
import json
import sys
import time
from pathlib import Path
from typing import Optional

# 添加src到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.config import Config
from zhipuai import ZhipuAI


class RateLimitHandler:
    """速率限制处理器"""
    
    def __init__(self, max_retries: int = 5, initial_delay: float = 1.0, max_delay: float = 60.0):
        self.max_retries = max_retries
        self.initial_delay = initial_delay
        self.max_delay = max_delay
        self.retry_count = 0
    
    def should_retry(self, error_code: int, error_message: str) -> bool:
        """判断是否应该重试"""
        # 429: 速率限制
        # 500, 502, 503: 服务器错误
        # 1113: 余额不足（不应该重试）
        retryable_codes = [429, 500, 502, 503]
        
        if error_code in retryable_codes:
            # 检查是否是余额不足
            if "余额不足" in error_message or "1113" in error_message:
                return False
            return True
        
        return False
    
    def get_delay(self, retry_count: int) -> float:
        """计算延迟时间（指数退避）"""
        delay = min(
            self.initial_delay * (2 ** retry_count),
            self.max_delay
        )
        # 添加随机抖动（±20%）
        import random
        jitter = delay * 0.2 * (random.random() * 2 - 1)
        return delay + jitter
    
    async def wait_with_backoff(self, retry_count: int):
        """等待并显示倒计时"""
        delay = self.get_delay(retry_count)
        print(f"   ⏳ 等待 {delay:.1f} 秒后重试 (第 {retry_count + 1}/{self.max_retries} 次)...", flush=True)
        
        # 显示倒计时
        for remaining in range(int(delay), 0, -1):
            print(f"   ⏱️  {remaining} 秒...", end='\r', flush=True)
            await asyncio.sleep(1)
        print("   ✅ 继续重试...", flush=True)


def create_test_image() -> str:
    """创建一个测试图片（base64编码）"""
    # 创建一个简单的测试图片
    from PIL import Image, ImageDraw, ImageFont
    import io
    
    # 创建图片
    img = Image.new('RGB', (800, 600), color='white')
    draw = ImageDraw.Draw(img)
    
    # 绘制文字
    text = "API Test Image\nVision Model Test"
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 40)
    except:
        font = ImageFont.load_default()
    
    # 获取文字尺寸
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # 居中绘制
    x = (800 - text_width) // 2
    y = (600 - text_height) // 2
    draw.text((x, y), text, fill='black', font=font)
    
    # 转换为base64
    buffer = io.BytesIO()
    img.save(buffer, format='JPEG', quality=85)
    img_bytes = buffer.getvalue()
    return base64.b64encode(img_bytes).decode('utf-8')


async def test_api_call(
    client: ZhipuAI,
    model: str,
    image_base64: str,
    request_num: int,
    delay_between_requests: float = 0,
    rate_limit_handler: Optional[RateLimitHandler] = None
) -> dict:
    """测试单次API调用"""
    print(f"\n📤 请求 #{request_num}: {model}", flush=True)
    
    if delay_between_requests > 0:
        print(f"   ⏳ 延迟 {delay_between_requests} 秒...", flush=True)
        await asyncio.sleep(delay_between_requests)
    
    prompt = "请简单描述这张图片的内容。"
    
    start_time = time.time()
    retry_count = 0
    
    while retry_count <= (rate_limit_handler.max_retries if rate_limit_handler else 0):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{
                    "role": "user",
                    "content": [
                        {"type": "image_url", "image_url": {"url": image_base64}},
                        {"type": "text", "text": prompt}
                    ]
                }]
            )
            
            elapsed = time.time() - start_time
            content = response.choices[0].message.content
            
            print(f"   ✅ 成功! 耗时: {elapsed:.2f}秒", flush=True)
            print(f"   📝 响应: {content[:100]}...", flush=True)
            
            return {
                "success": True,
                "request_num": request_num,
                "elapsed_time": elapsed,
                "response_length": len(content),
                "retry_count": retry_count
            }
            
        except Exception as e:
            elapsed = time.time() - start_time
            error_str = str(e)
            
            # 解析错误代码
            error_code = 0
            error_message = error_str
            
            if "Error code:" in error_str:
                try:
                    parts = error_str.split("Error code:")[1].split(",")[0].strip()
                    error_code = int(parts)
                except:
                    pass
            
            if "error text" in error_str:
                try:
                    import re
                    match = re.search(r'"message":"([^"]+)"', error_str)
                    if match:
                        error_message = match.group(1)
                except:
                    pass
            
            print(f"   ❌ 失败 (尝试 {retry_count + 1}): {error_message}", flush=True)
            
            # 检查是否应该重试
            if rate_limit_handler and rate_limit_handler.should_retry(error_code, error_message):
                if retry_count < rate_limit_handler.max_retries:
                    await rate_limit_handler.wait_with_backoff(retry_count)
                    retry_count += 1
                    continue
                else:
                    print(f"   ⚠️  已达到最大重试次数 ({rate_limit_handler.max_retries})", flush=True)
            
            return {
                "success": False,
                "request_num": request_num,
                "elapsed_time": elapsed,
                "error_code": error_code,
                "error_message": error_message,
                "retry_count": retry_count
            }
    
    return {
        "success": False,
        "request_num": request_num,
        "elapsed_time": elapsed,
        "error_message": "Max retries exceeded",
        "retry_count": retry_count
    }


async def run_test(
    model: str,
    count: int,
    delay: float,
    use_rate_limit_handler: bool = True
):
    """运行测试"""
    print("=" * 60)
    print("🧪 API请求测试")
    print("=" * 60)
    print(f"🤖 模型: {model}")
    print(f"📊 请求数量: {count}")
    print(f"⏱️  请求间隔: {delay} 秒")
    print(f"🔄 速率限制处理: {'启用' if use_rate_limit_handler else '禁用'}")
    print("=" * 60)
    
    # 验证配置
    if not Config.ZHIPU_API_KEY:
        print("\n❌ 错误: ZHIPU_API_KEY 未设置")
        print("请在 .env 文件中设置 ZHIPU_API_KEY")
        sys.exit(1)
    
    # 创建客户端
    client = ZhipuAI(api_key=Config.ZHIPU_API_KEY)
    
    # 创建测试图片
    print("\n📸 创建测试图片...", flush=True)
    test_image = create_test_image()
    print("   ✅ 测试图片已创建", flush=True)
    
    # 速率限制处理器
    rate_limit_handler = None
    if use_rate_limit_handler:
        rate_limit_handler = RateLimitHandler(
            max_retries=5,
            initial_delay=2.0,
            max_delay=60.0
        )
    
    # 执行测试
    results = []
    start_time = time.time()
    
    for i in range(count):
        result = await test_api_call(
            client=client,
            model=model,
            image_base64=test_image,
            request_num=i + 1,
            delay_between_requests=delay if i > 0 else 0,  # 第一个请求不延迟
            rate_limit_handler=rate_limit_handler
        )
        results.append(result)
    
    total_time = time.time() - start_time
    
    # 统计结果
    print("\n" + "=" * 60)
    print("📊 测试结果统计")
    print("=" * 60)
    
    success_count = sum(1 for r in results if r.get("success"))
    fail_count = count - success_count
    
    print(f"✅ 成功: {success_count}/{count}")
    print(f"❌ 失败: {fail_count}/{count}")
    print(f"⏱️  总耗时: {total_time:.2f} 秒")
    print(f"📈 平均耗时: {total_time / count:.2f} 秒/请求")
    
    if success_count > 0:
        success_results = [r for r in results if r.get("success")]
        avg_elapsed = sum(r["elapsed_time"] for r in success_results) / len(success_results)
        print(f"📊 成功请求平均耗时: {avg_elapsed:.2f} 秒")
    
    # 显示失败详情
    if fail_count > 0:
        print("\n❌ 失败详情:")
        for r in results:
            if not r.get("success"):
                print(f"   请求 #{r['request_num']}: {r.get('error_message', 'Unknown error')}")
                if r.get('retry_count', 0) > 0:
                    print(f"      (重试了 {r['retry_count']} 次)")
    
    # 速率限制建议
    if fail_count > 0:
        print("\n💡 改善建议:")
        if delay < 1.0:
            print("   1. 增加请求间隔 (--delay 2 或更高)")
        if not use_rate_limit_handler:
            print("   2. 启用速率限制处理（自动重试）")
        print("   3. 检查API余额和配额")
        print("   4. 考虑使用批量处理模式")
    
    print("=" * 60)
    
    return results


async def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='测试视觉模型API')
    parser.add_argument('--model', type=str, default=Config.VISION_MODEL, 
                       help=f'模型名称 (默认: {Config.VISION_MODEL})')
    parser.add_argument('--count', type=int, default=5, 
                       help='请求数量 (默认: 5)')
    parser.add_argument('--delay', type=float, default=1.0, 
                       help='请求间隔秒数 (默认: 1.0)')
    parser.add_argument('--no-retry', action='store_true', 
                       help='禁用自动重试')
    
    args = parser.parse_args()
    
    await run_test(
        model=args.model,
        count=args.count,
        delay=args.delay,
        use_rate_limit_handler=not args.no_retry
    )


if __name__ == "__main__":
    asyncio.run(main())
