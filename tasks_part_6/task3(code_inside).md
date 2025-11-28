# ЗАДАЧА №3

Выбрать два линейно коррелированных признака из своего датасет и вычислить линейную регрессию для них. Сделать для функции потерь MSE и MAE. Продемонстрировать результаты интерполяции и экстраполяции на основе регрессии.

# РЕШЕНИЕ

    train_test_split

    sklearn.model_selection.train_test_split(*arrays, test_size=None,
    train_size=None, random_state=None, shuffle=True, stratify=None)[source]
    
    Split arrays or matrices into random train and test subsets.

    Quick utility that wraps input validation, next(ShuffleSplit().split(X,
    y)), and application to input data into a single call for splitting (and
    optionally subsampling) data into a one-liner.

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

fuel_consumption = CO2['Fuel Consumption City (L/100 km)']
co2_emissions = CO2['CO2 Emissions(g/km)']

# Преобразование данных в NumPy массивы для scikit-learn
X = np.array(fuel_consumption).reshape(-1, 1)  # решейп в двумерный массив
y = np.array(co2_emissions)

# Разбиение данных на тренировочный и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # test_size - 20% для теста

# Создание и обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказание на тестовом наборе
y_pred = model.predict(X_test)

# Построение графика
plt.scatter(X_test, y_test, color='blue', label='Диаграмма рассеяния')
plt.plot(X_test, y_pred, color='red', label='Линейная регрессия')
plt.xlabel('Расход топлива в городе (л / 100км)')
plt.ylabel('Выбросы CO2 (г/км)')
plt.title(f'Уравнение линейной регрессии: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}') #intercept - свободный член уравнения прямой
plt.legend()
plt.show()
```

<img width="571" height="455" alt="image" src="https://github.com/user-attachments/assets/614e8a86-5a0f-4f6f-9ace-4350e713094b" />

---
> MSE (средняя квадратическая ошибка) — это оценка среднего значения квадрата ошибок, различие между предсказанием и фактическим значением. Эту метрику удобно использовать для выявления аномалий.

> MAE (средняя абсолютная ошибка) — это оценка того, насколько близки предсказания к фактическим значениями. Эта метрика менее чувствительна к выбросам и может дать общее представление о качестве модели.

> Простыми словами: если у нас сильные аномалии в значениях, то используем MAE; если аномалий мало, можно использовать MSE.
---

```
import numpy as np  # Импорт библиотеки NumPy для работы с массивами
import pandas as pd # Импорт библиотеки Pandas для работы с данными в формате DataFrame
from sklearn.metrics import mean_squared_error, mean_absolute_error # Импорт функций для вычисления MSE и MAE из библиотеки scikit-learn

def mse_loss(y_true, y_pred):
  """
  Вычисляет среднеквадратичную ошибку (MSE).

  Args:
    y_true: Массив истинных значений.
    y_pred: Массив предсказанных значений.

  Returns:
    MSE: Значение среднеквадратичной ошибки.
  """
  mse = mean_squared_error(y_true, y_pred)
  return mse

def mae_loss(y_true, y_pred):
  """
  Вычисляет среднюю абсолютную ошибку (MAE).

  Args:
    y_true: Массив истинных значений.
    y_pred: Массив предсказанных значений.

  Returns:
    MAE: Значение средней абсолютной ошибки.
  """
  mae = mean_absolute_error(y_true, y_pred)
  return mae

fuel_consumption = CO2['Fuel Consumption City (L/100 km)']
co2_emissions = CO2['CO2 Emissions(g/km)']

b = model.coef_[0]
c = model.intercept_

# Вычисление предсказанных значений выбросов CO2 по линейной модели
predicted_emissions = fuel_consumption * b + c

# Вычисление MSE и MAE
mse = mse_loss(co2_emissions, predicted_emissions)
mae = mae_loss(co2_emissions, predicted_emissions)

# Вывод результатов с проверкой на NaN значения
if not np.isnan(mse): # Проверка на NaN (Not a Number) для предотвращения ошибок
  print(f"Средняя квадратическая ошибка MSE: {mse}")
if not np.isnan(mae): # Проверка на NaN (Not a Number) для предотвращения ошибок
  print(f"Средняя абсолютная ошибка MAE: {mae}")
```

`Средняя квадратическая ошибка MSE: 528.3909921074217`

`Средняя абсолютная ошибка MAE: 14.332689402191853`
