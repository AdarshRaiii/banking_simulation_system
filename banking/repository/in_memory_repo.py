class InMemoryRepository:
    def __init__(self):
        self._storage = {}

    def save_account(self, account):
        self._storage[account.id] = account

    def get_account(self, account_id):
        return self._storage.get(account_id)

    def list_accounts(self):
        return list(self._storage.values())

    def create_account(self, account_id, account_type, initial_balance_minor=0):
        if account_id in self._storage:
            return None
        from banking.models.account import Account, AccountType
        type_enum = AccountType.SAVINGS if account_type.lower() == 'savings' else AccountType.CURRENT
        account = Account(account_id, type_enum, initial_balance_minor)
        self.save_account(account)
        return account