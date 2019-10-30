'''
输入2～99之间的素数
'''

import math

for x in range(2, 101):
    is_prime = True
    for y in range(2, int(math.sqrt(x)) + 1):
        if (x % y == 0):
            is_prime = False
            break
    if is_prime:
        print(x)
