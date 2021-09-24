# create list
lst = list()
print(lst)
print(len(lst))

lst = []
print(lst)
print(len(lst))

lst = [1]
print(lst)
print(len(lst))

# Accessing List Items Using Indexing
fruits = ['banana', 'orange', 'mango']
print(fruits[0], fruits[-1])

# Checking Items in a List
fruits = ['banana', 'orange', 'mango']
print('banana' in fruits)
print('banana1' in fruits)

# Adding Items to a List
lst = list()
lst.append(1)
lst.append(2)
print(lst)

lst.insert(0, 'insert')
lst.insert(100, 'insert2')
print(lst)

# Removing Items from a List
lst = ['item1', 'item2', 'item3']
lst.remove('item1')
print(lst)

# Removing items Using pop
lst = ['item1', 'item2', 'item3']
lst.pop(0)
print(lst)

# Removing items using Del
lst = ['item1', 'item2', 'item3']
del lst[0]
print(lst)

# Clear List Items
lst = ['item1', 'item2', 'item3']
lst.clear()
print(lst)

# copying a List
lst = ['item1', 'item2', 'item3']
print(lst.copy())

# joining a list using Plus Operator (+)
print([1, 2] + [3, 4])

# joining using extend()
lst1 = ['item1', 'item2']
lst2 = ['item3', 'item4']
lst1.extend(lst2)
print(lst1, lst2)

# Counting Items in a List
lst = ['item1', 'item1', 'item2']
print(lst.count('item1'), lst.count('item2'))

# Finding a Index of an Item
lst = ['item1', 'item2']
print(lst.index('item2'))

# Reversing a List
lst = ['item1', 'item2']
lst.reverse()
print(lst)

# Sorting a List
lst = [1, 2, 3, 4, 5, 6]
lst.sort(reverse=True)
print(lst)