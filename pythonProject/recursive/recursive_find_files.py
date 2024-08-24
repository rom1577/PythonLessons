import os

def make_dir_generator(directory: str)->list:
    walk_generator_list = list(os.walk(directory))
    return find_all_files(walk_generator_list, [])

def find_all_files(walk_generator_list: list, List: list)->list:
    '''
    Функция нахождения всех файлов в директории и в поддиректориях
    '''
    if len(walk_generator_list) == 0:
        return List

    for file in walk_generator_list[0][2]:
        List.append(file)

    find_all_files(walk_generator_list[1:], List)
    return List

