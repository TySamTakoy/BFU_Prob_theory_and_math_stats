# ЗАДАЧА №4

Найти предельные вероятности для систем S, граф которых изображен ниже

1.
<img width="256" height="59" alt="image" src="https://github.com/user-attachments/assets/194777c4-7794-479a-8072-60558cd1fce2" />

2.
<img width="275" height="151" alt="image" src="https://github.com/user-attachments/assets/20c2a15a-9bc7-4b6b-870b-1fbb7f046fce" />

# РЕШЕНИЕ

1. 
<img width="667" height="213" alt="image" src="https://github.com/user-attachments/assets/4b877e89-0d22-4d87-a170-afd294384806" />

$p_0=(1+\frac{2}{5}+\frac{3⋅2}{4⋅5})^{-1}≈0,588$
$p_1=\frac{2}{5}⋅0,588=0,235$
$p_2=\frac{3⋅2}{4⋅5}⋅0,588=0,177$

2. 
<img width="275" height="151" alt="image" src="https://github.com/user-attachments/assets/2c92c44e-eaab-42d7-80e2-0b889a60a7a5" />

<img width="243" height="137" alt="image" src="https://github.com/user-attachments/assets/4e4e21d3-b244-4428-9e14-a169df1940f7" />

Решение СЛАУ методом Гаусса.

Запишем систему в виде расширенной матрицы:

<img width="239" height="138" alt="image" src="https://github.com/user-attachments/assets/25c1d3f5-7c81-4f9d-ac0a-c94a2ee7ed70" />

После ряда преобразований в итоге получаем:
(2 строка - $p_3$;
3 строка - $p_2$;
4 строка - $p_1$;
5 строка - $p_0$)

<img width="220" height="142" alt="image" src="https://github.com/user-attachments/assets/0dbb32bd-41b1-467f-b2a3-d45d368aab31" />

Определим $p_0 ... p_4$:

<img width="229" height="143" alt="image" src="https://github.com/user-attachments/assets/08222523-9652-4bd6-a762-6634e09f2c78" />

Тогда
$p_3 = \frac{23}{87}$
$p_2 = \frac{2-(-2 ⋅ \frac{23}{87})}{22} = \frac{\frac{220}{87}}{22}=\frac{10}{87}$
$p_1 = \frac{0-(-23 ⋅ \frac{10}{87} + 4 ⋅ \frac{23}{87})}{3} = \frac{\frac{46}{29}}{5} = \frac{46}{87}$
$p_0 = \frac{0-( - 4 ⋅ \frac{10}{87})}{5} = \frac{\frac{40}{87}}{5} = \frac{8}{87}$

Итого, предельные вероятности равны:
$p_0 = \frac{8}{87}$
$p_1 = \frac{46}{87}$
$p_2 = \frac{10}{87}$
$p_3 = \frac{23}{87}$
