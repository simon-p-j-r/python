# 小彭的乱码
class Test:
    num = 0

    @staticmethod
    def printf_method():
        print('欢迎来到小彭工具房')

    @classmethod
    def print_num(cls):
        print(cls.num)

    def __init__(self, name):
        self.name = name


Test.num += 1
Test.print_num()


test = Test('cup')