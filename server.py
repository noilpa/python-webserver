import os

from http.server import BaseHTTPRequestHandler

from routes.main import routes

from response.staticHandler import StaticHandler
from response.templateHandler import TemplateHandler
from response.badRequestHandler import BadRequestHandler
from response.testHandler import TestHandler


class Server(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/api/createPoll/":
            msg = "create poll"
            print(msg)
            handler = TestHandler(msg)
        elif self.path == "/api/poll/":
            msg = "poll vote"
            print(msg)
            handler = TestHandler(msg)
        elif self.path == "/api/getResult/":
            msg = "poll result"
            print(msg)
            handler = TestHandler(msg)
        else:
            print("no such route")
            handler = BadRequestHandler()

        self.respond({
            'handler': handler
        })

    def handle_http(self, handler):
        status_code = handler.getStatus()

        self.send_response(status_code)

        if status_code is 200:
            content = handler.getContents()
            self.send_header('Content-type', handler.getContentType())
        else:
            content = "404 Not Found"

        self.end_headers()

        return bytes(content, 'UTF-8')

    def respond(self, opts):
        response = self.handle_http(opts['handler'])
        self.wfile.write(response)
