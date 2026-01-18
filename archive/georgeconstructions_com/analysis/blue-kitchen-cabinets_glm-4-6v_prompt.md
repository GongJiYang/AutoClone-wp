# WordPress 页面克隆任务

## ⚠️ 核心要求（必须满足）

1. **默认数据必须从截图提取真实内容** - 不可为空或使用占位符
2. **每个模块独立PHP文件** - `modules/{module-name}.php`
3. **完整的响应式CSS** - 4个断点（桌面/平板/移动/小屏）
4. **图片占位符使用placehold.co** - `https://placehold.co/600x400/e0e0e0/666?text=Product`

---

## 原始页面信息
- URL: https://georgeconstructions.com/blue-kitchen-cabinets/
- 标题: Everything You Need to Know About Blue Kitchen Cabinets
- 总高度: 12348px

---

## 页面结构分析

### 分块 1: hero
- **截图**: `blue-kitchen-cabinets_pixel_1.jpg`
- **建议模块名**: `kitchen-cabinets-hero`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 1, 行数: 2
- 水平间距: 0, 垂直间距: 0
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #ffffff
- 正文: #ffffff
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
  - navbar x1, 宽=auto, 高=auto, 圆角=0
    说明: 顶部导航栏，包含logo、7个导航项和1个橙色按钮，布局为flex，左右对齐
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'Custom Blue Kitchen Cabinets'，白色文字，加粗700
  - button x2, 宽=auto, 高=40px, 圆角=4px
    说明: 1个橙色背景（#FF8C00）白色文字的'Quick Quote'按钮（导航栏右侧），1个白色背景黑色文字的'Download Catalogues'按钮（hero区域右侧）

**图片占位符** (1组):
  - **hero-banner** x1
    尺寸: 100% x auto, 比例: 16:9
    位置: 居中, object-fit: cover
    占位符建议: blue-kitchen-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Custom Blue Kitchen Cabinets`
- **副标题**: `Blue Cabinets: Color Ideas, Pairings, and Design Tips`
- **按钮文字**: `Quick Quote`, `Download Catalogues`

**响应式**: 平板设备（≤768px）下，导航栏改为汉堡菜单，hero区域图片占满宽度，文字居中；移动端（≤480px）'Quick Quote'按钮文字简化为'Quote'
**特效**: 导航栏按钮hover时背景色加深至#E67300，hero区域图片有轻微渐变覆盖提升文字可读性
**内容摘要**: 页面顶部hero区域，包含导航栏和主视觉横幅，核心展示蓝色厨房橱柜的主题信息，包含主标题、副标题及行动号召按钮

---

### 分块 2: product-grid
- **截图**: `blue-kitchen-cabinets_pixel_2.jpg`
- **建议模块名**: `blue-kitchen-cabinets-grid`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 3, 行数: 2
- 水平间距: 20px, 垂直间距: 30px
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #2d3748
- 标题: #333333
- 正文: #666666
- 边框: none

**字体**:
- 标题: 20px, 字重: 600
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 50px
- 下边距: 50px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (2个):
  - card x6, 宽=auto, 高=auto, 圆角=8px, 有阴影
    说明: 白色背景卡片，带轻微阴影，每个卡片包含蓝色厨房橱柜图片和对应标题
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 深蓝色背景（#2d3748），白色文字，显示'More designs'，位于卡片区域下方居中

**图片占位符** (1组):
  - **product** x6
    尺寸: 100% x auto, 比例: 16:9
    位置: 网格排列（3列2行）, object-fit: cover
    占位符建议: kitchen-cabinet-image

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Blue Cabinets: Color Ideas, Pairings, and Design Tips`
- **按钮文字**: `More designs`
- **卡片内容** (6个):
  - `Blue kitchen cabinets`: ...
  - `Dark Blue Kitchen Cabinets`: ...
  - `Blue Gray Kitchen Cabinets`: ...

**响应式**: 平板设备（≤768px）下调整为2列布局，移动端（≤480px）改为单列，卡片宽度占满容器
**特效**: 卡片hover时阴影加深，按钮hover时背景色变浅（#4a5568）
**内容摘要**: 展示6种不同色调的蓝色厨房橱柜（浅蓝、深蓝、蓝灰、海军蓝、浅蓝、蓝灰），提供设计灵感，底部有'更多设计'按钮引导用户查看更多选项

---

### 分块 3: features
- **截图**: `blue-kitchen-cabinets_pixel_3.jpg`
- **建议模块名**: `blue-cabinets-surface-finishes`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 30px, 垂直间距: 40px
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #2d3748
- 标题: #2d3748
- 正文: #4a5568
- 边框: none

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 20px
- 卡片内边距: 25px

**组件** (2个):
  - card x4, 宽=auto, 高=auto, 圆角=8px
    说明: 白色背景卡片，包含标题、描述文字和'Need Help'按钮，无阴影和边框
  - button x4, 宽=auto, 高=40px, 圆角=6px
    说明: 深蓝色背景（#2d3748），白色文字，'Need Help'按钮，每个卡片一个

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Transform Your Blue Cabinets with Custom Surface Finishes`
- **段落** (4个):
  - `George Constructions has a lot of different finishes for kitchen doors, including smooth and recesse...`
  - `This custom choice is less frequent. It has a see-through finish that brings out the texture of the ...`
  - `Woodgrain finishes are often used in kitchens with a modern or rustic look because they may make the...`
- **按钮文字**: `Need Help`, `Need Help`, `Need Help`, `Need Help`
- **卡片内容** (4个):
  - `Smooth Flat And Dimpled Finishing`: George Constructions has a lot of different finish...
  - `Glaze Finishing`: This custom choice is less frequent. It has a see-...
  - `Woodgrain Finishing`: Woodgrain finishes are often used in kitchens with...

**响应式**: 平板设备（≤768px）下，布局改为2列；移动端（≤480px）下，布局改为1列，按钮文字保持不变
**特效**: 按钮hover时背景色加深至#1a202c
**内容摘要**: 该区域主要展示蓝色橱柜的四种定制表面处理方式，包括平滑/凹凸处理、釉面处理、木纹处理和珍珠色处理，每个处理方式配有详细描述和帮助按钮

---

### 分块 4: features
- **截图**: `blue-kitchen-cabinets_pixel_4.jpg`
- **建议模块名**: `kitchen-cabinets-layout-tips`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 20px, 垂直间距: 30px
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #2C3E50
- 标题: #222222
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
  - card x4, 宽=auto, 高=auto, 圆角=8px
    说明: 白色背景卡片，包含布局类型标题、描述文字及行动按钮
  - button x4, 宽=auto, 高=40px, 圆角=8px
    说明: 深蓝色背景（#2C3E50），白色文字，'Design Now'按钮

**图片占位符** (1组):
  - **thumbnail** x0
    尺寸: auto x auto, 比例: auto
    位置: 无, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Blue Kitchen Cabinets Design: Layout Tips & Inspiration`
- **按钮文字**: `Design Now`, `Design Now`, `Design Now`, `Design Now`
- **卡片内容** (4个):
  - `I-shaped`: Customized I-shaped designs with blue cabinets can...
  - `U-shaped`: A custom U-shaped design with blue kitchen cabinet...
  - `L-shaped`: The L-shaped design makes good use of corner space...

**响应式**: 平板设备（≤768px）下，布局改为2列；移动端（≤480px）下，布局改为1列，按钮文字保持不变
**特效**: 按钮hover时背景色加深至#1a2533
**内容摘要**: 该区域主要展示蓝色厨房橱柜的四种布局设计类型（I-shaped、U-shaped、L-shaped、Island），包含每种布局的描述及定制设计按钮，为用户提供布局灵感与操作指引

---

### 分块 5: features
- **截图**: `blue-kitchen-cabinets_pixel_5.jpg`
- **建议模块名**: `kitchen-cabinets-layout-tips`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #2D3748
- 标题: #2D3748
- 正文: #4A5568
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
  - card x4, 宽=auto, 高=auto, 圆角=8px
    说明: 白色卡片，包含布局类型标题、描述文字和行动按钮
  - button x4, 宽=auto, 高=40px, 圆角=4px
    说明: 深蓝色背景（#2D3748），白色文字，'Design Now'

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Blue Kitchen Cabinets Design: Layout Tips & Inspiration`
- **段落** (4个):
  - `Customized I-shaped designs with blue cabinets can maximize space use in tiny or open kitchens, prov...`
  - `A custom U-shaped design with blue kitchen cabinets might make your kitchen work better. This layout...`
  - `The L-shaped design makes good use of corner space to create a useful work triangle that keeps thing...`
- **按钮文字**: `Design Now`, `Design Now`, `Design Now`, `Design Now`
- **卡片内容** (4个):
  - `I-shaped`: Customized I-shaped designs with blue cabinets can...
  - `U-shaped`: A custom U-shaped design with blue kitchen cabinet...
  - `L-shaped`: The L-shaped design makes good use of corner space...

**响应式**: 平板设备（≤768px）下，布局改为2列；移动端（≤480px）下，布局改为1列，按钮文字保持不变
**特效**: 按钮hover时背景色加深至#1A202C
**内容摘要**: 页面中部展示蓝色厨房橱柜的四种布局设计（I形、U形、L形、岛台），每个布局包含功能描述和“Design Now”行动按钮，帮助用户选择合适的厨房布局

---

### 分块 6: features
- **截图**: `blue-kitchen-cabinets_pixel_6.jpg`
- **建议模块名**: `kitchen-cabinets-functional-accessories`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 20px, 垂直间距: 30px
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #2D3748
- 标题: #2D3748
- 正文: #4A5568
- 边框: none

**字体**:
- 标题: 24px, 字重: 600
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 15px
- 卡片内边距: 25px

**组件** (2个):
  - card x4, 宽=auto, 高=auto, 圆角=8px
    说明: 白色背景卡片，包含标题、描述文字和深色按钮，每个卡片展示一种厨房配件（Sink/Hinge/Handle/Drawer）
  - button x4, 宽=auto, 高=40px, 圆角=6px
    说明: 深灰色背景（#2D3748），白色文字，显示'Design Now'

**图片占位符** (1组):
  - **thumbnail** x0
    尺寸: auto x auto, 比例: auto
    位置: 无, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Blue Kitchen Cabinets: Must-Have Functional Accessories`
- **段落** (4个):
  - `You can choose from composite, ceramic, or stainless steel, all of which are long-lasting and good-l...`
  - `Chrome, oil-rubbed bronze, and matte black are among the available finishes. There are beautiful hin...`
  - `Elevate your cabinetry with a selection of styles from George Constructions, comprising modern handl...`
- **按钮文字**: `Design Now`, `Design Now`, `Design Now`, `Design Now`
- **卡片内容** (4个):
  - `Sink`: You can choose from composite, ceramic, or stainle...
  - `Hinge`: Chrome, oil-rubbed bronze, and matte black are amo...
  - `Handle`: Elevate your cabinetry with a selection of styles ...

**响应式**: 平板设备（≤768px）下，网格布局改为2列；移动端（≤480px）改为单列，按钮宽度占满
**特效**: 按钮hover时背景色加深至#1A202C
**内容摘要**: 页面中部展示蓝色厨房橱柜的必备功能性配件，包括水槽、铰链、把手和抽屉，每个配件提供详细描述及设计按钮

---

### 分块 7: content-block
- **截图**: `blue-kitchen-cabinets_pixel_7.jpg`
- **建议模块名**: `blue-cabinet-shade-guide`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 5, 行数: 5
- 水平间距: 20px, 垂直间距: 20px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #2d3748
- 标题: #2d3748
- 正文: #4a5568
- 边框: #e2e8f0

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 40px
- 下边距: 40px
- 元素间距: 20px
- 卡片内边距: 15px

**组件** (1个):
  - table x1, 宽=auto, 高=auto, 圆角=0
    说明: 包含5列（Shade、Mood、Best For、Pairs With、Finish Tip）和5行数据的表格，展示蓝色橱柜色板信息

**图片占位符** (1组):
  - **none** x0
    尺寸: auto x auto, 比例: auto
    位置: none, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Blue Cabinet Shade Guide`
- **副标题**: `Use the chart below to match mood, scale, and finish to the right blue. A quick sample pot or door sample will confirm the choice in your light.`
- **段落** (5个):
  - `Powder / Sky: Airy, soft, casual | Small kitchens, cottage or coastal | Warm whites, light oak, bead...`
  - `Blue-Gray / Slate: Modern, calm, sophisticated | Contemporary flats, minimal spaces | Matte black ha...`
  - `Navy: Classic, tailored, high-contrast | Traditional or transitional homes | Brass hardware, white q...`

**响应式**: 平板设备（≤768px）下，表格改为单列布局，每列垂直堆叠；移动端（≤480px）简化表格内容，保留核心信息
**特效**: 表格 hover 时行背景轻微变色，提升交互反馈
**内容摘要**: 页面中部展示蓝色橱柜色板指南，通过表格形式呈现不同蓝色调的 mood、适用场景、搭配元素及表面处理建议

---

### 分块 8: content-block
- **截图**: `blue-kitchen-cabinets_pixel_8.jpg`
- **建议模块名**: `blue-cabinets-pros-cons`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 40px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #2d3748
- 标题: #2d3748
- 正文: #4a5568
- 边框: none

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 20px
- 卡片内边距: 0

**组件** (4个):
  - image x1, 宽=50%, 高=auto, 圆角=0, 有阴影
    说明: 蓝色厨房橱柜实景图，展示橱柜与厨房布局
  - heading x2, 宽=auto, 高=auto, 圆角=0
    说明: 两个标题：'Advantages'和'Considerations'，深灰色（#2d3748），加粗700
  - paragraph x4, 宽=auto, 高=auto, 圆角=0
    说明: Advantages下的4个段落，描述蓝色橱柜的优势
  - paragraph x3, 宽=auto, 高=auto, 圆角=0
    说明: Considerations下的3个段落，描述蓝色橱柜的注意事项

**图片占位符** (1组):
  - **hero-banner** x1
    尺寸: 50% x auto, 比例: auto
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Pros and Cons of Blue Kitchen Cabinets`
- **段落** (7个):
  - `Blue behaves almost like a neutral, so it plays nice with wood, stone and most metals.`
  - `It covers a lot of looks. Coastal, modern, farmhouse, classic, even industrial, if you choose the ri...`
  - `Two tone layouts are easy. Blue bases with white uppers still looks fresh years later.`

**响应式**: 平板设备（≤768px）下，图文改为单列布局，图片占满宽度；移动端（≤480px）图片宽度调整为100%，文字区域调整内边距
**特效**: 图片带有轻微阴影效果，增强层次感；文字段落间有适当间距，提升可读性
**内容摘要**: 页面中部内容块，展示蓝色厨房橱柜的优缺点，包含实景图片与文字说明，分为Advantages（优势）和Considerations（注意事项）两部分

---

### 分块 9: content-block
- **截图**: `blue-kitchen-cabinets_pixel_9.jpg`
- **建议模块名**: `kitchen-cabinets-style-paths`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 3, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #2d3748
- 标题: #2d3748
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
  - card x3, 宽=auto, 高=auto, 圆角=0
    说明: 白色卡片，包含风格路径标题、描述文字和定制按钮
  - button x3, 宽=auto, 高=40px, 圆角=4px
    说明: 深蓝色背景（#2d3748），白色文字，显示'Custom Now'

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Style Paths: How to Make Blue Feel Intentional`
- **按钮文字**: `Custom Now`, `Custom Now`, `Custom Now`
- **卡片内容** (3个):
  - `Modern minimal`: Flat panels in blue gray keep lines clean. Use thi...
  - `Coastal calm`: Powder blue, white walls, natural fibers. Add a ru...
  - `Luxe & Moody`: Teal or petrol blue feels luxe in large kitchens. ...

**响应式**: 平板设备（≤768px）下，布局改为2列；移动端（≤480px）下，布局改为1列，按钮文字保持不变
**特效**: 按钮hover时背景色加深至#1a202c，文字保持白色
**内容摘要**: 该区域展示三种蓝色厨房橱柜的风格路径，包括每个风格的设计建议和定制按钮，帮助用户选择合适的蓝色橱柜风格

---

### 分块 10: features
- **截图**: `blue-kitchen-cabinets_pixel_10.jpg`
- **建议模块名**: `kitchen-cabinets-pairings`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 3, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #2d3748
- 标题: #2d3748
- 正文: #4a5568
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
  - card x3, 宽=auto, 高=auto, 圆角=8px
    说明: 白色卡片，包含标题和列表项，无按钮，无阴影

**图片占位符** (1组):
  - **gallery** x3
    尺寸: 100% x auto, 比例: 4:3
    位置: 网格排列, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Perfect Pairings: Countertops, Backsplashes, and Hardware`
- **列表项** (3个):
  - `Countertops`: ['Marble look quartz keeps navy crisp and classic....
  - `Backsplashes`: ['White Subway Tile: A timeless backdrop for every...
  - `Hardware`: ['Satin Brass: Warms up cool blues and feels upsca...
- **卡片内容** (3个):
  - `Countertops`: Marble look quartz keeps navy crisp and classic. B...
  - `Backsplashes`: White Subway Tile: A timeless backdrop for every s...
  - `Hardware`: Satin Brass: Warms up cool blues and feels upscale...

**响应式**: 平板设备（≤768px）下，网格布局改为2列；移动端（≤480px）下改为单列布局，卡片占满宽度
**特效**: 无
**内容摘要**: 展示厨房台面、 backsplash、硬件的搭配建议，每个类别包含具体材质和风格推荐

---

### 分块 11: content-block
- **截图**: `blue-kitchen-cabinets_pixel_11.jpg`
- **建议模块名**: `kitchen-cabinets-paint-vs-laminate`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #000000
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

**组件** (3个):
  - heading x2, 宽=auto, 高=auto, 圆角=0
    说明: 两个主标题，分别为'Paint vs. Laminate'和'Picking sheen'，深灰色（#222222），加粗700
  - paragraph x2, 宽=auto, 高=auto, 圆角=0
    说明: 两个段落，分别描述油漆与层压板的对比及光泽选择，深灰色（#333333），16px，400权重
  - image x1, 宽=50%, 高=auto, 圆角=0
    说明: 右侧厨房图片，展示蓝色橱柜，无阴影或边框

**图片占位符** (1组):
  - **image-text** x1
    尺寸: 50% x auto, 比例: auto
    位置: 右侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Paint vs. Laminate`
- **副标题**: `Picking sheen`
- **段落** (2个):
  - `Painted cabinets deliver depth and a hand-finished look, especially in satin. Micro-scratches can be...`
  - `Matte feels modern, but shows fingerprints on very dark blues. Satin is our go to because it looks r...`

**响应式**: 平板设备（≤768px）下，内容区域改为单列布局，图片移至文字下方，占满宽度；移动端（≤480px）文字字号调整为14px
**特效**: 无
**内容摘要**: 页面中部内容块，核心展示橱柜油漆与层压板的对比分析及光泽选择建议，包含文字说明与厨房实景图片

---

### 分块 12: image-text
- **截图**: `blue-kitchen-cabinets_pixel_12.jpg`
- **建议模块名**: `construction-quality-image-text`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #2d3748
- 标题: #2d3748
- 正文: #4a5568
- 边框: none

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 40px
- 下边距: 30px
- 元素间距: 20px
- 卡片内边距: 0

**组件** (8个):
  - image x1, 宽=50%, 高=auto, 圆角=0
    说明: 左侧蓝色橱柜图片，展示硬件细节
  - heading x2, 宽=auto, 高=auto, 圆角=0
    说明: 两个主标题：'Construction clues for quality'和'Day-to-Day Care'，深灰色（#2d3748），加粗700
  - list x1, 宽=auto, 高=auto, 圆角=0
    说明: 三个列表项，描述橱柜质量线索，使用项目符号
  - paragraph x1, 宽=auto, 高=auto, 圆角=0
    说明: 日常护理段落，描述清洁和维护建议
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 深灰色背景（#2d3748），白色文字，'Get a Free Quote'
  - heading x1, 宽=auto, 高=auto, 圆角=0, 有阴影
    说明: 预算规划标题'Budget & Planning: Where to Spend, Where to Save'，深灰色（#2d3748），加粗700
  - paragraph x1, 宽=auto, 高=auto, 圆角=0, 有阴影
    说明: 预算规划段落，描述蓝色橱柜的多种价格点
  - list x1, 宽=auto, 高=auto, 圆角=0, 有阴影
    说明: 编号列表项，'1. Map Your Zones: Prep, cook, clean, and snack'

**图片占位符** (1组):
  - **image** x1
    尺寸: 50% x auto, 比例: 4:3
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Construction clues for quality`
- **段落** (2个):
  - `Wipe up spills as they happen. Use a damp microfiber cloth and a mild soap, then dry immediately. St...`
  - `You can capture the look of blue cabinets at several price points: whether you're painting existing ...`
- **按钮文字**: `Get a Free Quote`
- **列表项** (3个):
  - `Soft close hardware keeps doors quiet and protects finishes over time.`: ...
  - `Strong cabinet boxes use plywood or high grade engineered wood that holds screws tight.`: ...
  - `Multi step finishes resist stains better. Ask how many steps are in the paint system, you should get a clear answer.`: ...

**响应式**: 平板设备（≤768px）下，布局改为单列，图片占满宽度，文字居中；移动端（≤480px）列表项改为单行显示，按钮文字简化为'Quote'
**特效**: 按钮hover时背景色加深至#1a202c
**内容摘要**: 展示橱柜质量的建设线索（如硬件、柜体、涂装）和日常护理建议，以及预算规划的基础信息

---

### 分块 13: content-block
- **截图**: `blue-kitchen-cabinets_pixel_13.jpg`
- **建议模块名**: `budget-planning-section`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #2d3748
- 标题: #222222
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
- 卡片内边距: 0

**组件** (4个):
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'Budget & Planning: Where to Spend, Where to Save'，深灰色（#222222），加粗700
  - paragraph x1, 宽=auto, 高=auto, 圆角=0
    说明: 段落描述蓝色橱柜的价格点和规划策略
  - list x1, 宽=auto, 高=auto, 圆角=0
    说明: 5个列表项，包含规划建议的标题和描述
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 深蓝色背景（#2d3748），白色文字，'Get a Free Quote'

**图片占位符** (1组):
  - **content-image** x1
    尺寸: 50% x auto, 比例: auto
    位置: 右侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Budget & Planning: Where to Spend, Where to Save`
- **段落** (1个):
  - `You can capture the look of blue cabinets at several price points: whether you're painting existing ...`
- **按钮文字**: `Get a Free Quote`
- **列表项** (5个):
  - `1. Map Your Zones`: Prep, cook, clean, and snack stations reduce back-...
  - `2. Sample in Real Light`: Order door samples and view them over a few days. ...
  - `3. Invest in Drawers`: Pot-and-pan drawers and pull-outs offer the best R...

**响应式**: 平板设备（≤768px）下，内容区域改为单列布局，图片占满宽度；移动端（≤480px）列表项改为单列，按钮文字保持不变
**特效**: 按钮hover时背景色加深至#1a202c
**内容摘要**: 页面中部内容块，展示蓝色橱柜预算规划与省钱策略，包含价格点分析、5条规划建议及行动号召按钮

---

### 分块 14: faq
- **截图**: `blue-kitchen-cabinets_pixel_14.jpg`
- **建议模块名**: `blue-cabinets-faqs`

**布局**:
- 容器: container-1200
- 类型: block
- 列数: 1, 行数: 1
- 水平间距: 0, 垂直间距: 40px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #2d3748
- 标题: #2d3748
- 正文: #4a5568
- 边框: #e2e8f0

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 20px
- 卡片内边距: 0

**组件** (2个):
  - faq-item x5, 宽=auto, 高=auto, 圆角=0
    说明: 每个FAQ项包含加号图标和问题文本，边框底部分隔，可折叠展开
  - form x1, 宽=auto, 高=auto, 圆角=8px
    说明: 包含姓名、邮箱、电话/WhatsApp、城市、国家选择输入框，产品需求复选框，提交按钮

**图片占位符** (1组):
  - **avatar** x1
    尺寸: 150px x 150px, 比例: 1:1
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `FAQs`
- **段落** (1个):
  - `* Kindly send us your project details and floor plan. We will quote for you within 8 hours!`
- **按钮文字**: `Get a Free Quote`
- **列表项** (5个):
  - `Are blue kitchen cabinets a fad?`: ...
  - `What's the best blue for a small kitchen?`: ...
  - `Which hardware looks best with blue cabinets?`: ...

**响应式**: 移动端下FAQ项改为单列，表单输入框占满宽度，复选框垂直排列
**特效**: FAQ项hover时加号图标变色，表单输入框focus时边框高亮
**内容摘要**: 页面中部FAQ模块，展示关于蓝色橱柜的常见问题及免费报价表单，包含5个可折叠问题项和联系表单

---

### 分块 15: faq
- **截图**: `blue-kitchen-cabinets_pixel_15.jpg`
- **建议模块名**: `blue-kitchen-cabinets-faq`

**布局**:
- 容器: container-1200
- 类型: block
- 列数: 1, 行数: 2
- 水平间距: 0, 垂直间距: 40px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #333333
- 标题: #222222
- 正文: #666666
- 边框: #e0e0e0

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 20px
- 卡片内边距: 0

**组件** (4个):
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'FAQs'，深灰色（#222222），加粗700
  - list x5, 宽=auto, 高=auto, 圆角=0
    说明: 5个FAQ问题列表，每个问题为可展开/折叠项，文本为灰色（#666666）
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 副标题'Get A Free Quote'，深灰色（#222222），加粗700
  - form x1, 宽=auto, 高=auto, 圆角=8px
    说明: 联系表单，包含Name、Email、Tel/Whatsapp、City、Country-Select输入框，Product Needed*复选框（9个选项），Message文本框，Choose File按钮，Send按钮

**图片占位符** (1组):
  - **avatar** x1
    尺寸: 150px x 200px, 比例: 3:4
    位置: 表单左侧, object-fit: cover
    占位符建议: avatar

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `FAQs`
- **副标题**: `Get A Free Quote`
- **段落** (1个):
  - `* Kindly send us your project details and floor plan. We will quote for you within 8 hours!`
- **按钮文字**: `Get a Free Quote`, `Send`
- **列表项** (5个):
  - `Are blue kitchen cabinets a fad?`: ...
  - `What's the best blue for a small kitchen?`: ...
  - `Which hardware looks best with blue cabinets?`: ...

**响应式**: 平板设备（≤768px）下，FAQ列表改为单列，表单字段堆叠；移动端（≤480px）头像隐藏，表单字段简化
**特效**: FAQ问题 hover 时背景色变浅（#f5f5f5），表单输入框 focus 时边框变色（#333333）
**内容摘要**: 页面中部FAQ模块，展示蓝色厨房橱柜的常见问题及获取免费报价的表单

---

### 分块 16: contact-form
- **截图**: `blue-kitchen-cabinets_pixel_16.jpg`
- **建议模块名**: `contact-form-bottom`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 1, 行数: 1
- 水平间距: 20px, 垂直间距: 30px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #6c757d
- 标题: #333333
- 正文: #666666
- 边框: #dee2e6

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 40px
- 下边距: 40px
- 元素间距: 20px
- 卡片内边距: 15px

**组件** (5个):
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'Want to Get Best Price Kitchen Cabinets?'，深灰色（#333333），加粗700
  - paragraph x1, 宽=auto, 高=auto, 圆角=0
    说明: 副标题'Share floor plan or house photos for 8-hour quote'，灰色（#666666）
  - textarea x1, 宽=100%, 高=120px, 圆角=4px
    说明: Message文本框，浅灰色背景（#f8f9fa），边框#dee2e6
  - file-input x1, 宽=auto, 高=auto, 圆角=4px
    说明: Choose File按钮，边框#dee2e6，显示'No file chosen'
  - button x1, 宽=100%, 高=40px, 圆角=4px
    说明: Send按钮，灰色背景（#6c757d），白色文字

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Want to Get Best Price Kitchen Cabinets?`
- **副标题**: `Share floor plan or house photos for 8-hour quote`
- **按钮文字**: `Send`

**响应式**: 平板设备（≤768px）和移动端（≤480px）下，表单元素改为单列布局，按钮宽度占满父容器
**特效**: Send按钮hover时背景色加深至#5a6268
**内容摘要**: 联系表单的下半部分，包含表单输入区域（Message文本框、文件上传）及提交按钮，用于收集用户项目信息和文件

---

### 分块 17: footer
- **截图**: `blue-kitchen-cabinets_pixel_17.jpg`
- **建议模块名**: `footer-sections`

**布局**:
- 容器: full-width
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: #000000
- 主色: #6c757d
- 标题: #ffffff
- 正文: #ffffff
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

**组件** (4个):
  - heading x4, 宽=auto, 高=auto, 圆角=0
    说明: 四个栏目标题：Products、One-Stop Solutions、Customer Services、Contact Us，白色文字，加粗
  - link x14, 宽=auto, 高=auto, 圆角=0
    说明: 各栏目下的链接，如Kitchen Cabinet、Wardrobe等，白色文字
  - form x1, 宽=auto, 高=auto, 圆角=4px
    说明: Contact Us下的订阅表单，包含whatsapp输入框、Email*输入框和Send按钮
  - icon x2, 宽=auto, 高=auto, 圆角=0
    说明: Contact Us下的邮箱和电话图标

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **按钮文字**: `Send`
- **卡片内容** (4个):
  - `Products`: ...
  - `One-Stop Solutions`: ...
  - `Customer Services`: ...

**响应式**: 平板设备（≤768px）下布局改为2列，移动端（≤480px）改为单列，订阅表单元素垂直堆叠
**特效**: 按钮hover时背景色加深
**内容摘要**: 页面底部footer区域，包含Products、One-Stop Solutions、Customer Services、Contact Us四个栏目，展示产品链接、解决方案、客户服务及联系方式，并设有订阅表单

---


---

## 设计参数汇总

### 颜色系统（CSS变量建议）
```css
:root {
    --color-primary: #6c757d;
    --color-secondary: #ffffff;
    --color-background: #000000;
    --color-heading: #ffffff;
    --color-text: #ffffff;
    --color-border: #dee2e6;
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


---

## 代码规范（详细）

### PHP模块结构
```php
<?php
if (!defined('ABSPATH')) {
    exit;
}

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
    </div>
</div>
```

### CSS样式结构
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

/* 响应式 */
@media (max-width: 1024px) {
    .{module-name}-module .module-title {
        font-size: 32px;
    }
}

@media (max-width: 768px) {
    .{module-name}-module {
        padding: 40px 0;
    }

    .{module-name}-module .module-title {
        font-size: 28px;
    }
}

@media (max-width: 480px) {
    .{module-name}-module .module-title {
        font-size: 24px;
    }
}
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
.image-placeholder {
    background: linear-gradient(135deg, #f0f0f0 0%, #e0e0e0 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #999;
    font-size: 14px;
    aspect-ratio: 16/9;
}
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
- `blue-kitchen-cabinets_pixel_1.jpg`
- `blue-kitchen-cabinets_pixel_10.jpg`
- `blue-kitchen-cabinets_pixel_11.jpg`
- `blue-kitchen-cabinets_pixel_12.jpg`
- `blue-kitchen-cabinets_pixel_13.jpg`
- `blue-kitchen-cabinets_pixel_14.jpg`
- `blue-kitchen-cabinets_pixel_15.jpg`
- `blue-kitchen-cabinets_pixel_16.jpg`
- `blue-kitchen-cabinets_pixel_17.jpg`
- `blue-kitchen-cabinets_pixel_2.jpg`
- `blue-kitchen-cabinets_pixel_3.jpg`
- `blue-kitchen-cabinets_pixel_4.jpg`
- `blue-kitchen-cabinets_pixel_5.jpg`
- `blue-kitchen-cabinets_pixel_6.jpg`
- `blue-kitchen-cabinets_pixel_7.jpg`
- `blue-kitchen-cabinets_pixel_8.jpg`
- `blue-kitchen-cabinets_pixel_9.jpg`

---

## 🎯 推荐输出方式：WordPress 页面模板

### 页面模板文件
**位置**: `wp-content/themes/{theme-name}/page-templates/template-{page-name}.php`

```php
<?php
/**
 * Template Name: {Page Name} 页面模板
 * Description: 克隆自 https://georgeconstructions.com/blue-kitchen-cabinets/
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
**位置**: `wp-content/themes/{theme-name}/assets/css/template-{page-name}.css`

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

### 在functions.php中注册样式

```php
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

1. 将PHP模板文件放入 `wp-content/themes/your-theme/page-templates/`
2. 将CSS文件放入 `wp-content/themes/your-theme/assets/css/`
3. 在`functions.php`中添加样式注册代码
4. WordPress后台 → 页面 → 新建页面
5. 选择页面模板并发布
