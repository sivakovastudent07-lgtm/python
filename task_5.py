n = int(input("Введите число: "))

if n % 7 == 0:
    print("Магическое число!")
else:
    #до трех знаков
    if n < 10:
        s = n
    elif n < 100:
        s = n // 10 + n % 10
    elif n < 1000:
        s = n // 100 + (n // 10) % 10 + n % 10
    else:
        print("Число большое")
        s = 0

    if s !=0:
        print("Сумма цифр =", s)