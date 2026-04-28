import http.server, socketserver

PORT = 3000
ROOT = "/Users/reubenpoole/Documents/GitHub/My-Portfolio-ReubenPoole"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
