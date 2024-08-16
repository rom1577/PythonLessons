def compute_sum_of_digits_in_number(number:int):
    # оперделение порядка числа
    number_order = 1
    while number // number_order >= 10:
        number_order *= 10

    if number_order == 1:
        return number
    return number // number_order + compute_sum_of_digits_in_number(number % number_order)

