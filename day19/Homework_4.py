# 小彭的乱码
class MyIterable:
    def __init__(self, mylist):
        self.mylist = mylist
        self.current = 0

    def __next__(self):
        if self.current < len(self.mylist.info_list):
            data = self.mylist.info_list[self.current]
            self.current += 1
            return data
        else:
            raise StopIteration

    def __iter__(self):
        return self


class Mylist:
    def __init__(self):
        self.info_list = []

    def addnum(self, num):
        self.info_list.append(num)

    def __iter__(self):
        myiterable = MyIterable(self)
        return myiterable


info_iterator = Mylist()
info_iterator.addnum(1)
info_iterator.addnum(2)
for i in info_iterator:
    print(i)
