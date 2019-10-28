'''
输入年份 返回True 或者 False
'''

year = int(input('请输入年份：'))

is_leap = (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

print('瑞年' if is_leap else '不是瑞年')
