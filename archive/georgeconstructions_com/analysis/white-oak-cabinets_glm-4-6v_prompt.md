# WordPress 页面克隆任务

## 原始页面信息
- URL: https://georgeconstructions.com/white-oak-cabinets/
- 标题: Why White Oak Cabinets Make a Perfect Choice
- 总高度: 9784px

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
- **截图**: `white-oak-cabinets_pixel_1.jpg`
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
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 30px
- 卡片内边距: 20px

**组件** (2个):
  - navbar x1, 宽=100%, 高=auto, 圆角=0
    说明: 顶部导航栏，包含logo、导航链接和Quick Quote按钮
  - button x2, 宽=auto, 高=40px, 圆角=4px
    说明: Quick Quote按钮（橙色）和Download Catalogues按钮（白色带边框）

**图片占位符** (1组):
  - **hero-banner** x1
    尺寸: 100% x auto, 比例: 16:9
    位置: 背景全屏, object-fit: cover
    遮罩: rgba(0,0,0,0.3)
    占位符建议: kitchen-interior-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `White Oak Cabinets`
- **副标题**: `Custom White Oak Kitchen Cabinets for Your Project`
- **段落** (1个):
  - `White Oak continues to be quite prominent in the design business, particularly with the growing popu...`
- **按钮文字**: `Quick Quote`, `Download Catalogues`

**响应式**: 移动端导航菜单折叠为汉堡图标，hero标题字体缩小，按钮宽度自适应
**特效**: 背景图片带半透明遮罩，按钮hover时有颜色加深效果
**内容摘要**: 展示White Oak橱柜的主视觉区域，包含导航栏、背景厨房图片、标题、描述文字及行动按钮

---

### 分块 2: product-grid
- **截图**: `white-oak-cabinets_pixel_2.jpg`
- **建议模块名**: `white-oak-cabinets-grid`

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
- 正文: #333333
- 边框: none

**字体**:
- 标题: 18px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 0
- 卡片内边距: 20px

**组件** (1个):
  - card x6, 宽=350px, 高=120px, 圆角=8px
    说明: 浅灰色背景卡片，居中排列，显示白橡木橱柜类型标题

**图片占位符** (0组):
  - 无图片

**⚠️ 提取的文字内容（用于默认数据）**:
- **卡片内容** (6个):
  - `White Oak Kitchen Cabinets`: ...
  - `Modern White Oak Kitchen Cabinets`: ...
  - `Rift Sawn White Oak Cabinets`: ...

**响应式**: 平板设备显示2列，移动端显示1列
**特效**: 无
**内容摘要**: 展示白橡木橱柜的不同变体类型，包括现代、 Rift Sawn、 Shaker等款式

---

### 分块 3: image-text
- **截图**: `white-oak-cabinets_pixel_3.jpg`
- **建议模块名**: `white-oak-kitchen-cabinets-image-text`

**布局**:
- 容器: container-1200
- 类型: flex
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
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 20px
- 卡片内边距: 20px

**组件** (3个):
  - image x2, 宽=50%, 高=auto, 圆角=0
    说明: 厨房橱柜产品图片，展示白橡木橱柜的实际应用场景
  - button x2, 宽=auto, 高=40px, 圆角=4px, 有阴影
    说明: 橙色主按钮，显示"Get a Free Quote"文字，用于引导用户获取报价
  - text x4, 宽=50%, 高=auto, 圆角=0
    说明: 深灰色正文文字，展示白橡木橱柜的介绍内容

**图片占位符** (1组):
  - **product** x2
    尺寸: 50% x auto, 比例: 16:9
    位置: 左侧（第一行）/右侧（第二行）, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Understanding White Oak for Kitchen Cabinets`
- **段落** (4个):
  - `White oak is not to be confused with rift oak, a technique of cutting wood; it is a different kind t...`
  - `The wood's appearance and composition differ in several important ways. White wood has a somewhat st...`
  - `The Wood Database offers a detailed comparison of red and white oak: "Upon casual observation, raw o...`
- **按钮文字**: `Get a Free Quote`, `Get a Free Quote`

**响应式**: 平板设备（768px-1024px）改为1列布局，移动端（<768px）堆叠为1列，每个图文块垂直排列
**特效**: 按钮 hover 时颜色加深（#E67E00），图片 hover 时轻微放大（scale 1.02）
**内容摘要**: 该区域通过图文混排形式，详细介绍了白橡木厨房橱柜的特点（如与红橡木的区别、外观特征），以及其受欢迎的原因，配合实际厨房场景图片增强内容的直观性和说服力

---

### 分块 4: why-choose
- **截图**: `white-oak-cabinets_pixel_4.jpg`
- **建议模块名**: `kitchen-cabinets-why-choose`

**布局**:
- 容器: container-1200
- 类型: grid
- 列数: 2, 行数: 2
- 水平间距: 30px, 垂直间距: 40px
- 对齐: left

**颜色**:
- 背景: #ffffff
- 主色: #ff8c00
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
  - button x1, 宽=120px, 高=40px, 圆角=4px
    说明: 橙色按钮，文字为"Get a Free Quote"，位于"Why Are White Oak Cabinets Our Obsession?"标题下方

**图片占位符** (1组):
  - **product** x2
    尺寸: 50% x auto, 比例: 16:9
    位置: 右列，上下排列, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Why Are White Oak Cabinets Our Obsession?`
- **段落** (2个):
  - `For many reasons, white oak cabinets have delighted homeowners and designers.`
  - `Numerous choices exist to obtain the appearance of white oak kitchen cabinetry.`
- **按钮文字**: `Get a Free Quote`
- **列表项** (3个):
  - `Considered as more flexible and "in vogue," white oak is.`: ...
  - `From classic to modern, the light tones complement many interior schemes.`: ...
  - `It also evokes an organic sense without being clearly conventional.`: ...

**响应式**: 平板设备显示2列，移动端设备显示1列
**特效**: 无
**内容摘要**: 该区域主要展示选择白橡木橱柜的理由（灵活性、风格适配、有机感），以及白橡木橱柜的不同选项（天然白橡木和染色红橡木）

---

### 分块 5: 解析失败
- 截图: `white-oak-cabinets_pixel_5.jpg`
- 错误: 
{
    "module_type": "content-block",
    "module_name_suggestion": "white-oak-cabinetry-options",


### 分块 6: features
- **截图**: `white-oak-cabinets_pixel_6.jpg`
- **建议模块名**: `kitchen-cabinets-benefits`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 20px
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
- 卡片内边距: 0

**组件** (2个):
  - image x1, 宽=400px, 高=auto, 圆角=0
    说明: 左侧展示厨房橱柜的实景图片，用于配合文字说明优势
  - button x1, 宽=120px, 高=40px, 圆角=4px
    说明: 橙色背景按钮，文字为‘Get a Free Quote’，用于引导用户获取报价

**图片占位符** (1组):
  - **product** x1
    尺寸: 400px x auto, 比例: auto
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Benefits of White Oak Kitchen Cabinets`
- **段落** (6个):
  - `When you picture oak cabinets, you probably picture the rich colors popular in the 1980s. Particular...`
  - `Red oak has become less popular, but oak in general shouldn’t be discounted in the field of interior...`
  - `There are many benefits to this increasingly chosen alternative. We have found several main advantag...`
- **按钮文字**: `Get a Free Quote`

**响应式**: 平板设备下调整为2列布局，移动端设备下调整为1列布局，图片宽度自适应
**特效**: 无特殊交互效果，以静态图文展示为主
**内容摘要**: 该区域主要展示白橡木厨房橱柜的优势，包括耐用性、纹理特点等，通过图文结合的方式阐述白橡木作为厨房橱柜材料的优势

---

### 分块 7: features
- **截图**: `white-oak-cabinets_pixel_7.jpg`
- **建议模块名**: `kitchen-cabinets-benefits`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 20px
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
- 卡片内边距: 20px

**组件** (2个):
  - image x1, 宽=50%, 高=auto, 圆角=0
    说明: 展示现代厨房场景的图片，包含橱柜、灯具和家具
  - text x1, 宽=50%, 高=auto, 圆角=0
    说明: 包含主标题、段落和子标题的文字内容区域

**图片占位符** (1组):
  - **gallery** x1
    尺寸: 50% x auto, 比例: 16:9
    位置: 右侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Benefits of White Oak Kitchen Cabinets`
- **段落** (5个):
  - `Red oak has become less popular, but oak in general shouldn’t be discounted in the field of interior...`
  - `There are many benefits to this increasingly chosen alternative. We have found several main advantag...`
  - `White oak, with a 1360 hardness value, is sturdier than many other hardwood species. This makes it a...`

**响应式**: 平板设备下调整为1列布局，移动端文字与图片堆叠显示
**特效**: 无
**内容摘要**: 该区域主要展示白橡木厨房橱柜的优势，包括耐用性、纹理美观性等，通过图文结合的方式呈现

---

### 分块 8: features
- **截图**: `white-oak-cabinets_pixel_8.jpg`
- **建议模块名**: `kitchen-cabinets-features`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 2
- 水平间距: 30px, 垂直间距: 40px
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
- 上边距: 60px
- 下边距: 60px
- 元素间距: 20px
- 卡片内边距: 0

**组件** (2个):
  - text x2, 宽=auto, 高=auto, 圆角=0
    说明: 左侧文本区域，包含两个标题及对应段落，无边框和阴影
  - image x1, 宽=600px, 高=auto, 圆角=0
    说明: 右侧厨房场景图片，展示白橡木橱柜应用，无边框和阴影

**图片占位符** (1组):
  - **product** x1
    尺寸: 600px x auto, 比例: 16:9
    位置: 右侧, object-fit: cover
    占位符建议: kitchen-scene

**⚠️ 提取的文字内容（用于默认数据）**:
- **段落** (2个):
  - `Honey’s and red oak’s warm crimson tones simply aren’t hip these days. We’re not sure if they’ll eve...`
  - `White oak finds application in many different spheres. In modern kitchens, where it can replace whit...`

**响应式**: 平板设备调整为1列布局，移动端文本与图片堆叠显示
**特效**: 无
**内容摘要**: 展示白橡木厨房橱柜的两大优势：趋势驱动的颜色方案与多样性应用，通过图文混排突出其现代适配性与设计灵活性

---

### 分块 9: image-text
- **截图**: `white-oak-cabinets_pixel_9.jpg`
- **建议模块名**: `kitchen-white-oak-contrasting-elements`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
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
- 上边距: 40px
- 下边距: 60px
- 元素间距: 20px
- 卡片内边距: 0

**组件** (2个):
  - image x1, 宽=100%, 高=auto, 圆角=0
    说明: 厨房场景图片，展示白橡木橱柜与对比元素的搭配
  - button x1, 宽=auto, 高=40px, 圆角=4px
    说明: 橙色背景按钮，显示‘Get a Free Quote’文字

**图片占位符** (1组):
  - **gallery** x1
    尺寸: 100% x auto, 比例: auto
    位置: 右侧, object-fit: cover
    占位符建议: kitchen-interior

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Incorporate Contrasting Elements`
- **段落** (3个):
  - `As said before, usage of red oak in former kitchens is the main reason behind most of today’s uncert...`
  - `One can reach this with a range of details. Because of its wide spectrum of colors and patterns as w...`
  - `Additional items that could greatly affect the whole impact are flooring, fixtures, and hardware. To...`
- **按钮文字**: `Get a Free Quote`

**响应式**: 平板设备下改为单列布局，图片宽度调整为100%
**特效**: 按钮hover时背景色加深，图片加载时淡入效果
**内容摘要**: 该区域主要介绍如何在厨房中通过对比元素（如台面、五金、地板等）搭配白橡木，以增强空间层次感和设计细节

---

### 分块 10: faq
- **截图**: `white-oak-cabinets_pixel_10.jpg`
- **建议模块名**: `white-oak-kitchen-cabinets-faq`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 1, 行数: 5
- 水平间距: 0px, 垂直间距: 30px
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
- 上边距: 40px
- 下边距: 40px
- 元素间距: 30px
- 卡片内边距: 0px

**组件** (2个):
  - card x5, 宽=auto, 高=auto, 圆角=0px
    说明: FAQ折叠项，包含加号图标和问题标题，边框颜色#e0e0e0
  - button x1, 宽=120px, 高=40px, 圆角=4px, 有阴影
    说明: 橙色背景按钮，白色文字，位于FAQ上方

**图片占位符** (1组):
  - **icon** x5
    尺寸: 20px x 20px, 比例: 1:1
    位置: 左侧, object-fit: contain
    占位符建议: plus-icon

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `White Oak Kitchen Cabinets From George`
- **段落** (2个):
  - `Search George’s large range of products while looking for innovative and motivating ideas to improve...`
  - `Should you be ready to start, do not hesitate to drop in one of our showrooms or visit our Design Ce...`
- **按钮文字**: `Get a Free Quote`
- **列表项** (5个):
  - `What is white oak?`: ...
  - `Which floor colors go best with white oak kitchen cabinets?`: ...
  - `Why do white wood cabinets appeal so much?`: ...

**响应式**: 移动端保持单列布局，FAQ项垂直堆叠，按钮宽度自适应
**特效**: FAQ项 hover 时加号图标旋转，按钮 hover 时背景色加深
**内容摘要**: 展示George白橡木厨房橱柜的FAQ部分，包含公司介绍和常见问题解答

---

### 分块 11: contact-form
- **截图**: `white-oak-cabinets_pixel_11.jpg`
- **建议模块名**: `white-oak-contact-form`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 0px
- 对齐: center

**颜色**:
- 背景: #ffffff
- 主色: #FF8C00
- 标题: #000000
- 正文: #333333
- 边框: #e0e0e0

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 20px
- 卡片内边距: 20px

**组件** (8个):
  - image x1, 宽=200px, 高=200px, 圆角=0px
    说明: 产品经理头像图片，位于左侧列，显示为正方形，无阴影和边框
  - text x1, 宽=auto, 高=auto, 圆角=0px
    说明: 主标题"Get A Free Quote"，位于左侧列，字体加粗，黑色
  - text x2, 宽=auto, 高=auto, 圆角=0px
    说明: 副标题和说明文字，位于左侧列，字体常规，深灰色
  - input x5, 宽=100%, 高=40px, 圆角=4px
    说明: 5个文本输入框（Name、Email、Tel/Whatsapp、City、Country-Select），白色背景，浅灰色边框，圆角4px
  - checkbox x10, 宽=auto, 高=auto, 圆角=0px
    说明: 10个复选框（Kitchen cabinet、Bedroom、Bathroom等），位于"Product Needed*"下方，默认未选中
  - textarea x1, 宽=100%, 高=120px, 圆角=4px
    说明: 消息文本框，白色背景，浅灰色边框，圆角4px
  - button x1, 宽=100%, 高=40px, 圆角=4px
    说明: 文件选择按钮"Choose File"，白色背景，浅灰色边框，圆角4px
  - button x1, 宽=100%, 高=40px, 圆角=4px
    说明: 提交按钮"Send"，橙色背景，白色文字，圆角4px

**图片占位符** (1组):
  - **avatar** x1
    尺寸: 200px x 200px, 比例: 1:1
    位置: 左侧列顶部, object-fit: cover
    占位符建议: product-manager-avatar

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Get A Free Quote`
- **副标题**: `* Kindly send us your project details and floor plan. We will quote for you within 8 hours!`
- **段落** (2个):
  - `Want to Get Best Price White Oak Cabinets?`
  - `Share floor plan or house photos for 8-hour quote`
- **按钮文字**: `Send`

**响应式**: 平板设备下左右列堆叠（1列），移动端输入框和复选框单列排列
**特效**: 无 hover 效果，表单元素为静态展示
**内容摘要**: 该区域为联系表单模块，用于收集用户项目信息和需求，提供免费报价服务

---

### 分块 12: contact-form
- **截图**: `white-oak-cabinets_pixel_12.jpg`
- **建议模块名**: `white-oak-contact-form`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 30px, 垂直间距: 20px
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #666666
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
- 卡片内边距: 20px

**组件** (5个):
  - image x1, 宽=200px, 高=200px, 圆角=0
    说明: 左侧展示的Product Manager头像图片，背景为浅灰色，尺寸固定
  - input x5, 宽=100%, 高=40px, 圆角=4px
    说明: 表单中的文本输入框，包括Name、Email、Tel/Whatsapp、City、Country-Select，边框为浅灰色
  - checkbox x10, 宽=auto, 高=auto, 圆角=0
    说明: Product Needed*下的复选框选项，包括Kitchen cabinet、Bedroom、Bathroom等10个选项
  - textarea x1, 宽=100%, 高=120px, 圆角=4px
    说明: Message文本域，用于输入项目详情，边框为浅灰色
  - button x2, 宽=100%, 高=40px, 圆角=4px
    说明: 表单中的按钮，包括Choose File（白色背景，灰色文字）和Send（灰色背景，白色文字）

**图片占位符** (1组):
  - **avatar** x1
    尺寸: 200px x 200px, 比例: 1:1
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Get A Free Quote`
- **副标题**: `* Kindly send us your project details and floor plan. We will quote for you within 8 hours!`
- **段落** (2个):
  - `Want to Get Best Price White Oak Cabinets?`
  - `Share floor plan or house photos for 8-hour quote`
- **按钮文字**: `Choose File`, `Send`
- **列表项** (10个):
  - `Kitchen cabinet`: ...
  - `Bedroom`: ...
  - `Bathroom`: ...

**响应式**: 平板设备下改为1列布局，移动端保持1列，表单元素堆叠显示
**特效**: 无显著特殊效果，表单元素 hover 时可能有边框颜色变化
**内容摘要**: 该区域为获取免费报价的联系表单，包含用户信息输入、产品需求选择、项目详情描述及文件上传功能，用于收集客户项目信息以提供8小时内报价

---

### 分块 13: contact-form
- **截图**: `white-oak-cabinets_pixel_13.jpg`
- **建议模块名**: `get-a-quote-form`

**布局**:
- 容器: container-1200
- 类型: flex
- 列数: 2, 行数: 1
- 水平间距: 40px, 垂直间距: 0px
- 对齐: space-between

**颜色**:
- 背景: #ffffff
- 主色: #6c757d
- 标题: #2d3748
- 正文: #333333
- 边框: #e2e8f0

**字体**:
- 标题: 24px, 字重: 700
- 正文: 16px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 60px
- 下边距: 60px
- 元素间距: 10px
- 卡片内边距: 20px

**组件** (7个):
  - image x1, 宽=200px, 高=200px, 圆角=0
    说明: 左侧展示的产品经理头像图片，方形，无阴影
  - input x4, 宽=100%, 高=45px, 圆角=4px
    说明: 表单输入框，包括Name、Email、City、Country-Select，边框为浅灰色
  - input x2, 宽=48%, 高=45px, 圆角=4px
    说明: 表单输入框，包括Email、Tel/Whatsapp，左右并列，各占48%宽度
  - checkbox x10, 宽=auto, 高=auto, 圆角=0
    说明: 产品需求复选框，包括Kitchen cabinet、Bedroom等10个选项，两行排列
  - textarea x1, 宽=100%, 高=120px, 圆角=4px
    说明: 消息输入框，多行文本域
  - file-upload x1, 宽=100%, 高=auto, 圆角=0
    说明: 文件上传按钮，显示'Choose File'和'No file chosen'
  - button x1, 宽=100%, 高=45px, 圆角=0
    说明: 发送按钮，灰色背景，白色文字

**图片占位符** (1组):
  - **avatar** x1
    尺寸: 200px x 200px, 比例: 1:1
    位置: 左侧, object-fit: cover
    占位符建议: gray-bg

**⚠️ 提取的文字内容（用于默认数据）**:
- **主标题**: `Get A Free Quote`
- **副标题**: `* Kindly send us your project details and floor plan. We will quote for you within 8 hours!`
- **段落** (2个):
  - `Want to Get Best Price White Oak Cabinets?`
  - `Share floor plan or house photos for 8-hour quote`
- **按钮文字**: `Send`
- **列表项** (1个):
  - `Product Needed*`: Kitchen cabinet, Bedroom, Bathroom, Windows & Door...

**响应式**: 平板端：左右列堆叠，表单输入框全宽；移动端：同平板端，复选框单列排列
**特效**: 无
**内容摘要**: 该区域展示获取免费报价的表单，包含个人信息输入、产品需求选择、消息输入及文件上传功能，用于收集用户项目信息以提供报价

---

### 分块 14: footer
- **截图**: `white-oak-cabinets_pixel_14.jpg`
- **建议模块名**: `footer`

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
- 边框: #cccccc

**字体**:
- 标题: 18px, 字重: 700
- 正文: 14px, 字重: 400
- 行高: 1.6

**间距**:
- 上边距: 80px
- 下边距: 80px
- 元素间距: 20px
- 卡片内边距: 20px

**组件** (4个):
  - text x19, 宽=auto, 高=auto, 圆角=0
    说明: 白色背景下的浅灰色文字链接，包含产品分类、解决方案、客户服务类目
  - button x2, 宽=auto, 高=40px, 圆角=0
    说明: 灰色背景、白色文字的“Send”按钮，位于联系表单区域
  - form x2, 宽=auto, 高=40px, 圆角=4px
    说明: 白色背景、浅灰色边框的输入框，分别用于输入whatsapp和Email
  - icon x2, 宽=16px, 高=16px, 圆角=0
    说明: 邮件和电话图标，位于联系信息区域

**图片占位符** (1组):
  - **icon** x0
    尺寸: 0 x 0, 比例: auto
    位置: none, object-fit: none
    占位符建议: none

**⚠️ 提取的文字内容（用于默认数据）**:
- **段落** (1个):
  - `Don’t miss our future updates! Get Subscribed Today!`
- **按钮文字**: `Send`, `Send`
- **列表项** (4个):
  - `Products`: ...
  - `One-Stop Solutions`: ...
  - `Customer Services`: ...

**响应式**: 平板设备下调整为2列布局，移动端设备下调整为1列布局
**特效**: 无
**内容摘要**: 页面底部footer区域，展示产品分类、一站式解决方案、客户服务类目、联系信息及订阅表单

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
    --spacing-element: 20px;
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
- `white-oak-cabinets_pixel_1.jpg`
- `white-oak-cabinets_pixel_10.jpg`
- `white-oak-cabinets_pixel_11.jpg`
- `white-oak-cabinets_pixel_12.jpg`
- `white-oak-cabinets_pixel_13.jpg`
- `white-oak-cabinets_pixel_14.jpg`
- `white-oak-cabinets_pixel_2.jpg`
- `white-oak-cabinets_pixel_3.jpg`
- `white-oak-cabinets_pixel_4.jpg`
- `white-oak-cabinets_pixel_5.jpg`
- `white-oak-cabinets_pixel_6.jpg`
- `white-oak-cabinets_pixel_7.jpg`
- `white-oak-cabinets_pixel_8.jpg`
- `white-oak-cabinets_pixel_9.jpg`

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
