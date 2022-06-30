# 小彭的乱码
class TestMethod:
    """
    sadasdasdasdasdasdasdasdasd
    """
    def __init__(self):
        self.neme = 'simon'
        self.age = 18

    def __call__(self, *args, **kwargs):
        self.age += args[0] + args[1]

    def __del__(self):
        print('哈哈哈')

tsetmethod = TestMethod()
print(tsetmethod.__doc__)
print(TestMethod.__dict__)
print(tsetmethod.__module__)
print(tsetmethod.__class__)
tsetmethod.__call__(1, 2)
print(tsetmethod.age)
