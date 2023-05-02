from models.transaction import TransactionCreateRequest, Transaction
from services.merchant import getMerchantById
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
