import random

def func(array, number):
    # инициализация словаря
    dict = {1:0, 2:0, 3:0, 4:0, 5:0,
            6:0, 7:0, 8:0, 9:0, 10:0}
    array_out = []

    # подсчет количества элементов списка от 1 до 10, используя словарь
    for elem in array:
        dict[elem] += 1

    for key,value in dict.items():
        # заполнение выходного списка значениями, которые повторяются не менее number раз
        if value >= number:
            array_out.append(key)

    if len(array_out) == 0:
        print("Число не повторяется указанное количество раз")
        return array_out

    return array_out

ar = []
n = 13
for i in range(100):
    ar.append(random.randint(1,10))
print(func(ar, n))
