# ЗАДАЧА №1

1.   Построить:

*   вариационный ряд;
*   гистограмму;
*   кумуляту  для любого признака вашего dataset.

2.   Определить:
*   является ли распределение признака скошенным либо уширенными относительно нормального;
*   для своего dataset коррелирующие параметры - построение матрицы корреляции (уровень корреляции более $+-0.5$);
*   для своего dataset не линейно коррелирующие параметры;
*   Для одного из признаков dataset среднее значение, стандартное отклонение.

# РЕШЕНИЕ

```
from google.colab import drive
drive.mount('/content/drive')

import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd

CO2 = pd.read_csv("/content/drive/My Drive/Colab Notebooks/CO2 Emissions.csv", sep = ',')

CO2.head(5)
```

<img width="1394" height="259" alt="image" src="https://github.com/user-attachments/assets/53462371-3c14-47e5-8b2d-b7b67d66916e" />

```
import matplotlib.pyplot as plt

# Получение столбца с выбросами CO2
co2_emissions = CO2['CO2 Emissions(g/km)']

aa = plt.hist(co2_emissions, bins='sturges')
plt.xlabel('CO2 Emissions (g/km)')
plt.ylabel('Frequency')
plt.title('Гистограмма выбросов CO2')
plt.show()
```

<img width="580" height="455" alt="image" src="https://github.com/user-attachments/assets/80a28cce-0ce8-40b1-b95f-4c66bc5a9ea5" />

```
tablus = pd.DataFrame({'Интервалы':aa[1][:-1], 'Частота':aa[0]})
print(tablus)
```

<img width="651" height="458" alt="image" src="https://github.com/user-attachments/assets/5e397cfd-6232-4b81-b0f8-b2c383117e2d" />

```
plt.bar(tablus['Интервалы'],tablus['Частота'], color='red')
aa = plt.hist(CO2['CO2 Emissions(g/km)'], bins='sturges', alpha=.4)
```

<img width="560" height="416" alt="image" src="https://github.com/user-attachments/assets/5c639336-cf19-45e3-be19-29f1689735a0" />

```
bb = []
for i in range(len(aa[1])-1):
    bb.append(f'{aa[1][i]:.1f} - {aa[1][i+1]:.1f}')

print(bb)
```

`['96.0 - 126.4', '126.4 - 156.9', '156.9 - 187.3', '187.3 - 217.7', '217.7 - 248.1', '248.1 - 278.6', '278.6 - 309.0', '309.0 - 339.4', '339.4 - 369.9', '369.9 - 400.3', '400.3 - 430.7', '430.7 - 461.1', '461.1 - 491.6', '491.6 - 522.0']`

```
tablus1 = pd.DataFrame({"Интервал":bb, "Частота":aa[0]})
tablus1['Частотность'] = tablus1["Частота"]/len(tablus1["Частота"])
tablus1['Накопленная частота'] = tablus1['Частота'].cumsum()
tablus1['Накопленная частотность'] = tablus1['Частотность'].cumsum()
tablus1
```

<img width="650" height="463" alt="image" src="https://github.com/user-attachments/assets/de45e112-b189-465c-b8cf-fc26a5f16967" />

```
# Сортировка значений CO2 Emissions
sorted_emissions = np.sort(co2_emissions)

# Создание кумулятивной функции распределения
cumulative_probabilities = np.arange(len(sorted_emissions)) / len(sorted_emissions)

# Построение графика кумулятивной функции распределения
plt.plot(sorted_emissions, cumulative_probabilities)
plt.xlabel('CO2 Emissions (g/km)')
plt.ylabel('Cumulative Probability')
plt.title('CDF of CO2 emissions')
plt.show()
```

<img width="567" height="455" alt="image" src="https://github.com/user-attachments/assets/980b3854-8a0c-452d-8f50-770696798ff6" />

```
import scipy.stats as stats

skewness = stats.skew(CO2['CO2 Emissions(g/km)'])

# Вычисление эксцесса (kurtosis)
kurtosis = stats.kurtosis(CO2['CO2 Emissions(g/km)'])

print(f"Коэффициент асимметрии: {skewness:.4f}")
print(f"Эксцесс: {kurtosis:.4f}")
```

`Коэффициент асимметрии: 0.5260`
`Эксцесс: 0.4777`



---


    skew(a, axis=0, bias=True, nan_policy='propagate', *, keepdims=False)[source]
> Для данных, распределенных нормально, асимметрия должна быть приблизительно равна нулю. Для унимодальных непрерывных распределений значение асимметрии больше нуля означает, что в правом хвосте распределения сосредоточена большая часть значений. Функция `skewtest` может использоваться для определения того, достаточно ли близко значение асимметрии к нулю в статистическом смысле.

    kurtosis(a, axis=0, fisher=True, bias=True, nan_policy='propagate', *, keepdims=False)[source]
> Эксцесс — это четвёртый центральный момент, делённый на квадрат дисперсии. Если используется определение Фишера, то из результата вычитается 3,0, чтобы получить 0,0 для нормального распределения.

> Если `bias` (смещение) равно `False`, то эксцесс вычисляется с использованием k-статистик для устранения смещения, возникающего из-за смещённых оценок моментов.


---

Положительное значение ***коэффициента асимметрии: 0.5260*** говорит о том, что распределение выбросов CO2 скошено вправо. Это означает, что в данных больше наблюдений с более низкими значениями выбросов, а длинный “хвост” распределения находится справа, с небольшим количеством наблюдений с очень высокими значениями выбросов.

Значение ***эксцесса: 0.4777***  немного больше 0, что указывает на то, что распределение выбросов CO2 немного более узкое и имеет более толстые хвосты, чем нормальное распределение. Это означает, что есть больше данных, расположенных ближе к пику распределения, и меньше данных в хвостах, по сравнению с нормальным распределением.

```
# Вычисление среднего значения
mean_co2 = CO2['CO2 Emissions(g/km)'].mean()

# Вычисление стандартного отклонения
std_co2 = CO2['CO2 Emissions(g/km)'].std()

print("Mean value CO2:", mean_co2)
print("Standard deviation CO2:", std_co2)
```

`Mean value CO2: 250.58469871360867`
`Standard deviation CO2: 58.512679394406476`

```
import seaborn as sns

# Выбор интересующих параметров
selected_parameters = ['Engine Size(L)', 'Cylinders', 'Fuel Consumption City (L/100 km)',
                      'Fuel Consumption Hwy (L/100 km)', 'Fuel Consumption Comb (L/100 km)',
                      'Fuel Consumption Comb (mpg)', 'CO2 Emissions(g/km)']

# Создание матрицы корреляции
correlation_matrix = CO2[selected_parameters].corr()

# Визуализация матрицы корреляции с помощью heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
# annot=True делает карту более читаемой, позволяя сразу видеть величину корреляции между переменными.
plt.title('Correlation matrix')
plt.show()
```

<img width="771" height="671" alt="image" src="https://github.com/user-attachments/assets/4bcdfae7-4498-4b39-87ef-d4df25529dfa" />

```
# Подсчет количества уникальных моделей
model_counts = CO2['Model'].value_counts()
print("Unique models:")
print(model_counts)

# Подсчет количества уникальных классов автомобилей
vehicle_class_counts = CO2['Vehicle Class'].value_counts()
print("\nUnigue vehicle classes:")
print(vehicle_class_counts)
```

<img width="311" height="592" alt="image" src="https://github.com/user-attachments/assets/7a35d073-c51f-4aa4-b850-c22495a687c9" />

```
import seaborn as sns
sns.pairplot(CO2)
```

<img width="1721" height="1721" alt="image" src="https://github.com/user-attachments/assets/13e79997-0cd2-449b-84c3-b58d2d420b41" />

```
import seaborn as sns
sns.pairplot(CO2, hue = 'Cylinders')
```

<img width="1570" height="1476" alt="image" src="https://github.com/user-attachments/assets/c29ec35c-95e7-40c0-81bb-0ed16e27e75f" />
