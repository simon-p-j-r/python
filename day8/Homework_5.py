# 小彭的乱码
class Appliance:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return '家具的名字是%s,占地面积%d' % (self.name, self.area)


class House:
    def __init__(self, house_type, area, free_area, item_list):
        self.house_type = house_type
        self.area = area
        self.free_area = free_area
        self.item_list = item_list

    def __str__(self):
        return "房子类型是%s,总面积为%d,剩余面积为%d" % (self.house_type, self.area, self.free_area)

    def add_item(self, item:Appliance):
        if item.area < self.free_area :
            self.free_area -= item.area
            self.item_list.append(item)
            print('已添加', end='')
            print(item, end=',')
            print(self)
        else:
            print('满了')


Tv = Appliance('Tv', 2)
print(Tv)
info_list = []
my_home = House("大平层", 200, 1, info_list)
print(my_home)
my_home.add_item(Tv)
