# 小彭的乱码
class TestOne:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __printf_age(self):
        print(self.__age)

    def printf_name(self):
        print(self.name + ' One')


class TestTwo:
    def __init__(self, name, hobby):
        self.name = name
        self.hobby = hobby

    def printf_name(self):
        print(self.name + ' Two')

    def printf_hobby(self):
        print(self.hobby)


class Test(TestOne, TestTwo):
    # def __init__(self, name, age, hobby):
    #     self.name = name
    #     self.age = age
    #     self.hobby =hobby

    def printf_hobby(self):
        super(Test, self).printf_hobby()
        print("addtional")


test1 = Test('pengjiaren', 18)
test1.hobby = '台球'
test1.printf_hobby()
test1.printf_name()

# 在多继承中，在子类申明对象时赋值，pycharm只联想了第一个父类init所需值，强写赋值其它父类init里的值报错。那其它父类到底该怎么赋值呢
# 直接变量.属性赋值就行