# python列表入门
ls = [1, 2, 3, 4, 5, 6]

# 获取对应下标
print(ls[2])
print(ls[-1])

# 获取长度
print(len(ls))

# 切片: 包括起始位置，不包括结束位置，不影响原列表
print(ls[1:2])
print(ls[1:])

# 复制列表
print(ls[:])

# 第三个参数表示间隔
print(ls[1:5:2])

# 列表累加
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(a + b)

# 列表复制
print([1, 2, 3] * 3)

# in 和 not in
print(1 in [1, 2, 3, 4])
print(1 not in [1, 2, 3, 4])

# min max
a = [1, 2, 3, 4, 5, 6, 2]
print(min(a))
print(max(a))

# index: 出现的下标
# count：出现的次数
print(a.index(3))
print(a.count(2))

# 修改列表
ls = ls2 = [1, 2, 3, 4]
print(ls, ls2)
ls[0] = 0
print(ls, ls2)

# del 删除元素
ls = [1, 2, 3, 4]
del ls[2]
# del ls{::2}
# del ls[1:]
print(ls)

# 切片赋值，必须传入序列，不可以是数字
ls = [1, 2, 3, 4]
ls[0:2] = 'ab'
print(ls)
ls = [1, 2, 3, 4]
# ls[0:2] = ['a', 'b', 'c', 'd']  # ['a', 'b', 3, 4]
ls[0:2] = 'a'  # ['a', 3, 4]
print(ls)

# 插入
ls = [1, 2, 3, 4]
ls[1:1] = '插入'
print(ls)

# 类型转换
a = '1234'
print(list(a))

# 最后拆入
ls = [0, 1, 2]
ls.append('a')
print(ls)

# 插入（下标,元素）
ls = [0, 1, 2]
ls.insert(1, 'aa')
print(ls)
