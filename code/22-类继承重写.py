class Animal:
    def __init__(self, name='动物'):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def run(self):
        print('奔跑')

    def sleep(self):
        print('睡觉')


a = Animal()
a.run()


# 继承
class Dog(Animal):
    def __init__(self, name='小狗'):
        # 不需要传递self
        super().__init__(name)

    # 魔法函数
    def __len__(self):
        return 10

    # 重写
    def sleep(self):
        print('小狗在睡觉')

    def bark(self):
        print("吼叫")


d = Dog()
d.sleep()
d.bark()
print(d.name)
print(len(d))

print(isinstance(d, Dog))
print(isinstance(d, Animal))
print(issubclass(Dog, Animal))
