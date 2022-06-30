# 小彭的乱码
class Parent:
    def __init__(self, name, *args, **kwargs):
        print('parent')
        self.name = name
        print('Parent')


class Som1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        print('son1')
        self.age = age
        super().__init__(name, *args, **kwargs)
        print('Son1')


class Som2(Parent):
    def __init__(self, name, gender, *args, **kwargs):
        print('son2')
        self.gender = gender
        super().__init__(name, *args, **kwargs)
        print('Son2')

class Grandson(Som1, Som2):
    def __init__(self, name, age, gender, *args, **kwargs):
        print('grandson')
        super(Grandson, self).__init__(name, age, gender, *args, **kwargs)
        print('Grandson')
grandson = Grandson('simon', 18, 'famale')
print(grandson.name,grandson.age,grandson.gender)
