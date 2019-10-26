file_name1 = './assets/test.txt'
file_name2 = './assets/test2.txt'
file_name3 = './assets/test3.txt'

file_obj1 = open(file_name1)
file_obj2 = open(file_name2)

file_obj3 = open(file_name3, 'w', encoding='utf-8')
file_obj3.write(file_obj1.read() + '\n' + file_obj2.read())

file_obj1.close()
file_obj2.close()
file_obj3.close()
