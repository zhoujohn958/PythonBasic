"""
字典推导式 
格式：{k: v for子句}
格式：{k: v for子句 更多的for子句或者if子句}
"""
d = {x: x**2 for x in range(4)}
print(d)

# 类比
d = {}
for x in range(4): # [0,1,2,3]
    d[x] = x ** 2
print(d) # {0: 0, 1: 1, 2: 4, 3: 9}


d = {x: v for x in range(4) for v in range(9) if v % 2}
print(d) # {0: 7, 1: 7, 2: 7, 3: 7}

# 类比
d = {}
for x in range(4):      # [0,1,2,3]
    for v in range(9):  # [0,1,2,3,4,5,6,7,8]
        if v % 2:       # 只处理奇数
            d[x] = v    # 每次满足条件都会覆盖之前的值
print(d)
