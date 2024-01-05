for i in range(100,1000):
    a = i // 100 + i // 10 % 10 + i % 10
    if a != 15:
        continue
    print(i)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
