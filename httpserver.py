import http.server
import sys

Handler = http.server.CGIHTTPRequestHandler
PORT = 8002
httpd = http.server.HTTPServer(("", PORT), Handler)
httpd.serve_forever()
print('server is up and running... ')
