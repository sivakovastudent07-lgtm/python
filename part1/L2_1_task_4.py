l1 = input("введите числа первого набора через пробел: ").split()
l2 = input("введите числа второго набора через пробел: ").split()

common = []
for num in l1:
    if num in l2 and num not in common:
        common.append(num)
print("общие числа:", common)

only_l1 = []
for num in l1:
    if num not in l2 and num not in only_l1:
        only_l1.append(num)
only_l2 = []
for num in l2:
    if num not in l1 and num not in only_l2:
        only_l2.append(num)

print("только в первом:", only_l1)
print("только во втором:", only_l2)

# все кроме общих
other = only_l1 + only_l2
print("все числа, кроме общих:", other)        