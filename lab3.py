from datetime import datetime
class InsufficientFundsError(Exception):
    """недостаточно средств на счёте"""

class AccountNotFoundError(Exception):
    """у клиента не найден счёт в указанной валюте"""

class CurrencyMismatchError(Exception):
    """попытка перевода между счетами в разных валютах"""

class AccountAlreadyExistsError(Exception):
    """счёт в указанной валюте уже существует"""


class ClientNotFoundError(Exception):
    """клиент не найден"""
    
class Client:
    def __init__(self, client_id, name, email):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.accounts = {}  
        
class BankAccount:
    def __init__(self, account_id, client, currency):
        self.account_id = account_id
        self.client = client
        self.currency = currency.upper()
        self.balance = 0.0
        self.transactions = []

class Bank:
    def __init__(self):
        self.clients = {}
        self.accounts = {}
    
    def create_client(self, name, email):
        global next_client_id
        client_id = next_client_id
        next_client_id += 1
        client = Client(client_id, name, email)
        self.clients[client_id] = client
        return client_id

    def open_account(self, client_id, currency):
        if client_id not in self.clients:
            raise ClientNotFoundError("Клиент не найден")
        client = self.clients[client_id]
        currency = currency.upper()

        if currency not in client.accounts:
            raise AccountNotFoundError("Счёт в валюте " + currency + " не найден")

        if client.accounts[currency].balance != 0:
            raise ValueError("Нельзя закрыть счёт с ненулевым балансом")

        account_id = client.accounts[currency].account_id
        del client.accounts[currency]
        del self.accounts[account_id]

    def deposit(self, client_id, currency, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        if client_id not in self.clients:
            raise ClientNotFoundError("Клиент не найден")

        client = self.clients[client_id]
        currency = currency.upper()

        if currency not in client.accounts:
            raise AccountNotFoundError("Счёт в валюте " + currency + " не найден")

        account = client.accounts[currency]
        account.balance += amount
        account.transactions.append({
            'type': 'deposit',
            'amount': amount,
            'timestamp': datetime.now(),
            'balance_after': account.balance
        })
    def withdraw(self, client_id, currency, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if client_id not in self.clients:
            raise ClientNotFoundError("Клиент не найден")

        client = self.clients[client_id]
        currency = currency.upper()

        if currency not in client.accounts:
            raise AccountNotFoundError("Счёт в валюте " + currency + " не найден")

        account = client.accounts[currency]
        if amount > account.balance:
            raise InsufficientFundsError("Недостаточно средств на счёте")

        account.balance -= amount
        account.transactions.append({
            'type': 'withdraw',
            'amount': amount,
            'timestamp': datetime.now(),
            'balance_after': account.balance
        })

    def transfer(self, from_client_id, from_currency, to_client_id, to_currency, amount):
        if from_client_id not in self.clients:
            raise ClientNotFoundError("Отправитель не найден")
        if to_client_id not in self.clients:
            raise ClientNotFoundError("Получатель не найден")

        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency != to_currency:
            raise CurrencyMismatchError("Перевод возможен только между счетами в одинаковой валюте")

        from_client = self.clients[from_client_id]
        to_client = self.clients[to_client_id]

        if from_currency not in from_client.accounts:
            raise AccountNotFoundError("Счёт отправителя в валюте " + from_currency + " не найден")
        if to_currency not in to_client.accounts:
            raise AccountNotFoundError("Счёт получателя в валюте " + to_currency + " не найден")

        from_account = from_client.accounts[from_currency]
        to_account = to_client.accounts[to_currency]

        if from_account.balance < amount:
            raise InsufficientFundsError("Недостаточно средств для перевода")

        now = datetime.now()
        from_account.balance -= amount
        to_account.balance += amount

        from_account.transactions.append({
            'type': 'transfer_out',
            'amount': amount,
            'timestamp': now,
            'balance_after': from_account.balance,
            'to_account': to_account.account_id
        })
        to_account.transactions.append({
            'type': 'transfer_in',
            'amount': amount,
            'timestamp': now,
            'balance_after': to_account.balance,
            'from_account': from_account.account_id
        })

    def get_client(self, client_id):
        return self.clients.get(client_id)

    def generate_statement(self, client_id, filename=None):
        if client_id not in self.clients:
            raise ClientNotFoundError("Клиент не найден")

        client = self.clients[client_id]
        if not client.accounts:
            raise AccountNotFoundError("У клиента нет счетов")

        if filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = "statement_" + str(client_id) + "_" + timestamp + ".txt"

        total_balance = 0.0
        currencies = []

        with open(filename, 'w', encoding='utf-8') as f:
            f.write("Выписка по счетам клиента\n")
            f.write("Имя: " + client.name + "\n")
            f.write("ID клиента: " + str(client.client_id) + "\n")
            f.write("Email: " + client.email + "\n")
            f.write("Дата выписки: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")
            f.write("=" * 50 + "\n\n")

            for currency, account in client.accounts.items():
                f.write("Счёт ID: " + str(account.account_id) + "\n")
                f.write("Валюта: " + account.currency + "\n")
                f.write("Баланс: " + "{:.2f}".format(account.balance) + " " + account.currency + "\n")
                f.write("-" * 30 + "\n")
                f.write("Транзакции:\n")
                for tx in account.transactions:
                    tx_time = tx['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
                    if tx['type'] == 'deposit':
                        f.write("  " + tx_time + " | Пополнение | +" + "{:.2f}".format(tx['amount']) + " | Баланс: " + "{:.2f}".format(tx['balance_after']) + "\n")
                    elif tx['type'] == 'withdraw':
                        f.write("  " + tx_time + " | Снятие | -" + "{:.2f}".format(tx['amount']) + " | Баланс: " + "{:.2f}".format(tx['balance_after']) + "\n")
                    elif tx['type'] == 'transfer_out':
                        f.write("  " + tx_time + " | Перевод исходящий | -" + "{:.2f}".format(tx['amount']) + " | Получатель: " + str(tx['to_account']) + " | Баланс: " + "{:.2f}".format(tx['balance_after']) + "\n")
                    elif tx['type'] == 'transfer_in':
                        f.write("  " + tx_time + " | Перевод входящий | +" + "{:.2f}".format(tx['amount']) + " | Отправитель: " + str(tx['from_account']) + " | Баланс: " + "{:.2f}".format(tx['balance_after']) + "\n")
                f.write("\n")
                total_balance += account.balance
                currencies.append(account.currency)

            f.write("=" * 50 + "\n")
            f.write("Суммарный баланс: " + "{:.2f}".format(total_balance) + " (в валютах: " + ", ".join(currencies) + ")\n")

        return filename

