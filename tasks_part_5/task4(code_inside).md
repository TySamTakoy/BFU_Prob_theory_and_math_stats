# ЗАДАНИЕ №4

Путем численной симуляции показать, что оценка дисперсии посредством величины среднеквадратического отклонения быстрее сходится для нормального распределения, чем для равномерного распределения случайной величины.

# РЕШЕНИЕ

```
import numpy as np
import matplotlib.pyplot as plt

# Параметры симуляции
n_samples = 1000  # Максимальный размер выборки
n_simulations = 100 # Количество симуляций для каждого размера выборки

# Генерация данных
sample_sizes = np.arange(10, n_samples + 1, 10)  # Размеры выборок

normal_mse = []
uniform_mse = []

for n in sample_sizes:
    normal_errors = []
    uniform_errors = []
    for _ in range(n_simulations):
        # Нормальное распределение
        normal_sample = np.random.normal(loc=0, scale=1, size=n)
        normal_estimate = np.var(normal_sample, ddof=1) # Вычисляет несмещенную оценку дисперсии (используется ddof=1). Если ddof=0, то вычисляет смещенную оценку
        normal_errors.append((normal_estimate - 1)**2) # (Оценка - истинное значение)^2

        # Равномерное распределение
        uniform_sample = np.random.uniform(low=-np.sqrt(3), high=np.sqrt(3), size=n) # дисперсия = 1
        uniform_estimate = np.var(uniform_sample, ddof=1)
        uniform_errors.append((uniform_estimate - 1)**2)

    normal_mse.append(np.sqrt(np.mean(normal_errors))) #MSE ошибок для нормального распределения
    uniform_mse.append(np.sqrt(np.mean(uniform_errors))) #MSE ошибок для равномерного распределения

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(sample_sizes, normal_mse, label='Нормальное распределение')
plt.plot(sample_sizes, uniform_mse, label='Равномерное распределение')
plt.xlabel('Размер выборки')
plt.ylabel('Среднеквадратичное отклонение оценки дисперсии')
plt.title('Сходимость оценки дисперсии')
plt.legend()
plt.grid(True)
plt.show()
```

<img width="846" height="547" alt="image" src="https://github.com/user-attachments/assets/e83ab228-dc58-4f22-bd98-d008d0cd92a8" />
