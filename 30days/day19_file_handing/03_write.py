from os import path
temp_path = path.join(path.dirname(__file__), 'temp2.txt')

with open(temp_path, 'w') as f:
  f.write('hello write file\n')

with open(temp_path, 'a') as f:
  f.write('hello append file\n')
