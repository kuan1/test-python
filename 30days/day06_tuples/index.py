# Creating a Tuple
empty_tuple = ()
empty_tuple2 = tuple()

print(empty_tuple, empty_tuple2, empty_tuple == empty_tuple2)

tpl = (1, 2, 3, 4)
print(tpl)

# Tuple length
tpl = (1, 2, 3, 4)
print(len(tpl))

# Accessing Tuple Items
tpl = (1, 2, 3, 4)
print(tpl[0])
print(tpl[-1])

# Slicing Tuples
tpl = ('item1', 'item2', 'item3', 'item4')
print(tpl[0:4])
print(tpl[1:2])
print(tpl[-2:-1])
print(tpl[-2:])

# Change Tuples to List
tpl = ('item1', 'item2', 'item3', 'item4')
print(tpl[0])
print(type(list(tpl)), list(tpl))

# Checking an Item in a Tuple
tpl = ('item1', 'item2', 'item3', 'item4')
print('item1' in tpl)
print('item11' in tpl)

# Joining Tuples
print((1, 2, 3, 4) + (5, 6))

# Deleting Tuples
tpl = (1,2,3)
del tpl
# print(tpl) # NameError: name 'tpl' is not defined
