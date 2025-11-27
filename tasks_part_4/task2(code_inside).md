# ЗАДАЧА №2

Случайный процесс определяется формулой $X(t) = X {e}^{-t}$ $(t>0)$, где $X$ - случайная величина, распределенная по нормальному закону с параметрами $a$ и $σ^2$. Найти математическое ожидание $M(X(t))$, дисперсию $D(X(t))$, корреляционную $K_X(t_1,t_2)$ и нормированную корреляционную функции $ρ_x(t_1, t_2)$ случайного процесса.

# РЕШЕНИЕ

1. Математическое ожидание

$M(X \cdot e^{-t}) = e^{-t} \cdot M(X) = a \cdot e^{-t}$

2. Дисперсия

$D(X \cdot e^{-t}) = e^{-2t} \cdot D(X) = σ^2 \cdot e^{-2t}$

3. Корреляционная функция

$K_X(t_1,t_2) = M[(X \cdot e^{-t_1} - a \cdot e^{-t_1})(X \cdot e^{-t_2} - a \cdot e^{-t_2})] = e^{-(t_1 + t_2)} \cdot M[(X - a)(X - a)] = e^{-(t_1 + t_2)} \cdot D(X) = σ^2 \cdot e^{-(t_1 + t_2)}$

4. Нормированная корреляционная функция

$ρ_X(t_1,t_2) = \frac{D(X) \cdot e^{-(t_1+t_2)}}{\sigma \cdot e^{-t_1} \cdot σ \cdot e^{-t_2}} = 1$

```
import numpy as np
import matplotlib.pyplot as plt
import math

t = np.linspace(0, 5, 1000)
X = np.random.rand(1000)
x = X * np.exp(-t)
xa = 0.5 * x * np.exp(-t)
d = 1/12
dx = d * np.exp(-2*t)

plt.figure(figsize=(12, 5)) # Увеличим размер фигуры для лучшей читаемости

plt.subplot(1, 2, 1) # Создаем подграфик 1 из 2
plt.plot(t, x, label='x(t)')
plt.plot(t, xa, label='xa(t)')
plt.plot(t, dx, label='dx(t)')
plt.xlabel('Время (t)')
plt.ylabel('Значение')
plt.title('Зависимость x(t), xa(t) и dx(t) от времени')
plt.legend() # Добавляем легенду

plt.subplot(1, 2, 2) # Создаем подграфик 2 из 2
plt.hist(X, bins='sturges') # bins - количество столбцов гистограммы
plt.xlabel('Значение X')
plt.ylabel('Частота')
plt.title('Гистограмма распределения X')

plt.tight_layout() # Автоматически корректирует расположение подграфиков
plt.show()
```

<img width="1189" height="490" alt="image" src="https://github.com/user-attachments/assets/5cc666b8-0c87-4fb8-9102-4427ba4d6d91" />
