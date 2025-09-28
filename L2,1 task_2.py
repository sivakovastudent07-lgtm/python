s = input("Введите числа через пробел: ")
nums = s.split()

numbers = []
for x in nums:
    numbers.append(float(x))
# 1
print("уникальные числа:")
for i in range(len(numbers)):
    found = False
    for j in range(len(numbers)):
        if i != j and numbers[i] == numbers[j]:
            found = True
    if not found:
        print(numbers[i])

# 2
print("повторяющтеся числа:")
for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1
    if count > 1:
        already = False
        for k in range(i):
            if numbers[k] == numbers[i]:
                already = True
        if not already:
            print(numbers[i])

# 3
print("чётные числа:")
for x in numbers:
    if type(x) == int and x % 2 == 0:
        print(x)

print("нечётные числа:")
for x in numbers:
    if type(x) == int and x % 2 != 0:
        print(x)

# 4
print("отрицательные числа:")
for x in numbers:
    if x < 0:
        print(x)

# 5
print("числа с плавающей точкой:")
for x in nums:
    if '.' in x:
        print(x)

# 6
sum5 = 0
for x in numbers:
    if type(x) == int and x % 5 == 0:
        sum5 += x
print("cумма чисел, кратных 5:", sum5)

# 7
max_num = numbers[0]
for x in numbers:
    if x > max_num:
        max_num = x
print("cамое большое число:", max_num)

# 8
min_num = numbers[0]
for x in numbers:
    if x < min_num:
        min_num = x
print("cамое маленькое число:", min_num)
