from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

HOST = "localhost"
PORT = 8080
TEMPLATES_DIR = Path("templates")
CONTACTS_FILE = TEMPLATES_DIR / "contacts.html"


class App(BaseHTTPRequestHandler):
    def do_GET(self):
        """Отдаём всегда contacts.html с корректным Content-Type."""
        try:
            html = CONTACTS_FILE.read_text(encoding="utf-8")
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        except FileNotFoundError:
            self.send_response(500)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"contacts.html not found")


if __name__ == "__main__":
    httpd = HTTPServer((HOST, PORT), App)
    print(f"Server started: http://{HOST}:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print("Server stopped.")
