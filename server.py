#!/usr/bin/python3

import http.server
import socketserver
import io
from src.volume import Volume
import sys
import config

class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_header('Content-type', 'application/json')
        try:
            volumeManagement = Volume(self.path.replace('/', ''))
            self.send_response(200)
            volumeManagement.apply()
        except:
            result = '{"error": "Preset not found"}'
            self.send_response(404)

        self.end_headers()

        self.wfile.write(bytes(result, 'UTF-8'))


print('Server listening on port '+str(config.SERVER_PORT)+'...')
httpd = socketserver.TCPServer(('', config.SERVER_PORT), Handler)
httpd.serve_forever()
