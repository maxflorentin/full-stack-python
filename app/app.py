import http.server
import socketserver
import os

directory = "./app"
port = 8000
handler = http.server.SimpleHTTPRequestHandler


class MyHandler(handler):
    def translate_path(self, path):
        path = http.server.SimpleHTTPRequestHandler.translate_path(self, path)
        abs_directory = os.path.abspath(directory)
        if not path.startswith(abs_directory):
            return (
                os.path.join(abs_directory, "index.html")
                if os.path.exists(os.path.join(abs_directory, "index.html"))
                else ""
            )
        return path


with socketserver.TCPServer(("", port), MyHandler) as httpd:
    print(f"Server running on port {port}")
    httpd.serve_forever()
