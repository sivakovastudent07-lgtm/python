s = input("Введите числа через пробел: ")
nums = []
for i in s.split():
    if '.' in i:
        nums = nums + [float(i)]
    else:
        nums = nums + [int(i)]

if len(nums) < 2:
    print("Нужно ввести хотя бы два числа.")
else:
    max1 = nums[0]
    for x in nums:
        if x > max1:
            max1 = x

    max2 = None
    for x in nums:
        if x != max1:
            if max2 is None or x > max2:
                max2 = x

print("второе по величине число:", max2)