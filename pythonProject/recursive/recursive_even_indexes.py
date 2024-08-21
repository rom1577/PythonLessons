def find_even_element(number_list: list):
    if len(number_list) == 0:
        return

    a = number_list.pop(0)
    if a % 2 == 0:
        print(a)
    return find_even_element(number_list)

