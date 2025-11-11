#сгенерировать структуру с отметками первашей 
#(сгенерировать структуру и в нее потом добавлять фио перваша и его отметку а также сохранял предыдущие записи) 
# пользователя можно добавлять и вводить отметку
# пустая структура для хранения фио и отметок первокурсников
grades = {}

while True:
    name = input("введите фио перваша (или 'стоп' для выхода): ").strip()
    if name.lower() == 'стоп':
        break
    if name in grades:
        print(f"фио {name} уже введено")
        print(f"отметка: {grades[name]}")
    else:
        grade = input("введите отметку: ").strip()
        if grade:
            grades[name] = grade
            print(f"у перваша {name}: {grade}")
        else:
            print("отметка не может быть пустой")

print("\nсписок студентов с отметками:")
for pervash, mark in grades.items():
    print(f"{pervash}: {mark}")