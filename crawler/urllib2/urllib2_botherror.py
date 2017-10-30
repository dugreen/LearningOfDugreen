#coding:utf-8

"""
异常处理:
    首先捕获子类的异常，如果子类捕获不到，那么可以捕获父类的异常。
"""
import urllib2

requset = urllib2.Request('http://blog.baidu.com/itcast')

try:
    urllib2.urlopen(requset)

except urllib2.HTTPError, err:
    print err.code

except urllib2.URLError, err:
    print err

else:
    print "Good Job"
