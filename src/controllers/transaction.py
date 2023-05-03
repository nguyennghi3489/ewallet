from services.transaction import create as createTransaction, confirm as confirmTransaction, verify as verifyTransaction
from http.server import BaseHTTPRequestHandler
from models.transaction import TransactionCreateRequest, TransactionProcessRequest
from models.account import AccountType
from services.account import checkAccountId
import json
import jwt

def create(req: BaseHTTPRequestHandler):
    content_length = int(req.headers.get('content-length'))
    req_body = dict(json.loads(req.rfile.read(content_length).decode()))
    data = TransactionCreateRequest(**req_body)
    token = req.headers.get('Authorization')
    parsedData = jwt.decode(token, key="secret", algorithms="HS256")
    if parsedData.get("accountType") != AccountType.MERCHANT.value or checkAccountId(parsedData.get("accountId") == None):
        req.send_response(400)
        req.send_header('Content-Type', 'text/plain')
        req.end_headers()
        req.wfile.write('JWT error'.encode())
        return

    try:
        result = createTransaction(data, parsedData.get("accountId"))
        req.send_response(200)
        req.send_header('Content-Type', 'application/json')
        req.end_headers()
        req.wfile.write(json.dumps(result.__dict__).encode())
    except Exception as err:
        req.send_response(400)
        req.send_header('Content-Type', 'text/plain')
        req.end_headers()
        req.wfile.write('Create Transaction Failed'.encode())

def confirm(req: BaseHTTPRequestHandler):
    content_length = int(req.headers.get('content-length'))
    req_body = dict(json.loads(req.rfile.read(content_length).decode()))
    data = TransactionProcessRequest(**req_body)
    token = req.headers.get('Authorization')
    parsedData = jwt.decode(token, key="secret", algorithms="HS256")
    if parsedData.get("accountType") != AccountType.PERSONAL.value or checkAccountId(parsedData.get("accountId") == None):
        req.send_response(400)
        req.send_header('Content-Type', 'text/plain')
        req.end_headers()
        req.wfile.write('JWT error'.encode())
        return
    
    try:
        result = confirmTransaction(data, parsedData.get("accountId"))
        req.send_response(200)
        req.send_header('Content-Type', 'application/json')
        req.end_headers()
        req.wfile.write(json.dumps(result).encode())

    except Exception as err:
        req.send_response(400)
        req.send_header('Content-Type', 'text/plain')
        req.end_headers()
        req.wfile.write('Create Transaction Failed'.encode())

def verify(req: BaseHTTPRequestHandler):
    content_length = int(req.headers.get('content-length'))
    req_body = dict(json.loads(req.rfile.read(content_length).decode()))
    data = TransactionProcessRequest(**req_body)
    token = req.headers.get('Authorization')
    parsedData = jwt.decode(token, key="secret", algorithms="HS256")
    if parsedData.get("accountType") != AccountType.PERSONAL.value or checkAccountId(parsedData.get("accountId") == None):
        req.send_response(400)
        req.send_header('Content-Type', 'text/plain')
        req.end_headers()
        req.wfile.write('JWT error'.encode())
        return
    try:
        result = verifyTransaction(data, parsedData.get("accountId"))
        if result:
            req.send_response(200)
            req.send_header('Content-Type', 'application/json')
            req.end_headers()
            req.wfile.write("OK".encode())
        else:
            req.send_response(400)
            req.send_header('Content-Type', 'text/plain')
            req.end_headers()
            req.wfile.write('Create Transaction Failed'.encode())
    except Exception as err:
        req.send_response(400)
        req.send_header('Content-Type', 'text/plain')
        req.end_headers()
        req.wfile.write('Create Transaction Failed'.encode())