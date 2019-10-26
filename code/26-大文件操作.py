# 文件操作
file_name = 'assets/test.txt'

# read可以传入读取字符的数量，再次调用会继续读取下边的文件
try:
    with open(file_name, encoding='utf-8') as file_obj:
        chunk = 1
        while True:
            content = file_obj.read(chunk)
            if not content:
                break
            else:
                print(content, end='')
except Exception as e:
    print(e)
