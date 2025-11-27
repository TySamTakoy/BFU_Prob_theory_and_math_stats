import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Определение функции Гаусса
def gaussian(x, mu, sigma):
  """
  Вычисляет значение функции Гаусса в точке x с заданными параметрами mu (среднее) и sigma (стандартное отклонение).

  Args:
    x: Значение аргумента функции.
    mu: Среднее значение.
    sigma: Стандартное отклонение.

  Returns:
    Значение функции Гаусса в точке x.
  """
  return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

# Параметры гауссова распределения
mu = 0  # Среднее значение
sigma = 1 # Стандартное отклонение

# Создание массива значений x от -5 до 5 с 1000 точками
x = np.linspace(-5, 5, 1000)

# Вычисление значений функции Гаусса для каждого x
y = gaussian(x, mu, sigma)

# Вычисление интеграла функции Гаусса от -бесконечности до x[i] для каждого x[i]
integral_values = []
for i in range(len(x)):
  integral, error = quad(gaussian, -np.inf, x[i], args=(mu, sigma))
  integral_values.append(integral)

# Построение графика функции Гаусса (синий) и её интеграла (зеленый)
plt.plot(x, y, color='blue', label='Функция Гаусса (PDF)')
plt.plot(x, integral_values, color='green', label='Интеграл Функции Гаусса (CDF)')
plt.grid(True) # Добавление сетки на график
plt.xlabel('x') # Подпись оси x
plt.ylabel('y') # Подпись оси y
plt.title('GAUSS PDF & CDF') # Заголовок графика
plt.legend() # Добавление легенды
plt.show()
