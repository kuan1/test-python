# Python Closures
def add_ten():
  ten = 10
  def add(num):
    return num + ten
  return add

closure_result = add_ten()

print(closure_result(10))
print(closure_result(20))
