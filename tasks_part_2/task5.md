# ЗАДАЧА №5

Построить поверхность двумерной случайной величины $Z$, где случайные величины $X$ и $Y$ распределены по нормальную закону  с математическими ожиданиями и дисперсиями: $M(X)=1$, $M(Y)=1$, $D(X) = 2$, $D(Y) = 2$. Построить условные вероятности $X=Y$ и $X<Y$. Использовать библиотеку plotly.

<img width="963" height="524" alt="image" src="https://github.com/user-attachments/assets/5fc25de1-5eb6-451d-9a5d-87046c651753" />

# РЕШЕНИЕ

```
import numpy as np
import plotly.graph_objects as go

# Параметры двумерного нормального распределения:
m_x = 1 # m_x - математическое ожидание по оси X
m_y = 1 # m_y - математическое ожидание по оси Y
sigma_x = np.sqrt(2) # sigma_x - стандартное отклонение по оси X
sigma_y = np.sqrt(2) # sigma_y - стандартные отклонение по оси Y

# Диапазон значений для построения графика.
#  Отображается область, охватывающая примерно 99.7% вероятности (правило 3 сигм).
x_range = np.linspace(m_x - 3 * sigma_x, m_x + 3 * sigma_x, 100)
y_range = np.linspace(m_y - 3 * sigma_y, m_y + 3 * sigma_y, 100)

# Создание сетки координат для вычисления плотности вероятности.
X, Y = np.meshgrid(x_range, y_range) #  np.meshgrid создает две матрицы координат X и Y, где каждая ячейка содержит координаты (x, y) точки на плоскости.

# Функция плотности вероятности (PDF) для двумерного нормального распределения.
#  Предполагается, что X и Y независимы.
def bi_normal_pdf(x, y, m_x, m_y, sigma_x, sigma_y):
    """
    Вычисляет значение функции плотности вероятности для двумерного нормального распределения в точке (x, y).

    Args:
        x: Значение по оси X.
        y: Значение по оси Y.
        m_x: Математическое ожидание по оси X.
        m_y: Математическое ожидание по оси Y.
        sigma_x: Стандартное отклонение по оси X.
        sigma_y: Стандартное отклонение по оси Y.

    Returns:
        Значение функции плотности вероятности в точке (x, y).
    """
    # Плотность вероятности для одномерного нормального распределения по оси X
    pdf_x = (1 / (sigma_x * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - m_x) / sigma_x)**2)
    # Плотность вероятности для одномерного нормального распределения по оси Y
    pdf_y = (1 / (sigma_y * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((y - m_y) / sigma_y)**2)
    # Так как X и Y независимы, общая плотность вероятности - произведение плотностей по осям.
    return pdf_x * pdf_y

# Вычисление плотности вероятности для каждой точки на сетке.  Результат - матрица Z.
Z = bi_normal_pdf(X, Y, m_x, m_y, sigma_x, sigma_y)

# Построение трехмерного графика поверхности плотности вероятности с помощью Plotly.
fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z)])
fig.update_layout(title="Поверхность двумерной случайной величины Z",
                  scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"),
                  width=800, height=600)
fig.show()
```

<img width="791" height="589" alt="image" src="https://github.com/user-attachments/assets/96b66914-e442-41a0-8211-2854dc639904" />

```
z_equal = [] # Инициализируем пустой список для хранения результатов

# Вычисляем условную вероятность P(X=Y)  в дискретном приближении.  На самом деле, это не совсем условная вероятность,
# а скорее плотность вероятности  при условии X=Y.  Для получения истинной вероятности нужно проинтегрировать.
for i in range(len(x_range)): #  Для каждой точки x вычисляем плотность вероятности при условии X=Y, т.е. когда x=y
  z_equal.append(bi_normal_pdf(x_range[i], x_range[i], m_x, m_y, sigma_x, sigma_y))
  # z_equal теперь содержит приближенное значение плотности вероятности P(X=Y) в каждой точке x_range.
# print(z_equal)

# Построение графика условной вероятности X=Y
fig_x_equal_y = go.Figure(data=[go.Scatter3d(x=x_range, y=x_range, z=z_equal)])
fig_x_equal_y.update_layout(title="Условная вероятность X=Y", scene = dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z",), width=800, height=600)
fig_x_equal_y.show()
```

<img width="791" height="577" alt="image" src="https://github.com/user-attachments/assets/fb800e5f-57c2-4b91-b432-6ff1c40d5c92" />

```
import numpy as np
import plotly.graph_objects as go

# Параметры распределений
m_x = 1
m_y = 1
sigma_x = np.sqrt(2)
sigma_y = np.sqrt(2)

# Диапазон для графиков
x_range = np.linspace(m_x - 3 * sigma_x, m_x + 3 * sigma_x, 100)
y_range = np.linspace(m_y - 3 * sigma_y, m_y + 3 * sigma_y, 100)

# Создание сетки
X, Y = np.meshgrid(x_range, y_range)

# Функция плотности вероятности (PDF) для двумерного нормального распределения
def bi_normal_pdf(x, y, m_x, m_y, sigma_x, sigma_y):
    pdf_x = (1 / (sigma_x * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - m_x) / sigma_x)**2)
    pdf_y = (1 / (sigma_y * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((y - m_y) / sigma_y)**2)
    return pdf_x * pdf_y

# Вычисление плотности вероятности для каждой точки на сетке
Z = bi_normal_pdf(X, Y, m_x, m_y, sigma_x, sigma_y)

# Построение поверхности двумерной случайной величины Z
fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z)])
fig.update_layout(title="Поверхность двумерной случайной величины Z и условной вероятности X=Y",
                  scene = dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z",), width=800, height=600)

# Вычисление условной вероятности для X=Y
z_equal = []
for i in range(len(x_range)):
   z_equal.append(bi_normal_pdf(x_range[i], x_range[i], m_x, m_y, sigma_x, sigma_y))

# Построение графика условной вероятности X=Y
fig.add_trace(go.Scatter3d(x=x_range, y=x_range, z=z_equal, line=dict(color='red', width=3)))
```

<img width="794" height="532" alt="image" src="https://github.com/user-attachments/assets/9662b57d-b5b0-4054-8367-7065cc3c408b" />

```
# Вычисление условной вероятности для X<Y
z_less = []
x_less = []
y_less = []
for i in range(len(x_range)):
    for j in range(len(y_range)):
        if x_range[i] < y_range[j]:
            z_less.append(bi_normal_pdf(x_range[i], y_range[j], m_x, m_y, sigma_x, sigma_y))
            x_less.append(x_range[i])
            y_less.append(y_range[j])

# Построение графика условной вероятности X<Y
fig_x_less_y = go.Figure(data=[go.Scatter3d(x=x_less, y=y_less, z=z_less, mode='markers')])
fig_x_less_y.update_layout(title="Условная вероятность X<Y", scene = dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z",), width=800, height=600)
fig_x_less_y.show()
```

<img width="789" height="537" alt="image" src="https://github.com/user-attachments/assets/1f52e1cd-ef0d-412a-96dc-9b2acf30e5a2" />

```
import numpy as np
import plotly.graph_objects as go

# Параметры распределений
m_x = 1
m_y = 1
sigma_x = np.sqrt(2)
sigma_y = np.sqrt(2)

# Диапазон для графиков
x_range = np.linspace(m_x - 3 * sigma_x, m_x + 3 * sigma_x, 100)
y_range = np.linspace(m_y - 3 * sigma_y, m_y + 3 * sigma_y, 100)

# Создание сетки
X, Y = np.meshgrid(x_range, y_range)

# Функция плотности вероятности (PDF) для двумерного нормального распределения
def bi_normal_pdf(x, y, m_x, m_y, sigma_x, sigma_y):
    pdf_x = (1 / (sigma_x * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - m_x) / sigma_x)**2)
    pdf_y = (1 / (sigma_y * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((y - m_y) / sigma_y)**2)
    return pdf_x * pdf_y

# Вычисление плотности вероятности для каждой точки на сетке
Z = bi_normal_pdf(X, Y, m_x, m_y, sigma_x, sigma_y)

# Построение поверхности двумерной случайной величины Z
fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z)])
fig.update_layout(title="Поверхность двумерной случайной величины Z и условной вероятности X<Y",
                  scene = dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z",), width=800, height=600)

# Вычисление условной вероятности для X<Y
z_less = []
x_less = []
y_less = []
for i in range(len(x_range)):
    for j in range(len(y_range)):
        if x_range[i] < y_range[j]:
            z_less.append(bi_normal_pdf(x_range[i], y_range[j], m_x, m_y, sigma_x, sigma_y))
            x_less.append(x_range[i])
            y_less.append(y_range[j])

# Построение поверхности двумерной случайной величины Z
fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z),
      go.Scatter3d(x=x_less, y=y_less, z=z_less, mode='markers', marker=dict(color='red', size=3))])
fig.update_layout(title="Поверхность двумерной случайной величины Z и условной вероятности X<Y",
                  scene = dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z",), width=800, height=600)
fig.show()
```

<img width="768" height="541" alt="image" src="https://github.com/user-attachments/assets/7d1502b3-0888-434c-95a4-b7dfd03f5cb8" />

```
import numpy as np
import plotly.graph_objects as go
from scipy.integrate import quad

# Параметры двумерного нормального распределения
m_x = 1  # Математическое ожидание по оси X
m_y = 1  # Математическое ожидание по оси Y
sigma_x = np.sqrt(2)  # Стандартное отклонение по оси X
sigma_y = np.sqrt(2)  # Стандартное отклонение по оси Y

# Диапазон для графиков (увеличен для лучшей визуализации)
x_range = np.linspace(m_x - 3 * sigma_x, m_x + 3 * sigma_x, 50)
y_range = np.linspace(m_y - 3 * sigma_y, m_y + 3 * sigma_y, 50)

# Создание сетки координат
X, Y = np.meshgrid(x_range, y_range)

# Функция плотности вероятности (PDF) для двумерного нормального распределения
def bi_normal_pdf(x, y, m_x, m_y, sigma_x, sigma_y):
    """
    Вычисляет значение функции плотности вероятности (PDF) для двумерного нормального распределения.

    Args:
        x: Значение по оси X.
        y: Значение по оси Y.
        m_x: Математическое ожидание по оси X.
        m_y: Математическое ожидание по оси Y.
        sigma_x: Стандартное отклонение по оси X.
        sigma_y: Стандартное отклонение по оси Y.

    Returns:
        Значение PDF в точке (x, y).  Предполагается независимость X и Y.
    """
    pdf_x = (1 / (sigma_x * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - m_x) / sigma_x)**2)
    pdf_y = (1 / (sigma_y * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((y - m_y) / sigma_y)**2)
    return pdf_x * pdf_y

# Функция кумулятивной функции распределения (CDF) для двумерного нормального распределения
def bi_normal_cdf(x, y, m_x, m_y, sigma_x, sigma_y):
    """
    Вычисляет значение кумулятивной функции распределения (CDF) для двумерного нормального распределения
    с помощью численного интегрирования.

    Args:
        x: Верхний предел интегрирования по оси X.
        y: Верхний предел интегрирования по оси Y.
        m_x: Математическое ожидание по оси X.
        m_y: Математическое ожидание по оси Y.
        sigma_x: Стандартное отклонение по оси X.
        sigma_y: Стандартное отклонение по оси Y.

    Returns:
        Значение CDF в точке (x, y).  Вычисление проводится через двойной интеграл.
    """
    # Внутренний интеграл по x от -бесконечности до x
    def inner_integral(y_val):
        return quad(lambda x_val: bi_normal_pdf(x_val, y_val, m_x, m_y, sigma_x, sigma_y), -float('inf'), x)[0]
    # Внешний интеграл по y от -бесконечности до y
    return quad(inner_integral, -float('inf'), y)[0]

# Вычисление CDF для каждой точки сетки
cdf_values = []
for x_val in x_range:
    for y_val in y_range:
        cdf_values.append(bi_normal_cdf(x_val, y_val, m_x, m_y, sigma_x, sigma_y))

# Преобразование списка значений CDF в массив 2D
cdf_values = np.array(cdf_values).reshape(len(x_range), len(y_range))

# Построение 3D поверхности CDF с помощью Plotly
fig = go.Figure(data=[go.Surface(x=X, y=Y, z=cdf_values)])
fig.update_layout(title="Поверхность кумулятивной функции распределения (CDF)",
                  scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="CDF"),
                  width=800, height=600)
fig.show()
```

<img width="756" height="516" alt="image" src="https://github.com/user-attachments/assets/1d6dda36-2f72-400a-bdcb-d2b65cf72e1c" />
