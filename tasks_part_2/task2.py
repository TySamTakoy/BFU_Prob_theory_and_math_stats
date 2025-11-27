import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import pchip_interpolate
from numpy.polynomial import Polynomial

# Точки для построения функции обучения
x_data = np.array([0, 1, 10])
y_data = np.array([0, 0.33, 0.95])

# Монотонная интерполяция с помощью pchip
x = np.linspace(0, 10, 100)
y_pchip = pchip_interpolate(x_data, y_data, x)

# Аппроксимация полиномом
poly = Polynomial.fit(x, y_pchip, 3)  # 3 - степень полинома

# Ограничение по y=1
y_poly = poly(x)
y_poly[y_poly > 1] = 1

# Функция, которая рассчитывает вероятность выучить билет
def probability_learn(x, poly):
  return poly(x)

# Строим график зависимости вероятности выучить билет от времени
plt.figure(2)
x_time = np.linspace(0, 10, 100)  # Время на изучение билета
y_prob_learn = probability_learn(x_time, poly)  # Вероятность выучить билет
plt.plot(x_time, y_prob_learn, label='Вероятность выучить билет (полином)')
plt.xlabel('Время (часы)')
plt.ylabel('Вероятность')
plt.title('Зависимость вероятности выучить билет от времени')
plt.legend()

# Определяем функции обучаемости
def func_kuklevsky(x):
    return np.where(x < 1, 0.33 * x, 0.95 - 0.62 * np.exp(-(x - 1) / 4))

def func_aleschenko(x):
    return 1 - np.exp(-x / 3)

def func_ryabov(x):
    return 1 - (1 - 0.33) * np.exp(-x / 4)

# Строим графики всех функций на одном рисунке
plt.figure(3)
plt.plot(x_time, func_kuklevsky(x_time), label='Куклевский')
plt.plot(x_time, func_aleschenko(x_time), label='Алещенко')
plt.plot(x_time, func_ryabov(x_time), label='Рябов')
plt.plot(x_time, y_prob_learn, label='Полином')
plt.scatter(x_data, y_data, color='red', label='Точки данных') #  Добавляем точки данных на график

plt.xlabel('Время (часы)')
plt.ylabel('Вероятность')
plt.title('Функции обучаемости')
plt.xlim(0, 10)
plt.ylim(0, 1)
plt.legend()

plt.show()
