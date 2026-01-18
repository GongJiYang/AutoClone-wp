# WordPress 页面克隆任务

## 原始页面信息
- URL: https://georgeconstructions.com/solid-wood-kitchen-cabinets/
- 标题: Best Solid Wood Kitchen Cabinets | Wood Kitchen Cabinets
- 总高度: 14107px

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
- **截图**: `solid-wood-kitchen-cabinets_pixel_1.jpg`
- **建议模块名**: `kitchen-cabinets-hero`

**布局**:
- 容器: full-width
- 类型: flex
- 列数: 1, 行数: 1
- 水平间距: 0, 垂直间距: 0
- 对齐: center

**颜色**:
- 背景: #FFFFFF
- 主色: #FF8C00
- 标题: #FFFFFF
- 正文: #333333
- 边框: none

**字体**:
- 标题: 48px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 0
- 卡片内边距: 0

**组件** (3个):
  - navbar x1, 宽=auto, 高=48px, 圆角=0
    说明: 白色导航栏，左侧包含George logo，中间7个导航链接（Products、Projects、Blog、Service、Video、About、Contact），右侧1个橙色Quick Quote按钮
  - hero-banner x1, 宽=100%, 高=auto, 圆角=0
    说明: 全宽背景图片，展示深色厨房场景，中间居中显示主标题和按钮
  - button x2, 宽=120px（Quick Quote）/150px（Download Catalog）, 高=40px, 圆角=4px
    说明: Quick Quote按钮为橙色（#FF8C00），白色文字；Download Catalog按钮为白色背景，黑色文字

**图片占位符** (1组):
  - **hero-banner** x1
    尺寸: 100% x auto, 比例: 16:9
    位置: 居中, object-fit: cover
    遮罩: rgba(0,0,0,0.5)
    占位符建议: 厨房场景图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `SOLID WOOD KITCHEN CABINETS`
- **按钮文字**: `Quick Quote`, `Download Catalog`

**响应式**: 平板端导航链接可能换行显示，移动端Quick Quote按钮可能调整为全宽，Download Catalog按钮缩小宽度
**特效**: 背景图片添加暗色（rgba(0,0,0,0.5)）叠加层，提升白色标题和按钮的可读性
**内容摘要**: 页面顶部主视觉区域，通过深色厨房背景图和白色标题突出产品主题，结合导航栏和行动按钮引导用户操作

---

### 分块 2: product-grid
- **截图**: `solid-wood-kitchen-cabinets_pixel_2.jpg`
- **建议模块名**: `kitchen-cabinets-product-grid`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 3, 行数: 2
- 水平间距: 24px, 垂直间距: 30px
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
  - card x6, 宽=auto, 高=auto, 圆角=8px
    说明: 浅灰色背景卡片，包含产品图片、标题和描述文字，无阴影和边框

**图片占位符** (1组):
  - **product** x6
    尺寸: 300px x auto, 比例: 4:3
    位置: 网格排列（卡片顶部）, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Custom Solid Wood Cabinets`
- **卡片内容** (6个):
  - `Traditional Solid Wood kitchen Cabinet for Sale`: In Europe and South East Asia, traditional kitchen...
  - `Solid Wood Shaker Kitchen Cabinets`: Shaker style cabinet doors are among our most popu...
  - `Solid Wood Rustic Kitchen Cabinet`: Rustic kitchen cabinets frequently display the woo...

**响应式**: 平板设备显示2列，移动端设备显示1列
**特效**: 无
**内容摘要**: 展示6种不同风格的实木厨房橱柜产品，每个产品卡片包含图片、标题和简要描述

---

### 分块 3: image-text
- **截图**: `solid-wood-kitchen-cabinets_pixel_3.jpg`
- **建议模块名**: `solid-wood-kitchen-image-text`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0px
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
- 元素间距: 30px
- 卡片内边距: 0px

**组件** (3个):
  - image x5, 宽=auto, 高=auto, 圆角=0px
    说明: 包含1张大尺寸厨房实景图（左侧）和4张小尺寸产品目录封面图（右侧），均无阴影和边框
  - button x1, 宽=120px, 高=40px, 圆角=4px
    说明: 橙色背景按钮，显示文字'Consult'
  - text x1, 宽=auto, 高=auto, 圆角=0px
    说明: 包含主标题和段落文字，文字左对齐

**图片占位符** (2组):
  - **product** x1
    尺寸: 400px x 250px, 比例: 16:9
    位置: 左侧, object-fit: cover
    占位符建议: kitchen-interior
  - **thumbnail** x4
    尺寸: 120px x 160px, 比例: 3:4
    位置: 右侧堆叠排列, object-fit: cover
    占位符建议: catalog-cover

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `In search of a Kitchen Made of Solid Wood?`
- **段落** (1个):
  - `Our cabinet makers utilize traditional construction techniques, such as mortise and tenon, and dovet...`
- **按钮文字**: `Consult`

**响应式**: 平板设备下，图片与文字调整为上下排列（图片在上，文字在下）；移动端下，图片和文字堆叠，按钮宽度100%
**特效**: 无明显的特殊效果，布局简洁直观
**内容摘要**: 该区域通过左侧厨房实景图与右侧文字说明，展示橱柜的传统制作工艺及核心特点，并引导用户下载产品目录

---

### 分块 4: content-block
- **截图**: `solid-wood-kitchen-cabinets_pixel_4.jpg`
- **建议模块名**: `cabinet-pricing-section`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 40px
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

**组件** (2个):
  - button x1, 宽=auto, 高=40px, 圆角=8px
    说明: 橙色按钮，显示'GET A PROJECT QUOTE'文字
  - text x2, 宽=auto, 高=auto, 圆角=0
    说明: 包含定价标题、段落和木材类型标题、段落的文本块

**图片占位符** (1组):
  - **product** x1
    尺寸: 50% x auto, 比例: 16:9
    位置: 右侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Transparent Cabinet Pricing`
- **段落** (4个):
  - `While it can be challenging to get solid wood kitchen cabinets at an inexpensive price, there's no r...`
  - `Wood cabinets are available in a wide range of hues, tones, and wood species, providing a unique ass...`
  - `It should be mentioned that premium timbers are both beautiful and long-lasting. The kitchen cabinet...`
- **按钮文字**: `GET A PROJECT QUOTE`

**响应式**: 平板设备显示2列布局，移动设备显示1列布局，按钮和文本自适应宽度
**特效**: 按钮hover时可能有颜色加深效果，图片hover时可能有轻微放大或阴影效果
**内容摘要**: 该区域主要展示透明橱柜定价信息以及9种木材橱柜的类型介绍，包含图文结合的内容块

---

### 分块 5: content-block
- **截图**: `solid-wood-kitchen-cabinets_pixel_5.jpg`
- **建议模块名**: `cabinet-pricing-wood-types-section`

**布局**:
- 容器: container-1200
- 类型: block
- 列数: 1, 行数: 2
- 水平间距: 0px, 垂直间距: 60px
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
- 上边距: 60px
- 下边距: 60px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (2个):
  - button x1, 宽=180px, 高=40px, 圆角=8px
    说明: 橙色按钮，文字为“GET A PROJECT QUOTE”
  - image x2, 宽=600px, 高=auto, 圆角=0
    说明: 厨房橱柜展示图片，分别位于定价模块右侧和木材类型模块左侧

**图片占位符** (1组):
  - **product** x2
    尺寸: 600px x auto, 比例: 16:9
    位置: 第一个位于定价模块右侧，第二个位于木材类型模块左侧, object-fit: cover
    占位符建议: kitchen-cabinet-image

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `['Transparent Cabinet Pricing', '9 Types of Wood Cabinets']`
- **段落** (4个):
  - `While it can be challenging to get solid wood kitchen cabinets at an inexpensive price, there's no r...`
  - `Wood cabinets are available in a wide range of hues, tones, and wood species, providing a unique ass...`
  - `It should be mentioned that premium timbers are both beautiful and long-lasting. The kitchen cabinet...`
- **按钮文字**: `GET A PROJECT QUOTE`

**响应式**: 平板设备下，两个模块变为单列，图片宽度100%；移动端下，图片和文字堆叠，按钮宽度100%
**特效**: 按钮hover时背景色加深，图片hover时轻微放大
**内容摘要**: 该区域展示橱柜定价信息和木材类型介绍，包含图文混排的定价模块和木材类型模块

---

### 分块 6: product-grid
- **截图**: `solid-wood-kitchen-cabinets_pixel_6.jpg`
- **建议模块名**: `wood-cabinets-types-grid`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 1, 行数: 4
- 水平间距: 20px, 垂直间距: 30px
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
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - card x4, 宽=auto, 高=auto, 圆角=8px
    说明: 每个卡片包含木柜类型的图片和文字描述，图片位于左侧，文字位于右侧，整体左对齐

**图片占位符** (1组):
  - **product** x4
    尺寸: 300px x 200px, 比例: 3:2
    位置: 左侧, object-fit: cover
    占位符建议: wood-cabinets-thumbnail

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `9 Types of Wood Cabinets`
- **段落** (4个):
  - `Walnuts range in hue from light reddish gray to deep chocolate brown, with a smooth, consistent text...`
  - `Strong and sturdy, hickory has an oak-like grain and is available in a wide variety of colors and to...`
  - `Red oak showcases unique curved and straight grain designs. Extremely robust, sturdy, long-lasting, ...`
- **列表项** (4个):
  - `3.Walnut Cabinets`: Walnuts range in hue from light reddish gray to de...
  - `4.Hickory Cabinets`: Strong and sturdy, hickory has an oak-like grain a...
  - `5.Red Oak Cabinets`: Red oak showcases unique curved and straight grain...

**响应式**: 平板端调整为2列布局，移动端保持1列，图片尺寸自适应缩小
**特效**: 无动态效果，采用静态图文混排展示
**内容摘要**: 该区域主要展示9种木柜类型中的第3至第6种（Walnut、Hickory、Red Oak、White Oak）的详细介绍，每个类型通过图片和文字结合的方式呈现，突出木柜的材质特点、外观特征及适用风格

---

### 分块 7: features-service
- **截图**: `solid-wood-kitchen-cabinets_pixel_7.jpg`
- **建议模块名**: `kitchen-cabinet-wood-types`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 1, 行数: 4
- 水平间距: 20px, 垂直间距: 30px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #8B4513
- 标题: #222222
- 正文: #333333
- 边框: none

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 30px
- 下边距: 30px
- 元素间距: 10px
- 卡片内边距: 15px

**组件** (1个):
  - card x4, 宽=100%, 高=auto, 圆角=8px
    说明: 白色卡片，包含木材类型图片和文字说明，图片与文字并排布局

**图片占位符** (1组):
  - **product** x4
    尺寸: 300px x 200px, 比例: 3:2
    位置: 左侧/右侧交替排列, object-fit: cover
    占位符建议: wood-texture-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **段落** (4个):
  - `White oak cabinets have a more understated grain and a golden hue compared to red oak. Slightly more...`
  - `Alder wood has a similar straight, fine-textured grain as cherry and maple. It is a type of lightwei...`
  - `Birch is a fine-textured, sturdy, and versatile wood that is often used for affordable cabinetry. Co...`
- **列表项** (4个):
  - `6.White Oak Cabinets`: White oak cabinets have a more understated grain a...
  - `7.Alder Cabinets`: Alder wood has a similar straight, fine-textured g...
  - `8.Birch Cabinets`: Birch is a fine-textured, sturdy, and versatile wo...

**响应式**: 移动端单列显示，平板端双列交替排列
**特效**: 无
**内容摘要**: 该区域主要展示厨房橱柜常用木材类型（白橡木、赤杨木、桦木、杨木）的特点、外观及适用风格

---

### 分块 8: content-block
- **截图**: `solid-wood-kitchen-cabinets_pixel_8.jpg`
- **建议模块名**: `kitchen-cabinets-poplar-advantages`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 1, 行数: 2
- 水平间距: 20px, 垂直间距: 40px
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
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (2个):
  - image x1, 宽=300px, 高=auto, 圆角=0px
    说明: Poplar Cabinets产品图片，左侧排列，展示浅色木质橱柜
  - button x1, 宽=120px, 高=40px, 圆角=4px, 有阴影
    说明: 橙色背景按钮，显示文字“Consult”，位于Advantages部分下方

**图片占位符** (1组):
  - **product** x1
    尺寸: 300px x auto, 比例: 16:9
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Advantages of Solid Wood Cabinets`
- **段落** (2个):
  - `One of the few softwoods utilized in cabinetry is poplar, one of the hardest varieties of wood. Its ...`
  - `Cabinet makers consider solid wood to be a superior material. Choosing alder, cherry, maple, or oak ...`
- **按钮文字**: `Consult`

**响应式**: 移动端Poplar Cabinets部分改为上下排列（图片在上，文字在下），Advantages部分保持居中
**特效**: 按钮hover时背景色加深，图片hover时轻微缩放
**内容摘要**: 展示Poplar橱柜的材质特点及 solid wood橱柜的优势，包含行动号召按钮引导用户咨询

---

### 分块 9: features
- **截图**: `solid-wood-kitchen-cabinets_pixel_9.jpg`
- **建议模块名**: `solid-wood-cabinets-advantages`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 1, 行数: 2
- 水平间距: 30px, 垂直间距: 40px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #000000
- 正文: #333333
- 边框: none

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 40px
- 下边距: 60px
- 元素间距: 20px
- 卡片内边距: 25px

**组件** (3个):
  - image-text x1, 宽=auto, 高=auto, 圆角=0
    说明: 左侧图片（poplar cabinets），右侧文字描述（包括标题和段落）
  - button x1, 宽=120px, 高=40px, 圆角=4px
    说明: 橙色背景按钮，文字为白色，显示“Consult”
  - card x3, 宽=auto, 高=auto, 圆角=0
    说明: 三个优势卡片，每个卡片包含标题和段落，背景为浅灰色

**图片占位符** (1组):
  - **product** x1
    尺寸: 350px x 200px, 比例: 16:9
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Advantages of Solid Wood Cabinets`
- **副标题**: `Cabinet makers consider solid wood to be a superior material. Choosing alder, cherry, maple, or oak comes with numerous advantages due to the use of solid wood. Here are 5 advantages of solid wood cabinets to assist you in making the ideal selection for your home.`
- **段落** (6个):
  - `One of the few softwoods utilized in cabinetry is poplar, one of the hardest varieties of wood. Its ...`
  - `It is light but sturdy, adaptable, and simple to paint (although it might need more paint than antic...`
  - `Favored by farmhouse, rustic, contemporary, and modern designs.`
- **按钮文字**: `Consult`
- **卡片内容** (3个):
  - `Customization`: You're getting the best return on your investment ...
  - `Aesthetics`: Any room can benefit from the beauty and coziness ...
  - `Durable & Strong`: Solid wood is utilized globally for constructing b...

**响应式**: 平板设备下，优势卡片调整为2列；移动端下，图片与文字堆叠，卡片调整为1列
**特效**: 按钮hover时背景色加深，卡片hover时轻微阴影
**内容摘要**: 该区域主要展示solid wood cabinets的优势，包括poplar橱柜的介绍及五个核心优势（Customization、Aesthetics、Durable & Strong等）

---

### 分块 10: features
- **截图**: `solid-wood-kitchen-cabinets_pixel_10.jpg`
- **建议模块名**: `kitchen-cabinets-advantages`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 1, 行数: 1
- 水平间距: 0px, 垂直间距: 30px
- 对齐: center

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
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 0px

**组件** (1个):
  - button x1, 宽=auto, 高=40px, 圆角=8px
    说明: 橙色填充按钮，白色文字，无阴影，位于段落下方

**图片占位符** (1组):
  - **none** x0
    尺寸: 0px x 0px, 比例: none
    位置: none, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Advantages of Solid Wood Cabinets`
- **段落** (1个):
  - `Cabinet makers consider solid wood to be a superior material. Choosing alder, cherry, maple, or oak ...`
- **按钮文字**: `Consult`

**响应式**: 平板及移动端保持1列布局，标题和段落自适应字体大小
**特效**: 按钮 hover 时可能触发颜色加深效果（未在截图中显示，但常见于此类模块）
**内容摘要**: 该区域主要展示固体木橱柜的优势，通过标题、说明文字和咨询按钮引导用户了解产品优势

---

### 分块 11: image-text
- **截图**: `solid-wood-kitchen-cabinets_pixel_11.jpg`
- **建议模块名**: `kitchen-cabinet-accessories`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 40px, 垂直间距: 0
- 对齐: center

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
- 元素间距: 0
- 卡片内边距: 0

**组件** (2个):
  - image x1, 宽=450px, 高=300px, 圆角=0
    说明: 厨房橱柜内部配件展示图片，左侧布局，无阴影和边框
  - text x1, 宽=auto, 高=auto, 圆角=0
    说明: 右侧文字内容区域，包含标题和段落

**图片占位符** (1组):
  - **product** x1
    尺寸: 450px x 300px, 比例: 3:2
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Inside Kitchen Cabinet Accessories`
- **副标题**: `Every centimeter is utilized efficiently here`
- **段落** (1个):
  - `Our natural wood kitchens have customised equipment that keeps ingredients and cookware easily acces...`

**响应式**: 平板端（768px-1024px）改为1列布局，图片在上、文字在下；移动端（<768px）保持1列，图片宽度100%，文字宽度100%
**特效**: 无特殊动画或交互效果，静态图文展示
**内容摘要**: 展示厨房橱柜内部配件的定制化设计，强调空间利用效率、人体工学及材料选择

---

### 分块 12: content-block
- **截图**: `solid-wood-kitchen-cabinets_pixel_12.jpg`
- **建议模块名**: `kitchen-cabinet-accessories-bar-elements`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 50px
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
- 上边距: 50px
- 下边距: 50px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (2个):
  - image x2, 宽=500px, 高=auto, 圆角=0
    说明: 左右排列的图片，分别展示吧台和延伸桌产品
  - button x1, 宽=auto, 高=40px, 圆角=8px, 有阴影
    说明: 橙色背景按钮，文字为“GET A PROJECT QUOTE”

**图片占位符** (1组):
  - **product** x2
    尺寸: 500px x auto, 比例: 16:9
    位置: 左右排列, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Bar elements, counters, extension tables`
- **副标题**: `Bars & counters`
- **段落** (2个):
  - `Different bar elements and counters create a social atmosphere in the kitchen, turning it into a pop...`
  - `You can quickly turn your kitchen into a full dining area and improve the homey atmosphere by employ...`
- **按钮文字**: `GET A PROJECT QUOTE`

**响应式**: 平板端2列，移动端1列
**特效**: 按钮hover时颜色加深，图片hover时轻微缩放
**内容摘要**: 展示厨房柜子配件中的吧台元素、延伸桌等内容，包含图文混排和行动号召按钮

---

### 分块 13: content-block
- **截图**: `solid-wood-kitchen-cabinets_pixel_13.jpg`
- **建议模块名**: `kitchen-cabinets-accessories`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 20px
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
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (2个):
  - image x2, 宽=400px, 高=300px, 圆角=0
    说明: 展示厨房吧台和延伸桌的产品图片，左右排列
  - button x1, 宽=150px, 高=40px, 圆角=8px, 有阴影
    说明: 橙色背景按钮，显示'GET A PROJECT QUOTE'文字

**图片占位符** (1组):
  - **product** x2
    尺寸: 400px x 300px, 比例: 4:3
    位置: 左右排列, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Bar elements, counters, extension tables`
- **副标题**: `Bars & counters`
- **段落** (2个):
  - `Different bar elements and counters create a social atmosphere in the kitchen, turning it into a pop...`
  - `You can quickly turn your kitchen into a full dining area and improve the homey atmosphere by employ...`
- **按钮文字**: `GET A PROJECT QUOTE`

**响应式**: 平板设备显示2列布局，移动端设备显示1列布局，图片宽度自适应
**特效**: 无
**内容摘要**: 该区域主要展示厨房吧台元素、延伸桌等配件，强调其功能性和设计感，并提供项目报价按钮

---

### 分块 14: why-choose
- **截图**: `solid-wood-kitchen-cabinets_pixel_14.jpg`
- **建议模块名**: `kitchen-cabinets-why-choose`

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
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 20px
- 卡片内边距: 0

**组件** (3个):
  - image x2, 宽=auto, 高=200px, 圆角=0
    说明: 左侧木块纹理图片（Why Choose Solid Wood?模块），右侧厨房安装场景图片（Easy to Install Kitchens模块）
  - text x4, 宽=auto, 高=auto, 圆角=0
    说明: 包含2个标题（Why Choose Solid Wood?、Easy to Install Kitchens）和2个段落（实心木优点、厨房安装说明）
  - faq x1, 宽=100%, 高=auto, 圆角=0
    说明: FAQs模块标题及第一个问题（Can you paint solid wood kitchen cabinets?）

**图片占位符** (1组):
  - **thumbnail** x2
    尺寸: 45% x 200px, 比例: auto
    位置: 左右两侧（Why Choose Solid Wood?左侧，Easy to Install Kitchens右侧）, object-fit: cover
    占位符建议: wood-texture-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Why Choose Solid Wood?`
- **副标题**: `Easy to Install Kitchens`
- **段落** (2个):
  - `Solid wood is both durable and extremely adaptable. Cabinets are essential in every kitchen and typi...`
  - `All our kitchen units made of real wood are delivered fully assembled and complete, resembling a sta...`

**响应式**: 平板端调整为1列布局，移动端保持1列，图片宽度自适应
**特效**: 无
**内容摘要**: 该区域主要展示实心木厨房橱柜的优势（耐用性、适应性、制作工艺）及安装便利性，同时开始介绍常见问题

---

### 分块 15: faq
- **截图**: `solid-wood-kitchen-cabinets_pixel_15.jpg`
- **建议模块名**: `kitchen-cabinets-faqs`

**布局**:
- 容器: container-1200
- 类型: block
- 列数: 1, 行数: 7
- 水平间距: 0px, 垂直间距: 30px
- 对齐: left

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
- 上边距: 30px
- 下边距: 30px
- 元素间距: 0px
- 卡片内边距: 0px

**组件** (1个):
  - card x7, 宽=100%, 高=auto, 圆角=0
    说明: 白色卡片，无阴影和边框，每个卡片包含问题标题和回答段落

**图片占位符** (1组):
  - **image-text** x1
    尺寸: 300px x auto, 比例: 1:1
    位置: 右侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `FAQs`
- **段落** (7个):
  - `Any surface that can be roughened with sandpaper is excellent for painting, but wooden cabinets are ...`
  - `Yes. When comparing solid wood cabinets with other cabinet materials, solid wood consistently proves...`
  - `When it comes to your cabinets, nothing beats the strength and durability of solid wood. If you want...`
- **卡片内容** (7个):
  - `Can you paint solid wood kitchen cabinets?`: Any surface that can be roughened with sandpaper i...
  - `Is it worth investing money in solid wood cabinets?`: Yes. When comparing solid wood cabinets with other...
  - `Are solid wood good for kitchen cabinets?`: When it comes to your cabinets, nothing beats the ...

**响应式**: 平板端1列显示，移动端1列显示，每个问题卡片保持完整宽度
**特效**: 无特殊动画或交互效果，仅静态内容展示
**内容摘要**: 该区域主要展示关于实木厨房橱柜的常见问题及详细回答，帮助用户了解实木橱柜的相关信息

---

### 分块 16: faq
- **截图**: `solid-wood-kitchen-cabinets_pixel_16.jpg`
- **建议模块名**: `kitchen-cabinets-faq`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 1, 行数: 1
- 水平间距: 0px, 垂直间距: 20px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #222222
- 正文: #333333
- 边框: #e0e0e0

**字体**:
- 标题: 36px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 40px
- 下边距: 30px
- 元素间距: 20px
- 卡片内边距: 15px

**组件** (2个):
  - card x5, 宽=100%, 高=auto, 圆角=8px
    说明: 浅灰色背景卡片，包含问题标题和回答内容，垂直排列
  - button x1, 宽=120px, 高=40px, 圆角=4px
    说明: 橙色背景按钮，显示‘Consult’文字

**图片占位符** (1组):
  - **none** x0
    尺寸: 0px x 0px, 比例: auto
    位置: none, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `FAQs`
- **段落** (7个):
  - `Any surface that can be roughened with sandpaper is excellent for painting, but wooden cabinets are ...`
  - `Yes. When comparing solid wood cabinets with other cabinet materials, solid wood consistently proves...`
  - `When it comes to your cabinets, nothing beats the strength and durability of solid wood. If you want...`
- **按钮文字**: `Consult`
- **卡片内容** (7个):
  - `Can you paint solid wood kitchen cabinets?`: Any surface that can be roughened with sandpaper i...
  - `Is it worth investing money in solid wood cabinets?`: Yes. When comparing solid wood cabinets with other...
  - `Are solid wood good for kitchen cabinets?`: When it comes to your cabinets, nothing beats the ...

**响应式**: 平板和移动端保持1列布局，桌面端1列，卡片间距自适应
**特效**: 无显著动画效果，卡片 hover 时可能显示轻微阴影（截图中未明确显示）
**内容摘要**: 展示关于厨房橱柜的常见问题及详细解答，涵盖喷漆可行性、投资价值、适用性、存在性、操作指南、成本替代选项及材质对比等内容

---

### 分块 17: 解析失败
- 截图: `solid-wood-kitchen-cabinets_pixel_17.jpg`
- 错误: 
{
    "module_type": "content-block",
    "module_name_suggestion": "kitchen-cabinets-comparison-an

### 分块 18: showroom-section
- **截图**: `solid-wood-kitchen-cabinets_pixel_18.jpg`
- **建议模块名**: `george-showroom-section`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 1, 行数: 4
- 水平间距: 0px, 垂直间距: 30px
- 对齐: left

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
- 卡片内边距: 0px

**组件** (4个):
  - text x1, 宽=auto, 高=auto, 圆角=0px
    说明: 主标题'Showroom'
  - text x2, 宽=auto, 高=auto, 圆角=0px
    说明: 段落文字，关于MDF和实木的决策，以及George的展厅介绍
  - list x1, 宽=auto, 高=auto, 圆角=0px
    说明: 包含8个列表项，展示产品类别
  - button x1, 宽=120px, 高=40px, 圆角=4px
    说明: 橙色按钮，白色文字，用于咨询

**图片占位符** (1组):
  - **hero-banner/product/thumbnail/avatar/icon/background/gallery** x0
    尺寸: auto x auto, 比例: auto
    位置: none, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Showroom`
- **段落** (2个):
  - `The decision between MDF and real wood ultimately comes down to your personal preferences for the st...`
  - `George has 20000㎡ showroom with the whole category of products, including`
- **按钮文字**: `Consult`
- **列表项** (8个):
  - `Kitchen Cabinets & Wardrobe`: ...
  - `Doors & Windows`: ...
  - `Bathroom Fitting & Tiles`: ...

**响应式**: 平板和移动端保持单列布局，内容垂直排列
**特效**: 无特殊效果，按钮 hover 可能会有颜色变化（如加深橙色）
**内容摘要**: 该区域展示George的展厅信息，包括展厅面积、产品类别以及咨询按钮，帮助用户了解展厅的规模和产品范围

---

### 分块 19: footer
- **截图**: `solid-wood-kitchen-cabinets_pixel_19.jpg`
- **建议模块名**: `footer-section`

**布局**:
- 容器: full-width
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 30px, 垂直间距: 20px
- 对齐: space-between

**颜色**:
- 背景: #000000
- 主色: #666666
- 标题: #ffffff
- 正文: #cccccc
- 边框: none

**字体**:
- 标题: 18px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 20px
- 卡片内边距: 0

**组件** (3个):
  - text/link x24, 宽=auto, 高=auto, 圆角=0
    说明: footer列中的文本链接，包括产品、解决方案、客户服务和联系方式的列表项
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 灰色发送按钮，位于Contact Us列底部
  - input x2, 宽=200px, 高=40px, 圆角=4px
    说明: WhatsApp和邮箱输入框，位于Contact Us列底部

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **按钮文字**: `Send`
- **列表项** (4个):
  - `Products`: Kitchen Cabinet, Wardrobe, Windows and Doors, Bath...
  - `One-Stop Solutions`: Hotel Solutions, Resort Solutions, Villa Solutions...
  - `Customer Services`: Measurement Guidance, Packaging Info, Delivery & S...

**响应式**: 平板设备下调整为2列布局，移动端设备下调整为1列布局
**特效**: 无
**内容摘要**: 页面底部footer区域，展示产品分类、一站式解决方案、客户服务链接及联系方式，包含订阅表单

---


## 设计参数汇总

### 颜色系统（CSS变量建议）
```css
:root {
    --color-primary: #666666;
    --color-secondary: #cccccc;
    --color-background: #000000;
    --color-heading: #ffffff;
    --color-text: #cccccc;
    --color-border: #e0e0e0;
}
```

### 字体系统
```css
:root {
    --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    --font-size-h1: 18px;
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
- `solid-wood-kitchen-cabinets_pixel_1.jpg`
- `solid-wood-kitchen-cabinets_pixel_10.jpg`
- `solid-wood-kitchen-cabinets_pixel_11.jpg`
- `solid-wood-kitchen-cabinets_pixel_12.jpg`
- `solid-wood-kitchen-cabinets_pixel_13.jpg`
- `solid-wood-kitchen-cabinets_pixel_14.jpg`
- `solid-wood-kitchen-cabinets_pixel_15.jpg`
- `solid-wood-kitchen-cabinets_pixel_16.jpg`
- `solid-wood-kitchen-cabinets_pixel_17.jpg`
- `solid-wood-kitchen-cabinets_pixel_18.jpg`
- `solid-wood-kitchen-cabinets_pixel_19.jpg`
- `solid-wood-kitchen-cabinets_pixel_2.jpg`
- `solid-wood-kitchen-cabinets_pixel_3.jpg`
- `solid-wood-kitchen-cabinets_pixel_4.jpg`
- `solid-wood-kitchen-cabinets_pixel_5.jpg`
- `solid-wood-kitchen-cabinets_pixel_6.jpg`
- `solid-wood-kitchen-cabinets_pixel_7.jpg`
- `solid-wood-kitchen-cabinets_pixel_8.jpg`
- `solid-wood-kitchen-cabinets_pixel_9.jpg`

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
