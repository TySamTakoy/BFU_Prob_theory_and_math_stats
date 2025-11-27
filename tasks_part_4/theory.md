Закон больших чисел на примере увеличения кол-ва случайных величин

<img width="276" height="118" alt="image" src="https://github.com/user-attachments/assets/a2f4c1a5-cbe5-4b8d-b583-dc5277ea6572" />


$ϕ(x_1)+ϕ(x_2)$

<img width="261" height="117" alt="image" src="https://github.com/user-attachments/assets/5e5bc4f6-763b-46fc-804f-56cf9649224d" />


$ϕ(x_1)+ϕ(x_2)+ϕ(x_3)$

<img width="298" height="125" alt="image" src="https://github.com/user-attachments/assets/10130239-738c-42dd-abb6-32cbecc4d743" />


$M(X)=\frac{a+b}{2}$
$D(X)=\frac{(b-a)^2}{12}$

```
import random as rnd
import matplotlib.pyplot as plt

spisok = []
for i in range(100):
  spisok.append(rnd.random())

plt.hist(spisok)
plt.xlabel("Значения")
plt.ylabel("Частота")
plt.title("Гистограмма случайных чисел")
plt.show()
```

<img width="562" height="455" alt="image" src="https://github.com/user-attachments/assets/d23c2195-04bb-46d9-b4c8-cae3fa204bf8" />

```
import random as rnd
import matplotlib.pyplot as plt

spisok = []
for i in range(100):
  spisok.append(rnd.random()+rnd.random())

plt.hist(spisok)
plt.xlabel("Значения")
plt.ylabel("Частота")
plt.title("Гистограмма случайных чисел")
plt.show()
```

<img width="576" height="455" alt="image" src="https://github.com/user-attachments/assets/e04e0e70-7778-495b-bd72-bd8595e7d6c5" />

```
import random as rnd
import matplotlib.pyplot as plt

spisok = []
for i in range(100):
  spisok.append(rnd.random()+rnd.random()+rnd.random())

plt.hist(spisok)
plt.xlabel("Значения")
plt.ylabel("Частота")
plt.title("Гистограмма случайных чисел")
plt.show()
```

<img width="562" height="455" alt="image" src="https://github.com/user-attachments/assets/a6b23f98-e85f-4e33-95e5-ccb56a169696" />
