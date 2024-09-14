import random as rnd

n = 0
m = 0
num = 100000
a = [0]

for i in range (num + 1):
    x = rnd.uniform(-1, 1)
    y = rnd.uniform(-1, 1)
    x = round(x, 4)
    y = round(y, 4)
    if (x ** 2 + y ** 2) <= 1:
        n += 1
    else:
        m += 1

print(n, m)   
pi = (4 * n) / (num + 1)
print(pi)