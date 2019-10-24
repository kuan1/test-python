# 创建函数
def test():
    print('这是一个python的函数')
    print('test')


print(test)
test()

# 默认参数和位置参数要放在前边


def sum(a=1, b=2, c=3):
    return a + b + c


print(sum(1, c=2))


# 不定长参数
def sum(*args) -> int:
    '''
    文档字符串
    sum函数，可以输入不定长度的数字参数，返回int类型
    '''
    print(args)
    total = 0
    for i in args:
        total += i
    print(locals())
    return total


print(sum(1, 2, 3, 4, 5))
ls = (1, 2, 3)
print(sum(*ls))


# ** 对字典进行解包

# help内置函数使用说明，文档字符串
# help(print)
# help(sum)

# 获取命名空间
print(locals())

# 获取全局命名空间
print(globals())

# 递归方式实现阶乘


def factorial(num) -> int:
    if num > 1:
        return num * factorial(num - 1)
    else:
        return num


print(factorial(3))
