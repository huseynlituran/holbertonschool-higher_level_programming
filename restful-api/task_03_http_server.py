#!/usr/bin/python3
"""
A simple HTTP server using the http.server module.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    This class handles HTTP requests.
    """

    def do_GET(self):
        """
        Handles GET requests and serves data based on the path.
        """
        # Root endpoint
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # Data endpoint (JSON)
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            # Dictionary-ni JSON stringinə çeviririk və encode edirik
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # Status endpoint
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        # Handle 404 Not Found
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    """
    Starts the HTTP server on port 8000.
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Starting server on port 8000...")
    httpd.serve_forever()
