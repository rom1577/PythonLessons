def find_second_max_input(list_of_numbers: list):
    if len(list_of_numbers) < 2:
        return None

    if list_of_numbers[0] > list_of_numbers[1]:
        max1 = list_of_numbers.pop(0)
        max2 = list_of_numbers.pop(0)
    else:
        max2 = list_of_numbers.pop(0)
        max1 = list_of_numbers.pop(0)
    return find_second_max(list_of_numbers, max1, max2)

def find_second_max(list_of_numbers: list, first_max_element: int, second_max_element: int)->int:
    if len(list_of_numbers) == 0:
        return second_max_element

    cur_element = list_of_numbers.pop(0)

    if cur_element >= first_max_element:
        second_max_element = first_max_element
        first_max_element = cur_element
    elif cur_element > second_max_element:
        second_max_element = cur_element

    return find_second_max(list_of_numbers, first_max_element, second_max_element)

