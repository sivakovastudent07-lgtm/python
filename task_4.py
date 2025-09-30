a = int(input("Введите сумму: "))

if a>= 100:
    hundreds = a//100
    a = a%100
else:
    hundreds = 0
    if a>=50:
        fifties=a//50
        a=a%50
    else:
        fifties = 0
        if a>=10:
            tens=a//10
            a=a%10
        else:
            tens= 0
            if a>=5:
                fives = a//5
                a=a%5
            else:
                fives = 0
                if a>=2:
                    two_rub=a//2
                    a=a%2
                else:
                    two_rub =0
                    if a>=1:
                        rubl =a
                    else:
                        rubl = 0
print('kol-vo 100: ', hundreds)
print('kol-vo 50: ', fifties)
print('kol-vo 10: ', tens)
print('kol-vo 5: ', fives)
print('kol-vo 2: ', two_rub)
print('kol-vo 1: ', rubl)
