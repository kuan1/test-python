from os import path, remove
temp_path = path.join(path.dirname(__file__), 'temp2.txt')

if path.exists(temp_path):
  remove(temp_path)
  print(f'删除{temp_path}成功')
else:
  print(f'{temp_path} does not exist')
  