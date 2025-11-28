# РЕШЕНИЕ

```
import random as rnd
import numpy as np
import matplotlib.pyplot as plt
```

    Syntax : random.normalvariate(mu, sigma)

    Parameters :

    mu : mean

    sigma : standard deviation

```
bb = [rnd.normalvariate(0,5) for i in range(100)]
x = np.linspace(0,10, 100)
y = 3 * x + bb

plt.scatter(x,y)

plt.title('Зависимость y = 3x + random.norm')

plt.xlabel('x')
plt.ylabel('y')

plt.show()
```

<img width="574" height="455" alt="image" src="https://github.com/user-attachments/assets/d32a03c8-1399-4893-b235-17352025dd72" />

```
k1 = 4

y1 = k1 * x

plt.scatter(x, y)
plt.plot(x, y1, color='red')

plt.title('Диаграмма рассеяния и угадываемая линейная \n регрессия в простейшем своем исполнении')

plt.xlabel('x')
plt.ylabel('y')

plt.show()
```

<img width="574" height="476" alt="image" src="https://github.com/user-attachments/assets/2e2f1504-54c4-4411-b499-913a47256a00" />

```
sum = np.sum(abs(y-y1))
print(f'{sum:.4f}')
```

`655.3516`

```
error_list=[]  # Инициализируем пустой список для хранения значений суммарных ошибок.

# Цикл перебирает значения k от 0 до 9.9 с шагом 0.1.
for i in range(100):
  k1 = i / 10  # Вычисляем значение k.  i/10 создаёт значения 0, 0.1, 0.2... 9.9
  y1 = k1 * x  # Вычисляем приближенные значения y используя текущее k.
  error = np.sum(abs(y-y1))  # Вычисляем суммарную абсолютную ошибку между истинными и приближенными значениями y.
  error_list.append(error)

plt.plot(error_list)

plt.xlabel("Значение k")
plt.ylabel("Суммарная абсолютная ошибка")
plt.title("Зависимость суммарной ошибки от значения k")

min_error = np.min(error_list)
min_k_index = np.argmin(error_list)
min_k = min_k_index / 10

print(f'Минимальная ошибка: {min_error:.4f}')
print(f'Индекс минимальной ошибки: {min_k_index}')

plt.show()
```

`Минимальная ошибка: 409.3361`
`Индекс минимальной ошибки: 29`

<img width="580" height="455" alt="image" src="https://github.com/user-attachments/assets/d6871d7e-48bb-4aca-aeaf-35dcce7e197a" />

```
error_list1=[]

# Цикл для вычисления суммы квадратов ошибок для разных значений k1
for i in range(100):
  k1 = i / 10  # Значение k1 варьируется от 0 до 10 с шагом 0.1
  y1 = k1 * x  # Вычисляем предсказанные значения y1 на основе k1 и x
  error = y - y1 # Разница между фактическими (y) и предсказанными (y1) значениями
  error_list1.append(np.sum(error**2)) # Сумма квадратов ошибок для данного k1

plt.plot(error_list1, linestyle='-')
plt.xlabel("Номер итерации (k1 = i/10)")
plt.ylabel("Сумма квадратов ошибок")
plt.title("Зависимость суммы квадратов ошибок от параметра k1")

# Находим минимальное значение суммы квадратов ошибок и его индекс
min_1 = np.min(error_list1)

print(f'{min_1:.4f}') # Вывод минимального значения суммы квадратов ошибок с точностью до 4 знаков после запятой
print(np.argmin(error_list1)) # Вывод индекса минимального значения (соответствует значению k1)

plt.show()
```

`2637.0238`

`29`

<img width="597" height="455" alt="image" src="https://github.com/user-attachments/assets/00a6fcaa-2f0f-4cf7-954d-dee590d733ea" />
