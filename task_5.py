word1 = input("введите первое слово: ")
word2 = input("введите второе слово: ")

s1 = ""
for c in word1:
    s1 +=c.lower()

s2 = ""
for c in word2:
    s2 += c.lower()

if len(s1) != len(s2):
    print(False)
else:
    list1 = []
    for c in s1:
        list1 += [c]

    list2 = []
    for c in s2:
        list2 += [c]

    temp = []
    for c in list2:
        temp += [c]

    anagram = True
    for c1 in list1:
        found = False
        new_temp = []
        removed = False
        for c2 in temp:
            if not removed and c1 == c2:
                removed = True  
            else:
                new_temp += [c2]
        if removed:
            temp = new_temp
        else:
            anagram = False
            break

    print(anagram)