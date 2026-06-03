#!/usr/bin/env python3
"""删除项目里指定的「段落标题」行。

默认删除每个 .md 页面里这几条通用小标题（连同其后紧跟的一个空行）：

    ## 背景与难题
    ## 求解
    ## 意义

想多删/少删，改下面的 LABELS 即可（只写 # 后面的文字，不含 # 和空格）。
代码块（``` 围栏内）里的同名行不会被动。

用法：
    python scripts/strip_section_headings.py            # 直接修改文件
    python scripts/strip_section_headings.py --dry-run  # 只看会删哪些，不写盘
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# 要删除的标题文字（# 后面的部分）。按需增删。
LABELS = {
    # paradoxes / prehistory
    "背景与难题",
    "求解",
    "意义",
    # nature-of-time
    "背景与思潮",
    "主张与方法",
    "结果与意义",
    "余响",
    # history
    "时代背景",
    "影响与遗产",
}

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", ".jekyll-cache", "_site", "vendor"}

# 匹配 “# 一到六个井号 + 空格 + 标签 + 行尾（可有尾随空格）”
HEADING_RE = re.compile(r"^#{1,6}\s+(?P<label>.+?)\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")


def strip_file(path: Path) -> tuple[int, list[str]]:
    """处理单个文件，返回 (删除的标题数, 被删标题文本列表)。"""
    # newline="" 保留原始换行符，避免 LF/CRLF 被改写
    with open(path, "r", encoding="utf-8", newline="") as f:
        text = f.read()
    lines = text.splitlines(keepends=True)

    out: list[str] = []
    removed: list[str] = []
    in_fence = False
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue

        if not in_fence:
            m = HEADING_RE.match(line.rstrip("\r\n"))
            if m and m.group("label") in LABELS:
                removed.append(m.group("label"))
                i += 1
                # 连带删掉紧跟的一个空行，避免留下双空行
                if i < n and lines[i].strip() == "":
                    i += 1
                continue

        out.append(line)
        i += 1

    new_text = "".join(out)
    if new_text != text:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(new_text)
    return len(removed), removed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="只统计，不写文件")
    args = parser.parse_args()

    # Windows 控制台默认 GBK，强制 UTF-8 以免中文输出乱码
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

    total = 0
    touched = 0
    for path in sorted(ROOT.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if args.dry_run:
            # 干跑：复用逻辑但不落盘——临时读、数、不写
            with open(path, "r", encoding="utf-8", newline="") as f:
                text = f.read()
            count = 0
            in_fence = False
            for raw in text.splitlines():
                if FENCE_RE.match(raw):
                    in_fence = not in_fence
                    continue
                if not in_fence:
                    m = HEADING_RE.match(raw)
                    if m and m.group("label") in LABELS:
                        count += 1
        else:
            count, _ = strip_file(path)
        if count:
            touched += 1
            total += count
            rel = path.relative_to(ROOT).as_posix()
            print(f"  {rel}: 删除 {count} 条")

    verb = "将删除" if args.dry_run else "已删除"
    print(f"\n{verb} {total} 条标题，涉及 {touched} 个文件。")
    if args.dry_run:
        print("（这是 --dry-run，未改动任何文件。）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
