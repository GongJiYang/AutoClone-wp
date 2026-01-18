# WordPress 页面克隆任务

## ⚠️ 核心要求（必须满足）

1. **默认数据必须从截图提取真实内容** - 不可为空或使用占位符
2. **每个模块独立PHP文件** - `modules/{module-name}.php`
3. **完整的响应式CSS** - 4个断点（桌面/平板/移动/小屏）
4. **图片占位符使用placehold.co** - `https://placehold.co/600x400/e0e0e0/666?text=Product`

---

## 原始页面信息
- URL: https://georgeconstructions.com/white-kitchen-cabinets/
- 标题: White Kitchen Cabinets – Custom Solutions For Your Home
- 总高度: 8437px

---

## 页面结构分析

### 分块 1: hero
- **截图**: `white-kitchen-cabinets_pixel_1.jpg`
- **建议模块名**: `kitchen-cabinets-hero`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 1, 行数: 1
- 水平间距: 0, 垂直间距: 0
- 对齐: center

**颜色**:
- 背景: #f8f8f8
- 主色: #FF8C00
- 标题: #ffffff
- 正文: #ffffff
- 边框: none

**字体**:
- 标题: 48px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 0

**组件** (4个):
  - navbar x1, 宽=100%, 高=auto, 圆角=0
    说明: 白色背景导航栏，包含logo、7个菜单项（Products/Projects/Blog/Service/Video/About/Contact）和1个橙色按钮（Quick Quote）
  - heading x2, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'Custom White Kitchen Cabinets For Your Projects'（白色，48px，700），副标题'White Kitchen Cabinets: Timeless Designs for Modern Homes'（白色，24px，600）
  - paragraph x1, 宽=auto, 高=auto, 圆角=0
    说明: 白色文字段落，描述乙烯基地板定义
  - button x2, 宽=auto, 高=40px, 圆角=4px
    说明: 橙色背景（#FF8C00），白色文字，分别为'Quick Quote'和'Download Catalogues'

**图片占位符** (1组):
  - **hero-banner** x1
    尺寸: 100% x auto, 比例: auto
    位置: 背景, object-fit: cover
    遮罩: rgba(0,0,0,0.1)
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Custom White Kitchen Cabinets For Your Projects`
- **副标题**: `White Kitchen Cabinets: Timeless Designs for Modern Homes`
- **段落** (1个):
  - `Vinyl flooring refers to luxury vinyl tiles (LVT) as well as vinyl roll flooring, sometimes known as...`
- **按钮文字**: `Quick Quote`, `Download Catalogues`

**响应式**: 平板设备（≤768px）下，导航栏菜单项折叠为汉堡菜单，hero区域标题居中显示；移动端（≤480px）主标题字体缩小至36px，按钮文字简化为'Quote'和'Download'
**特效**: 按钮hover时背景色加深至#E67300，背景图有轻微模糊效果
**内容摘要**: 页面顶部hero区域，展示白色厨房橱柜主题，包含导航栏、主视觉背景图、核心标题、项目描述及行动号召按钮

---

### 分块 2: product-grid
- **截图**: `white-kitchen-cabinets_pixel_2.jpg`
- **建议模块名**: `kitchen-cabinets-grid`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 3, 行数: 2
- 水平间距: 20px, 垂直间距: 30px
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #222222
- 正文: #666666
- 边框: none

**字体**:
- 标题: 18px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.5

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 0
- 卡片内边距: 15px

**组件** (1个):
  - card x6, 宽=auto, 高=auto, 圆角=8px
    说明: 白色背景卡片，包含厨房橱柜图片和标题，图片居上，标题居下

**图片占位符** (1组):
  - **product** x6
    尺寸: 100% x 200px, 比例: 16:9
    位置: 网格排列（2行3列）, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **卡片内容** (6个):
  - `white kitchen cabinets`: ...
  - `white oak kitchen cabinets`: ...
  - `black and white kitchen cabinets`: ...

**响应式**: 平板设备（≤768px）下，网格改为2列；移动端（≤480px）下，网格改为1列，卡片宽度占满
**特效**: 卡片hover时可能显示阴影或轻微缩放效果
**内容摘要**: 页面中部展示6种不同风格的白色厨房橱柜产品，以2行3列的网格布局呈现，每个卡片包含产品图片和标题

---

### 分块 3: features
- **截图**: `white-kitchen-cabinets_pixel_3.jpg`
- **建议模块名**: `kitchen-cabinet-finish-upgrades`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 20px, 垂直间距: 30px
- 对齐: center

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
- 上边距: 60px
- 下边距: 60px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - card x4, 宽=auto, 高=auto, 圆角=8px
    说明: 白色背景卡片，包含标题和描述文本，展示不同的橱柜翻新选项

**图片占位符** (1组):
  - **none** x0
    尺寸: auto x auto, 比例: auto
    位置: 网格排列, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `White Kitchen Cabinet Makeover: 4 Durable Finish Upgrades`
- **卡片内容** (4个):
  - `Smooth Flat And Dimpled Finishing`: For your modern white kitchen...
  - `Glaze Finishing`: This custom option has a semi-transparent finish t...
  - `Woodgrain Finishing`: This finish transforms your space into a cozy have...

**响应式**: 平板设备（≤768px）下，网格布局改为2列；移动端（≤480px）改为单列，卡片宽度占满
**特效**: 卡片hover时可能显示边框或阴影效果
**内容摘要**: 页面中部展示橱柜翻新的4种耐用饰面升级选项，以网格形式排列，每个选项包含标题和简短描述

---

### 分块 4: features
- **截图**: `white-kitchen-cabinets_pixel_4.jpg`
- **建议模块名**: `kitchen-cabinet-finishes`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 30px, 垂直间距: 30px
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
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (2个):
  - card x4, 宽=auto, 高=auto, 圆角=8px
    说明: 白色背景卡片，包含标题、描述文字和'Custom Now'按钮，无阴影和边框
  - button x4, 宽=auto, 高=40px, 圆角=6px
    说明: 深蓝色背景（#2d3748），白色文字，'Custom Now'按钮，圆角6px

**图片占位符** (1组):
  - **thumbnail** x0
    尺寸: auto x auto, 比例: auto
    位置: 无图片，仅文字卡片, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `White Kitchen Cabinet Makeover: 4 Durable Finish Upgrades`
- **段落** (4个):
  - `For your modern white kitchen cabinets, you can get styles that are smooth, flat, or rippled. Smooth...`
  - `This custom option has a semi-transparent finish that brings out the texture of the cabinets, giving...`
  - `This finish transforms your space into a cozy haven, perfect for those who want a combination of mod...`
- **按钮文字**: `Custom Now`, `Custom Now`, `Custom Now`, `Custom Now`
- **卡片内容** (4个):
  - `Smooth Flat And Dimpled Finishing`: For your modern white kitchen cabinets, you can ge...
  - `Glaze Finishing`: This custom option has a semi-transparent finish t...
  - `Woodgrain Finishing`: This finish transforms your space into a cozy have...

**响应式**: 平板设备（≤768px）下改为2列布局，移动端（≤480px）改为1列布局，按钮文字保持不变
**特效**: 按钮hover时背景色加深，卡片hover时轻微阴影效果
**内容摘要**: 页面中部展示白色厨房橱柜的4种耐用表面处理升级选项，包含标题、4个特色卡片（每个卡片有标题、描述和行动按钮）

---

### 分块 5: features
- **截图**: `white-kitchen-cabinets_pixel_5.jpg`
- **建议模块名**: `kitchen-cabinet-designs`

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
- 标题: 36px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 20px
- 卡片内边距: 25px

**组件** (2个):
  - card x4, 宽=auto, 高=auto, 圆角=8px
    说明: 白色背景卡片，包含设计类型标题、描述文字及深色按钮，无阴影和边框
  - button x4, 宽=auto, 高=40px, 圆角=6px
    说明: 深灰色背景（#2D3748），白色文字，统一尺寸的'Custom Now'按钮

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Best White Kitchen Cabinet Designs for Any Space`
- **按钮文字**: `Custom Now`, `Custom Now`, `Custom Now`, `Custom Now`
- **卡片内容** (4个):
  - `U-shaped`: A custom U-shaped design with white kitchen cabine...
  - `I-shaped`: Make your kitchen functional and well-organized wi...
  - `L-shaped`: The L-shaped design makes good use of the corners ...

**响应式**: 平板设备（≤768px）下，布局改为2列；移动端（≤480px）下，布局改为1列，按钮文字保持不变
**特效**: 按钮hover时背景色加深至#1A202C，文字保持白色
**内容摘要**: 页面中部展示四种白色厨房橱柜设计类型（U-shaped、I-shaped、L-shaped、Island），每个设计包含功能描述及定制按钮，帮助用户选择适合的厨房布局

---

### 分块 6: features
- **截图**: `white-kitchen-cabinets_pixel_6.jpg`
- **建议模块名**: `white-cabinet-must-haves`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 20px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #2d3748
- 标题: #2d3748
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
    说明: 浅灰色背景卡片，包含标题、描述文字和按钮，每个卡片独立展示一个橱柜配件
  - button x4, 宽=auto, 高=40px, 圆角=4px
    说明: 深灰色背景（#2d3748），白色文字，每个卡片底部有'Custom Now'按钮

**图片占位符** (1组):
  - **thumbnail** x0
    尺寸: auto x auto, 比例: auto
    位置: 无, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Pull-Out Trays & More: White Cabinet Must-Haves`
- **段落** (4个):
  - `Stainless steel, porcelain, and composite are all long-lasting and attractive choices. We have a wid...`
  - `Chrome, oil-rubbed bronze, and matte black are among the available finishes. You can choose between ...`
  - `George Constructions offers a variety of designs to choose from, including modern handles, classic k...`
- **按钮文字**: `Custom Now`, `Custom Now`, `Custom Now`, `Custom Now`
- **卡片内容** (4个):
  - `Sink`: Stainless steel, porcelain, and composite are all ...
  - `Hinge`: Chrome, oil-rubbed bronze, and matte black are amo...
  - `Handle`: George Constructions offers a variety of designs t...

**响应式**: 平板设备（≤768px）下，卡片布局改为2列；移动端（≤480px）下改为1列，按钮文字保持不变
**特效**: 按钮hover时背景色加深至#1a202c
**内容摘要**: 页面中部展示白色橱柜必备配件（水槽、铰链、把手、抽屉）的详细信息，每个配件包含材质、设计选择及功能描述，并提供定制选项按钮

---

### 分块 7: why-choose
- **截图**: `white-kitchen-cabinets_pixel_7.jpg`
- **建议模块名**: `why-choose-white-kitchen-cabinets`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 30px, 垂直间距: 30px
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

**组件** (2个):
  - card x4, 宽=auto, 高=auto, 圆角=8px, 有阴影
    说明: 白色卡片，带轻微阴影，每个卡片包含黑色图标、标题和描述文字
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 橙色背景（#FF8C00），白色文字，'Get a free quote →'

**图片占位符** (1组):
  - **icon** x4
    尺寸: auto x auto, 比例: 1:1
    位置: 卡片顶部居中, object-fit: contain
    占位符建议: black-icon

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Why Choose Us for White Kitchen Cabinets?`
- **按钮文字**: `Get a free quote →`
- **卡片内容** (4个):
  - `Homeowners (Remodel Or Upgrade)`: George Constructions helps homeowners a lot by off...
  - `Builders (High-Quality For Projects)`: By focusing on long-lasting craftsmanship and stre...
  - `Contractors (Trusted By Clients)`: We help contractors by giving them premium white k...

**响应式**: 平板设备（≤768px）下，卡片改为2列布局；移动端（≤480px）改为单列布局，按钮文字简化为'Quote'
**特效**: 按钮hover时背景色加深至#E67300，卡片hover时阴影增强
**内容摘要**: 页面中部展示“为什么选择我们”模块，针对不同客户群体（房主、建筑商、承包商、建筑师）介绍服务优势，包含四个卡片和底部行动号召按钮

---

### 分块 8: content-block
- **截图**: `white-kitchen-cabinets_pixel_8.jpg`
- **建议模块名**: `showroom-inspiration`

**布局**:
- 容器: container-1200
- 类型: block
- 列数: 1, 行数: 1
- 水平间距: 0, 垂直间距: 30px
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #2d3748
- 正文: #4a5568
- 边框: none

**字体**:
- 标题: 28px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 80px
- 元素间距: 20px
- 卡片内边距: 0

**组件** (4个):
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'Visit Our Showroom for White Cabinet Inspiration'，深灰色（#2d3748），加粗700
  - paragraph x1, 宽=auto, 高=auto, 圆角=0
    说明: 描述展厅面积和展示内容的段落，文字颜色#4a5568
  - list x1, 宽=auto, 高=auto, 圆角=0
    说明: 包含5个带勾的列表项，列表项文字颜色#4a5568，勾图标为黑色
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 橙色背景（#FF8C00），白色文字，'Book time to visit →'

**图片占位符** (1组):
  - **icon** x5
    尺寸: 16px x 16px, 比例: 1:1
    位置: 列表项左侧, object-fit: contain
    占位符建议: checkmark-icon

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Visit Our Showroom for White Cabinet Inspiration`
- **段落** (1个):
  - `George Constructions has a 20,000-square-foot showroom where customers can see many different home d...`
- **按钮文字**: `Book time to visit →`
- **列表项** (5个):
  - `Kitchen Cabinets & Wardrobes`: ...
  - `Windows & Doors`: ...
  - `Bathrooms & Tiles`: ...

**响应式**: 移动端设备下，列表项垂直堆叠，按钮宽度调整为100%，主标题字体大小调整为24px
**特效**: 按钮hover时背景色加深至#e67300，列表项勾图标hover时颜色变深
**内容摘要**: 展示George Constructions展厅信息，包括展厅面积、展示内容范围，以及预约参观的行动号召

---

### 分块 9: faq
- **截图**: `white-kitchen-cabinets_pixel_9.jpg`
- **建议模块名**: `white-kitchen-cabinets-faq`

**布局**:
- 容器: container-1200
- 类型: block
- 列数: 1, 行数: 1
- 水平间距: 0, 垂直间距: 40px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #222222
- 正文: #666666
- 边框: #e0e0e0

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 20px
- 卡片内边距: 15px

**组件** (4个):
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'FAQs About White Kitchen Cabinets'，深灰色（#222222），加粗700
  - accordion x3, 宽=100%, 高=auto, 圆角=0
    说明: 三个可折叠FAQ问题，每个问题带加号图标，点击展开内容，边框为浅灰色（#e0e0e0）
  - form x1, 宽=100%, 高=auto, 圆角=8px, 有阴影
    说明: 联系表单，包含Name、Email、Tel/Whatsapp、City、Country-Select输入框，Product Needed复选框，Message文本域
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 橙色背景（#FF8C00），白色文字，'Book time to visit →'

**图片占位符** (1组):
  - **background** x1
    尺寸: 50% x auto, 比例: auto
    位置: 左侧, object-fit: cover
    占位符建议: team-photo

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `FAQs About White Kitchen Cabinets`
- **段落** (1个):
  - `Kindly send us your project details and floor plan. We will quote for you within 8 hours!`
- **按钮文字**: `Book time to visit →`
- **卡片内容** (3个):
  - `What goes best with white kitchen cabinets?`: ...
  - `What are the best colors to paint white kitchen cabinets?`: ...
  - `Should I Install White Kitchen Cabinets?`: ...

**响应式**: 平板设备（≤768px）下，表单输入框改为单列布局；移动端（≤480px）FAQ问题图标和文字左对齐
**特效**: FAQ问题点击时展开/收起内容，表单输入框 hover 时边框变色
**内容摘要**: 页面中部FAQ模块，展示关于白色厨房橱柜的常见问题及联系表单，包含可折叠问题列表和项目咨询表单

---

### 分块 10: faq
- **截图**: `white-kitchen-cabinets_pixel_10.jpg`
- **建议模块名**: `white-kitchen-cabinets-faq`

**布局**:
- 容器: container-1200
- 类型: block
- 列数: 1, 行数: 2
- 水平间距: 0, 垂直间距: 40px
- 对齐: left

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
- 上边距: 60px
- 下边距: 60px
- 元素间距: 20px
- 卡片内边距: 0

**组件** (5个):
  - accordion x3, 宽=auto, 高=auto, 圆角=0
    说明: 三个可展开的FAQ问题，每个问题前有加号图标，文字为深灰色（#333333），未展开时显示问题标题
  - input x5, 宽=100%, 高=40px, 圆角=4px
    说明: 五个文本输入框（Name、Email、Tel/Whatsapp、City、Country-Select），边框为浅灰色（#e0e0e0），占满容器宽度
  - checkbox x8, 宽=auto, 高=auto, 圆角=0
    说明: 八个复选框（Kitchen cabinet、Bedroom、Windows & Doors、Sanitary Ware、Furniture、Lighting、Soft Furnishing、Tiles and Wood Flooring、Whole House Solution、Other Building Material），文字为灰色（#666666）
  - textarea x1, 宽=100%, 高=120px, 圆角=4px
    说明: 一个消息输入框（Message），边框为浅灰色（#e0e0e0），占满容器宽度
  - button x1, 宽=100%, 高=40px, 圆角=4px
    说明: 灰色背景（#666666）的发送按钮，白色文字，文字为'Send'

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `FAQs About White Kitchen Cabinets`
- **段落** (1个):
  - `Kindly send us your project details and floor plan. We will quote for you within 8 hours!`
- **按钮文字**: `Send`
- **列表项** (3个):
  - `What goes best with white kitchen cabinets?`: ...
  - `What are the best colors to paint white kitchen cabinets?`: ...
  - `Should I Install White Kitchen Cabinets?`: ...

**响应式**: 平板设备（≤768px）下，输入框和复选框改为单列布局；移动端（≤480px）复选框文字缩小至14px
**特效**: FAQ问题hover时加号图标变为橙色（#FF8C00），表单输入框focus时边框变为橙色（#FF8C00）
**内容摘要**: 页面中部FAQ模块，展示白色厨房橱柜的常见问题及获取报价表单，包含可展开的FAQ问题和项目需求表单

---

### 分块 11: contact-form
- **截图**: `white-kitchen-cabinets_pixel_11.jpg`
- **建议模块名**: `free-quote-form`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #6c757d
- 标题: #333333
- 正文: #000000
- 边框: #e0e0e0

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 50px
- 下边距: 50px
- 元素间距: 20px
- 卡片内边距: 15px

**组件** (6个):
  - form x1, 宽=auto, 高=auto, 圆角=8px
    说明: 包含Name、Email、Tel/Whatsapp、City、Country-Select输入框，Product Needed复选框（10个选项），Message文本框，Choose File按钮，Send按钮的表单，背景为浅灰色（#f8f8f8），边框为浅灰色（#e0e0e0）
  - input x5, 宽=100%, 高=40px, 圆角=4px
    说明: 文本输入框，包括Name、Email、Tel/Whatsapp、City、Country-Select，边框为浅灰色（#e0e0e0）
  - checkbox x10, 宽=auto, 高=auto, 圆角=0
    说明: Product Needed复选框，选项包括Kitchen cabinet、Bedroom、Windows & Doors、Sanitary Ware、Furniture、Lighting、Soft Furnishing、Tiles and Wood Flooring、Whole House Solution、Other Building Material
  - textarea x1, 宽=100%, 高=120px, 圆角=4px
    说明: Message文本框，边框为浅灰色（#e0e0e0）
  - file-input x1, 宽=auto, 高=auto, 圆角=0
    说明: Choose File按钮，显示文件选择界面
  - button x1, 宽=100%, 高=40px, 圆角=4px
    说明: Send按钮，背景为灰色（#6c757d），白色文字

**图片占位符** (1组):
  - **team** x1
    尺寸: 50% x auto, 比例: auto
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Get A Free Quote`
- **段落** (1个):
  - `Kindly send us your project details and floor plan. We will quote for you within 8 hours!`
- **按钮文字**: `Send`
- **列表项** (10个):
  - `Kitchen cabinet`: ...
  - `Bedroom`: ...
  - `Windows & Doors`: ...

**响应式**: 平板设备（≤768px）下，表单与图片改为单列布局，图片占满宽度；移动端（≤480px）下，表单元素垂直堆叠，输入框宽度占满容器
**特效**: Send按钮hover时背景色加深至#5a6268
**内容摘要**: 页面中部联系表单区域，用于收集用户项目信息以获取免费报价，包含个人信息输入、产品需求选择、详细描述及文件上传功能

---

### 分块 12: footer
- **截图**: `white-kitchen-cabinets_pixel_12.jpg`
- **建议模块名**: `footer-sections`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 4, 行数: 1
- 水平间距: 40px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: #000000
- 主色: #6c757d
- 标题: #ffffff
- 正文: #cccccc
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

**组件** (5个):
  - card x4, 宽=auto, 高=auto, 圆角=0
    说明: 四个等宽分栏，每个分栏包含标题和列表项
  - list x7, 宽=auto, 高=auto, 圆角=0
    说明: Products分栏下的7个列表项（Kitchen Cabinet至Whole-house Design）
  - list x5, 宽=auto, 高=auto, 圆角=0
    说明: One-Stop Solutions分栏下的5个列表项（Hotel Solutions至Office Solutions）
  - list x7, 宽=auto, 高=auto, 圆角=0, 有阴影
    说明: Customer Services分栏下的7个列表项（CUSTOMER SERVICES至FAQ）
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: Contact Us分栏下的灰色（#6c757d）'Send'按钮

**图片占位符** (1组):
  - **none** x0
    尺寸: auto x auto, 比例: auto
    位置: none, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **按钮文字**: `Send`
- **列表项** (27个):
  - `Products`: ...
  - `One-Stop Solutions`: ...
  - `Customer Services`: ...

**响应式**: 平板设备（≤768px）下，footer分栏改为2列布局；移动端（≤480px）改为单列布局，列表项垂直排列
**特效**: 按钮hover时背景色加深至#5a6268
**内容摘要**: 页面底部footer区域，包含四个分栏：Products（产品分类）、One-Stop Solutions（一站式解决方案）、Customer Services（客户服务）、Contact Us（联系我们），展示公司产品、服务及联系方式

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
    --color-text: #cccccc;
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
- `white-kitchen-cabinets_pixel_1.jpg`
- `white-kitchen-cabinets_pixel_10.jpg`
- `white-kitchen-cabinets_pixel_11.jpg`
- `white-kitchen-cabinets_pixel_12.jpg`
- `white-kitchen-cabinets_pixel_2.jpg`
- `white-kitchen-cabinets_pixel_3.jpg`
- `white-kitchen-cabinets_pixel_4.jpg`
- `white-kitchen-cabinets_pixel_5.jpg`
- `white-kitchen-cabinets_pixel_6.jpg`
- `white-kitchen-cabinets_pixel_7.jpg`
- `white-kitchen-cabinets_pixel_8.jpg`
- `white-kitchen-cabinets_pixel_9.jpg`

---

## 🎯 推荐输出方式：WordPress 页面模板

### 页面模板文件
**位置**: `wp-content/themes/{theme-name}/page-templates/template-{page-name}.php`

```php
<?php
/**
 * Template Name: {Page Name} 页面模板
 * Description: 克隆自 https://georgeconstructions.com/white-kitchen-cabinets/
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
