import random

def func(array, number):
    # инициализация словаря
    dict = {1:0, 2:0, 3:0, 4:0, 5:0,
            6:0, 7:0, 8:0, 9:0, 10:0}
    array_out = []

    # подсчет количества элементов списка от 1 до 10, используя словарь
    for elem in array:
        dictc[elem] += 1

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
