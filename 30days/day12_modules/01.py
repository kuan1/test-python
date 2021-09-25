# import mymodule

# print(mymodule.generate_fullname('卢', '忠宽'))

from mymodule import generate_fullname as get_fullname, toast_age as get_age

print(get_fullname('卢', '卢忠宽'))
print(get_age(28))