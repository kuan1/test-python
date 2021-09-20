# create string
letter = "p"
print(letter)
print(len(letter))

# string concatenation
first_name = '忠宽'
last_name = '卢'
print(first_name + ' ' + last_name)

# String formatting
print('这是 %s, 那是 %s' %('A', 'B'))
python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string)
print('我是{name},今年{age}'.format(name="卢忠宽", age="28"))
print('我是{},今年{}'.format("卢忠宽", "28"))

# String interpolation
a = 3
b = 4
print(f'{a} + {b} = {a + b}')