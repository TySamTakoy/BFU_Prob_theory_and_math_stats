# ЗАДАЧА №3

1.   Придумать свою случайную величину со значениями от 0 до 10 с помощью задания ее функции плотности вероятности.( не использовать нормальное распределение)
 В блокноте Google  Colab визуализировать ее.
2.   Визуализировать в Google  Colab ее функц распределения ( попробовать посчитать интеграл аналитически)
3.   найти чему равна вероятность того, что эта случайная величина будет принимать значения от 2 до 4.

Исходная функция плотности распределения вероятности:

$f(x)={e}^{-x} \sin x$

# РЕШЕНИЕ

```
import numpy as np
import matplotlib.pyplot as plt

# Определение функции плотности вероятности
def pdf(x):
  return np.exp(-x) * np.sin(x)

# Диапазон значений случайной величины
x = np.linspace(0, 10, 1000)

# Визуализация функции плотности вероятности
plt.figure(figsize=(8, 5))
plt.plot(x, pdf(x), label='Функция плотности вероятности')
plt.xlabel('x')
plt.ylabel('pdf(x)')
plt.title('Функция плотности вероятности случайной величины')
plt.grid(True)
plt.legend()
plt.show()
```

<img width="700" height="470" alt="image" src="https://github.com/user-attachments/assets/04b9fb33-3c06-4485-ae09-9e1f9e5504c7" />

Проинтегрируем исходную функцию и получим:

$∫f(x)=∫{e}^{-x} \sin x = -\frac{1}{2} {e}^{-x} (\sin x + \cos x) + C$

```
import numpy as np
import matplotlib.pyplot as plt

# Диапазон значений x
x = np.linspace(0, 10, 1000)

# Определяем функцию плотности вероятности (PDF)
def pdf(x):
    """
    Функция плотности вероятности случайной величины.

    Args:
        x: Значение случайной величины.

    Returns:
        Значение функции плотности вероятности в точке x.
    """
    return np.exp(-x) * np.sin(x)

# Определяем кумулятивную функцию распределения (CDF)
cdf = lambda x: quad(pdf, 0, x)[0]
"""
    Кумулятивная функция распределения (CDF).  Вычисляет интеграл от функции плотности вероятности от 0 до x.

    Использует функцию quad из библиотеки scipy.integrate для численного интегрирования.
    quad(pdf, 0, x)[0] возвращает значение интеграла (первый элемент кортежа, который возвращает quad).
"""

# Вычисляем вероятность того, что случайная величина будет принимать значения от 2 до 4
probability = cdf(4) - cdf(2)

# Выводим результат
print(f'Вероятность того, что эта случайная величина будет принимать значения от 2 до 4:  {probability:.4f} \n')

# Вычисляем значения функции распределения для всех точек x
y = [cdf(i) for i in x]

#  График функции распределения
plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('CDF(X)')
plt.title('График функции распределения CDF(X)')
plt.grid(True)
plt.show()
```

`Вероятность того, что эта случайная величина будет принимать значения от 2 до 4:  0.0463`

<img width="691" height="470" alt="image" src="https://github.com/user-attachments/assets/2b848e13-2e75-43d2-98ac-49f7d2cf33c9" />

Определим математическое ожидание:

$M(X)=\int_{-∞}^{+∞}{x \cdot f(x)}{dx}$

```
Syntax  :  numpy.trapz(y, x = None, dx = 1.0, axis = -1)


Parameters :

y  : [array_like] Input array to integrate.

x  : [array_like, optional] The sample points corresponding to the y values.
     If x is None, the sample points are assumed to be evenly spaced dx apart.
     The default is None.

dx  : [scalar, optional] The spacing between sample points when x is None. The default is 1.

axis  : [int, optional] The axis along which to integrate.


Return  :

trapz:  [float] Definite integral as approximated by trapezoidal rule.
```


```
import numpy as np
import matplotlib.pyplot as plt

# Диапазон значений x
x = np.linspace(0, 10, 1000)

def pdf(x):
  return np.exp(-x) * np.sin(x)

# Определяем cdf
cdf = lambda x: quad(pdf, 0, x)[0]

# Вычисляем математическое ожидание через интеграл в numpy (np.trapz)
expectation = np.trapz(x * pdf(x), x)

print(f'Математическое ожидание M(X): {expectation:.4f}')
```

`Математическое ожидание M(X): 0.5003`


```
import scipy.integrate as integ

def expect(x):
  return pdf(x)*x

integral, err = integ.quad (expect, 0, 10)
print(f'Математическое ожиадание M(X): {integral:.4f}')
```

`Математическое ожиадание M(X): 0.5003`

Определим дисперсию:

$D(X)=M((X-M(X))^2)$

$D(X) = M(X^2)-M(X)^2$

```
def expect2(x):
  return pdf(x)*x**2

integral2, err = integ.quad(expect2, 0, 10)
print(f'Математическое ожидание квадрата СВ M(X^2): {integral2:.4f}')

DX = integral2 - integral**2
print(f'Дисперсия D(X): {DX:.4f}')

print(f'Стандартное отклонение sigma: {DX**(1/2):.4f}')
```

`Математическое ожидание квадрата СВ M(X^2): 0.5035`
`Дисперсия D(X): 0.2532`
`Стандартное отклонение sigma: 0.5032`

