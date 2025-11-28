# ЗАДАНИЕ №5

На основе датасета цветов Ириса определить ошибки первого и второго рода для гипотезы определения вида Setosa по средней и доверительному интервалу с уровнем $p=0,7$ распределения Sepal Length.
Датасет по ссылке - https://cloud.mail.ru/public/yBJm/4zz7PDnJn

# РЕШЕНИЕ

```
iris = pd.read_csv("/content/drive/My Drive/Colab Notebooks/Iris.csv", sep = ',')

iris.head(5)
```

<img width="579" height="185" alt="image" src="https://github.com/user-attachments/assets/b94fffee-10e2-4420-8da5-78fd7c8fe2c0" />

```
# Фильтрация данных для вида Iris-setosa
setosa = iris[iris['Species'] == 'Iris-setosa']
# Извлечение значений длины чашелистника для Setosa
sepal_length_setosa = setosa['SepalLengthCm']

# Вычисление среднего значения длины чашелистика для Setosa
mean_setosa = np.mean(sepal_length_setosa)
# Вычисление стандартного отклонения (с поправкой Бесселя, ddof=1 для выборочной дисперсии)
std_setosa = np.std(sepal_length_setosa, ddof=1)

# Вычисление 70% доверительного интервала
confidence_level = 0.7  # Уровень доверия (p)
alpha = 1 - confidence_level # Уровень значимости
z_score = stats.norm.ppf(1 - alpha / 2) # Квантиль нормального распределения
margin_of_error = z_score * (std_setosa / np.sqrt(len(setosa))) # Погрешность
confidence_interval = (mean_setosa - margin_of_error, mean_setosa + margin_of_error) # Доверительный интервал

# Вывод результатов
print(f"Среднее значение SepalLengthCm для Setosa: {mean_setosa:.2f}")
print(f"Стандартное отклонение: {std_setosa:.2f}")
print(f"Доверительный интервал (p=0.7): {confidence_interval}")

# Классификация и подсчет ошибок I и II рода.
# Используем доверительный интервал для классификации:
# если значение SepalLengthCm попадает в интервал - считаем Iris-setosa, иначе - нет.

errors_type1 = 0 # Счетчик ошибок первого рода (ложноотрицательные)
errors_type2 = 0 # Счетчик ошибок второго рода (ложноположительные)

for index, row in iris.iterrows():
    # Проверка на принадлежность к виду Iris-setosa
    if row['Species'] == 'Iris-setosa':
        # Проверка на попадание в доверительный интервал. Если значение вне интервала - ошибка первого рода.
        if row['SepalLengthCm'] < confidence_interval[0] or row['SepalLengthCm'] > confidence_interval[1]:
            errors_type1 += 1
    else:
        # Проверка на попадание в доверительный интервал.  Если значение внутри интервала - ошибка второго рода.
        if row['SepalLengthCm'] >= confidence_interval[0] and row['SepalLengthCm'] <= confidence_interval[1]:
            errors_type2 += 1

# Вывод количества ошибок
print(f"Ошибки первого рода (процент от общего числа Setosa): {(errors_type1 / len(setosa) * 100):.0f}%")
print(f"Ошибки второго рода (общее число): {errors_type2}")
```

`Среднее значение SepalLengthCm для Setosa: 5.01`

`Стандартное отклонение: 0.35`

`Доверительный интервал (p=0.7): (4.95433424158835, 5.057665758411651)`

`Ошибки первого рода (процент от общего числа Setosa): 84%`

`Ошибки второго рода (общее число): 2`
