# Creating Decorator 
def greeting():
  return 'Welcome To Python'

def uppercase_decorator(function):
  def wrapper():
    res = function()
    make_uppercase = res.upper()
    return make_uppercase
  return wrapper

g = uppercase_decorator(greeting)
print(g())

def split_string_decorator(function):
  def wrapper():
    return function().split()
  return wrapper

# Multiple Decorators 
@split_string_decorator
@uppercase_decorator
def greeting2():
  return 'Welcome To Python'

print(greeting2())