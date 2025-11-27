import plotly.graph_objects as go
import numpy as np
import scipy.stats as sc

# Задаем вероятность успеха в одном испытании
p = 0.5
# Создаем список значений n (число испытаний) от 1 до 100
n_values = list(range(1, 101))

def binomial_distribution(n, p):
    """
    Вычисляет значения функции вероятности массы биномиального распределения.

    Args:
        n: Число испытаний.
        p: Вероятность успеха в одном испытании.

    Returns:
        Кортеж (x, y), где:
            x: Массив возможных значений числа успехов (от 0 до n).
            y: Массив соответствующих вероятностей.
    """
    x = np.arange(n + 1) # Создаем массив возможных значений числа успехов от 0 до n
    y = sc.binom(n, p).pmf(x) # Используем функцию pmf (probability mass function) из scipy.stats для вычисления вероятностей
    return x, y

# Создаем начальный график для n = 1
x, y = binomial_distribution(n_values[0], p)
fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines+markers', name=f'n = {n_values[0]}')]) # Создаем объект графика с линией и маркерами

# Создаем шаги для слайдера
steps = []
for i, n in enumerate(n_values):
    x, y = binomial_distribution(n, p) # Вычисляем вероятности для текущего значения n
    step = dict(
        method="update", # Метод обновления графика
        args=[{"x": [x], "y": [y]}, {"title": f"Биномиальное распределение, n = {n}"}], # Аргументы обновления: новые данные x, y и заголовок
        label=str(n) # Метка шага слайдера
    )
    steps.append(step)

# Создаем слайдер
sliders = [dict(
    active=0, # Активный шаг (начальный)
    currentvalue={"prefix": "n: "}, # Префикс текущего значения n на слайдере
    pad={"t": 50}, # Отступ сверху
    steps=steps # Список шагов
)]

# Настраиваем макет графика
fig.update_layout(
    title=f'Биномиальное распределение при p = {p}', # Заголовок графика
    xaxis_title='Количество успехов', # Подпись оси x
    yaxis_title='Вероятность', # Подпись оси y
    sliders=sliders, # Добавляем слайдер
    xaxis_range=[0, max(n_values) + 1], # Диапазон оси x
    yaxis_range=[0, p ], # Диапазон оси y
    width=800,  # Устанавливаем ширину графика
    height=600 # Устанавливаем высоту графика
)

fig.show() # Отображаем график
