import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

def f(x):
    return 1 / ((x - 2) * (x + 1))

y = f(x)
y = np.where(np.abs(y) > 100, np.nan, y)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$f(x) = \frac{1}{(x - 2)(x + 1)}$', color='blue')

plt.axvline(x=-1, color='red', linestyle='--', alpha=0.7, label='Разрывы (x = -1, x = 2)')
plt.axvline(x=2, color='red', linestyle='--', alpha=0.7)

plt.title('График функции с точками разрыва')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.ylim(-10, 10) 

plt.show()