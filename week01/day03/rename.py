import sys
from pathlib import Path


def main():
    if len(sys.argv) < 2:
        print("用法: python rename.py <目录> [--dry-run]")
        return

    folder = Path(sys.argv[1])
    dry = "--dry-run" in sys.argv

    # TODO 1: 如果 folder 不存在，打印一句人能看懂的话，然后 return
    if not folder.exists():
        print("目标目录不存在")
        return
    
    # TODO 2: 遍历 folder 下所有 .txt 文件
    for p in Path(folder).glob("*.txt"):

    # TODO 3: 对每个文件，新名字 = "new_" + 原文件名
    #         dry 为真时只打印"将把 A 改成 B"，不真改
    #         否则真的改名
        if dry:
            print("将把 " + p.name + " 改成 " + "new_" + p.name)
        else:
            p.rename(p.with_name("new_"+p.name))

if __name__ == "__main__":
    main()