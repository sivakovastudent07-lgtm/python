class ClientNotFoundError(Exception):
    """ если клиента нет в приложении банка"""
    pass

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