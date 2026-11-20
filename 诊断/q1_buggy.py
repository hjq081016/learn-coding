# q1_buggy.py —— 先读，不要运行
scores = {"语文": 88, "数学": 92, "英语": 75}

total = 0
for k, v in scores:
    total = total + v

print("总分:", total)
print("平均分:", total / len(scores))
