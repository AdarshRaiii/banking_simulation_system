import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from banking.models.account import Account, AccountType
from banking.repository.in_memory_repo import InMemoryRepository
from banking.services.transaction_service import TransactionService
from banking.models.ledger import Ledger

def run():
    repo = InMemoryRepository()
    ledger = Ledger()
    service = TransactionService(repo, ledger)
    
    # Create initial user
    user = Account("001", AccountType.SAVINGS, 10000)  # balance_minor in cents
    repo.save_account(user)
    
    print("Welcome to Banking Simulation!")
    amt = float(input("Enter deposit amount: "))
    amount_minor = int(amt * 100)  # convert to minor units
    if service.deposit("001", amount_minor):
        print(f"New Balance: {user.balance_minor / 100:.2f}")

if __name__ == "__main__":
    run()