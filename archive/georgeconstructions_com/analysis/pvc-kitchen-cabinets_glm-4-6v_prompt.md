# WordPress 页面克隆任务

## ⚠️ 核心要求（必须满足）

1. **默认数据必须从截图提取真实内容** - 不可为空或使用占位符
2. **每个模块独立PHP文件** - `modules/{module-name}.php`
3. **完整的响应式CSS** - 4个断点（桌面/平板/移动/小屏）
4. **图片占位符使用placehold.co** - `https://placehold.co/600x400/e0e0e0/666?text=Product`

---

## 原始页面信息
- URL: https://georgeconstructions.com/pvc-kitchen-cabinets/
- 标题: PVC Kitchen Cabinets Design - George
- 总高度: 9141px

---

## 页面结构分析

### 分块 1: hero
- **截图**: `pvc-kitchen-cabinets_pixel_1.jpg`
- **建议模块名**: `kitchen-cabinets-hero`

**布局**:
- 容器: full-width
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0
- 对齐: space-between

**颜色**:
- 背景: 图片（厨房场景）
- 主色: #FF8C00
- 标题: #FFFFFF
- 正文: #FFFFFF
- 边框: none

**字体**:
- 标题: 48px, 字重: 700
- 正文: 20px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (4个):
  - navbar x1, 宽=auto, 高=auto, 圆角=0
    说明: 顶部导航栏，包含logo和7个导航链接（Products/Projects/Blog/Service/Video/About/Contact）及1个橙色按钮（Quick Quote）
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'PVC KITCHEN CABINETS'，白色（#FFFFFF），加粗700
  - paragraph x1, 宽=auto, 高=auto, 圆角=0
    说明: 副标题'One-Stop Building Material Solution Supplier'，白色（#FFFFFF）
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 橙色背景（#FF8C00），白色文字，'Quick Quote'

**图片占位符** (1组):
  - **hero-banner** x1
    尺寸: 100% x auto, 比例: auto
    位置: 居中, object-fit: cover
    遮罩: #00000080
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `PVC KITCHEN CABINETS`
- **副标题**: `One-Stop Building Material Solution Supplier`
- **按钮文字**: `Quick Quote`

**响应式**: 平板设备（≤768px）下，hero区域改为单列布局，图片占满宽度，文字居中；移动端（≤480px）导航栏折叠为汉堡菜单
**特效**: 按钮hover时背景色加深至#E67300，hero图片有半透明黑色叠加层突出文字
**内容摘要**: 页面顶部hero区域，展示PVC厨房橱柜的主视觉信息，包含导航栏、主标题、副标题及行动号召按钮

---

### 分块 2: product-grid
- **截图**: `pvc-kitchen-cabinets_pixel_2.jpg`
- **建议模块名**: `pvc-kitchen-cabinets-grid`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 3, 行数: 1
- 水平间距: 30px, 垂直间距: 40px
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
- 上边距: 40px
- 下边距: 40px
- 元素间距: 20px
- 卡片内边距: 20px

**组件** (1个):
  - card x3, 宽=auto, 高=auto, 圆角=8px, 有阴影
    说明: 白色背景卡片，带轻微阴影，每个卡片包含产品图片、标题和描述文本

**图片占位符** (1组):
  - **product/thumbnail** x3
    尺寸: 100% x 200px, 比例: 16:9
    位置: 网格排列, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Custom Your PVC Kitchen Cabinets from China`
- **段落** (1个):
  - `Enhance the look of your kitchen with our professional guidance on various PVC kitchen cabinets inco...`
- **按钮文字**: `Check Demos →`
- **卡片内容** (3个):
  - `White PVC Shaker Kitchen Cabinets`: Product Design The kitchen in the picture exemplif...
  - `White PVC Kitchen Cabinets`: As one of the most important parts of any home, ki...
  - `PVC Material For Modular Kitchen`: Types And Uses Of PVC In Modular Kitchen In contem...

**响应式**: 平板设备（≤768px）下，网格布局改为2列；移动端（≤480px）改为单列，卡片宽度占满容器
**特效**: 卡片hover时阴影加深，图片hover时轻微缩放
**内容摘要**: 页面中部产品网格展示区域，核心展示不同类型的PVC厨房橱柜产品，包含产品图片、标题及简要描述，提供产品分类浏览

---

### 分块 3: content-block
- **截图**: `pvc-kitchen-cabinets_pixel_3.jpg`
- **建议模块名**: `pvc-boards-details`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 1, 行数: 2
- 水平间距: 30px, 垂直间距: 50px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #222222
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
- 卡片内边距: 20px

**组件** (3个):
  - heading x2, 宽=auto, 高=auto, 圆角=0
    说明: 两个标题，分别为'PVC hollow boards'和'PVC foam boards'，深灰色（#222222），加粗700
  - paragraph x2, 宽=auto, 高=auto, 圆角=0
    说明: 两个段落，分别描述PVC空心板和泡沫板的特点
  - image x2, 宽=300px, 高=auto, 圆角=0
    说明: 两个产品图片，展示PVC空心板和泡沫板的实物样例

**图片占位符** (1组):
  - **product** x2
    尺寸: 300px x auto, 比例: 4:3
    位置: 左右交替（空心板在左，泡沫板在右）, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **段落** (2个):
  - `PVC hollow boards have an empty interior and are known for their greater flexibility. They are not o...`
  - `PVC foam boards may be pricier, yet they possess numerous favorable characteristics. Hollow boards a...`

**响应式**: 平板设备（≤768px）下，每个部分改为单列布局，图片与文字垂直堆叠；移动端（≤480px）图片宽度调整为100%，文字居中显示
**特效**: 图片hover时可能触发轻微阴影效果，增强视觉层次感
**内容摘要**: 该区域详细对比PVC空心板与泡沫板的特点，通过图文结合的方式展示两种材料在厨房橱柜中的应用差异

---

### 分块 4: features
- **截图**: `pvc-kitchen-cabinets_pixel_4.jpg`
- **建议模块名**: `kitchen-cabinets-advantages`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 3, 行数: 2
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

**组件** (1个):
  - card x6, 宽=auto, 高=auto, 圆角=8px
    说明: 白色卡片，带线条图标（齿轮/计时器/手势/铅笔/文档/星星），显示优势标题（如Durable）和描述文字

**图片占位符** (1组):
  - **icon** x6
    尺寸: 40px x 40px, 比例: 1:1
    位置: 卡片左上角, object-fit: contain
    占位符建议: line-icon

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Advantages - Raw Materials`
- **段落** (7个):
  - `George PVC offers a wide variety of color options, with a PVC film thickness of approximately 0.035m...`
  - `PVC kitchen cabinets are well-known for their superior strength, guaranteeing they can endure the de...`
  - `Choosing cabinets that can withstand spills and moisture is essential for kitchens to maintain their...`
- **按钮文字**: `Contact Us`
- **卡片内容** (6个):
  - `Durable`: PVC kitchen cabinets are well-known for their supe...
  - `Moisture Resistance`: Choosing cabinets that can withstand spills and mo...
  - `Installing It Easy`: PVC kitchen cabinet installation is an easy proces...

**响应式**: 平板设备（≤768px）下，网格布局改为2列；移动端（≤480px）改为单列，卡片垂直排列
**特效**: 按钮hover时背景色加深至#E67300，卡片hover时轻微阴影效果
**内容摘要**: 页面中部展示PVC厨房橱柜的六大核心优势（耐用性、防潮、安装便捷、价格实惠、环保、白蚁抵抗），每个优势以卡片形式呈现，包含图标、标题和详细描述

---

### 分块 5: features
- **截图**: `pvc-kitchen-cabinets_pixel_5.jpg`
- **建议模块名**: `kitchen-cabinets-features`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 3, 行数: 2
- 水平间距: 30px, 垂直间距: 30px
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
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (1个):
  - card x6, 宽=auto, 高=auto, 圆角=8px
    说明: 白色卡片，每个包含左侧线条图标、标题和描述文本，无阴影和边框

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **段落** (6个):
  - `PVC kitchen cabinets are well-known for their superior strength, guaranteeing they can endure the de...`
  - `Choosing cabinets that can withstand spills and moisture is essential for kitchens to maintain their...`
  - `PVC kitchen cabinet installation is an easy process that ensures homeowners have a smooth transition...`
- **卡片内容** (6个):
  - `Durable`: PVC kitchen cabinets are well-known for their supe...
  - `Moisture Resistance`: Choosing cabinets that can withstand spills and mo...
  - `Installing It Easy`: PVC kitchen cabinet installation is an easy proces...

**响应式**: 平板设备（≤768px）下，布局改为2列；移动端（≤480px）下，布局改为1列，卡片垂直排列
**特效**: 无
**内容摘要**: 该区域主要展示PVC厨房橱柜的六大核心优势：耐用性、防潮性、安装便捷性、经济时尚性、环保性及防白蚁特性，通过卡片式布局清晰呈现每项优势的详细说明

---

### 分块 6: image-text
- **截图**: `pvc-kitchen-cabinets_pixel_6.jpg`
- **建议模块名**: `pvc-cabinet-characteristics`

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
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (4个):
  - image x1, 宽=50%, 高=auto, 圆角=0
    说明: 左侧展示PVC厨房橱柜设计特性的图片，占布局50%宽度
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'Characteristics of a PVC kitchen cabinet design'，深灰色（#222222），加粗700
  - paragraph x1, 宽=auto, 高=auto, 圆角=0
    说明: 描述泡沫板在PVC厨房橱柜设计中的优势，包括耐热、防火、无毒等特性
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 橙色背景（#FF8C00），白色文字，'Get a Free Quote'

**图片占位符** (1组):
  - **image** x1
    尺寸: 50% x auto, 比例: auto
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Characteristics of a PVC kitchen cabinet design`
- **段落** (1个):
  - `Consider opting for foam boards when selecting PVC kitchen cupboard designs. This is because hollow ...`
- **按钮文字**: `Get a Free Quote`

**响应式**: 平板设备（≤768px）下，图文布局改为单列，图片占满宽度；移动端（≤480px）按钮文字简化为'Quote'
**特效**: 按钮hover时背景色加深至#E67300
**内容摘要**: 页面中部展示PVC厨房橱柜设计的特性，通过图文混排形式介绍泡沫板的优势，包含行动号召按钮

---

### 分块 7: content-block
- **截图**: `pvc-kitchen-cabinets_pixel_7.jpg`
- **建议模块名**: `pvc-installation-process`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 2
- 水平间距: 20px, 垂直间距: 20px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #333333
- 正文: #000000
- 边框: none

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
  - card x4, 宽=auto, 高=auto, 圆角=0
    说明: 四个步骤卡片，每个包含步骤标题和描述文字，左右两列排列

**图片占位符** (1组):
  - **image** x1
    尺寸: 300px x auto, 比例: auto
    位置: 左下角, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `PVC installation process`
- **段落** (1个):
  - `An important benefit of PVC is how easy it is to install. It comes in pre-made boards that typically...`
- **列表项** (4个):
  - `1. Measure the space:`: Before installing PVC cabinets, make sure to prope...
  - `2. Choose the cabinet design:`: After measuring the space, you can select the PVC ...
  - `3. Assembly:`: Assemble the separate cabinet units of modular PVC...

**响应式**: 平板设备（≤768px）下，步骤改为单列布局，图片占满宽度；移动端（≤480px）下，图片隐藏，步骤单列显示
**特效**: 无
**内容摘要**: 展示PVC厨房橱柜的安装过程步骤，包括测量空间、选择设计、组装和安装四个关键环节，配合厨房图片辅助说明

---

### 分块 8: timeline
- **截图**: `pvc-kitchen-cabinets_pixel_8.jpg`
- **建议模块名**: `pvc-installation-process`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 3
- 水平间距: 20px, 垂直间距: 20px
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
  - card x6, 宽=auto, 高=auto, 圆角=8px
    说明: 6个步骤卡片，每个卡片包含步骤标题和描述，背景为白色，无阴影和边框

**图片占位符** (1组):
  - **none** x0
    尺寸: auto x auto, 比例: auto
    位置: none, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `PVC installation process`
- **段落** (1个):
  - `An important benefit of PVC is how easy it is to install. It comes in pre-made boards that typically...`
- **列表项** (6个):
  - `1. Measure the space:`: Before installing PVC cabinets, make sure to prope...
  - `2. Choose the cabinet design:`: After measuring the space, you can select the PVC ...
  - `3. Assembly:`: Assemble the separate cabinet units of modular PVC...

**响应式**: 平板设备（≤768px）下，步骤卡片改为单列布局，每行1个；移动端（≤480px）步骤标题字体缩小至18px
**特效**: 步骤卡片hover时背景色轻微变灰（#f8f8f8），提升交互反馈
**内容摘要**: 页面中部展示PVC厨房橱柜的安装流程，包含6个有序步骤，每个步骤有详细说明，帮助用户了解安装过程

---

### 分块 9: faq
- **截图**: `pvc-kitchen-cabinets_pixel_9.jpg`
- **建议模块名**: `pvc-kitchen-cabinets-faq`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 1, 行数: 7
- 水平间距: 0, 垂直间距: 20px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #007bff
- 标题: #333333
- 正文: #666666
- 边框: none

**字体**:
- 标题: 36px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 50px
- 下边距: 50px
- 元素间距: 20px
- 卡片内边距: 15px

**组件** (1个):
  - card x7, 宽=auto, 高=auto, 圆角=0
    说明: 白色背景的FAQ卡片，包含加号图标和问题文字

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `PVC Kitchen Cabinets: Buying Guide`
- **列表项** (7个):
  - `Can You Paint PVC Kitchen Cabinets?`: ...
  - `Which Is Better: Plywood or PVC?`: ...
  - `Are Cabinets Made Of PVC Waterproof?`: ...

**响应式**: 平板和移动端均保持单列布局，每个FAQ项垂直排列
**特效**: hover时加号图标变为蓝色，问题文字变为深灰色
**内容摘要**: 展示PVC厨房橱柜的常见问题列表，用户可点击展开查看答案

---

### 分块 10: faq
- **截图**: `pvc-kitchen-cabinets_pixel_10.jpg`
- **建议模块名**: `pvc-kitchen-cabinets-faq`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 1, 行数: 1
- 水平间距: 30px, 垂直间距: 30px
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
- 上边距: 60px
- 下边距: 60px
- 元素间距: 20px
- 卡片内边距: 15px

**组件** (1个):
  - accordion x10, 宽=auto, 高=auto, 圆角=0
    说明: 每个FAQ项是一个手风琴组件，白色背景带浅灰色边框，显示问题标题，可点击展开显示答案

**图片占位符** (1组):
  - **avatar** x1
    尺寸: 200px x 200px, 比例: 1:1
    位置: 左侧（联系表单区域）, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `PVC Kitchen Cabinets: Buying Guide`
- **按钮文字**: `Consult`
- **列表项** (10个):
  - `Is PVC A Suitable Material For Cabinets In Kitchens?`: ...
  - `Are PVC Cabinets Expensive?`: ...
  - `Are PVC Kitchen Cabinets Good?`: ...

**响应式**: 移动端设备下，FAQ列表单列显示，每个问题占满宽度；平板设备下保持单列布局
**特效**: FAQ项hover时标题颜色变为#FF8C00，点击展开显示答案内容
**内容摘要**: 页面中部展示PVC厨房橱柜的常见问题列表，包含10个可展开的手风琴项，用户可点击查看详细答案

---

### 分块 11: contact-form
- **截图**: `pvc-kitchen-cabinets_pixel_11.jpg`
- **建议模块名**: `free-quote-form`

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
- 卡片内边距: 15px

**组件** (7个):
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'Get A Free Quote'，深灰色（#222222），加粗700
  - paragraph x1, 宽=auto, 高=auto, 圆角=0
    说明: 副标题'* Kindly send us your project details and floor plan. We will quote for you within 8 hours!'，深灰色（#333333），常规400
  - image x1, 宽=200px, 高=200px, 圆角=0
    说明: 产品经理头像图片，左侧显示，无阴影
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 副标题'Want to Get Best Price Kitchen Cabinets?'，深灰色（#333333），常规400
  - paragraph x1, 宽=auto, 高=auto, 圆角=0
    说明: 段落'Share floor plan or house photos for 8-hour quote'，深灰色（#333333），常规400
  - form x1, 宽=auto, 高=auto, 圆角=0
    说明: 表单包含Name、Email、Tel/Whatsapp、City、Country-Select、Product Needed*（复选框）、Message、Choose File字段，无阴影
  - button x2, 宽=auto, 高=40px, 圆角=4px
    说明: 两个按钮，'Consult'为橙色（#FF8C00），'Send'为灰色（#666666），均无阴影

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
- **按钮文字**: `Consult`, `Send`

**响应式**: 平板设备（≤768px）下，左右列改为单列布局，图片在上，表单在下；移动端（≤480px）输入框堆叠，按钮占满宽度
**特效**: 按钮hover时'Consult'背景色加深至#E67300，'Send'背景色加深至#555555；表单输入框focus时边框高亮为#FF8C00
**内容摘要**: 页面中部获取免费报价的表单区域，包含产品经理头像、表单字段及行动号召按钮，用于收集用户项目信息

---

### 分块 12: contact-form
- **截图**: `pvc-kitchen-cabinets_pixel_12.jpg`
- **建议模块名**: `free-quote-form`

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
- 边框: #e0e0e0

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 20px
- 卡片内边距: 15px

**组件** (9个):
  - heading x1, 宽=auto, 高=auto, 圆角=0
    说明: 主标题'Get A Free Quote'，深灰色（#333333），加粗700
  - paragraph x1, 宽=auto, 高=auto, 圆角=0
    说明: 副标题'* Kindly send us your project details and floor plan. We will quote for you within 8 hours!'，灰色（#666666），常规400
  - image x1, 宽=200px, 高=auto, 圆角=0
    说明: 产品经理头像图片，左侧显示
  - text x2, 宽=auto, 高=auto, 圆角=0
    说明: 左侧文字'Want to Get Best Price Kitchen Cabinets?'和'Share floor plan or house photos for 8-hour quote'，灰色（#666666），常规400
  - input x5, 宽=100%, 高=40px, 圆角=4px
    说明: 输入框（姓名、邮箱、电话/Whatsapp、城市、国家-Select），白色背景，浅灰色边框（#e0e0e0）
  - checkbox x10, 宽=auto, 高=auto, 圆角=0
    说明: 产品选项复选框（Kitchen cabinet、Bedroom、Bathroom、Windows & Doors、Furniture、Lighting、Soft Furnishing、Tiles and Wood Flooring、Whole House Solution、Other Building Material）
  - textarea x1, 宽=100%, 高=120px, 圆角=4px
    说明: 消息文本域，白色背景，浅灰色边框（#e0e0e0）
  - file-upload x1, 宽=100%, 高=auto, 圆角=0
    说明: 文件上传按钮'Choose File'，默认显示'No file chosen'
  - button x2, 宽=auto, 高=40px, 圆角=4px
    说明: 按钮'Consult'（橙色背景#FF8C00，白色文字）和'Send'（灰色背景#6c757d，白色文字）

**图片占位符** (1组):
  - **avatar** x1
    尺寸: 200px x auto, 比例: auto
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Get A Free Quote`
- **副标题**: `* Kindly send us your project details and floor plan. We will quote for you within 8 hours!`
- **段落** (2个):
  - `Want to Get Best Price Kitchen Cabinets?`
  - `Share floor plan or house photos for 8-hour quote`
- **按钮文字**: `Consult`, `Send`
- **列表项** (10个):
  - `Kitchen cabinet`: ...
  - `Bedroom`: ...
  - `Bathroom`: ...

**响应式**: 平板设备（≤768px）下，表单与图片区域改为单列布局，图片占满宽度；移动端（≤480px）输入框占满容器宽度，复选框改为垂直排列
**特效**: Consult按钮hover时背景色加深至#E67300，Send按钮hover时背景色变浅至#5a6268
**内容摘要**: 页面中部联系表单区域，用于用户提交项目细节和产品需求以获取免费报价，包含个人信息输入、产品选项选择、消息描述及文件上传功能

---

### 分块 13: footer
- **截图**: `pvc-kitchen-cabinets_pixel_13.jpg`
- **建议模块名**: `footer-common`

**布局**:
- 容器: container-1200
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
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (4个):
  - heading x4, 宽=auto, 高=auto, 圆角=0
    说明: 四个列标题：Products、One-Stop Solutions、Customer Services、Contact Us，白色文字，加粗
  - text x21, 宽=auto, 高=auto, 圆角=0
    说明: 各列下的链接文字，如Kitchen Cabinet、Wardrobe等，白色文字
  - form x2, 宽=auto, 高=40px, 圆角=4px
    说明: whatsapp和Email输入框，白色背景，灰色边框
  - button x2, 宽=auto, 高=40px, 圆角=4px
    说明: 灰色背景（#6c757d），白色文字，'Send'按钮

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Products, One-Stop Solutions, Customer Services, Contact Us`
- **段落** (1个):
  - `Don't miss our future updates! Get Subscribed Today!`
- **按钮文字**: `Send`, `Send`
- **列表项** (21个):
  - `Kitchen Cabinet`: ...
  - `Wardrobe`: ...
  - `Windows and Doors`: ...

**响应式**: 平板设备（≤768px）下，四列改为两列布局；移动端（≤480px）改为单列布局，各元素垂直排列
**特效**: 按钮hover时背景色加深，输入框focus时边框高亮
**内容摘要**: 页面底部footer区域，包含四个功能模块：产品分类、一站式解决方案、客户服务、联系我们，提供链接导航、联系信息和订阅表单

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
    --spacing-card-padding: 20px;
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
- `pvc-kitchen-cabinets_pixel_1.jpg`
- `pvc-kitchen-cabinets_pixel_10.jpg`
- `pvc-kitchen-cabinets_pixel_11.jpg`
- `pvc-kitchen-cabinets_pixel_12.jpg`
- `pvc-kitchen-cabinets_pixel_13.jpg`
- `pvc-kitchen-cabinets_pixel_2.jpg`
- `pvc-kitchen-cabinets_pixel_3.jpg`
- `pvc-kitchen-cabinets_pixel_4.jpg`
- `pvc-kitchen-cabinets_pixel_5.jpg`
- `pvc-kitchen-cabinets_pixel_6.jpg`
- `pvc-kitchen-cabinets_pixel_7.jpg`
- `pvc-kitchen-cabinets_pixel_8.jpg`
- `pvc-kitchen-cabinets_pixel_9.jpg`

---

## 🎯 推荐输出方式：WordPress 页面模板

### 页面模板文件
**位置**: `wp-content/themes/{theme-name}/page-templates/template-{page-name}.php`

```php
<?php
/**
 * Template Name: {Page Name} 页面模板
 * Description: 克隆自 https://georgeconstructions.com/pvc-kitchen-cabinets/
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
