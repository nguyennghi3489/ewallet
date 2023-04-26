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