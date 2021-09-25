# syntax
# [i for i in iterable if expression]
print([i for i in range(10) if i % 2])

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([number for row in list_of_lists for number in row])

# Creating a Lambda Function
print((lambda param1, params2, param3: param1 + params2 + param3)(1, 2, 3))

# Lambda Function Inside Another Function


def pow(x):
    return lambda n: x ** n
print(pow(2)(3))