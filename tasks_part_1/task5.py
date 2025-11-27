import numpy as np
import plotly.graph_objects as go
import math

def bernoulli_probability(n, m, p):
  """
  Вычисляет вероятность m успехов в n независимых испытаниях Бернулли
  с вероятностью успеха p в каждом испытании.

  Args:
      n: Количество испытаний.
      m: Количество успехов.
      p: Вероятность успеха в одном испытании.

  Returns:
      Вероятность m успехов в n испытаниях.
  """
  if m > n:
    return 0
  return (math.factorial(n) / (math.factorial(m) * math.factorial(n - m))) * (p**m) * ((1 - p)**(n - m))

def poisson_probability(n, m, p):
  """
  Вычисляет вероятность m событий в интервале времени
  с интенсивностью n*p событий в этом интервале.

  Args:
      n: Количество испытаний.
      m: Количество событий.
      p: Вероятность успеха в одном испытании.

  Returns:
      Вероятность m событий.
  """
  return (np.exp(-n*p) * ((n*p)**m)) / math.factorial(m)

# Задаем диапазоны значений для n и m
n_range = np.arange(1, 20)
m_range = np.arange(0, 20)

# Задаем вероятность успеха
p = 0.5

# Вычисляем вероятности для каждого сочетания n и m
bernoulli_probs = np.array([[bernoulli_probability(n, m, p) for m in m_range] for n in n_range])
poisson_probs = np.array([[poisson_probability(n, m, p) for m in m_range] for n in n_range])

# Вычисляем разность между вероятностями
difference = bernoulli_probs - poisson_probs

# Создаем сетку для осей x и y
n_grid, m_grid = np.meshgrid(n_range, m_range)

# Создаем 3D-график с помощью Plotly
fig = go.Figure(data=[go.Surface(x=m_grid, y=n_grid, z=difference, colorscale='viridis')])

# Устанавливаем метки осей и заголовок
fig.update_layout(
    title="Разность между вероятностями Бернулли и Пуассона",
    scene=dict(
        xaxis_title="m",
        yaxis_title="n",
        zaxis_title="Разность вероятностей"
    ),
    width=800,  # Устанавливаем ширину графика
    height=600 # Устанавливаем высоту графика
)

fig.show()
