# WordPress 页面克隆任务

## 原始页面信息
- URL: https://georgeconstructions.com/products/
- 标题: George Group: One-stop solution for Residential & Commercial building materials
- 总高度: 4486px

## 代码规范

### PHP模块结构
- 文件位置：`modules/{module-name}.php`
- 使用 `.elementor-container` 作为容器（最大宽度1200px）
- 模块最外层类名：`{module-name}-module`
- 使用 `esc_html()` 和 `esc_url()` 进行输出转义
- 使用 `get_svg_placeholder()` 函数处理图片占位符

### CSS样式结构
- 文件位置：`assets/css/modules/{module-name}.css`
- 使用模块化的类名（避免全局冲突）
- 必须包含响应式设计：
  - 桌面：默认（>1024px）
  - 平板：`@media (max-width: 1024px)`
  - 移动：`@media (max-width: 768px)`
  - 小屏：`@media (max-width: 480px)`

### 设计系统
- 字体：`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`
- 主色调：`#FF8C00` / `#FF7A00`（橙色）
- 文字颜色：标题 `#333`，正文 `#666`
- 容器内边距：`padding: 0 15px`
- 模块间距：通常 `padding: 80px 0`（移动端减少为40px）

### ⚠️ 默认数据规范（重要）

**每个模块必须提供有意义的默认示例数据**，确保页面在没有传入参数时也能正常显示：

```php
// ❌ 错误写法 - 空默认值（页面会显示空白）
$title = isset($module_args['title']) ? $module_args['title'] : '';
$content = isset($module_args['content']) ? $module_args['content'] : '';

// ✅ 正确写法 - 提供有意义的默认数据
$title = isset($module_args['title']) ? $module_args['title'] : 'Best Patio Floor Tiles for Your Outdoor Space';
$content = isset($module_args['content']) ? $module_args['content'] : '<p>Transform your patio with our selection of premium floor tiles. From natural stone to modern porcelain, find the perfect option for your outdoor living area.</p>';
```

**默认数据要求：**
1. **标题**：必须有默认值，使用从截图中提取的实际标题或合理的占位文本
2. **正文内容**：必须有默认值，至少2-3句描述性文字
3. **列表类数据**：必须提供2-3个默认项目，每项包含标题和描述
4. **按钮文字**：使用实际的CTA文案如"View Products"、"Learn More"
5. **图片Alt**：提供有意义的描述性alt文本

### 图片占位符规范
使用以下方式处理图片占位符：

```php
// 方式1：使用WordPress占位符函数
<?php echo get_svg_placeholder($width, $height, $text); ?>

// 方式2：使用CSS背景色占位
<div class="image-placeholder" style="aspect-ratio: 16/9; background: #e0e0e0;"></div>

// 方式3：使用placehold.co（推荐）
<img src="https://placehold.co/600x400/e0e0e0/666?text=Product" alt="产品图片">
```

图片占位符CSS示例：
```css
.image-placeholder {
    background: linear-gradient(135deg, #f0f0f0 0%, #e0e0e0 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #999;
    font-size: 14px;
}
```

## 页面结构分析

### 分块 1: hero
- **截图**: `products_pixel_1.jpg`
- **建议模块名**: `home-hero`

**布局**:
- 容器: full-width
- 类型: block
- 列数: 1, 行数: 1
- 水平间距: 0px, 垂直间距: 0px
- 对齐: left

**颜色**:
- 背景: #FFFFFF
- 主色: #FF8C00
- 标题: #FFFFFF
- 正文: #FFFFFF
- 边框: none

**字体**:
- 标题: 36px, 字重: 700
- 正文: 18px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 20px
- 卡片内边距: 0px

**组件** (5个):
  - logo x1, 宽=auto, 高=auto, 圆角=0
    说明: 品牌logo，显示‘George’文字，位于导航栏左侧
  - nav-item x7, 宽=auto, 高=auto, 圆角=0
    说明: 导航链接，包括‘Products’、‘Projects’、‘Blog’、‘Service’、‘Video’、‘About’、‘Contact’，位于导航栏中间
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 橙色按钮，文字‘Quick Quote’，位于导航栏右侧
  - text x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题，文字‘TOP BRAND IN THE WORLD’，位于hero区域左侧
  - text x1, 宽=auto, 高=auto, 圆角=0
    说明: 副标题，文字‘For Whole House Customization’，位于主标题下方

**图片占位符** (1组):
  - **hero-banner** x1
    尺寸: 100% x auto, 比例: 16:9
    位置: center, object-fit: cover
    遮罩: rgba(0,0,0,0.3)
    占位符建议: gradient-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `TOP BRAND IN THE WORLD`
- **副标题**: `For Whole House Customization`
- **按钮文字**: `Quick Quote`

**响应式**: 平板端（768px-1024px）：导航栏调整为2行，‘Quick Quote’按钮移至下方；移动端（<768px）：导航栏隐藏，显示汉堡菜单，hero区域padding_top和padding_bottom调整为40px
**特效**: 导航项‘Products’ hover 时变为橙色（#FF8C00），其他导航项 hover 时变为深灰色（#666666）；‘Quick Quote’按钮 hover 时背景色加深至#E67E00；hero背景图片带有半透明黑色叠加层，增强文字可读性
**内容摘要**: 该区域作为主视觉横幅，通过高质量室内设计图片展示品牌形象，突出‘世界顶级品牌’定位，传递全屋定制服务的核心价值

---

### 分块 2: product-grid
- **截图**: `products_pixel_2.jpg`
- **建议模块名**: `whole-house-customization-grid`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 5, 行数: 2
- 水平间距: 20px, 垂直间距: 30px
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #f97316
- 标题: #2d3748
- 正文: #4a5568
- 边框: none

**字体**:
- 标题: 36px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - card x10, 宽=220px, 高=180px, 圆角=0
    说明: 白色卡片，包含产品图片和标题文字，无阴影和边框

**图片占位符** (1组):
  - **product** x10
    尺寸: 220px x 180px, 比例: 16:9
    位置: 网格排列（5列2行）, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Whole House Customization`
- **副标题**: `See how George improves the living areas and useful spaces in a whole-house design to be inspired.`
- **按钮文字**: `Get a Free Quote`
- **卡片内容** (10个):
  - `Kitchen Cabinets`: ...
  - `Wardrobe`: ...
  - `Doors & Windows`: ...

**响应式**: 平板设备（768px-1024px）显示3列，移动端（<768px）显示1列
**特效**: 无可见特殊效果（如hover动画、渐变等）
**内容摘要**: 展示全屋定制中的各类产品，包括厨房橱柜、衣柜、门窗、卫浴用品、木地板、照明、家具、软装饰、瓷砖及全屋解决方案

---

### 分块 3: features-service
- **截图**: `products_pixel_3.jpg`
- **建议模块名**: `design-service-features`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 20px, 垂直间距: 30px
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #333333
- 正文: #666666
- 边框: #e0e0e0

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (2个):
  - button x1, 宽=120px, 高=40px, 圆角=4px
    说明: 橙色背景按钮，显示'Get a Free Quote'文字
  - card x4, 宽=auto, 高=auto, 圆角=0
    说明: 白色卡片，包含标题和描述文字，均匀排列

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **段落** (2个):
  - `George delivers professionalism and dependability, focused on fulfilling your engineering requiremen...`
  - `Feel free to come and visit George Group's main showroom, which spans over 20,000 square meters. Bel...`
- **按钮文字**: `Get a Free Quote`
- **卡片内容** (4个):
  - `Design Service`: Receive complimentary interior design service to c...
  - `0+`: Receive complimentary interior design service to c...
  - `0+`: Designers are ready with their newest design ideas...

**响应式**: 平板设备显示2列，移动端显示1列
**特效**: 无明显的特殊效果，可能包含按钮hover变色或卡片hover效果
**内容摘要**: 该区域主要展示设计服务的特色，包括免费设计服务、设计师的创意和定制化解决方案，以及行动号召按钮

---

### 分块 4: timeline
- **截图**: `products_pixel_4.jpg`
- **建议模块名**: `order-procedures-timeline`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 4, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #333333
- 正文: #666666
- 边框: none

**字体**:
- 标题: 36px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - icon/text x4, 宽=auto, 高=auto, 圆角=50px
    说明: 每个步骤包含一个圆形橙色图标（放大镜、报价单、对勾、货车）和对应的文字，图标位于左侧，文字位于右侧，整体居中对齐

**图片占位符** (1组):
  - **icon** x4
    尺寸: 50px x 50px, 比例: 1:1
    位置: 每个步骤左侧, object-fit: contain
    占位符建议: orange-circle-icon

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Order Procedures`
- **段落** (1个):
  - `Feel free to come and visit George Group's main showroom, which spans over 20,000 square meters. Bel...`
- **按钮文字**: `Get a Free Quote`

**响应式**: 平板设备（768px-1024px）显示2列，移动端设备（<768px）显示1列
**特效**: 图标和按钮使用橙色作为主色调，按钮 hover 时可能触发背景色加深或文字颜色变化（如变为白色）
**内容摘要**: 该区域主要展示George Group的订单流程，通过四个步骤（询价、设计报价、订单确认生产、交付运输）清晰呈现业务流程，配合橙色图标增强视觉引导

---

### 分块 5: contact-form
- **截图**: `products_pixel_5.jpg`
- **建议模块名**: `get-a-free-quote-form`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0px
- 对齐: space-between

**颜色**:
- 背景: #f8f9fa
- 主色: #6c757d
- 标题: #212529
- 正文: #495057
- 边框: #dee2e6

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 15px
- 卡片内边距: 20px

**组件** (5个):
  - input x5, 宽=100%, 高=40px, 圆角=4px
    说明: 表单输入框，包括Name、Email、Tel/Whatsapp、City、Country-Select
  - checkbox x9, 宽=auto, 高=auto
    说明: 产品需要的复选框选项（Kitchen cabinet、Bedroom等）
  - textarea x1, 宽=100%, 高=120px, 圆角=4px
    说明: Message文本框
  - file-upload x1, 宽=auto, 高=auto
    说明: Choose File文件上传按钮
  - button x1, 宽=100%, 高=50px, 圆角=4px
    说明: Send提交按钮

**图片占位符** (1组):
  - **background** x1
    尺寸: 45% x auto, 比例: 16:9
    位置: 左侧, object-fit: cover
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Get A Free Quote`
- **副标题**: `Kindly send us your project details and floor plan. We will quote for you within 8 hours!`
- **按钮文字**: `Send`
- **列表项** (10个):
  - `Kitchen cabinet`: ...
  - `Bedroom`: ...
  - `Bathroom`: ...

**响应式**: 平板端（768px-1024px）改为2列布局，移动端（<768px）改为1列布局，表单元素垂直堆叠
**特效**: 按钮hover时背景色加深（#5a6268），输入框focus时边框颜色变为#6c757d
**内容摘要**: 该区域为联系表单模块，用于用户提交项目详情以获取免费报价，包含输入框、复选框、文本框、文件上传和提交按钮

---

### 分块 6: footer
- **截图**: `products_pixel_6.jpg`
- **建议模块名**: `footer-with-four-columns`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 20px, 垂直间距: 30px
- 对齐: left

**颜色**:
- 背景: #000000
- 主色: #6c757d
- 标题: #ffffff
- 正文: #cccccc
- 边框: none

**字体**:
- 标题: 18px, 字重: 700
- 正文: 14px, 字重: 400
- 行高: 1.5

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 20px
- 卡片内边距: 0

**组件** (4个):
  - button x2, 宽=auto, 高=40px, 圆角=0
    说明: 深灰色按钮，显示'Send'文字
  - input x2, 宽=200px, 高=40px, 圆角=0
    说明: 白色输入框，显示占位符文字'whatsapp'和'Email*'
  - icon x3, 宽=16px, 高=16px, 圆角=0
    说明: 橙色图标，分别代表邮件、电话、whatsapp
  - link x21, 宽=auto, 高=auto, 圆角=0
    说明: 浅灰色链接文字，显示各列下的产品、解决方案、服务、联系方式

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **段落** (1个):
  - `Don't miss our future updates! Get Subscribed Today!`
- **按钮文字**: `Send`, `Send`
- **列表项** (4个):
  - `Products`: Kitchen Cabinet, Wardrobe, Windows and Doors, Bath...
  - `One-Stop Solutions`: Hotel Solutions, Resort Solutions, Villa Solutions...
  - `Customer Services`: Measurement Guidance, Packaging Info, Delivery & S...

**响应式**: 平板设备显示2列，移动端显示1列
**特效**: 无
**内容摘要**: 该区域主要展示产品分类、一站式解决方案、客户服务及联系方式，包含订阅表单

---


## 设计参数汇总

### 颜色系统（CSS变量建议）
```css
:root {
    --color-primary: #6c757d;
    --color-secondary: #cccccc;
    --color-background: #000000;
    --color-heading: #ffffff;
    --color-text: #cccccc;
    --color-border: #dee2e6;
}
```

### 字体系统
```css
:root {
    --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    --font-size-h1: 18px;
    --font-size-body: 14px;
    --font-weight-heading: 700;
    --font-weight-body: 400;
    --line-height: 1.5;
}
```

### 间距系统
```css
:root {
    --spacing-module-top: 80px;
    --spacing-module-bottom: 80px;
    --spacing-element: 20px;
    --spacing-card-padding: 0;
    --container-max-width: 1200px;
    --container-padding: 15px;
}
```

### 响应式断点
```css
/* 桌面 */
@media (min-width: 1025px) { }

/* 平板 */
@media (max-width: 1024px) {
    :root {
        --spacing-module-top: 60px;
        --spacing-module-bottom: 60px;
    }
}

/* 移动 */
@media (max-width: 768px) {
    :root {
        --spacing-module-top: 40px;
        --spacing-module-bottom: 40px;
        --font-size-h1: 28px;
    }
}
```


## 任务要求

请根据上述分析和截图，为每个模块生成：

1. **PHP文件** (`modules/{module-name}.php`)
2. **CSS文件** (`assets/css/modules/{module-name}.css`)
3. **模块参数** (`$args` 数组结构)

### PHP代码模板（包含默认数据示例）

```php
<?php
if (!defined('ABSPATH')) {
    exit;
}

$module_args = isset($args) ? $args : array();

// ========== 默认数据（必须提供有意义的内容）==========
$default_title = 'Module Title from Screenshot';
$default_content = '<p>This is meaningful default content extracted from the original page screenshot. It should describe what this section is about and provide value even without custom data.</p>';
$default_items = array(
    array(
        'title' => 'Feature One',
        'description' => 'Description of the first feature with details about its benefits.',
        'icon' => 'icon-class-1'
    ),
    array(
        'title' => 'Feature Two', 
        'description' => 'Description of the second feature highlighting key advantages.',
        'icon' => 'icon-class-2'
    ),
    array(
        'title' => 'Feature Three',
        'description' => 'Description of the third feature explaining its value proposition.',
        'icon' => 'icon-class-3'
    )
);

// ========== 获取参数（带默认值）==========
$title = isset($module_args['title']) ? $module_args['title'] : $default_title;
$content = isset($module_args['content']) ? $module_args['content'] : $default_content;
$items = !empty($module_args['items']) ? $module_args['items'] : $default_items;
$button_text = isset($module_args['button_text']) ? $module_args['button_text'] : 'Learn More';
$button_url = isset($module_args['button_url']) ? $module_args['button_url'] : '#';
?>

<div class="{module-name}-module">
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
        
        <a href="<?php echo esc_url($button_url); ?>" class="module-button">
            <?php echo esc_html($button_text); ?>
        </a>
    </div>
</div>
```

### CSS代码模板

```css
.{module-name}-module {
    padding: 80px 0;
    background-color: #fff;
}

.{module-name}-module .elementor-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 15px;
}

.{module-name}-module .module-title {
    font-size: 36px;
    font-weight: 700;
    color: #333;
    margin-bottom: 20px;
}

.{module-name}-module .module-content {
    font-size: 16px;
    line-height: 1.6;
    color: #666;
    margin-bottom: 40px;
}

@media (max-width: 768px) {
    .{module-name}-module {
        padding: 40px 0;
    }
    
    .{module-name}-module .module-title {
        font-size: 28px;
    }
}
```

## 截图参考

请查看 `output/screenshots/` 目录下的分块截图：
- `products_pixel_1.jpg`
- `products_pixel_2.jpg`
- `products_pixel_3.jpg`
- `products_pixel_4.jpg`
- `products_pixel_5.jpg`
- `products_pixel_6.jpg`

**重要**：请从截图中提取实际的文字内容作为默认数据，不要使用空字符串或无意义的占位符。

---

## 🎯 推荐输出方式：WordPress 页面模板

### 页面模板结构

请生成一个完整的 WordPress 页面模板文件，包含所有模块：

**文件位置**: `wp-content/themes/{theme-name}/page-templates/template-{page-name}.php`

### 页面模板代码示例

```php
<?php
/**
 * Template Name: {Page Name} 页面模板
 * Description: 克隆自 {source_url} 的页面模板
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();
?>

<main class="page-{page-slug}">

    <!-- ========== Section 1: Hero ========== -->
    <section class="hero-section">
        <div class="elementor-container">
            <?php
            $hero_title = '从截图提取的实际标题';
            $hero_subtitle = '从截图提取的副标题内容';
            $hero_button_text = 'Quick Quote';
            $hero_button_url = '#contact';
            ?>
            <div class="hero-content">
                <h1><?php echo esc_html($hero_title); ?></h1>
                <p class="hero-subtitle"><?php echo esc_html($hero_subtitle); ?></p>
                <a href="<?php echo esc_url($hero_button_url); ?>" class="btn btn-primary">
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
                    'title' => '产品标题1',
                    'description' => '产品描述内容...',
                    'image' => 'https://placehold.co/400x300/e0e0e0/666?text=Product+1'
                ),
                array(
                    'title' => '产品标题2',
                    'description' => '产品描述内容...',
                    'image' => 'https://placehold.co/400x300/e0e0e0/666?text=Product+2'
                ),
                // 更多产品...
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

    <!-- 继续添加其他 sections... -->

</main>

<?php get_footer(); ?>
```

### 配套 CSS 文件

**文件位置**: `wp-content/themes/{theme-name}/assets/css/template-{page-name}.css`

```css
/* ========== Page Template: {Page Name} ========== */

.page-{page-slug} {
    /* 页面全局样式 */
}

/* Hero Section */
.hero-section {
    padding: 80px 0;
    background: #f8f8f8;
}

.hero-section .elementor-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 15px;
    display: flex;
    align-items: center;
    gap: 40px;
}

.hero-content {
    flex: 1;
}

.hero-content h1 {
    font-size: 48px;
    font-weight: 700;
    color: #333;
    margin-bottom: 20px;
}

/* Product Grid Section */
.product-grid-section {
    padding: 80px 0;
    background: #fff;
}

.products-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
}

.product-card {
    background: #fff;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

/* 响应式 */
@media (max-width: 1024px) {
    .products-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 768px) {
    .hero-section .elementor-container {
        flex-direction: column;
    }
    
    .products-grid {
        grid-template-columns: 1fr;
    }
    
    .hero-content h1 {
        font-size: 32px;
    }
}
```

### 在 functions.php 中注册样式

```php
// 在 functions.php 中添加
function enqueue_page_template_styles() {
    if (is_page_template('page-templates/template-{page-name}.php')) {
        wp_enqueue_style(
            'template-{page-name}-style',
            get_template_directory_uri() . '/assets/css/template-{page-name}.css',
            array(),
            '1.0.0'
        );
    }
}
add_action('wp_enqueue_scripts', 'enqueue_page_template_styles');
```

---

## 使用方式

生成代码后，按以下步骤在 WordPress 中创建页面：

1. 将 PHP 模板文件放入 `wp-content/themes/your-theme/page-templates/` 目录
2. 将 CSS 文件放入 `wp-content/themes/your-theme/assets/css/` 目录
3. 在 `functions.php` 中添加样式注册代码
4. WordPress 后台 → 页面 → 新建页面
5. 在页面属性中选择 **"{Page Name} 页面模板"**
6. 发布页面

---

## 输出要求

请生成以下文件：

1. **页面模板 PHP 文件**: `template-{page-name}.php`
   - 包含所有 sections
   - 每个 section 使用从截图提取的真实内容作为默认数据
   - 图片使用 placehold.co 占位符

2. **CSS 样式文件**: `template-{page-name}.css`
   - 完整的响应式设计
   - 使用分析中提取的颜色、字体、间距参数

3. **functions.php 代码片段**: 注册样式的代码
