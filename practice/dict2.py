import random

def func(array, number):
    dictc = {}
    array_out = []

    # подсчет количества элементов списка, используя словарь
    for elem in array:
        dictc[elem] = dictc.get(elem, 0) + 1
        if dictc[elem] == number:
            array_out.append(elem)

    return array_out

ar = []
N = 10
for i in range(100):
    ar.append(random.randint(1,10))
print(func(ar, N))
