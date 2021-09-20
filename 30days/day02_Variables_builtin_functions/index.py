# abs
print(abs(-1))
print(abs(1))

# dir
print(dir())

# divmod 返回除数和余数
print(divmod(1, 2))  # (0，1)

# filter
arr = [1, 2, 3, 4, 5]
print(list(filter(lambda n: n % 2, arr)))

# format
print("今天在学习{name}, 继续{action}".format(action="努力", name="python"))
print("今天在学习{}, 继续{}".format("python", "努力"))

# input 收集输入
# print(input('-->'))

# int
print(int('080'))
print(int('050', 8))

# len 获取长度
print(len('1234'))

# list 列表
print(list('1234'), [1, 2, 3, 4])

# globals locals
print(globals())


def fn():
    a = 1
    b = 2
    print(locals(), locals().get('a'))


fn()

# map
print(list(map(lambda x: 2 * x, [1, 2, 3, 4])))

# max
print(max('1234'))
print(max(1, 2, 3, 4))

# min
print(min('1234'))
print(min(1, 2, 3, 4))

# pow
print(pow(2, 3))

# range
for item in range(0, 10):
    print(item)

# reversed
print(list(reversed([1, 2, 3, 4])))

# round
print(round(1.22))
print(round(2.622, 2))

# set
print(set([1, 2, 1, 2]))

# slice
print(list([0, 1, 2, 3, 4, 5, 6][0:5]))
print(list([0, 1, 2, 3, 4, 5, 6][1:]))
print(list([0, 1, 2, 3, 4, 5, 6][0:5:2]))

# sorted
print(sorted([1,2,5,3], reverse=True))
print(sorted([{"a": 3},{"a": 1},{"a": 2}], key=lambda x: x.get("a"), reverse=True))

# tuple
print(tuple([1,2,1,2]))

# type
print(type([1,2]))