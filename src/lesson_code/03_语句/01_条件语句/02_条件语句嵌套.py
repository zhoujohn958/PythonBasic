"""条件语句嵌套"""
age = float(input('请问你今年多少岁? '))
if age >= 18:
    ans = input('可以出示您的身份证吗(Y/N): ')
    if ans == 'Y':
        print('身份核对正确, 请尽情冲浪吧!')
    else:
        print('成年人需要凭身份证上网!')
else:
    print('未成年人禁止出入网吧!')


""" 条件语句特点 """
''' ① 每个条件语句中，最多只会满足一次条件 '''
num = 5
if num > 0:
    print('a')
elif num > 1:
    print('b')
elif num > 2:
    print('c')

if num > 3:
    print('d')

if num > 4:
    print('f')

if num > 5:
    print('g')
else:
    print('h')

''' ② 当判断条件是一个值时，该值bool判定的结果决定条件是否成立 '''
if 1:
    print('hello world')
if None:
    print('hello world')

""" 简单的猜拳游戏 """
d = {'石头': 0, '剪刀': 1, '布': 2}
computer = set(d).pop()
player = input('请出拳(石头、剪刀、布): ')
# 出拳展示
print(f'电脑出拳: {computer}\n玩家出拳: {player}')
# 胜负判定
c, p = d[computer], d[player]
if p-c in (-1, 2):
    print('玩家胜!')
elif c == p:
    print('平局!')
else:
    print('电脑胜!')
