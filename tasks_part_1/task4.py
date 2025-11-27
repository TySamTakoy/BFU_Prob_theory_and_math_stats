import random
import matplotlib.pyplot as plt

# Функция моделирования игры в орлянку с экспоненциально растущей ставкой
def coin_flip_game(N, p, lambda_):
    """
    Моделирует игру в орлянку с экспоненциально растущей ставкой.

    Args:
        N: Начальный размер банка.
        p: Доля начальной ставки.
        lambda_: Фактор увеличения ставки.

    Returns:
        Количество раундов до проигрыша, или None, если проигрыша не было за 100000 раундов.
    """
    rounds = 0  # Счетчик раундов
    bank = N  # Текущий размер банка
    while rounds < 100000:  # Ограничение по количеству раундов
        rounds += 1
        # Ставка экспоненциально растет, но не превышает размер банка
        bet = min(p * lambda_**(rounds - 1) * N, bank)
        outcome = random.choice([True, False])  # True - выигрыш, False - проигрыш
        if outcome:
            bank += bet  # При выигрыше ставка добавляется к банку
        else:
            bank -= bet  # При проигрыше ставка вычитается из банка
        if bank == 0:  # Проверка на проигрыш
            return rounds
    return None  # Игра не закончилась проигрышем за 100000 раундов

# Параметры игры
N = 100  # Начальный банк
p = 0.1  # Доля начальной ставки (10%)
lambda_ = 2  # Фактор увеличения ставки (ставка удваивается в каждом раунде)

# Проведение симуляции
num_simulations = 1000  # Количество симуляций игры
results = []  # Список для хранения результатов симуляций

for _ in range(num_simulations):
    result = coin_flip_game(N, p, lambda_)
    results.append(result)

# Анализ результатов
num_losses = len([r for r in results if r is not None])  # Количество симуляций, закончившихся проигрышем
probability_of_loss = num_losses / num_simulations  # Вероятность проигрыша

print(f"Количество симуляций: {num_simulations}")
print(f"Количество проигрышей: {num_losses}")
print(f"Вероятность проигрыша: {probability_of_loss}")

# Визуализация распределения длины игр, закончившихся проигрышем
losses = [r for r in results if r is not None] # Список длительностей игр, закончившихся проигрышем
plt.hist(losses, bins='sturges')  # Построение гистограммы
plt.title("Распределение длины игр, закончившихся проигрышем")
plt.xlabel("Число раундов")
plt.ylabel("Частота")
plt.show()
