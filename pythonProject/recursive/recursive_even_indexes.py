def find_even_indexes(number_list: list, i=0):
    if i == len(number_list):
        return
    if number_list[i] % 2 == 0:
        print(i)
    i += 1
    return find_even_indexes(number_list, i)

