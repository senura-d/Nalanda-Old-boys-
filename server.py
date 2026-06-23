import http.server
import socketserver
import os
import sys

PORT = 3000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve Home.html when root / is requested
        if self.path == '/' or self.path == '':
            self.path = '/Home.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def end_headers(self):
        # Prevent the browser from caching during development so edits always show
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        return http.server.SimpleHTTPRequestHandler.end_headers(self)

# Allow port customization via command line
if len(sys.argv) > 1:
    try:
        PORT = int(sys.argv[1])
    except ValueError:
        pass

socketserver.TCPServer.allow_reuse_address = True
try:
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Serving custom web server on port {PORT}...")
        print(f"URL: http://localhost:{PORT}")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
except Exception as e:
    print(f"Error starting server: {e}")
