# 小彭的乱码
import random


class ranking():
    def __init__(self, length):
        self.info_list = [random.randint(0, 9) for i in range(0, length)]
        self.length = length

    def bubble_ranking(self):
        tag = 0
        i = self.length - 1
        while i > 0:
            j = 0
            while j < i:
                if self.info_list[j] > self.info_list[j + 1]:
                    self.info_list[j], self.info_list[j + 1] = self.info_list[j + 1], self.info_list[j]
                    tag = 1
                j += 1
            if tag == 0:
                break
            i -= 1

    def selection_ranking(self):
        min_posi = 0
        min_num = self.info_list[0]
        min_index = 0
        i = 0
        while i < self.length - 1:
            j = min_posi
            min_num = self.info_list[min_posi]
            while j < self.length:
                if self.info_list[j] < min_num:
                    min_num = self.info_list[j]
                    min_index = j
                j += 1
            self.info_list[min_index], self.info_list[min_posi] = self.info_list[min_posi], self.info_list[min_index]
            min_posi += 1
            i += 1

    def insert_ranking(self):
        i = 1
        while i < self.length:
            j = i - 1
            num = self.info_list[i]
            while self.info_list[j] < num:
                self.info_list[j + 1] = self.info_list[j]
                if j == 0:
                    break
                j -= 1
            self.info_list[j] = num
            i += 1

    def take_num(self, low, high):
        tag = self.info_list[low]
        while low < high:
            while (low < high) & (self.info_list[high] > tag):
                high -= 1
            self.info_list[low] = self.info_list[high]
            while (low < high) & (self.info_list[low] <= tag):
                low += 1
            self.info_list[high] = self.info_list[low]
        self.info_list[low] = tag
        return low

    def quick_ranking(self, low, high):
        if low < high:
            mid = self.take_num(low, high)
            self.quick_ranking(low, mid - 1)
            self.quick_ranking(mid + 1, high)

    def adjust_max_heap(self, pos, len):
        dad = pos
        son = 2 * dad + 1
        while son < len:
            if son + 1 < len and self.info_list[son] < self.info_list[son + 1]:
                son += 1
            if self.info_list[son] > self.info_list[dad]:
                self.info_list[son], self.info_list[dad] = self.info_list[dad], self.info_list[son]
                dad = son
                son = dad * 2 + 1
            else:
                break

    def heap_ranking(self):
        arr = self.info_list
        for i in range(self.length // 2 - 1, -1, -1):
            self.adjust_max_heap(i, self.length)
        for i in range(self.length - 1, -1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.adjust_max_heap(0, i)

    def test_ranking(self, ranking, *args, **kwargs):
        print(self.info_list)
        ranking(*args, **kwargs)
        print(self.info_list)


list1 = ranking(8)
list1.test_ranking(list1.heap_ranking)
