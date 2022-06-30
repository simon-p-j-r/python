# 小彭的乱码
import re
email_list = ["xiaoWang@163.com","xiao.Wang@163.com",
              "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
for num in email_list:
    ret = re.sub(r'\w+@163\.com$', '1354527247@qq.com', num)
    print(ret)