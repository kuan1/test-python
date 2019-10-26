# 文件(File) I/O(input/output)

# 步骤 打开文件 -> 修改文件 -> 关闭文件

file_name = 'assets/test.txt'

# 打开文件
file_obj = open(file_name)

print(file_obj)

# 关闭文件
file_obj.close()

# with操作之后会自动关闭
with open(file_name) as file_obj:
    print(file_obj.read())
