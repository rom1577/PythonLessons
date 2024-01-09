
class Animal:  # Класс описывает поля животных, которые дают молоко
    def __init__(self, user_name, user_size, user_velocity, user_weight):
        self.name = user_name  # вид животного
        self.size = user_size  # размер животного
        self.stress_level = 10  # уровень стресса животного по умолчанию
        self.velocity = user_velocity  # скорость животного
        self.weight = user_weight  # вес животного

    # метод оперделяет скорость животного, если она стоит
    def stop(self):
        self.velocity = 0

    # метод оперделяет поведение животного во сне
    def sleep(self):
        self.stress_level = 10  # сброс уровня стресса
        self.stop()  # скорость равно нулю

    # метод поведения животного при еде
    def eating(self, grass):
        self.stress_level -= 1  # уменьшение уровня стерсса
        self.weight += grass  # увеличение веса

    # метод поведения животного при дойке
    def milking(self):
        self.stress_level += 10  # увеличение уровня стресса
        if self.stress_level >= 20:  # если уровень стресса првеышает 30, то животное не выдерживает и засыпает
            self.sleep()

    # метод увеличения размера животного (при взрослении)
    def exchange_size(self):
        self.size *= 2

# Создание объекта класса Animal для животного "Корова"
Cow = Animal("Корова", 150, 2, 100)
print(Cow.name, Cow.size, Cow.stress_level, Cow.velocity, Cow.weight)
Cow.milking()  # дойка 2 раза
Cow.milking()
print(Cow.name, Cow.size, Cow.stress_level, Cow.velocity, Cow.weight)
Cow.eating(20)  # поедание травы на 20 у.е.
print(Cow.name, Cow.size, Cow.stress_level, Cow.velocity, Cow.weight)
Cow.exchange_size()  # увеличение в размере
print(Cow.name, Cow.size, Cow.stress_level, Cow.velocity, Cow.weight)

# Создание объекта класса Animal для животного "Лама"
Lama = Animal("Лама", 75, 5, 80)
print(Lama.name, Lama.size, Lama.stress_level, Lama.velocity, Lama.weight)
Lama.sleep()  # сон ламы
print(Lama.name, Lama.size, Lama.stress_level, Lama.velocity, Lama.weight)
Lama.eating(10)  # поедание травы на 10 у.е.
print(Lama.name, Lama.size, Lama.stress_level, Lama.velocity, Lama.weight)

class Guy:
    # рассматривается класс Guy, в котором описано поведение игрока шутера
    def __init__(self, name_user, user_status, user_health, user_velocity, user_hunger):
        self.name = name_user  # имя пользователя
        self.status = user_status  # статус игрока
        self.health = user_health  # уровень здоровья
        self.velocity = user_velocity  # скорость бега
        self.hunger_level = user_hunger  # уровень голода

    # метод получения ранения. Задается получаемый урон, который вычитается из уровня здоровья. Изменяется статус игрока
    def injury(self, damage):
        self.health -= damage
        self.user_status = "injured"
        if self.health <= 0:
            self.status = "dead"

    # метод использования аптечки. Увеличивается уровень здоровья при использовании аптечки
    def medicine_kit(self, kit_effect):
        self.health += kit_effect

    # метод остановки игорока. При остановке скорость игрока равна нулю
    def stop(self):
        self.velocity = 0

    # метод поедания еды. Игрок останавливается, увеличивает своё здоровье и уровень голода
    def eating(self):
        self.stop()
        self.health += 0.5
        self.hunger_level += 5

    # метод бега. Задается скорость бега. Уменьшается уровень голода
    def run(self, speed):
        self.velocity = speed
        self.hunger_level -= 1
        if self.hunger_level <= 0:
            self.stop()

# Создание объектов, вызов методов из класса Guy и демонстрация того, как меняются поля объекта (класса)
Roma = Guy("Roma", "normal", 100, 5, 10)
print( Roma.status, Roma.health, Roma.velocity, Roma.hunger_level)
Roma.injury(89)  # ранение на урон 89 жизней
print( Roma.status, Roma.health, Roma.velocity, Roma.hunger_level)
Roma.medicine_kit(8)  # восстановление аптечкой 8 жизней
print( Roma.status, Roma.health, Roma.velocity, Roma.hunger_level)
Roma.eating()  # перерыв на еду
print( Roma.status, Roma.health, Roma.velocity, Roma.hunger_level)
Roma.run(10)  # бег со скоростью 10
print( Roma.status, Roma.health, Roma.velocity, Roma.hunger_level)

Vasya = Guy("Vasya", "normal", 70, 10, 4)
print( Vasya.status, Vasya.health, Vasya.velocity, Vasya.hunger_level)
Vasya.injury(71) # ранение на урон 89 жизней
print( Vasya.status, Vasya.health, Vasya.velocity, Vasya.hunger_level)
