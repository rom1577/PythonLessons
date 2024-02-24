import random

def func(array, number):
    dictc = {}
    array_out = []

    # подсчет количества элементов списка, используя словарь
    for elem in array:
        # если ключ elem уже существует
        if elem in dictc:
            dictc[elem] += 1
        # если ключа elem ещё нет
        else:
            dictc[elem] = 1

    for key,value in dictc.items():
        # заполнение выходного списка значениями, которые повторяются не менее number раз
        if value >= number:
            array_out.append(key)

    return array_out

ar = []
N = 10
for i in range(100):
    ar.append(random.randint(1,10))
print(func(ar, N))
