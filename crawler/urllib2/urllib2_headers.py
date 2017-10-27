#!/usr/bin/env python
#!coding:utf-8

import urllib2

url = "http://www.itcast.cn"

#IE 9.0 的 User-Agent
header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"} 
request = urllib2.Request(url, headers = header)

#也可以通过调用Request.add_header() 添加/修改一个特定的header
request.add_header("Connection", "keep-alive")

# 也可以通过调用Request.get_header()来查看header信息
# request.get_header(header_name="Connection")

response = urllib2.urlopen(req)

print response.code     #可以查看响应状态码
html = response.read()

print html
