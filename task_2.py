s = input("Введите числа через пробел: ")
nums = []
for i in s.split():
    if '.' in i:
        nums = nums + [float(i)]
    else:
        nums = nums + [int(i)]

# 1
uniq = []
for x in nums:
    found = False
    for u in uniq:
        if u == x:
            found = True
            break
    if not found:
        uniq = uniq + [x]
print("1. уникальные числа:", uniq)

# 2
dups = []
for x in nums:
    count = 0
    for y in nums:
        if y == x:
            count = count + 1
    already = False
    for d in dups:
        if d == x:
            already = True
    if count > 1 and not already:
        dups = dups + [x]
print("2. повторки:", dups if dups else "отсутствуют")

# 3
even = []
odd = []
for x in nums:
    is_integer = False
    value = 0
    if type(x) == int:
        is_integer = True
        value = x
    elif type(x) == float and x == int(x):
        is_integer = True
        value = int(x)
    if is_integer:
        if value % 2 == 0:
            even = even + [x]
        else:
            odd = odd + [x]
print("3. чётные числа:", even if even else "отсутствуют")
print("нечётные числа:", odd if odd else "отсутствуют")

# 4
neg = []
for x in nums:
    if x < 0:
        neg = neg + [x]
print("4. отрицательные числа:", neg if neg else "отсутствуют")

# 5
floats = []
for x in nums:
    if type(x) == float and x != int(x):
        floats = floats + [x]
print("5. числа с плавающей точкой:", floats if floats else "отсутствуют")

# 6
sum5 = 0
for x in nums:
    is_int_val = (type(x) == int) or (type(x) == float and x == int(x))
    if is_int_val:
        n = int(x)
        if n % 5 == 0:
            sum5 = sum5 + n
print("6. сумма чисел, кратных 5:", sum5)

# 7
big = nums[0]
for x in nums:
    if x > big:
        big = x
print("7. самое большое число:", big)

# 8
small = nums[0]
for x in nums:
    if x < small:
        small = x
print("8. самое маленькое число:", small)