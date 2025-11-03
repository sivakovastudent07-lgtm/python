s = input("введите элементы через пробел: ")

items = []
for x in s.split():
    items = items + [x]

unique = []
for x in items:
    found = False
    for y in unique:
        if y == x:
            found = True
            break
    if not found:
        unique = unique + [x]
print("список без дубликатов:", unique)