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
  """
  Рассчитывает вероятность выучить билет за заданное время.

  Args:
    x: Время, затраченное на изучение билета (часы).
    poly: Полином, аппроксимирующий функцию обучения.

  Returns:
    Вероятность выучить билет.
  """
  return poly(x)

# Функция, которая рассчитывает вероятность сдать экзамен
def probability_pass(num_tickets, poly):
  """
  Рассчитывает вероятность сдать экзамен, учитывая количество билетов.

  Args:
    num_tickets: Количество билетов, которые необходимо выучить.
    poly: Полином, аппроксимирующий функцию обучения.

  Returns:
    Вероятность сдать экзамен.
  """
  # Вероятность выучить билет
  probability_learn_ticket = probability_learn(10/num_tickets, poly)

  # Вероятность вытащить этот билет на экзамене
  probability_draw_ticket = num_tickets / 10

  # Вероятность сдать экзамен
  probability_pass = probability_learn_ticket**num_tickets * probability_draw_ticket
  return probability_pass

# Находим оптимальное количество билетов
num_tickets = np.arange(1, 11) #  Создаем массив с количеством билетов от 1 до 10
probabilities = [probability_pass(n, poly) for n in num_tickets]  #  Рассчитываем вероятности сдачи для каждого количества билетов
# Оптимальное количество билетов
optimal_tickets = num_tickets[np.argmax(probabilities)]  #  Находим максимальную вероятность сдачи и получаем соответствующее количество билетов

# Вывод результатов
print(f"Оптимальное количество билетов для максимальной вероятности сдачи экзамена: {optimal_tickets}")
print(f"Вероятность сдачи при этом: {np.max(probabilities):.4f}")

# Строим график зависимости вероятности сдачи от количества билетов
plt.figure(1)
plt.plot(num_tickets, probabilities, label='Вероятность сдачи')
plt.xlabel('Количество билетов')
plt.ylabel('Вероятность')
plt.title('Зависимость вероятности сдачи от количества билетов')
plt.legend()

# Строим график зависимости вероятности выучить билет от времени
plt.figure(2)
x_time = np.linspace(0, 10, 100)  # Время на изучение билета
y_prob_learn = probability_learn(x_time, poly)  # Вероятность выучить билет
plt.plot(x_time, y_prob_learn, label='Вероятность выучить билет')
plt.xlabel('Время (часы)')
plt.ylabel('Вероятность')
plt.title('Зависимость вероятности выучить билет от времени')
plt.legend()

plt.show()
