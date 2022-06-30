# 小彭的乱码
import sys
from socket import *

tco_client = socket(AF_INET, SOCK_STREAM)
tcp_addr = (sys.argv[1], 2000)
tco_client.connect(tcp_addr)
tco_client.send(b'hi')
tco_client.close()