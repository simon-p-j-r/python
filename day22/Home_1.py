# 小彭的乱码
class TestMethod:
    def __init__(self):
        self.__mood = 'sad'

    @property
    def mood(self):
        return self.__mood

    @mood.setter
    def mood(self, food):
        if food == 'cake':
            self.__mood = 'happy'
        if food == 'potato':
            self.__mood = 'sad'

    @mood.deleter
    def mood(self):
        del self.__mood


test_method = TestMethod()
print(test_method.mood)
test_method.mood = 'cake'
print(test_method.mood)
del test_method.mood
print(test_method.mood)
