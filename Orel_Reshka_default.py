import random as rnd

def flip():
    result = rnd.choice(['Орел', 'Решка'])
    return result

N = int(input('Введите численное кол-во подбрасываний:\n'))

print(f'Проводим симуляциию {N} подбрасывания(-ий) монеты:')
for i in range(N):
    flip_result = flip()
    print(f'Flip {i + 1}: {flip_result}')