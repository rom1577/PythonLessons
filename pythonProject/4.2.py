import random
'''
В качестве метода для переоперделения используется метод drive().
'''

# класс автомобиль
class Auto:
    def __init__(self, max_user_velocity):
        self._max_velocity = max_user_velocity  # максимальная скорость машины
        self._cur_velocity = 0  # текущая скорость машины

    # метод езды
    def drive(self):
        self._cur_velocity = self._max_velocity  # присваивание текущей скорости максимальной
        print("Класс Auto() - родитель")

# класс грузовик
class Truck(Auto):
    def __init__(self, max_user_velocity, status_user):
        super().__init__(max_user_velocity)
        self.__status = status_user  # статус грузовика

    # переопределение метода drive() - скорость грузовика зависит от его статуса
    def drive(self):
        print("Класс Truck() - потомок")
        if self.__status == "загружен":
            self._cur_velocity = self._max_velocity / 2  # если грузовик загружен, то его максимальная скорость меньше
        elif self.__status == "разгружен":
            self._cur_velocity = self._max_velocity  # если грузовик загружен, то его максимальная скорость больше
        else:
            self._cur_velocity = 0  # если статус грузовика неопределен, то его максимальная скорость равна 0

# класс специальных машин
class Special_machine(Auto):
    def __init__(self, max_user_velocity):
        super().__init__(max_user_velocity)

    # переопределение метода drive() - спец машина уздит задним ходом при уборке
    def drive(self):
        print("Класс Special_machine() - потомок")
        self._cur_velocity = - self._max_velocity
# создание массива для записи экземпляров
c = []

# цикл записи экзепляров классов потомков в массив "с"
for i in range(0,500):
    m = random.randint(0,1)
    if m == 0:
        c.append(Truck(20, "загружен"))
    else:
        c.append(Special_machine(30))

# исполнение метода drive() в цикле для каждого элемента массива "с"
for dr in c:
    dr.drive()

'''
Данный вывод получается из-за механизма "полиморфизм подтипов". Автоматически выбирается нужна версия метода в
зависимости от типа объекта. Т.е. когда в цикле "dor dr in c" элемент массива "c" в данную итерацию является
объектом класса Truck(Auto), то вызывается метод drive() из класса Truck(Auto). Если из класса Special_machine(Auto),
то метод drive() вызывается из него. Этот выбор происходит автоматически.

Метод drive() из класса Auto не вызывается, т.к. в классах Truck(Auto) и Special_machine(Auto) данный метод
переопределяется.
'''
