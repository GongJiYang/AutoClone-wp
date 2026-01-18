# AutoClone 架构文档

## 项目概述

AutoClone 是一个自动化工具，用于将网页克隆到WordPress。采用**视觉模型分析 + 代码模型生成**的混合方案。

## 架构设计

### 核心流程

```
URL列表
  ↓
智能分块截图（DOM优先，像素降级）
  ↓
视觉模型分析结构（GLM-4.6V）
  ↓
生成结构描述JSON + Cursor提示
  ↓
Cursor/Claude Code 生成代码
  ↓
WordPress REST API 写入
```

### 目录结构

```
autoclone/
├── data/                    # 数据文件
│   └── urls.csv            # URL列表
├── src/                     # 源代码
│   ├── core/               # 核心模块
│   │   ├── config.py       # 配置管理
│   │   ├── screenshot.py   # 截图功能
│   │   ├── analyzer.py     # 视觉分析
│   │   └── wordpress.py    # WordPress客户端
│   └── cli/                # 命令行入口
│       └── main.py
├── scripts/                 # 工具脚本
│   └── cleanup.py
├── output/                  # 输出目录
│   ├── screenshots/         # 截图
│   ├── analysis/           # 分析结果
│   └── generated/          # 生成的HTML
└── docs/                    # 文档
```

## 核心模块

### Config (配置管理)
- 统一管理所有配置
- 环境变量读取
- 目录路径管理

### ScreenshotCapture (截图)
- DOM结构分块（优先）
- 像素分块（降级）
- 智能重叠处理

### VisionAnalyzer (视觉分析)
- GLM-4.6V / GPT-4V 支持
- 结构分析（不生成代码）
- JSON格式输出

### WordPressClient (WordPress)
- REST API 客户端
- 页面/文章创建
- 连接测试

## 设计原则

1. **职责分离**：视觉模型只分析，代码模型只生成
2. **智能降级**：DOM分块失败自动降级到像素分块
3. **模块化**：核心功能独立，易于测试和维护
4. **配置集中**：所有配置统一管理

## 技术栈

- Python 3.9+
- Playwright - 浏览器自动化
- ZhipuAI GLM-4.6V - 视觉分析
- WordPress REST API - 内容写入
