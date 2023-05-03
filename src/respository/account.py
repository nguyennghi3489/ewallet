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

def doTransfer(incomeAccountId: str, outcomeAccountId: str, amount: int):
    try:
        accounts = readJson(accounts_file_path)
        incomeAccountIndex = [ index for (index, data) in enumerate(accounts) if data["accountId"] == incomeAccountId]
        if len(incomeAccountIndex) > 0:
            accounts[incomeAccountIndex[0]]["balance"] += amount
        outcomeAccountIndex = [ index for (index, data) in enumerate(accounts) if data["accountId"] == outcomeAccountId]
        if len(outcomeAccountIndex) > 0:
            accounts[outcomeAccountIndex[0]]["balance"] -= amount
        updateJson(accounts_file_path, accounts)
        return True
    except:
        return None