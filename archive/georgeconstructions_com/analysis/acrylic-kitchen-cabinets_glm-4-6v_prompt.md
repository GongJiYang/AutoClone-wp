# WordPress 页面克隆任务

## 原始页面信息
- URL: https://georgeconstructions.com/acrylic-kitchen-cabinets/
- 标题: Acrylic Kitchen Cabinets｜Buying Guide | Supplier
- 总高度: 9694px

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
- **截图**: `acrylic-kitchen-cabinets_pixel_1.jpg`
- **建议模块名**: `kitchen-cabinets-hero`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #222222
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

**组件** (5个):
  - navbar x1, 宽=100%, 高=60px, 圆角=0
    说明: 顶部导航栏，包含logo、7个菜单项（Products/Projects/Blog/Service/Video/About/Contact）和1个Quick Quote按钮
  - text x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题‘Acrylic Kitchen Cabinets’，深灰色（#222222），加粗700
  - paragraph x2, 宽=auto, 高=auto, 圆角=0
    说明: 两个段落，描述丙烯酸厨房橱柜的项目需求及George的服务内容
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 橙色背景（#FF8C00），白色文字，‘Get a Free Quote →’
  - image x1, 宽=50%, 高=auto, 圆角=8px, 有阴影
    说明: 右侧空白区域，带轻微阴影，为产品图片预留位置

**图片占位符** (1组):
  - **hero-banner** x1
    尺寸: 50% x auto, 比例: auto
    位置: 右侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Acrylic Kitchen Cabinets`
- **段落** (2个):
  - `For your project, do you require acrylic kitchen cabinets? You've undoubtedly heard of "acrylic kitc...`
  - `At George, we will explore acrylic cabinets, outlining their advantages and disadvantages to assist ...`
- **按钮文字**: `Get a Free Quote →`

**响应式**: 平板设备（≤768px）下，主内容区域改为单列布局，图片占满宽度；移动端（≤480px）导航菜单折叠为汉堡菜单，按钮文字简化为‘Quote’
**特效**: Quick Quote按钮 hover 时背景色加深至#E67300，图片占位区域阴影增强；导航栏滚动时固定定位
**内容摘要**: 页面顶部hero区域，核心展示丙烯酸厨房橱柜的主题信息，包含主标题、项目需求描述、服务说明及行动号召按钮，右侧预留产品视觉展示位置

---

### 分块 2: product-grid
- **截图**: `acrylic-kitchen-cabinets_pixel_2.jpg`
- **建议模块名**: `acrylic-kitchen-cabinets-grid`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 3, 行数: 2
- 水平间距: 20px, 垂直间距: 30px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #333333
- 正文: #666666
- 边框: #e0e0e0

**字体**:
- 标题: 18px, 字重: 700
- 正文: 14px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - card x6, 宽=auto, 高=auto, 圆角=8px, 有阴影
    说明: 白色卡片，带轻微阴影，包含产品图片、标题和简短描述

**图片占位符** (1组):
  - **product** x6
    尺寸: 100% x 200px, 比例: 16:9
    位置: 卡片顶部, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **卡片内容** (6个):
  - `White Acrylic Kitchen Cabinet`: Acrylic Kitchen Cabinet Supplier & Manufacturer An...
  - `Solid Acrylic Kitchen Cabinet Doors`: Solid Acrylic Kitchen Cabinet Doors Acrylic cabine...
  - `Modern Acrylic Kitchen Cabinets`: Extended sunshine exposure will have a significant...

**响应式**: 平板设备显示2列，移动端设备显示1列
**特效**: 卡片带有轻微阴影效果， hover时可能触发阴影加深或缩放动画（截图中未显示）
**内容摘要**: 该区域主要展示6种不同类型的亚克力厨房橱柜产品，每个产品包含高清图片、标题及简短功能描述

---

### 分块 3: features
- **截图**: `acrylic-kitchen-cabinets_pixel_3.jpg`
- **建议模块名**: `acrylic-kitchen-cabinets-advantages`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 2
- 水平间距: 30px, 垂直间距: 40px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #222222
- 正文: #333333
- 边框: none

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 20px
- 卡片内边距: 20px

**组件** (2个):
  - image x2, 宽=50%, 高=auto, 圆角=0
    说明: 左侧和右下角的厨房橱柜图片，展示产品外观
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 橙色背景的CTA按钮，位于‘Resistant to Moisture and Durability’段落下方

**图片占位符** (1组):
  - **product** x2
    尺寸: 50% x auto, 比例: 16:9
    位置: 左右排列（左上角和右下角）, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Advantages of Acrylic Kitchen Cabinets`
- **段落** (3个):
  - `The obvious advantage of acrylic cabinets is their fashionable and modern appearance. Every kitchen ...`
  - `The kitchen environment is a perfect fit for acrylic cabinets because of their exceptional resistanc...`
  - `Behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind text...`
- **按钮文字**: `GET A PROJECT QUOTE`

**响应式**: 平板设备显示2列，移动端设备显示1列（堆叠排列）
**特效**: 按钮 hover 时可能有颜色加深或阴影效果（推测）
**内容摘要**: 该区域主要展示丙烯酸厨房橱柜的核心优势，包括美学吸引力、防潮耐用性、易维护性和颜色多样性，通过图文混排形式突出产品特点

---

### 分块 4: features
- **截图**: `acrylic-kitchen-cabinets_pixel_4.jpg`
- **建议模块名**: `acrylic-cabinets-features-drawbacks`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 30px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #333333
- 正文: #666666
- 边框: none

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 30px
- 下边距: 30px
- 元素间距: 20px
- 卡片内边距: 20px

**组件** (2个):
  - button x2, 宽=180px, 高=40px, 圆角=4px
    说明: 橙色背景按钮，白色文字，显示‘GET A PROJECT QUOTE’
  - text x6, 宽=auto, 高=auto, 圆角=0
    说明: 深灰色标题文字和浅灰色正文文字，用于展示优势与缺点内容

**图片占位符** (1组):
  - **product** x2
    尺寸: 50% x auto, 比例: auto
    位置: 左右两侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Variety of Colors`
- **副标题**: `Drawbacks of Acrylic Kitchen Cabinets`
- **段落** (3个):
  - `Acrylic cabinets provide a variety of color choices to match your taste and enhance your kitchen's d...`
  - `Despite their strength, acrylic cabinets are readily scratched if improper maintenance is not given....`
  - `In the event of acrylic cabinets being damaged, repairs can be difficult. Extensive scratches or fra...`
- **按钮文字**: `GET A PROJECT QUOTE`, `GET A PROJECT QUOTE`

**响应式**: 平板设备下调整为1列布局，移动端图片宽度100%
**特效**: 按钮 hover 时可能有颜色加深效果，图片 hover 时无变化
**内容摘要**: 该区域主要展示亚克力橱柜的颜色多样性与缺点（易刮伤、修复选项有限），采用图文混排形式

---

### 分块 5: features
- **截图**: `acrylic-kitchen-cabinets_pixel_5.jpg`
- **建议模块名**: `acrylic-cabinet-comparison`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 2
- 水平间距: 30px, 垂直间距: 40px
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #222222
- 正文: #333333
- 边框: none

**字体**:
- 标题: 24px, 字重: 600
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - card x4, 宽=auto, 高=auto, 圆角=8px
    说明: 每个卡片包含左侧产品图片和右侧对比文字，展示亚克力橱柜与其他材料的差异

**图片占位符** (1组):
  - **product** x4
    尺寸: 300px x 200px, 比例: 4:3
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Acrylic Kitchen Cabinet vs. Other Materials: Which Is Ideal for Your Needs?`
- **段落** (4个):
  - `Acrylic cabinets provide a modern and sleek look, as opposed to traditional wood cabinets. Although ...`
  - `Acrylic and lacquer cabinets both have a shiny appearance. Yet, acrylic cabinets are favored by home...`
  - `Acrylic and laminate cabinets have different looks and longevity. Although acrylic cabinets provide ...`
- **卡片内容** (4个):
  - `Acrylic vs. Wood`: Acrylic cabinets provide a modern and sleek look, ...
  - `Acrylic vs. Lacquer`: Acrylic and lacquer cabinets both have a shiny app...
  - `Acrylic vs. Laminate`: Acrylic and laminate cabinets have different looks...

**响应式**: 平板设备显示2列，移动端设备显示1列
**特效**: 无
**内容摘要**: 该区域主要展示亚克力厨房橱柜与其他常见材料（木材、漆器、 laminate、PVC）的对比分析，突出各材料的优劣势，帮助用户选择适合的橱柜类型

---

### 分块 6: features
- **截图**: `acrylic-kitchen-cabinets_pixel_6.jpg`
- **建议模块名**: `kitchen-cabinets-comparison-features`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 2
- 水平间距: 30px, 垂直间距: 30px
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

**组件** (1个):
  - card x4, 宽=560px, 高=300px, 圆角=8px
    说明: 包含图片和文字的对比卡片，展示亚克力橱柜与其他材料的差异

**图片占位符** (1组):
  - **thumbnail** x4
    尺寸: 560px x 300px, 比例: 16:9
    位置: 网格排列, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Acrylic Kitchen Cabinet vs. Other Materials: Which Is Ideal for Your Needs?`
- **段落** (4个):
  - `Acrylic cabinets provide a modern and sleek look, as opposed to traditional wood cabinets. Although ...`
  - `Acrylic and lacquer cabinets both have a shiny appearance. Yet, acrylic cabinets are favored by home...`
  - `Acrylic and laminate cabinets have different looks and longevity. Although acrylic cabinets provide ...`
- **卡片内容** (4个):
  - `Acrylic vs. Wood`: Acrylic cabinets provide a modern and sleek look, ...
  - `Acrylic vs. Lacquer`: Acrylic and lacquer cabinets both have a shiny app...
  - `Acrylic vs. Laminate`: Acrylic and laminate cabinets have different looks...

**响应式**: 平板设备显示2列，移动端设备显示1列
**特效**: 无
**内容摘要**: 该区域主要展示亚克力厨房橱柜与其他材料（木材、漆器、 laminate、PVC）的对比，通过图片和文字说明各材料的优缺点，帮助用户根据需求选择合适的橱柜材料

---

### 分块 7: content-block
- **截图**: `acrylic-kitchen-cabinets_pixel_7.jpg`
- **建议模块名**: `acrylic-cabinets-details`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 2
- 水平间距: 30px, 垂直间距: 20px
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #222222
- 正文: #333333
- 边框: none

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 20px
- 卡片内边距: 20px

**组件** (2个):
  - image x2, 宽=50%, 高=auto, 圆角=0
    说明: 展示定制亚克力橱柜细节的图片，左侧为厨房场景图，右侧为橱柜局部图
  - button x1, 宽=120px, 高=40px, 圆角=8px
    说明: 橙色背景按钮，文字为白色，用于获取项目报价

**图片占位符** (1组):
  - **product** x2
    尺寸: 50% x auto, 比例: 16:9
    位置: 左右并列排列, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Custom Acrylic Kitchen Cabinets`
- **段落** (4个):
  - `The material of the carcass is crucial in deciding how long the kitchen cabinet lasts, specifically ...`
  - `Frequently, the acrylic kitchen cabinet door will have the same acrylic finish as the rest of the ca...`
  - `Acrylic kitchen cabinets are available in numerous colors including black, gray, red, white, yellow,...`
- **按钮文字**: `GET A PROJECT QUOTE`

**响应式**: 平板设备下调整为1列布局，移动端单列显示，图片宽度100%
**特效**: 按钮 hover 时可能触发颜色变化或阴影效果，图片 hover 无明显交互
**内容摘要**: 该区域详细展示定制亚克力厨房橱柜的关键组成部分（柜体材料、门、颜色、台面）的特性和选择建议

---

### 分块 8: content-block
- **截图**: `acrylic-kitchen-cabinets_pixel_8.jpg`
- **建议模块名**: `kitchen-cabinets-content-block`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 60px
- 对齐: space-between

**颜色**:
- 背景: #ffffff
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
- 元素间距: 20px
- 卡片内边距: 15px

**组件** (3个):
  - text x1, 宽=50%, 高=auto, 圆角=0
    说明: 左侧文本块，背景色#D47A7A，白色文字，包含Hardware标题和段落内容
  - image x1, 宽=50%, 高=auto, 圆角=0
    说明: 右侧厨房橱柜图片，展示Hardware部分对应场景
  - card x2, 宽=48%, 高=auto, 圆角=8px
    说明: 5 Types of Acrylic Sheeting子项卡片，包含标题和缩略图

**图片占位符** (2组):
  - **background** x1
    尺寸: 100% x auto, 比例: auto
    位置: 右侧, object-fit: cover
    占位符建议: kitchen-cabinet-hardware
  - **thumbnail** x2
    尺寸: 300px x 200px, 比例: 3:2
    位置: 卡片内左侧, object-fit: cover
    占位符建议: acrylic-sheeting

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Hardware`
- **段落** (2个):
  - `In addition to minimizing wear and tear and preventing fingerprints, cabinet hardware also serves as...`
  - `Although any hardware will do, scroll pulls, bar pulls, bronze cup pull-outs, and steel knobs are th...`
- **卡片内容** (2个):
  - `Clear Acrylic Sheeting`: One of the most popular options for kitchen cabine...
  - `White Acrylic Sheeting`: White acrylic sheets exude minimalism and cleanlin...

**响应式**: 平板设备下Hardware部分改为单列布局，5 Types子项改为1列；移动端所有内容单列显示
**特效**: Hardware文本块背景色#D47A7A与右侧图片形成对比，5 Types子项卡片 hover 时可能显示更多细节
**内容摘要**: 该区域展示定制亚克力厨房橱柜的Hardware部分（图文混排）及5种亚克力板材类型（产品网格）

---

### 分块 9: product-grid
- **截图**: `acrylic-kitchen-cabinets_pixel_9.jpg`
- **建议模块名**: `kitchen-acrylic-sheeting-grid`

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
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - card x5, 宽=auto, 高=auto, 圆角=8px
    说明: 包含产品图片、标题和描述的白色卡片，无阴影，无边框，图片与文字左右排列

**图片占位符** (1组):
  - **product** x5
    尺寸: 300px x 200px, 比例: 16:9
    位置: 网格排列（每行2个，共3行）, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `5 Types of Acrylic Sheeting for Kitchen Cabinet`
- **段落** (5个):
  - `One of the most popular options for kitchen cabinets is clear acrylic sheets. These sheets offer cab...`
  - `White acrylic sheets exude minimalism and cleanliness, making them ideal for kitchen cabinets. They ...`
  - `A terrific alternative for anyone wishing to add color to their kitchen are colorful acrylic sheets....`
- **卡片内容** (5个):
  - `Clear Acrylic Sheeting`: One of the most popular options for kitchen cabine...
  - `White Acrylic Sheeting`: White acrylic sheets exude minimalism and cleanlin...
  - `Colored Acrylic Sheeting`: A terrific alternative for anyone wishing to add c...

**响应式**: 平板设备显示2列，移动端设备显示1列
**特效**: 图片hover时可能显示轻微阴影或缩放效果（截图中未明确显示，但常见于产品网格）
**内容摘要**: 该区域主要展示五种厨房橱柜用亚克力板材的类型（透明、白色、彩色、镜面、漫光）及其特点

---

### 分块 10: product-grid
- **截图**: `acrylic-kitchen-cabinets_pixel_10.jpg`
- **建议模块名**: `acrylic-sheeting-product-grid`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 3
- 水平间距: 20px, 垂直间距: 30px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #000000
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
  - card x5, 宽=50%, 高=auto, 圆角=8px
    说明: 白色卡片，显示产品图片和描述文字，无阴影和边框

**图片占位符** (1组):
  - **product** x5
    尺寸: 100% x auto, 比例: 16:9
    位置: 网格排列（每列1张，共2列）, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `5 Types of Acrylic Sheeting for Kitchen Cabinet`
- **段落** (5个):
  - `One of the most popular options for kitchen cabinets is clear acrylic sheets. These sheets offer cab...`
  - `White acrylic sheets exude minimalism and cleanliness, making them ideal for kitchen cabinets. They ...`
  - `A terrific alternative for anyone wishing to add color to their kitchen are colorful acrylic sheets....`
- **卡片内容** (5个):
  - `Clear Acrylic Sheeting`: One of the most popular options for kitchen cabine...
  - `White Acrylic Sheeting`: White acrylic sheets exude minimalism and cleanlin...
  - `Colored Acrylic Sheeting`: A terrific alternative for anyone wishing to add c...

**响应式**: 平板设备显示2列，移动端设备显示1列
**特效**: 无显著特殊效果，图片采用cover方式填充，保持比例
**内容摘要**: 该区域主要展示5种适用于厨房橱柜的丙烯酸板材类型，每个类型包含图片和详细描述，用于帮助用户了解不同板材的特点和适用场景

---

### 分块 11: contact-form
- **截图**: `acrylic-kitchen-cabinets_pixel_11.jpg`
- **建议模块名**: `contact-form-quote`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #4a5568
- 标题: #222222
- 正文: #333333
- 边框: #e2e8f0

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 20px
- 卡片内边距: 30px

**组件** (5个):
  - avatar x1, 宽=200px, 高=200px, 圆角=8px
    说明: 产品经理头像，位于左侧，右上角显示‘Product Manager’蓝色标签
  - input x5, 宽=460px, 高=40px, 圆角=4px
    说明: 表单输入框，包括Name、Email、Tel/Whatsapp、City、Country-Select五个字段，边框为浅灰色
  - checkbox x10, 宽=auto, 高=auto, 圆角=0
    说明: Product Needed*下的复选框，包含Kitchen cabinet、Bedroom、Bathroom、Windows & Doors、Furniture、Lighting、Soft Furnishing、Tiles and Wood Flooring、Whole House Solution、Other Building Material十个选项
  - textarea x1, 宽=100%, 高=120px, 圆角=4px
    说明: Message文本框，用于输入项目详情，边框为浅灰色
  - button x2, 宽=auto, 高=40px, 圆角=4px
    说明: Choose File按钮（文件上传）和Send按钮（提交表单），Send按钮为深灰色主按钮

**图片占位符** (1组):
  - **avatar** x1
    尺寸: 200px x 200px, 比例: 1:1
    位置: 左侧, object-fit: cover
    占位符建议: product-manager-avatar

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Get A Free Quote`
- **副标题**: `* Kindly send us your project details and floor plan. We will quote for you within 8 hours!`
- **段落** (2个):
  - `Want to Get Best Price Kitchen Cabinets?`
  - `Share floor plan or house photos for 8-hour quote`
- **按钮文字**: `Choose File`, `Send`

**响应式**: 平板设备（768px-1024px）将两列布局改为单列，移动端（<768px）输入框、复选框、文本框均占100%宽度，按钮居中显示
**特效**: Send按钮 hover 时颜色加深（如#3a4a58），输入框 focus 时边框变为品牌色（如#4a5568）
**内容摘要**: 该区域为联系表单模块，核心功能是收集用户项目信息以提供免费报价，包含个人信息输入、产品需求选择、留言上传及提交按钮，左侧搭配产品经理头像增强信任感

---

### 分块 12: contact-form
- **截图**: `acrylic-kitchen-cabinets_pixel_12.jpg`
- **建议模块名**: `free-quote-form`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #666666
- 标题: #222222
- 正文: #333333
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

**组件** (6个):
  - image x1, 宽=200px, 高=200px, 圆角=0
    说明: 左侧Product Manager头像图片，方形，无阴影
  - text x2, 宽=auto, 高=auto, 圆角=0
    说明: 左侧标题和副标题文字块，无装饰
  - input x5, 宽=100%, 高=45px, 圆角=4px
    说明: 表单输入框（Name、Email、Tel/Whatsapp、City、Country-Select），带浅灰色边框
  - checkbox x9, 宽=auto, 高=auto, 圆角=0
    说明: Product Needed*下的复选框选项，无装饰
  - textarea x1, 宽=100%, 高=120px, 圆角=4px
    说明: Message文本框，带浅灰色边框
  - button x2, 宽=auto, 高=45px, 圆角=0
    说明: Choose File按钮（灰色边框）和Send按钮（深灰色背景）

**图片占位符** (1组):
  - **avatar** x1
    尺寸: 200px x 200px, 比例: 1:1
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Get A Free Quote`
- **副标题**: `* Kindly send us your project details and floor plan. We will quote for you within 8 hours!`
- **段落** (2个):
  - `Want to Get Best Price Kitchen Cabinets?`
  - `Share floor plan or house photos for 8-hour quote`
- **按钮文字**: `Choose File`, `Send`
- **列表项** (10个):
  - `Kitchen cabinet`: ...
  - `Bedroom`: ...
  - `Bathroom`: ...

**响应式**: 平板设备显示2列布局，移动端设备切换为1列布局（表单字段垂直堆叠）
**特效**: 无明确特殊效果，按钮 hover 时可能触发颜色变化（截图未显示）
**内容摘要**: 页面中部联系表单模块，用于收集用户项目详情和文件，提供8小时内免费报价服务

---

### 分块 13: footer
- **截图**: `acrylic-kitchen-cabinets_pixel_13.jpg`
- **建议模块名**: `footer-sections`

**布局**:
- 容器: full-width
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 30px, 垂直间距: 0px
- 对齐: space-between

**颜色**:
- 背景: #000000
- 主色: #666666
- 标题: #ffffff
- 正文: #ffffff
- 边框: none

**字体**:
- 标题: 18px, 字重: 700
- 正文: 14px, 字重: 400
- 行高: 1.5

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 15px
- 卡片内边距: 0px

**组件** (4个):
  - text x4, 宽=auto, 高=auto, 圆角=0
    说明: 白色标题文字，加粗，显示各模块名称（Products、One-Stop Solutions、Customer Services、Contact Us）
  - list x1, 宽=auto, 高=auto, 圆角=0
    说明: 白色列表项，显示产品、解决方案、客户服务链接
  - button x2, 宽=auto, 高=40px, 圆角=4px
    说明: 灰色背景按钮，白色文字，显示“Send”
  - input x2, 宽=auto, 高=40px, 圆角=4px
    说明: 白色背景输入框，显示“whatsapp”和“Email*”占位符

**图片占位符** (1组):
  - **none** x0
    尺寸: 0px x 0px, 比例: none
    位置: none, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **段落** (1个):
  - `Don't miss our future updates! Get Subscribed Today!`
- **按钮文字**: `Send`, `Send`
- **列表项** (21个):
  - `Kitchen Cabinet`: ...
  - `Wardrobe`: ...
  - `Windows and Doors`: ...

**响应式**: 平板设备下footer列调整为2列，移动端设备下footer列堆叠为1列
**特效**: 无
**内容摘要**: 页面底部footer区域，展示产品分类、一站式解决方案、客户服务链接、联系方式及订阅表单

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
    --color-border: #e0e0e0;
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
    --spacing-module-top: 60px;
    --spacing-module-bottom: 60px;
    --spacing-element: 15px;
    --spacing-card-padding: 0px;
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
- `acrylic-kitchen-cabinets_pixel_1.jpg`
- `acrylic-kitchen-cabinets_pixel_10.jpg`
- `acrylic-kitchen-cabinets_pixel_11.jpg`
- `acrylic-kitchen-cabinets_pixel_12.jpg`
- `acrylic-kitchen-cabinets_pixel_13.jpg`
- `acrylic-kitchen-cabinets_pixel_2.jpg`
- `acrylic-kitchen-cabinets_pixel_3.jpg`
- `acrylic-kitchen-cabinets_pixel_4.jpg`
- `acrylic-kitchen-cabinets_pixel_5.jpg`
- `acrylic-kitchen-cabinets_pixel_6.jpg`
- `acrylic-kitchen-cabinets_pixel_7.jpg`
- `acrylic-kitchen-cabinets_pixel_8.jpg`
- `acrylic-kitchen-cabinets_pixel_9.jpg`

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
