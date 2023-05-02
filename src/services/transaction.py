from models.transaction import TransactionCreateRequest, Transaction, TransactionConfirmRequest, Status
from services.merchant import getMerchantById
from services.account import getAccountById
import respository.transaction

def create(requests: TransactionCreateRequest, merchantAccountId: str):
    try:
        merchant = getMerchantById(merchantAccountId)
        signature = requests.createSignature()
        newTransaction = Transaction.create(merchant, requests.buyerId, requests.amount, requests.extraData, signature)
        respository.transaction.create(newTransaction)
        return newTransaction
    except:
        raise

def confirm(requests: TransactionConfirmRequest, personalId: str):
    try:
        transaction = respository.transaction.getTransactionById(requests.transactionId)
        account = getAccountById(personalId)
        if account == None:
            return {"msg": "Sorry, there is no matched account", "code": "UNK"}
        if transaction.get("amount") > account.get("balance"):
            return {"msg": "Sorry, your balance is not valid", "code": "BNE"}
            
        if respository.transaction.confirm(transaction.get("transactionId")):
            return {"msg": "Transaction is confirmed", "code": "SUC"}
        
    except:
        raise


