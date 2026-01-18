# WordPress 页面克隆任务

## 原始页面信息
- URL: https://georgeconstructions.com/lacquer-kitchen-cabinets/
- 标题: Lacquer Cabinets | Modern Kitchen | Ideas
- 总高度: 7252px

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
- **截图**: `lacquer-kitchen-cabinets_pixel_1.jpg`
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
- 正文: #ffffff
- 边框: none

**字体**:
- 标题: 48px, 字重: 700
- 正文: 24px, 字重: 400
- 行高: 1.2

**间距**:
- 上边距: 120px
- 下边距: 80px
- 元素间距: 0px
- 卡片内边距: 0px

**组件** (6个):
  - navbar x1, 宽=auto, 高=auto, 圆角=0
    说明: 顶部导航栏，包含logo、导航链接和按钮
  - logo x1, 宽=120px, 高=40px, 圆角=0
    说明: 左侧品牌logo，包含图标和文字
  - nav-link x7, 宽=auto, 高=auto, 圆角=0
    说明: 导航链接，包括Products、Projects、Blog、Service、Video、About、Contact
  - button x1, 宽=120px, 高=40px, 圆角=4px
    说明: 橙色“Quick Quote”按钮，位于导航栏右侧
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题“LACQUER KITCHEN CABINETS”，居中显示
  - text x1, 宽=auto, 高=auto, 圆角=0
    说明: 副标题“ One-Stop Building Material Solution Supplier”，居中显示

**图片占位符** (1组):
  - **hero-banner** x1
    尺寸: 100% x auto, 比例: 16:9
    位置: 全屏背景, object-fit: cover
    遮罩: rgba(0,0,0,0.5)
    占位符建议: 厨房场景背景图

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `LACQUER KITCHEN CABINETS`
- **副标题**: ` One-Stop Building Material Solution Supplier`
- **按钮文字**: `Quick Quote`

**响应式**: 移动端导航栏折叠为汉堡菜单，hero区域文字居中显示，背景图自适应
**特效**: 背景图带有半透明黑色叠加层，增强文字可读性；按钮 hover 可能会有颜色加深效果
**内容摘要**: 展示漆面厨房橱柜的主视觉区域，包含导航栏和核心产品信息

---

### 分块 2: product-grid
- **截图**: `lacquer-kitchen-cabinets_pixel_2.jpg`
- **建议模块名**: `lacquer-kitchen-cabinets-product-grid`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 3, 行数: 2
- 水平间距: 20px, 垂直间距: 30px
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
- 上边距: 60px
- 下边距: 60px
- 元素间距: 0px
- 卡片内边距: 20px

**组件** (1个):
  - card x6, 宽=360px, 高=auto, 圆角=0px, 有阴影
    说明: 白色卡片，带轻微阴影，包含产品图片、标题和描述文字

**图片占位符** (1组):
  - **product** x6
    尺寸: 100% x 200px, 比例: 16:9
    位置: 网格排列, object-fit: cover
    占位符建议: product-thumbnail

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Most Popular Lacquered Kitchen Cabinet Designs`
- **卡片内容** (6个):
  - `Grey Melamine Kitchen Cupboards`: Grey Melamine Kitchen Cabinet Design Melamine kitc...
  - `White and Black Lacquer Kitchen Cabinet`: Two Tone Black and White Kitchen Cabinets Design o...
  - `Modern Matte Lacquer Kitchen`: Kitchen Cabinet Doors & Panels Modern Matte Lacque...

**响应式**: 平板设备显示2列，移动端显示1列
**特效**: 卡片 hover 时可能显示阴影增强效果，图片采用 cover 模式保持比例
**内容摘要**: 该区域主要展示最受欢迎的烤漆厨房橱柜设计，以网格布局呈现6个产品卡片，每个卡片包含产品图片、标题和简要描述

---

### 分块 3: content-block
- **截图**: `lacquer-kitchen-cabinets_pixel_3.jpg`
- **建议模块名**: `kitchen-cabinets-content-block`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 50px
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #333333
- 正文: #666666
- 边框: none

**字体**:
- 标题: 32px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (2个):
  - button x1, 宽=120px, 高=40px, 圆角=4px
    说明: 橙色按钮，文字为Consult，位于左侧文字下方
  - text x1, 宽=auto, 高=auto, 圆角=0
    说明: 左侧文字，描述下载目录的内容

**图片占位符** (1组):
  - **gallery** x1
    尺寸: 400px x 266px, 比例: 3:2
    位置: 右侧, object-fit: cover
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: ` What Are Lacquered kitchen cabinets`
- **段落** (2个):
  - `Lacquered kitchen cabinets are cabinets with a shiny, tough coating made from lacquer resin. The fir...`
  - `Almost limitless design possibilities are possible with the variety of lacquer finish options availa...`
- **按钮文字**: `Consult`

**响应式**: 平板设备：左右布局变为上下布局，图片宽度调整为100%，按钮宽度调整为100%；移动端：单列布局，所有元素垂直排列
**特效**: 无
**内容摘要**: 该区域展示下载目录的CTA和漆面橱柜的定义及特点

---

### 分块 4: features
- **截图**: `lacquer-kitchen-cabinets_pixel_4.jpg`
- **建议模块名**: `lacquered-cabinets-features`

**布局**:
- 容器: container-1200
- 类型: block
- 列数: 1, 行数: 1
- 水平间距: 30px, 垂直间距: 40px
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

**组件** (5个):
  - heading x2, 宽=auto, 高=auto, 圆角=0
    说明: 两个标题，分别为“Pros of lacquered kitchen cabinets”和“Drawbacks of lacquered kitchen cabinets”，加粗显示
  - list x4, 宽=auto, 高=auto, 圆角=0
    说明: Pros下的4个优点列表项，使用圆点符号
  - text x2, 宽=auto, 高=auto, 圆角=0
    说明: Drawbacks下的两段文本，描述缺点
  - image x2, 宽=300px, 高=200px, 圆角=8px, 有阴影
    说明: 两个产品图片，分别对应“Kitchen Lacquer Cabinets: Designs And Finishes”和“Styles Of Kitchen Cabinets”标题
  - heading x2, 宽=auto, 高=auto, 圆角=0
    说明: 两个子标题，分别为“Kitchen Lacquer Cabinets: Designs And Finishes”和“Styles Of Kitchen Cabinets”，加粗显示

**图片占位符** (1组):
  - **thumbnail** x2
    尺寸: 300px x 200px, 比例: 3:2
    位置: 左右排列, object-fit: cover
    占位符建议: product-thumbnail

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Pros of lacquered kitchen cabinets / Drawbacks of lacquered kitchen cabinets`
- **段落** (2个):
  - `Needs regular upkeep to maintain a glossy appearance of cabinets.`
  - `Painting wood differs from painting other materials. If you want your cabinets to blend with your cu...`
- **列表项** (4个):
  - `Stylish cabinets with a variety of color options to accommodate a wide range of tastes.`: ...
  - `very robust and long-lasting; it doesn't flake for many years.`: ...
  - `Easy to reapply, it dries quickly for instant use after installation.`: ...
- **卡片内容** (2个):
  - `Kitchen Lacquer Cabinets: Designs And Finishes`: ...
  - `Styles Of Kitchen Cabinets`: ...

**响应式**: 移动端下图片和子标题堆叠显示，列表项保持单列
**特效**: 图片 hover 时可能显示阴影加深，列表项 hover 时可能有轻微颜色变化
**内容摘要**: 该区域主要展示清漆厨房橱柜的优缺点及设计风格分类

---

### 分块 5: features
- **截图**: `lacquer-kitchen-cabinets_pixel_5.jpg`
- **建议模块名**: `lacquered-kitchen-cabinets-features`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 2
- 水平间距: 30px, 垂直间距: 40px
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
- 元素间距: 20px
- 卡片内边距: 20px

**组件** (2个):
  - list x6, 宽=auto, 高=auto, 圆角=0
    说明: 优缺点列表，使用点符号展示上漆厨房橱柜的4个优点和2个缺点
  - card x2, 宽=auto, 高=auto, 圆角=8px
    说明: 两个卡片，分别展示“设计和饰面”与“风格”，包含图片、标题和描述文字

**图片占位符** (1组):
  - **thumbnail** x2
    尺寸: 300px x 200px, 比例: 3:2
    位置: 网格排列（两列）, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Pros of lacquered kitchen cabinets`
- **副标题**: `Drawbacks of lacquered kitchen cabinets`
- **段落** (6个):
  - `Stylish cabinets with a variety of color options to accommodate a wide range of tastes.`
  - `very robust and long-lasting; it doesn't flake for many years.`
  - `Easy to reapply, it dries quickly for instant use after installation.`
- **列表项** (6个):
  - `Pros`: Stylish cabinets with a variety of color options t...
  - `Pros`: very robust and long-lasting; it doesn't flake for...
  - `Pros`: Easy to reapply, it dries quickly for instant use ...
- **卡片内容** (2个):
  - `Kitchen Lacquer Cabinets: Designs And Finishes`: Lacquer kitchen cabinets imitate the lavish appear...
  - `Styles Of Kitchen Cabinets`: Lacquer kitchen cabinets complement modern spaces ...

**响应式**: 平板设备显示2列，移动端设备显示1列
**特效**: 无
**内容摘要**: 该区域主要展示上漆厨房橱柜的优缺点，以及设计和风格的详细信息，帮助用户全面了解产品特点

---

### 分块 6: content-block
- **截图**: `lacquer-kitchen-cabinets_pixel_6.jpg`
- **建议模块名**: `modern-kitchen-cabinetry-material`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0
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
- 元素间距: 30px
- 卡片内边距: 0

**组件** (2个):
  - button x1, 宽=auto, 高=40px, 圆角=8px, 有阴影
    说明: 橙色按钮，位于左侧文字下方，显示'Get a Free Quote'文字
  - image x1, 宽=600px, 高=auto, 圆角=0
    说明: 右侧厨房场景图片，展示漆面橱柜的实际应用效果

**图片占位符** (1组):
  - **thumbnail** x1
    尺寸: 600px x auto, 比例: 16:9
    位置: 右侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Modern Kitchen Cabinetry Material`
- **段落** (2个):
  - `Since its sleek surface gives any space a contemporary feel, lacquer is a popular material for kitch...`
  - `It's important to consider the overall style and design of your kitchen when selecting lacquer kitch...`
- **按钮文字**: `Get a Free Quote`

**响应式**: 平板设备显示2列（文字左、图片右），移动端设备显示1列（文字在上、图片在下）
**特效**: 按钮 hover 时可能触发颜色加深或阴影增强效果
**内容摘要**: 该区域主要介绍漆面作为现代厨房橱柜材料的优势（耐用性、防水性、易清洁等），并引导用户通过按钮获取免费报价

---

### 分块 7: gallery
- **截图**: `lacquer-kitchen-cabinets_pixel_7.jpg`
- **建议模块名**: `kitchen-related-ideas-gallery`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 3, 行数: 1
- 水平间距: 20px, 垂直间距: 30px
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
- 上边距: 30px
- 下边距: 30px
- 元素间距: 20px
- 卡片内边距: 20px

**组件** (1个):
  - card x3, 宽=auto, 高=auto, 圆角=8px
    说明: 白色卡片，包含图片、标题和描述，用于展示厨房相关创意

**图片占位符** (1组):
  - **gallery** x3
    尺寸: 100% x 200px, 比例: 16:9
    位置: 网格排列, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Get A Free Quote`
- **段落** (1个):
  - `Kindly send us your project details and floor plan. We will quote for you within 8 hours!`
- **卡片内容** (3个):
  - `MUDROOM STORAGE IDEAS 2026`: Mudroom Storage Ideas That Actually Work for Busy ...
  - `Butler’s Pantry Ideas`: Butler’s Pantry Ideas That Truly Work - Make Life ...
  - `Kitchen Curtain Ideas 2026`: Kitchen Curtain Ideas For 2026: Styles That Actual...

**响应式**: 平板设备显示2列，移动端显示1列
**特效**: 无
**内容摘要**: 展示厨房相关的创意内容（储物、 Butler’s Pantry、窗帘），并包含联系表单的起始部分

---

### 分块 8: contact-form
- **截图**: `lacquer-kitchen-cabinets_pixel_8.jpg`
- **建议模块名**: `contact-form-module`

**布局**:
- 容器: full-width
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 20px, 垂直间距: 0
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #4a5568
- 标题: #000000
- 正文: #333333
- 边框: #e2e8f0

**字体**:
- 标题: 16px, 字重: 700
- 正文: 14px, 字重: 400
- 行高: 1.5

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 10px
- 卡片内边距: 20px

**组件** (6个):
  - image x1, 宽=46%, 高=auto, 圆角=0
    说明: 左侧背景图片，展示现代住宅场景，占容器左侧46%宽度
  - input x4, 宽=100%, 高=40px, 圆角=4px
    说明: 表单输入框（Name、Email、City、Country-Select），白色背景，浅灰色边框
  - checkbox x10, 宽=auto, 高=auto, 圆角=0
    说明: Product Needed*下的复选框选项，共10个，包括Kitchen cabinet、Bedroom等
  - textarea x1, 宽=100%, 高=120px, 圆角=4px
    说明: Message文本框，多行输入区域
  - button x1, 宽=100%, 高=40px, 圆角=4px
    说明: Choose File按钮，显示“No file chosen”文字
  - button x1, 宽=100%, 高=40px, 圆角=4px
    说明: Send按钮，灰色背景，白色文字

**图片占位符** (1组):
  - **background** x1
    尺寸: 46% x auto, 比例: 16:9
    位置: 左侧, object-fit: cover
    占位符建议: modern-residential-image

**⚠️ 提取的文字内容（用于默认数据）**:
- **按钮文字**: `Send`

**响应式**: 平板设备下表单区域调整为单列布局，图片宽度调整为100%
**特效**: 表单输入框 hover 时边框颜色加深，发送按钮 hover 时背景色变深
**内容摘要**: 页面中部联系表单模块，包含左侧背景图片和右侧表单，用于收集用户项目需求和联系信息

---

### 分块 9: contact-form
- **截图**: `lacquer-kitchen-cabinets_pixel_9.jpg`
- **建议模块名**: `contact-form-with-footer`

**布局**:
- 容器: container-1200
- 类型: block
- 列数: 1, 行数: 2
- 水平间距: 30px, 垂直间距: 40px
- 对齐: left

**颜色**:
- 背景: #f8f8f8
- 主色: #6c757d
- 标题: #333333
- 正文: #333333
- 边框: #dddddd

**字体**:
- 标题: 24px, 字重: 700
- 正文: 14px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 40px
- 下边距: 40px
- 元素间距: 20px
- 卡片内边距: 0

**组件** (8个):
  - input x5, 宽=100%, 高=40px, 圆角=4px
    说明: 表单输入框（Name、Email、Tel/Whatsapp、City、Country-Select），边框#dddddd
  - checkbox x10, 宽=auto, 高=auto, 圆角=0
    说明: Product Needed复选框，共10个选项
  - textarea x1, 宽=100%, 高=120px, 圆角=4px
    说明: Message文本框，多行输入
  - button x1, 宽=auto, 高=auto, 圆角=4px
    说明: Choose File按钮，文件上传控件
  - button x1, 宽=100%, 高=40px, 圆角=4px
    说明: 灰色发送按钮，文字'Send'
  - link x19, 宽=auto, 高=auto, 圆角=0
    说明: footer导航链接，包括Products、One-Stop Solutions、Customer Services列的文本链接
  - input x2, 宽=100%, 高=40px, 圆角=4px
    说明: footer订阅输入框（whatsapp、Email*）
  - button x1, 宽=100%, 高=40px, 圆角=4px
    说明: footer灰色发送按钮，文字'Send'

**图片占位符** (1组):
  - **background** x0
    尺寸: 0 x 0, 比例: auto
    位置: none, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Get A Free Quote`
- **段落** (1个):
  - `Kindly send us your project details and floor plan. We will quote for you within 8 hours!`
- **按钮文字**: `Send`
- **列表项** (10个):
  - `Kitchen cabinet`: ...
  - `Bedroom`: ...
  - `Bathroom`: ...

**响应式**: 平板端footer导航列调整为2列，移动端footer列堆叠为1列；表单字段在移动端垂直堆叠
**特效**: 无
**内容摘要**: 该区域主要展示获取免费报价的联系表单（含项目详情输入、产品需求选择、文件上传及发送功能）及页面底部的导航链接（产品、解决方案、客户服务、联系我们）

---

### 分块 10: footer
- **截图**: `lacquer-kitchen-cabinets_pixel_10.jpg`
- **建议模块名**: `company-footer`

**布局**:
- 容器: full-width
- 类型: grid
- 列数: 4, 行数: 7
- 水平间距: 30px, 垂直间距: 20px
- 对齐: space-between

**颜色**:
- 背景: #000000
- 主色: #6c7a89
- 标题: #ffffff
- 正文: #ffffff
- 边框: #cccccc

**字体**:
- 标题: 18px, 字重: 700
- 正文: 14px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 10px
- 卡片内边距: 0

**组件** (3个):
  - text x21, 宽=auto, 高=auto, 圆角=0
    说明: 白色文本链接，包括Products、One-Stop Solutions、Customer Services、Contact Us列下的所有导航项
  - input x2, 宽=220px, 高=40px, 圆角=4px
    说明: 白色背景输入框，分别带有'whatsapp'和'Email*'占位符
  - button x2, 宽=220px, 高=40px, 圆角=4px
    说明: 灰色背景按钮，文字为'Send'

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Products, One-Stop Solutions, Customer Services, Contact Us`
- **按钮文字**: `Send`, `Send`
- **列表项** (21个):
  - `Kitchen Cabinet`: ...
  - `Wardrobe`: ...
  - `Windows and Doors`: ...

**响应式**: 平板设备下调整为2列，移动端调整为1列
**特效**: 无
**内容摘要**: 页面底部footer区域，展示公司产品分类、一站式解决方案、客户服务及联系方式，包含导航链接、联系表单和订阅入口

---


## 设计参数汇总

### 颜色系统（CSS变量建议）
```css
:root {
    --color-primary: #6c7a89;
    --color-secondary: #ffffff;
    --color-background: #000000;
    --color-heading: #ffffff;
    --color-text: #ffffff;
    --color-border: #cccccc;
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
    --spacing-element: 10px;
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
- `lacquer-kitchen-cabinets_pixel_1.jpg`
- `lacquer-kitchen-cabinets_pixel_10.jpg`
- `lacquer-kitchen-cabinets_pixel_2.jpg`
- `lacquer-kitchen-cabinets_pixel_3.jpg`
- `lacquer-kitchen-cabinets_pixel_4.jpg`
- `lacquer-kitchen-cabinets_pixel_5.jpg`
- `lacquer-kitchen-cabinets_pixel_6.jpg`
- `lacquer-kitchen-cabinets_pixel_7.jpg`
- `lacquer-kitchen-cabinets_pixel_8.jpg`
- `lacquer-kitchen-cabinets_pixel_9.jpg`

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
