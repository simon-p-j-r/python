# 小彭的乱码
import os
import sys


def depth_list(path_name, depth):
    file_name = os.listdir(path_name)
    for i in file_name:
        print(' ' * depth*4 + i)
        current_path = path_name + '/' + i
        if os.path.isdir(current_path):
            depth += 1
            depth_list(current_path, depth)


# if __name__ == '__main__':
depth_list(sys.argv[1], 0)
