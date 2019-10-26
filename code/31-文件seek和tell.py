file_name = "./assets/test.txt"

with open(file_name, 'rb') as file_obj:
    # 当前读取位置
    file_obj.seek(5)
    print(file_obj.read(2))
    # 当前读取的位置
    print(file_obj.tell())
