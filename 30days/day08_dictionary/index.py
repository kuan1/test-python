# Creating a Dictionary
empty_dict = {}
empty_dict = dict()
print(empty_dict)

# Dictionary Length
dct = {'a': 1, 'b': 2, 'c': 3}
print(len(dct))

# Accessing Dictionary Items
dct = {'a': 1, 'b': 2, 'c': 3}
print(dct['a'])

# Adding items to a Dictionary
dct = {'a': 1, 'b': 2, 'c': 3}
dct['d'] = 4
print(dct)

# Checking Keys in Dictionary
dct = {'a': 1, 'b': 2, 'c': 3}
print('a' in dct)
print('aa' in dct)

# Removing Key and Value Pairs from a Dictionary
dct = {'a': 1, 'b': 2, 'c': 3}
dct.pop('a')
print(dct)
dct.popitem()
print(dct)

# Changing Dictionary to a List of Items
dct = {'a': 1, 'b': 2, 'c': 3}
print(dct.items())

# Clearing a Dictionary
dct = {'a': 1, 'b': 2, 'c': 3}
dct.clear()
print(dct)

# Copy a Dictionary
dct = {'a': 1, 'b': 2, 'c': 3}
print(dct.copy())

# Getting Dictionary Keys as a List
dct = {'a': 1, 'b': 2, 'c': 3}
print(dct.keys())

# Getting Dictionary Values as a List
dct = {'a': 1, 'b': 2, 'c': 3}
print(dct.values())