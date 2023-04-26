class TopupRequest:
    def __init__(self, accountId: str, amount: int):
        self.accountId = accountId
        self.amount = amount