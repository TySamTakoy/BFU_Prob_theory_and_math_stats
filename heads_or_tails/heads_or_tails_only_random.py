import random as rnd

num = int(input('Введите требуемое кол-во экспериментов:'))

def flip():
    result = rnd.choice(['Орел', 'Решка'])
    return result

tr = 0
fls = 0

for i in range (num + 1):
    flip_result = flip()
    if flip_result == 'Орел':
        tr += 1
    else:
        fls += 1
    
rtr = tr/num*100
rfls = fls/num*100

rtr = round(rtr, 3)
rfls = round(rfls, 3)

print(f'Итоговый счет: Орел - {tr}, Решка - {fls}')
print(f'Процентное соотношение выпадения Орлов к выпадению Решек: {rtr}% : {rfls}%')
