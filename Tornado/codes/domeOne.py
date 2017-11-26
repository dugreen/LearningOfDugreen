# coding:utf-8

import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    """处理主页"""
    def get(self):
        """get请求方法"""
        self.write('helloworld')

if __name__ == '__main__':
    app = tornado.web.Application([(r'/',IndexHandler)])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
