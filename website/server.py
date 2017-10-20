import tornado.ioloop
import tornado.options
import tornado.httpserver

from website.app import application

from tornado.options import define,options


define("port",default=3000,help="run on",type=int)

def main():
    tornado.options.parse_command_line()
    http_server=tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)

    print ("server is run" )
    print("quit the server with control-c")
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()