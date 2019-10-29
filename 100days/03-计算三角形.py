'''
判断是否是三角形
通过三边计算三角形周长和面积
'''

import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('周长：', perimeter)
    print('面积：', area)
else:
    print('不可以构成三角形')
