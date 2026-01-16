import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, render_template, request, jsonify

from banking.models.account import Account, AccountType
from banking.repository.in_memory_repo import InMemoryRepository
from banking.services.transaction_service import TransactionService
from banking.models.ledger import Ledger

app = Flask(__name__)

# Initialize services
repo = InMemoryRepository()
ledger = Ledger()
service = TransactionService(repo, ledger)

# Create initial accounts
user1 = Account("001", AccountType.SAVINGS, 10000)  # $100.00
user2 = Account("002", AccountType.CURRENT, 5000)   # $50.00
repo.save_account(user1)
repo.save_account(user2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer')
def customer():
    return render_template('customer.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.json
    account_id = data.get('account_id')
    amount = data.get('amount')
    try:
        amount_minor = int(float(amount) * 100)
        if service.deposit(account_id, amount_minor):
            acc = repo.get_account(account_id)
            return jsonify({'success': True, 'balance': acc.balance_minor / 100})
        else:
            return jsonify({'success': False, 'message': 'Deposit failed'})
    except:
        return jsonify({'success': False, 'message': 'Invalid input'})

@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.json
    account_id = data.get('account_id')
    amount = data.get('amount')
    try:
        amount_minor = int(float(amount) * 100)
        if service.withdraw(account_id, amount_minor):
            acc = repo.get_account(account_id)
            return jsonify({'success': True, 'balance': acc.balance_minor / 100})
        else:
            return jsonify({'success': False, 'message': 'Withdrawal failed'})
    except:
        return jsonify({'success': False, 'message': 'Invalid input'})

@app.route('/transfer', methods=['POST'])
def transfer():
    data = request.json
    from_id = data.get('from_id')
    to_id = data.get('to_id')
    amount = data.get('amount')
    try:
        amount_minor = int(float(amount) * 100)
        txn = service.transfer(from_id, to_id, amount_minor)
        if txn:
            from_acc = repo.get_account(from_id)
            to_acc = repo.get_account(to_id)
            return jsonify({'success': True, 'from_balance': from_acc.balance_minor / 100, 'to_balance': to_acc.balance_minor / 100})
        else:
            return jsonify({'success': False, 'message': 'Transfer failed'})
    except:
        return jsonify({'success': False, 'message': 'Invalid input'})

@app.route('/balance', methods=['POST'])
def balance():
    data = request.json
    account_id = data.get('account_id')
    acc = repo.get_account(account_id)
    if acc:
        return jsonify({'success': True, 'balance': acc.balance_minor / 100})
    else:
        return jsonify({'success': False, 'message': 'Account not found'})

@app.route('/history', methods=['POST'])
def history():
    data = request.json
    account_id = data.get('account_id')
    history_list = [entry for entry in ledger.history if entry.id == account_id]
    history_data = [{'time': str(entry.time), 'type': entry.type, 'amount': abs(entry.amount) / 100} for entry in history_list]
    return jsonify({'success': True, 'history': history_data})

@app.route('/admin/list_accounts', methods=['GET'])
def list_accounts():
    accounts = repo.list_accounts()
    accounts_data = [{'id': acc.id, 'type': acc.type.value, 'balance': acc.balance_minor / 100} for acc in accounts]
    return jsonify({'accounts': accounts_data})

@app.route('/admin/create_account', methods=['POST'])
def create_account():
    data = request.json
    account_id = data.get('account_id')
    account_type = data.get('account_type')
    initial_balance = data.get('initial_balance', 0)
    try:
        initial_balance_minor = int(float(initial_balance) * 100)
        account = repo.create_account(account_id, account_type, initial_balance_minor)
        if account:
            return jsonify({'success': True, 'account': {'id': account.id, 'type': account.type.value, 'balance': account.balance_minor / 100}})
        else:
            return jsonify({'success': False, 'message': 'Account ID already exists'})
    except:
        return jsonify({'success': False, 'message': 'Invalid input'})

@app.route('/admin/global_history', methods=['GET'])
def global_history():
    history_data = [{'time': str(entry.time), 'id': entry.id, 'type': entry.type, 'amount': entry.amount / 100} for entry in ledger.history]
    return jsonify({'history': history_data})

if __name__ == '__main__':
    app.run(debug=True)