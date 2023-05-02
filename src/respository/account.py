from models.account import Account
from models.topup import TopupRequest
from config.api import DATA_BASE_PATH
from helpers.JsonHandler import readJson, updateJson
import json

accounts_file_path = DATA_BASE_PATH / './accounts.json'

def create(data: Account):
    try:
        accounts = readJson(accounts_file_path)
        accounts.append(data.__dict__)
        updateJson(accounts_file_path, accounts)
    except:
        raise

def getAccountById(id: str):
    try:
        accounts = readJson(accounts_file_path)
        filtered_list = [ i for i in accounts if i["accountId"] == id]
        if filtered_list:
            return filtered_list[0]
        return None
    except:
        return None

def topupAccount(request: TopupRequest):
    try:
        accounts = readJson(accounts_file_path)
        filtered_index = [ index for (index, data) in enumerate(accounts) if data["accountId"] == request.accountId]
        if len(filtered_index) > 0:
            accounts[filtered_index[0]]["balance"] += request.amount
        updateJson(accounts_file_path, accounts)
        return True
    except:
        return None