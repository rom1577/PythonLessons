def find_even_indexes(number_list: list, i=0):
    if i == len(number_list):
        return

    print(number_list[i])
    return find_even_indexes(number_list, i+2)

