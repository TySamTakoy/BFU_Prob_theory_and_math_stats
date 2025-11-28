# ЗАДАНИЕ №2

Построить кривую соответствующую среднему арифметическому кривых испытания полимера нагрузка-деформация, полученных после $11$ измерений. Также на графике средней указать доверительные интервалы, соответствующие вероятности наблюдения кривой нагрузка-деформация $p=0,95$.
Данные измерений - https://cloud.mail.ru/public/BToL/T6YeXR6dG

<img width="325" height="258" alt="image" src="https://github.com/user-attachments/assets/75c1d768-035f-4229-874d-9785d1d26738" />

# РЕШЕНИЕ

```
from google.colab import drive
drive.mount('/content/drive')

import math
import statistics
import numpy as np
import scipy.stats as stats
import pandas as pd

stress_data = [
    pd.read_csv("/content/drive/My Drive/Colab Notebooks/stress-train/stress_1.csv", sep = ','),
    pd.read_csv("/content/drive/My Drive/Colab Notebooks/stress-train/stress_2.csv", sep = ','),
    pd.read_csv("/content/drive/My Drive/Colab Notebooks/stress-train/stress_3.csv", sep = ','),
    pd.read_csv("/content/drive/My Drive/Colab Notebooks/stress-train/stress_4.csv", sep = ','),
    pd.read_csv("/content/drive/My Drive/Colab Notebooks/stress-train/stress_5.csv", sep = ','),
    pd.read_csv("/content/drive/My Drive/Colab Notebooks/stress-train/stress_6.csv", sep = ','),
    pd.read_csv("/content/drive/My Drive/Colab Notebooks/stress-train/stress_7.csv", sep = ','),
    pd.read_csv("/content/drive/My Drive/Colab Notebooks/stress-train/stress_8.csv", sep = ','),
    pd.read_csv("/content/drive/My Drive/Colab Notebooks/stress-train/stress_9.csv", sep = ','),
    pd.read_csv("/content/drive/My Drive/Colab Notebooks/stress-train/stress_10.csv", sep = ','),
    pd.read_csv("/content/drive/My Drive/Colab Notebooks/stress-train/stress_11.csv", sep = ',')
]
```

```
stress_1.head(3)
```

<img width="120" height="114" alt="image" src="https://github.com/user-attachments/assets/fd505ee5-c2cb-4b3a-a241-f66456f34330" />

```
stress_2.head(3), stress_3.head(3), stress_4.head(3), stress_5.head(3), stress_6.head(3), stress_7.head(3), stress_8.head(3), stress_9.head(3), stress_10.head(3), stress_11.head(3)
```

<img width="127" height="284" alt="image" src="https://github.com/user-attachments/assets/6d233bc0-e067-4a5b-b3e4-b761cac0b2c8" /> <img width="128" height="420" alt="image" src="https://github.com/user-attachments/assets/4b022a45-340a-4658-8466-4507f0bf7580" />

```
import matplotlib.pyplot as plt

for i, df in enumerate(stress_data):
  plt.figure(figsize=(8, 6))
  plt.plot(df.iloc[:, 0], df.iloc[:, 1], linestyle='-')
  plt.xlabel("Нагрузка")
  plt.ylabel("деформация")
  plt.title(f"График Нагрузка-Деформация для stress_{i+1}.csv")
  plt.grid(True)
  plt.show()
```

<img width="686" height="547" alt="image" src="https://github.com/user-attachments/assets/7a87b695-1626-4466-ba10-be2b339d2981" />

<img width="686" height="547" alt="image" src="https://github.com/user-attachments/assets/3032c2cc-3117-4462-8073-f96302826de6" />

<img width="686" height="547" alt="image" src="https://github.com/user-attachments/assets/bb8335f1-f1a6-4eb2-9f10-5fd153ab12ba" />

<img width="686" height="547" alt="image" src="https://github.com/user-attachments/assets/12b724d6-3155-4ee3-9580-259f42e5b878" />

<img width="690" height="547" alt="image" src="https://github.com/user-attachments/assets/d79a40a4-b0d7-4b75-9009-cfe7fcee41f5" />

<img width="686" height="547" alt="image" src="https://github.com/user-attachments/assets/1ceb51b4-ad17-415f-934e-46ab5a57e6ce" />

<img width="686" height="547" alt="image" src="https://github.com/user-attachments/assets/ceec8abb-46e2-4841-89bf-ccd29269374f" />

<img width="686" height="547" alt="image" src="https://github.com/user-attachments/assets/bb2b329f-6412-4798-bd14-a6261c44a824" />

<img width="686" height="547" alt="image" src="https://github.com/user-attachments/assets/99833473-cd9c-4ef8-b4d4-ec5a6063df27" />

<img width="688" height="547" alt="image" src="https://github.com/user-attachments/assets/c9c11d3a-198a-4082-bdbd-207a91e3badd" />

<img width="686" height="547" alt="image" src="https://github.com/user-attachments/assets/0004ae5c-d923-4476-8d85-1cf54f784b6c" />

```
combined_data = pd.concat(stress_data)

# Группируем данные по x и усредняем y
average_data = combined_data.groupby(combined_data.columns[0])[combined_data.columns[1]].mean().reset_index()

# Строим график
plt.figure(figsize=(10, 6))  # Устанавливаем размер графика
plt.plot(average_data[combined_data.columns[0]], average_data[combined_data.columns[1]], linestyle='-')
plt.xlabel('Нагрузка')
plt.ylabel('Деформация')
plt.title('Средний график Нагрузка-Деформация для групп измерений')
plt.grid(True)
plt.show()
```

<img width="841" height="547" alt="image" src="https://github.com/user-attachments/assets/2e7dee34-8dee-40cf-8b9d-85b962c0cb45" />

```
combined_data = pd.concat(stress_data)

# Группируем данные по x и усредняем y
average_data = combined_data.groupby(combined_data.columns[0])[combined_data.columns[1]].mean().reset_index()

# Строим график с помощью plotly.graph_objects
fig = go.Figure()
fig.add_trace(go.Scatter(x=average_data[combined_data.columns[0]],
                         y=average_data[combined_data.columns[1]],
                         mode='lines'))
fig.update_layout(title='Средний график Нагрузка-Деформация для групп измерений',
                  xaxis_title='Нагрузка',
                  yaxis_title='Деформация',
                  xaxis_showgrid=True,
                  yaxis_showgrid=True,
                  width=800,
                  height=600)
fig.show()
```

<img width="721" height="539" alt="image" src="https://github.com/user-attachments/assets/a6b1dec9-cc91-4981-8e26-3394f287a06b" />

```
# Группируем данные по x и считаем среднее, стандартное отклонение и дисперсию y
grouped_data = combined_data.groupby(combined_data.columns[0])[combined_data.columns[1]].agg(['mean', 'std', 'var']).reset_index()

# Переименовываем столбцы для удобства
grouped_data.columns = ['Нагрузка', 'Средняя деформация', 'Стандартное отклонение', 'Дисперсия']

# Строим график среднего значения
plt.figure(figsize=(10, 6))
plt.plot(grouped_data['Нагрузка'], grouped_data['Средняя деформация'], linestyle='-')
plt.xlabel('Нагрузка')
plt.ylabel('Средняя деформация')
plt.title('Средний график Нагрузка-Деформация для групп измерений')
plt.grid(True)

# Добавим на график стандартное отклонение (в виде error bars)
plt.errorbar(grouped_data['Нагрузка'], grouped_data['Средняя деформация'], yerr=grouped_data['Стандартное отклонение'], fmt='o', capsize=5)

plt.show()
```

<img width="841" height="547" alt="image" src="https://github.com/user-attachments/assets/5b22c50d-036e-4f52-81bd-74ba6fde9e2e" />

```
fig = go.Figure()

# Добавляем линию среднего значения
fig.add_trace(go.Scatter(x=grouped_data['Нагрузка'],
                         y=grouped_data['Средняя деформация'],
                         mode='lines',
                         name='Среднее значение'))

# Добавляем error bars
fig.add_trace(go.Scatter(x=grouped_data['Нагрузка'],
                         y=grouped_data['Средняя деформация'],
                         error_y=dict(type='data', array=grouped_data['Стандартное отклонение']),
                         mode='markers',
                         marker=dict(size=8), # Размер маркеров
                         name='Стандартное отклонение'))


fig.update_layout(title='Средний график Нагрузка-Деформация для групп измерений',
                  xaxis_title='Нагрузка',
                  yaxis_title='Средняя деформация',
                  xaxis_showgrid=True,
                  yaxis_showgrid=True,
                  width=1000,
                  height=600,
                  legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)) # Легенда внизу

fig.show()
```

<img width="901" height="545" alt="image" src="https://github.com/user-attachments/assets/e164f783-0904-4fa4-9087-57ca25b7f21c" />
