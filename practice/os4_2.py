import os
from os4_1 import func

def func2(Path):
    # вызов функции из задания 4.1
    arr = func(Path,".*",False)

    if len(arr[0]) > 0:
        return False
    for i in arr[1]:
        os.remove(os.path.join(Path, i))  # удаление файла
    os.rmdir(Path)  # удаление каталога
    return True

p = "test_directory"
print(func2(p))
