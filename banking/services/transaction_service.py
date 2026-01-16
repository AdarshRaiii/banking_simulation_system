from banking.models.transaction import Transaction

class TransactionService:
    def __init__(self, repo, ledger):
        self.repo = repo
        self.ledger = ledger

    def transfer(self, from_id, to_id, amount_minor):
        from_acc = self.repo.get_account(from_id)
        to_acc = self.repo.get_account(to_id)
        if from_acc and to_acc and from_acc.balance_minor >= amount_minor > 0:
            from_acc.balance_minor -= amount_minor
            to_acc.balance_minor += amount_minor
            txn = Transaction(src_account_id=from_id, dst_account_id=to_id, amount_minor=amount_minor, type="TRANSFER")
            self.ledger.log(from_id, "TRANSFER_OUT", -amount_minor)
            self.ledger.log(to_id, "TRANSFER_IN", amount_minor)
            return txn
        return None

    def deposit(self, account_id, amount_minor):
        acc = self.repo.get_account(account_id)
        if acc and amount_minor > 0:
            acc.balance_minor += amount_minor
            self.ledger.log(account_id, "DEPOSIT", amount_minor)
            return True
        return False

    def withdraw(self, account_id, amount_minor):
        acc = self.repo.get_account(account_id)
        if acc and 0 < amount_minor <= acc.balance_minor:
            acc.balance_minor -= amount_minor
            self.ledger.log(account_id, "WITHDRAWAL", -amount_minor)
            return True
        return False