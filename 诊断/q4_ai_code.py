# q4_ai_code.py —— 假设这是 AI 给你生成的代码
import os


def read_total(path):
    f = open(path, "r", encoding="utf-8")
    lines = f.readlines()
    total = 0
    for line in lines:
        total += int(line.split(",")[1])
    return total


def main():
    try:
        print(read_total("data.csv"))
    except:
        pass


main()
