
class Animal:  # Класс описывает поля животных, которые дают молоко
    def __init__(self, user_name, user_size, user_velocity, user_weight):
        self.__name = user_name  # вид животного
        self.__size = user_size  # размер животного
        self.__stress_level = 10  # уровень стресса животного по умолчанию
        self.__velocity = user_velocity  # скорость животного
        self.__weight = user_weight  # вес животного

    # добавление геттеров для приватных полей
    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def get_stress_level(self):
        return self.__stress_level

    def get_velocity(self):
        return self.__velocity

    def get_weight(self):
        return self.__weight

    # метод определяет скорость животного, если оно стоит
    def stop(self):
        self.__velocity = 0

    # метод оперделяет поведение животного во сне
    def sleep(self):
        self.__stress_level = 10  # сброс уровня стресса
        self.stop()  # скорость равно нулю

    # метод поведения животного при еде
    def eating(self, grass):
        self.__stress_level -= 1  # уменьшение уровня стерсса
        self.__weight += grass  # увеличение веса

    # метод поведения животного при дойке
    def milking(self):
        self.__stress_level += 10  # увеличение уровня стресса
        if self.__stress_level >= 20:  # если уровень стресса првеышает 30, то животное не выдерживает и засыпает
            self.sleep()

    # метод увеличения размера животного (при взрослении)
    def exchange_size(self):
        self.__size *= 2

# создание объекта класса Animal для животного "Корова"
Cow = Animal("Корова", 150, 2, 100)
# получение значения приватных полей через геттеры
print(Cow.get_name(), Cow.get_size(), Cow.get_stress_level(), Cow.get_velocity(), Cow.get_weight())
Cow.milking()
Cow.eating(20)
Cow.sleep()
print(Cow.get_name(), Cow.get_size(), Cow.get_stress_level(), Cow.get_velocity(), Cow.get_weight())

# Создание объекта класса Animal для животного "Лама"
Lama = Animal("Лама", 75, 5, 80)
print(Lama.get_name(), Lama.get_size(), Lama.get_stress_level(), Lama.get_velocity(), Lama.get_weight())
Lama.sleep()  # сон ламы
Lama.eating(10)  # поедание травы на 10 у.е.
print(Lama.get_name(), Lama.get_size(), Lama.get_stress_level(), Lama.get_velocity(), Lama.get_weight())

class Dwarf:
    # класс Dwarf, в котором описано поведение Дварфов
    def __init__(self, user_name, user_status, user_health, user_velocity, user_hunger):
        self.__name = user_name  # имя пользователя
        self.__status = user_status  # статус игрока
        self.__health = user_health  # уровень здоровья
        self.__velocity = user_velocity  # скорость бега
        self.__hunger_level = user_hunger  # уровень голода

    # добавление геттеров для приватных полей
    def get_name(self):
        return self.__name

    def get_status(self):
        return self.__status

    def get_health(self):
        return self.__health

    def get_velocity(self):
        return self.__velocity

    def get_hunger_level(self):
        return self.__hunger_level

    # метод получения ранения. Задается получаемый урон, который вычитается из уровня здоровья. Изменяется статус игрока
    def injury(self, damage):
        self.__health -= damage
        self.__status = "injured"
        if self.__health <= 0:
            self.__status = "dead"

    # метод использования аптечки. Увеличивается уровень здоровья при использовании аптечки
    def medicine_kit(self, kit_effect):
        self.__health += kit_effect

    # метод остановки игорока. При остановке скорость игрока равна нулю
    def stop(self):
        self.__velocity = 0

    # метод поедания еды. Игрок останавливается, увеличивает своё здоровье и уровень голода
    def eating(self):
        self.stop()
        self.__health += 0.5
        self.__hunger_level += 5

    # метод бега. Задается скорость бега. Уменьшается уровень голода
    def run(self, speed):
        self.__velocity = speed
        self.__hunger_level -= 1
        if self.__hunger_level <= 0:
            self.stop()

# Создание объектов, вызов методов из класса Guy и демонстрация того, как меняются поля объекта (класса)
Nikolas = Dwarf("Nikolas", "normal", 100, 5, 10)
print(Nikolas.get_name(), Nikolas.get_status(), Nikolas.get_health(), Nikolas.get_velocity(), Nikolas.get_hunger_level())
Nikolas.injury(89)  # ранение на урон 89 жизней
Nikolas.medicine_kit(8)  # восстановление аптечкой 8 жизней
Nikolas.eating()  # перерыв на еду
Nikolas.run(10)  # бег со скоростью 10
print(Nikolas.get_name(), Nikolas.get_status(), Nikolas.get_health(), Nikolas.get_velocity(), Nikolas.get_hunger_level())

Vasya = Dwarf("Vasya", "normal", 70, 10, 4)
print(Vasya.get_name(), Vasya.get_status(), Vasya.get_health(), Vasya.get_velocity(), Vasya.get_hunger_level())
Vasya.injury(71) # ранение на урон 89 жизней
print(Vasya.get_name(),Vasya.get_status(), Vasya.get_health(), Vasya.get_velocity(), Vasya.get_hunger_level())

class Gun:
    # конструктор класса Gun
    def __init__(self,user_name, user_type, user_distance, user_damage, user_rate_fire, user_number_bullet):
        self.__name = user_name  # название оружия
        self.__type = user_type  # тип оружия
        self.__distance = user_distance  # дистанция поражения
        self.__damage = user_damage  # урон от оружия
        self.__rate_fire = user_rate_fire  # скорострельность
        self.__cur_number_bullet = user_number_bullet  # текущее количетво патронов
        self.__full_number_bullet = user_number_bullet  # полное количетво патронов
        self.__temp = 20  # температура оружия

    # добавление геттеров для приватных полей
    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_distance(self):
        return self.__distance

    def get_damage(self):
        return self.__damage

    def get_rate_fire(self):
        return self.__rate_fire

    def get_number_bullet(self):
        return self.__cur_number_bullet

    def get_temp(self):
        return self.__temp

    # метод перезарядки оружия
    def recharge(self):
        self.__cur_number_bullet = self.__full_number_bullet

    # метод стрельбы оружия
    def shoot(self, time_shoot):
        # уменьшение патронов в зависимости от времени стрельбы и темпа стрельбы
        self.__cur_number_bullet -= time_shoot * self.__rate_fire
        self.__temp += 1  # увеличение температуры
        if self.__cur_number_bullet <= 0:  # если кончились патроны, то перезарядка
            self.recharge()
        if self.__temp >= 25:  # если оружие нагрелось до 25 градусов, то его перегрев
            self.heat()

    # метод оружия при перегреве
    def heat(self):
        self.__damage /= 2
        self.__rate_fire /= 2
        self.__distance /= 2

P = Gun("Пистолет","Среднего боя", 50, 5, 1,30)
P.shoot(3)
P.shoot(5)
print( P.get_number_bullet())


