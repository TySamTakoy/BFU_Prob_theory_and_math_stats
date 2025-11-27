# ЗАДАЧА №1 СО ЗВЕЗДОЧКОЙ

Двумерная случайная величина распределена равномерно в круге радиуса $R=1$. Определить:
1.   выражение совместной плотности и функции распределения случайной величины $(X, Y)$;
2.   плотности вероятности и функции распределения одномерных составляющих $X$ и $Y$;
3.   вероятность того, что расстояние от точки $(X, Y)$ до начала координата будет меньше $1/3$

<img width="863" height="251" alt="image" src="https://github.com/user-attachments/assets/9b38b0ad-a641-444f-96a4-7956ef75d3c6" />

# РЕШЕНИЕ

1.   выражение совместной плотности и функции распределения случайной величины $(X, Y)$

```
import numpy as np
import plotly.graph_objects as go

def joint_pdf(x, y, R=1):
  """
  Вычисляет значение совместной плотности вероятности для заданных координат x и y.

  Функция моделирует равномерное распределение вероятности внутри круга радиуса R.

  Args:
    x: Массив значений координаты x.
    y: Массив значений координаты y.
    R: Радиус круга (по умолчанию 1).

  Returns:
    Массив значений совместной плотности вероятности. Возвращает 0, если точка (x, y) находится вне круга.
    Если x или y не массивы, вернет float.
  """
  r = np.sqrt(x**2 + y**2)
  # Используем np.where для эффективного вычисления:
  # возвращает 1 / (pi * R^2) если r <= R, иначе 0.  Работает и для массивов, и для одиночных значений
  return np.where(r <= R, 1 / (np.pi * R**2), 0)

def joint_cdf(x, y, R=1):
  """
  Вычисляет значение совместной функции распределения для заданных координат x и y.

  Функция моделирует равномерное распределение вероятности внутри круга радиуса R.

  Args:
    x: Значение координаты x.
    y: Значение координаты y.
    R: Радиус круга (по умолчанию 1).

  Returns:
    Значение совместной функции распределения. Возвращает 1, если точка (x, y) находится вне круга.
  """
  r = np.sqrt(x**2 + y**2)

  # Проверка на то, что все значения в массиве r меньше или равны R.
  # Если x, y - скаляры, то (r <= R) - тоже скаляр, и .all() не работает.
  if isinstance(x, (int, float)) and isinstance(y, (int, float)):
    if r <= R:
      return (1 / (np.pi * R**2)) * np.pi * r**2
    else:
      return 1
  elif (r <= R).all():  # Если r - массив, используем .all() для проверки.
                        # проверяет, находятся ли все точки из
                        # массива r (координаты точек) внутри круга заданного
                        # радиусом R. Если хотя бы одна точка за пределами
                        # круга, результат будет False
      return (1 / (np.pi * R**2)) * np.pi * r**2
  else:
      return 1

# Параметры для сетки
R = 1
x_grid = np.linspace(-1.2, 1.2, 100)
y_grid = np.linspace(-1.2, 1.2, 100)
X, Y = np.meshgrid(x_grid, y_grid)

# Вычисление значений плотности вероятности и функции распределения
Z_pdf = joint_pdf(X, Y, R)
Z_cdf = np.zeros_like(X)  # Инициализация Z_cdf нулями с размерами X

for i in range(X.shape[0]):
  for j in range(X.shape[1]):
    Z_cdf[i, j] = joint_cdf(X[i, j], Y[i, j], R)

# Создание двух 3D графиков с помощью plotly
fig_pdf = go.Figure()
fig_cdf = go.Figure()

fig_pdf.add_surface(x=X, y=Y, z=Z_pdf, name="Совместная плотность вероятности", colorscale='viridis')
fig_cdf.add_surface(x=X, y=Y, z=Z_cdf, name="Совместная функция распределения", colorscale='viridis')

fig_pdf.update_layout(title="Совместная плотность вероятности",
    scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"), width=800, height=600)

fig_cdf.update_layout(title="Совместная функция распределения",
    scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"), width=800, height=600)

fig_pdf.show()
fig_cdf.show()
```

<img width="783" height="537" alt="image" src="https://github.com/user-attachments/assets/ea0b5d75-fe37-4338-a8bd-d2e4efa9f43e" />

<img width="756" height="496" alt="image" src="https://github.com/user-attachments/assets/727d7668-8ca1-49c0-b230-c21c9c2e699b" />

2.   плотности вероятности и функции распределения одномерных составляющих $X$ и $Y$

Маргинальное распределение — это вероятностное распределение вероятностей одной или множества случайных величин, рассматриваемых в качестве компоненты или множества компонент некоторого известного многомерного распределения

```
import numpy as np
import plotly.graph_objects as go

def joint_pdf(x, y, R=1):
  """
  Вычисляет значение совместной плотности вероятности для заданных x и y.

  Предполагается, что (x, y) находятся внутри круга радиуса R с центром в (0, 0).
  Функция возвращает 1/(pi*R^2) внутри круга и 0 вне его.

  Args:
    x: Значение x.
    y: Значение y.
    R: Радиус круга (по умолчанию 1).

  Returns:
    Значение совместной плотности вероятности.
  """
  r = np.sqrt(x**2 + y**2)
  return np.where(r <= R, 1 / (np.pi * R**2), 0)


def marginal_pdf_x(x, R=1):
  """
  Вычисляет значение маргинальной плотности вероятности для x.

  Предполагается, что распределение - это круг радиуса R с центром в (0,0).
  Возвращает 0, если x вне круга, иначе рассчитывает значение плотности.

  Args:
    x: Значение x.
    R: Радиус круга (по умолчанию 1).

  Returns:
    Значение маргинальной плотности вероятности.
  """
  return np.where(np.abs(x) <= R, 2 * np.sqrt(1 - x**2) / (np.pi * R**2), 0)


def marginal_pdf_y(y, R=1):
  """
  Аналогично marginal_pdf_x, но для y.
  """
  return np.where(np.abs(y) <= R, 2 * np.sqrt(1 - y**2) / (np.pi * R**2), 0)


def marginal_cdf_x(x, R=1):
  """
  Вычисляет значение маргинальной функции распределения для x.

  Предполагается, что распределение - это круг радиуса R с центром в (0,0).
  Возвращает 0 если x < -R, 1 если x > R, и рассчитывает интеграл в другом случае.

  Args:
    x: Значение x.
    R: Радиус круга (по умолчанию 1).

  Returns:
    Значение маргинальной функции распределения.
  """
  return np.where(np.abs(x) <= R, (1 / (np.pi * R**2)) * (np.pi * x**2 / 2 + np.arcsin(x)),
                  np.where(x > R, 1, 0))

def marginal_cdf_y(y, R=1):
  """
  Аналогично marginal_cdf_x, но для y.
  """
  return np.where(np.abs(y) <= R, (1 / (np.pi * R**2)) * (np.pi * y**2 / 2 + np.arcsin(y)),
                  np.where(y > R, 1, 0))

# Параметры для сетки точек
R = 1
x_grid = np.linspace(-1, 1, 100)
y_grid = np.linspace(-1, 1, 100)

# Вычисление значений плотности вероятности и функции распределения
pdf_x = marginal_pdf_x(x_grid, R)
pdf_y = marginal_pdf_y(y_grid, R)
cdf_x = marginal_cdf_x(x_grid, R)
cdf_y = marginal_cdf_y(y_grid, R)

# Создание 2D графиков с помощью plotly
fig_pdf_x = go.Figure()
fig_pdf_y = go.Figure()
fig_cdf_x = go.Figure()
fig_cdf_y = go.Figure()

fig_pdf_x.add_trace(go.Scatter(x=x_grid, y=pdf_x, name="Плотность вероятности X"))
fig_pdf_y.add_trace(go.Scatter(x=y_grid, y=pdf_y, name="Плотность вероятности Y"))

fig_cdf_x.add_trace(go.Scatter(x=x_grid, y=cdf_x, name="Функция распределения X"))
fig_cdf_y.add_trace(go.Scatter(x=y_grid, y=cdf_y, name="Функция распределения Y"))

# Настройка осей и заголовка для каждого графика
fig_pdf_x.update_layout(title="Плотность вероятности X", xaxis_title="X", yaxis_title="f(X)",width=400, height=300)

fig_pdf_y.update_layout(title="Плотность вероятности Y", xaxis_title="Y", yaxis_title="f(Y)",width=400, height=300)

fig_cdf_x.update_layout(title="Функция распределения X", xaxis_title="X", yaxis_title="F(X)",width=400, height=300)

fig_cdf_y.update_layout(title="Функция распределения Y", xaxis_title="Y", yaxis_title="F(Y)",width=400, height=300)

fig_pdf_x.show()
fig_pdf_y.show()
fig_cdf_x.show()
fig_cdf_y.show()
```

<img width="321" height="240" alt="image" src="https://github.com/user-attachments/assets/20d34ccd-49a6-4e24-8248-4233c998b821" />

<img width="319" height="237" alt="image" src="https://github.com/user-attachments/assets/3d7a48e0-a521-41a2-9e61-351fe5c4589f" />

<img width="318" height="232" alt="image" src="https://github.com/user-attachments/assets/746b3e48-42ba-4b48-bcbd-52152165d292" />

<img width="314" height="237" alt="image" src="https://github.com/user-attachments/assets/b298cdb6-2840-47d2-9ebd-222fa711acbf" />

```
import numpy as np
import plotly.graph_objects as go

def joint_pdf(x, y, R=1):
  r = np.sqrt(x**2 + y**2)
  return np.where(r <= R, 1 / (np.pi * R**2), 0)

# Параметры для сетки точек
R = 1
x_grid = np.linspace(-1, 1, 100)
y_grid = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x_grid, y_grid)

# Вычисление значений плотности вероятности
Z = joint_pdf(X, Y, R)

# Вычисление расстояния от каждой точки до начала координат
r = np.sqrt(X**2 + Y**2)

# Вычисление вероятности
probability = np.sum(np.where(r < 1/3, Z, 0)) * ((x_grid[1] - x_grid[0]) * (y_grid[1] - y_grid[0]))  # Интегрирование по области

# Создание 3D графика с помощью plotly
fig = go.Figure()

fig.add_surface(x=X, y=Y, z=Z, name="Совместная плотность вероятности", colorscale='viridis')

# Добавление круга радиуса 1/3
fig.add_trace(go.Surface(x=np.linspace(-1/3, 1/3, 50), y=np.linspace(-1/3, 1/3, 50), z=np.zeros((50, 50)),
    showscale=False, opacity=0.5, colorscale='hot'))

# Настройка осей и заголовка
fig.update_layout(title=f"Вероятность того, что расстояние < 1/3: {probability:.4f}",
    scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"),width=800, height=600)

fig.show()
```

<img width="755" height="499" alt="image" src="https://github.com/user-attachments/assets/97babd0f-dad5-48ea-a661-fe60bce23613" />
