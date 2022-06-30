# 小彭的乱码
import random


class tanking:
    def __init__(self, length):
        self.info_list = [random.randint(0, 10) for i in range(length)]
        self.length = length
        self.info_help = [0] * length

    def merge_adjust_ranking(self, low, high):
        list1 = self.info_list
        info_list_help = self.info_help
        for num in range(low, high + 1):
            info_list_help[num] = list1[num]
        mid = (low + high) // 2
        tag_mid = mid+1
        tag_low = low
        tag = low
        while tag_low <= mid and tag_mid <= high:
            if info_list_help[tag_low] < info_list_help[tag_mid]:
                list1[tag] = info_list_help[tag_low]
                tag_low += 1
                tag += 1
            else:
                list1[tag] = info_list_help[tag_mid]
                tag_mid += 1
                tag += 1
        while tag_low <= mid:
            list1[tag] = info_list_help[tag_low]
            tag_low += 1
            tag += 1
        while tag_mid <= high:
            list1[tag] = info_list_help[tag_mid]
            tag_mid += 1
            tag += 1
        print(info_list_help)

    def merge_ranking(self, low, high):
        if low < high:
            mid = (high + low) // 2
            self.merge_ranking(low, mid)
            self.merge_ranking(mid + 1, high)
            self.merge_adjust_ranking(low, high)

    def num_ranking(self, top):
        list1 = [0] * top
        for num in self.info_list:
            list1[num] += 1
        tag = 0
        i = 0
        print(list1)
        for num in list1:
            while num > 0:
                self.info_list[i] = tag
                i += 1
                num -= 1
            tag += 1

    def test_ranging(self, way, *args, **kwargs):
        print(self.info_list)
        way(*args, **kwargs)
        print(self.info_list)


info_list = tanking(9)
# info_list.test_ranging(info_list.merge_ranking, 0, info_list.length - 1)
info_list.test_ranging(info_list.num_ranking, 10)
