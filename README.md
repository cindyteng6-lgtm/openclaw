# OpenClaw PPT 生成器

专业的 OpenClaw 智能助手平台演示文稿生成工具

## 📁 文件说明

- `create_ppt.py` - PPTX 生成脚本（使用 python-pptx）
- `create_pdf_pro.py` - PDF 生成脚本（使用 reportlab，商业专业版）
- `OpenClaw_专业正式版.pptx` - 生成的 PPTX 文件（12 页）
- `OpenClaw_专业正式版.pdf` - 生成的 PDF 文件（12 页）

## 🚀 快速开始

### 安装依赖

```bash
# PPT 生成
pip install python-pptx

# PDF 生成
pip install reportlab
```

### 生成 PPT

```bash
python3 create_ppt.py
```

### 生成 PDF

```bash
python3 create_pdf_pro.py
```

## 📊 PPT 内容大纲

1. **封面** - OpenClaw 智能助手平台
2. **什么是 OpenClaw** - 平台定位与核心价值
3. **核心功能** - 文件管理、浏览器操作、定时任务、多平台消息
4. **技术架构** - 三层架构设计
5. **系统架构概览** - Gateway/Agent/Surface 层
6. **记忆系统** - AI 连续性设计
7. **子代理系统** - 并行任务处理
8. **安全设计** - 隐私优先
9. **安全边界** - 最佳实践
10. **快速开始** - 安装配置指南
11. **使用场景** - 生产力与生活场景
12. **结束页** - GitHub 链接

## 🎨 设计特点

- **Apple/特斯拉发布会风格** - 深蓝渐变封面
- **专业配色方案** - 科技蓝 + 橙色强调
- **字号精准适配** - 横版 A4 最优显示
- **可视化架构图** - 三层架构 + 插件系统
- **商业级设计** - 卡片阴影、图标圆形背景、装饰图案

## 📝 字体说明

- macOS 使用系统字体 STHeiti（黑体）
- Windows 可使用微软雅黑
- PDF 无需嵌入字体，跨平台显示一致

## 🔄 自动备份

已配置每日自动备份（每晚 8:00）：

- 自动将当天修改的代码保存到 `archive/YYYY-MM-DD/` 子目录
- 自动提交并推送到 GitHub
- 日志文件：`/tmp/openclaw_backup.log`

## 🔗 相关链接

- OpenClaw 官方文档：https://docs.openclaw.ai
- OpenClaw GitHub：https://github.com/openclaw/openclaw

## 📄 License

MIT License
