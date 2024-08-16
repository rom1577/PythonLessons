def compute_number_in_degree(N_number:int, M_degree:int):
    if M_degree == 0:
        return 1
    return N_number * compute_number_in_degree(N_number, M_degree-1)

