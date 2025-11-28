# ЗАДАНИЕ №1

Для любого признака из своего датасета определить среднюю величину и доверительный интервал, соответствующие вероятности наблюдения величины выбранного признака с $p=0,933$ и $p=0,743$.

# РЕШЕНИЕ

  ## Bootstrap method

---
> Бутстрэп (англ. bootstrap) — метод определения доверительных интервалов статистических оценок по выборке. Основан на многократной генерации выборок методом Монте-Карло на базе имеющейся выборки.

> Суть метода состоит в том, чтобы по имеющейся выборке построить эмпирическое распределение. Используя это распределение как теоретическое распределение вероятностей, можно с помощью датчика псевдослучайных чисел сгенерировать практически неограниченное количество псевдовыборок произвольного размера, например, того же, как у исходной. На множестве псевдовыборок можно оценить не только анализируемые статистические характеристики, но и изучить их вероятностные распределения.
---

```
import pandas as pd
import numpy as np
from scipy import stats

co2_emissions = CO2['CO2 Emissions(g/km)']

# Бутстреп
n_bootstrap_samples = 10000 # устанавливается количество бутстреп-выборок — 10000.
                            # Бутстреп — это метод статистического вывода,
                            # который использует повторную выборку с возвращением
                            # из исходного набора данных для оценки распределения
                            # статистики (в данном случае — среднего значения).
bootstrap_means = []
for i in range(n_bootstrap_samples):
    bootstrap_sample = np.random.choice(co2_emissions, size=len(co2_emissions), replace=True)
    bootstrap_means.append(np.mean(bootstrap_sample))

# Доверительный интервал
confidence_level = 0.933
lower_bound = np.percentile(bootstrap_means, (1 - confidence_level) / 2 * 100)
upper_bound = np.percentile(bootstrap_means, (1 + confidence_level) / 2 * 100)

print(f"Среднее значение выбросов CO2: {np.mean(co2_emissions):.2f} г/км")
print(f"Доверительный интервал ({confidence_level:.3f}) (бутстреп): ({lower_bound:.2f}, {upper_bound:.2f})")
```

`Среднее значение выбросов CO2: 250.58 г/км`

`Доверительный интервал (0.933) (бутстреп): (249.36, 251.80)`

```
import pandas as pd
import numpy as np
from scipy import stats

co2_emissions = CO2['CO2 Emissions(g/km)']

# Бутстреп
n_bootstrap_samples = 10000 # количество бутстреп выборок
bootstrap_means = []
for i in range(n_bootstrap_samples):
    bootstrap_sample = np.random.choice(co2_emissions, size=len(co2_emissions), replace=True)
    bootstrap_means.append(np.mean(bootstrap_sample))

# Доверительный интервал
confidence_level = 0.743
lower_bound = np.percentile(bootstrap_means, (1 - confidence_level) / 2 * 100)
upper_bound = np.percentile(bootstrap_means, (1 + confidence_level) / 2 * 100)

print(f"Среднее значение выбросов CO2: {np.mean(co2_emissions):.2f} г/км")
print(f"Доверительный интервал ({confidence_level:.3f}) (бутстреп): ({lower_bound:.2f}, {upper_bound:.2f})")
```

`Среднее значение выбросов CO2: 250.58 г/км`

`Доверительный интервал (0.743) (бутстреп): (249.80, 251.34)`

  ## Через $N$($M$; $σ$)

```
import numpy as np
import pandas as pd
from scipy.stats import norm

# Среднее значение
mean = np.mean(co2_emissions)

# Стандартное отклонение
std_dev = np.std(co2_emissions, ddof=1)  # ddof=1 для выборочного отклонения

# Размер выборки
n = len(co2_emissions)

# Стандартная ошибка
sem = std_dev / np.sqrt(n)

# Значения z для указанных уровней доверия
p_values = [0.933, 0.743]
z_scores = [norm.ppf((1 + p) / 2) for p in p_values]

# Расчет доверительных интервалов
confidence_intervals = [(mean - z * sem, mean + z * sem) for z in z_scores]

# Результаты
print(f"Среднее значение: {mean:.2f}")
for p, ci in zip(p_values, confidence_intervals):
    print(f"Доверительный интервал для p={p}: {ci[0]:.2f} до {ci[1]:.2f}")
```

`Среднее значение: 250.58`

`Доверительный интервал для p=0.933: 249.34 до 251.83`

`Доверительный интервал для p=0.743: 249.81 до 251.36`
