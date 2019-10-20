# python字符串
a = "ab"
print(a)

a = 'ab'
print(a)

a = 'a\
\n\
b'
print(a)

# 多行文本
a = '''a
b'''
print(a)

a = 'a' + 'b'
print(a)

# 字符串不能累加数字
# a = 'a' + 123

# 字符串占位符
# %2.5s 表示2-5位
# %s 表示任意占位符
# %f 浮点数占位符
# %d 整数占位符
a = 'hello %s'%'world'
print(a)

a = 'hello %.2f'%1.002
print(a)

a = 'hello %.2d'%1.002
print(a)

# python3格式化字符串
temp1 = '临时1'
temp2 = '临时2'
a = f'你好！ {temp1}、{temp2}'
print(a)

# 复制字符串
a = 'hello \n'
print(a * 100)
