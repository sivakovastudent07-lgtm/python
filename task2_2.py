def merge_dicts(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise TypeError("оба аргумента должны быть словарями")
    for key in dict2:
        if key in dict1:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                merge_dicts(dict1[key], dict2[key])
            else:
                dict1[key] = dict2[key]
        else:
            dict1[key] = dict2[key]

try:
    input1 = input("введите первый словарь в формате python: ")
    input2 = input("введите второй словарь в формате python: ")
    dict1 = eval(input1)
    dict2 = eval(input2)
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        print("ошибка: оба введённых значения должны быть словарями")
    else:
        merge_dicts(dict1, dict2)
        print(dict1)
except Exception as error:
    print(f"ошибка: {error}")