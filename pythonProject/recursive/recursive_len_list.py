def calculate_length_of_list(list_of_numbers: list):
    if not list_of_numbers:
        return 0
    list_of_numbers.pop(0)
    return 1 + calculate_length_of_list(list_of_numbers)

