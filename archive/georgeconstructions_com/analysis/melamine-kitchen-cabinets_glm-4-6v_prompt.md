# WordPress 页面克隆任务

## 原始页面信息
- URL: https://georgeconstructions.com/melamine-kitchen-cabinets/
- 标题: Melamine Kitchen Cabinets - George
- 总高度: 10947px

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
- **截图**: `melamine-kitchen-cabinets_pixel_1.jpg`
- **建议模块名**: `kitchen-cabinets-hero`

**布局**:
- 容器: full-width
- 类型: flex
- 列数: 1, 行数: 1
- 水平间距: 0px, 垂直间距: 0px
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #ffffff
- 正文: #333333
- 边框: none

**字体**:
- 标题: 48px, 字重: 700
- 正文: 18px, 字重: 400
- 行高: 1.5

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 0px
- 卡片内边距: 0px

**组件** (2个):
  - navbar x1, 宽=100%, 高=80px, 圆角=0
    说明: 顶部导航栏，包含logo、菜单项和按钮，背景为白色
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 橙色背景的“Quick Quote”按钮，位于导航栏右侧

**图片占位符** (1组):
  - **hero-banner** x1
    尺寸: 100% x auto, 比例: 16:9
    位置: 全屏背景, object-fit: cover
    遮罩: rgba(0,0,0,0.3)
    占位符建议: 厨房场景背景图

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `MELAMINE KITCHEN CABINETS`
- **副标题**: `One-Stop Building Material Solution Supplier`
- **按钮文字**: `Quick Quote`

**响应式**: 导航栏在移动端可能折叠为汉堡菜单，hero区域图片自适应屏幕宽度
**特效**: hero背景图带有半透明黑色叠加层，提升文字可读性
**内容摘要**: 页面顶部主视觉横幅，展示厨房橱柜产品，包含导航栏和核心产品信息

---

### 分块 2: product-grid
- **截图**: `melamine-kitchen-cabinets_pixel_2.jpg`
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
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - card x6, 宽=320px, 高=300px, 圆角=8px, 有阴影
    说明: 浅灰色背景卡片，包含厨房橱柜产品图片、标题和描述文字，带轻微阴影效果

**图片占位符** (1组):
  - **product** x6
    尺寸: 320px x 200px, 比例: 16:9
    位置: 网格排列（2行3列）, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Custom Melamine Cabinets`
- **卡片内容** (6个):
  - `Wood Grain Melamine Cabinets`: Modern Wood Grain Melamine Kitchen Cabinets Design...
  - `White Melamine Kitchen Cabinets`: Are you considering renovating or updating kitchen...
  - `Modern Black Melamine Kitchen Cabinets`: Black Melamine Kitchen Cabinet for Sale Both in cu...

**响应式**: 平板设备显示2列，移动端显示1列（卡片垂直堆叠）
**特效**: 卡片hover时可能触发阴影加深或文字颜色变化（截图中未显示，但为常见交互效果）
**内容摘要**: 该区域主要展示6种不同风格的定制三聚氰胺厨房橱柜产品，包括木纹、白色、黑色、极简、设计款和灰色款式，每个产品卡片包含图片、标题和简要描述

---

### 分块 3: content-block
- **截图**: `melamine-kitchen-cabinets_pixel_3.jpg`
- **建议模块名**: `melamine-info-content-block`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 3
- 水平间距: 20px, 垂直间距: 40px
- 对齐: left

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
- 元素间距: 40px
- 卡片内边距: 20px

**组件** (4个):
  - image x3, 宽=480px, 高=auto, 圆角=0
    说明: 左侧堆叠板材图片（Melamine: What Is It?部分）、右侧目录图片（CTA部分）、左侧灰色柜子图片（What Are Melamine Wood Cabinets部分），均为产品/信息展示图片
  - button x1, 宽=120px, 高=40px, 圆角=4px
    说明: 橙色背景、白色文字的'Consult'按钮，位于CTA区域
  - heading x2, 宽=auto, 高=auto, 圆角=0
    说明: 深灰色主标题（Melamine: What Is It?、What Are Melamine Wood Cabinets），粗体显示
  - text x6, 宽=auto, 高=auto, 圆角=0
    说明: 浅灰色正文段落，介绍Melamine的定义、特点及木柜信息

**图片占位符** (3组):
  - **image** x1
    尺寸: 480px x auto, 比例: 4:3
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg
  - **gallery** x1
    尺寸: 480px x auto, 比例: auto
    位置: 右侧, object-fit: contain
    占位符建议: product-catalog
  - **image** x1
    尺寸: 480px x auto, 比例: 4:3
    位置: 左侧, object-fit: cover
    占位符建议: gray-cabinet

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Melamine: What Is It?`
- **段落** (6个):
  - `We might as well start with the 'science bit.'`
  - `Essentially, it is a board made of raw particle board with resin-infused paper decorated with a spec...`
  - `When the resin is subjected to heat and pressure, it securely seals the substrate.`
- **按钮文字**: `Consult`

**响应式**: 平板端调整为1列布局（图片与文字堆叠），移动端保持1列，按钮宽度自适应
**特效**: 按钮 hover 时可能呈现颜色加深效果（如#E67E00），图片 hover 时可能有轻微缩放动画
**内容摘要**: 该区域主要介绍Melamine材料的定义、制作工艺及Melamine木柜的特点，包含图文混排内容和下载目录的CTA按钮

---

### 分块 4: features
- **截图**: `melamine-kitchen-cabinets_pixel_4.jpg`
- **建议模块名**: `melamine-kitchen-cabinets-features`

**布局**:
- 容器: container-1200
- 类型: block
- 列数: 1, 行数: 1
- 水平间距: 0px, 垂直间距: 0px
- 对齐: left

**颜色**:
- 背景: #f8f8f8
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
- 元素间距: 20px
- 卡片内边距: 0px

**组件** (1个):
  - text x1, 宽=auto, 高=auto, 圆角=0px
    说明: 文本内容块，包含标题和多个段落，描述 melamine 厨房橱柜的特色与优势

**图片占位符** (1组):
  - **background** x0
    尺寸: 0px x 0px, 比例: auto
    位置: 无, object-fit: none
    占位符建议: 无

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Features & Benefits of Melamine Kitchen Cabinets`
- **段落** (3个):
  - `Melamine cabinets are available in both glossy and matte finishes, allowing you to pick based on whe...`
  - `The popularity of melamine cabinets has grown in recent years due to their versatility. It is a high...`
  - `In summary, a melamine kitchen cabinet checked off all the boxes.`

**响应式**: 平板端和移动端保持单列布局，文本内容自适应宽度
**特效**: 无
**内容摘要**: 该区域主要展示 melamine 厨房橱柜的特色（如光泽/哑光 finishes、颜色选择）与优势（成本效益、耐用性、抗污/抗刮/耐高温/耐湿、承重能力强、易清洁维护）

---

### 分块 5: features
- **截图**: `melamine-kitchen-cabinets_pixel_5.jpg`
- **建议模块名**: `melamine-cabinets-features`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 2
- 水平间距: 30px, 垂直间距: 40px
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #222222
- 正文: #333333
- 边框: none

**字体**:
- 标题: 32px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - card x4, 宽=auto, 高=auto, 圆角=8px, 有阴影
    说明: 白色卡片，带轻微阴影，左侧/顶部嵌入图片，右侧/下方展示文字描述，卡片内容包含优势标题与详细说明

**图片占位符** (1组):
  - **thumbnail** x4
    尺寸: 300px x 200px, 比例: 3:2
    位置: 卡片左侧/顶部, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Pros of Melamine Kitchen Cabinet`
- **段落** (1个):
  - `If you're looking to install new kitchen cabinets or renovate your kitchen, Melamine is a common cho...`
- **卡片内容** (4个):
  - `Very cost-effective`: Cost plays a significant role for numerous homeown...
  - `Easy maintenance`: Melamine offers a selection of faux wood grains in...
  - `Durability`: Melamine is a strong material that is able to hand...

**响应式**: 平板端（768px-1024px）保持2列布局，移动端（<768px）调整为1列，卡片间距自适应缩小
**特效**: 卡片 hover 时阴影加深（box-shadow: 0 4px 12px rgba(0,0,0,0.15)），文字颜色从#333333变为#222222
**内容摘要**: 该区域以网格布局展示三聚氰胺厨房橱柜的核心优势，每个优势通过图片+文字卡片形式呈现，突出成本效益、易维护、耐用性等卖点

---

### 分块 6: features
- **截图**: `melamine-kitchen-cabinets_pixel_6.jpg`
- **建议模块名**: `custom-melamine-cabinets-ideas`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0px
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #444444
- 标题: #333333
- 正文: #666666
- 边框: none

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 50px
- 下边距: 50px
- 元素间距: 0px
- 卡片内边距: 25px

**组件** (1个):
  - card x2, 宽=570px, 高=auto, 圆角=0px
    说明: 深灰色背景卡片，包含标题和段落文字，无阴影和边框

**图片占位符** (1组):
  - **none** x0
    尺寸: 0px x 0px, 比例: auto
    位置: 无, object-fit: none
    占位符建议: 无

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Custom Melamine kitchen cabinets ideas`
- **段落** (1个):
  - `Melamine kitchen cabinets are a very popular option for modern kitchens because they combine excelle...`
- **卡片内容** (2个):
  - `Styles of Kitchen Cabinets`: We offer a plethora of melamine kitchen cabinet de...
  - `Colors of Kitchen Cabinets`: Patterned and solid color choices are offered for ...

**响应式**: 平板设备显示2列，移动端设备显示1列
**特效**: 无
**内容摘要**: 该区域主要展示定制三聚氰胺厨房橱柜的两种核心选项：橱柜风格和颜色选择，强调其设计多样性和个性化定制能力

---

### 分块 7: features
- **截图**: `melamine-kitchen-cabinets_pixel_7.jpg`
- **建议模块名**: `kitchen-cabinets-features`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 2
- 水平间距: 30px, 垂直间距: 30px
- 对齐: space-between

**颜色**:
- 背景: #f5f5f5
- 主色: #555555
- 标题: #ffffff
- 正文: #ffffff
- 边框: none

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 50px
- 下边距: 50px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - card x4, 宽=50%, 高=auto, 圆角=0
    说明: 深灰色背景卡片，包含标题和段落，无阴影和边框

**图片占位符** (1组):
  - **thumbnail** x4
    尺寸: 100% x auto, 比例: 16:9
    位置: 网格排列（2列2行）, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Custom Melamine kitchen cabinets ideas`
- **副标题**: `Melamine kitchen cabinets are a very popular option for modern kitchens because they combine excellent durability and elegance. This is the option for you if you're searching for reasonably priced cabinets that will last for a long time. There aren't many places that offer as many options as George does for melamine kitchen cabinets.`
- **段落** (4个):
  - `We offer a plethora of melamine kitchen cabinet designs for you to choose from. You have the option ...`
  - `Patterned and solid color choices are offered for melamine kitchen cabinets. You have the option of ...`
  - `U-shaped, L-shaped, island, and more are among your options. Putting together the perfect cabinet la...`
- **卡片内容** (4个):
  - `Styles of Kitchen Cabinets`: We offer a plethora of melamine kitchen cabinet de...
  - `Colors of Kitchen Cabinets`: Patterned and solid color choices are offered for ...
  - `Custom Kitchen Cabinet Layout`: U-shaped, L-shaped, island, and more are among you...

**响应式**: 平板端2列，移动端1列
**特效**: 无特殊动画效果，卡片布局简洁，重点突出文字内容
**内容摘要**: 该区域主要展示定制三聚氰胺厨房橱柜的四个核心特色：橱柜风格、颜色选择、定制布局和当代材料，每个特色以卡片形式呈现，包含标题和详细描述

---

### 分块 8: content-block
- **截图**: `melamine-kitchen-cabinets_pixel_8.jpg`
- **建议模块名**: `kitchen-color-trends`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 2
- 水平间距: 30px, 垂直间距: 30px
- 对齐: center

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
- 上边距: 40px
- 下边距: 40px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (2个):
  - card x4, 宽=auto, 高=auto, 圆角=8px
    说明: 浅灰色背景卡片，包含标题和描述文字，排列为2列2行网格
  - button x1, 宽=120px, 高=40px, 圆角=4px
    说明: 橙色背景按钮，白色文字，位于标题下方

**图片占位符** (1组):
  - **background** x0
    尺寸: 0 x 0, 比例: auto
    位置: none, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Kitchen Color Trends`
- **副标题**: `如果正在更新当前的家或翻新刚买的房子以更好地适应未来的需求，我们整理了一些现代橱柜颜色趋势，给你一些想法。这些颜色趋势中的很多都表明，房间正在被更有意识地规划，有效地将风格与功能结合起来。`
- **按钮文字**: `Consult`
- **卡片内容** (4个):
  - `Cool, Comfortable Blues`: Blues complement the neutral palette nicely, makin...
  - `Whites and Off-Whites`: White cabinets symbolize a longing for a clean liv...
  - `Color Blocking`: Vibrant blocks of rich, traditional colors will br...

**响应式**: 平板设备显示2列，移动端设备显示1列
**特效**: 无
**内容摘要**: 该区域主要展示厨房颜色趋势，包括四种不同的颜色风格（冷蓝色、白色/米白色、色彩块、双色橱柜），每种风格配有详细描述，帮助用户了解现代厨房颜色的流行趋势

---

### 分块 9: features
- **截图**: `melamine-kitchen-cabinets_pixel_9.jpg`
- **建议模块名**: `kitchen-color-trends`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 2
- 水平间距: 30px, 垂直间距: 30px
- 对齐: left

**颜色**:
- 背景: #f8f8f8
- 主色: #FF8C00
- 标题: #333333
- 正文: #666666
- 边框: none

**字体**:
- 标题: 36px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (2个):
  - card x4, 宽=50%, 高=auto, 圆角=8px
    说明: 白色卡片，无阴影，显示颜色趋势标题和描述
  - button x1, 宽=120px, 高=40px, 圆角=4px
    说明: 橙色按钮，白色文字，位于主标题下方

**图片占位符** (1组):
  - **none** x0
    尺寸: 0 x 0, 比例: none
    位置: none, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Kitchen Color Trends`
- **副标题**: `If you're updating your current home or remodeling a recently bought one to better suit your future requirements, we've put together some modern cabinet color trends to give you ideas. A lot of these color trends indicate a move towards rooms being planned with more intention, combining style with functionality effectively.`
- **段落** (4个):
  - `Blues complement the neutral palette nicely, making them a calming choice for modern kitchens and ba...`
  - `White cabinets symbolize a longing for a clean living space and provide the opportunity for adaptabl...`
  - `Vibrant blocks of rich, traditional colors will bring a feeling of opulence to our lives. Shiny blac...`
- **按钮文字**: `Consult`
- **卡片内容** (4个):
  - `Cool, Comfortable Blues`: Blues complement the neutral palette nicely, makin...
  - `Whites and Off-Whites`: White cabinets symbolize a longing for a clean liv...
  - `Color Blocking`: Vibrant blocks of rich, traditional colors will br...

**响应式**: 平板设备显示2列，移动端设备显示1列
**特效**: 按钮 hover 时可能显示橙色加深效果
**内容摘要**: 该区域主要展示现代厨房橱柜的颜色趋势，包括四种不同的颜色风格：舒适蓝、白与米白、色彩块和双色橱柜

---

### 分块 10: features-service
- **截图**: `melamine-kitchen-cabinets_pixel_10.jpg`
- **建议模块名**: `customizing-melamine-cabinets-features`

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
- 上边距: 40px
- 下边距: 40px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - card x6, 宽=50%, 高=auto, 圆角=0
    说明: 白色卡片，显示定制melamine厨房橱柜的各个特色（颜色、台面、柜体结构、照明、硬件、门）的标题和描述

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Customizing Melamine Kitchen Cabinets`
- **段落** (6个):
  - `There are many different color choices for melamine kitchen cabinets. You can choose a hue that comp...`
  - `The inner structure of the cabinets is referred to as the carcass. Particleboard elements like MCF, ...`
  - `Cabinet hardware includes handles, knobs, locks, hinges, backplates, and latches, all of which are e...`
- **卡片内容** (6个):
  - `Color`: There are many different color choices for melamin...
  - `Countertops`: Countertops will be regularly utilized for prepari...
  - `Carcass Composition`: The inner structure of the cabinets is referred to...

**响应式**: 平板设备显示2列，移动端设备显示1列
**特效**: 无明确特殊效果，卡片布局简洁，注重内容可读性
**内容摘要**: 该区域主要展示定制melamine厨房橱柜的六大特色方面，包括颜色选择、台面材质、柜体结构、照明设计、硬件配件及门体构造，为用户提供定制橱柜的详细选项说明

---

### 分块 11: content-block
- **截图**: `melamine-kitchen-cabinets_pixel_11.jpg`
- **建议模块名**: `kitchen-cabinets-customization-options`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 3
- 水平间距: 30px, 垂直间距: 30px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #222222
- 正文: #666666
- 边框: none

**字体**:
- 标题: 24px, 字重: 600
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 50px
- 下边距: 50px
- 元素间距: 0
- 卡片内边距: 20px

**组件** (2个):
  - card x6, 宽=auto, 高=auto, 圆角=8px
    说明: 白色背景卡片，包含标题和段落，无阴影和边框
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 橙色背景按钮，白色文字，位于模块上方

**图片占位符** (1组):
  - **none** x0
    尺寸: 0 x 0, 比例: none
    位置: none, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **段落** (6个):
  - `There are many different color choices for melamine kitchen cabinets. You can choose a hue that comp...`
  - `Countertops will be regularly utilized for preparing food, handling kitchen appliances, and performi...`
  - `The inner structure of the cabinets is referred to as the carcass. Particleboard elements like MCF, ...`
- **按钮文字**: `Consult`
- **卡片内容** (6个):
  - `Color`: There are many different color choices for melamin...
  - `Countertops`: Countertops will be regularly utilized for prepari...
  - `Carcass Composition`: The inner structure of the cabinets is referred to...

**响应式**: 平板设备显示2列，移动端显示1列
**特效**: 无
**内容摘要**: 该区域主要展示定制厨房橱柜的六大选项：颜色、台面、柜体结构、照明、五金件和门，每个选项包含详细说明

---

### 分块 12: content-block
- **截图**: `melamine-kitchen-cabinets_pixel_12.jpg`
- **建议模块名**: `kitchen-cabinets-tips`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 20px, 垂直间距: 30px
- 对齐: center

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
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (2个):
  - card x4, 宽=100%, 高=auto, 圆角=8px, 有阴影
    说明: 白色卡片，带轻微阴影，用于展示技巧内容
  - button x1, 宽=auto, 高=40px, 圆角=4px, 有阴影
    说明: 橙色背景按钮，白色文字，居中显示

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `4 Tips for Choosing the Melamine Kitchen Cabinets`
- **副标题**: `Consider the following ideas when choosing melamine kitchen cabinets for your area:`
- **按钮文字**: `Consult`

**响应式**: 平板设备下调整为2列布局，移动端设备下调整为1列布局
**特效**: 按钮 hover 时背景色加深，卡片 hover 时阴影效果增强
**内容摘要**: 该区域主要展示选择三聚氰胺厨房橱柜的4个关键技巧，包括前期研究、需求分析、预算考虑及专业咨询建议

---

### 分块 13: features
- **截图**: `melamine-kitchen-cabinets_pixel_13.jpg`
- **建议模块名**: `melamine-cabinets-tips`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: #f5f5f5
- 主色: #FF8C00
- 标题: #333333
- 正文: #666666
- 边框: none

**字体**:
- 标题: 28px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - card x4, 宽=100%, 高=auto, 圆角=8px, 有阴影
    说明: 白色卡片，带轻微阴影，包含标题和段落内容

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `4 Tips for Choosing the Melamine Kitchen Cabinets`
- **副标题**: `Consider the following ideas when choosing melamine kitchen cabinets for your area:`
- **按钮文字**: `Consult`

**响应式**: 平板设备显示2列，移动端设备显示1列
**特效**: 按钮hover时颜色加深，卡片hover时阴影增强
**内容摘要**: 该区域主要展示选择三聚氰胺厨房橱柜的4个核心建议，通过卡片形式分点呈现

---

### 分块 14: features
- **截图**: `melamine-kitchen-cabinets_pixel_14.jpg`
- **建议模块名**: `kitchen-cabinets-features`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 20px, 垂直间距: 30px
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
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - card x4, 宽=auto, 高=auto, 圆角=8px
    说明: 浅灰色背景卡片，包含标题和段落，无阴影和边框

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Best Custom Melamine Kitchen Cabinets From China`
- **段落** (5个):
  - `Before purchasing melamine kitchen cabinets, conduct research to compare various brands and prices. ...`
  - `Think about how you want to use your kitchen and note the elements that are important to you. You wi...`
  - `After you have a clear idea of your desired features, go to showrooms to view various melamine kitch...`
- **卡片内容** (4个):
  - `Do Your Research:`: Before purchasing melamine kitchen cabinets, condu...
  - `Consider your needs:`: Think about how you want to use your kitchen and n...
  - `Consider Your Budget:`: After you have a clear idea of your desired featur...

**响应式**: 平板设备下调整为2列布局，移动端设备下调整为1列布局
**特效**: 无明显的动态效果，采用静态展示
**内容摘要**: 该区域主要展示购买美耐板厨房橱柜的四个关键要点（研究、需求分析、预算考虑、专业咨询）及公司简介

---

### 分块 15: footer
- **截图**: `melamine-kitchen-cabinets_pixel_15.jpg`
- **建议模块名**: `footer-sections`

**布局**:
- 容器: full-width
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 30px, 垂直间距: 40px
- 对齐: space-between

**颜色**:
- 背景: #000000
- 主色: #FF8C00
- 标题: #FFFFFF
- 正文: #CCCCCC
- 边框: none

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 0px

**组件** (3个):
  - text x22, 宽=auto, 高=auto, 圆角=0
    说明: footer各分栏的列表项文本，包括产品、解决方案、客户服务、联系信息的文字内容
  - input x2, 宽=200px, 高=40px, 圆角=4px
    说明: Contact Us部分的whatsapp和Email输入框，用于订阅更新
  - button x1, 宽=120px, 高=40px, 圆角=4px
    说明: Contact Us部分的Send按钮，用于提交订阅表单

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **按钮文字**: `Consult`, `Send`
- **列表项** (21个):
  - `Kitchen Cabinet`: ...
  - `Wardrobe`: ...
  - `Windows and Doors`: ...

**响应式**: 平板设备下footer分栏调整为2列，移动端设备下调整为1列堆叠布局
**特效**: 列表项 hover 时可能改变文字颜色或背景，输入框 focus 时可能有边框高亮效果
**内容摘要**: 页面底部footer区域，包含四个主要分栏：产品分类（Products）、一站式解决方案（One-Stop Solutions）、客户服务（Customer Services）、联系我们（Contact Us），提供产品列表、解决方案类型、客户服务信息和联系表单

---


## 设计参数汇总

### 颜色系统（CSS变量建议）
```css
:root {
    --color-primary: #FF8C00;
    --color-secondary: #333333;
    --color-background: #000000;
    --color-heading: #FFFFFF;
    --color-text: #CCCCCC;
    --color-border: #e0e0e0;
}
```

### 字体系统
```css
:root {
    --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    --font-size-h1: 24px;
    --font-size-body: 16px;
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
    --spacing-element: 30px;
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
- `melamine-kitchen-cabinets_pixel_1.jpg`
- `melamine-kitchen-cabinets_pixel_10.jpg`
- `melamine-kitchen-cabinets_pixel_11.jpg`
- `melamine-kitchen-cabinets_pixel_12.jpg`
- `melamine-kitchen-cabinets_pixel_13.jpg`
- `melamine-kitchen-cabinets_pixel_14.jpg`
- `melamine-kitchen-cabinets_pixel_15.jpg`
- `melamine-kitchen-cabinets_pixel_2.jpg`
- `melamine-kitchen-cabinets_pixel_3.jpg`
- `melamine-kitchen-cabinets_pixel_4.jpg`
- `melamine-kitchen-cabinets_pixel_5.jpg`
- `melamine-kitchen-cabinets_pixel_6.jpg`
- `melamine-kitchen-cabinets_pixel_7.jpg`
- `melamine-kitchen-cabinets_pixel_8.jpg`
- `melamine-kitchen-cabinets_pixel_9.jpg`

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
