elements = input("введите элементы через пробел: ").split()

unique_i = []
for i in elements:
    found = False
    for saved in unique_i:
        if i.lower() == saved.lower():
            found = True
            break
    if not found:
        unique_i.append(i)

print("список без дубликатов: ", unique_i)