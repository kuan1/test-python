# 读取二进制文件

file_name = '/Users/kuan/Desktop/设计稿/01登录.psd'

with open(file_name, 'rb') as file_obj:
    while True:
        content = file_obj.read(100)
        if not content:
            break
        print(content)
