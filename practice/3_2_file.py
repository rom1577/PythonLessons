def func3_2(a, b, path):
    sum = 0  # сумма чисел из двух файлов

    # цикл для последовательной обработки двух файлов
    for i in range(2):
        if i == 0: file = a
        else: file = b

        count = 0
        with open(path + str(file) + ".txt", "r") as f:
                try:
                    for s in f:
                        sum += int(s)
                        count += 1
                except Exception:
                    return [0, 1]
        if count != 3:
            return [0, 2]
    return [sum, 0]

# предполагается, что файлы находятся в одной директорииш
print("Сумма равна = ", func3_2(1, 10, ""))

