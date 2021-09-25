import random
# Declaring and Calling a Function

def test_fn():
  print(1)

test_fn()
test_fn()

# Function without Parameters

def generate_full_name():
  first_name = 'first_name'
  last_name = 'last_name'
  full_name = first_name + last_name
  print(full_name)

generate_full_name()

# Function Returning a Value - Part 1

def get_num():
  return random.randint(10, 20)

print(get_num())

# Function with Parameters

def sum(a, b):
  return a + b

print(sum(1, 2))

# Passing Arguments with Key and Value
def sum(a = 1, b = 2):
  return a + b

print(sum(a = 2, b = 4))
print(sum(b = 4))

# Arbitrary Number of Arguments
def sum(*numbers):
  print(numbers)
  total = 0
  for num in numbers:
    total += num
  return total

print(sum(1,2,3,4))

def reverse_list(lst = []):
  lst2 = []
  for item in lst:
    lst2.insert(0, item)
  return lst2

print(reverse_list([1,2,3]))
