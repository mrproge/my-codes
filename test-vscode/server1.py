# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from http.server import HTTPServer, BaseHTTPRequestHandler

hostName = "localhost"
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_Get(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://testserver.com</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    webserver = HTTPServer((hostName, serverPort), MyServer)
    print("server started http://%s:%s" % (hostName, serverPort))
    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass
    webserver.server_close()
    print("Server stopped.")