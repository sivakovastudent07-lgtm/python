def merge_sorted_list(l1, l2):
    merged = []
    i, j = 0, 0

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1

    while i < len(l1):
        merged.append(l1[i])
        i += 1
    while j < len(l2):
        merged.append(l2[j])
        j += 1

    return merged

def parse_numbers(line):
    """Преобразует строку '1 2 3' в список чисел [1, 2, 3]"""
    numbers = []
    for part in line.split():
        try:
            numbers.append(int(part))
        except ValueError:
            try:
                numbers.append(float(part))
            except ValueError:
                raise ValueError(f"'{part}' не является числом")
    return numbers

print("введите первый отсортированный список чисел через пробел (например: 1 3 5 7)")
line1 = input().strip()
print("введите второй отсортированный список чисел через пробел (например: 2 4 6 8)")
line2 = input().strip()

try:
    list1 = parse_numbers(line1) if line1 else []
    list2 = parse_numbers(line2) if line2 else []

    result = merge_sorted_list(list1, list2)
    print("результат слияния:", result)

except ValueError as error:
    print("ошибка:", error)
except Exception as error:
    print("неожиданная ошибка:", error)