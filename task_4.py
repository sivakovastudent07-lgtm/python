a = int(input("Введите сумму: "))

if a>= 100:
    h = a//100
    a = a%100
else:
    h = 0
    if a>=50:
        f=a//50
        a=a%50
    else:
        f = 0
        if a>=10:
            t=a//10
            a=a%10
        else:
            t= 0
            if a>=5:
                fv = a//5
                a=a%5
            else:
                fv = 0
                if a>=2:
                    tw=a//2
                    a=a%2
                else:
                    tw =0
                    if a>=1:
                        r =a
                    else:
                        r = 0
print('kol-vo 100: ', h)
print('kol-vo 50: ', f)
print('kol-vo 10: ', t)
print('kol-vo 5: ', fv)
print('kol-vo 2: ', tw)
print('kol-vo 1: ', r)
