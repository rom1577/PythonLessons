# класс кота с тремя полями
class Cat:
    def __init__(self, userName, userWeight, userFreq):
        self.__name = userName
        self.__weight = userWeight
        self.__fr = userFreq

    def getName(self):
        return self.__name
    def getWeight(self):
        return self.__weight
    def getFr(self):
        return self.__fr

listCats = []  # список для экземпляров
j = 1  # счётчик строки
n = 3  # поличество полей класса
with open("object.txt", "r") as f:
    for s in f:
       try:
            list = s.split(';')  # в качестве разделителя используется символ ";". Он удаляется
            for k in range(n):
                list[k] = list[k].rstrip()  # удаление символа "\n" в конце строки

            cats = Cat(list[0], float(list[1]), int(list[2]))  # создание экземпляра
            listCats.append(cats)  # запись экземпляра в список
            j += 1
       except ValueError:
           print("В строке ", j ," значение некоректного типа")
           j += 1
           continue
       except IndexError:
           print("Строка ", j, " содержит неверное количество полей")
           j += 1
           continue

# работа с одним экземпляром, если хотя бы один экземпляр существует
if (len(listCats) != 0):
    m = 0
    cat1 = listCats[m]
    print("Поля экземпляра под номером строки ",m + 1,":")
    print("Имя: ", cat1.getName())
    print("Вес:", cat1.getWeight())
    print("Частота мурлыкания: ", cat1.getFr())

