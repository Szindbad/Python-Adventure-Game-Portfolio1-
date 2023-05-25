import http.server
import socketserver


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/terminal':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Virtual Terminal</h1>')
            self.wfile.write(b'<p>This is a virtual terminal.</p>')
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)


PORT = 8000

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Serving game at http://localhost:8000")
    httpd.serve_forever()
