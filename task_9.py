ip = input("Введите IP-адрес: ")
parts = ip.split(".")

if len(parts) == 4:
    if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit() and parts[3].isdigit():
        a, b, c, d = int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3])
        if 0 <= a <= 255 and 0 <= b <= 255 and 0 <= c <= 255 and 0 <= d <= 255:
            print("Корректный IP-адрес")
        else:
            print("Некорректный IP-адрес")
    else:
        print("Некорректный IP-адрес")
else:
    print("Некорректный IP-адрес")
