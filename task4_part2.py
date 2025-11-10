import numpy as np
from scipy import integrate

print("вычисление интегралаот функции x^2 · ln(x + 1) dx")

a = float(input("введите нижний предел интегрирования (a): "))
b = float(input("введите верхний предел интегрирования (b): "))
if a < -1:
    print("функция ln(x+1) не определена при x <= -1")
elif a >= b:
    print("нижний предел должен быть меньше верхнего")
else:
    result, _ = integrate.quad(f, a, b)
    print(f"Значение интеграла от {a} до {b} = {result:.6f}")
def f(x):
    return x**2 * np.log(x + 1)
