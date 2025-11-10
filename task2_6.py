def unique_elements(lst):
    """
    возвращает список уникальных элементов из воженного списка,
    сохраняя порядок
    """
    result = []

    def flatten(current_list, output):
        for item in current_list:
            if isinstance(item, list):
                flatten(item, output)
            else:
                if item not in output:
                    output.append(item)

    flatten(lst, result)
    return result
print("введите элементы через пробел (например: 1 2 3 2 4 1)")
user_input = input().strip()

if not user_input:
    print("ошибка: пустой ввод")
else:
    items = []
    for part in user_input.split():
        try:
           items.append(int(part))
        except ValueError:
            try:
                items.append(float(part))
            except ValueError:
                items.append(part)

    input_list = items
    result = unique_elements(input_list)
    print("уникальные элементы с сохранением порядка:", result)