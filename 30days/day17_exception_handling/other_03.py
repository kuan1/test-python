# unpacking list
lst = [1, 2, 3, 4, 5]


def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

print(sum_of_five_nums(*lst))


# packing List

def sum_all(*args):
  s = 0
  for i in args:
    s += i
  return s

print(sum_all(1,2,3))
print(sum_all(1,2,3,4))
print(sum_all(1,2,3,4,5))

# Spreading in Python
lst_one = [1,2,3]
lst_two = [4,5,6]

print([0, *lst_one, *lst_two])

# Enumerate
for i,item in enumerate(['a', 'b', 'c', 'd']):
  print(i, item)

# Zip
lst_x = ['a', 'b', 'c']
lst_y = ['d', 'e', 'f']

for x,y in zip(lst_x, lst_y):
  print({"x": x, "y": y})
