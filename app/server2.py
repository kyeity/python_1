from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from http import HTTPStatus
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class HttpGetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        #self.send_header("Content-type", "text-html; charset=utf-8")
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        #self.wfile.write(open(dir_path + '/templates/home.html', 'r').read().encode())
        self.wfile.write(json.dumps({'server_name': 'Simple HTTP server', 'author': 'Dima Korablov'}).encode())


    def do_POST(self):
        if self.path == '/v1/a':
            self.post_a()
        elif self.path == '/v1/b':
            self.post_b()
        else:
            self.send_error(HTTPStatus.NOT_IMPLEMENTED, 'Wrong path')


    def post_a(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(
            json.dumps({'server_name': 'Simple HTTP server', 'author': 'Dima Korablov', 'path': self.path,
                        'method': self.command, 'func': 'post_a'}).encode())

    def post_b(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(
            json.dumps({'server_name': 'Simple HTTP server', 'author': 'Dima Korablov', 'path': self.path,
                        'method': self.command, 'func': 'post_b'}).encode())

def run(server_class=HTTPServer, handler_class=HttpGetHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

if __name__ == '__main__':
    run()