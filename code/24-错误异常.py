# try:
#     print('1' + 2)
# except Exception as e:
#     print(e)


# 自定义错误
def test(a):
    if a < 0:
        raise Exception('参数不可以小于0')


test(-100)
