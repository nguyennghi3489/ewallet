from http.server import BaseHTTPRequestHandler
from models.account import AccountCreateRequest
from models.topup import TopupRequest
from services.account import create as createAccount, getToken, checkAccountId, topupAccount
import json
import jwt

def create(req: BaseHTTPRequestHandler):
    content_length = int(req.headers.get('content-length'))
    req_body = dict(json.loads(req.rfile.read(content_length).decode()))
    data = AccountCreateRequest(**req_body)
    try:
        result = createAccount(data)
        req.send_response(200)
        req.send_header('Content-Type', 'application/json')
        req.end_headers()
        req.wfile.write(json.dumps(result.__dict__).encode())
    except:
        req.send_response(400)
        req.send_header('Content-Type', 'text/plain')
        req.end_headers()
        req.wfile.write('Error'.encode())

def token(req: BaseHTTPRequestHandler):
    _route = dict(req.route)
    accountId = _route.get('accountId')
    try:
        result = getToken(accountId)
        req.send_response(200)
        req.send_header('Content-Type', 'application/json')
        req.end_headers()
        req.wfile.write(result.encode())
    except:
        req.send_response(400)
        req.send_header('Content-Type', 'text/plain')
        req.end_headers()
        req.wfile.write('Error'.encode())

def topup(req: BaseHTTPRequestHandler):
    content_length = int(req.headers.get('content-length'))
    req_body = dict(json.loads(req.rfile.read(content_length).decode()))
    token = req.headers.get('Authorization')
    topupRequest = TopupRequest(**req_body)
    try:
        parsedData = jwt.decode(token, key="secret", algorithms="HS256")
        if parsedData.get("accountType") != "issuer" or checkAccountId(parsedData.get("accountId") == None):
            req.send_response(400)
            req.send_header('Content-Type', 'text/plain')
            req.end_headers()
            req.wfile.write('Error'.encode())

        try:
            topupAccount(topupRequest)
            req.send_response(200)
            req.send_header('Content-Type', 'application/json')
            req.end_headers()
            req.wfile.write(token.encode())
        except:
            req.send_response(400)
            req.send_header('Content-Type', 'text/plain')
            req.end_headers()
            req.wfile.write('Error'.encode())
    except:
        req.send_response(400)
        req.send_header('Content-Type', 'text/plain')
        req.end_headers()
        req.wfile.write('Signature verification failed'.encode())