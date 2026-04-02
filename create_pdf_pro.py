#!/usr/bin/env python3
"""
创建专业美观的 OpenClaw 介绍 PDF - 商业专业版
优化字号适配 + 专业图形图标
"""

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
import math

# 专业配色方案
COLORS = {
    'primary': colors.HexColor('#0066CC'),
    'primary_dark': colors.HexColor('#004C99'),
    'primary_light': colors.HexColor('#3399FF'),
    'secondary': colors.HexColor('#1D1D1F'),
    'accent': colors.HexColor('#FF9500'),
    'accent_blue': colors.HexColor('#5AC8FA'),
    'light_bg': colors.HexColor('#F5F5F7'),
    'medium_bg': colors.HexColor('#E8E8ED'),
    'dark': colors.HexColor('#1D1D1F'),
    'white': colors.white,
    'gray': colors.HexColor('#86868B'),
    'light_gray': colors.HexColor('#D2D2D7'),
}

def register_chinese_font():
    """注册中文字体"""
    font_paths = [
        ('PingFang SC', '/System/Library/Fonts/PingFang.ttc'),
        ('STHeiti', '/System/Library/Fonts/STHeiti Light.ttc'),
        ('STHeiti', '/System/Library/Fonts/STHeiti Medium.ttc'),
    ]
    
    for font_name, font_path in font_paths:
        if os.path.exists(font_path):
            try:
                pdfmetrics.registerFont(TTFont('ChineseFont', font_path))
                print(f"✅ 使用字体：{font_path}")
                return 'ChineseFont'
            except:
                continue
    
    return 'ChineseFont'

def draw_gradient_bg(c, width, height, color1, color2):
    """绘制渐变背景"""
    for i in range(100):
        y = i * height / 100
        ratio = i / 100
        c.setFillColor(colors.Color(
            color1.red + (color2.red - color1.red) * ratio,
            color1.green + (color2.green - color1.green) * ratio,
            color1.blue + (color2.blue - color1.blue) * ratio
        ))
        c.rect(0, y, width, height/100, fill=1, stroke=0)

def draw_decorative_pattern(c, x, y, size, color):
    """绘制装饰性几何图案"""
    c.setFillColor(color)
    # 圆环
    c.setStrokeColor(color)
    c.setLineWidth(2)
    c.circle(x, y, size, fill=0, stroke=1)
    c.circle(x, y, size * 0.6, fill=0, stroke=1)
    c.circle(x, y, size * 0.3, fill=1, stroke=0)

def draw_tech_pattern(c, width, height):
    """绘制科技感背景图案"""
    c.setStrokeColor(colors.Color(0, 0.4, 0.8, 0.08))
    c.setLineWidth(1)
    
    # 网格线
    for i in range(0, int(width), 60):
        c.line(i, 0, i, height)
    for j in range(0, int(height), 60):
        c.line(0, j, width, j)
    
    # 装饰点
    c.setFillColor(colors.Color(0, 0.4, 0.8, 0.15))
    for i in range(0, int(width), 120):
        for j in range(0, int(height), 120):
            c.circle(i, j, 3, fill=1, stroke=0)

def draw_icon_circle(c, x, y, radius, icon_text, bg_color, text_color):
    """绘制图标圆形背景"""
    # 外圈光晕
    c.setFillColor(colors.Color(bg_color.red, bg_color.green, bg_color.blue, 0.2))
    c.circle(x, y, radius + 8, fill=1, stroke=0)
    
    # 主圆形
    c.setFillColor(bg_color)
    c.circle(x, y, radius, fill=1, stroke=0)
    
    # 内圈高光
    c.setStrokeColor(colors.Color(1, 1, 1, 0.3))
    c.setLineWidth(2)
    c.circle(x, y, radius, fill=0, stroke=1)
    
    # 图标文字
    c.setFillColor(text_color)
    c.setFont('ChineseFont', int(radius * 0.9))
    c.drawCentredString(x - radius/2, y - radius/2, icon_text)

def draw_arrow(c, x1, y1, x2, y2, color):
    """绘制箭头"""
    c.setStrokeColor(color)
    c.setLineWidth(3)
    c.setLineCap(1)
    c.line(x1, y1, x2, y2)
    
    # 箭头头部
    arrow_size = 12
    angle = math.atan2(y2 - y1, x2 - x1)
    c.line(x2, y2, 
           x2 - arrow_size * math.cos(angle - math.pi/6),
           y2 - arrow_size * math.sin(angle - math.pi/6))
    c.line(x2, y2,
           x2 - arrow_size * math.cos(angle + math.pi/6),
           y2 - arrow_size * math.sin(angle + math.pi/6))

def draw_title_page(c, width, height):
    """封面页 - 商业专业风格"""
    # 深蓝渐变背景
    draw_gradient_bg(c, width, height, 
        colors.HexColor('#001A33'), 
        colors.HexColor('#004080'))
    
    # 科技感背景图案
    draw_tech_pattern(c, width, height)
    
    # 装饰圆形图案
    draw_decorative_pattern(c, width * 0.85, height * 0.8, 80, colors.Color(0, 0.4, 0.8, 0.15))
    draw_decorative_pattern(c, width * 0.15, height * 0.2, 60, colors.Color(0, 0.4, 0.8, 0.1))
    
    # 主标题
    c.setFillColor(COLORS['white'])
    c.setFont('ChineseFont', 72)
    c.drawCentredString(width/2, height/2 + 120, "OpenClaw")
    
    # 副标题
    c.setFont('ChineseFont', 36)
    c.setFillColor(COLORS['primary_light'])
    c.drawCentredString(width/2, height/2 + 40, "智能助手平台")
    
    # 描述
    c.setFont('ChineseFont', 22)
    c.setFillColor(COLORS['gray'])
    c.drawCentredString(width/2, height/2 - 20, "下一代 AI 自动化与任务编排系统")
    
    # 底部装饰线（带渐变效果）
    gradient_x = width/2 - 150
    for i in range(300):
        x = gradient_x + i
        ratio = i / 300
        c.setFillColor(colors.Color(
            COLORS['primary_light'].red * (1-ratio) + COLORS['accent'].red * ratio,
            COLORS['primary_light'].green * (1-ratio) + COLORS['accent'].green * ratio,
            COLORS['primary_light'].blue * (1-ratio) + COLORS['accent'].blue * ratio
        ))
        c.rect(x, height/2 - 80, 1, 4, fill=1, stroke=0)

def draw_section_page(c, width, height, title, description=""):
    """章节页 - 极简专业风格"""
    # 白色背景
    c.setFillColor(COLORS['white'])
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # 左侧色条
    c.setFillColor(COLORS['primary'])
    c.rect(0, 0, 20, height, fill=1, stroke=0)
    
    # 左上角装饰
    c.setFillColor(colors.Color(0, 0.4, 0.8, 0.05))
    c.circle(100, height - 100, 80, fill=1, stroke=0)
    c.setFillColor(colors.Color(0, 0.4, 0.8, 0.08))
    c.circle(100, height - 100, 50, fill=1, stroke=0)
    
    # 大标题
    c.setFillColor(COLORS['secondary'])
    c.setFont('ChineseFont', 56)
    c.drawString(100, height/2 + 80, title)
    
    # 装饰线条组合
    c.setStrokeColor(COLORS['primary'])
    c.setLineWidth(4)
    c.line(100, height/2 + 50, 180, height/2 + 50)
    c.setStrokeColor(COLORS['accent'])
    c.setLineWidth(4)
    c.line(185, height/2 + 50, 220, height/2 + 50)
    
    if description:
        c.setFont('ChineseFont', 26)
        c.setFillColor(COLORS['gray'])
        c.drawString(100, height/2 - 10, description)
    
    # 右下角装饰图案
    draw_decorative_pattern(c, width - 120, 120, 70, colors.Color(0, 0.4, 0.8, 0.12))

def draw_content_page(c, width, height, title, items, page_num=0, total_pages=0):
    """内容页 - 专业布局"""
    # 白色背景
    c.setFillColor(COLORS['white'])
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # 顶部区域（带装饰）
    c.setFillColor(COLORS['primary'])
    c.rect(0, height - 100, width, 100, fill=1, stroke=0)
    
    # 左侧色条延续
    c.setFillColor(COLORS['primary'])
    c.rect(0, 0, 20, height, fill=1, stroke=0)
    
    # 顶部装饰图案
    c.setFillColor(colors.Color(1, 1, 1, 0.1))
    c.circle(100, height - 50, 40, fill=1, stroke=0)
    c.setFillColor(colors.Color(1, 1, 1, 0.15))
    c.circle(width - 150, height - 50, 30, fill=1, stroke=0)
    
    # 标题
    c.setFillColor(COLORS['white'])
    c.setFont('ChineseFont', 28)
    c.drawString(60, height - 65, title)
    
    # 页码
    c.setFont('ChineseFont', 13)
    c.setFillColor(colors.Color(1, 1, 1, 0.8))
    c.drawRightString(width - 60, height - 65, f"{page_num} / {total_pages}")
    
    # 内容区域背景（带阴影效果）
    c.setFillColor(colors.Color(0, 0, 0, 0.05))
    c.roundRect(45, 65, width - 90, height - 240, 15, fill=1, stroke=0)
    
    c.setFillColor(COLORS['light_bg'])
    c.roundRect(50, 70, width - 100, height - 250, 12, fill=1, stroke=0)
    
    # 内容文本
    y_position = height - 155
    text_x = 85
    
    for item in items:
        if y_position < 90:
            break
        
        if item.startswith('##'):
            # 小标题（带图标背景）
            c.setFillColor(COLORS['primary_light'])
            c.rect(text_x - 10, y_position - 5, 8, 22, fill=1, stroke=0)
            c.setFillColor(COLORS['primary'])
            c.setFont('ChineseFont', 22)
            c.drawString(text_x + 10, y_position, item[2:].strip())
            y_position -= 36
            c.setFillColor(COLORS['secondary'])
        elif item.startswith('•') or item.startswith('  •'):
            # 列表项
            indent = 35 if item.startswith('  •') else 0
            c.setFont('ChineseFont', 17)
            # 项目符号
            c.setFillColor(COLORS['accent'])
            c.drawString(text_x + indent - 15, y_position, "●")
            c.setFillColor(COLORS['secondary'])
            c.drawString(text_x + indent, y_position, item)
            y_position -= 28
        elif item == '':
            y_position -= 20
        else:
            c.setFont('ChineseFont', 17)
            c.drawString(text_x, y_position, item)
            y_position -= 28

def draw_feature_grid(c, width, height, title, features, page_num=0, total_pages=0):
    """特性网格页 - 2x2 布局"""
    # 白色背景
    c.setFillColor(COLORS['white'])
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # 顶部区域
    c.setFillColor(COLORS['primary'])
    c.rect(0, height - 100, width, 100, fill=1, stroke=0)
    
    # 左侧色条
    c.setFillColor(COLORS['primary'])
    c.rect(0, 0, 20, height, fill=1, stroke=0)
    
    # 标题
    c.setFillColor(COLORS['white'])
    c.setFont('ChineseFont', 28)
    c.drawString(60, height - 65, title)
    
    # 页码
    c.setFont('ChineseFont', 13)
    c.setFillColor(colors.Color(1, 1, 1, 0.8))
    c.drawRightString(width - 60, height - 65, f"{page_num} / {total_pages}")
    
    # 2x2 网格
    card_width = (width - 160) / 2
    card_height = (height - 260) / 2
    gap = 25
    
    positions = [
        (60, height - 150 - card_height),
        (60 + card_width + gap, height - 150 - card_height),
        (60, height - 150 - card_height * 2 - gap),
        (60 + card_width + gap, height - 150 - card_height * 2 - gap),
    ]
    
    icons = ['📁', '🌐', '⏰', '💬']
    icon_colors = [COLORS['primary'], COLORS['accent'], COLORS['accent_blue'], COLORS['primary_light']]
    
    for i, (feature, icon, icon_color) in enumerate(zip(features, icons, icon_colors)):
        x, y = positions[i]
        
        # 卡片阴影
        c.setFillColor(colors.Color(0, 0, 0, 0.08))
        c.roundRect(x + 3, y - 3, card_width, card_height, 12, fill=1, stroke=0)
        
        # 卡片背景
        c.setFillColor(COLORS['white'])
        c.roundRect(x, y, card_width, card_height, 12, fill=1, stroke=0)
        
        # 卡片顶部色条
        c.setFillColor(icon_color)
        c.roundRect(x, y + card_height - 8, card_width, 8, 0, fill=1, stroke=0)
        
        # 图标（带圆形背景）
        draw_icon_circle(c, x + 55, y + card_height - 55, 32, icon, icon_color, COLORS['white'])
        
        # 标题
        c.setFillColor(COLORS['secondary'])
        c.setFont('ChineseFont', 19)
        c.drawString(x + 105, y + card_height - 55, feature['title'])
        
        # 描述
        c.setFont('ChineseFont', 14)
        c.setFillColor(COLORS['gray'])
        desc_y = y + card_height - 85
        for line in feature['desc'].split('\n'):
            c.drawString(x + 105, desc_y, line)
            desc_y -= 22

def draw_architecture_page(c, width, height, page_num=0, total_pages=0):
    """架构图页"""
    # 白色背景
    c.setFillColor(COLORS['white'])
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # 顶部区域
    c.setFillColor(COLORS['primary'])
    c.rect(0, height - 100, width, 100, fill=1, stroke=0)
    
    # 左侧色条
    c.setFillColor(COLORS['primary'])
    c.rect(0, 0, 20, height, fill=1, stroke=0)
    
    # 标题
    c.setFillColor(COLORS['white'])
    c.setFont('ChineseFont', 28)
    c.drawString(60, height - 65, "系统架构概览")
    
    # 页码
    c.setFont('ChineseFont', 13)
    c.setFillColor(colors.Color(1, 1, 1, 0.8))
    c.drawRightString(width - 60, height - 65, f"{page_num} / {total_pages}")
    
    # 三层架构图
    layers = [
        ('Surface 层', '用户界面与交互', 'Web / Telegram / Discord', COLORS['primary_light'], '🖥️'),
        ('Agent 层', 'AI 模型推理与决策', 'Qwen / GPT / Claude', COLORS['primary'], '🧠'),
        ('Gateway 层', '核心调度与服务管理', '任务编排 / 工具调用', colors.HexColor('#003366'), '⚙️'),
    ]
    
    layer_height = 115
    start_y = height - 200
    
    for i, (name, desc, detail, color, icon) in enumerate(layers):
        y = start_y - i * (layer_height + 30)
        
        # 层背景（带阴影）
        c.setFillColor(colors.Color(0, 0, 0, 0.08))
        c.roundRect(85, y - 3, width - 170, layer_height + 6, 14, fill=1, stroke=0)
        
        # 层背景
        c.setFillColor(color)
        c.roundRect(85, y, width - 170, layer_height, 12, fill=1, stroke=0)
        
        # 左侧装饰条
        c.setFillColor(colors.Color(1, 1, 1, 0.3))
        c.roundRect(85, y, 8, layer_height, 0, fill=1, stroke=0)
        
        # 图标
        c.setFillColor(COLORS['white'])
        c.setFont('ChineseFont', 28)
        c.drawString(110, y + layer_height - 50, icon)
        
        # 层名称
        c.setFillColor(COLORS['white'])
        c.setFont('ChineseFont', 26)
        c.drawString(150, y + layer_height - 45, name)
        
        # 描述
        c.setFont('ChineseFont', 17)
        c.setFillColor(colors.Color(1, 1, 1, 0.9))
        c.drawString(150, y + layer_height - 75, desc)
        
        # 详情
        c.setFont('ChineseFont', 14)
        c.setFillColor(colors.Color(1, 1, 1, 0.75))
        c.drawString(150, y + layer_height - 98, detail)
        
        # 层间箭头
        if i < len(layers) - 1:
            draw_arrow(c, width/2, y - 5, width/2, y - 25, COLORS['gray'])
    
    # 插件系统模块
    box_width = (width - 220) / 2
    box_height = 100
    
    # Skills 模块
    c.setFillColor(colors.Color(0, 0, 0, 0.06))
    c.roundRect(85, 75, box_width, box_height, 14, fill=1, stroke=0)
    c.setFillColor(COLORS['accent'])
    c.roundRect(88, 78, box_width - 6, box_height - 6, 12, fill=1, stroke=0)
    c.setFillColor(COLORS['white'])
    c.setFont('ChineseFont', 20)
    c.drawCentredString(88 + box_width / 2, 138, "🔌 Skills 技能")
    c.setFont('ChineseFont', 14)
    c.setFillColor(colors.Color(1, 1, 1, 0.9))
    c.drawCentredString(88 + box_width / 2, 108, "GitHub / 天气 / 健康检查")
    
    # Memory 模块
    c.setFillColor(colors.Color(0, 0, 0, 0.06))
    c.roundRect(88 + box_width + 15, 75, box_width, box_height, 14, fill=1, stroke=0)
    c.setFillColor(COLORS['accent_blue'])
    c.roundRect(91 + box_width + 15, 78, box_width - 6, box_height - 6, 12, fill=1, stroke=0)
    c.setFillColor(COLORS['white'])
    c.setFont('ChineseFont', 20)
    c.drawCentredString(91 + box_width * 1.5 + 15, 138, "🧠 Memory 记忆")
    c.setFont('ChineseFont', 14)
    c.setFillColor(colors.Color(1, 1, 1, 0.9))
    c.drawCentredString(91 + box_width * 1.5 + 15, 108, "短期日志 + 长期记忆")

def main():
    output_path = '/Users/xiaowu/.openclaw/workspace/OpenClaw_专业正式版.pdf'
    width, height = landscape(A4)
    
    # 注册中文字体
    register_chinese_font()
    
    c = canvas.Canvas(output_path, pagesize=landscape(A4))
    total_pages = 12
    
    # 1. 封面
    draw_title_page(c, width, height)
    c.showPage()
    
    # 2. 什么是 OpenClaw
    draw_content_page(c, width, height, "什么是 OpenClaw？", [
        "## 平台定位",
        "开源 AI 助手运行平台，让 AI 真正融入你的工作流",
        "",
        "## 核心特性",
        "• 支持多模型接入（Qwen、GPT、Claude 等）",
        "• 内置丰富工具集：文件操作、浏览器控制、定时任务",
        "• 可扩展的技能系统，轻松定制专属能力",
        "",
        "## 核心价值",
        "• 🔧 自动化日常任务，释放人力",
        "• 🧠 持久化记忆，真正理解你的需求",
        "• 🔐 本地部署，数据完全可控",
    ], 2, total_pages)
    c.showPage()
    
    # 3. 核心功能 - 网格布局
    draw_feature_grid(c, width, height, "核心功能特性", [
        {'title': '文件与 Workspace', 'desc': '读写编辑文件\n自动整理归类'},
        {'title': '浏览器操作', 'desc': '自动化网页交互\n内容提取与搜索'},
        {'title': '定时任务', 'desc': 'Cron 表达式支持\n心跳检查提醒'},
        {'title': '多平台消息', 'desc': 'Telegram/Discord\n群组智能参与'},
    ], 3, total_pages)
    c.showPage()
    
    # 4. 技术架构章节页
    draw_section_page(c, width, height, "技术架构", "模块化设计 · 灵活扩展")
    c.showPage()
    
    # 5. 系统架构图
    draw_architecture_page(c, width, height, 5, total_pages)
    c.showPage()
    
    # 6. 记忆系统
    draw_content_page(c, width, height, "记忆系统 - AI 的连续性", [
        "## 📝 日常记忆",
        "  • memory/YYYY-MM-DD.md",
        "  • 每日自动创建，记录原始对话与事件",
        "  • 类似人类的日记，保留完整上下文",
        "",
        "## 🧠 长期记忆",
        "  • MEMORY.md",
        "  • 精选精华记忆，仅主会话加载",
        "  • 安全隔离：群聊不访问个人隐私",
        "",
        "## 📋 配置文件",
        "  • SOUL.md：AI 人格与行为准则",
        "  • USER.md：用户偏好与背景信息",
        "  • IDENTITY.md：AI 自我认知",
    ], 6, total_pages)
    c.showPage()
    
    # 7. 子代理系统
    draw_content_page(c, width, height, "子代理系统 - 并行任务处理", [
        "## 核心能力",
        "• 🚀 支持 spawn 独立子代理处理复杂任务",
        "• 📊 子代理可运行不同模型、不同配置",
        "• 🔄 主代理可 steer/kill/监控子代理状态",
        "",
        "## 适用场景",
        "• GitHub issue 批量处理",
        "• 多文件代码重构",
        "• 长时间后台任务",
    ], 7, total_pages)
    c.showPage()
    
    # 8. 安全设计章节页
    draw_section_page(c, width, height, "安全设计", "隐私优先 · 权限可控")
    c.showPage()
    
    # 9. 安全边界
    draw_content_page(c, width, height, "安全边界与最佳实践", [
        "## 🔒 数据安全",
        "  • 本地部署，数据不出境",
        "  • MEMORY.md 主会话隔离，群聊不泄露隐私",
        "  • 敏感操作需用户确认（删除、外部发送）",
        "",
        "## ⚠️ 红线规则",
        "  • 禁止主动外发隐私数据",
        "  • 禁止执行破坏性命令无确认",
        "  • 群聊中不代表用户发声",
        "",
        "## ✅ 推荐实践",
        "  • 使用 trash 而非 rm（可恢复）",
        "  • 不确定时先询问用户",
    ], 9, total_pages)
    c.showPage()
    
    # 10. 快速开始
    draw_content_page(c, width, height, "快速开始指南", [
        "## 1️⃣ 安装",
        "  npm install -g openclaw",
        "",
        "## 2️⃣ 配置",
        "  openclaw config  # 设置模型、Surface 等",
        "",
        "## 3️⃣ 启动",
        "  openclaw gateway start",
        "",
        "## 4️⃣ 连接",
        "  Web 界面 / Telegram / Discord / 移动端 App",
        "",
        "## 📚 文档",
        "  本地：/usr/local/lib/node_modules/openclaw/docs",
        "  在线：https://docs.openclaw.ai",
    ], 10, total_pages)
    c.showPage()
    
    # 11. 使用场景
    draw_content_page(c, width, height, "典型使用场景", [
        "## 生产力场景",
        "• 📧 智能邮件管理 - 自动分类、摘要、提醒",
        "• 📅 日程助手 - 心跳检查即将到来的会议",
        "• 💻 开发辅助 - GitHub issue 处理、代码审查",
        "",
        "## 生活场景",
        "• 🏠 智能家居 - 通过节点控制摄像头、通知",
        "• 📰 信息聚合 - 定时抓取新闻、天气、股票",
        "• 📝 知识管理 - 自动整理笔记、更新记忆",
    ], 11, total_pages)
    c.showPage()
    
    # 12. 结束页
    draw_title_page(c, width, height)
    draw_gradient_bg(c, width, height, 
        colors.HexColor('#001A33'), 
        colors.HexColor('#004080'))
    c.setFillColor(COLORS['white'])
    c.setFont('ChineseFont', 54)
    c.drawCentredString(width/2, height/2 + 120, "开始构建你的 AI 助手")
    c.setFont('ChineseFont', 22)
    c.setFillColor(COLORS['primary_light'])
    c.drawCentredString(width/2, height/2 + 40, "https://github.com/openclaw/openclaw")
    c.showPage()
    
    c.save()
    
    print(f"✅ PDF 已生成：{output_path}")
    print(f"📄 文件大小：{os.path.getsize(output_path) / 1024:.1f} KB")

if __name__ == '__main__':
    main()
