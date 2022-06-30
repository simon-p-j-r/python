# 小彭的乱码
import re

info_list = ['http://www.interoem.com/messageinfo.asp?id=35',
             'http://3995503.com/class/class09/news_show.asp?id=14',
             'http://lib.wzmc.edu.cn/news/onews.asp?id=769',
             'http://www.zy-ls.com/alfx.asp?newsid=377&id=6',
             'http://www.fincm.com/newslist.asp?id=415'
             ]
for num in info_list:
    ret = re.sub(r'http://', '', num)
    ret = re.match(r'([^/]+)', ret)
    print(ret.group())