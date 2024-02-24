"Импорт рандома"
import random

def func(array, number):
    "func получает список и число N, и выдаёт список из тех значений \
    в этом списке, которые повторяются не менее N раз \
    :array - список; \
    :number - число; \
    :return - список"
    # инициализация словаря
    # dict = {1:0, 2:0, 3:0, 4:0, 5:0,
    #         6:0, 7:0, 8:0, 9:0, 10:0}
    dictc = {}
    array_out = []

    # подсчет количества элементов списка от 1 до 10, используя словарь
    for elem in array:
        dictc[elem] += 1
    # заполнение выходного списка значениями, которые повторяются не менее number раз
    for key,value in dictc.items():
        if value >= number:
            array_out.append(key)

    if len(array_out) == 0:
        print("Число не повторяется укащанное количество раз")
        return array_out

    return array_out

ar = []
N = 10
for i in range(100):
    ar.append(random.randint(1,10))
print(func(ar, N))
