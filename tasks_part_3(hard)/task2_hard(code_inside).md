# ЗАДАЧА №2 СО ЗВЕЗДОЧКОЙ

см. `task2_hard.zip`

<img width="153" height="130" alt="image" src="https://github.com/user-attachments/assets/a45f21a9-a705-490f-8b22-e02d8dc105a2" />

```
from google.colab import drive
drive.mount('/content/drive')

raw_x = open("/content/drive/My Drive/Colab Notebooks/raw_x.txt", "r")
raw_x_array = raw_x.readlines()
raw_x.close()
raw_x_array = [line.strip() for line in raw_x_array]
float_x = [float(x) for x in raw_x_array]

raw_y = open("/content/drive/My Drive/Colab Notebooks/raw_y.txt", "r")
raw_y_array = raw_y.readlines()
raw_y.close()
raw_y_array = [line.strip() for line in raw_y_array]
float_y = [float(y) for y in raw_y_array]

raw_y1 = open("/content/drive/My Drive/Colab Notebooks/raw_y1.txt", "r")
raw_y1_array = raw_y1.readlines()
raw_y1.close()
raw_y1_array = [line.strip() for line in raw_y1_array]
float_y1 = [float(y1) for y1 in raw_y1_array]

import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(x=float_x, y=float_y, mode='markers'))
fig.update_xaxes(tickformat=".2f")
fig.update_yaxes(tickformat=".2f")
fig.show()

fig = go.Figure(data=go.Scatter(x=float_x, y=float_y1, mode='markers'))
fig.update_xaxes(tickformat=".2f")
fig.update_yaxes(tickformat=".2f")
fig.show()
```

<img width="1301" height="388" alt="image" src="https://github.com/user-attachments/assets/6bfbfa0a-13d9-41ba-bb81-f1261699ac2a" />

<img width="1285" height="385" alt="image" src="https://github.com/user-attachments/assets/01eca29b-8c0c-4168-8990-a3fe2f1d7363" />

```
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(np.array(float_x).reshape(-1, 1), np.array(float_y))

# Получение коэффициентов регрессии
slope = model.coef_[0]
intercept = model.intercept_

# Формула регрессии
regression_formula = f"y = {slope:.2f}x + {intercept:.2f}"

# Предсказания для построения графика
predicted_y = model.predict(np.array(float_x).reshape(-1, 1))

# Создание графика
fig = go.Figure(data=[
    go.Scatter(x=float_x, y=float_y, mode='markers', name='Данные'),
    go.Scatter(x=float_x, y=predicted_y, mode='lines', name='Регрессия')
])

# Форматирование осей
fig.update_xaxes(tickformat=".2f")
fig.update_yaxes(tickformat=".2f")

# Добавление формулы регрессии на график
fig.add_annotation(
    x=0.5,
    y=0.1,
    xref="paper",
    yref="paper",
    text=regression_formula,
    showarrow=False,
    font=dict(size=16)
)

fig.show()
```

<img width="1363" height="379" alt="image" src="https://github.com/user-attachments/assets/ffedb141-abba-43a3-859d-4a3af197ec7a" />

*   `kernel='gaussian'`: Этот аргумент задаёт тип ядра для оценки плотности. `'gaussian'` означает, что будет использоваться гауссово ядро. Другие возможные ядра включают `'tophat'`, `'epanechnikov'`, `'exponential'`, `'linear'`, `'cosine'`. Выбор ядра может влиять на результат. Гауссово ядро обычно хорошее, поскольку оно плавно изменяется.
*   `bandwidth=bandwidth_y`: Это один из самых важных параметров. Он определяет ширину ядра. `bandwidth_y` должно быть положительным числом. Чем больше `bandwidth`, тем плавнее будет кривая плотности, но она будет менее точной в отражении детали распределения данных. Чем меньше `bandwidth`, тем больше “пиков” будет на кривой плотности, но она может слишком сильно зависеть от шума и случайных вариаций данных. Правильный выбор `bandwidth` очень важен и часто требует некоторой подстройки. Часто используют методы оценки `bandwidth` автоматически, например, с помощью `bandwidth_selector`.

```
import numpy as np
import plotly.graph_objects as go
from sklearn.neighbors import KernelDensity

# Преобразуем списки в массивы NumPy, необходимые для scikit-learn
x = np.array(float_x).reshape(-1, 1)  # Reshape для работы KDE
y = np.array(float_y).reshape(-1, 1)

# Определяем параметры KDE.  Bandwidth - влияет на гладкость оценки.
# Правило Скотта
bandwidth_y = 1.06 * np.std(y) * len(y)**(-1/5)  # для y

# Создаем объекты KDE для y и y1
kde_y = KernelDensity(kernel='gaussian', bandwidth=bandwidth_y).fit(y)

# Создаем сетку для оценки плотности
x_grid = np.linspace(min(min(float_y), min(float_y1)) - 1, max(max(float_y), max(float_y1)) + 1, 100).reshape(-1,1) # расширенный диапазон для визуализации

# Вычисляем плотность вероятности
pdf_y = np.exp(kde_y.score_samples(x_grid))

# Визуализируем результаты с помощью Plotly
fig = go.Figure()

fig.add_trace(go.Scatter(x=x_grid.flatten(), y=pdf_y, mode='lines', name='PDF оценка для y'))

fig.update_layout(
    title='PDF оценка для y',
    xaxis_title='y',
    yaxis_title='Плотность вероятности',
    width=800,
    height=600
)

fig.show()
```

<img width="738" height="553" alt="image" src="https://github.com/user-attachments/assets/9fe83e6f-34c2-406a-8a96-4ccbb81b18a0" />

```
np.mean(y)
```

`50.118971815102356`

```
np.std(y)
```

`176.62127340121006`

```
import numpy as np
from scipy.integrate import cumtrapz

x_grid = np.linspace(min(float_y) - 1, max(float_y) + 1, 100)

# Вычисляем CDF с помощью cumtrapz (трапецеидальное правило)
cdf_y = cumtrapz(pdf_y, x_grid)

# Нормализуем CDF, чтобы он достигал 1 в конце
cdf_y = cdf_y / cdf_y[-1]

x_grid = x_grid[1:]

# Визуализация PDF и CDF с помощью Plotly
fig = go.Figure()

fig.add_trace(go.Scatter(x=x_grid, y=cdf_y,
                         mode='lines',
                         name='CDF оценки для y'))

fig.update_layout(title='CDF оценка для y',
                  xaxis_title='y',
                  yaxis_title='Кумулятивная вероятность',
                  width=800,
                  height=600)

fig.show()
```

<img width="706" height="537" alt="image" src="https://github.com/user-attachments/assets/4e086885-b059-4c4c-9e57-8d2d9f1dc32f" />

```
import numpy as np
from sklearn.neighbors import KernelDensity
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='median')

# Преобразуем списки в массивы NumPy, необходимые для scikit-learn
x = np.array(float_x).reshape(-1, 1)  # Reshape для работы KDE
y1 = imputer.fit_transform(np.array(float_y1).reshape(-1, 1))

# Определяем параметры KDE.  Bandwidth (bandwidth) - важный параметр, влияющий на гладкость оценки.
# Правило Скотта
bandwidth_y1 = 1.06 * np.std(y) * len(y)**(-1/5)  # для y1

# Создаем объекты KDE для y1
kde_y1 = KernelDensity(kernel='gaussian', bandwidth=bandwidth_y1).fit(y1)

# Создаем сетку для оценки плотности
x_grid = np.linspace(min(min(float_y), min(float_y1)) - 1, max(max(float_y), max(float_y1)) + 1, 100).reshape(-1,1) # расширенный диапазон для визуализации

# Вычисляем плотность вероятности
pdf_y1 = np.exp(kde_y1.score_samples(x_grid))


# Визуализируем результаты с помощью Plotly
fig = go.Figure()

fig.add_trace(go.Scatter(x=x_grid.flatten(), y=pdf_y1, mode='lines',
                         name='PDF оценки для y1'))

fig.update_layout(title='PDF оценка для y1',
                  xaxis_title='y1',
                  yaxis_title='Плотность вероятности',
                  width=800,
                  height=600)


fig.show()
```

<img width="741" height="543" alt="image" src="https://github.com/user-attachments/assets/2acd238a-9d03-443b-8906-94dbe958df12" />

```
np.mean(y1)
```

`8.331949948844718`

```
np.std(y1)
```

`0.7338872337960554`

```
import numpy as np
from scipy.integrate import cumtrapz

x_grid = np.linspace(min(float_y) - 1, max(float_y) + 1, 100)  # Теперь одномерный массив
cdf_y1 = cumtrapz(pdf_y1, x_grid)
cdf_y1 = cdf_y1 / cdf_y1[-1]
x_grid = x_grid[1:]

fig = go.Figure()

fig.add_trace(go.Scatter(x=x_grid, y=cdf_y1, mode='lines',
                         name='CDF оценка для y'))

fig.update_layout(title='CDF оценка для y',
                  xaxis_title='y',
                  yaxis_title='Кумулятивная вероятность',
                  width=800,
                  height=600)

fig.show()
```

<img width="710" height="537" alt="image" src="https://github.com/user-attachments/assets/8f7fb408-8541-47f7-abf5-e67ddef74e8f" />
