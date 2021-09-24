# Accessing Characters in Strings by Index
print('Python'[2])

# Slicing Python Strings
print('Python'[0:2])
print('Python'[-3:])
print('Python'[1:])

# Reversing a String
print('Python'[::-1])

# Skipping Characters While Slicing
print('Python'[0::2])

# capitalize
print('python'.capitalize())

# count
print('python python'.count('p'))

# endswith
print('Python'.endswith('on'))

# startswith
print('Python'.startswith('P'))

# find
print('thirty days of python'.find('y')) # 5
print('thirty days of python'.find('th')) # 0
print('a'.find('b'))

# rfind
print('thirty days of python'.rfind('y'))  # 16
print('thirty days of python'.rfind('th')) # 17

# index
print('abc'.index('a'))
print('abc'.index('c'))
# print('abc'.index('d'))

# join
print('|'.join(["a", "b", "c"]))

# split
print('1,2,3,4'.split(','))
print(type('1,2,3,4'.split(',')))