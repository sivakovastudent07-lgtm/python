word1 = input("введите первое слово: ")
word2 = input("введите второе слово: ")

print(sorted(word1.lower()) == sorted(word2.lower()))