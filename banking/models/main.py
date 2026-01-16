from banking.models import Account, AccountType, Ledger

def demo():
    acc = Account(id="A1", type=AccountType.SAVINGS, balance_minor=10000)
    print("Demo account:", acc)
    ledger = Ledger()
    print("Ledger integrity:", ledger.verify_integrity())

if __name__ == "__main__":
    demo()