# == 和 !=比较的是赋值是否相等
# is 和 not比较的是id是否相等，是否是同一个对象
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
print(id(a), id(b))
