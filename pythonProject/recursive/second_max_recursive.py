def find_second_max_input(list_of_numbers: list):
    if len(list_of_numbers) < 2:
        return None

    if list_of_numbers[0] > list_of_numbers[1]:
        max1 = list_of_numbers[0]
        max2 = list_of_numbers[1]
    else:
        max1 = list_of_numbers[1]
        max2 = list_of_numbers[0]
    return find_second_max(list_of_numbers[2:], max1, max2)

def find_second_max(list_of_numbers: list, first_max_element: int, second_max_element: int)->int:
    if len(list_of_numbers) == 0:
        return second_max_element

    if list_of_numbers[0] >= first_max_element:
        second_max_element = first_max_element
        first_max_element = list_of_numbers[0]
    elif list_of_numbers[0] > second_max_element:
        second_max_element = list_of_numbers[0]

    return find_second_max(list_of_numbers[1:], first_max_element, second_max_element)

