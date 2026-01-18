# WordPress 页面克隆任务

## ⚠️ 核心要求（必须满足）

1. **默认数据必须从截图提取真实内容** - 不可为空或使用占位符
2. **每个模块独立PHP文件** - `modules/{module-name}.php`
3. **完整的响应式CSS** - 4个断点（桌面/平板/移动/小屏）
4. **图片占位符使用placehold.co** - `https://placehold.co/600x400/e0e0e0/666?text=Product`

---

## 原始页面信息
- URL: https://georgeconstructions.com/mdf-kitchen-cabinets/
- 标题: Custom Modern Kitchen Cabinets｜ Design ideas
- 总高度: 12268px

---

## 页面结构分析

### 分块 1: hero
- **截图**: `mdf-kitchen-cabinets_pixel_1.jpg`
- **建议模块名**: `kitchen-cabinets-hero`

**布局**:
- 容器: full-width
- 类型: flex
- 列数: 1, 行数: 1
- 水平间距: 0, 垂直间距: 0
- 对齐: center

**颜色**:
- 背景: #000000
- 主色: #FF8C00
- 标题: #ffffff
- 正文: #ffffff
- 边框: none

**字体**:
- 标题: 48px, 字重: 700
- 正文: 20px, 字重: 400
- 行高: 1.5

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 20px
- 卡片内边距: 0

**组件** (3个):
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'MDF KITCHEN CABINETS'，白色（#ffffff），加粗700
  - paragraph x1, 宽=auto, 高=auto, 圆角=0
    说明: 副标题'One-Stop Building Material Solution Supplier'，白色（#ffffff），常规400
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 橙色背景（#FF8C00），白色文字，'Quick Quote'

**图片占位符** (1组):
  - **hero-banner** x1
    尺寸: 100% x auto, 比例: 16:9
    位置: 居中, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `MDF KITCHEN CABINETS`
- **副标题**: `One-Stop Building Material Solution Supplier`
- **按钮文字**: `Quick Quote`

**响应式**: 平板设备（≤768px）下，主标题字体缩小至36px，副标题缩小至16px；移动端（≤480px）按钮宽度调整为90%
**特效**: 按钮hover时背景色加深至#E67300
**内容摘要**: 页面顶部hero区域，核心展示MDF厨房橱柜的主题信息，包含主标题、副标题及行动号召按钮，背景为深色厨房实景图

---

### 分块 2: product-grid
- **截图**: `mdf-kitchen-cabinets_pixel_2.jpg`
- **建议模块名**: `kitchen-cabinets-product-grid`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 3, 行数: 2
- 水平间距: 20px, 垂直间距: 30px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #222222
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
  - card x6, 宽=auto, 高=auto, 圆角=8px, 有阴影
    说明: 白色卡片，带轻微阴影，每个卡片包含产品图片、标题和描述文字

**图片占位符** (1组):
  - **product-thumbnail** x6
    尺寸: 100% x 200px, 比例: 16:9
    位置: 网格排列, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Custom MDF Kitchen Cabinet Designs`
- **卡片内容** (6个):
  - `U Shaped Kitchen Island MDF Cabinets`: U Shaped Kitchen MDF Cabinets For Sale Design of P...
  - `Two-tone MDF Kitchen Cabinets`: U Shaped MDF Kitchen Cabinets With Marble The Esse...
  - `One Wall MDF Kitchen Cabinets`: Custom MDF Kitchen Cabinets Design of Products Thi...

**响应式**: 平板设备（≤768px）下，网格改为2列；移动端（≤480px）改为单列布局，卡片宽度占满
**特效**: 卡片hover时阴影加深，图片缩放效果
**内容摘要**: 页面中部产品网格模块，展示6种不同设计的MDF厨房橱柜，每个卡片包含产品图片、标题和简短描述

---

### 分块 3: content-block
- **截图**: `mdf-kitchen-cabinets_pixel_3.jpg`
- **建议模块名**: `mdf-types-content-block`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0
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
- 卡片内边距: 0

**组件** (3个):
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'6 Types of MDF'，深灰色（#333333），加粗700
  - list x1, 宽=auto, 高=auto, 圆角=0
    说明: 6种MDF类型列表，包含标题和描述，文字颜色#666666
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 橙色背景（#FF8C00），白色文字，'Consult'按钮

**图片占位符** (1组):
  - **content-image** x1
    尺寸: 45% x auto, 比例: auto
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `6 Types of MDF`
- **按钮文字**: `Consult`
- **列表项** (6个):
  - `Standard MDF`: Typical Medium-Density Fiberboard (MDF)...
  - `Ultra-Light MDF`: A lighter, slimmer type of Medium-Density Fiberboa...
  - `Water-resistant MDF`: Unique moisture protection treatment....

**响应式**: 平板设备（≤768px）下，布局改为单列，图片在上，文字在下；移动端（≤480px）按钮宽度占满
**特效**: 按钮hover时背景色加深至#E67300
**内容摘要**: 页面中部展示6种MDF类型及其特点，包含图文混排布局，左侧为MDF材质图片，右侧为类型列表和行动号召按钮

---

### 分块 4: features
- **截图**: `mdf-kitchen-cabinets_pixel_4.jpg`
- **建议模块名**: `6-types-of-mdf`

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
- 卡片内边距: 20px

**组件** (3个):
  - image x1, 宽=50%, 高=auto, 圆角=0
    说明: 左侧展示MDF板材堆叠的图片，自然木色，无阴影
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'6 Types of MDF'，深灰色（#333333），加粗700
  - list x1, 宽=auto, 高=auto, 圆角=0
    说明: 6个列表项，每个包含MDF类型标题和简短描述，正文深灰色（#666666）

**图片占位符** (1组):
  - **product** x1
    尺寸: 50% x auto, 比例: auto
    位置: 左侧, object-fit: cover
    占位符建议: wood-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `6 Types of MDF`
- **列表项** (6个):
  - `Standard MDF`: Typical Medium-Density Fiberboard (MDF)...
  - `Ultra-Light MDF`: A lighter, slimmer type of Medium-Density Fiberboa...
  - `Water-resistant MDF`: Unique moisture protection treatment....

**响应式**: 平板设备（≤768px）下，图片与文字改为单列布局，图片在上，文字在下；移动端（≤480px）列表项间距调整为15px
**特效**: 无
**内容摘要**: 页面中部展示MDF的6种类型及其特点，左侧为MDF板材图片，右侧为类型列表，属于特色展示模块

---

### 分块 5: content-block
- **截图**: `mdf-kitchen-cabinets_pixel_5.jpg`
- **建议模块名**: `mdf-finishes-content`

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
- 卡片内边距: 0

**组件** (3个):
  - heading x2, 宽=auto, 高=auto, 圆角=0
    说明: 两个主标题，分别为'Medium-Density Fiberboard Finishes'和'MDF Kitchen Cabinet Custom & Designs'，深灰色（#222222），加粗700
  - paragraph x3, 宽=auto, 高=auto, 圆角=0
    说明: 三个段落，描述MDF饰面的特点、注意事项及厨房橱柜定制的优势
  - image x1, 宽=auto, 高=auto, 圆角=0
    说明: 右侧展示MDF饰面样品的图片，无阴影和边框

**图片占位符** (1组):
  - **product** x1
    尺寸: 50% x auto, 比例: auto
    位置: 右侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Medium-Density Fiberboard Finishes`
- **段落** (3个):
  - `Medium-density fiberboards are composed of engineered wood, which means that staining them will not ...`
  - `Nevertheless, MDF is a perfect painting basis due to its pristine, non-textured appearance. To avoid...`
  - `MDF cabinets are a fantastic choice if you want to modernize your kitchen. MDF is an adaptable, reas...`

**响应式**: 平板设备（≤768px）下，布局改为单列，图片占满宽度；移动端（≤480px）文字与图片垂直堆叠，标题字体缩小
**特效**: 无
**内容摘要**: 展示MDF饰面的特性及厨房橱柜定制的优势，包含文字说明与产品图片

---

### 分块 6: features
- **截图**: `mdf-kitchen-cabinets_pixel_6.jpg`
- **建议模块名**: `mdf-cabinet-features`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 3
- 水平间距: 20px, 垂直间距: 30px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #000000
- 标题: #222222
- 正文: #666666
- 边框: none

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 40px
- 下边距: 60px
- 元素间距: 20px
- 卡片内边距: 15px

**组件** (3个):
  - heading x6, 宽=auto, 高=auto, 圆角=0
    说明: 包含2个主标题（'Medium-Density Fiberboard Finishes'、'MDF Kitchen Cabinet Custom & Designs'）和4个小节标题（'Versatile Design'、'Customizable Storage Solutions'、'Cost Effective'、'Easy to Clean and Maintain'），深灰色（#222222），加粗700
  - paragraph x6, 宽=auto, 高=auto, 圆角=0
    说明: 6个段落，描述MDF饰面特点及橱柜定制优势，黑色（#000000），常规400
  - image x5, 宽=auto, 高=auto, 圆角=0
    说明: 5张图片，展示MDF饰面及橱柜设计，无阴影，无边框

**图片占位符** (1组):
  - **gallery** x5
    尺寸: 100% x auto, 比例: 16:9
    位置: 网格排列（1张大图+4张小图）, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `MDF Kitchen Cabinet Custom & Designs`
- **副标题**: `MDF cabinets are a fantastic choice if you want to modernize your kitchen. MDF is an adaptable, reasonably priced material that may add a contemporary, fashionable look to your kitchen. Using MDF cabinets to update your kitchen has the following benefits:`
- **段落** (7个):
  - `Medium-density fiberboards are composed of engineered wood, which means that staining them will not ...`
  - `Nevertheless, MDF is a perfect painting basis due to its pristine, non-textured appearance. To avoid...`
  - `MDF cabinets are a fantastic choice if you want to modernize your kitchen. MDF is an adaptable, reas...`

**响应式**: 平板设备（≤768px）下，网格布局改为单列，图片占满宽度；移动端（≤480px）小节标题简化为单行显示
**特效**: 图片hover时无特殊效果，保持静态展示
**内容摘要**: 展示MDF橱柜的饰面特点（不可染色但适合涂漆）及定制设计优势（多样化外观、可定制存储、成本效益、易清洁维护），通过图文结合的方式突出MDF作为厨房橱柜材料的适用性

---

### 分块 7: features
- **截图**: `mdf-kitchen-cabinets_pixel_7.jpg`
- **建议模块名**: `mdf-cabinets-features`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 2
- 水平间距: 30px, 垂直间距: 30px
- 对齐: center

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

**组件** (1个):
  - card x4, 宽=auto, 高=auto, 圆角=8px
    说明: 白色卡片，包含标题、描述文字和产品图片，展示MDF橱柜的四个优势

**图片占位符** (1组):
  - **product** x4
    尺寸: 100% x auto, 比例: 16:9
    位置: 卡片顶部, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `MDF Kitchen Cabinet Custom & Designs`
- **副标题**: `MDF cabinets are a fantastic choice if you want to modernize your kitchen. MDF is an adaptable, reasonably priced material that may add a contemporary, fashionable look to your kitchen. Using MDF cabinets to update your kitchen has the following benefits:`
- **段落** (4个):
  - `MDF cabinets offer the option to be painted, stained, or laminated to create various appearances. Yo...`
  - `To improve your kitchen's efficiency, add several storage alternatives to your MDF cabinets. Pull-ou...`
  - `MDF is a more affordable option compared to solid wood due to its cost-effectiveness. This is an exc...`
- **按钮文字**: `Get a Free Quote`
- **卡片内容** (4个):
  - `Versatile Design`: MDF cabinets offer the option to be painted, stain...
  - `Customizable Storage Solutions`: To improve your kitchen's efficiency, add several ...
  - `Cost Effective`: MDF is a more affordable option compared to solid ...

**响应式**: 平板设备（≤768px）下，卡片布局改为单列；移动端（≤480px）卡片内图片宽度调整为100%，文字间距适当缩小
**特效**: 按钮hover时背景色加深至#E67300，卡片图片hover时轻微放大
**内容摘要**: 页面中部展示MDF厨房橱柜的四大优势（多功能设计、可定制存储、成本效益、易清洁维护），每个优势以卡片形式呈现，包含标题、描述文字和对应产品图片

---

### 分块 8: content-block
- **截图**: `mdf-kitchen-cabinets_pixel_8.jpg`
- **建议模块名**: `mdf-cabinet-cost`

**布局**:
- 容器: container-1200
- 类型: block
- 列数: 1, 行数: 1
- 水平间距: 0, 垂直间距: 0
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #222222
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
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'MDF Kitchen Cabinet Cost'，深灰色（#222222），加粗700
  - paragraph x2, 宽=auto, 高=auto, 圆角=0
    说明: 两个段落，分别描述MDF橱柜的成本范围和清洁建议

**图片占位符** (1组):
  - **background** x0
    尺寸: auto x auto, 比例: auto
    位置: none, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `MDF Kitchen Cabinet Cost`
- **段落** (2个):
  - `The cost varies depending on the size of your cabinets, with prices ranging from $60 to $250 for sto...`
  - `Advice: Before cleaning your MDF cabinets, use a dry cloth to remove any dust. After dissolving a fe...`

**响应式**: 平板设备（≤768px）下，内容区域保持单列布局，文字大小调整为14px；移动端（≤480px）段落行高调整为1.5
**特效**: 无
**内容摘要**: 页面中部内容块，核心展示MDF厨房橱柜的成本信息及清洁维护建议

---

### 分块 9: gallery
- **截图**: `mdf-kitchen-cabinets_pixel_9.jpg`
- **建议模块名**: `mdf-kitchen-cabinet-ideas-gallery`

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
- 上边距: 60px
- 下边距: 60px
- 元素间距: 30px
- 卡片内边距: 0

**组件** (1个):
  - image x3, 宽=33.33%, 高=auto, 圆角=0
    说明: 三个厨房橱柜图片，横向排列，展示不同风格的MDF橱柜设计

**图片占位符** (1组):
  - **gallery** x3
    尺寸: 33.33% x auto, 比例: auto
    位置: 横向网格排列, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `MDF Kitchen Cabinet Ideas`
- **副标题**: `Do you think painted kitchen cabinets with a smooth finish are a great idea? These MDF cabinet ideas can be used in eclectic, farmhouse, or glitzy kitchen decor.`

**响应式**: 平板设备（≤768px）下，图片改为2列布局；移动端（≤480px）改为1列，图片占满宽度
**特效**: 无
**内容摘要**: 展示MDF厨房橱柜的设计想法，包含三个不同风格的橱柜图片，用于启发用户选择

---

### 分块 10: why-choose
- **截图**: `mdf-kitchen-cabinets_pixel_10.jpg`
- **建议模块名**: `kitchen-cabinets-why-choose`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 3
- 水平间距: 30px, 垂直间距: 40px
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
- 元素间距: 20px
- 卡片内边距: 0

**组件** (3个):
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'The George Group One-stop Kitchen Cabinets Solution: Why Choose It?'，深灰色（#333333），加粗600
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 橙色背景（#FF8C00），白色文字，'Consult'
  - card x6, 宽=auto, 高=auto, 圆角=0
    说明: 白色卡片，包含图片和文字，分为两列三行排列

**图片占位符** (1组):
  - **service-image** x6
    尺寸: auto x auto, 比例: auto
    位置: 卡片左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `The George Group One-stop Kitchen Cabinets Solution: Why Choose It?`
- **按钮文字**: `Consult`
- **卡片内容** (6个):
  - `All-in-one Service`: Showroom spanning an area of 20,000 square meters....
  - `Save Your Money`: Through buying directly from our factory. Cut out ...
  - `Expert Group`: Over 200 experienced sales team members customize ...

**响应式**: 平板设备（≤768px）下，卡片改为单列布局，每行1个；移动端（≤480px）按钮文字简化为'咨询'
**特效**: 按钮hover时背景色加深至#E67300，卡片hover时轻微阴影效果
**内容摘要**: 页面中部why-choose模块，核心展示选择The George Group厨房橱柜解决方案的六大优势，包含标题、咨询按钮及6个图文卡片

---

### 分块 11: content-block
- **截图**: `mdf-kitchen-cabinets_pixel_11.jpg`
- **建议模块名**: `custom-kitchen-cabinets-ideas`

**布局**:
- 容器: container-1200
- 类型: block
- 列数: 1, 行数: 1
- 水平间距: 0, 垂直间距: 30px
- 对齐: left

**颜色**:
- 背景: #ffffff
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
- 卡片内边距: 0

**组件** (4个):
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'Custom Kitchen Cabinets Ideas'，深灰色（#222222），加粗700
  - paragraph x2, 宽=auto, 高=auto, 圆角=0
    说明: 两个段落，描述George厨房橱柜定制服务的范围及定制依据
  - list x2, 宽=auto, 高=auto, 圆角=0
    说明: 两个列表项，分别展示电气 appliances 和功能配件的具体内容
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 橙色背景（#FF8C00），白色文字，'Consult'

**图片占位符** (1组):
  - **none** x0
    尺寸: 0 x 0, 比例: auto
    位置: none, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Custom Kitchen Cabinets Ideas`
- **段落** (2个):
  - `George kitchen cabinet customization service involves customizing the entire kitchen, including a co...`
  - `-Electrical Appliances: Stoves, range hoods, electric ovens, garbage disposals, dishwashers, disinfe...`
- **按钮文字**: `Consult`
- **列表项** (2个):
  - `-Electrical Appliances:`: Stoves, range hoods, electric ovens, garbage dispo...
  - `-Functional Accessories:`: Hinges, slides, spotlights, skirtings, sinks, pull...

**响应式**: 平板设备（≤768px）下，列表项改为单列布局；移动端（≤480px）按钮文字简化为'咨询'
**特效**: 按钮hover时背景色加深至#E67300
**内容摘要**: 页面中部展示定制厨房橱柜的想法与服务内容，包含定制范围说明、电气 appliances 和功能配件列表，以及行动号召按钮

---

### 分块 12: gallery
- **截图**: `mdf-kitchen-cabinets_pixel_12.jpg`
- **建议模块名**: `mdf-kitchen-cabinets-gallery`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 2
- 水平间距: 20px, 垂直间距: 20px
- 对齐: center

**颜色**:
- 背景: #F5F1E8
- 主色: #FF8C00
- 标题: #8B4513
- 正文: #333333
- 边框: none

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 40px
- 下边距: 40px
- 元素间距: 20px
- 卡片内边距: 0

**组件** (1个):
  - image x8, 宽=auto, 高=auto, 圆角=0
    说明: 8张MDF厨房橱柜设计灵感图片，展示不同风格厨房橱柜布局

**图片占位符** (1组):
  - **gallery** x8
    尺寸: 25% x auto, 比例: auto
    位置: 网格排列（2行4列）, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `MORE DESIGN INSPIRATIONS FOR MDF KITCHEN CABINETS`

**响应式**: 平板设备（≤768px）下调整为2列布局，移动端（≤480px）调整为1列布局，图片宽度占满容器
**特效**: 无
**内容摘要**: 展示MDF厨房橱柜的设计灵感，通过8张不同风格的厨房橱柜图片呈现多种设计方向

---

### 分块 13: gallery
- **截图**: `mdf-kitchen-cabinets_pixel_13.jpg`
- **建议模块名**: `mdf-kitchen-cabinets-gallery`

**布局**:
- 容器: full-width
- 类型: grid
- 列数: 4, 行数: 2
- 水平间距: 20px, 垂直间距: 20px
- 对齐: center

**颜色**:
- 背景: #f5f5f5
- 主色: #D2691E
- 标题: #D2691E
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
- 卡片内边距: 0

**组件** (1个):
  - image x8, 宽=25%, 高=auto, 圆角=0
    说明: 展示MDF厨房橱柜设计灵感的图片，包含现代、简约、轻奢等风格，无文字叠加

**图片占位符** (1组):
  - **gallery** x8
    尺寸: 25% x auto, 比例: auto
    位置: 网格排列（4列2行）, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `MORE DESIGN INSPIRATIONS FOR MDF KITCHEN CABINETS`

**响应式**: 平板设备（≤768px）下网格布局改为2列，移动端（≤480px）改为1列，图片宽度调整为100%
**特效**: 无
**内容摘要**: 该区域主要展示MDF厨房橱柜的设计灵感图片，通过多风格案例为用户提供视觉参考

---

### 分块 14: contact-form
- **截图**: `mdf-kitchen-cabinets_pixel_14.jpg`
- **建议模块名**: `contact-form-section`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 40px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #4a5568
- 标题: #2d3748
- 正文: #4a5568
- 边框: #e2e8f0

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 80px
- 元素间距: 20px
- 卡片内边距: 0

**组件** (2个):
  - image x1, 宽=400px, 高=auto, 圆角=0
    说明: 左侧展示团队合影图片，包含黄色舞狮装饰，背景为现代室内场景
  - form x1, 宽=auto, 高=auto, 圆角=8px
    说明: 右侧表单区域，包含Name、Email、Tel/Whatsapp、City、Country-Select输入框，Product Needed复选框，Message文本框，Choose File按钮和Send按钮

**图片占位符** (2组):
  - **team-avatar** x1
    尺寸: 400px x auto, 比例: auto
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg
  - **gallery** x3
    尺寸: auto x auto, 比例: auto
    位置: 底部网格排列, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Get A Free Quote`
- **副标题**: `Kindly send us your project details and floor plan. We will quote for you within 8 hours!`
- **按钮文字**: `Send`
- **列表项** (1个):
  - `Product Needed*`: Kitchen cabinet, Bedroom, Bathroom, Interior Door,...
- **卡片内容** (3个):
  - `Kitchen Scullery Designs`: ...
  - `MUDROOM STORAGE IDEAS 2026`: ...
  - `Butler's Pantry Ideas`: ...

**响应式**: 平板设备（≤768px）下，表单改为单列布局，左侧图片移至表单上方；移动端（≤480px）输入框占满宽度，复选框单列排列
**特效**: Send按钮hover时背景色加深至#2d3748，输入框focus时边框颜色变为#4a5568
**内容摘要**: 页面中部联系表单区域，核心展示获取免费报价的表单，包含用户信息输入、产品需求选择及文件上传功能，底部附带相关设计案例图片

---

### 分块 15: content-grid
- **截图**: `mdf-kitchen-cabinets_pixel_15.jpg`
- **建议模块名**: `design-ideas-grid`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 3, 行数: 1
- 水平间距: 30px, 垂直间距: 30px
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
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - card x3, 宽=33.33%, 高=auto, 圆角=8px
    说明: 白色卡片，包含顶部图片和下方文字内容，展示设计案例

**图片占位符** (1组):
  - **thumbnail** x3
    尺寸: 100% x auto, 比例: 16:9
    位置: 网格排列, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Design Ideas Grid`
- **段落** (6个):
  - `Scullery: The Smart Back-Kitchen Upgrade For Modern Homes`
  - `Sculleries aren’t just Victorian leftovers or something you only see in period dramas. In 2026 homes...`
  - `Mudroom Storage Ideas That Actually Work for Busy Families`
- **卡片内容** (3个):
  - `Kitchen Scullery Designs`: Scullery: The Smart Back-Kitchen Upgrade For Moder...
  - `Mudroom Storage Ideas 2026`: Mudroom Storage Ideas That Actually Work for Busy ...
  - `Butler’s Pantry Ideas`: Butler’s Pantry Ideas That Truly Work - Make Life ...

**响应式**: 平板设备（≤768px）下，网格布局改为2列；移动端（≤480px）改为单列，图片占满宽度
**特效**: 无
**内容摘要**: 页面中部展示三个设计案例，包括厨房备餐区、泥房储物和管家 pantry 的设计想法，每个案例包含图片和文字描述

---

### 分块 16: project-cases
- **截图**: `mdf-kitchen-cabinets_pixel_16.jpg`
- **建议模块名**: `home-design-ideas-grid`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 3, 行数: 1
- 水平间距: 30px, 垂直间距: 30px
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #6c757d
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

**组件** (1个):
  - card x3, 宽=auto, 高=auto, 圆角=0
    说明: 白色背景卡片，包含图片、标题和描述文本，无阴影和边框

**图片占位符** (1组):
  - **thumbnail** x3
    尺寸: 100% x auto, 比例: 16:9
    位置: 卡片顶部, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **段落** (3个):
  - `Scullery: The Smart Back-Kitchen Upgrade For Modern Homes
Sculleries aren't just Victorian leftovers...`
  - `Mudroom Storage Ideas That Actually Work for Busy Families
Most mornings don't start neatly. Someone...`
  - `Butler's Pantry Ideas That Truly Work - Make Life Easier
Most homes don't lack space. They lack func...`
- **卡片内容** (3个):
  - `Kitchen Scullery Designs`: Scullery: The Smart Back-Kitchen Upgrade For Moder...
  - `Mudroom Storage Ideas 2026`: Mudroom Storage Ideas That Actually Work for Busy ...
  - `Butler's Pantry Ideas`: Butler's Pantry Ideas That Truly Work - Make Life ...

**响应式**: 平板设备（≤768px）下，网格布局改为2列；移动端（≤480px）下改为单列布局，图片宽度占满
**特效**: 无 hover 或动画效果，静态展示
**内容摘要**: 页面中部展示三个家庭设计相关的案例卡片，分别聚焦厨房备餐区、储物间和备餐间的设计想法，每个卡片包含图片、标题和简短描述

---

### 分块 17: footer
- **截图**: `mdf-kitchen-cabinets_pixel_17.jpg`
- **建议模块名**: `footer-common`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 40px, 垂直间距: 20px
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
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 15px
- 卡片内边距: 0

**组件** (4个):
  - list x6, 宽=auto, 高=auto, 圆角=0
    说明: Products列下的6个列表项，包括Kitchen Cabinet、Wardrobe等，白色文字，无装饰
  - list x5, 宽=auto, 高=auto, 圆角=0
    说明: One-Stop Solutions列下的5个列表项，包括Hotel Solutions、Resort Solutions等，白色文字，无装饰
  - list x6, 宽=auto, 高=auto, 圆角=0
    说明: Customer Services列下的6个列表项，包括Measurement Guidance、Packaging Info等，白色文字，无装饰
  - form x1, 宽=auto, 高=auto, 圆角=4px
    说明: Contact Us列下的表单，包含whatsapp输入框、Email输入框（带*）和Send按钮，灰色背景（#666666）

**图片占位符** (1组):
  - **none** x0
    尺寸: auto x auto, 比例: auto
    位置: none, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Products`
- **段落** (23个):
  - `Kitchen Cabinet`
  - `Wardrobe`
  - `Windows and Doors`
- **按钮文字**: `Send`
- **列表项** (18个):
  - `Kitchen Cabinet`: ...
  - `Wardrobe`: ...
  - `Windows and Doors`: ...

**响应式**: 平板设备（≤768px）下，footer列布局改为2列；移动端（≤480px）下改为单列，表单元素占满宽度
**特效**: Send按钮hover时背景色加深至#555555
**内容摘要**: 页面底部footer区域，包含Products、One-Stop Solutions、Customer Services、Contact Us四个功能模块，展示产品类别、解决方案类型、客户服务内容及联系信息

---


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
    --color-border: #e2e8f0;
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
    --spacing-module-top: 60px;
    --spacing-module-bottom: 60px;
    --spacing-element: 15px;
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
- `mdf-kitchen-cabinets_pixel_1.jpg`
- `mdf-kitchen-cabinets_pixel_10.jpg`
- `mdf-kitchen-cabinets_pixel_11.jpg`
- `mdf-kitchen-cabinets_pixel_12.jpg`
- `mdf-kitchen-cabinets_pixel_13.jpg`
- `mdf-kitchen-cabinets_pixel_14.jpg`
- `mdf-kitchen-cabinets_pixel_15.jpg`
- `mdf-kitchen-cabinets_pixel_16.jpg`
- `mdf-kitchen-cabinets_pixel_17.jpg`
- `mdf-kitchen-cabinets_pixel_2.jpg`
- `mdf-kitchen-cabinets_pixel_3.jpg`
- `mdf-kitchen-cabinets_pixel_4.jpg`
- `mdf-kitchen-cabinets_pixel_5.jpg`
- `mdf-kitchen-cabinets_pixel_6.jpg`
- `mdf-kitchen-cabinets_pixel_7.jpg`
- `mdf-kitchen-cabinets_pixel_8.jpg`
- `mdf-kitchen-cabinets_pixel_9.jpg`

---

## 🎯 推荐输出方式：WordPress 页面模板

### 页面模板文件
**位置**: `wp-content/themes/{theme-name}/page-templates/template-{page-name}.php`

```php
<?php
/**
 * Template Name: {Page Name} 页面模板
 * Description: 克隆自 https://georgeconstructions.com/mdf-kitchen-cabinets/
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
