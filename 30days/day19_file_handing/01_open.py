# Opening Files for Reading
#
# Syntax
# open('filename', mode)
# r: Read
# a: Append
# w: Write
# x: Create
# t: Text
# b: Binary 

from os import path

# Open File and Reading
f = open(path.join(path.dirname(__file__), 'temp.txt'))

print(f)
txt = f.read()
print(txt)
print(type(txt))

f.close()