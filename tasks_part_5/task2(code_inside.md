# ЗАДАЧА №2

Определить параметры PDF, которые наилучшим образом описывают наблюдаемую статистику какого-нибудь признака в датасете.

# РЕШЕНИЕ

```
plt.hist(CO2['CO2 Emissions(g/km)'], density=True)
plt.xlabel('Выбросы CO2 (г/км)')
plt.ylabel('Плотность')
plt.title('Гистограмма выбросов CO2')
plt.show()

mean = np.mean(CO2['CO2 Emissions(g/km)'])
std = np.std(CO2['CO2 Emissions(g/km)'])

print(f'Мат. ожидание: {mean:.4f}')
print(f'Стандартное отклонение: {std:.4f}')
```

<img width="584" height="455" alt="image" src="https://github.com/user-attachments/assets/316fab01-0ed8-4471-b5b7-9e54f157da48" />

`Мат. ожидание: 250.5847`
`Стандартное отклонение: 58.5087`

```
import scipy.stats as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(min(CO2['CO2 Emissions(g/km)']), max(CO2['CO2 Emissions(g/km)']), 100)
y = st.norm.pdf(x, np.mean(CO2['CO2 Emissions(g/km)']), np.std(CO2['CO2 Emissions(g/km)']))

result = st.norm.fit(CO2['CO2 Emissions(g/km)'])
mean_1 = result[0]
std_1 = result[1]

print(f'Мат. ожидание: {mean_1:.4f}')
print(f'\nСтандартное отклонение: {std_1:.4f}\n')

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, y, color='blue', label='Norm Fit')
ax.hist(CO2['CO2 Emissions(g/km)'], density=True, alpha=0.6, label='Гистограмма данных')
ax.fill_between(x, y, alpha=0.3, color='orange')

ax.set_xlabel('Выбросы CO2 (г/км)', fontsize=12)
ax.set_ylabel('Плотность', fontsize=12)
ax.set_title('CO2 hist & Norm Fit', fontsize=14)
ax.legend(fontsize=10)

plt.show()
```

`Мат. ожидание: 250.5847`
`Стандартное отклонение: 58.5087`

<img width="867" height="552" alt="image" src="https://github.com/user-attachments/assets/e970d35d-3ff1-4e94-9186-ff701a4d8c80" />

```
fited_data = st.beta.fit(CO2['CO2 Emissions(g/km)'])
print(fited_data)
```

`(17.710288505141385, 11620397.09463828, 4.978774516600691, 161144659.79916453)`

```
x = np.linspace(min(CO2['CO2 Emissions(g/km)']), max(CO2['CO2 Emissions(g/km)']), 100)

pdf_beta = st.beta.pdf(x,fited_data[0],fited_data[1],fited_data[2],fited_data[3])

predicted_values = st.beta.pdf(CO2['CO2 Emissions(g/km)'], fited_data[0], fited_data[1], fited_data[2], fited_data[3])

actual_values = CO2['CO2 Emissions(g/km)']
mse_beta = np.mean((actual_values - predicted_values) ** 2)

print(f"Среднеквадратичная ошибка (MSE_beta): {mse_beta:.4f}\n")

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, pdf_beta, color='red', label='Beta Fit')
ax.hist(CO2['CO2 Emissions(g/km)'], density=True, alpha=0.6, label='Гистограмма данных')
ax.fill_between(x, pdf_beta, alpha=0.3, color='orange')

ax.set_xlabel('Выбросы CO2 (г/км)', fontsize=12)
ax.set_ylabel('Плотность', fontsize=12)
ax.set_title('CO2 hist & Beta Fit', fontsize=14)
ax.legend(fontsize=10)

plt.show()
```

`Среднеквадратичная ошибка (MSE_beta): 66213.5553`

<img width="867" height="552" alt="image" src="https://github.com/user-attachments/assets/1bb5e17e-6def-4a22-a813-ce37e8db2377" />

```
print(st.gamma.fit(CO2['CO2 Emissions(g/km)']))
```

`(17.72388733350435, 4.88218959416638, 13.862788933978418)`

```
x = np.linspace(min(CO2['CO2 Emissions(g/km)']), max(CO2['CO2 Emissions(g/km)']), 100)

fited_data2 = st.gamma.fit(CO2['CO2 Emissions(g/km)'])

pdf_gamma = st.gamma.pdf(x, fited_data2[0], fited_data2[1], fited_data2[2])

predicted_values_gamma = st.gamma.pdf(CO2['CO2 Emissions(g/km)'], fited_data2[0], fited_data2[1], fited_data2[2])
actual_values = CO2['CO2 Emissions(g/km)']

mse_gamma = np.mean((actual_values - predicted_values_gamma) ** 2)

print(f"Среднеквадратичная ошибка (MSE_gamma): {mse_gamma:.4f}\n")

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, pdf_gamma, color='green', label='Gamma Fit')
ax.hist(CO2['CO2 Emissions(g/km)'], density=True, alpha=0.6, label='Гистограмма данных')
ax.fill_between(x, pdf_gamma, alpha=0.3, color='orange')

ax.set_xlabel('Выбросы CO2 (г/км)', fontsize=12)
ax.set_ylabel('Плотность', fontsize=12)
ax.set_title('CO2 hist & Gamma Fit', fontsize=14)
ax.legend(fontsize=10)

plt.show()
```

`Среднеквадратичная ошибка (MSE_gamma): 66213.5554`

<img width="867" height="552" alt="image" src="https://github.com/user-attachments/assets/091f56b7-30c6-4a73-9f3e-77c0781a0e46" />

```
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Histogram(x=CO2['CO2 Emissions(g/km)'], histnorm='probability density', opacity=0.6, name='Гистограмма данных'))

fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='blue'), name='Norm Fit', fill='tozeroy', fillcolor='rgba(135,206,250,0.4)'))
fig.add_trace(go.Scatter(x=x, y=pdf_beta, mode='lines', line=dict(color='red'), name='Beta Fit', fill='tozeroy', fillcolor='rgba(255,165,0,0.3)'))
fig.add_trace(go.Scatter(x=x, y=pdf_gamma, mode='lines', line=dict(color='green'), name='Gamma Fit', fill='tozeroy', fillcolor='rgba(255,165,0,0.3)'))


fig.update_layout(
    xaxis_title='Выбросы CO2 (г/км)',
    yaxis_title='Плотность',
    legend=dict(font=dict(size=10)),
    width=1000,
    height=600
)

fig.show()
```

<img width="981" height="477" alt="image" src="https://github.com/user-attachments/assets/4d84c4ec-7398-43c6-89db-d6e476d49f77" />

```
fited_data1 = st.norm.fit(CO2['CO2 Emissions(g/km)'])
mean = fited_data1[0]
std_dev = fited_data1[1]

actual_values = CO2['CO2 Emissions(g/km)']
predicted_values_norm = st.norm.pdf(CO2['CO2 Emissions(g/km)'], mean, std_dev)
mse_norm = np.mean((actual_values - predicted_values_norm) ** 2)

print(f"Среднеквадратичная ошибка (MSE_norm): {mse_norm:.4f}\n")
print(f"Среднеквадратичная ошибка (MSE_beta): {mse_beta:.4f}\n")
print(f"Среднеквадратичная ошибка (MSE_gamma): {mse_gamma:.4f}\n")
```

`Среднеквадратичная ошибка (MSE_norm): 66213.5698`

`Среднеквадратичная ошибка (MSE_beta): 66213.5553`

`Среднеквадратичная ошибка (MSE_gamma): 66213.5554`
