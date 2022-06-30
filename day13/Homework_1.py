# 小彭的乱码
import random


class Bisearch:
    def __init__(self):
        self.info_list = [1, 2, 3, 5, 9, 56, 66]
        self.length = 7

    def test_ranging(self, way, *args, **kwargs):
        print(self.info_list)
        way(*args, **kwargs)
        print(self.info_list)

    def bi_search(self, target):
        low = 0
        high = self.length - 1
        info_list = self.info_list
        while low <= high:
            mid = (low + high) // 2
            if info_list[mid] > target:
                high = mid - 1
            elif info_list[mid] < target:
                low = mid + 1
            else:
                print(mid)
                break


list1 = Bisearch()
list1.test_ranging(list1.bi_search, 66)
