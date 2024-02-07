def func3_2(a, b, path):
    sum = 0  # сумма чисел из двух файлов

    # цикл для последовательной обработки двух файлов
    for i in range(2):
        if i == 0: file = a
        else: file = b

        count_rows = 0  # счётчик количества строк в файле
        with open(path + str(file) + ".txt", "r") as f:
            try:
                # для каждой строки в файле
                for s in f:
                    s.rstrip()  # уборка "\n" символов
                    count_rows += 1
                    element = float(s)
                    sum += element
            # обработка исключения, если данные файле были другого типа и выход из функции
            except ValueError:
                raise ValueError("Проверьте файл " + str(file) + ".txt на корректность типа содержимых данных")

            # продолжение после блока try
            else:
                # проверка на то, чтобы количество заполненных строк в файле было ровно 3
                if count_rows != 3:
                    # генерация исключения и выход из функции
                    raise IndexError("Количесво заполненных строк в файле " + str(file) + ".txt должно быть 3")
    return sum

# предполагается, что файлы находятся в одной директорииш
print("Сумма равна = ", func3_2(1, 2, "/mnt/c/python_lesson/practice/"))
