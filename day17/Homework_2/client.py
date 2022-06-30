# 小彭的乱码
import struct
import sys
from socket import *
file_client = socket(AF_INET,SOCK_STREAM)
file_addr = ('192.168.3.144', 2000)
file_client.connect(file_addr)
length = file_client.recv(4)
file_name = file_client.recv(struct.unpack('I', length)[0])
file = open(file_name.decode('utf-8') + 'copy', 'wb')
file_length = file_client.recv(4)
text = file_client.recv(struct.unpack('I', file_length)[0])
file.write(text)
file.close()
file_client.close()
