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
