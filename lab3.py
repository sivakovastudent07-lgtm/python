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
    
next_client_id = 1
next_account_id = 1    
    
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

def main():
    bank = Bank()
    print("Добро пожаловать в банк!")

    while True:
        print()
        print("ГЛАВНОЕ МЕНЮ")
        print()
        print("1. Создать нового клиента")
        print("2. Войти по ID клиента")
        print("3. Выйти из системы")
        choice = input("Выберите действие (1–3): ")

        if choice == '1':
            name = input("Введите имя клиента: ")
            email = input("Введите email клиента: ")
            client_id = bank.create_client(name, email)
            print("Клиент успешно создан!")
            print("Ваш ID: " + str(client_id))

        elif choice == '2':
            try:
                client_id = int(input("Введите ваш ID: "))
                client = bank.get_client(client_id)
                if client is None:
                    print("Клиент с таким ID не найден")
                    continue

                while True:
                    print("\nЛичный кабинет")
                    print("Клиент: " + client.name + " (ID: " + str(client.client_id) + ")")
                    print("Счета:")
                    if client.accounts:
                        for currency, account in client.accounts.items():
                            print("  " + currency + ": " + "%.2f" % account.balance)
                    else:
                        print("У вас пока нет счетов")

                    print("\nОперации:")
                    print("1. Открыть счёт")
                    print("2. Закрыть счёт")
                    print("3. Пополнить счёт")
                    print("4. Снять деньги")
                    print("5. Перевести деньги другому клиенту")
                    print("6. Получить выписку")
                    print("7. Выйти в главное меню")
                    op = input("Выберите операцию (1–7): ")

                    try:
                        if op == '1':
                            currency = input("Введите валюту счёта (например, BYN, USD, EUR, RUB): ")
                            account_id = bank.open_account(client_id, currency)
                            print("Счёт в валюте " + currency.upper() + " успешно открыт! ID счёта: " + str(account_id))

                        elif op == '2':
                            if not client.accounts:
                                print("У вас нет счетов для закрытия")
                                continue
                            currency = input("Введите валюту счёта для закрытия: ")
                            bank.close_account(client_id, currency)
                            print("Счёт в валюте " + currency.upper() + " закрыт")

                        elif op == '3':
                            currency = input("Введите валюту счёта: ")
                            amount = float(input("Введите сумму для пополнения: "))
                            bank.deposit(client_id, currency, amount)
                            print("Счёт пополнен на " + str(amount) + " " + currency.upper())

                        elif op == '4':
                            currency = input("Введите валюту счёта: ")
                            amount = float(input("Введите сумму для снятия: "))
                            bank.withdraw(client_id, currency, amount)
                            print("Со счёта снято " + str(amount) + " " + currency.upper())

                        elif op == '5':
                            to_id = int(input("Введите ID получателя: "))
                            if to_id == client_id:
                                print("Нельзя перевести деньги самому себе")
                                continue
                            currency = input("Введите валюту перевода: ")
                            amount = float(input("Введите сумму перевода: "))
                            bank.transfer(client_id, currency, to_id, currency, amount)
                            print("Перевод на " + str(amount) + " " + currency.upper() + " успешно выполнен!")

                        elif op == '6':
                            filename = bank.generate_statement(client_id)
                            print("Выписка сохранена в файл: " + filename)

                        elif op == '7':
                            break

                        else:
                            print("Неверный выбор. Попробуйте снова")

                    except Exception as e:
                        print("Ошибка: " + str(e))

            except ValueError:
                print("Ошибка: ID должен быть числом")
            except Exception as e:
                print("Ошибка: " + str(e))

        elif choice == '3':
            print("Спасибо за использование банковской системы! До свидания!")
            break

        else:
            print("Неверный выбор. Пожалуйста, введите 1, 2 или 3")


if __name__ == "__main__":
    main()