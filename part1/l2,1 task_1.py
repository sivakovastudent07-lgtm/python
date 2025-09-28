s = input('vvedite stroky: ')
words = s.split( )
for i in range(len(words)):
    words[i] = words[i].lower()
    
for i in range(len(words)):
    count = 0
    for j in range(len(words)):
           if words[j]==words[i]:
               count+=1
               print( words[i], count)
            
unique = 0
for i in range(len(words)):
    found = False
    for j in range(i):
        if words[j] == words[i]:
            found = True
    if not found:
        unique += 1

print("Уникальных слов:", unique)