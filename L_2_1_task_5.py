word1 = input('введите первое слово')
word2 = input('введите втроео слово')
if len(word1) != len(word2):
    print("false")
else:
    letters1 = []
    letters2 = []

    for letter in word1:
        letters1.append(letter)

    for letter in word2:
        letters2.append(letter)

    is_anagram = True
    for letter in letters1:
        if letters1.count(letter) != letters2.count(letter):
            is_anagram = False
            break

    if is_anagram:
        print("true")
    else:
        print("false")