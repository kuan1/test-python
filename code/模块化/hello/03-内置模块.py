# 系统模块
import sys
# 访问操作系统
import os
from pprint import pprint

# print(sys)
# 参数
print(sys.argv)


# 所有模块
# print(sys.modules)
# pprint(sys.modules)

# sys.path: 所有模块路径
# pprint(sys.path)


# sys.platform: 系统
# print(sys.platform)


# sys.exit：程序结束
# sys.exit('程序异常结束')
# print('测试')

# os
print(os)

# 查看环境变量
pprint(os.environ['HOME'])

# 执行操作系统
r = os.system("ls")
print(type(r))
