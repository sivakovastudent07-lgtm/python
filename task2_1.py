def flatten_list(lst):
    if not isinstance(lst, list):
        raise TypeError("аргумент должен быть списком")
    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            flatten_list(lst[i])
            nested = lst.pop(i)
            for j, item in enumerate(nested):
                lst.insert(i + j, item)
        else:
            i += 1

try:
    user_input = input("введите список (например, [1, [2, 3], 4]): ")
    data = list(user_input)
    flatten_list(data)
    print(data)
except Exception as error:
    print(f"ошибка: {error}")