import os

def func(directory, extension, flag):
    ar1 = []  # массив root
    ar2 = []  # массив массивов имён папок
    ar3 = []  # массив массивов имён файлов
    
    # с помощью функции os.walk() записываем в массивы root, массив папок, массив файлов
    for root, dirs, files in os.walk(directory):
        ar1.append(root)
        ar2.append(dirs)
        ar3.append(files)
    
    ss1_files = []  # массив имён файлов, нахдоящихся исходной директории
    ss1_dir = []  # массив имён папок, находящихся в исходной директории
    ss2_files = []  # массив имён файлов, находящихся в подподкаталоге первого уровня
    ss2_dir = []  # массив имён папок, находящихся в подкаталоге первого уровня

    # для каждой строки root из массива выполняем следующий алгоритм
    for i in range(len(ar1)):
        s = list(ar1[i])
        count = 0 

        # подсчёт количества знаков "/" в строке root
        for k in range(len(s)):
            if s[k] == "/":
                count += 1

        # если счётчик равен 0, то мы находимся в исходной директории
        if count == 0:
            for m in ar2[i]:
                ss1_dir.append(m)  # заполнение массива папок исходной директории
            for m in ar3[i]:
                g = m.split(".")  # разделение имени файла по символу "."
                if "." + g[1] == extension:  # если расширение файла равно заданному
                    ss1_files.append(m)  # заполнение массива файлов исходной директории
        
        # если счётчик равен 1, то мы находимся в подкатологе первого уровня 
        # относительно исходной директории
        if count == 1:
            for m in ar2[i]:
                ss2_dir.append(m)  # заполнение массива папок подкаталога первого уровня
            for m in ar3[i]:
                g = m.split(".")  # разделение имени файла по символу "."
                if "." + g[1] == extension:  # если расширение файла равно заданному
                    ss2_files.append(m)  # заполнение массива файлов подкаталога первого уровня
    if flag:
        
        return [ss1_dir + ss2_dir, ss1_files + ss2_files]
    else:
        return [ss1_dir, ss1_files]
   

# использование функции
directory_path = "test_directory"  # путь выбранной директории
file_extension = ".txt"  # расширение
print(func(directory_path, file_extension, True))
