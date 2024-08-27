def find_second_max_input(list_of_numbers: list):
    if len(list_of_numbers) < 2:
        return None

    if list_of_numbers[0] > list_of_numbers[1]:
        max1 = list_of_numbers[0]
        max2 = list_of_numbers[1]
    else:
        max1 = list_of_numbers[1]
        max2 = list_of_numbers[0]
    return find_second_max(list_of_numbers, max1, max2)

def find_second_max(list_of_numbers: list, first_max_element: int, second_max_element: int, i=2)->int:
    if i == len(list_of_numbers):
        return second_max_element

    if list_of_numbers[i] >= first_max_element:
        second_max_element = first_max_element
        first_max_element = list_of_numbers[i]
    elif list_of_numbers[i] > second_max_element:
        second_max_element = list_of_numbers[i]
    i +=1
    return find_second_max(list_of_numbers, first_max_element, second_max_element,i)

