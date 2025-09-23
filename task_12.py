minutes = int(input("Минуты разговора: "))
sms = int(input("Количество SMS: "))
data = int(input("Интернет-трафик (МБ): "))

base = 24.99
extra_minutes = 0
extra_sms = 0
extra_data = 0

if minutes > 60:
    extra_minutes = (minutes - 60) * 0.89
if sms > 30:
    extra_sms = (sms - 30) * 0.59
if data > 1024:  
    extra_data = (data - 1024) * 0.79

subtotal = base + extra_minutes + extra_sms + extra_data
tax = subtotal * 0.02
total = subtotal + tax

print("Базовая стоимость тарифа: " + str(round(base, 2)) + " руб.")
if extra_minutes > 0:
    print("Доп. минуты: " + str(round(extra_minutes, 2)) + " руб.")
if extra_sms > 0:
    print("Доп. SMS: " + str(round(extra_sms, 2)) + " руб.")
if extra_data > 0:
    print("Доп. интернет: " + str(round(extra_data, 2)) + " руб.")
print("Налог: " + str(round(tax, 2)) + " руб.")
print("Итого к оплате: " + str(round(total, 2)) + " руб.")
