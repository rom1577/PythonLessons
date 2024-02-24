def func3_2(a, b, path):
    sum = 0  # сумма чисел из двух файлов

    # цикл для последовательной обработки двух файлов
    for i in range(2):
        if i == 0: file = a
        else: file = b

        with open(path + str(file) + ".txt", "r") as f:
                try:
                    for j in range(3):
                        s = f.readline()
                        sum += int(s)
                except Exception:
                    return [0, 1]
    return [sum, 0]

# предполагается, что файлы находятся в одной директорииш
print("Сумма равна = ", func3_2(1, 10, ""))

