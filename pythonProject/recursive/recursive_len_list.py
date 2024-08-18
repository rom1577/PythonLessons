def calculate_length_of_list(list_of_numbers: list):
    try:
        list_of_numbers.pop(0)
        return 1 + calculate_length_of_list(list_of_numbers)
    except IndexError:
        return 0

