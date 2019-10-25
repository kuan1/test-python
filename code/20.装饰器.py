# decorate
def need_login(fn):
    def new_fn(*args, **kwargs):
        print("login")
        r = fn(*args, **kwargs)
        print('end')
        return r
    return new_fn


@need_login
def test(*args):
    print('测试')
    return [*args]


print(test(1, 2, 3))
