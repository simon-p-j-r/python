# 小彭的乱码
from pymysql import *

con = connect(host='192.168.28.128', user='root', password='123',
              database='demo1', charset='utf8')
cs1 = con.cursor()
# mysql_str = 'insert into students values (5, "rose", 18, 180, 1, 1, 0)'
# count = cs1.execute(mysql_str)
# print(count)
# con.commit()

# mysql_str ='delete from students where id = 5'
# count = cs1.execute(mysql_str)
# print(count)
# con.commit()

# mysql_str = 'update students set id = 123 where id = 321'
# count = cs1.execute(mysql_str)
# print(count)
# con.commit()

mysql_str = 'select * from students'
count = cs1.execute(mysql_str)
for i in range(count):
    print(cs1.fetchone())
print(count)
con.commit()
cs1.close()
con.close()