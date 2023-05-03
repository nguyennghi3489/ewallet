from models.transaction import Transaction, Status
from config.api import DATA_BASE_PATH
from helpers.JsonHandler import readJson, updateJson

transaction_file_path = DATA_BASE_PATH / './transactions.json'

def create(data: Transaction):
    try:
        transactions = readJson(transaction_file_path)
        transactions.append(data.__dict__)
        updateJson(transaction_file_path, transactions)
    except:
        raise

def getTransactionById(id: str)->Transaction:
    try:
        transactions = readJson(transaction_file_path)
        filtered_list = [ i for i in transactions if i["transactionId"] == id]
        if filtered_list:
            return filtered_list[0]
        return None
    except:
        return None

def updateState(transactionId: str, state: Status):
    try:
        transactions = readJson(transaction_file_path)
        filtered_index = [ index for (index, data) in enumerate(transactions) if data["transactionId"] == transactionId]
        if len(filtered_index) > 0:
            transactions[filtered_index[0]]["status"] = state
        updateJson(transaction_file_path, transactions)
        return True
    except:
        return None

def confirm(transactionId: str):
    try:
        return updateState(transactionId, Status.CONFIRMED.value)
    except:
        return None

def verify(transactionId: str):
    try:
        return updateState(transactionId, Status.VERIFIED.value)
    except:
        return None

def complete(transactionId: str):
    try:
        return updateState(transactionId, Status.COMPLETED.value)
    except:
        return None
