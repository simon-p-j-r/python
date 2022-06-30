# 小彭的乱码
class Test:
    def __init__(self, num, tag):
        self.num = num
        self.__tag = tag
        # self.__test()

    def __test(self):
        self.__tag = 5
        print(self.__tag)


test = Test(20, 18)
print(test.num)