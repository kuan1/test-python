'''
判断一个数字是否是素数
'''

import math

num = int(input('请输入一个正整数：'))
end = int(math.sqrt(num))

is_prime = True
for x in range(2, end + 1):
    if num % num == 0:
        is_prime = False
        break

resp = '素数' if is_prime and num != 1 else '不是素数'
print(resp)
