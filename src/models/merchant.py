import uuid


class MerchantCreateRequest:
    def __init__(self, merchantName: str, merchantUrl: str):
        self.merchantName = merchantName
        self.merchantUrl = merchantUrl


class Merchant:
    def __init__(self, merchantName: str,
                 accountId: str,
                 merchantId: str,
                 merchantUrl: str,
                 apiKey: str,
                 ):
        self.merchantName = merchantName
        self.accountId = accountId
        self.merchantId = merchantId
        self.merchantUrl = merchantUrl
        self.apiKey = apiKey

    def createMerchant(merchantName: str, merchantUrl: str, accountId: str):
        merchantId = str(uuid.uuid4())
        apiKey = str(uuid.uuid4())
        return Merchant(merchantName, accountId, merchantId, merchantUrl, apiKey)
