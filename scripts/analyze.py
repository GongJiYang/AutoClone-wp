#!/usr/bin/env python3
"""
页面分析脚本 - 优化版
整合视觉分析和WordPress代码生成

用法:
  python scripts/analyze.py <url> [output_name]
  
示例:
  python scripts/analyze.py https://example.com/products
  python scripts/analyze.py https://example.com/products my-products
"""
import asyncio
import json
import re
import shutil
import sys
import time
from pathlib import Path
from typing import Optional, Tuple
from urllib.parse import urlparse

# 添加src到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from playwright.async_api import async_playwright  # type: ignore
from src.core.config import Config
from src.core.analyzer import VisionAnalyzer, generate_cursor_prompt_file

# ============== 常量配置 ==============
# 滚动和等待时间（毫秒）
SCROLL_WAIT_MS = 500
ANIMATION_WAIT_MS = 400
LAZY_LOAD_WAIT_MS = 1500  # 增加懒加载等待时间
FIRST_SCREEN_WAIT_MS = 2500  # 增加第一屏等待时间
ANIMATION_COMPLETE_WAIT_MS = 3000
ELEMENT_SCREENSHOT_TIMEOUT_MS = 10000
IMAGE_LOAD_CHECK_TIMEOUT_MS = 5000  # 图片加载检查超时
IMAGE_LOAD_RETRY_DELAY_MS = 200  # 图片加载重试间隔

# API 请求间隔（秒）
API_RATE_LIMIT_DELAY = 1


def sanitize_filename(name: str) -> str:
    """清理文件名，移除特殊字符
    
    Args:
        name: 原始文件名
        
    Returns:
        str: 安全的文件名
    """
    # 只保留字母、数字、下划线和连字符
    safe_name = re.sub(r'[^\w\-]', '_', name)
    # 移除连续的下划线
    safe_name = re.sub(r'_+', '_', safe_name)
    # 移除首尾下划线
    safe_name = safe_name.strip('_')
    return safe_name or 'page'


def extract_domain_name(url: str) -> str:
    """从URL提取域名作为归档目录名
    
    Args:
        url: 网页URL
        
    Returns:
        str: 清理后的域名（用于目录名）
    """
    try:
        parsed = urlparse(url)
        domain = parsed.netloc or parsed.path
        # 移除 www. 前缀
        domain = re.sub(r'^www\.', '', domain)
        # 移除端口号
        domain = domain.split(':')[0]
        # 清理为安全的目录名
        return sanitize_filename(domain)
    except Exception:
        return sanitize_filename(url.rstrip('/').split('/')[-1] or 'unknown')


def archive_files(url: str, output_name: str) -> None:
    """将文件复制到归档目录（保留原文件）
    
    Args:
        url: 网页URL
        output_name: 输出文件名
    """
    domain_name = extract_domain_name(url)
    archive_base_dir = Config.ARCHIVE_DIR / domain_name
    archive_base_dir.mkdir(parents=True, exist_ok=True)
    
    # 创建子目录
    archive_screenshots_dir = archive_base_dir / "screenshots"
    archive_analysis_dir = archive_base_dir / "analysis"
    archive_screenshots_dir.mkdir(parents=True, exist_ok=True)
    archive_analysis_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n📦 复制文件到归档目录: {archive_base_dir}...", flush=True)
    
    archived_count = 0
    archived_size = 0
    
    # 复制截图文件（保留原文件）
    for pattern in [f"{output_name}_*.jpg", f"{output_name}_*.png"]:
        for file_path in Config.SCREENSHOT_DIR.glob(pattern):
            try:
                dest_path = archive_screenshots_dir / file_path.name
                # 如果归档目录已存在同名文件，先删除
                if dest_path.exists():
                    dest_path.unlink()
                size = file_path.stat().st_size
                shutil.copy2(str(file_path), str(dest_path))
                archived_count += 1
                archived_size += size
            except Exception as e:
                print(f"   ⚠️  复制失败 {file_path.name}: {e}", flush=True)
    
    # 复制分析文件（保留原文件）
    for pattern in [f"{output_name}_*.json", f"{output_name}_*.md"]:
        for file_path in Config.ANALYSIS_DIR.glob(pattern):
            try:
                dest_path = archive_analysis_dir / file_path.name
                # 如果归档目录已存在同名文件，先删除
                if dest_path.exists():
                    dest_path.unlink()
                size = file_path.stat().st_size
                shutil.copy2(str(file_path), str(dest_path))
                archived_count += 1
                archived_size += size
            except Exception as e:
                print(f"   ⚠️  复制失败 {file_path.name}: {e}", flush=True)
    
    if archived_count > 0:
        print(f"   ✅ 已复制 {archived_count} 个文件到归档目录 ({archived_size / (1024*1024):.2f} MB)", flush=True)
        print(f"   📁 归档位置: {archive_base_dir}", flush=True)
        print(f"   📂 原文件保留在: {Config.SCREENSHOT_DIR} 和 {Config.ANALYSIS_DIR}", flush=True)
    else:
        print(f"   ⚠️  没有找到要归档的文件", flush=True)


def get_class_name_safe(class_name) -> str:
    """安全获取 className，处理 SVG 元素等特殊情况
    
    Args:
        class_name: 元素的 className 属性
        
    Returns:
        str: 安全的类名字符串
    """
    if isinstance(class_name, str):
        return class_name[:100]
    return ''


async def detect_dom_sections(page) -> list[dict]:
    """检测DOM结构中的sections，返回包含选择器的信息
    
    Returns:
        list[dict]: 包含section信息的字典列表，每个字典包含：
            - tag: 标签名
            - className: 类名
            - id: ID
            - selector: CSS选择器
            - top: 顶部位置
            - height: 高度
            - bottom: 底部位置
            - width: 宽度
    """
    sections = await page.evaluate("""
        () => {
            const selectors = [
                'header', 'nav', 'main > section', 'section',
                '[class*="hero"]', '[class*="banner"]', '[class*="features"]',
                '[class*="products"]', '[class*="testimonials"]', '[class*="cta"]',
                '[class*="footer"]', 'footer', '[id*="section"]', '[class*="section"]'
            ];
            
            const found = new Set();
            const sections = [];
            
            // 安全获取 className 的辅助函数
            const getClassName = (el) => {
                if (typeof el.className === 'string') {
                    return el.className;
                }
                // 处理 SVG 元素的 className (SVGAnimatedString)
                if (el.className && el.className.baseVal !== undefined) {
                    return el.className.baseVal;
                }
                return '';
            };
            
            for (const selector of selectors) {
                const elements = document.querySelectorAll(selector);
                elements.forEach((el, idx) => {
                    const rect = el.getBoundingClientRect();
                    const top = Math.round(rect.top + window.scrollY);
                    const height = Math.round(rect.height);
                    const width = Math.round(rect.width);
                    
                    if (height < 50 || width < 100) return;
                    
                    const key = `${top}-${height}`;
                    if (!found.has(key) && height > 100) {
                        found.add(key);
                        
                        const className = getClassName(el);
                        
                        // 生成唯一选择器
                        let uniqueSelector = selector;
                        if (el.id) {
                            uniqueSelector = `#${el.id}`;
                        } else if (className) {
                            // 使用类名生成更精确的选择器
                            const classes = className.split(' ').filter(c => c.trim()).slice(0, 2);
                            if (classes.length > 0) {
                                uniqueSelector = `${el.tagName.toLowerCase()}.${classes.join('.')}`;
                            } else {
                                uniqueSelector = `${selector}:nth-of-type(${idx + 1})`;
                            }
                        } else {
                            uniqueSelector = `${selector}:nth-of-type(${idx + 1})`;
                        }
                        
                        sections.push({
                            tag: el.tagName.toLowerCase(),
                            className: className.slice(0, 100),
                            id: el.id || '',
                            selector: uniqueSelector,
                            top: top,
                            height: height,
                            bottom: top + height,
                            width: width
                        });
                    }
                });
            }
            
            sections.sort((a, b) => a.top - b.top);
            
            // 合并重叠sections
            const merged = [];
            for (const section of sections) {
                if (merged.length === 0) {
                    merged.push(section);
                } else {
                    const last = merged[merged.length - 1];
                    const overlap = Math.max(0, Math.min(last.bottom, section.bottom) - Math.max(last.top, section.top));
                    if (overlap / Math.min(last.height, section.height) > 0.3) {
                        last.bottom = Math.max(last.bottom, section.bottom);
                        last.height = last.bottom - last.top;
                    } else {
                        merged.push(section);
                    }
                }
            }
            
            return merged;
        }
    """)
    return sections


async def wait_for_images_in_viewport(page, viewport_height: int, scroll_y: int) -> bool:
    """等待视口内的图片加载完成
    
    Args:
        page: Playwright页面对象
        viewport_height: 视口高度
        scroll_y: 当前滚动位置
        
    Returns:
        bool: 是否所有图片都已加载
    """
    max_wait_time = IMAGE_LOAD_CHECK_TIMEOUT_MS
    start_time = time.time() * 1000
    
    while (time.time() * 1000 - start_time) < max_wait_time:
        # 检查视口内的图片是否加载完成
        images_loaded = await page.evaluate(f"""
            () => {{
                const viewportTop = {scroll_y};
                const viewportBottom = viewportTop + {viewport_height};
                const images = Array.from(document.querySelectorAll('img'));
                const visibleImages = images.filter(img => {{
                    const rect = img.getBoundingClientRect();
                    const imgTop = rect.top + window.scrollY;
                    const imgBottom = imgTop + rect.height;
                    return (imgBottom >= viewportTop && imgTop <= viewportBottom);
                }});
                
                if (visibleImages.length === 0) return true;
                
                const loadedCount = visibleImages.filter(img => {{
                    // 检查图片是否加载完成
                    if (img.complete && img.naturalHeight > 0) return true;
                    // 检查是否有data-src等懒加载属性
                    if (img.dataset.src || img.dataset.lazySrc) {{
                        // 懒加载图片，检查是否已经开始加载
                        return img.src && img.src !== window.location.href;
                    }}
                    return false;
                }}).length;
                
                return loadedCount === visibleImages.length;
            }}
        """)
        
        if images_loaded:
            return True
        
        # 等待一小段时间后重试
        await page.wait_for_timeout(IMAGE_LOAD_RETRY_DELAY_MS)
    
    return False


async def preload_lazy_content(page) -> None:
    """预加载懒加载内容：滚动整页触发所有懒加载和动画
    
    Args:
        page: Playwright页面对象
    """
    print("   ⏳ 预加载懒加载内容...", flush=True)
    
    # 获取页面高度
    total_height = await page.evaluate("document.body.scrollHeight")
    viewport_height = await page.evaluate("window.innerHeight")
    
    # 分段滚动，触发懒加载和滚动动画
    scroll_step = viewport_height // 2
    current_scroll = 0
    
    while current_scroll < total_height:
        await page.evaluate(f"window.scrollTo(0, {current_scroll})")
        await page.wait_for_timeout(SCROLL_WAIT_MS)
        # 等待当前视口的图片加载
        await wait_for_images_in_viewport(page, viewport_height, current_scroll)
        current_scroll += scroll_step
        total_height = await page.evaluate("document.body.scrollHeight")
    
    # 滚动到底部
    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    await page.wait_for_timeout(LAZY_LOAD_WAIT_MS)
    await wait_for_images_in_viewport(page, viewport_height, total_height - viewport_height)
    
    # 再次从头到尾滚动一遍，确保所有滚动触发的动画都执行
    print("   ⏳ 触发滚动动画...", flush=True)
    await page.evaluate("window.scrollTo(0, 0)")
    await page.wait_for_timeout(SCROLL_WAIT_MS)
    
    current_scroll = 0
    while current_scroll < total_height:
        await page.evaluate(f"window.scrollTo(0, {current_scroll})")
        await page.wait_for_timeout(ANIMATION_WAIT_MS)
        await wait_for_images_in_viewport(page, viewport_height, current_scroll)
        current_scroll += scroll_step
    
    # 滚动回顶部
    await page.evaluate("window.scrollTo(0, 0)")
    await page.wait_for_timeout(LAZY_LOAD_WAIT_MS)
    await wait_for_images_in_viewport(page, viewport_height, 0)
    
    # 等待所有动画完成（数字计数器、淡入等）
    await page.wait_for_timeout(ANIMATION_COMPLETE_WAIT_MS)
    
    print("   ✅ 懒加载和动画已完成", flush=True)


async def capture_screenshots(page, output_name: str) -> Tuple[dict, list]:
    """智能分块截图
    
    Args:
        page: Playwright页面对象
        output_name: 输出文件名（已清理）
    
    Returns:
        tuple: (page_info字典, screenshots列表)
    """
    viewport_height = Config.VIEWPORT_HEIGHT
    overlap = Config.OVERLAP
    
    # 预加载懒加载内容
    await preload_lazy_content(page)
    
    # 获取页面信息（懒加载后的真实高度）
    page_info = await page.evaluate("""
        () => ({
            title: document.title,
            totalHeight: document.body.scrollHeight
        })
    """)
    
    total_height = page_info['totalHeight']
    
    # 检测 DOM 结构（仅供参考）
    print("   🔍 检测DOM结构（仅供参考）...", flush=True)
    sections = await detect_dom_sections(page)
    
    screenshots = []
    
    # 始终使用像素分块，确保完整覆盖，不遗漏轮播图等动态内容
    method = 'pixel'

    # 像素分块 - 确保从上到下完整截取，不遗漏任何内容
    print(f"   📸 使用像素分块，确保完整覆盖页面（总高度: {total_height}px）", flush=True)

    chunk_height = viewport_height - overlap
    # 计算所需分块数，确保完整覆盖
    num_chunks = max(1, (total_height + chunk_height - 1) // chunk_height)

    # 如果分块太多，给出警告但继续
    if num_chunks > 20:
        print(f"   ⚠️  页面较长，将生成 {num_chunks} 个分块", flush=True)

    print(f"   📊 分块参数: 视口高度={viewport_height}px, 重叠={overlap}px, 分块高度={chunk_height}px", flush=True)

    for i in range(num_chunks):
        scroll_y = i * chunk_height

        # 滚动到位置
        await page.evaluate(f"window.scrollTo(0, {scroll_y})")

        # 等待滚动完成
        await page.wait_for_timeout(max(Config.LAZY_LOAD_SCROLL_WAIT, SCROLL_WAIT_MS))

        # 等待视口内的图片加载完成
        print(f"   ⏳ 等待分块 {i+1}/{num_chunks} 的图片加载...", flush=True)
        images_loaded = await wait_for_images_in_viewport(page, viewport_height, scroll_y)
        if not images_loaded:
            print(f"   ⚠️  分块 {i+1} 部分图片可能未完全加载，继续截图...", flush=True)

        # 额外等待动态内容（轮播图切换、动画等）
        if i == 0:  # 第一屏可能需要更多时间加载轮播图
            await page.wait_for_timeout(FIRST_SCREEN_WAIT_MS)
            # 再次检查第一屏的图片
            await wait_for_images_in_viewport(page, viewport_height, 0)
        else:
            # 其他分块也额外等待一下，确保懒加载图片有时间加载
            await page.wait_for_timeout(LAZY_LOAD_WAIT_MS)

        # 等待网络空闲（确保没有正在进行的请求）
        try:
            await page.wait_for_load_state("networkidle", timeout=2000)
        except Exception:
            pass  # 如果超时，继续截图

        chunk_path = Config.SCREENSHOT_DIR / f"{output_name}_pixel_{i+1}.jpg"
        await page.screenshot(path=str(chunk_path), type='jpeg', quality=Config.SCREENSHOT_QUALITY)

        # 计算实际覆盖范围
        chunk_bottom = min(scroll_y + viewport_height, total_height)

        screenshots.append({
            'path': str(chunk_path),
            'scroll_y': scroll_y,
            'scroll_bottom': chunk_bottom,
            'method': 'pixel'
        })
        print(f"   ✅ 像素分块 {i+1}/{num_chunks} (覆盖: {scroll_y}px - {chunk_bottom}px)", flush=True)

    # 验证是否完整覆盖
    last_bottom = screenshots[-1].get('scroll_bottom', 0) if screenshots else 0
    coverage = (last_bottom / total_height * 100) if total_height > 0 else 0
    print(f"   📊 覆盖范围: {last_bottom}/{total_height}px ({coverage:.1f}%)", flush=True)

    if coverage < 95:
        print(f"   ⚠️  警告: 页面覆盖不完整，可能遗漏了 {total_height - last_bottom}px 内容", flush=True)
    
    return {
        'title': page_info['title'],
        'total_height': total_height,
        'screenshots': screenshots,
        'method': method,
        'dom_sections': sections
    }, screenshots


async def analyze_page(url: str, output_name: Optional[str] = None) -> dict:
    """分析页面主函数
    
    Args:
        url: 要分析的页面URL
        output_name: 输出文件名（可选，默认从URL提取）
        
    Returns:
        dict: 分析报告字典
    """
    # 处理输出文件名
    if not output_name:
        raw_name = url.rstrip('/').split('/')[-1] or 'homepage'
    else:
        raw_name = output_name
    
    # 清理文件名
    output_name = sanitize_filename(raw_name)
    
    print("=" * 60, flush=True)
    print("🚀 页面分析（WordPress优化版）", flush=True)
    print(f"   URL: {url}", flush=True)
    print(f"   输出名称: {output_name}", flush=True)
    print(f"   视觉模型: {Config.VISION_MODEL}", flush=True)
    print("=" * 60, flush=True)
    
    # 清空 output 目录（保留 archive）
    print("\n🧹 清空 output 目录（保留 archive）...", flush=True)
    deleted_files, deleted_size = Config.cleanup_output(keep_archive=True)
    if deleted_files > 0:
        print(f"   ✅ 已删除 {deleted_files} 个文件 ({deleted_size / (1024*1024):.2f} MB)", flush=True)
    else:
        print(f"   ℹ️  output 目录已为空", flush=True)
    
    Config.ensure_dirs()
    
    # Step 1: 截图
    print(f"\n📸 智能截图: {url}", flush=True)
    
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = None
            page = None
            try:
                context = await browser.new_context(viewport={
                    'width': Config.VIEWPORT_WIDTH,
                    'height': Config.VIEWPORT_HEIGHT
                })
                page = await context.new_page()
                await page.goto(url, wait_until='networkidle', timeout=60000)
                await page.wait_for_timeout(ANIMATION_COMPLETE_WAIT_MS)

                page_info, screenshots = await capture_screenshots(page, output_name)
            finally:
                if page:
                    await page.close()
                if context:
                    await context.close()
            await browser.close()
    except Exception as e:
        print(f"\n❌ 截图失败: {e}", flush=True)
        raise
    
    # Step 2: 视觉分析
    print(f"\n🎨 分析页面结构...", flush=True)
    
    analyzer = VisionAnalyzer()
    chunks_analysis = []
    
    for i, screenshot_info in enumerate(screenshots):
        screenshot_path = screenshot_info['path']
        section_info = screenshot_info.get('section')
        
        # 获取上下文截图路径（从第二张开始提供上下文）
        prev_image_path = None
        next_image_path = None
        
        if i > 0:  # 从第二张开始，提供上一张作为上下文
            prev_image_path = screenshots[i-1]['path']
        
        if i < len(screenshots) - 1:  # 如果不是最后一张，提供下一张作为上下文
            next_image_path = screenshots[i+1]['path']
        
        context_info = ""
        if prev_image_path or next_image_path:
            context_parts = []
            if prev_image_path:
                context_parts.append("上一张")
            if next_image_path:
                context_parts.append("下一张")
            context_info = f"（含{'和'.join(context_parts)}上下文）"
        
        print(f"   [{i+1}/{len(screenshots)}] 分析分块{context_info}...", flush=True)
        try:
            analysis = analyzer.analyze_chunk(
                screenshot_path, i, len(screenshots), section_info,
                prev_image_path=prev_image_path,
                next_image_path=next_image_path
            )
            chunks_analysis.append(analysis)
            module_type = analysis.get('module_type', 'unknown')
            print(f"       ✅ {module_type}", flush=True)
        except KeyboardInterrupt:
            print("\n⚠️  用户中断分析", flush=True)
            raise
        except Exception as e:
            error_msg = str(e)
            print(f"       ❌ 分析失败: {error_msg[:100]}", flush=True)
            chunks_analysis.append({
                "error": error_msg,
                "screenshot": screenshot_path,
                "chunk_index": i
            })
        
        # 避免API限流（最后一个分块不需要等待）
        if i < len(screenshots) - 1:
            await asyncio.sleep(API_RATE_LIMIT_DELAY)
    
    # Step 3: 生成报告
    print(f"\n📦 生成分析报告...", flush=True)
    
    # 保存JSON分析结果
    analysis_report = {
        "url": url,
        "title": page_info['title'],
        "total_height": page_info['total_height'],
        "method": page_info['method'],
        "vision_model": Config.VISION_MODEL,
        "screenshots": [s['path'] for s in screenshots],
        "chunks": chunks_analysis
    }
    
    # 生成带模型后缀的文件名
    model_suffix = Config.get_model_suffix()
    json_path = Config.ANALYSIS_DIR / f"{output_name}_{model_suffix}.json"
    
    try:
        json_path.write_text(
            json.dumps(analysis_report, ensure_ascii=False, indent=2), 
            encoding='utf-8'
        )
        print(f"   ✅ JSON报告已保存", flush=True)
    except Exception as e:
        print(f"   ⚠️  JSON保存失败: {e}", flush=True)
    
    # 生成Cursor提示文件
    prompt_path = None
    try:
        prompt_content = generate_cursor_prompt_file(
            url=url,
            title=page_info['title'],
            total_height=page_info['total_height'],
            chunks=chunks_analysis,
            screenshot_dir=Config.SCREENSHOT_DIR,
            output_name=output_name
        )

        prompt_path = Config.ANALYSIS_DIR / f"{output_name}_{model_suffix}_prompt.md"
        prompt_path.write_text(prompt_content, encoding='utf-8')
        print(f"   ✅ Prompt文件已保存", flush=True)
    except Exception as e:
        print(f"   ⚠️  Prompt生成失败: {e}", flush=True)
    
    print("\n" + "=" * 60, flush=True)
    print("✅ 分析完成!", flush=True)
    print(f"   📸 截图: {Config.SCREENSHOT_DIR}/{output_name}_*.jpg", flush=True)
    print(f"   📊 分析: {json_path}", flush=True)
    if prompt_path:
        print(f"   📝 Prompt: {prompt_path}", flush=True)
    print(f"   🔧 方法: {page_info['method']}", flush=True)
    print(f"   📊 分块数: {len(screenshots)}", flush=True)
    print(f"   ✅ 成功分析: {sum(1 for c in chunks_analysis if 'error' not in c)}/{len(chunks_analysis)}", flush=True)
    print("=" * 60, flush=True)

    if prompt_path:
        print("\n" + "=" * 60, flush=True)
        print("👉 下一步：在Cursor中使用", flush=True)
        print(f"   @{prompt_path.name} @output/screenshots 根据分析生成WordPress模块代码", flush=True)
        print("=" * 60, flush=True)
    
    # 归档文件
    archive_files(url, output_name)
    
    return analysis_report


async def main() -> None:
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python scripts/analyze.py <url> [output_name]")
        print("\n示例:")
        print("  python scripts/analyze.py https://example.com/products")
        print("  python scripts/analyze.py https://example.com/products my-products")
        sys.exit(1)
    
    url = sys.argv[1]
    output_name = sys.argv[2] if len(sys.argv) > 2 else None
    
    # 验证URL格式
    if not url.startswith(('http://', 'https://')):
        print(f"❌ 无效的URL格式: {url}")
        print("   请使用完整的URL，例如: https://example.com")
        sys.exit(1)
    
    # 验证配置
    errors = Config.validate()
    if errors:
        print("\n❌ 配置错误:")
        for error in errors:
            print(f"   - {error}")
        print("\n请在 .env 文件中设置相关配置")
        sys.exit(1)
    
    try:
        await analyze_page(url, output_name)
    except KeyboardInterrupt:
        print("\n\n⚠️  用户中断操作", flush=True)
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ 分析失败: {e}", flush=True)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
    