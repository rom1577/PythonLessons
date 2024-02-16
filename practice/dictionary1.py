import random

k = []  # массив ключей
dict = {}

# заполнение массива ключей
for i in range(100):
    k.append(i)

# заполнение словаря
for i in range(100):
    val = str(random.randint(200,300))
    dict[k[i]] = val
    
# с помощью метода pop() считывание по ключам k[i] значений, вывод на консоль, удаление пар ключ-значение
for i in range(100):
    print(dict.pop(k[i]))





