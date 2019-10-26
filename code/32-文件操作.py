import os
from pprint import pprint

# 获取指定目录结构
pprint(os.listdir('.'))

# 获取当前所在目录
print(os.getcwd())

# 切换目录 相当于
os.chdir('..')
print(os.getcwd())

# 创建目录
os.mkdir('test-mkdir')

# 删除目录
os.rmdir('test-mkdir')

# 删除文件
# os.remove('file_path')

# 重命名
os.rename('src', 'dst')
