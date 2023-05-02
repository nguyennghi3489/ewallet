from models.transaction import Transaction
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
