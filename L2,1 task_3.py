s = input("введите числа через пробел: ")
nums = s.split()

numbers = []
for i in nums:
    numbers.append(float(i))

max_num = numbers[0]
for i in numbers:
    if i > max_num:
        max_num = i

second_max = 0
for i in numbers:
    if i != max_num:
        if second_max == 0 or i > second_max:
            second_max = i

print("второе по величине число:", second_max)