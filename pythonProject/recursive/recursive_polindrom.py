def is_polindrom(string:str):
    '''
    :return 1 - строка полиндром
    :return 0 - строка не полиндром
    '''
    string = ''.join(string.split())
    string = string.lower()

    if len(string) == 0:
        return 1

    if string[0] == string[-1]:
        return is_polindrom(string[1:-1])
    return 0

