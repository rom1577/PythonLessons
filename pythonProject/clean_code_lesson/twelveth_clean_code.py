# №1

class Airplane:
    def __init__(self, model, capacity, fuel_level_kg):
        self.model = model  # Модель самолёта
        self.capacity = capacity  # Вместимость самолёта
        self.current_passengers = 0  # Текущее количество пассажиров
        self.is_flying = False  # Состояние самолёта (в полёте или нет)
        self.fuel_level_L = fuel_level_kg  # Уровень топлива

    def board_passengers(self, number_of_passengers):
        #  Посадка пассажиров на самолёт
        if self.current_passengers + number_of_passengers <= self.capacity:
            self.current_passengers += number_of_passengers
            print(f"Посажено {number_of_passengers} пассажиров. Всего пассажиров: {self.current_passengers}")
        else:
            print("Недостаточно места для всех пассажиров.")

    def take_off(self):
        #  Взлёт самолёта
        if self.fuel_level_kg > 0 and self.current_passengers > 0:
            self.is_flying = True
            print(f"Самолёт {self.model} взлетел.")
        else:
            print("Не хватает топлива или нет пассажиров для взлёта.")

    def fly(self, distance):
        #  Полёт самолёта
        if not self.is_flying:
            print("Самолёт не в полёте.")
            return

        fuel_consumption_per_km = 0.1  # Потребление топлива на км
        traveled_distance_km = 0

        for km in range(distance):
            if self.fuel_level_kg <= 0:
                print("Топливо закончилось")
                self.is_flying = False
                break
            self.fuel_level_kg -= fuel_consumption_per_km
            traveled_distance_km += 1
            print(f"Полетел {traveled_distance_km} км")

        if self.fuel_level_kg > 0:
            print(f"Самолёт пролетел {traveled_distance_km} км")
            self.is_flying = False

SSJ_100 = Airplane('SSJ-100', 98, 8000)

# Использовал связывание во время написания кода при определении атрибутов экземпляра класса.
# Предполагается, что эти значения будут использованы только в этой
# части программы и не будут меняться во время выполнения программы.



# №2
PASSENGER_CAPACITY_SSJ_100 = 98
FUEL_LEVEL_SSJ_100 = 8000

class Airplane:
    def __init__(self, model, capacity, fuel_level_kg):
        self.model = model  # Модель самолёта
        self.capacity = capacity  # Вместимость самолёта
        self.current_passengers = 0  # Текущее количество пассажиров
        self.is_flying = False  # Состояние самолёта (в полёте или нет)
        self.fuel_level_L = fuel_level_kg  # Уровень топлива

    def board_passengers(self, number_of_passengers):
        #  Посадка пассажиров на самолёт
        if self.current_passengers + number_of_passengers <= self.capacity:
            self.current_passengers += number_of_passengers
            print(f"Посажено {number_of_passengers} пассажиров. Всего пассажиров: {self.current_passengers}")
        else:
            print("Недостаточно места для всех пассажиров.")

    def take_off(self):
        #  Взлёт самолёта
        if self.fuel_level_kg > 0 and self.current_passengers > 0:
            self.is_flying = True
            print(f"Самолёт {self.model} взлетел.")
        else:
            print("Не хватает топлива или нет пассажиров для взлёта.")

    def fly(self, distance):
        #  Полёт самолёта
        if not self.is_flying:
            print("Самолёт не в полёте.")
            return

        fuel_consumption_per_km = 0.1  # Потребление топлива на км
        traveled_distance_km = 0

        for km in range(distance):
            if self.fuel_level_kg <= 0:
                print("Топливо закончилось")
                self.is_flying = False
                break
            self.fuel_level_kg -= fuel_consumption_per_km
            traveled_distance_km += 1
            print(f"Полетел {traveled_distance_km} км")

        if self.fuel_level_kg > 0:
            print(f"Самолёт пролетел {traveled_distance_km} км")
            self.is_flying = False

SSJ_100 = Airplane('SSJ-100', PASSENGER_CAPACITY_SSJ_100, FUEL_LEVEL_SSJ_100)

# связывание во время компиляции (термин не совсем для питона, конечно), если нужно в дальнейшем по коду
# использовать константы PASSENGER_CAPACITY_SSJ_100, FUEL_LEVEL_SSJ_100 в нескольких местах программы.
# При этом параметры могут быть изменены разработчиками и остаются постоянными во время выполнения программы.

# №3
SSJ_100_INIT_DATA_PATH = 'C:/...'

def read_pas_capacity(path_init_data):
    # чтение с файла кол-во пассажиров
    with open(path_init_data, 'r') as file:
        passenger_capacity = int(file.read().strip())
    return passenger_capacity

def read_fuel_level(path_init_data):
    # считывание с файла уровень топлива
    with open(path_init_data, 'r') as file:
        fuel_level = int(file.read().strip())
    return fuel_level

class Airplane:
    def __init__(self, model, capacity, fuel_level_kg):
        self.model = model  # Модель самолёта
        self.capacity = capacity  # Вместимость самолёта
        self.current_passengers = 0  # Текущее количество пассажиров
        self.is_flying = False  # Состояние самолёта (в полёте или нет)
        self.fuel_level_L = fuel_level_kg  # Уровень топлива

    def board_passengers(self, number_of_passengers):
        #  Посадка пассажиров на самолёт
        if self.current_passengers + number_of_passengers <= self.capacity:
            self.current_passengers += number_of_passengers
            print(f"Посажено {number_of_passengers} пассажиров. Всего пассажиров: {self.current_passengers}")
        else:
            print("Недостаточно места для всех пассажиров.")

    def take_off(self):
        #  Взлёт самолёта
        if self.fuel_level_kg > 0 and self.current_passengers > 0:
            self.is_flying = True
            print(f"Самолёт {self.model} взлетел.")
        else:
            print("Не хватает топлива или нет пассажиров для взлёта.")

    def fly(self, distance):
        #  Полёт самолёта
        if not self.is_flying:
            print("Самолёт не в полёте.")
            return

        fuel_consumption_per_km = 0.1  # Потребление топлива на км
        traveled_distance_km = 0

        for km in range(distance):
            if self.fuel_level_kg <= 0:
                print("Топливо закончилось")
                self.is_flying = False
                break
            self.fuel_level_kg -= fuel_consumption_per_km
            traveled_distance_km += 1
            print(f"Полетел {traveled_distance_km} км")

        if self.fuel_level_kg > 0:
            print(f"Самолёт пролетел {traveled_distance_km} км")
            self.is_flying = False

SSJ_100 = Airplane('SSJ-100', read_pas_capacity(SSJ_100_INIT_DATA_PATH), read_fuel_level(SSJ_100_INIT_DATA_PATH))

# Использовал связывание во время выполнения с помощью считыавания параметров с файла.
# Предположим, что данные параметры могут меняться по мере
# выполнения программы и поступают из сети или из датчиков в реальном времени.

