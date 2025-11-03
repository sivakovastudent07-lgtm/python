s1 = input("введите первый набор чисел через пробел: ")
s2 = input("введите второй набор чисел через пробел: ")

nums1 = []
for i in s1.split():
    if '.' in i:
        nums1 = nums1 + [float(i)]
    else:
        nums1 = nums1 + [int(i)]

nums2 = []
for i in s2.split():
    if '.' in i:
        nums2 = nums2 + [float(i)]
    else:
        nums2 = nums2 + [int(i)]

#числа, которые есть в обоих наборах
common = []
for x in nums1:
    #есть ли x в nums2
    found = False
    for y in nums2:
        if x == y:
            found = True
            break
    #не добавлено ли уже в common
    already = False
    for z in common:
        if z == x:
            already = True
            break
    if found and not already:
        common = common + [x]

#числа из первого, которых нет во втором
only1 = []
for x in nums1:
    found = False
    for y in nums2:
        if x == y:
            found = True
            break
    #если нет во втором и ещ не добавлено
    already = False
    for z in only1:
        if z == x:
            already = True
            break
    if not found and not already:
        only1 = only1 + [x]

#есть только во втором 
only2 = []
for x in nums2:
    found = False
    for y in nums1:
        if x == y:
            found = True
            break
    already = False
    for z in only2:
        if z == x:
            already = True
            break
    if not found and not already:
        only2 = only2 + [x]

rest = only1 + only2
print("числа, которые есть в обоих наборах:", common if common else "отсутствуют")
print("числа только в первом наборе:", only1 if only1 else "отсутствуют")
print("числа только во втором наборе:", only2 if only2 else "отсутствуют")
print("все числа, кроме общих:", rest if rest else "отсутствуют")