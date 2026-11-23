"""Local-only, single-request playground. No non-container fallback."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from pathlib import Path
import argparse

from playground.sandbox import MAX_SOURCE, ready, run

STATIC = Path(__file__).parent / 'static'
FILES = {'/': ('index.html', 'text/html; charset=utf-8'),
         '/app.js': ('app.js', 'application/javascript; charset=utf-8'),
         '/style.css': ('style.css', 'text/css; charset=utf-8')}


class Handler(BaseHTTPRequestHandler):
    def setup(self):
        super().setup()
        self.connection.settimeout(10)

    def send(self, status, body, content_type='application/json; charset=utf-8'):
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; frame-ancestors 'none'; base-uri 'none'")
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def valid_host(self):
        return self.headers.get('Host') == f'127.0.0.1:{self.server.server_port}'

    def do_GET(self):
        if not self.valid_host():
            return self.send(403, b'{}')
        item = FILES.get(self.path)
        if not item:
            return self.send(404, b'{}')
        filename, content_type = item
        self.send(200, (STATIC / filename).read_bytes(), content_type)

    def do_POST(self):
        expected_origin = f'http://127.0.0.1:{self.server.server_port}'
        if not self.valid_host() or self.headers.get('Origin') != expected_origin:
            return self.send(403, b'{}')
        if self.path != '/run':
            return self.send(404, b'{}')
        if self.headers.get('Content-Type') != 'application/json':
            return self.send(415, b'{}')
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if not 0 < length <= MAX_SOURCE * 6 + 100:
                return self.send(413, b'{}')
            payload = json.loads(self.rfile.read(length))
            source = payload['source']
            if not isinstance(source, str) or len(source.encode('utf-8')) > MAX_SOURCE:
                return self.send(413, b'{}')
            result = run(source)
            self.send(200, json.dumps(result, ensure_ascii=False).encode('utf-8'))
        except (ValueError, KeyError, TypeError):
            self.send(400, b'{"error":"Invalid source"}')
        except Exception:
            self.send(503, b'{"error":"Sandbox unavailable. No code executed on server."}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    ready()  # No Docker/image means no service, never unsandboxed exec.
    server = HTTPServer(('127.0.0.1', args.port), Handler)
    server.timeout = 10
    print(f'APL Playground: http://127.0.0.1:{args.port}')
    server.serve_forever()


if __name__ == '__main__':
    main()
