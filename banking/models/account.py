from enum import Enum

class AccountType(Enum):
    SAVINGS = "savings"
    CURRENT = "current"

class Account:
    def __init__(self, id, type, balance_minor):
        self.id = id
        self.type = type
        self.balance_minor = balance_minor