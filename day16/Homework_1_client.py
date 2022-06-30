# 小彭的乱码
import sys
from socket import *


tcp_client = socket(AF_INET, SOCK_STREAM)
addr = (sys.argv[1], 2000)
tcp_client.connect(addr)
tcp_client.send(b'hi')
data = tcp_client.recv(100)
print(data)
tcp_client.close()