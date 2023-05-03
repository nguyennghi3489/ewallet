from enum import Enum
import hashlib
import bencode
from models.merchant import Merchant
import uuid

class Status(Enum):
    INITIALIZED = 'INITIALIZED'
    CONFIRMED = 'CONFIRMED'
    VERIFIED = 'VERIFIED'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'
    EXPIRED = 'EXPIRED'
    FAILED = 'FAILED'

class TransactionCreateRequest:
    def __init__(self, buyerId: str, amount: int, extraData: str):
        self.buyerId = buyerId
        self.amount = amount
        self.extraData = extraData

    def createSignature(self):
        data = self.buyerId + str(self.amount) + self.extraData
        result = hashlib.md5(data.encode()).hexdigest()
        return result

class TransactionProcessRequest:
    def __init__(self, transactionId: str):
        self.transactionId = transactionId

class Transaction:
    def __init__(self, transactionId: str, merchantId: str, incomeAccount: str, outcomeAccount: str, amount: int, extraData: str, signature: str, status: Status):
        self.merchantId = merchantId
        self.transactionId = transactionId
        self.incomeAccount = incomeAccount
        self.outcomeAccount = outcomeAccount
        self.amount = amount
        self.extraData = extraData
        self.signature = signature
        self.status = status
    def create(merchant: Merchant, buyerId: str, amount: int, extraData: str, signature:str):
        transactionId = str(uuid.uuid4())
        return Transaction(merchant.get("merchantId"), transactionId, merchant.get("accountId"), buyerId, amount, extraData, signature, Status.INITIALIZED.value)