import os

def func(Path):
    ar1 = []  # массив root
    ar3 = []  # массив файлов

    # получаем массив root и массив файлов. 
    # Если нет подкаталогов, то массив файлов будет корректно заполненным.
    # Если подкатологи есть, массив файлов будет заполнен некорректно,
    # но выход из функции произойдет раньше, чем работа с данным массивом
    for root, dirs, files in os.walk(Path):
        ar1.append(root)
        ar3 = files
    
    # если существует больше чем один элемент root, значит есть
    # подкаталоги
    if len(ar1) > 1:
        return False

    for i in range(len(ar3)):
        name = os.path.join(ar1[0], ar3[i]) 
        os.remove(name)  # удаление файла
    os.rmdir(Path)  # удаление каталога
    return True

p = "test_directory2"
print(func(p))
