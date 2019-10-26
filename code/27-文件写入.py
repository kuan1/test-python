# 文件写入 以下是mode类型
# r 只读
# w 写入
# a 追加
# x 新建 如果有则报错
# r+ 可读写 如果文件不存在会报错
# a+
file_name = './assets/test2.txt'
with open(file_name, 'r+', encoding='utf-8') as file_obj:
    print(file_obj.read())
    file_obj.write('bbb\n')
    file_obj.write('bbb\n')
    print('成功')
