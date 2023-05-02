from models.merchant import Merchant
from config.api import DATA_BASE_PATH
from helpers.JsonHandler import readJson, updateJson

merchants_file_path = DATA_BASE_PATH / './merchants.json'

def create(data: Merchant):
    try:
        merchants = readJson(merchants_file_path)
        merchants.append(data.__dict__)
        updateJson(merchants_file_path, merchants)
    except:
        raise

def getMerchantById(merchantId: str):
    try:
        accounts = readJson(merchants_file_path)
        filtered_list = [ i for i in accounts if i["accountId"] == merchantId]
        if filtered_list:
            return filtered_list[0]
        return None
    except:
        return None