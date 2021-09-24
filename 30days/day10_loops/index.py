# While Loop
i = 1
while i < 5:
  i = i + 1 
  print(i)

# Break and Continue 
i = 1
while i < 5:
  i = i + 1
  if i == 2:
    print('continue', i)
    continue
  if i == 4:
    break
  print(i)

# For Loop
print('\nFor Loop')
numbers = [3,4,5]
for i in numbers:
  print(i)

for i in 'abc':
  print(i)

# Break and Continue - Part 2
print('\nFor Loop')
for i in 'abcdef':
  if i == 'b':
    continue
  if i == 'e':
    break
  print(i)

# Nested For Loop
person = {
  'name': 'luzhongkuan',
  'age': 28,
  'study': 'Python'
}

for i in range(10):
  for key in person:
    print('{name}: {value}'.format(name=key, value=person[key]))

# test loop
for n in range(10):
  str = '#'
  for i in range(n):
    str += '#'
  print(str)