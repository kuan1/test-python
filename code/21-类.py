# class
class People:
    # 自动执行
    def __init__(self, name, age=18, score=100):
        # print(self)  # 当前实例对象
        self.name = name
        self.__age = 18
        self.__score = score

    def say(self, str):
        print(self.name + ':' + str)

    # 隐藏属性
    def get_age(self):
        return self.__age

    # 不可修改
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        print('修改成绩', score)
        self.__score = score


# print(People)
p = People('卢')
# print(isinstance(p, People))
p.say('你好啊')
print(p.score)
p.score = 10

p = People('卢2')
# print(isinstance(p, People))
p.say('你好啊')

print(p.name)

# print(p.__age)
print(p.get_age())

p.__age = 100
print(p.__age)
print(p.get_age())


# 内存回收
class A():
    def __del__(self):
        print('对象被删除了')


def test():
    a = A()
    print('test运行了')


test()
print('结束了')
