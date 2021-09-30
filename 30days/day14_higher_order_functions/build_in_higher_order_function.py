from functools import reduce
numbers = [1, 2, 3, 4, 5, 6]

# map
print(list(map(lambda x: 2 * x, numbers)))

# filter
print(list(filter(lambda x: x % 2, numbers)))
print([x for x in numbers if x % 2])

# reduce
print(reduce(lambda x, y: x + y, numbers))