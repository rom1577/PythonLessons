'''
Моё решение прошлого задания не вписывается в понятие "композиция", потому что для
класса "Автомобиль" я создал подклассы "Грузовик" и "Специтехника" (разновидности автомобиля),
а не подклассы компоновки автомобиля (двери, колёса). Поэтому я создам новые классы.
'''

# класс Колесо
class Wheel:
    # конструктор
    def __init__(self, pressure_user):
        self.pressure = pressure_user  # давление в шинах
        self.massflow_air = 0.1 * 101325  # расход вулканизации

    # метод подкачки шин
    def inflating(self, time):
        self.pressure += time * self.massflow_air

    # метод уменьшения давления в шинах при езде в зависимости от скорости
    def decrease_pressure(self, speed, time_drive):
        if speed < 70:
            self.pressure = time_drive * 0.01 * 101325
        else:
            self.pressure = time_drive * 0.05 * 101325

# класс двигатель
class Engine:
    def __init__(self, temp_env_user, weight_user):
        self.weight = weight_user  # масса машины
        self.temperature_engine = 25  # температура двигателя
        self.consunotion = 15  # расход топлива двигателя
        self.temperature_enviroment = temp_env_user  # температура окружающей среды

    # метод охлаждения
    def cooling(self, speed):
        self.temperature_engine -= speed / 100  # уменьшение температуры двигателя

    # метод нагревания
    def heating(self, speed):
        self.temperature_engine += speed / 100 + 0.1 * self.temperature_enviroment  # увеличение температуры двигателя

    # увеличение крутящего момента
    def increase_torque(self, thrust_motor,speed):
        gravity_force = self.weight * 9.81  # сила тяжести машины
        if gravity_force > thrust_motor:  # если сила тяжести больше тяги двигателя
            self.heating(speed)
            self.consunotion += 2  # увеличение расхода топлива
        else:
            self.cooling(speed)
            self.consunotion -= 2

# класс автомобиль
class Car:
    # в конструкторе атрибуты wheel, engine - экземпляры соответствующих классов
    def __init__(self, pressure_user, temp_env_user, weight_user):
        self.wheel_left_front = Wheel(pressure_user)  # экземпляр класса Wheel()
        self.wheel_right_front = Wheel(pressure_user)  # экземпляр класса Wheel()
        self.wheel_left_back = Wheel(pressure_user)  # экземпляр класса Wheel()
        self.wheel_right_back = Wheel(pressure_user)  # экземпляр класса Wheel()
        self.engine = Engine(temp_env_user, weight_user)  # экземпляр класса Engine()
        self.speed = 0

    # метод езды автомобиля
    def drive(self):
        self.engine.consunotion -= 1
        self.speed = 10

    # метод остановки автомобиля
    def stop(self):
        self.speed = 0

car = Car(2 * 101325, 35, 1000)  # экземпляр класса Car
car.drive()  # автомобиль едет
print(car.engine.consunotion)  # вывод расхода автомобиля
print(car.speed)  # вывод скорости автомобился
car.engine.cooling(car.speed)  # выполнение охлаждения двигателя
print(car.engine.temperature_engine)  # вывод температуры двигателя
print(car.wheel_left_front.pressure)  # вывод давления в первом колесе

# класс тело
class Body:
    # конструктор класса
    def __init__(self, user_weight, user_weight_wool, user_size):
        self.weight = user_weight
        self.weight_wool = user_weight_wool
        self.size = user_size

    # увеличение размера тела
    def increase_size(self):
        self.weight += 1
        self.size += 1

    # увеличение волосянного покрова, в зависимости от температуры
    def wooling(self, temperature):
        if temperature > 30:
            self.weight_wool -= 1
        else:
            self.weight_wool += 1

# класс голова
class Head:
    # конструктор класса
    def __init__(self):
        self.angle = 0  # угол поворота головы

    # метод вращения головой при опасности
    def rotate(self, danger_side):
        if danger_side == "left":
            self.angle  = 30
        if danger_side == "right":
            self.angle  = -30

    # метод изадавания звуков
    def voice(self, single):
        print(single)

# класс животное
class Animal:
    # в конструкторе атрибуты body, head - экземпляры соответствующих классов
    def __init__(self, user_weight, user_weight_wool, user_size):
     self.body = Body(user_weight, user_weight_wool, user_size)  # экземпля класса Body()
     self.head = Head()  # экземпляр класса Head()
     self.emotion = "None"  # эмоция животного

    # метод употребления еды
    def eat(self):
        self.body.increase_size()
        self.emotion = "Good"

    # метод атаки
    def attack(self):
        self.emotion = "Angry"
        self.head.voice("RRR-rrr-RRR")


wolf = Animal(50, 10, 1500)  # создание экземпляра класса Animal()

wolf.head.rotate("left side")  # поворот головы на опасность слева
wolf.attack()  # атака противника
wolf.eat()  # поедание противника
wolf.head.voice("MMM-mmm-MMM")  # голос животного
print(wolf.body.weight)  # на сколько увеличился вес
print(wolf.body.size)  # на сколько увеличился размер




