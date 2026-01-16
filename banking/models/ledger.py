from datetime import datetime
from dataclasses import dataclass

@dataclass
class LedgerEntry:
    time: datetime
    id: str
    type: str
    amount: int

class Ledger:
    def __init__(self):
        self.history = []

    def log(self, account_id, type, amount):
        entry = LedgerEntry(time=datetime.now(), id=account_id, type=type, amount=amount)
        self.history.append(entry)

    def verify_integrity(self):
        # Simple implementation: always return True for now
        return True