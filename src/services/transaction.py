import time
from models.transaction import TransactionCreateRequest, Transaction, TransactionProcessRequest, Status
from services.merchant import getMerchantById
from services.account import getAccountById, transfer
import respository.transaction

def checkTransactionExpire():
    try:
        expiredList = []
        result = respository.transaction.getAllUnFinishTransaction()
        if result != None:
            for i in result:
                if i.get('created_at') != None:
                    if time.time() - i.get('created_at') > 60*5:
                        expiredList.append(i.get('transactionId'))
            if len(expiredList) > 0:
                respository.transaction.setTransactionsExpire(expiredList)
    except:
        raise
    
def create(requests: TransactionCreateRequest, merchantAccountId: str):
    try:
        merchant = getMerchantById(merchantAccountId)
        signature = requests.createSignature()
        newTransaction = Transaction.create(merchant, requests.buyerId, requests.amount, requests.extraData, signature)
        respository.transaction.create(newTransaction)
        return newTransaction
    except:
        raise

def confirm(requests: TransactionProcessRequest, personalId: str):
    try:
        transaction = respository.transaction.getTransactionById(requests.transactionId)
        account = getAccountById(personalId)
        if account == None:
            return {"msg": "Sorry, there is no matched account", "code": "UNK"}
        if transaction.get("status") != Status.INITIALIZED.value:
            return {"msg": "Sorry, transaction is not valid state", "code": "UNK"}
        if transaction.get("amount") > account.get("balance"):
            return {"msg": "Sorry, your balance is not valid", "code": "BNE"}
            
        if respository.transaction.confirm(transaction.get("transactionId")):
            return {"msg": "Transaction is confirmed", "code": "SUC"}
        
    except:
        raise

def verify(requests: TransactionProcessRequest, personalId: str):
    try:
        transaction = respository.transaction.getTransactionById(requests.transactionId)
        account = getAccountById(personalId)
        if account == None:
            return {"msg": "Sorry, there is no matched account", "code": "UNK"}
        if transaction.get("amount") > account.get("balance"):
            return {"msg": "Sorry, your balance is not valid", "code": "BNE"}
        if transaction.get("status") != Status.CONFIRMED.value:
            return {"msg": "Sorry, transaction is not valid state", "code": "UNK"}
            
        if respository.transaction.verify(transaction.get("transactionId")):
            if transfer(transaction.get("incomeAccount"), transaction.get("outcomeAccount"), transaction.get("amount")):
                return respository.transaction.complete(transaction.get("transactionId"))
        
    except:
        raise



