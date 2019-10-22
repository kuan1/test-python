from time import *

start = time()

# 数字
num = 100002111111111

# 是否是质数
flag = False
i = 2

while i < num ** 0.5:
    i += 1
    if not (num % i):
        print(i, num / i)
        flag = True

end = time()

print(flag,  end - start)
