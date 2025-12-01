text = input("введите текст: ")
words = text.split()
count = {}

for word in words:
    word = word.lower()  
    if word in count:
        count[word] += 1 
    else:
        count[word] = 1 

unique = len(count)

print(" слова их количества:")
print(count)
print("уникальные слова:", unique)