from services.merchant import create
from http.server import BaseHTTPRequestHandler
from models.merchant import MerchantCreateRequest
import json

def signup(req: BaseHTTPRequestHandler):
    content_length = int(req.headers.get('content-length'))
    req_body = dict(json.loads(req.rfile.read(content_length).decode()))
    data = MerchantCreateRequest(**req_body)
    try:
        result = create(data)
        req.send_response(200)
        req.send_header('Content-Type', 'application/json')
        req.end_headers()
        req.wfile.write(json.dumps(result.__dict__).encode())
    except Exception as err:
        print(err)
        
        req.send_response(400)
        req.send_header('Content-Type', 'text/plain')
        req.end_headers()
        req.wfile.write('Error'.encode())
