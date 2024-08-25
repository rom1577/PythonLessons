def find_second_max_input(list_of_numbers: list):
    '''
    Функция вызова для нахождения второго максимального элемента в списке
    '''
    if len(list_of_numbers) < 2:
        return None
    return find_second_max(list_of_numbers, list_of_numbers[0])[1]  # Определение второго максимального элемента

def find_second_max(list_of_numbers: list, first_max_element: int)->int:
    '''
    Функция нахождения второго максимального элемента в списке
    '''

    # Опредлеение первого максимального числа при прямом ходе рекурсии
    if list_of_numbers[0] > first_max_element:
        second_max_element = first_max_element
        first_max_element = list_of_numbers[0]
    else:
        second_max_element = list_of_numbers[0]

    if len(list_of_numbers) == 1:
        return first_max_element, second_max_element

    first_max_element, second_max_element = find_second_max(list_of_numbers[1:], first_max_element)

    # Опредлеение второго максимального числа при обратном ходе рекурсии
    if list_of_numbers.count(first_max_element) != 1 and list_of_numbers.count(first_max_element) != 0:
        second_max_element = first_max_element
    elif list_of_numbers[0] > second_max_element and list_of_numbers[0] < first_max_element:
        second_max_element = list_of_numbers[0]

    return first_max_element, second_max_element

