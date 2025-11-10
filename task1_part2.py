import numpy as np

print("введите расходы с января по декабрь:")
rashody = np.array([float(input(f"месяц {i + 1}: ")) for i in range(12)])

zima = [11, 0, 1]   # декабрь, январь, февраль
leto = [5, 6, 7]    # июнь, июль, август

sum_zima = rashody[zima].sum()
sum_leto = rashody[leto].sum()

if sum_zima > sum_leto:
    print("зимой расходф больше, чем летом")
elif sum_leto > sum_zima:
    print("летом расходов юольше, чем зимой")
else:
    print("зимой и летом расходы одинаковы")

max_rashod = rashody.max()
max_mes = np.where(rashody == max_rashod)[0] + 1  

print(f"наибольшие расходы ({max_rashod}) были в месяцах:", *max_mes)