# WordPress 页面克隆任务

## ⚠️ 核心要求（必须满足）

1. **默认数据必须从截图提取真实内容** - 不可为空或使用占位符
2. **每个模块独立PHP文件** - `modules/{module-name}.php`
3. **完整的响应式CSS** - 4个断点（桌面/平板/移动/小屏）
4. **图片占位符使用placehold.co** - `https://placehold.co/600x400/e0e0e0/666?text=Product`

---

## 原始页面信息
- URL: https://georgeconstructions.com/gray-kitchen-cabinets/
- 标题: Gray Kitchen Cabinets: Timeless Meets Modern Kitchen Design
- 总高度: 12832px

---

## 页面结构分析

### 分块 1: hero
- **截图**: `gray-kitchen-cabinets_pixel_1.jpg`
- **建议模块名**: `gray-kitchen-cabinets-hero`

**布局**:
- 容器: full-width
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: #000000
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
- 卡片内边距: 0

**组件** (4个):
  - navbar x1, 宽=auto, 高=auto, 圆角=0
    说明: 顶部导航栏，包含7个链接（Products、Projects、Blog、Service、Video、About、Contact）和1个Quick Quote按钮，白色文字，橙色按钮背景
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'Custom Gray Kitchen Cabinets: Perfect for Any Home or Project'，'Gray'为橙色（#FF8C00），其余为白色（#ffffff），加粗700
  - paragraph x1, 宽=auto, 高=auto, 圆角=0
    说明: 描述文字'Gray kitchen cabinets are timeless, versatile, and elegant—perfect for any kitchen style. Discover why they're a top choice for homeowners, architects, and builders alike.'，白色文字
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 橙色背景（#FF8C00），白色文字，'Get A Free Quote'

**图片占位符** (1组):
  - **hero-banner** x1
    尺寸: 100% x auto, 比例: auto
    位置: 背景覆盖, object-fit: cover
    遮罩: #00000080
    占位符建议: gradient-overlay

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Custom Gray Kitchen Cabinets: Perfect for Any Home or Project`
- **段落** (1个):
  - `Gray kitchen cabinets are timeless, versatile, and elegant—perfect for any kitchen style. Discover w...`
- **按钮文字**: `Get A Free Quote`

**响应式**: 平板设备（≤768px）下，导航栏改为汉堡菜单，hero区域改为单列布局，图片占满宽度；移动端（≤480px）按钮文字简化为'Quote'
**特效**: 按钮hover时背景色加深至#E67300，背景图片带有半透明黑色overlay增强文字可读性
**内容摘要**: 页面顶部hero区域，核心展示灰色厨房橱柜的主题信息，包含主标题、产品描述及行动号召按钮，背景为现代厨房场景图片

---

### 分块 2: product-grid
- **截图**: `gray-kitchen-cabinets_pixel_2.jpg`
- **建议模块名**: `gray-kitchen-cabinets-grid`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 2
- 水平间距: 20px, 垂直间距: 30px
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #2D3748
- 标题: #333333
- 正文: #666666
- 边框: none

**字体**:
- 标题: 20px, 字重: 600
- 正文: 16px, 字重: 400
- 行高: 1.5

**间距**:
- 上边距: 50px
- 下边距: 50px
- 元素间距: 0
- 卡片内边距: 15px

**组件** (1个):
  - card x8, 宽=auto, 高=auto, 圆角=8px, 有阴影
    说明: 白色背景卡片，带轻微阴影，每个卡片包含产品图片和标题文字

**图片占位符** (1组):
  - **product** x8
    尺寸: 100% x 200px, 比例: 1:1
    位置: 网格排列, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **按钮文字**: `Get a Free Quote`
- **卡片内容** (8个):
  - `Gray Kitchen Cabinets`: ...
  - `Blue Gray Kitchen Cabinets`: ...
  - `Modern Gray Kitchen Cabinets`: ...

**响应式**: 平板设备（≤768px）下，网格改为2列布局；移动端（≤480px）改为1列，卡片宽度占满容器
**特效**: 卡片hover时阴影加深，标题文字可能变为深灰色（#333333）
**内容摘要**: 页面中部展示8种不同风格的灰色厨房橱柜产品，以网格形式排列，每个产品卡片包含图片和标题，下方有行动号召按钮

---

### 分块 3: features
- **截图**: `gray-kitchen-cabinets_pixel_3.jpg`
- **建议模块名**: `kitchen-cabinets-materials-features`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 20px, 垂直间距: 20px
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #2d3748
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
    说明: 白色背景卡片，包含材料标题、描述文字和定制按钮，无阴影和边框
  - button x4, 宽=auto, 高=40px, 圆角=8px
    说明: 深蓝色（#2d3748）背景，白色文字，'Custom Now'按钮，圆角8px

**图片占位符** (1组):
  - **none** x0
    尺寸: auto x auto, 比例: auto
    位置: 无, object-fit: none
    占位符建议: 无

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Premium Gray Kitchen Cabinets: Durable Materials That Last`
- **段落** (4个):
  - `Choosing gray particleboard kitchen cabinets is a great way to combine a modern look with eco-friend...`
  - `The material known as MDF is a construction material that is made up of residual hardwood and softwo...`
  - `Plywood cabinets are not as common as particleboard or MDF options. Gray plywood cabinets are crafte...`
- **按钮文字**: `Custom Now`, `Custom Now`, `Custom Now`, `Custom Now`
- **卡片内容** (4个):
  - `Particle Board`: Choosing gray particleboard kitchen cabinets is a ...
  - `MDF`: The material known as MDF is a construction materi...
  - `Plywood`: Plywood cabinets are not as common as particleboar...

**响应式**: 平板设备（≤768px）下，网格布局改为2列；移动端（≤480px）下改为1列，按钮文字保持不变
**特效**: 按钮hover时背景色变浅（如#4a5568），文字颜色保持白色
**内容摘要**: 页面中部展示灰色厨房橱柜的四种材料选项（刨花板、MDF、胶合板、实木），每个材料包含特点描述及定制按钮，强调材料的耐用性和环保性

---

### 分块 4: features
- **截图**: `gray-kitchen-cabinets_pixel_4.jpg`
- **建议模块名**: `kitchen-cabinets-custom-finishes`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 30px, 垂直间距: 40px
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #2D3748
- 标题: #2D3748
- 正文: #4A5568
- 边框: none

**字体**:
- 标题: 28px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 20px
- 卡片内边距: 25px

**组件** (2个):
  - card x4, 宽=auto, 高=auto, 圆角=8px
    说明: 白色背景卡片，包含标题、描述文本和按钮，每个卡片内边距25px
  - button x4, 宽=auto, 高=40px, 圆角=6px
    说明: 深灰色背景（#2D3748），白色文字，'Custom Now'按钮

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Upgrade Gray Kitchen Cabinets with Custom Finishes`
- **段落** (4个):
  - `Modern gray kitchen cabinets come with a flat, smooth surface or bespoke curves. Future cleaning and...`
  - `Gray cabinetry with a translucent glaze finish will make your kitchen stand out. In addition to comp...`
  - `Wood grain aesthetics are versatile and may be used in both modern and rustic kitchens. Grey wood gr...`
- **按钮文字**: `Custom Now`, `Custom Now`, `Custom Now`, `Custom Now`
- **卡片内容** (4个):
  - `Smooth Flat And Dimpled Finishing`: Modern gray kitchen cabinets come with a flat, smo...
  - `Glaze Finishing`: Gray cabinetry with a translucent glaze finish wil...
  - `Woodgrain Finishing`: Wood grain aesthetics are versatile and may be use...

**响应式**: 平板设备（≤768px）下，卡片布局改为2列；移动端（≤480px）改为单列，按钮宽度占满
**特效**: 按钮hover时背景色加深至#1A202C，文字颜色保持白色
**内容摘要**: 展示灰色厨房橱柜的四种定制饰面选项，包括每种饰面的特点描述及定制按钮，帮助用户选择合适的饰面风格

---

### 分块 5: features
- **截图**: `gray-kitchen-cabinets_pixel_5.jpg`
- **建议模块名**: `kitchen-layout-features`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 30px, 垂直间距: 30px
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #2d3748
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
    说明: 白色卡片，包含布局标题、描述文字和"Custom Now"按钮，每个卡片展示一种厨房布局选项

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Gray Kitchen Cabinets Designed for Your Space`
- **段落** (4个):
  - `Designing your gray kitchen cabinets in a U-shaped layout is absolutely perfect! Contributes to maki...`
  - `A great choice for small kitchens is the I-shaped layout! Cleanliness, minimalism, and efficacy are ...`
  - `Unlike the I-shaped layout, the L-shaped layout makes better use of corner space and forms a useful ...`
- **按钮文字**: `Custom Now`
- **卡片内容** (4个):
  - `U-shaped`: Designing your gray kitchen cabinets in a U-shaped...
  - `I-shaped`: A great choice for small kitchens is the I-shaped ...
  - `L-shaped`: Unlike the I-shaped layout, the L-shaped layout ma...

**响应式**: 平板设备（≤768px）下，布局改为2列；移动端（≤480px）下，布局改为1列，按钮文字保持不变
**特效**: 按钮hover时背景色可能加深至#1a202c，文字颜色保持白色
**内容摘要**: 该区域主要展示四种厨房布局选项（U-shaped、I-shaped、L-shaped、Island）及其特点，帮助用户根据厨房空间和需求选择合适的布局方案

---

### 分块 6: features
- **截图**: `gray-kitchen-cabinets_pixel_6.jpg`
- **建议模块名**: `gray-kitchen-cabinets-accessories`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 30px, 垂直间距: 40px
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
    说明: 白色背景卡片，包含标题、描述文字和'Custom Now'按钮，每个卡片对应一种厨房配件（水槽、把手、铰链、抽屉）
  - button x4, 宽=auto, 高=40px, 圆角=8px
    说明: 深蓝色（#2D3748）背景，白色文字，'Custom Now'按钮，位于每个卡片底部

**图片占位符** (1组):
  - **thumbnail** x0
    尺寸: auto x auto, 比例: auto
    位置: 无, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Must-Have Accessories for Gray Kitchen Cabinets`
- **按钮文字**: `Custom Now`, `Custom Now`, `Custom Now`, `Custom Now`
- **卡片内容** (4个):
  - `Sink`: George has a wide variety of sink materials to cho...
  - `Handle`: Picking the right handle can definitely cut down o...
  - `Hinge`: You've probably seen many modern kitchens with tho...

**响应式**: 平板设备（≤768px）下，卡片布局改为2列；移动端（≤480px）下改为1列，按钮文字保持不变
**特效**: 按钮hover时背景色加深至#1A202C，文字保持白色
**内容摘要**: 页面中部展示灰色厨房橱柜的必备配件，包括水槽、把手、铰链、抽屉四种类型，每个配件卡片包含详细描述和定制按钮，帮助用户了解配件选择及功能

---

### 分块 7: content-block
- **截图**: `gray-kitchen-cabinets_pixel_7.jpg`
- **建议模块名**: `gray-cabinets-shades-undertones`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 5, 行数: 6
- 水平间距: 20px, 垂直间距: 10px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #333333
- 标题: #333333
- 正文: #000000
- 边框: #e0e0e0

**字体**:
- 标题: 28px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 30px
- 卡片内边距: 15px

**组件** (1个):
  - table x1, 宽=100%, 高=auto, 圆角=0
    说明: 6行5列表格，表头背景#333333（深灰色），白色文字；数据行背景#ffffff（白色），黑色文字，边框#e0e0e0（浅灰色）

**图片占位符** (1组):
  - **none** x0
    尺寸: auto x auto, 比例: auto
    位置: none, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Shades, Undertones, And What They Do To Your Space`
- **段落** (1个):
  - `All grays carry an undertone. Blue, green, violet, even a whisper of brown. That undertone is what d...`
- **卡片内容** (5个):
  - `Blue-leaning`: Crisp, airy, modern; Soft white or pale greige; Wh...
  - `Green-leaning`: Organic, calm, earthy; Warm white or clay beige; B...
  - `Violet-leaning`: Sophisticated, cool toned; Warm white with a hint ...

**响应式**: 平板设备（≤768px）下，表格改为单列布局，表头固定；移动端（≤480px）表格内容可横向滚动
**特效**: 表格表头hover时背景色加深至#222222，文字保持白色
**内容摘要**: 该区域主要展示灰色橱柜的不同色调（底色）及其对空间氛围的影响，通过表格形式提供适合的墙面颜色、台面材质和五金配件建议

---

### 分块 8: features
- **截图**: `gray-kitchen-cabinets_pixel_8.jpg`
- **建议模块名**: `gray-cabinet-door-styles`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #2d3748
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
  - card x4, 宽=auto, 高=auto, 圆角=8px
    说明: 白色背景卡片，包含门风格标题、描述文字和定制按钮，每个卡片布局一致
  - button x4, 宽=auto, 高=40px, 圆角=6px
    说明: 深蓝色背景（#2d3748），白色文字，统一显示'Custom Now'

**图片占位符** (1组):
  - **thumbnail** x0
    尺寸: auto x auto, 比例: auto
    位置: 无图片，纯文字卡片, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Popular Door Styles In Gray`
- **副标题**: `Choose the profile first, then dial the color. Door style sets the character of the room and affects cleaning effort. Here are the four most requested looks in our projects.`
- **按钮文字**: `Custom Now`, `Custom Now`, `Custom Now`, `Custom Now`
- **卡片内容** (4个):
  - `Shaker`: Flexible, trim lines work with almost any handle. ...
  - `Slab`: Clean and seamless. Perfect with long pulls or pus...
  - `Beadboard`: Cottage charm for pantries or islands. Paint in li...

**响应式**: 平板设备（≤768px）下，门风格卡片改为2列布局；移动端（≤480px）改为1列，按钮文字保持不变
**特效**: 按钮hover时背景色加深至#1a202c，文字保持白色
**内容摘要**: 页面中部展示灰色橱柜的四种流行门风格（Shaker、Slab、Beadboard、Fluted or ribbed accents），每个风格包含特点描述及定制按钮，帮助用户选择合适的门型

---

### 分块 9: product-grid
- **截图**: `gray-kitchen-cabinets_pixel_9.jpg`
- **建议模块名**: `gray-door-styles-grid`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 20px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #2D3E50
- 标题: #333333
- 正文: #666666
- 边框: none

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 40px
- 下边距: 30px
- 元素间距: 20px
- 卡片内边距: 20px

**组件** (1个):
  - card x4, 宽=auto, 高=auto, 圆角=8px
    说明: 包含门风格标题、描述文字和'Custom Now'按钮的白色卡片，每个卡片独立展示一种门风格

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Popular Door Styles In Gray`
- **副标题**: `Choose the profile first, then dial the color. Door style sets the character of the room and affects cleaning effort. Here are the four most requested looks in our projects.`
- **段落** (4个):
  - `Flexible, trim lines work with almost any handle. Easy to paint or stain. Great for classic-meets-mo...`
  - `Clean and seamless. Perfect with long pulls or push-latch for a minimal look.`
  - `Cottage charm for pantries or islands. Paint in light gray to keep it fresh, not fussy.`
- **按钮文字**: `Custom Now`, `Custom Now`, `Custom Now`, `Custom Now`
- **卡片内容** (4个):
  - `Shaker`: Flexible, trim lines work with almost any handle. ...
  - `Slab`: Clean and seamless. Perfect with long pulls or pus...
  - `Beadboard`: Cottage charm for pantries or islands. Paint in li...

**响应式**: 平板设备（≤768px）下改为2列布局，移动端（≤480px）改为1列布局，按钮文字保持不变
**特效**: 按钮hover时背景色可能变浅（如#3A4F6B），提升交互反馈
**内容摘要**: 页面中部展示四种流行的灰色门风格，每个风格包含特点描述和定制按钮，帮助用户选择适合的门型

---

### 分块 10: content-block
- **截图**: `gray-kitchen-cabinets_pixel_10.jpg`
- **建议模块名**: `kitchen-layout-tips`

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
- 元素间距: 30px
- 卡片内边距: 0

**组件** (3个):
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'Layout Tips That Make Gray Shine'，深灰色（#222222），加粗700
  - paragraph x2, 宽=auto, 高=auto, 圆角=0
    说明: 两个段落，描述灰色橱柜的布局技巧，包括厨房动线规划、区域划分建议
  - image x1, 宽=50%, 高=auto, 圆角=0
    说明: 右侧展示厨房布局的图片，灰色橱柜与白色墙面搭配，体现现代简约风格

**图片占位符** (1组):
  - **content-image** x1
    尺寸: 50% x auto, 比例: auto
    位置: 右侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Layout Tips That Make Gray Shine`
- **段落** (2个):
  - `Color is only half of the picture. The smartest-looking kitchens handle traffic and tasks without fr...`
  - `For deep planning questions, check NKBA's planning page for accepted dimensions and safe clearances.`

**响应式**: 平板设备（≤768px）下，左右布局改为单列，图片占满宽度；移动端（≤480px）图片置于文字下方，宽度100%
**特效**: 无
**内容摘要**: 该区域主要展示让灰色橱柜更出色的布局技巧，包括厨房动线规划、区域划分及安全间距建议

---

### 分块 11: content-block
- **截图**: `gray-kitchen-cabinets_pixel_11.jpg`
- **建议模块名**: `kitchen-cabinets-two-tone-ideas`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #333333
- 标题: #222222
- 正文: #444444
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
    说明: 主标题'Two-Tone Looks And Accent Ideas'，深灰色（#222222），加粗700
  - paragraph x1, 宽=auto, 高=auto, 圆角=0
    说明: 段落描述灰色的搭配技巧，包含小厨房和大空间的搭配建议
  - list x1, 宽=auto, 高=auto, 圆角=0
    说明: 三个列表项，每个包含灰色的搭配方案描述
  - image x1, 宽=auto, 高=auto, 圆角=0
    说明: 右侧厨房图片，展示灰色的两色搭配效果

**图片占位符** (1组):
  - **product** x1
    尺寸: 50% x auto, 比例: 16:9
    位置: 右侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Two-Tone Looks And Accent Ideas`
- **段落** (1个):
  - `Gray plays nicely with contrast. Small kitchens get a lift with pale gray uppers and medium gray bas...`
- **列表项** (3个):
  - `Light gray perimeter with a walnut or white oak island`: Inviting and fresh....
  - `Charcoal base units with white uppers`: Graphic and modern without feeling hard....
  - `Greige shaker doors with marble-look quartz`: Soft and timeless for all-day livability....

**响应式**: 平板设备（≤768px）下，内容改为单列布局，图片占满宽度；移动端（≤480px）列表项文字简化，图片置于文字上方
**特效**: 无
**内容摘要**: 页面中部内容块，展示灰色橱柜的两色搭配技巧及具体方案，包含文字说明和厨房效果图

---

### 分块 12: image-text
- **截图**: `gray-kitchen-cabinets_pixel_12.jpg`
- **建议模块名**: `gray-kitchen-cabinets-two-tone`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: space-between

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
- 上边距: 40px
- 下边距: 30px
- 元素间距: 20px
- 卡片内边距: 0

**组件** (4个):
  - image x1, 宽=50%, 高=auto, 圆角=0
    说明: 左侧厨房场景图片，展示灰色柜子与白色台面的搭配
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'Two-Tone Looks And Accent Ideas'，深灰色（#333333），加粗700
  - paragraph x1, 宽=auto, 高=auto, 圆角=0
    说明: 描述灰色柜子与对比色的搭配建议，包括小厨房和大空间的配色方案
  - list x1, 宽=auto, 高=auto, 圆角=0
    说明: 三个bullet points，分别介绍浅灰色 perimeter 与核桃/白橡岛台、炭灰色底柜与白色上柜、灰褐色 shaker 门与大理石纹理石英石的搭配

**图片占位符** (1组):
  - **hero-banner** x1
    尺寸: 50% x auto, 比例: auto
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Two-Tone Looks And Accent Ideas`
- **段落** (1个):
  - `Gray plays nicely with contrast. Small kitchens get a lift with pale gray uppers and medium gray bas...`
- **列表项** (3个):
  - `Light gray perimeter with a walnut or white oak island`: Inviting and fresh....
  - `Charcoal base units with white uppers`: Graphic and modern without feeling hard....
  - `Greige shaker doors with marble-look quartz`: Soft and timeless for all-day livability....

**响应式**: 平板设备（≤768px）下，图文布局改为单列，图片占满宽度；移动端（≤480px）列表项改为单列排列
**特效**: 无
**内容摘要**: 展示灰色厨房柜子的双色调和 accent ideas，通过图片与文字结合说明不同配色方案的应用场景及效果

---

### 分块 13: why-choose
- **截图**: `gray-kitchen-cabinets_pixel_13.jpg`
- **建议模块名**: `why-choose-gray-cabinets`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 3, 行数: 1
- 水平间距: 30px, 垂直间距: 40px
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #333333
- 标题: #222222
- 正文: #666666
- 边框: none

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - card x3, 宽=auto, 高=auto, 圆角=0
    说明: 三个卡片，每个包含图片、标题、描述和箭头链接，展示为什么选择该公司的原因

**图片占位符** (1组):
  - **feature-image** x3
    尺寸: auto x auto, 比例: auto
    位置: 网格排列（每个卡片左侧）, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Why George Constructions for Gray Kitchen Cabinets`
- **副标题**: `Three reasons our clients come back: selection, engineering, and service. Here is how that helps your project.`
- **按钮文字**: `→`
- **卡片内容** (3个):
  - `Broad selection`: Link into our dedicated gray collection to compare...
  - `Engineered quality`: Our cabinet boxes and finishes are built for real-...
  - `Design support`: From mood boards to shop drawings, our team guides...

**响应式**: 平板设备（≤768px）下，卡片布局改为2列；移动端（≤480px）改为单列，图片宽度占满
**特效**: 卡片链接hover时可能有颜色变化或下划线效果
**内容摘要**: 页面中部展示为什么选择George Constructions的三个核心优势：广泛的产品选择、工程质量和设计支持，每个优势通过卡片形式呈现，包含图片、标题、描述及链接

---

### 分块 14: content-block
- **截图**: `gray-kitchen-cabinets_pixel_14.jpg`
- **建议模块名**: `gray-kitchen-cabinets-planner-faq`

**布局**:
- 容器: container-1200
- 类型: block
- 列数: 1, 行数: 3
- 水平间距: 0, 垂直间距: 30px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #333333
- 标题: #333333
- 正文: #666666
- 边框: #e0e0e0

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 40px
- 下边距: 40px
- 元素间距: 20px
- 卡片内边距: 15px

**组件** (3个):
  - list x1, 宽=auto, 高=auto, 圆角=0
    说明: 5步指南列表，每步以数字编号，描述选择灰色橱柜的步骤
  - accordion x1, 宽=auto, 高=auto, 圆角=8px
    说明: 4个FAQ折叠面板，每个面板包含问题标题，可展开查看答案
  - text x1, 宽=auto, 高=auto, 圆角=0
    说明: 下一步行动段落，包含联系团队和访问博客的提示

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Quick Planner: Choose Your Gray In 5 Steps`
- **段落** (1个):
  - `Collect inspiration, measure, and send us your plan. Contact our team for a free consultation and a ...`
- **按钮文字**: `Contact our team`
- **列表项** (5个):
  - `1. Check your light`: North-facing rooms look cooler. South-facing reads...
  - `2. Pick a door style`: that suits the architecture. Shaker for transition...
  - `3. Select a finish`: Satin is the reliable daily driver. Matte for a so...
- **卡片内容** (4个):
  - `Will gray cabinets go out of style soon?`: ...
  - `Which hardware looks best with gray?`: ...
  - `Light or dark gray for a small kitchen?`: ...

**响应式**: 平板设备（≤768px）和移动端（≤480px）下，保持单列布局，步骤列表和FAQ面板自适应宽度，折叠面板在移动端可点击展开
**特效**: FAQ折叠面板具有展开/收起动画效果，点击问题标题可切换显示答案
**内容摘要**: 展示选择灰色厨房橱柜的5步规划指南、常见问题解答及下一步行动建议，帮助用户决策

---

### 分块 15: contact-form
- **截图**: `gray-kitchen-cabinets_pixel_15.jpg`
- **建议模块名**: `gray-kitchen-cabinets-contact-form`

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
- 正文: #666666
- 边框: #e0e0e0

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 50px
- 下边距: 50px
- 元素间距: 20px
- 卡片内边距: 20px

**组件** (4个):
  - image x1, 宽=45%, 高=auto, 圆角=0
    说明: 左侧展示George店铺外观的图片，用于增强品牌信任感
  - form x1, 宽=55%, 高=auto, 圆角=0
    说明: 包含姓名、邮箱、电话、城市、国家选择、产品需求（多选框）、消息文本域、文件上传和发送按钮的表单
  - heading x2, 宽=auto, 高=auto, 圆角=0
    说明: 两个标题：'Next Steps' 和 'Get A Free Quote'，深灰色（#222222），加粗700
  - paragraph x2, 宽=auto, 高=auto, 圆角=0
    说明: 两个段落，分别描述下一步行动指引和色彩搭配建议

**图片占位符** (1组):
  - **thumbnail** x1
    尺寸: 45% x auto, 比例: 4:3
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Get A Free Quote`
- **副标题**: `* Kindly send us your project details and floor plan. We will quote for you within 8 hours!`
- **段落** (2个):
  - `Collect inspiration, measure, and send us your plan. Contact our team for a free consultation and a ...`
  - `Further reading for color pairing ideas: Benjamin Moore gray families and Kitchen Cabinet Depot's mo...`
- **按钮文字**: `Send`

**响应式**: 平板设备（≤768px）下，左右两列改为单列布局，图片宽度调整为100%；移动端（≤480px）表单元素堆叠显示，按钮文字居中
**特效**: 表单输入框hover时边框色加深至#ccc；发送按钮hover时背景色加深至#555
**内容摘要**: 页面中部联系表单区域，核心展示获取灰色厨房橱柜报价的表单及配套指引，包含品牌店铺图片、行动号召文字和详细表单字段

---

### 分块 16: contact-form
- **截图**: `gray-kitchen-cabinets_pixel_16.jpg`
- **建议模块名**: `gray-kitchen-cabinets-quote-form`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #6c757d
- 标题: #222222
- 正文: #333333
- 边框: #dee2e6

**字体**:
- 标题: 24px, 字重: 600
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 40px
- 下边距: 40px
- 元素间距: 20px
- 卡片内边距: 15px

**组件** (2个):
  - image x1, 宽=45%, 高=auto, 圆角=0
    说明: 左侧展示George店铺外观图片，用于增强品牌信任感
  - form x1, 宽=55%, 高=auto, 圆角=0
    说明: 包含Name、Email、Tel/Whatsapp、City、Country-Select输入框，Product Needed复选框组，Message文本域，Choose File按钮及Send提交按钮

**图片占位符** (1组):
  - **product-banner** x1
    尺寸: 100% x auto, 比例: auto
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Get A Free Quote`
- **段落** (3个):
  - `Collect inspiration, measure, and send us your plan. Contact our team for a free consultation and a ...`
  - `Further reading for color pairing ideas: Benjamin Moore gray families and Kitchen Cabinet Depot's mo...`
  - `* Kindly send us your project details and floor plan. We will quote for you within 8 hours!`
- **按钮文字**: `Send`

**响应式**: 平板设备（≤768px）下，表单区域改为单列布局，图片与表单垂直排列；移动端（≤480px）输入框宽度占满，复选框组单列显示
**特效**: Send按钮hover时背景色加深至#5a6268
**内容摘要**: 页面中部联系表单模块，核心展示灰色厨房橱柜报价申请流程，包含店铺形象图、表单填写说明及详细报价申请表单

---

### 分块 17: contact-form
- **截图**: `gray-kitchen-cabinets_pixel_17.jpg`
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
- 标题: #333333
- 正文: #666666
- 边框: #ddd

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 40px
- 下边距: 40px
- 元素间距: 20px
- 卡片内边距: 15px

**组件** (6个):
  - image x1, 宽=45%, 高=auto, 圆角=0
    说明: 左侧店铺图片，显示George constructions的店面
  - input x5, 宽=100%, 高=40px, 圆角=4px
    说明: Name、Email、Tel/Whatsapp、City、Country-Select输入框，白色背景，浅灰色边框
  - checkbox x10, 宽=auto, 高=auto, 圆角=0
    说明: Product Needed的10个选项复选框，包括Kitchen cabinet、Bedroom、Bathroom、Windows & Doors、Furniture、Lighting、Soft Furnishing、Tiles and Wood Flooring、Whole House Solution、Other Building Material
  - textarea x1, 宽=100%, 高=120px, 圆角=4px
    说明: Message文本框，白色背景，浅灰色边框
  - file-upload x1, 宽=100%, 高=40px, 圆角=4px
    说明: Choose File文件上传按钮，白色背景，浅灰色边框
  - button x1, 宽=100%, 高=40px, 圆角=4px
    说明: Send按钮，灰色背景，白色文字

**图片占位符** (1组):
  - **product** x1
    尺寸: 45% x auto, 比例: auto
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Get A Free Quote`
- **副标题**: `Want to Get Best Price Gray Kitchen Cabinets?`
- **段落** (2个):
  - `* Kindly send us your project details and floor plan. We will quote for you within 8 hours!`
  - `Share floor plan or house photos for 8-hour quote`
- **按钮文字**: `Send`

**响应式**: 平板设备（≤768px）下，左右分栏改为单列，图片在上，表单在下；移动端（≤480px）输入框占满宽度，复选框改为单列
**特效**: Send按钮hover时背景色加深至#555555
**内容摘要**: 提供免费报价的表单，用户可提交项目详情、图纸及产品需求，获取8小时内的定制报价

---

### 分块 18: footer
- **截图**: `gray-kitchen-cabinets_pixel_18.jpg`
- **建议模块名**: `footer-common`

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
- 上边距: 60px
- 下边距: 60px
- 元素间距: 20px
- 卡片内边距: 0

**组件** (3个):
  - heading x4, 宽=auto, 高=auto, 圆角=0
    说明: 四个列标题：'Products'、'One-Stop Solutions'、'Customer Services'、'Contact Us'，白色文字，加粗
  - link x17, 宽=auto, 高=auto, 圆角=0
    说明: 17个链接文字，包括'Kitchen Cabinet'、'Wardrobe'等，白色文字，无下划线
  - form x3, 宽=auto, 高=auto, 圆角=4px
    说明: 包含'whatsapp'输入框、'Email*'输入框、'Send'按钮，输入框白色背景，灰色边框，按钮灰色背景

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **按钮文字**: `Send`
- **列表项** (4个):
  - `Products`: ['Kitchen Cabinet', 'Wardrobe', 'Windows and Doors...
  - `One-Stop Solutions`: ['Hotel Solutions', 'Resort Solutions', 'Villa Sol...
  - `Customer Services`: ['CUSTOMER SERVICES', 'Measurement Guidance', 'Pac...

**响应式**: 平板设备（≤768px）下，四列改为两列布局；移动端（≤480px）下改为单列布局，各元素垂直排列
**特效**: 按钮hover时背景色加深，链接hover时文字颜色变浅
**内容摘要**: 页面底部footer区域，展示产品分类、一站式解决方案、客户服务及联系方式，包含导航链接和订阅表单

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
    --color-border: #ddd;
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
    --spacing-module-top: 60px;
    --spacing-module-bottom: 60px;
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
- `gray-kitchen-cabinets_pixel_1.jpg`
- `gray-kitchen-cabinets_pixel_10.jpg`
- `gray-kitchen-cabinets_pixel_11.jpg`
- `gray-kitchen-cabinets_pixel_12.jpg`
- `gray-kitchen-cabinets_pixel_13.jpg`
- `gray-kitchen-cabinets_pixel_14.jpg`
- `gray-kitchen-cabinets_pixel_15.jpg`
- `gray-kitchen-cabinets_pixel_16.jpg`
- `gray-kitchen-cabinets_pixel_17.jpg`
- `gray-kitchen-cabinets_pixel_18.jpg`
- `gray-kitchen-cabinets_pixel_2.jpg`
- `gray-kitchen-cabinets_pixel_3.jpg`
- `gray-kitchen-cabinets_pixel_4.jpg`
- `gray-kitchen-cabinets_pixel_5.jpg`
- `gray-kitchen-cabinets_pixel_6.jpg`
- `gray-kitchen-cabinets_pixel_7.jpg`
- `gray-kitchen-cabinets_pixel_8.jpg`
- `gray-kitchen-cabinets_pixel_9.jpg`

---

## 🎯 推荐输出方式：WordPress 页面模板

### 页面模板文件
**位置**: `wp-content/themes/{theme-name}/page-templates/template-{page-name}.php`

```php
<?php
/**
 * Template Name: {Page Name} 页面模板
 * Description: 克隆自 https://georgeconstructions.com/gray-kitchen-cabinets/
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
