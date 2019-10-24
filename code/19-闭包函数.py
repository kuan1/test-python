# 闭包函数
def fn():
    l = []

    def inner():
        l.append(1)
        print(l)

    return inner


inner = fn()
print(inner)

inner()
inner()
