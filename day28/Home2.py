# 小彭的乱码
def orange(self):
    print("orange's color is orange")


class Fruit:
    def output_fruit(self):
        print("Fruit have apple and orange")


Food = type('Food', (Fruit,), {'apple': 'tasty', 'orange': orange})
food = Food()
food.orange()
food.output_fruit()
print(food.apple)
