'''
7.1

today_sunny - is_sunny  # проверка солнечная ли погода
hungry_dwarf - is_hungry  # проверка голодный ли Дварф
online_user - is_online  # проверка пользователь ли в ести
authenticated_user - is_authenticated  # прошел ли пользователь аутентификацию
student - is_student  # является ли переменная типо студент
'''

'''
7.2

# пример с done
done = False
for i in range(len(diametr_of_chamber_list)):
    diametr_with_ribers_m = diametr_of_chamber_list[i] + 2 * thikness_of_riber_m
    step_of_ribers_m = 3.14 * diametr_with_ribers_m / number_of_ribers
    step_of_ribers_list = np.append(step_of_ribers_list, step_of_ribers_m)
done = True 

# пример с success
done = False
for i in range(len(diametr_of_chamber_list)):
    diametr_with_ribers_m = diametr_of_chamber_list[i] + 2 * thikness_of_riber_m
    step_of_ribers_m = np.pi * diametr_with_ribers_m / number_of_ribers
    step_of_ribers_list = np.append(step_of_ribers_list, step_of_ribers_m)
done = True 

if(done):
    success = True
else:
    success = False
    
# пример с found, когда ищется определённый пользователь
found = False
for i in list_of_id_user:
    if i == 1:
        found = True
'''

'''
7.3

# перменная цикла определяет локальный максимум массива, сравнивая 2 рядом стаящих элемента
for local_max_diametr in range(len(diametr_of_chamber_list)-1):
    if diametr_of_chamber_list[local_max_diametr] > diametr_of_chamber_list[local_max_diametr+1]:
        break

print("Максимальный диаметр = ", local_max_diametr)
'''

'''
7.4

# пример 1
# например класс Node, используемый в качестве узла двунаправленного связного списка
# имеет поля prev, next
class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

# пример 2
# используем переменные-антонимы для обозначения начала и конца среза списка
diametr_of_chamber_list = [i for i in range(20)]
start_point = 2
finish_point = 10
actual_diamettr_list = diametr_of_chamber_list[start_point:finish_point]
'''

'''
7.5

# № 1
# Функция, которая получает список из 100 значений
# (сгенерованные заранее с числами в диапазоне от 1 до 10) 
# и число N, и выдаёт список из тех значений в этом списке, 
# которые повторяются не менее N раз

# Исходный вариант:

import random

def func2(val, N):
    array_out = []
    dictionary = {}
    for value in val:
        if value in dictionary:
            dictionary[value] += 1
        else:
            dictionary[value] = 1

        if dictionary[value] == N:
            array_out.append(value)
    return array_out

# Измененный вариант:

import random

def find_repeated_val(input_list_100_elem, N):
    repeated_val_list = []
    freq_dict_1_to_10 = {}
    for value in input_list_100_elem:
        if value in dictionary:
            freq_dict_1_to_10[value] += 1
        else:
            freq_dict_1_to_10[value] = 1

        if freq_dict_1_to_10[value] == N:
            repeated_val_list.append(value)
    return repeated_val_list


# №2
# Написан класс Stack, который имеет метод pop(), size(), push(). В методе pop() 
# есть лишняя переменная b и имеются невыразительные имена

# Исходный вариант

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() != 0:
            a = self.stack[0]
            b = self.stack
            b.pop(0)
            self.stack.pop(0)
            return a
        return None
    
    def push(self, value):
        self.stack.insert(0,value)
        
# Измененный вариант

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() != 0:
            first_elem_of_stack = self.stack[0]
            self.stack.pop(0)
            return first_elem_of_stack
        return None
    
    def push(self, value):
        self.stack.insert(0,value)
'''

