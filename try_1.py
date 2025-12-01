#сгенерировать структуру с отметками первашей 
#(сгенерировать структуру и в нее потом добавлять фио перваша и его отметку а также сохранял предыдущие записи) 
# пользователя можно добавлять и вводить отметку
# пустая структура для хранения фио и отметок первокурсников
#использовать только структуры и декораторы

def student_storage(func):
    storage = {}  

    def wrapper(*args, **kwargs):
        return func(storage, *args, **kwargs)  

    return wrapper

@student_storage
def add_student(storage):
    fio = input("ФИО: ").strip()
    if fio and len(fio.split()) >= 2 and all(c.isalpha() or c==' ' for c in fio):
        if fio not in storage:
            storage[fio] = []
            print("Добавлен")
        else:
            print("Уже есть")
    else:
        print("Некорректное ФИО")
    return storage

@student_storage
def add_grade(storage):
    fio = input("ФИО: ").strip()
    if fio in storage:
        try:
            grade = float(input("Оценка (1-10): "))
            if 1 <= grade <= 10:
                storage[fio].append(grade)
                print("Оценка добавлена")
            else:
                print("1-10 только")
        except:
            print("Число надо")
    else:
        print("Нет такого студента")
    return storage

@student_storage
def show(storage):
    fio = input("ФИО: ").strip()
    if fio in storage:
        grades = storage[fio]
        avg = sum(grades)/len(grades) if grades else 0
        print(f"Оценки: {grades}, ср: {avg:.1f}")
    else:
        print("Не найден")
    return storage

while True:
    print("\n1-Добавить студента\n2-Добавить оценку\n3-Показать\n4-Выход")
    choice = input("> ")

    if choice == "1": add_student()
    elif choice == "2": add_grade()
    elif choice == "3": show()
    elif choice == "4": break
    else: print("1-4!")

