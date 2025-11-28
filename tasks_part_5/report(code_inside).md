```
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Данные
data = [9, 5, 7, 7, 4, 10]
n = len(data)
mean = np.mean(data)
sigma = 1

# Уровень доверия и квантиль
alpha = 0.01
z_alpha = norm.ppf(1 - alpha / 2)

# Погрешность
delta = z_alpha * (sigma / np.sqrt(n))

# Доверительный интервал
confidence_interval = (mean - delta, mean + delta)

# График
x = np.linspace(mean - 3 * sigma, mean + 3 * sigma, 100)
y = norm.pdf(x, loc=mean, scale=sigma)

plt.plot(x, y)
plt.fill_between(x, y, where=((x >= confidence_interval[0]) & (x <= confidence_interval[1])), color='skyblue', alpha=0.7)
plt.axvline(mean, color='red', linestyle='dashed', linewidth=1, label=f'Среднее: {mean:.2f}')
plt.axvline(confidence_interval[0], color='green', linestyle='--', linewidth=1, label=f'Дов. интервал: ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f})')
plt.axvline(confidence_interval[1], color='green', linestyle='--', linewidth=1)

plt.title('Доверительный интервал для среднего значения')
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.legend()
plt.grid(True)
plt.show()

print(f"99% доверительный интервал: {confidence_interval}")
```

<img width="576" height="455" alt="image" src="https://github.com/user-attachments/assets/7d13df2b-d8fc-4db8-8207-5682f4b16431" />

`99% доверительный интервал: (5.948422090299438, 8.051577909700562)`

```
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Параметры нормального распределения
mu = 0  # Среднее значение
sigma = 1  # Стандартное отклонение

# Создаем массив значений x для построения графика
x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)

# Вычисляем значения функции плотности вероятности (PDF)
y = norm.pdf(x, mu, sigma)

# Вычисляем область, соответствующую 95.4% вероятности (два стандартных отклонения)
x_fill = np.linspace(mu - 2 * sigma, mu + 2 * sigma, 100)
y_fill = norm.pdf(x_fill, mu, sigma)

# Строим график
plt.plot(x, y)
plt.fill_between(x_fill, 0, y_fill, color='skyblue', alpha=0.7)

# Добавляем подписи и заголовок
plt.title('N(0,1)')
plt.xlabel('Значение признака')
plt.ylabel('Плотность вероятности')
plt.grid(True)

# Добавляем текст, указывающий на ширину доверительного интервала
plt.text(mu, 0.1, f'95.4%', ha='center', va='bottom') # Позиционирование текста может потребовать подстройки

# Добавляем вертикальные линии, отмечающие границы интервала
plt.axvline(x=mu - 2 * sigma, color='red', linestyle='--', linewidth=0.8)
plt.axvline(x=mu + 2 * sigma, color='red', linestyle='--', linewidth=0.8)


plt.show()

# Расчет вероятности
probability = norm.cdf(mu + 2 * sigma, mu, sigma) - norm.cdf(mu - 2 * sigma, mu, sigma)
```

<img width="576" height="455" alt="image" src="https://github.com/user-attachments/assets/807156b2-4e0e-4168-812b-fa74b5f6c25a" />

```
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Диапазон значений x
x = np.linspace(-3, 3, 500)

# Степени свободы
dfs = [1, 2, 5, 10, 20]

# Создаем график
plt.figure(figsize=(10, 6))

# Строим графики для каждой степени свободы
for df in dfs:
    # Вычисляем плотность распределения
    y = t.pdf(x, df)
    # Строим график
    plt.plot(x, y, label=f'df = {df}')

# Добавляем подписи и легенду
plt.title('Плотность распределения Стьюдента для разных степеней свободы')
plt.xlabel('x')
plt.ylabel('Плотность')
plt.legend()
plt.grid(True)

# Отображаем график
plt.show()
```

<img width="855" height="547" alt="image" src="https://github.com/user-attachments/assets/ee031fa5-467f-4477-b186-3e70dd678bc6" />
