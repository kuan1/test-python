class A:
    name = 'AA'

    def __init__(self):
        self.name = "BB"

    def test(self):
        print('test', self.name)

    @classmethod
    def test2(cals):
        print('test2', cals.name)

    @staticmethod
    def test3():
        print('test3')

    def __del__(self):
        print('对象被删除了')


a = A()
a.test()
A.test2()
a.test2()
A.test3()
A = 1
