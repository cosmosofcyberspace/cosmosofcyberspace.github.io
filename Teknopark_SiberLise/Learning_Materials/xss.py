import threading
import html
from http.server import BaseHTTPRequestHandler, HTTPServer

LHOST = "127.0.0.1"
WEB_PORT = 5006

JS_PAYLOAD = "<script>alert(1)</script>"

class MyHandler(BaseHTTPRequestHandler):


    def do_GET(self):
        if self.path.endswith("/xss_html_encoded.html"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            # XSS Remediation Usage - HTML Encoding
            encoded_payload = html.escape(JS_PAYLOAD)
            self.wfile.write(encoded_payload.encode())



        elif self.path.endswith("/xss_not_html_encoded.html"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            # Vulnerable Usage - raw JS payload
            self.wfile.write(JS_PAYLOAD.encode())
        


        elif self.path.endswith("/xss_content_type_text_html.html"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(JS_PAYLOAD.encode())


        elif self.path.endswith("/xss_content_type_application_json.html"):
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(JS_PAYLOAD.encode())



        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")



def start_web_server():
    httpd = HTTPServer((LHOST, WEB_PORT), MyHandler)
    print(f"[*] Serving on http://{LHOST}:{WEB_PORT}")
    threading.Thread(target=httpd.serve_forever, daemon=True).start()

start_web_server()

# Keep the main thread alive
input("Press Enter to stop the server...\n")
