from models.account import Account, AccountCreateRequest, AccountType
from models.topup import TopupRequest
import respository.account 
import jwt

def create(requests: AccountCreateRequest):
    data = Account(requests.accountType)
    respository.account.create(data)
    return data

def createAccountByType(type: AccountType):
    data = Account(type)
    respository.account.create(data)
    return data

def getToken(accountId: str):
    try:
        account = respository.account.getAccountById(accountId)
        return jwt.encode({"accountId": account.get("accountId"), "accountType": account.get("accountType")}, "secret", algorithm="HS256")
    except:
        raise

def checkAccountId(accountId: str):
    try:
        isValid = respository.account.getAccountById(accountId)
        return True if isValid != None else False
    except:
        raise

def topupAccount(request: TopupRequest):
    try:
        return respository.account.topupAccount(request)
    except:
        raise

def getAccountById(id: str)->Account|None:
    merchant = respository.account.getAccountById(id)
    return merchant

def transfer(incomeAccountId: str, outcomeAccountId: str, amount: int):
    try:
        return respository.account.doTransfer(incomeAccountId, outcomeAccountId, amount)
    except:
        raise
    
