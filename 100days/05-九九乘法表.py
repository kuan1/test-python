'''
输出九九乘法表
'''

for x in range(1, 10):
    for y in range(1, x + 1):
        print(f'{y} * {x} = {x * y}', end='\t')
    print()
