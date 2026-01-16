import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from banking.models import Account, AccountType, Ledger
from banking.repository.in_memory_repo import InMemoryRepository
from banking.services import TransactionService

def test_transfer_flow():
    repo = InMemoryRepository()
    ledger = Ledger()
    svc = TransactionService(repo, ledger)

    a1 = Account(id="A1", type=AccountType.SAVINGS, balance_minor=50000)
    a2 = Account(id="A2", type=AccountType.CURRENT, balance_minor=10000)
    repo.save_account(a1)
    repo.save_account(a2)

    txn = svc.transfer("A1", "A2", 15000)

    assert repo.get_account("A1").balance_minor == 35000
    assert repo.get_account("A2").balance_minor == 25000
    assert ledger.verify_integrity() is True
    assert txn.type == "TRANSFER"