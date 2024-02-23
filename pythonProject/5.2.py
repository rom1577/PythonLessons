# класс автомобиль
class Auto:
    def __init__(self, user_name,max_user_velocity, user_cost):
        self.name = user_name  #  название машины
        self.max_velocity = max_user_velocity  # максимальная скорость машины
        self.cur_velocity = 0  # текущая скорость машины
        self.cost = user_cost  # стоимость машины

    # геттер возвращения скорости
    def get_velocity(self):
        return self.cur_velocity
    # метод езды
    def drive(self):
        self.cur_velocity = self.max_velocity  # присваивание текущей скорости максимальной

    # метод остановки машины
    def stop(self):
        self.cur_velocity = 0  # обнуление текущей скорости машины

    # метод ремонта машины
    def repair(self):
        self.cost -= 1  # стоимость машины уменьшается на 1 у.е.
        self.stop()  # машина стоит при ремонте

# класс грузовик
class Truck(Auto):
    def __init__(self, user_name, max_user_velocity, user_cost, user_max_weght):
        super().__init__(user_name, max_user_velocity, user_cost)
        # статус грузовика. "0" - разгружен; "1" - разгружается; "2" - загружается; "3" - "загружен"
        self.__status = 0
        self.__cur_weight = 0  # текущий вес груза
        self.__max_weight = user_max_weght  # максимально возможный вес груза

    # переопределение метода drive()
    def drive(self):
        if self.__status == 3:
            self.cur_velocity = self.max_velocity / 2  # если грузовик загружен, то его максимальная скорость меньше
        elif self.__status == 0:
            self.cur_velocity = self.max_velocity  # если грузовик загружен, то его максимальная скорость больше
        else:
            self.cur_velocity = 0  # если статус грузовика неопределен, то его максимальная скорость равна 0

    # метод загрузки груза
    def load(self, weight_load):
        self.__status = 2  # изменение статуса
        self.__cur_weight += weight_load  # увеличение веса текущего груза
        Auto.stop(self)  # грузовик стоит

        # если достигнут или превышен максимальный вес груза, то изменяется статус и текущий вес максимален
        if self.__cur_weight >= self.__max_weight:
            self.__status = 3
            self.__cur_weight = self.__max_weight

    # разгрузка грузовика
    def unload(self, unload_weight):
        self.__status = 1  # изменение статуса
        self.__cur_weight -= unload_weight  # уменьшение веса текущего груза
        Auto.stop(self)  # грузовик стоит

        # если весь груз разгружен, то текущий вес груза равен нулю и меняется статус
        if self.__cur_weight <= 0:
            self.__cur_weight = 0
            self.__status = 0

# класс специальных машин
class Special_machine(Auto):
    def __init__(self, user_name, max_user_velocity, user_cost, user_flow_solt, user_lifetime, user_weight_solt):
        super().__init__(user_name, max_user_velocity, user_cost)
        self.__flow_solt = user_flow_solt  # расход соли для посыпания дорог в кг/мин
        self.__weight_solt = user_weight_solt  # вес соли
        self.__lifetime = user_lifetime  # ресурс щётки для чистки асфальта
        self.__new_lifetime = user_lifetime  # ресурс щётки для чистки асфальта

    # метод распыливания соли на асфальт
    def spray_solt(self, time):
        self.__weight_solt -= time * self.__flow_solt  # уменьшается вес соли в машине
        if self.__weight_solt <= 0:  # если соль кончилась, то её вес равен нулю и машина останавливается
            self.__weight_solt = 0
            Auto.stop(self)

    # метод чистки асфальта щёткой
    def clean(self, time_work):
        self.__lifetime -= time_work  # уменьшение ресурса щётки

        # если достигнут предельный ресурс щётки, то ресурс обновляется и машина идёт на ремонт
        if self.__lifetime < 10:
            self.__lifetime = self.__new_lifetime
            Auto.repair(self)

# работа с классами
kamaz = Truck("Камаз", 200, 1000, 30)
kamaz.drive()  # пустой камаз доехал до точки
print(kamaz.get_velocity())  # скорость камаза
kamaz.load(15)  # загрузка камаза
kamaz.load(15)
kamaz.drive()  # камаз доехал до точки
print(kamaz.get_velocity())  # скорость камаза

tractor = Special_machine("a",50, 1000, 5, 25, 15)
tractor.drive()  # трактор поехал
tractor.spray_solt(2)  # трактор распылил соль 2 минуты
tractor.clean(5)  # трактор почистил асфальт 5 минут

# класс животное
class Animal():
    def __init__(self, user_weight):
        self.cur_speed = 0  # начальная скорость животного равна нулю
        self.weight = user_weight  # вес животного

    # метод бега животного
    def run(self, speed):
        self.cur_speed = speed  # устанавливается скорость животного при беге

    # метод остановки животного
    def stop(self):
        self.cur_speed = 0  #  остновка животного

    # метод поедания еды дивотным
    def eat(self, weight_eat):
        self.weight += weight_eat # увеличение веса животного

# класс корова
class Cow(Animal):
    def __init__(self, user_weight, user_cur_age, user_max_age):
        super().__init__(user_weight)
        self.__num_milk = 0  # количество молока с одной дойки
        self.__max_age = user_max_age  # количество лет жизни
        self.__cur_age = user_cur_age  # возраст коровы на данный момент
        self.__meet = 0

    # метод доения коровы в зависимости от времени года
    def milk(self, season):
        Animal.stop(self)
        if season == "лето" or season == "весна":
            self.__num_milk = 20
        else:
            self.__num_milk = 10

    # метод взросления коровы
    def grow_up(self):
        self.__cur_age += 1  # увеличение года жизни на 1

    # метод получения с коровы мяса, если она достигла максимального возраста
    def meet(self):
        if self.__cur_age >= self.__max_age:
            self.__meet = self.weight  # вес коровы переходит в вес мяса
            self.__num_milk = 0  # корова больше не дает молоко

# класс овцы
class Sheep(Animal):
    def __init__(self, user_weight, user_weight_wool):
        super().__init__(user_weight)
        self.__stress_level = 0  # уорвень стресса овцы
        self.__weight_wool = user_weight_wool  # вес шерсти овцы

    # метод страха стрижки
    def fear(self):
        Animal.stop(self)  # остановка овцы
        self.__stress_level += 1  # повышения уровня стресса

    # метод стрижки овцы
    def wool(self):
        self.fear()  # вызов метода страха
        self.__weight_wool += 1  # увеличение веса собранной шерсти
        self.weight -= self.__weight_wool  # снижение веса овцы за счёт снятия шерсти

masha = Cow(10, 5, 25)  # объект коровы Маша
masha.milk("лето")  # дойка Маши летом
masha.grow_up()  # увеличение возраста Маши

barash = Sheep(20, 2)
barash.wool()  # подстригаение овцы

