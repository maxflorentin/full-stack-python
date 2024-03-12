"""
This module contains the configuration and setup for the HTTP server.
"""

import http.server
import socketserver
import os

DIRECTORY = "./app"
PORT = 8000


class MyHandler(http.server.SimpleHTTPRequestHandler):
    """
    Custom request handler class.
    """

    def translate_path(self, path):
        """
        Translate the given path to the actual file path.
        """
        path = http.server.SimpleHTTPRequestHandler.translate_path(self, path)
        abs_directory = os.path.abspath(DIRECTORY)
        if not path.startswith(abs_directory):
            return (
                os.path.join(abs_directory, "index.html")
                if os.path.exists(os.path.join(abs_directory, "index.html"))
                else ""
            )
        return path


with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Server running on port {PORT}")
    httpd.serve_forever()
