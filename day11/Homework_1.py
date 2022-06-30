# 小彭的乱码
class circle_queue():
    def __init__(self, length):
        self.length = length + 1
        self.queue_test = [0] * self.length
        self.front = 0
        self.rear = 0

    def enqueue(self, num):
        if (self.rear + 1) % self.length == self.front:
            print('满了')
        else:
            self.queue_test[self.rear] = num
            self.rear = (self.rear + 1) % self.length

    def dequeue(self):
        if self.front == self.rear:
            print('空的')
        else:
            self.queue_test.pop(self.front)
            self.front = (self.front + 1) % self.length


    def gettop(self):
        if self.front == self.rear:
            print('空的')
        else:
            return self.queue_test[self.rear]


info_queue = circle_queue(5)
for num in range(5, 0, -1):
    info_queue.enqueue(num)
print(info_queue.queue_test)