# №1
# неверный вариант
my_numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(my_numbers)):
    for j in range(len(my_numbers[i])):
        print(my_numbers[i][j])

# верный вариант
my_numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row_idx, row in enumerate(my_numbers):
    for col_idx, value in enumerate(row):
        print(value)

# заменил обращение по индексу во вложенном цикле на обращение к элементам через функцию enumerate


# №2
# неверный вариант
my_numbers = [1, 2, 3, 4]

for i in range(len(my_numbers)):
    my_numbers[i] = my_numbers[i] ** 2

# верный вариант
my_numbers = [1, 2, 3, 4]
my_numbers = map(lambda x: x ** 2, my_numbers)

# при возведении каждого элемента массива в квадрат в неверном варианте использовал поиндексное обращение в цикле,
# в верном варианте использовал функцию map, не обращаясь в массиве по индексу и не используя цикл


# №3
# неверный вариант
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []
for i in range(len(my_numbers)):
    if my_numbers[i] % 2 == 0:
        even_numbers.append(my_numbers[i])

# верный вариант
my_numbers_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers_set = {number for number in my_numbers_set if number % 2 == 0}

# в неверном варианте использовал поиндексное обращение к массиву для нахождения всех четных чисел,
# в верном варианте использовал множество и заполнение его без использования обращения по индексу к массиву


# №4
# неверный вариант
my_numbers = [10, 5, 20, 20, 4, 8, 15]

# Проверка на наличие хотя бы двух элементов
if len(my_numbers) < 2:
    print("Длина слишком маленькая")

max_num = my_numbers[0]
second_max = float('-inf')

# Проходим по элементам массива для поиска второго максимального элемента
for i in range(1, len(my_numbers)):
    if my_numbers[i] > max_num:
        second_max = max_num
        max_num = my_numbers[i]
    elif my_numbers[i] > second_max and my_numbers[i] != max_num:
        second_max = my_numbers[i]

# верный вариант
my_stack = [10, 5, 20, 20, 4, 8, 15]

# Проверка на наличие хотя бы двух элементов
if len(my_stack) < 2:
    print("Длина слишком маленькая")

first_max = float('-inf')
second_max = float('-inf')

# Проходим по элементам стека для поиска второго максимального элемента
while my_stack:
    value = my_stack.pop()

    if value > first_max:
        second_max, first_max = first_max, value
    elif first_max > value and value > second_max:
        second_max = value

# использовал стек для нахождения второго максимального элемента вместо использования массива


# №5
# неверный вариант
my_numbers = [10, 5, 20, 20, 4, 8, 15]

max_value = my_numbers[0]
for i in range(1, len(my_numbers)):
    if max_value[i] > max_value:
        max_value = max_value[i]

# верный вариант
from queue import Queue

my_list = [10, 5, 20, 20, 4, 8, 15]
my_queue = Queue()  # Создаем очередь
my_queue.put(my_list)
max_value = my_queue.get()  # Извлекаем первый элемент и считаем его максимальным

my_queue2 = Queue()
my_queue2.put(max_value)  # Сохраняем извлеченный элемент во временную очередь

while not my_queue.empty():
    current = my_queue.get()  # Извлекаем текущий элемент из очереди
    if current > max_value:
        max_value = current  # Обновляем максимум, если находим большее значение
    my_queue2.put(current)  # Сохраняем текущий элемент во временную очередь

# Возвращаем все элементы обратно в исходную очередь
while not my_queue2.empty():
    my_queue.put(my_queue2.get())

# использовал очередь для поиска максимального элемента списка вместо поиндексного обращения к массиву

