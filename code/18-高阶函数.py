# 匿名函数
print((lambda a, b: a + b)(1, 2))

# filter函数
l = [1, 2, 3, 4]
f = filter(lambda i: i % 2, l)
print(list(f))


# map函数
l = [1, 2, 3, 4]
m = map(lambda i: i * 2, l)
print(list(m))


# sort函数
l = ['aaaa', 'ccc', 'bb']
l.sort(key=len)
print(l)


# sorted排序 不影响原文件
l = [1, '2', '3', 4]
print(sorted(l, key=int))
l = '1234322'
print(sorted(l))
