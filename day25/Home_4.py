# 小彭的乱码
from pymysql import *
con = connect(host='192.168.28.128', user='root', password='123',
              database='demo1', charset='utf8')
cl1 = con.cursor();
for i in range(6,100000):
    mysql_str = "insert into classes(name) value ('当前为%d')"%i
    count = cl1.execute(mysql_str)
con.commit()
cl1.close()
con.close()
