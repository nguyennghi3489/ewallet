from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
import os
from config.api import HOST_NAME, PORT, BASE_PATH
from api_routes import route_mapper

class EWalletRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self._handle_request()

    def do_POST(self):
        self._handle_request()

    def _handle_request(self):
        try:
            route = route_mapper.match(self.path)
            if (route is None):
                return
            controller = route.get('controller', None)
            if (controller is None):
                return
            _req = self
            _req.route = route
            controller(_req)
        except Exception as e:
            print(f"Unexpected {e=}, {type(e)=}")
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'msg': e.__str__()}).encode())

def startServer():
    appServer = HTTPServer((HOST_NAME, PORT), EWalletRequestHandler)
    print(time.asctime(), "Start Server - %s:%s" % (HOST_NAME, PORT))

    try:
        appServer.serve_forever()
    except Exception as e:
        print(f"Unexpected {e=}, {type(e)=}")

    print(time.asctime(), 'Stop Server - %s:%s' % (HOST_NAME, PORT))
