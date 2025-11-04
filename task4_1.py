s1 = input("введите первый набор чисел через пробел: ")
s2 = input("введите второй набор чисел через пробел: ")
def numbers(s):
    nums = []
    for part in s.split():
        if '.' in part:
            nums.append(float(part))
        else:
            nums.append(int(part))
    return nums

nums1 = numbers(s1)
nums2 = numbers(s2)
set1 = set(nums1)
set2 = set(nums2)

common = set1 & set2 
only1 = set1 - set2 
only2 = set2 - set1
rest = only1 | only2  

def format_output(s):
    return sorted(s) if s else "отсутствуют"

print("числа, которые есть в обоих наборах:", format_output(common))
print("числа только в первом наборе:", format_output(only1))
print("числа только во втором наборе:", format_output(only2))
print("все числа, кроме общих:", format_output(rest))