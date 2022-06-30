# 小彭的乱码
class Printer:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            return cls.instance
        return cls.instance

    def __init__(self, name, page):
        self.name = name
        self.page = page

    def print_state(self):
        print(self.name)
        print(self.page)

printer = Printer("水浒传", 10000)
printer.print_state()
print(printer)
printer2 = Printer("红楼梦", 10000)
printer2.print_state()
print(printer2)