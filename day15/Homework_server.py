# 小彭的乱码
import sys
from socket import *
server = socket(AF_INET, SOCK_DGRAM)
local_addr = (sys.argv[1], 2000)
server.bind(local_addr)
recv_data = server.recvfrom(200)
print(recv_data[0].decode('utf-8'))
server.sendto('你也好'.encode('utf-8'), recv_data[1])
server.close()