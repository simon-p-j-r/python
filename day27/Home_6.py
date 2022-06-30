# 小彭的乱码
class tes_module:
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('test_call')
        return self.func()


@tes_module
def test_over():
    return 'test'


print(test_over())
