# 小彭的乱码
import time
from multiprocessing import Process


def output_test():
    while True:
        print('222')
        time.sleep(1)


if __name__ == '__main__':
    process_one = Process(target=output_test)
    process_one.start()
    while True:
        print('111')
        time.sleep(1)
