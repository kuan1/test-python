from os import path

temp_path = path.join(path.dirname(__file__), 'temp.txt')

# readline
f = open(temp_path)
line = f.readline()
print(type(line))
print(line)
f.close()

# readlines
f = open(temp_path)
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
