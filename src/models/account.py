from enum import Enum
import uuid

class AccountType(Enum):
    MERCHANT = 'merchant'
    PERSONAL = 'personal'
    ISSUER = 'issuer'


class AccountCreateRequest:
    def __init__(self, accountType: AccountType):
        self.accountType = accountType

class Account:
    def __init__(self, accountType: AccountType):
        self.accountType = accountType
        self.balance = 0
        self.accountId = str(uuid.uuid4())
