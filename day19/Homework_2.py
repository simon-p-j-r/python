# 小彭的乱码
import threading

num = 0
mutex1 = 0
mutex2 = 1


def add_num(lock):
    global num
    global mutex1
    global mutex2
    tag = 0
    while tag < 10000000:
        if mutex1 == 0 and mutex2 == 1:
            mutex1 = 1
            mutex2 = 0
            lock.acquire()
            num += 1
            lock.release()
            print(num)
            tag += 1


def add_num1(lock):
    global num
    global mutex1
    global mutex2
    tag = 0
    while tag < 10000000:
        if mutex1 == 1 and mutex2 == 0:
            mutex1 = 0
            mutex2 = 1
            lock.acquire()
            num += 1
            lock.release()
            print(num)
            tag += 1


if __name__ == '__main__':
    lock = threading.Lock()
    ti = threading.Thread(target=add_num, args=(lock,))
    t2 = threading.Thread(target=add_num, args=(lock,))
    ti.start()
    t2.start()
    ti.join()
    t2.join()
    print(num)
