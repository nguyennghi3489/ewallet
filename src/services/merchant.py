from models.merchant import MerchantCreateRequest, Merchant
from models.account import AccountType
from services.account import createAccountByType
import respository.merchant 

def create(requests: MerchantCreateRequest):
    account = createAccountByType(AccountType.MERCHANT.value)
    data = Merchant.createMerchant(requests.merchantName, requests.merchantUrl, account.accountId)
    respository.merchant.create(data)
    return data