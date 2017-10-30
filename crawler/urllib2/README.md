# urllib2模块使用

#### urllib2_urlopen.py
* 爬取百度首页（直接打开，参数为URL）

#### urllib2_useragent.py
* 爬取百度首页(设置User-Agent)

#### urllib2_add_headers.py
* 爬取百度首页（随机设置User-Agent）

#### urllib2_request.py
* 爬取百度（参数为REQUEST对象）

#### urllib2_get.py      
* 爬取百度关键字搜索页面

#### urllib2_headers.py
* 爬取百度首页（设置User-Agent）

### Handler处理器 和 自定义Opener
* opener是 urllib2.OpenerDirector 的实例，我们之前一直都在使用的urlopen，它是一个特殊的opener（也就是模块帮我们构建好的）。
* 但是基本的urlopen()方法不支持代理、cookie等其他的HTTP/HTTPS高级功能。所以要支持这些功能：
* 使用相关的 Handler处理器 来创建特定功能的处理器对象；
然后通过 urllib2.build_opener()方法使用这些处理器对象，创建自定义opener对象；
* 使用自定义的opener对象，调用open()方法发送请求。
* 如果程序里所有的请求都使用自定义的opener，可以使用urllib2.install_opener() 将自定义的 opener 对象 定义为 全局opener，表示如果之后凡是调用urlopen，都将使用这个opener（根据自己的需求来选择）

### ProxyHandler处理器（代理设置）
* 使用代理IP，这是爬虫/反爬虫的第二大招，通常也是最好用的。
* 很多网站会检测某一段时间某个IP的访问次数(通过流量统计，系统日志等)，如果访问次数多的不像正常人，它会禁止这个IP的访问。
* 所以我们可以设置一些代理服务器，每隔一段时间换一个代理，就算IP被禁止，依然可以换个IP继续爬取。
* urllib2中通过ProxyHandler来设置使用代理服务器，下面代码说明如何使用自定义opener来使用代理：
