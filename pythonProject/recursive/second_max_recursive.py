from functools import reduce

def find_second_max(list_of_numbers: list, first_max_element: int):
    '''
    Функция для расчета второго максимального элемента списка
    '''
    if len(list_of_numbers) == 1:
        return list_of_numbers[0] if list_of_numbers[0] != first_max_element else None

    second_max_element = find_second_max(list_of_numbers[1:], first_max_element)

    if list_of_numbers[0] != first_max_element:
        return max(list_of_numbers[0], second_max_element) if second_max_element is not None else list_of_numbers[0]
    elif list_of_numbers.count(list_of_numbers[0]) > 1:
        return first_max_element
    else:
        return second_max_element

def find_first_max(x, y):
    '''
    Функция для нахождения первого максимального элемента в списке
    '''
    return x if x > y else y

def find_second_max_input(list_of_numbers: list):
    '''
    Функция вызова для нахождения второго максимального элемента в списке
    '''
    if len(list_of_numbers) < 2:
        return None

    first_max = reduce(find_first_max, list_of_numbers)
    return find_second_max(list_of_numbers, first_max)  # Определение второго максимального элемента

