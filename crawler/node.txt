
网页三大特性：
1.唯一的URL（统一资源定位符）
2.都使用HTML（超文本标记语言）来描述页面信息
3.网页都使用HTTP/HTTPS（超文本传输协议）协议来传输HTML数据

爬虫设计思路
1.首先确定要爬取的URL地址
2.通过HTTP/HTTPS协议来获取对应的HTML页面
3.提取HTML页面里有用的数据

如何抓取HTML页面
	HTTP请求的处理：urllib urllib2 requests
	处理后的请求可以模拟浏览器发送请求，获取服务器响应的文件

解析服务器相应的内容
re xpath BeautifulSoup4(bs4) jsonpath pyquery

采集动态HTML，验证码的处理
	通用的动态页面采集 Selenium PhantomJS（无界面）

Scrapy框架
	高可定制性 高性能（异步网络框架twisted),数据下载快

通用爬虫  聚焦爬虫
通用爬虫：搜索引擎用的爬虫系统
聚焦爬虫：爬虫程序员写的针对某种内容爬虫

搜索爬虫排名
	PageRang值
	竞价排名


















