# set集合和列表很相似
# 不同点： 无序、只存不可变集合、不能有重复元素
a = {2, 1, 3, 4, 4, 4, 5}
print(a, type(a))

# 创建空集合
a = set()
print(a)

# 字典转换为集合时，只会有健
a = set('hello')
a = set([1, 2, 3, 4, 5])
a = set({'a': 1, 'b': 2})
print(a)

# add 添加元素，无返回值
a = set()
a.add(1)
print(a)

# update 将一个集合添加到另一集合
a = {1, 2, 3}
b = {3, 4, 5}
a.update(b)
print(a)

# pop随机删除
a = {1, 2, 3}
a.pop()

# remove 指定删除
a = {'a', 'b', 'c'}
a.remove('a')
print(a)
