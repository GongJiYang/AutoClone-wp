# WordPress 页面克隆任务

## 原始页面信息
- URL: https://georgeconstructions.com/modern-kitchen-cabinets/
- 标题: Custom Modern Kitchen Cabinets｜ Design ideas
- 总高度: 12519px

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
- **截图**: `modern-kitchen-cabinets_pixel_1.jpg`
- **建议模块名**: `kitchen-cabinets-hero`

**布局**:
- 容器: full-width
- 类型: flex
- 列数: 1, 行数: 1
- 水平间距: 0px, 垂直间距: 30px
- 对齐: left

**颜色**:
- 背景: #000000
- 主色: #FF8C00
- 标题: #FFFFFF
- 正文: #FFFFFF
- 边框: none

**字体**:
- 标题: 48px, 字重: 700
- 正文: 18px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 0px

**组件** (7个):
  - navbar x1, 宽=auto, 高=auto, 圆角=0
    说明: 包含logo和导航链接的顶部导航栏
  - logo x1, 宽=auto, 高=auto, 圆角=0
    说明: 页面左上角的George logo
  - nav-link x7, 宽=auto, 高=auto, 圆角=0
    说明: 导航栏中的Products、Projects、Blog、Service、Video、About、Contact链接
  - button x1, 宽=auto, 高=auto, 圆角=4px
    说明: 右上角的Quick Quote按钮，橙色背景，白色文字
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: hero区域的主标题，白色和橙色文字
  - paragraph x1, 宽=auto, 高=auto, 圆角=0
    说明: hero区域的副标题段落，白色文字
  - button x1, 宽=auto, 高=auto, 圆角=4px
    说明: hero区域的Get A Free Quote按钮，橙色背景，白色文字

**图片占位符** (1组):
  - **hero-banner** x1
    尺寸: 100% x auto, 比例: 16:9
    位置: 背景, object-fit: cover
    遮罩: rgba(0,0,0,0.3)
    占位符建议: 厨房场景图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Modern kitchen cabinets`
- **副标题**: `Modern kitchen cabinets instantly elevate your space. Discover stylish designs for a sleek, functional kitchen.`
- **段落** (1个):
  - `Modern kitchen cabinets instantly elevate your space. Discover stylish designs for a sleek, function...`
- **按钮文字**: `Quick Quote`, `Get A Free Quote`

**响应式**: 平板端导航链接可能折叠为汉堡菜单，hero区域标题和按钮保持响应式布局
**特效**: hero背景图片可能有淡入效果，按钮 hover 时有颜色变化
**内容摘要**: 展示现代厨房橱柜的主视觉区域，包含标题、描述和行动号召按钮

---

### 分块 2: product-grid
- **截图**: `modern-kitchen-cabinets_pixel_2.jpg`
- **建议模块名**: `kitchen-cabinets-product-grid`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 3, 行数: 2
- 水平间距: 20px, 垂直间距: 30px
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #333333
- 正文: #666666
- 边框: none

**字体**:
- 标题: 18px, 字重: 700
- 正文: 14px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 50px
- 下边距: 50px
- 元素间距: 10px
- 卡片内边距: 20px

**组件** (1个):
  - card x6, 宽=auto, 高=auto, 圆角=8px, 有阴影
    说明: 浅灰色背景卡片，包含产品图片、标题和描述，带轻微阴影效果

**图片占位符** (1组):
  - **product** x6
    尺寸: 300px x 200px, 比例: 16:9
    位置: 网格排列（每行3个，共2行）, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **卡片内容** (6个):
  - `Modern Metal Kitchen Cabinets`: Kitchen Metal Cabinets Design Ideas Modern metal k...
  - `Modern Wood Veneer Luxury Kitchen Cabinet Design`: Wood Veneer Cabinets Ideas And Inspiration Wood ve...
  - `High Gloss Modern Cabinets`: Contemporary High Gloss Kitchen Cabinets When remo...

**响应式**: 平板设备显示2列，移动端显示1列
**特效**: 卡片 hover 时可能显示阴影增强效果
**内容摘要**: 展示现代厨房橱柜的不同设计类型，包括金属、木皮、高光、双色、蓝色三聚氰胺、黑色L型等6种风格

---

### 分块 3: image-text
- **截图**: `modern-kitchen-cabinets_pixel_3.jpg`
- **建议模块名**: `kitchen-cabinets-ideas-section`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: left

**颜色**:
- 背景: #f8f8f8
- 主色: #333333
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
- 元素间距: 20px
- 卡片内边距: 0

**组件** (2个):
  - image x1, 宽=450px, 高=300px, 圆角=0
    说明: 左侧现代厨房图片，展示橱柜与吧台设计，无阴影或边框
  - text x4, 宽=auto, 高=auto, 圆角=0
    说明: 右侧文字内容，包含主标题与三段段落，无阴影或边框

**图片占位符** (1组):
  - **content-image** x1
    尺寸: 450px x 300px, 比例: 3:2
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Modern Kitchen Cabinet Ideas`
- **段落** (3个):
  - `The days have passed when kitchens were only used for cooking food. In today's society, kitchens are...`
  - `Using contemporary cabinet door designs is one of the best ways to create a modern look. Cabinet doo...`
  - `This comprehensive guide will explore modern kitchen cabinets in great detail. We will examine their...`

**响应式**: 平板设备下图片与文字堆叠（1列），移动端图片宽度100%，文字宽度100%
**特效**: 无
**内容摘要**: 该区域通过图文混排形式介绍现代厨房橱柜的设计理念与重要性，左侧展示厨房实景图，右侧阐述橱柜在现代厨房中的核心作用及设计趋势

---

### 分块 4: image-text
- **截图**: `modern-kitchen-cabinets_pixel_4.jpg`
- **建议模块名**: `kitchen-cabinets-ideas`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: #f8f8f8
- 主色: #FF8C00
- 标题: #222222
- 正文: #333333
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

**组件** (2个):
  - image x1, 宽=400px, 高=auto, 圆角=0
    说明: 左侧厨房场景图片，展示现代橱柜设计，采用cover方式填充，保持16:9比例
  - text x4, 宽=auto, 高=auto, 圆角=0
    说明: 右侧文字区域，包含1个主标题和3个段落，文字颜色为深灰，标题权重加粗

**图片占位符** (1组):
  - **product** x1
    尺寸: 400px x auto, 比例: 16:9
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Modern Kitchen Cabinet Ideas`
- **段落** (3个):
  - `The days have passed when kitchens were only used for cooking food. In today’s society, kitchens are...`
  - `Using contemporary cabinet door designs is one of the best ways to create a modern look. Cabinet doo...`
  - `This comprehensive guide will explore modern kitchen cabinets in great detail. We will examine their...`

**响应式**: 平板设备（768px-1024px）显示为1列堆叠布局，移动端（<768px）显示为1列堆叠布局，图片和文字垂直排列
**特效**: 图片采用object-fit: cover属性保持比例，文字区域无特殊动画效果
**内容摘要**: 该区域主要展示现代厨房橱柜的设计理念，解释厨房在现代家庭中的核心地位及现代橱柜对空间实用性与视觉美感的提升作用，为后续内容做铺垫

---

### 分块 5: features
- **截图**: `modern-kitchen-cabinets_pixel_5.jpg`
- **建议模块名**: `modern-design-features`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 3, 行数: 1
- 水平间距: 30px, 垂直间距: 40px
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #333333
- 正文: #666666
- 边框: none

**字体**:
- 标题: 24px, 字重: 700
- 正文: 14px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - card x3, 宽=auto, 高=auto, 圆角=8px
    说明: 白色卡片，包含橙色图标、标题和描述

**图片占位符** (1组):
  - **image** x1
    尺寸: 50% x auto, 比例: 16:9
    位置: 右侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Features of Modern Design`
- **卡片内容** (3个):
  - `Sleek Aesthetics`: A minimalistic style with straight lines that emph...
  - `Functional Elegance`: The result of combining style with utility in a de...
  - `Natural Light and Open Space`: Increasing the openness of the space by making use...

**响应式**: 平板设备2列，移动端1列
**特效**: 无
**内容摘要**: 展示现代设计的三个核心特征：简洁美学、功能优雅、自然光与开放空间

---

### 分块 6: features
- **截图**: `modern-kitchen-cabinets_pixel_6.jpg`
- **建议模块名**: `modern-design-features`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 3, 行数: 1
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

**组件** (2个):
  - card x3, 宽=auto, 高=auto, 圆角=0
    说明: 白色卡片，无阴影，包含图标、标题和描述，排列为水平一行
  - icon x3, 宽=40px, 高=40px, 圆角=0
    说明: 橙色图标（星形、网格、太阳），位于卡片顶部

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Features of Modern Design`
- **卡片内容** (3个):
  - `Sleek Aesthetics`: A minimalistic style with straight lines that emph...
  - `Functional Elegance`: The result of combining style with utility in a de...
  - `Natural Light and Open Space`: Increasing the openness of the space by making use...

**响应式**: 平板设备下调整为2列布局，移动端设备下调整为1列布局
**特效**: 无
**内容摘要**: 该区域主要展示现代设计的三大核心特色：简洁美学、功能优雅、自然光与开放空间

---

### 分块 7: features
- **截图**: `modern-kitchen-cabinets_pixel_7.jpg`
- **建议模块名**: `kitchen-cabinets-materials-features`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 2
- 水平间距: 30px, 垂直间距: 30px
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #333333
- 标题: #333333
- 正文: #666666
- 边框: none

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 40px
- 下边距: 40px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - card x4, 宽=auto, 高=auto, 圆角=8px
    说明: 白色卡片，包含材料标题和描述

**图片占位符** (1组):
  - **thumbnail** x0
    尺寸: auto x auto, 比例: auto
    位置: 网格排列, object-fit: contain
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Popular Materials for Modern Design Kitchen Cabinets`
- **副标题**: `Multiple trendy materials exist for contemporary kitchen cabinet design, each offering distinct advantages and visual attractiveness.`
- **段落** (2个):
  - `Modern kitchens frequently employ laminate since it's affordable and long-lasting. You can choose fr...`
  - `Kitchen cabinets made of wood are classic. Modern wooden cabinets usually accentuate wood grain by m...`
- **卡片内容** (2个):
  - `Laminate`: Modern kitchens frequently employ laminate since i...
  - `Wood`: Kitchen cabinets made of wood are classic. Modern ...

**响应式**: 平板2列，移动端1列
**特效**: 无
**内容摘要**: 该区域主要展示现代厨房橱柜的流行材料（laminate、wood、acrylic、stainless steel），每个材料介绍其特点和优势

---

### 分块 8: product-grid
- **截图**: `modern-kitchen-cabinets_pixel_8.jpg`
- **建议模块名**: `kitchen-cabinets-materials-grid`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 2
- 水平间距: 30px, 垂直间距: 30px
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #333333
- 标题: #333333
- 正文: #666666
- 边框: none

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - card x3, 宽=45%, 高=auto, 圆角=8px
    说明: 材料卡片，包含标题和描述，无阴影和边框

**图片占位符** (1组):
  - **background** x1
    尺寸: 100% x 300px, 比例: 16:9
    位置: 左列中间位置, object-fit: cover
    占位符建议: 厨房场景图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **卡片内容** (3个):
  - `Acrylic`: Acrylic is known for its shiny, reflective finish ...
  - `Stainless Steel`: Stainless steel cabinets are popular with people w...
  - `Laminate`: Selecting contemporary kitchen cabinets with glass...

**响应式**: 平板设备显示2列，移动端设备显示1列
**特效**: 无
**内容摘要**: 该区域主要展示现代厨房橱柜的流行材料（Acrylic、Stainless Steel、Laminate），每个材料包含标题和详细描述，中间穿插厨房场景图片

---

### 分块 9: content-block
- **截图**: `modern-kitchen-cabinets_pixel_9.jpg`
- **建议模块名**: `kitchen-color-trends`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 2
- 水平间距: 20px, 垂直间距: 30px
- 对齐: space-between

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

**组件** (2个):
  - card x4, 宽=auto, 高=auto, 圆角=8px
    说明: 白色背景卡片，左侧配图，右侧文字描述，无阴影无边框
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 橙色背景按钮，白色文字，圆角4px

**图片占位符** (1组):
  - **thumbnail** x4
    尺寸: 300px x 200px, 比例: 3:2
    位置: 网格排列（2x2，左图右文）, object-fit: cover
    占位符建议: kitchen-color-trend

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Kitchen Color Trends In Modern Design`
- **副标题**: `Color is a key factor in determining the overall appearance and atmosphere of your kitchen area. Popular color trends in contemporary kitchen cabinet design consist of:`
- **按钮文字**: `Consult`
- **卡片内容** (4个):
  - `Neutral Tones`: Neutral colors like white, gray, and beige remain ...
  - `Bold And Dramatic`: Although neutral tones are still a popular choice,...
  - `Two-Tone`: The two-tone look is another popular color choice ...

**响应式**: 平板设备（768px以上）显示2列网格布局，移动设备（768px以下）显示1列垂直排列
**特效**: 无动态效果，静态图文展示
**内容摘要**: 该区域主要展示现代厨房橱柜设计的四种流行颜色趋势（中性色调、大胆戏剧色、双色、自然木色），每种趋势通过图片与文字说明结合呈现

---

### 分块 10: features
- **截图**: `modern-kitchen-cabinets_pixel_10.jpg`
- **建议模块名**: `customizing-kitchen-cabinets`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 2
- 水平间距: 30px, 垂直间距: 40px
- 对齐: space-between

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

**组件** (3个):
  - image x1, 宽=400px, 高=240px, 圆角=0
    说明: 左侧内容图片，展示团队或场景，用于图文混排
  - button x1, 宽=120px, 高=40px, 圆角=4px
    说明: 橙色按钮，文字为Consult
  - card x2, 宽=48%, 高=auto, 圆角=8px, 有阴影
    说明: 白色卡片，包含标题和描述，用于展示定制选项

**图片占位符** (1组):
  - **content-image** x1
    尺寸: 400px x 240px, 比例: 4:3
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Customizing Modern Design Kitchen Cabinets`
- **段落** (1个):
  - `Modern kitchen cabinets have the benefit of being customizable to fit your unique needs and style th...`
- **按钮文字**: `Consult`
- **卡片内容** (2个):
  - `Hardware`: The hardware a modern kitchen chooses can have a b...
  - `Cabinet Organization`: Adding pull-out shelves, drawer organizers, and ot...

**响应式**: 平板设备下，卡片变为1列；移动端图文混排变为垂直排列，卡片1列
**特效**: 按钮 hover 时可能有颜色加深效果，卡片 hover 时有阴影变化
**内容摘要**: 该区域主要展示现代厨房橱柜的定制选项，包括硬件和橱柜组织等特色功能

---

### 分块 11: features
- **截图**: `modern-kitchen-cabinets_pixel_11.jpg`
- **建议模块名**: `kitchen-cabinets-customization-features`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 3
- 水平间距: 20px, 垂直间距: 20px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #ff8c00
- 标题: #333333
- 正文: #666666
- 边框: none

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
  - card x6, 宽=300px, 高=200px, 圆角=8px
    说明: 白色卡片，包含图片和文字，展示厨房定制选项
  - button x1, 宽=150px, 高=40px, 圆角=4px
    说明: 橙色按钮，文字为'Consult'

**图片占位符** (1组):
  - **thumbnail** x6
    尺寸: 300px x 200px, 比例: 3:2
    位置: 卡片左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Customizing Modern Design Kitchen Cabinets`
- **副标题**: `Modern kitchen cabinets have the benefit of being customizable to fit your unique needs and style thanks to their flexibility. Several often selected customisation options include:`
- **按钮文字**: `Consult`
- **卡片内容** (6个):
  - `Hardware`: The hardware a modern kitchen chooses can have a b...
  - `Cabinet Organization`: Adding pull-out shelves, drawer organizers, and ot...
  - `Open Shelves`: Open shelves are a trendy choice for contemporary ...

**响应式**: 平板设备2列，移动端1列
**特效**: 无
**内容摘要**: 该区域展示厨房定制的主要选项，包括硬件、收纳、开放式架子、灯光、混合材料和大胆用色等特色

---

### 分块 12: features
- **截图**: `modern-kitchen-cabinets_pixel_12.jpg`
- **建议模块名**: `kitchen-cabinets-customization-options`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 3
- 水平间距: 20px, 垂直间距: 30px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #333333
- 正文: #666666
- 边框: none

**字体**:
- 标题: 24px, 字重: 600
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 10px
- 卡片内边距: 20px

**组件** (2个):
  - card x6, 宽=570px, 高=250px, 圆角=8px, 有阴影
    说明: 白色卡片，带轻微阴影，左侧显示图片，右侧显示标题和描述文字
  - button x1, 宽=150px, 高=40px, 圆角=4px
    说明: 橙色背景按钮，白色文字，位于标题下方

**图片占位符** (1组):
  - **thumbnail** x6
    尺寸: 300px x 200px, 比例: 3:2
    位置: 卡片左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Customizing Modern Design Kitchen Cabinets`
- **副标题**: `Modern kitchen cabinets have the benefit of being customizable to fit your unique needs and style thanks to their flexibility. Several often selected customisation options include:`
- **段落** (6个):
  - `The hardware a modern kitchen chooses can have a big impact on how the room looks overall. For a sle...`
  - `Adding pull-out shelves, drawer organizers, and other storage solutions to your contemporary kitchen...`
  - `Open shelves are a trendy choice for contemporary kitchen cabinets, allowing you to showcase your fa...`
- **按钮文字**: `Consult`
- **卡片内容** (6个):
  - `Hardware`: The hardware a modern kitchen chooses can have a b...
  - `Cabinet Organization`: Adding pull-out shelves, drawer organizers, and ot...
  - `Open Shelves`: Open shelves are a trendy choice for contemporary ...

**响应式**: 平板设备显示2列，移动端设备显示1列，按钮在小屏幕下全宽显示
**特效**: 卡片 hover 时轻微阴影加深，按钮 hover 时背景色变深
**内容摘要**: 展示现代厨房橱柜的6种定制选项，包括硬件、储物组织、开放式搁架、照明、材料混合及大胆用色，每个选项通过图片和文字说明其特点和优势

---

### 分块 13: features-service
- **截图**: `modern-kitchen-cabinets_pixel_13.jpg`
- **建议模块名**: `kitchen-cabinets-design-tips`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 3
- 水平间距: 20px, 垂直间距: 40px
- 对齐: left

**颜色**:
- 背景: #f8f8f8
- 主色: #FF8C00
- 标题: #333333
- 正文: #666666
- 边框: #e0e0e0

**字体**:
- 标题: 36px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (2个):
  - card x6, 宽=580px, 高=auto, 圆角=8px, 有阴影
    说明: 白色卡片，带轻微阴影，包含图片和文字内容
  - button x1, 宽=150px, 高=40px, 圆角=4px
    说明: 橙色背景按钮，白色文字，居中显示

**图片占位符** (1组):
  - **thumbnail** x7
    尺寸: 300px x 200px, 比例: 3:2
    位置: 卡片左侧/CTA左侧/网格排列, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Tips for Choosing the Perfect Modern Kitchen Cabinets`
- **副标题**: `Consider the following ideas when choosing modern kitchen cabinets for your area:`
- **段落** (6个):
  - `Mix various materials, like wood and acrylic, for an original and visually appealing kitchen layout.`
  - `Do not hesitate to integrate vibrant and striking colors in your contemporary style kitchen cabinets...`
  - `It's crucial to consider your unique requirements and preferences before choosing cabinets. Think ab...`
- **按钮文字**: `Consult`
- **卡片内容** (6个):
  - `Mix And Match Materials`: Mix various materials, like wood and acrylic, for ...
  - `Go Bold With Color`: Do not hesitate to integrate vibrant and striking ...
  - `Assess Your Needs:`: It's crucial to consider your unique requirements ...

**响应式**: 桌面端2列（前2个卡片）/1列（CTA）/4列（后4个卡片），平板端2列/1列/2列，移动端1列/1列/1列
**特效**: 卡片 hover 时轻微阴影加深，按钮 hover 时背景色变深
**内容摘要**: 该区域主要展示现代厨房橱柜的设计建议，包括材料混搭、色彩运用、需求评估、材料选择、预算考虑及专业咨询等内容，通过图文卡片和CTA按钮引导用户获取更多帮助

---

### 分块 14: features
- **截图**: `modern-kitchen-cabinets_pixel_14.jpg`
- **建议模块名**: `kitchen-cabinets-features`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: #f8f8f8
- 主色: #FF8C00
- 标题: #333333
- 正文: #666666
- 边框: none

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - card x4, 宽=auto, 高=auto, 圆角=8px
    说明: 浅灰色背景卡片，包含标题和段落文本，展示厨房橱柜选择的四个建议

**图片占位符** (1组):
  - **thumbnail** x4
    尺寸: 300px x 200px, 比例: 4:3
    位置: 网格排列，每个卡片左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **段落** (4个):
  - `It's crucial to consider your unique requirements and preferences before choosing cabinets. Think ab...`
  - `It's essential to choose long-lasting, high-quality materials for contemporary kitchen cabinets.`
  - `Consider your budget when choosing your cabinets. There is a wide range of modern kitchen cabinet ch...`
- **卡片内容** (4个):
  - `Assess Your Needs:`: It's crucial to consider your unique requirements ...
  - `Select Top-Notch Materials:`: It's essential to choose long-lasting, high-qualit...
  - `Consider Your Budget:`: Consider your budget when choosing your cabinets. ...

**响应式**: 平板设备下可能调整为2列，移动端1列
**特效**: 无特殊动画效果，hover时可能无变化或轻微阴影
**内容摘要**: 展示选择现代厨房橱柜的四个关键建议：评估需求、选择优质材料、考虑预算、咨询专业人士

---

### 分块 15: contact-form
- **截图**: `modern-kitchen-cabinets_pixel_15.jpg`
- **建议模块名**: `contact-form-section`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #666666
- 标题: #000000
- 正文: #333333
- 边框: #e0e0e0

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 40px
- 下边距: 40px
- 元素间距: 15px
- 卡片内边距: 20px

**组件** (7个):
  - image x1, 宽=200px, 高=200px, 圆角=0
    说明: 左侧Product Manager头像图片，黑色上衣，白色背景
  - text x2, 宽=auto, 高=auto, 圆角=0
    说明: 左侧标题和副标题文字
  - input x4, 宽=100%, 高=40px, 圆角=4px
    说明: Name、Email、Tel/Whatsapp、City输入框，白色背景，浅灰色边框
  - select x1, 宽=100%, 高=40px, 圆角=4px
    说明: Country-Select选择框
  - checkbox x10, 宽=auto, 高=auto, 圆角=0
    说明: Product Needed复选框，包括Kitchen cabinet、Bedroom、Bathroom、Windows & Doors、Furniture、Lighting、Soft Furnishing、Tiles and Wood Flooring、Whole House Solution、Other Building Material
  - textarea x1, 宽=100%, 高=120px, 圆角=4px
    说明: Message文本框
  - button x2, 宽=auto, 高=40px, 圆角=4px
    说明: Choose File按钮（灰色）和Send按钮（灰色）

**图片占位符** (1组):
  - **avatar** x1
    尺寸: 200px x 200px, 比例: 1:1
    位置: 左侧, object-fit: cover
    占位符建议: product-manager-avatar

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Want to Get Best Price Kitchen Cabinets?`
- **副标题**: `Share floor plan or house photos for 8-hour quote`
- **按钮文字**: `Choose File`, `Send`
- **列表项** (1个):
  - `Product Needed*`: Kitchen cabinet, Bedroom, Bathroom, Windows & Door...

**响应式**: 平板端可能改为1列布局，移动端表单元素堆叠显示
**特效**: 无明显的动画或渐变效果，表单元素有常规的焦点状态
**内容摘要**: 该区域是联系表单，用于用户提交项目详情获取报价，包含Product Manager头像、表单标题、输入框、选择框、复选框、文本框和提交按钮

---

### 分块 16: contact-form
- **截图**: `modern-kitchen-cabinets_pixel_16.jpg`
- **建议模块名**: `kitchen-cabinets-quote-form`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0px
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #666666
- 标题: #333333
- 正文: #666666
- 边框: #dddddd

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 50px
- 下边距: 50px
- 元素间距: 20px
- 卡片内边距: 15px

**组件** (5个):
  - image x1, 宽=200px, 高=200px, 圆角=8px
    说明: 左侧展示的Product Manager头像图片，圆形/方形圆角，位于模块左侧
  - input x5, 宽=100%, 高=40px, 圆角=4px
    说明: 表单中的输入框，包括Name、Email、Tel/Whatsapp、City、Country-Select，边框为浅灰色
  - checkbox x10, 宽=auto, 高=auto, 圆角=0
    说明: Product Needed选项的复选框，包括Kitchen cabinet、Bedroom等10个选项，排列为两行
  - textarea x1, 宽=100%, 高=120px, 圆角=4px
    说明: Message文本框，多行输入，边框为浅灰色
  - button x2, 宽=100%, 高=40px, 圆角=4px
    说明: 表单中的按钮，包括Choose File（文件选择）和Send（提交）按钮，背景为灰色

**图片占位符** (1组):
  - **avatar** x1
    尺寸: 200px x 200px, 比例: 1:1
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Want to Get Best Price Kitchen Cabinets?`
- **副标题**: `Share floor plan or house photos for 8-hour quote`
- **按钮文字**: `Send`, `Choose File`

**响应式**: 平板设备显示为2列布局（图片+表单），移动端设备显示为1列布局（图片在上，表单在下）
**特效**: 表单输入框聚焦时边框变为蓝色，按钮hover时背景色加深
**内容摘要**: 该区域主要展示获取厨房橱柜报价的表单，用户可提交项目详情、联系方式及产品需求，以获取8小时内的报价

---

### 分块 17: footer
- **截图**: `modern-kitchen-cabinets_pixel_17.jpg`
- **建议模块名**: `footer-section`

**布局**:
- 容器: full-width
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: left

**颜色**:
- 背景: #000000
- 主色: #666666
- 标题: #ffffff
- 正文: #ffffff
- 边框: #333333

**字体**:
- 标题: 18px, 字重: 700
- 正文: 14px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 20px
- 卡片内边距: 0

**组件** (3个):
  - text x22, 宽=auto, 高=auto, 圆角=0
    说明: 白色文字链接，包括Products、One-Stop Solutions、Customer Services列下的导航链接及Contact Us列下的文字内容
  - form x2, 宽=auto, 高=40px, 圆角=4px
    说明: 白色边框输入框，包含Whatsapp和Email字段
  - button x2, 宽=100%, 高=40px, 圆角=4px
    说明: 灰色背景按钮，包含Send文字

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Products, One-Stop Solutions, Customer Services, Contact Us`
- **段落** (1个):
  - `Share floor plan or house photos for 8-hour quote`
- **按钮文字**: `Send`, `Send`
- **列表项** (23个):
  - `Kitchen Cabinet`: ...
  - `Wardrobe`: ...
  - `Windows and Doors`: ...

**响应式**: 平板设备下调整为2列，移动端调整为1列
**特效**: 无
**内容摘要**: 页面底部导航栏，包含产品分类、一站式解决方案、客户服务及联系方式，提供订阅功能

---


## 设计参数汇总

### 颜色系统（CSS变量建议）
```css
:root {
    --color-primary: #666666;
    --color-secondary: #ffffff;
    --color-background: #000000;
    --color-heading: #ffffff;
    --color-text: #ffffff;
    --color-border: #333333;
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
    --line-height: 1.6;
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
- `modern-kitchen-cabinets_pixel_1.jpg`
- `modern-kitchen-cabinets_pixel_10.jpg`
- `modern-kitchen-cabinets_pixel_11.jpg`
- `modern-kitchen-cabinets_pixel_12.jpg`
- `modern-kitchen-cabinets_pixel_13.jpg`
- `modern-kitchen-cabinets_pixel_14.jpg`
- `modern-kitchen-cabinets_pixel_15.jpg`
- `modern-kitchen-cabinets_pixel_16.jpg`
- `modern-kitchen-cabinets_pixel_17.jpg`
- `modern-kitchen-cabinets_pixel_2.jpg`
- `modern-kitchen-cabinets_pixel_3.jpg`
- `modern-kitchen-cabinets_pixel_4.jpg`
- `modern-kitchen-cabinets_pixel_5.jpg`
- `modern-kitchen-cabinets_pixel_6.jpg`
- `modern-kitchen-cabinets_pixel_7.jpg`
- `modern-kitchen-cabinets_pixel_8.jpg`
- `modern-kitchen-cabinets_pixel_9.jpg`

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
