'''
输入两个正整数计算最大公约数和最小工倍数
'''
x = int(input('请输入整数：'))
y = int(input('请输入整数：'))

if x > y:
    (x, y) = (y, x)

for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print(f'{x}和{y}的最大公约数：{factor}')
        print(f'{x}和{y}的最小公倍数：{x * y // factor}')
        break
