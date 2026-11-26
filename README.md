# 编程学习

从零开始的学习仓库，每个练习都带说明，能照着复现。

## 环境
- Windows
- Python 3.13（安装命令：winget install --id Python.Python.3.13 -e）
- Git
- VS Code + Python 扩展

## 目录
| 目录 | 内容 |
|---|---|
| week01/day01 | 第一个 Python 程序 |
| week01/day02 | 终端命令笔记 |
| week01/day03 | 批量重命名工具 |
| week01/day04 | 调试练习 |

## 怎么确认环境没问题
python --version
git --version

# rename.py —— 批量重命名小工具

给目录里所有 .txt 文件加上 `new_` 前缀。

## 用法

    python rename.py <目录> [--dry-run]

- `<目录>`：要处理的文件夹
- `--dry-run`：只预览，不真的改名

## 例子

    python week01\day03\rename.py week01\day03\demo --dry-run
    python week01\day03\rename.py week01\day03\demo

## 什么情况会失败

- 目录不存在：打印"目标目录不存在"并退出
- 目录里没有 .txt：什么也不做
- 目标文件名已存在：报 FileExistsError