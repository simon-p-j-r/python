# 小彭的乱码
import socket
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest_addr = (sys.argv[1], 2000)
client.sendto('你好'.encode('utf-8'), dest_addr)
recv_data = client.recvfrom(100)
print(recv_data[0].decode('utf-8'))
client.close()
