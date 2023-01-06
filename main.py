# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import time, os

hostName = "0.0.0.0"
serverPort = 8080
ha_webhook = os.environ['HA_WEBHOOK']

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        data = requests.post(ha_webhook, timeout=5)
        if data.status_code == 200:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Plex Server</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<h1>Befehl zum Starten wurde gesendet.</h1>", "utf-8"))
            self.wfile.write(bytes("<h1>Plex sollte in ca. 4Min verfuegbar sein.</h1>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        else:
            self.send_response(500)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Plex Server</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>Es gab einen Fehler beim Senden des Befehls.</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")