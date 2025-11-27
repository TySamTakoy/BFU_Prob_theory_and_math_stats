# ЗАДАЧА №3 СО ЗВЕЗДОЧКОЙ

<img width="1109" height="117" alt="image" src="https://github.com/user-attachments/assets/a09705e8-5942-4fc6-adc0-02ba43a91f3e" />


# РЕШЕНИЕ

Функция плотности вероятности для равномерного распределения на $[0; 1]$ равна $1$ на этом отрезке и 0 вне его. Сумма двух независимых случайных величин $X$ и $Y$ с PDF $f_X(x)$ и $f_Y(y)$ соответственно имеет PDF, который является сверткой:

$f_Z(z) = \int {f_X(x) ⋅ f_Y(z-x)}{dx}$

где $Z = X + Y$. В нашем случае:

$f_X(x) = 1$ для $0 ≤ x ≤ 1$, $0$ иначе

$f_Y(y) = 1$ для $0 ≤ y ≤ 1$, $0$ иначе

Свертка будет:

$f_Z(z) = \int_{0}^{1} {f_X(x) \cdot f_Y(z-x)}{dx}$

Нужно разбить интеграл на части в зависимости от значения z:

$\left\{\begin{aligned}0 ≤ z ≤ 1: f_Z(z) = \int_{0}^{z} {1}{dx} = z\\1 ≤ z ≤ 2: f_Z(z) = \int_{z-1}^{1} {1}{dx} = 2 - z\\z < 0 \; или \; z > 2: f_Z(z) = 0\end{aligned}\right.$

Таким образом, получаем треугольное распределение:

    Способ 1: Свертка функций плотности вероятности

```
import numpy as np
import matplotlib.pyplot as plt

def pdf_sum_uniform(z):
  """Функция плотности вероятности суммы двух равномерных величин."""
  if 0 <= z <= 1:
    return z
  elif 1 < z <= 2:
    return 2 - z
  else:
    return 0

z_values = np.linspace(0, 2, 100)
pdf_values = [pdf_sum_uniform(z) for z in z_values]

plt.plot(z_values, pdf_values)
plt.xlabel('z')
plt.ylabel('f_Z(z)')
plt.title('Функция плотности вероятности суммы двух равномерных величин')
plt.grid(True)
plt.show()
```

<img width="621" height="455" alt="image" src="https://github.com/user-attachments/assets/a4883c12-8294-46df-9b38-70b16d27febc" />

    Способ 2: Метод Монте-Карло

```
import numpy as np
import matplotlib.pyplot as plt

num_samples = 1000000
x = np.random.uniform(0, 1, num_samples)
y = np.random.uniform(0, 1, num_samples)
z = x + y

plt.hist(z, bins='sturges', density=True, alpha=0.7, label='Гистограмма')
z_values = np.linspace(0, 2, 100)
pdf_values = [pdf_sum_uniform(z) for z in z_values] # Используем функцию из Способа 1 для сравнения
plt.plot(z_values, pdf_values, label='Теоретическая PDF')
plt.xlabel('z')
plt.ylabel('Плотность вероятности')
plt.title('Гистограмма суммы двух равномерных величин (Монте-Карло)')
plt.legend()
plt.grid(True)
plt.show()
```

<img width="598" height="455" alt="image" src="https://github.com/user-attachments/assets/d5c60577-7927-4eb6-88be-92238a9b57b1" />

Оба метода показывают, что сумма двухравномерно распределенных случайных величин на $[0; 1]$ имеет треугольное распределение на $[0; 2]$. Метод Монте-Карло приближенный, точность увеличивается с ростом `num_samples`. Первый метод дает точное аналитическое решение.
