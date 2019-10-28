'''
输入半径计算周长和面积
'''

import math

radius = float(input('请输入半径'))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f'周长：{perimeter}')
print(f'面积：{area}')
