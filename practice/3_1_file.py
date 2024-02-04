from random import randint

for i in range(1,11):
    # откыртие файла с помощью директивы with
    with open(str(i) + ".txt", "w") as fi:
        # получение рандомных чисел
        a = randint(1, 10)
        b = randint(1, 10)
        c = randint(1, 10)

        # запись трех чисел с новой строки
        fi.write(str(a) + "\n")
        fi.write(str(b) + "\n")
        fi.write(str(c))


