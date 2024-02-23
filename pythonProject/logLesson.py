import logging  # импорт библиотеки логирования

class Dwarf:
    # класс Dwarf, в котором описано поведение Дварфов
    def __init__(self, user_name, user_status, user_health, user_velocity, user_hunger):
        self.__name = user_name  # имя пользователя
        # статус игрока. "0" - good; "1" - injured; "2" - dead
        self.__status = user_status
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
        self.__status = 1
        if self.__health <= 0:
            self.__health = 0
            self.__status = 2
        assert (self.__health >= 0 and self.__health <= 100)  # проверка адекватности уровня здоровья
        logging.debug('Вызов метода: ')  # использование логирования

    # метод использования аптечки. Увеличивается уровень здоровья при использовании аптечки
    def medicine_kit(self, kit_effect):
        self.__health += kit_effect
        logging.debug('Вызов метода: ')
        if self.__health > 100:
            logging.warning("Warning! Переменная health имеет неадекватное значение")
            self.__health = 100
        assert (self.__health >= 0 and self.__health <= 100) # проверка адекватности уровня здоровья

    # метод остановки игорока. При остановке скорость игрока равна нулю
    def stop(self):
        self.__velocity = 0
        logging.debug('Вызов метода: ')  # использование логирования

    # метод поедания еды. Игрок останавливается, увеличивает своё здоровье и уровень голода
    def eating(self):
        self.stop()
        self.__health += 0.5
        self.__hunger_level += 5
        if self.__hunger_level > 10:
            self.__hunger_level = 10
        if self.__health > 100:
            logging.warning("Warning! Переменная health имеет неадекватное значение")
            self.__health = 100
        assert(self.__hunger_level <= 10 and self.__hunger_level >= 0)  # проверка адекватности шкалы голода
        assert(self.__health >= 0 and self.__health <= 100)  # проверка адекватности уровня здоровья и скорости
        logging.debug('Вызов метода: ')  # использование логирования

    # метод бега. Задается скорость бега. Уменьшается уровень голода
    def run(self, speed):
        self.__velocity = speed
        self.__hunger_level -= 1
        if self.__hunger_level <= 0:
            self.__hunger_level =0
            self.stop()
        assert(self.__velocity < 50)  # проверка адекватности скорости
        assert(self.__hunger_level <= 10 and self.__hunger_level >= 0)  # проверка адекватности шкалы голода
        logging.debug('Вызов метода: ')  # использование логирования

# составляется конфигурация логера и обработчика.
# задается уровень важности DEBUG, то, что местом для вывода логов будет файл и используемый формат вывода
logging.basicConfig(level = 10, filename = 'Logi.log', format='%(asctime)s - %(name)s - %(message)s - %(funcName)s ')

# работа с экземпляром класса Dwarf
dw = Dwarf("Коля", 0, 49, 0, 8)
dw.run(5)
dw.injury(10)
dw.stop()
dw.eating()
dw.injury(20)
dw.medicine_kit(200)  # здесь программа обрабатывает исключение, т.к. не пройдет проверку assert()




