# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

from tornado.options import define,options
from tornado.web import RequestHandler,url

tornado.options.define("port",type=int,default=8888,help="服务器窗口")

class IndexHandler(RequestHandler):
    def get(self):
        self.write('<a href="'+self.reverse_url("cpp_url")+'">cpp</a,,,>')

class SubjectHandler(RequestHandler):
    def initialize(self,subject):
        self.subject = subject
    def get(self):
        self.write(self.subject)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [(r"/",IndexHandler),
        (r"python",SubjectHandler,{"subject":"python"}),
        url(r"/app",SubjectHandler,{"subject":"cpp"},name="cpp_url")
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
