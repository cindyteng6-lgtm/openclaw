#!/bin/bash
# OpenClaw PPT 每日自动备份脚本
# 每天将修改的代码保存到日期子目录并推送到 GitHub

set -e

# 配置
WORKSPACE="/Users/xiaowu/.openclaw/workspace"
REPO_DIR="$WORKSPACE/openclaw-ppt"
BACKUP_FILES=(
    "create_pdf_pro.py"
    "create_ppt.py"
    "OpenClaw_专业正式版.pdf"
    "OpenClaw_专业正式版.pptx"
)

# 获取当天日期
DATE=$(date +%Y-%m-%d)
DATE_DIR="$REPO_DIR/archive/$DATE"

echo "🚀 开始每日备份 - $DATE"

# 创建日期子目录
mkdir -p "$DATE_DIR"

# 复制文件到日期子目录
for file in "${BACKUP_FILES[@]}"; do
    if [ -f "$WORKSPACE/$file" ]; then
        cp "$WORKSPACE/$file" "$DATE_DIR/"
        echo "✅ 已复制：$file"
    else
        echo "⚠️  文件不存在：$file"
    fi
done

# 复制 README.md（如有更新）
if [ -f "$REPO_DIR/README.md" ]; then
    cp "$REPO_DIR/README.md" "$DATE_DIR/"
fi

# 进入仓库目录
cd "$REPO_DIR"

# Git 操作
git add archive/$DATE
git commit -m "📦 每日备份 $DATE

- 自动归档当天代码版本
- 包含 PPT/PDF 生成脚本及输出文件" || echo "ℹ️  无变更，跳过提交"

# 推送到 GitHub
git push origin main

echo "✅ 每日备份完成 - $DATE"
echo "📂 存档位置：$DATE_DIR"
