# bug.py —— 计算购物车折扣后的总价
prices = [120, 88, 45, 200]
rates = [0.9, 0.8, 0.75, 0.5]

total = 0
for i in range(len(prices)):
    price = prices[i]
    rate = rates[i]
    final = price * rate
    total += final
    print(f"第 {i + 1} 件：原价 {price}，折后 {final}")

print(f"应付总额：{total}")
