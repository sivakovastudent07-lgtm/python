a = input("Введите пароль: ")
if len(a) < 16:
    print('Слишком короткий')
elif a.isalpha() or a.isdigit:
    print('Слабый пароль')
else:
    print('Надёжный пароль')        