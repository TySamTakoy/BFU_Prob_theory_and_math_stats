# ЗАДАЧА №1

Нормальный закон распределения СВ (нормированная функия Гаусса):

$p(x)=\frac{1}{\sigma \sqrt{2π}} \exp{(-\frac{(x-X)^2}{2\sigma^2})}$

# РЕШЕНИЕ

```
  quad() вычисляет определённый интеграл численно.
  gaussian - функция, которую интегрируем.
  -np.inf, x[i] - пределы интегрирования (от минус бесконечности до x[i]).
  args=(mu, sigma) - передача дополнительных аргументов функции gaussian (mu и sigma).
```

<img width="567" height="455" alt="image" src="https://github.com/user-attachments/assets/00abd66b-22dc-4f9d-9cd7-6c2d95b599fa" />
