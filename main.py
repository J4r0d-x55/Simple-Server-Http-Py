from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = "your ipv4"
PORT = "port"

class SimpleHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>SERVER</h1></body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strtime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"Date et heure": "' + date + '"}', "utf-8"))

server = HTTPServer((HOST, PORT), SimpleHTTP)
print("Serveur en cours...")

server.serve_forever()
server.server_close()
print("Arrêt du serveur")
