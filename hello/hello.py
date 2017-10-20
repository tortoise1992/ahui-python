

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import options,define

define('port',default=3000,help="run on the given port",type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        greeting=self.get_argument('greeting','hello')
        self.write(greeting+',welcome you to reed:ahui')

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app=tornado.web.Application(handlers=[(r"/",IndexHandler)])
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()