# симуляция подбрасывания монеты с выиграл/проиграл
import random as rnd

side = input('Выберите сторону монеты: "Орел" или "Решка":')

def flip():
    result = rnd.choice(['Орел', 'Решка'])
    return result

flip_result = flip()

if flip_result == side:
    print(f'{flip_result} - ВЫ ПОБЕДИЛИ!')
else:
    print(f'{flip_result} - ВЫ ПРОИГРАЛИ!')
