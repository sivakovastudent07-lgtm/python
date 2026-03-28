"""
написать класс сотрудники. экземпляр класса с аргументами: имя, должность, стаж.
методы: приходить на работу, уходить с работы, выыполнять задачи, получать зп.  
обязательно прописать какую-то свою ошибку.
пользовательский ввод: добавить сотрудника, выбрать его действие (ушел с работы, пришел на работу) 
"""
class MyError(Exception):
    pass

class Employee:
    def __init__(self, name, role, exp_years):
        self.name = name
        self.role = role
        self.exp_years = exp_years
        self.at_work = False

    def arrive(self):
        if self.at_work:
            raise MyError("уже на работе")
        self.at_work = True
        return self.name + " пришел"

    def leave(self):
        if not self.at_work:
            raise MyError("еще не пришел")
        self.at_work = False
        return self.name + " ушел"

    def do_task(self, task):
        return self.name + " делает: " + task

    def get_salary(self, amount):
        return self.name + " получил " + str(amount)

employees = {}

def add_employee():
    try:
        name = input("имя: ")
        role = input("должность: ")
        exp = input("стаж лет: ")
        if not exp.isdigit():
            raise MyError("стаж должен быть числом")
        employees[name] = Employee(name, role, int(exp))
        print("добавлен")
    except MyError as err:
        print("ошибка:", err)

def show_employees():
    if not employees:
        print("нет сотрудников")
        return
    num = 1
    for name in employees:
        print(str(num) + ". " + name)
        num += 1

def choose_action():
    try:
        name = input("кого выбрать: ")
        if name not in employees:
            raise MyError("нет такого")
        person = employees[name]
        print("1 прийти, 2 уйти, 3 задача, 4 зп")
        choice = input("номер: ")
        if choice == "1":
            print(person.arrive())
        elif choice == "2":
            print(person.leave())
        elif choice == "3":
            task = input("что делать: ")
            print(person.do_task(task))
        elif choice == "4":
            amount = input("сколько выдать: ")
            print(person.get_salary(amount))
        else:
            raise MyError("неверный выбор")
    except MyError as err:
        print("ошибка:", err)

while True:
    cmd = input("\n1 добавить, 2 действие, 3 показать имена, 4 выход\n")
    if cmd == "1":
        add_employee()
    elif cmd == "2":
        choose_action()
    elif cmd == "3":
        show_employees()
    elif cmd == "4":
        break
    else:
        print("введите 1-4")