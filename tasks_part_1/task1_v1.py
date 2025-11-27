def probability_of_passing(n):
    return (1 - (1 - 0.95 / n) ** 10) * (1 - 0.33 / n)

n = 0
max_probability = 0

for i in range(1, 11):
    p = probability_of_passing(i)
    if p > max_probability:
        max_probability = p
        n = i
    p = round(p, 2)
    print(i, p)

print("Оптимальное количество билетов:", n)
