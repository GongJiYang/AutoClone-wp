"""
Prompt 模板管理 - 优化版
整合视觉分析和WordPress代码生成的提示词

优化内容：
- 精简prompt长度，提升token效率
- 添加few-shot示例，提升输出质量
- 改进上下文利用机制
- 添加结构化输出支持
- 拆分核心要求与详细规范
"""

# WordPress 模块类型映射
MODULE_TYPES = {
    "header": "页面头部导航",
    "hero": "主视觉横幅区域",
    "hero-carousel": "轮播图横幅",
    "features": "特色/优势展示",
    "features-service": "服务特色",
    "product-grid": "产品网格展示",
    "product-carousel": "产品轮播",
    "why-choose": "为什么选择我们",
    "project-cases": "项目案例",
    "testimonials": "客户评价",
    "cta": "行动号召区域",
    "contact-form": "联系表单",
    "footer": "页面底部",
    "content-block": "内容块",
    "image-text": "图文混排",
    "gallery": "图片画廊",
    "faq": "常见问题",
    "stats": "数据统计",
    "team": "团队展示",
    "pricing": "价格表",
    "timeline": "时间线",
    "logo-cloud": "合作伙伴Logo",
}

# Few-shot 示例库
FEWSHOT_EXAMPLES = {
    "hero": """{
    "module_type": "hero",
    "module_name_suggestion": "kitchen-cabinets-hero",
    "is_common_module": true,
    "layout": {
        "container": "container-1200",
        "type": "flex",
        "columns": 2,
        "rows": 1,
        "gap_horizontal": "30px",
        "gap_vertical": "0",
        "alignment": "space-between",
        "direction": "row"
    },
    "colors": {
        "background": "#ffffff",
        "primary": "#FF8C00",
        "secondary": "#333333",
        "heading": "#222222",
        "text": "#666666",
        "border": "none"
    },
    "typography": {
        "heading_size": "36px",
        "heading_weight": "700",
        "body_size": "16px",
        "body_weight": "400",
        "line_height": "1.6"
    },
    "spacing": {
        "padding_top": "80px",
        "padding_bottom": "80px",
        "padding_left": "15px",
        "padding_right": "15px",
        "element_margin": "30px",
        "card_padding": "20px"
    },
    "components": [
        {
            "type": "heading",
            "count": 1,
            "width": "auto",
            "height": "auto",
            "border_radius": "0",
            "has_shadow": false,
            "has_border": false,
            "details": "主标题'Acrylic Kitchen Cabinets'，深灰色（#222222），加粗700"
        },
        {
            "type": "paragraph",
            "count": 2,
            "width": "auto",
            "height": "auto",
            "border_radius": "0",
            "has_shadow": false,
            "has_border": false,
            "details": "两个段落，描述丙烯酸厨房橱柜的项目需求及服务内容"
        },
        {
            "type": "button",
            "count": 1,
            "width": "auto",
            "height": "40px",
            "border_radius": "4px",
            "has_shadow": false,
            "has_border": false,
            "details": "橙色背景（#FF8C00），白色文字，'Get a Free Quote →'"
        }
    ],
    "images": [
        {
            "type": "hero-banner",
            "count": 1,
            "width": "50%",
            "height": "auto",
            "aspect_ratio": "auto",
            "position": "右侧",
            "object_fit": "cover",
            "has_overlay": false,
            "overlay_color": "none",
            "placeholder_suggestion": "gray-bg"
        }
    ],
    "extracted_content": {
        "main_title": "Acrylic Kitchen Cabinets",
        "subtitle": "",
        "paragraphs": [
            "For your project, do you require acrylic kitchen cabinets? You've undoubtedly heard of \"acrylic kitchen cabinets\" and are now interested in learning more.",
            "At George, we will explore acrylic cabinets, outlining their advantages and disadvantages to assist you in making an informed decision for your kitchen renovation."
        ],
        "button_texts": ["Get a Free Quote →"],
        "list_items": [],
        "card_contents": []
    },
    "responsive_hints": "平板设备（≤768px）下，主内容区域改为单列布局，图片占满宽度；移动端（≤480px）按钮文字简化为'Quote'",
    "content_summary": "页面顶部hero区域，核心展示丙烯酸厨房橱柜的主题信息，包含主标题、项目需求描述、服务说明及行动号召按钮",
    "special_effects": "按钮hover时背景色加深至#E67300"
}""",

    "product-grid": """{
    "module_type": "product-grid",
    "module_name_suggestion": "acrylic-kitchen-cabinets-grid",
    "is_common_module": true,
    "layout": {
        "container": "container-1200",
        "type": "grid",
        "columns": 3,
        "rows": 2,
        "gap_horizontal": "20px",
        "gap_vertical": "30px",
        "alignment": "left",
        "direction": "row"
    },
    "colors": {
        "background": "#ffffff",
        "primary": "#FF8C00",
        "secondary": "#333333",
        "heading": "#333333",
        "text": "#666666",
        "border": "#e0e0e0"
    },
    "typography": {
        "heading_size": "18px",
        "heading_weight": "700",
        "body_size": "14px",
        "body_weight": "400",
        "line_height": "1.6"
    },
    "spacing": {
        "padding_top": "80px",
        "padding_bottom": "80px",
        "padding_left": "15px",
        "padding_right": "15px",
        "element_margin": "30px",
        "card_padding": "20px"
    },
    "components": [
        {
            "type": "card",
            "count": 6,
            "width": "auto",
            "height": "auto",
            "border_radius": "8px",
            "has_shadow": true,
            "has_border": false,
            "details": "白色卡片，带轻微阴影，包含产品图片、标题和简短描述"
        }
    ],
    "images": [
        {
            "type": "product",
            "count": 6,
            "width": "100%",
            "height": "200px",
            "aspect_ratio": "16:9",
            "position": "卡片顶部",
            "object_fit": "cover",
            "has_overlay": false,
            "overlay_color": "none",
            "placeholder_suggestion": "gray-bg"
        }
    ],
    "extracted_content": {
        "main_title": "",
        "subtitle": "",
        "paragraphs": [],
        "button_texts": [],
        "list_items": [],
        "card_contents": [
            {"title": "White Acrylic Kitchen Cabinet", "description": "Acrylic Kitchen Cabinet Supplier & Manufacturer", "link_text": ""},
            {"title": "Solid Acrylic Kitchen Cabinet Doors", "description": "Solid Acrylic Kitchen Cabinet Doors Acrylic cabinets are available in a wide range of colors", "link_text": ""},
            {"title": "Modern Acrylic Kitchen Cabinets", "description": "Extended sunshine exposure will have a significant impact on the color of acrylic kitchen cabinets", "link_text": ""}
        ]
    },
    "responsive_hints": "平板设备显示2列，移动端设备显示1列",
    "content_summary": "该区域主要展示6种不同类型的亚克力厨房橱柜产品，每个产品包含高清图片、标题及简短功能描述",
    "special_effects": "卡片带有轻微阴影效果，hover时可能触发阴影加深或缩放动画"
}"""
}

# 视觉模型分析 Prompt（优化版 - 精简且高效）
VISION_ANALYZE_PROMPT = """你是WordPress主题开发专家和UI分析师。分析这个网页截图分块。

## 位置信息
{position}
{dom_hint}
{context_hint}

## 任务要求（核心）

### 1. 精确性要求（重要）
- **数量精确**：如"6个卡片"，不是"多个"
- **像素精确**：如"36px"，不是"较大"
- **颜色精确**：如"#FF8C00"，不是"橙色"
- **文字提取**：提取所有可见文字用于默认数据

### 2. 上下文理解
{context_guidance}

### 3. 模块类型参考
{module_types_hint}

## 输出JSON格式

```json
{{
    "module_type": "模块类型（hero/product-grid/features等）",
    "module_name_suggestion": "建议的模块文件名（如kitchen-cabinets-hero）",
    "is_common_module": true/false,
    "layout": {{
        "container": "full-width/container-1200/container-1400",
        "type": "grid/flex/block",
        "columns": 具体数字,
        "rows": 具体数字,
        "gap_horizontal": "具体像素值如20px",
        "gap_vertical": "具体像素值如30px",
        "alignment": "left/center/right/space-between",
        "direction": "row/column"
    }},
    "colors": {{
        "background": "#具体hex值",
        "primary": "#具体hex值（按钮颜色等）",
        "secondary": "#具体hex值",
        "heading": "#具体hex值",
        "text": "#具体hex值",
        "border": "#具体hex值或none"
    }},
    "typography": {{
        "heading_size": "具体像素值如36px",
        "heading_weight": "具体数值如700",
        "body_size": "具体像素值如16px",
        "body_weight": "具体数值如400",
        "line_height": "具体数值如1.6"
    }},
    "spacing": {{
        "padding_top": "具体像素值如80px",
        "padding_bottom": "具体像素值如80px",
        "padding_left": "具体像素值如15px",
        "padding_right": "具体像素值如15px",
        "element_margin": "元素间距如30px",
        "card_padding": "卡片内边距如20px"
    }},
    "components": [
        {{
            "type": "navbar/logo/button/card/image/text/form/icon/badge/divider",
            "count": 精确数量,
            "width": "具体尺寸如200px或auto",
            "height": "具体尺寸如150px或auto",
            "border_radius": "圆角值如8px或0",
            "has_shadow": true/false,
            "has_border": true/false,
            "details": "具体描述（如：白色卡片，带阴影，显示产品图片和标题）"
        }}
    ],
    "images": [
        {{
            "type": "hero-banner/product/thumbnail/avatar/icon/background/gallery",
            "count": 精确数量,
            "width": "具体像素或百分比如300px或100%",
            "height": "具体像素或auto如200px",
            "aspect_ratio": "宽高比如16:9/4:3/1:1/auto",
            "position": "位置描述如左侧/居中/网格排列",
            "object_fit": "cover/contain/fill",
            "has_overlay": true/false,
            "overlay_color": "#rgba值或none",
            "placeholder_suggestion": "占位符建议如gray-bg/gradient/svg-icon"
        }}
    ],
    "extracted_content": {{
        "main_title": "截图中的主标题文字",
        "subtitle": "副标题文字",
        "paragraphs": ["段落1完整内容...", "段落2完整内容..."],
        "button_texts": ["按钮文字1", "按钮文字2"],
        "list_items": [
            {{"title": "列表项标题", "description": "列表项描述"}}
        ],
        "card_contents": [
            {{"title": "卡片标题", "description": "卡片描述", "link_text": "链接文字"}}
        ]
    }},
    "responsive_hints": "响应式建议（如：平板2列，移动端1列）",
    "content_summary": "该区域主要展示什么内容",
    "special_effects": "特殊效果（如：hover变色、渐变背景、动画等）"
}}
```

## 输出示例

{few_shot_example}

## 重要提醒

⚠️ **只输出JSON，不要其他内容**
⚠️ **数量必须是精确数字**
⚠️ **颜色必须是hex值（#开头）**
⚠️ **必须提取截图中所有可见文字**
"""


# 生成给Cursor的完整Prompt模板（优化版）
CURSOR_PROMPT_TEMPLATE = """# WordPress 页面克隆任务

## ⚠️ 核心要求（必须满足）

1. **默认数据必须从截图提取真实内容** - 不可为空或使用占位符
2. **每个模块独立PHP文件** - `modules/{{module-name}}.php`
3. **完整的响应式CSS** - 4个断点（桌面/平板/移动/小屏）
4. **图片占位符使用placehold.co** - `https://placehold.co/600x400/e0e0e0/666?text=Product`

---

## 原始页面信息
- URL: {url}
- 标题: {title}
- 总高度: {total_height}px

---

## 页面结构分析

{sections_analysis}

---

## 设计参数汇总

{design_tokens}

---

## 代码规范（详细）

### PHP模块结构
```php
<?php
if (!defined('ABSPATH')) {{
    exit;
}}

$module_args = isset($args) ? $args : array();

// ========== 默认数据（从截图提取）==========
$default_title = '从截图提取的实际标题';
$default_content = '<p>从截图提取的描述内容，至少2-3句完整文字。</p>';
$default_items = array(
    array(
        'title' => '从截图提取的项目1标题',
        'description' => '从截图提取的项目1描述',
        'icon' => 'icon-class-1'
    ),
    array(
        'title' => '从截图提取的项目2标题',
        'description' => '从截图提取的项目2描述',
        'icon' => 'icon-class-2'
    )
);

// ========== 获取参数（带默认值）==========
$title = isset($module_args['title']) ? $module_args['title'] : $default_title;
$content = isset($module_args['content']) ? $module_args['content'] : $default_content;
$items = !empty($module_args['items']) ? $module_args['items'] : $default_items;

// ========== 输出HTML ==========
?>
<div class="{{module-name}}-module">
    <div class="elementor-container">
        <h2 class="module-title"><?php echo esc_html($title); ?></h2>
        <div class="module-content"><?php echo wp_kses_post($content); ?></div>

        <?php if (!empty($items)) : ?>
        <div class="module-items">
            <?php foreach ($items as $item) : ?>
            <div class="module-item">
                <h3><?php echo esc_html($item['title']); ?></h3>
                <p><?php echo esc_html($item['description']); ?></p>
            </div>
            <?php endforeach; ?>
        </div>
        <?php endif; ?>
    </div>
</div>
```

### CSS样式结构
```css
.{{module-name}}-module {{
    padding: 80px 0;
    background-color: #fff;
}}

.{{module-name}}-module .elementor-container {{
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 15px;
}}

.{{module-name}}-module .module-title {{
    font-size: 36px;
    font-weight: 700;
    color: #333;
    margin-bottom: 20px;
}}

/* 响应式 */
@media (max-width: 1024px) {{
    .{{module-name}}-module .module-title {{
        font-size: 32px;
    }}
}}

@media (max-width: 768px) {{
    .{{module-name}}-module {{
        padding: 40px 0;
    }}

    .{{module-name}}-module .module-title {{
        font-size: 28px;
    }}
}}

@media (max-width: 480px) {{
    .{{module-name}}-module .module-title {{
        font-size: 24px;
    }}
}}
```

### 设计系统
- 字体：`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`
- 主色调：`#FF8C00` / `#FF7A00`（橙色）
- 文字颜色：标题 `#333`，正文 `#666`
- 容器内边距：`padding: 0 15px`
- 模块间距：通常 `padding: 80px 0`（移动端40px）

---

## 图片占位符规范

### 方式1：placehold.co（推荐）
```html
<img src="https://placehold.co/600x400/e0e0e0/666?text=Product+Name" alt="产品名称">
```

### 方式2：CSS占位符
```css
.image-placeholder {{
    background: linear-gradient(135deg, #f0f0f0 0%, #e0e0e0 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #999;
    font-size: 14px;
    aspect-ratio: 16/9;
}}
```

---

## ✅ 验证清单

生成代码后，请检查：
- [ ] 所有模块都有从截图提取的有意义的默认数据（不为空）
- [ ] 图片占位符使用placehold.co，尺寸匹配
- [ ] 响应式CSS包含4个断点（1024px, 768px, 480px）
- [ ] 所有输出使用`esc_html()`或`esc_url()`进行转义
- [ ] 模块可以独立运行（不依赖外部数据）
- [ ] 文件名使用建议的模块名（如`kitchen-cabinets-hero`）

---

## 截图参考

请查看 `output/screenshots/` 目录下的分块截图：
{screenshot_list}

---

## 🎯 推荐输出方式：WordPress 页面模板

### 页面模板文件
**位置**: `wp-content/themes/{{theme-name}}/page-templates/template-{{page-name}}.php`

```php
<?php
/**
 * Template Name: {{Page Name}} 页面模板
 * Description: 克隆自 {url}
 */

if (!defined('ABSPATH')) {{
    exit;
}}

get_header();
?>

<main class="page-{{page-slug}}">

    <!-- ========== Section 1: Hero ========== -->
    <section class="hero-section">
        <div class="elementor-container">
            <?php
            $hero_title = '从截图提取的标题';
            $hero_subtitle = '从截图提取的副标题';
            $hero_button_text = '从截图提取的按钮文字';
            ?>
            <div class="hero-content">
                <h1><?php echo esc_html($hero_title); ?></h1>
                <p class="hero-subtitle"><?php echo esc_html($hero_subtitle); ?></p>
                <a href="#contact" class="btn btn-primary">
                    <?php echo esc_html($hero_button_text); ?>
                </a>
            </div>
            <div class="hero-image">
                <img src="https://placehold.co/800x600/e0e0e0/666?text=Hero+Image" alt="Hero Banner">
            </div>
        </div>
    </section>

    <!-- ========== Section 2: Product Grid ========== -->
    <section class="product-grid-section">
        <div class="elementor-container">
            <?php
            $section_title = '从截图提取的标题';
            $products = array(
                array(
                    'title' => '从截图提取的产品1',
                    'description' => '从截图提取的描述',
                    'image' => 'https://placehold.co/400x300/e0e0e0/666?text=Product+1'
                ),
                array(
                    'title' => '从截图提取的产品2',
                    'description' => '从截图提取的描述',
                    'image' => 'https://placehold.co/400x300/e0e0e0/666?text=Product+2'
                )
            );
            ?>
            <h2 class="section-title"><?php echo esc_html($section_title); ?></h2>
            <div class="products-grid">
                <?php foreach ($products as $product) : ?>
                <div class="product-card">
                    <img src="<?php echo esc_url($product['image']); ?>" alt="<?php echo esc_attr($product['title']); ?>">
                    <h3><?php echo esc_html($product['title']); ?></h3>
                    <p><?php echo esc_html($product['description']); ?></p>
                </div>
                <?php endforeach; ?>
            </div>
        </div>
    </section>

</main>

<?php get_footer(); ?>
```

### 配套CSS文件
**位置**: `wp-content/themes/{{theme-name}}/assets/css/template-{{page-name}}.css`

```css
/* ========== Page Template: {{Page Name}} ========== */

.page-{{page-slug}} {{
    /* 页面全局样式 */
}}

/* Hero Section */
.hero-section {{
    padding: 80px 0;
    background: #f8f8f8;
}}

.hero-section .elementor-container {{
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 15px;
    display: flex;
    align-items: center;
    gap: 40px;
}}

.hero-content {{
    flex: 1;
}}

.hero-content h1 {{
    font-size: 48px;
    font-weight: 700;
    color: #333;
    margin-bottom: 20px;
}}

/* Product Grid Section */
.product-grid-section {{
    padding: 80px 0;
    background: #fff;
}}

.products-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
}}

.product-card {{
    background: #fff;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}}

/* 响应式 */
@media (max-width: 1024px) {{
    .products-grid {{
        grid-template-columns: repeat(2, 1fr);
    }}
}}

@media (max-width: 768px) {{
    .hero-section .elementor-container {{
        flex-direction: column;
    }}

    .products-grid {{
        grid-template-columns: 1fr;
    }}

    .hero-content h1 {{
        font-size: 32px;
    }}
}}
```

### 在functions.php中注册样式

```php
function enqueue_page_template_styles() {{
    if (is_page_template('page-templates/template-{{page-name}}.php')) {{
        wp_enqueue_style(
            'template-{{page-name}}-style',
            get_template_directory_uri() . '/assets/css/template-{{page-name}}.css',
            array(),
            '1.0.0'
        );
    }}
}}
add_action('wp_enqueue_scripts', 'enqueue_page_template_styles');
```

---

## 使用方式

1. 将PHP模板文件放入 `wp-content/themes/your-theme/page-templates/`
2. 将CSS文件放入 `wp-content/themes/your-theme/assets/css/`
3. 在`functions.php`中添加样式注册代码
4. WordPress后台 → 页面 → 新建页面
5. 选择页面模板并发布
"""


def get_module_types_hint():
    """获取模块类型提示"""
    hints = []
    for key, desc in MODULE_TYPES.items():
        hints.append(f"- {key}: {desc}")
    return "\n".join(hints)


def format_vision_prompt(position: str, dom_hint: str = "", context_hint: str = "",
                         has_context: bool = False) -> str:
    """格式化视觉分析prompt（优化版）

    Args:
        position: 位置描述
        dom_hint: DOM信息提示
        context_hint: 上下文信息提示
        has_context: 是否有上下文图片

    Returns:
        格式化后的prompt
    """
    # 选择合适的few-shot示例
    module_types_hint = get_module_types_hint()

    # 生成上下文指导
    if has_context:
        context_guidance = """
**如何使用上下文图片**：
- **上一张截图**：帮助你理解当前内容的延续性，可能包含当前模块的起始部分
- **下一张截图**：帮助你预览后续内容，判断当前模块是否结束
- **重叠区域**：当前截图可能与上下截图有重叠，这是正常的（用于确保完整覆盖）
- **模块边界**：结合上下文判断当前截图是独立模块还是某模块的一部分

**分析策略**：
1. 先看当前截图的主要内容和结构
2. 结合上一张判断是否有延续关系
3. 结合下一张判断模块是否结束
4. 如果当前截图包含上一个模块的结尾，请标注出来
"""
    else:
        context_guidance = "当前是独立分块，无上下文参考。"

    # 选择一个示例（优先hero或product-grid）
    few_shot_example = FEWSHOT_EXAMPLES.get("hero", FEWSHOT_EXAMPLES.get("product-grid", ""))

    return VISION_ANALYZE_PROMPT.format(
        position=position,
        dom_hint=dom_hint,
        context_hint=context_hint,
        context_guidance=context_guidance,
        module_types_hint=module_types_hint,
        few_shot_example=few_shot_example
    )


def format_cursor_prompt(url: str, title: str, total_height: int,
                         sections_analysis: str, design_tokens: str,
                         screenshot_list: str) -> str:
    """格式化Cursor prompt（优化版）

    Args:
        url: 页面URL
        title: 页面标题
        total_height: 页面总高度
        sections_analysis: 页面结构分析
        design_tokens: 设计参数
        screenshot_list: 截图列表

    Returns:
        格式化后的prompt
    """
    return CURSOR_PROMPT_TEMPLATE.format(
        url=url,
        title=title,
        total_height=str(total_height),  # 确保是字符串
        sections_analysis=sections_analysis,
        design_tokens=design_tokens,
        screenshot_list=screenshot_list
    )
