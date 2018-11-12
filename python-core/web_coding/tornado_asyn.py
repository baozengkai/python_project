# -*- coding:utf-8 -*-
import tornado.web
import tornado.options
import tornado.ioloop
from tornado import gen
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
import time

"""
    Tornado具备有异步非阻塞的能力
        1.使用@gen.coroutine和yield组合可以实现异步非阻塞
          但是需要所作用的函数支持异步，如果不支持异步，那么还是异步阻塞
        2.可以使用ThreadPoolExecutor来实现线程池(在python3中自带，在python2中需安装pip install futures)
"""
# 1.使用@gen.coroutine和yield实现异步非阻塞
# class TestHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("I am hello")

# class BlockingHandler(tornado.web.RequestHandler):
#     def get(self):
#         time.sleep(10)
#         self.write("I am block")

# class NoBlockingHandler(tornado.web.RequestHandler):
#     @gen.coroutine
#     def get(self):
#         yield gen.sleep(10)
#         self.write("I am noBlock")

# 2.使用ThreadPoolExecutor实现线程池来处理阻塞模块变为非阻塞
class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("I am hello")

class NoBlockingHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(1)

    @run_on_executor
    def sleep(self,second):
        time.sleep(second)
        return second

    @gen.coroutine
    def get(self):
        second = yield self.sleep(8)
        self.write("I am noBlock")


def app_route():
    return tornado.web.Application([
        (r"/", TestHandler),
        (r"/noblock", NoBlockingHandler)
    ])

if __name__ == "__main__":
    app = app_route()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
