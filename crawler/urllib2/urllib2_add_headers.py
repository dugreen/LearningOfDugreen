#!coding:utf-8
import urllib2
import random

url = "http://www.itcast.cn"

ua_list = [
            "Mozilla/5.0 (Windows NT 6.1; ) Apple.... ",
                "Mozilla/5.0 (X11; CrOS i686 2268.111.0)... ",
                    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X.... ",
                        "Mozilla/5.0 (Macintosh; Intel Mac OS... "
                        ]

user_agent = random.choice(ua_list)

request = urllib2.Request(url)

#也可以通过调用Request.add_header() 添加/修改一个特定的header
request.add_header("User-Agent", user_agent)

# 第一个字母大写，后面的全部小写
request.get_header("User-agent")

response = urllib2.urlopen(request)

html = response.read()
print html

