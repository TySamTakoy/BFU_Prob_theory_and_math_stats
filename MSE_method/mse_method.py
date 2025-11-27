# MSE method через математику и полностью на рандоме, только ввод кол-ва n
# чем выше n, тем точнее построение
# вокруг исходного уравнения прямой, которое тоже в рандоме
# задаем диаграмму рассеяния через рандом и
# отыскиваем график и уравнение через MSE method

import numpy as np
import random as rnd
import matplotlib.pyplot as plt

print('Введите требуемое кол-во экспериментов:')
N = int(input())
sigma = rnd.uniform(0, 5) #стандартное отклонение из нормального распределения
k = rnd.uniform(-1, 1)
k = round(k, 3)
b = rnd.randint(-10, 10)
print('Исходные данные: f(x) =',k, 'x +', b)

f = np.array([k*z+b for z in range (N)])   #массив f по заданным значениям
                                           #по Z в диапазоне N
y = f + np.random.normal(0, sigma, N)

x = np.array(range(N))

mx = x.sum()/N                             #мат ожидание x

my = y.sum()/N                             #мат ожидание y

a2 = np.dot(x.T, x)/N                      #второй начальный момент
                                           #вместо sum(Xi ** 2)
                                           #используем перемножение
                                           #транспонированного вектора XT
                                           #на обычный вектор X

a11 = np.dot(x.T, y)/N                     #смешанный момент
                                           #вместо sum(Xi * Yi)
                                           #используем перемножение
                                           #транспонированного вектора XT
                                           #на вектор Y

k_mnk = (a11 - mx*my)/(a2 - mx**2)
b_mnk = my - k_mnk*mx
k_mnk = round(k_mnk, 3)
b_mnk = round(b_mnk, 3)
f_mnk = np.array([k_mnk*v+b_mnk for v in range(N)])
print('Коэффициенты полученные МНК: f_mnk(x) =', k_mnk, 'x +', b_mnk)

plt.plot(f)
plt.plot(f_mnk, c = 'green')
plt.scatter(x, y, s = 2, c = 'red')
plt.grid(True)
plt.show()
