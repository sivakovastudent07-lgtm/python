import numpy as np
import matplotlib.pyplot as plt

x_deg = np.linspace(-360, 360, 721)
x_rad = np.deg2rad(x_deg) 
f_x = np.exp(np.cos(x_rad)) + np.log(np.cos(0.6 * x_rad)**2 + 1) * np.sin(x_rad)
h_x = -np.log((np.cos(x_rad) + np.sin(x_rad))**2 + 2.5) + 10

plt.figure(figsize=(15, 10))

plt.plot(x_deg, f_x, label='f(x) = e^cos(x) + ln(cos²(0.6x)+1)·sin(x)', linewidth=2)
plt.plot(x_deg, h_x, label='h(x) = -ln((cos(x)+sin(x))²+2.5) + 10', linewidth=2, linestyle='--')

plt.title('Графики функций f(x) и h(x) на интервале [-360°, 360°]')
plt.xlabel('x (градусы)')
plt.ylabel('y')
plt.grid(True, alpha=0.3)
plt.legend()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim(-360, 360)

plt.show()