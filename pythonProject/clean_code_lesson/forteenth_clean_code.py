# №1
# вариант без комментариев
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__odometer_reading = 0
        self.__fuel_level_L = 0

    def drive(self, distance_km):
        fuel_consumption_rate_kgs = 0.1
        if self.__fuel_level_L <= 0:
            print("Бак пуст")
        else:
            self.__odometer_reading += distance_km
            self.__fuel_level_L -= distance_km * fuel_consumption_rate_kgs
            if self.__fuel_level_L < 0:
                self.__fuel_level_L = 0
            print(f"Проехали {distance_km} км")

# вариант с комментариями
class Car:
    def __init__(self, make, model, year):
        self.__make = make  # производитель
        self.__model = model  # модель
        self.__year = year  # год выпуска
        self.__odometer_reading = 0  # показания адоментра
        self.__fuel_level_L = 0  # текущий уровень топлива

    # метод вождения автомобиля
    def drive(self, distance_km):
        fuel_consumption_rate_kgs = 0.1  # расход топлива
        # если уровень топлива меньше нуля
        if self.__fuel_level_L <= 0:
            print("Бак пуст")
        else:
            self.__odometer_reading += distance_km
            self.__fuel_level_L -= distance_km * fuel_consumption_rate_kgs
            if self.__fuel_level_L < 0:
                self.__fuel_level_L = 0
            print(f"Проехали {distance_km} км")

# вставил комментарии к методам и полям класса


# №2
# вариант без комментариев

class Airplane:
    def __init__(self, model, capacity, fuel_level_kg):
        self.model = model
        self.capacity = capacity
        self.current_passengers = 0
        self.is_flying = False
        self.fuel_level_L = fuel_level_kg

    def board_passengers(self, number_of_passengers):
        if self.current_passengers + number_of_passengers <= self.capacity:
            self.current_passengers += number_of_passengers
            print(f"Посажено {number_of_passengers} пассажиров. Всего пассажиров: {self.current_passengers}")
        else:
            print("Недостаточно места для всех пассажиров.")

    def take_off(self):
        if self.fuel_level_kg > 0 and self.current_passengers > 0:
            self.is_flying = True
            print(f"Самолёт {self.model} взлетел.")
        else:
            print("Не хватает топлива или нет пассажиров для взлёта.")


# вариант с комментариями
class Airplane:
    def __init__(self, model, capacity, fuel_level_kg):
        self.model = model  # Модель самолёта
        self.capacity = capacity  # Вместимость самолёта
        self.current_passengers = 0  # Текущее количество пассажиров
        self.is_flying = False  # Состояние самолёта (в полёте или нет)
        self.fuel_level_L = fuel_level_kg  # Уровень топлива

    # посадка пассажирова в самолёт
    def board_passengers(self, number_of_passengers):
        # проверить, количество вошедших в самолёт пассажиров не первышает количество посадочных мест
        if self.current_passengers + number_of_passengers <= self.capacity:
            self.current_passengers += number_of_passengers
            print(f"Посажено {number_of_passengers} пассажиров. Всего пассажиров: {self.current_passengers}")
        else:
            print("Недостаточно места для всех пассажиров.")

    # взлёт самолёта
    def take_off(self):
        # проверить возможность взлёта самолёта
        if self.fuel_level_kg > 0 and self.current_passengers > 0:
            self.is_flying = True
            print(f"Самолёт {self.model} взлетел.")
        else:
            print("Не хватает топлива или нет пассажиров для взлёта.")

# вставил комментарии к методам и полям класса


# №3
# вариант без комментариев

class Marker:
    def __init__(self, color, ink_level=100):
        self.__color = color
        self.__ink_level = ink_level
        self.__is_open = False

    def write(self, text):
        if not self.__is_open:
            print("Маркер закрыт! Сначала откройте маркер.")
            return

        if self.__ink_level <= 0:
            print("Чернила закончились! Невозможно писать.")
            return

        print(f"Пишем '{text}' цветом {self.__color}")

        ink_used = len(text) * 0.5
        self.__ink_level -= ink_used

        if self.__ink_level < 0:
            self.__ink_level = 0
        print(f"Остаток чернил: {self.__ink_level:.2f}%")

    def open_close(self):
        self.__is_open = not self.__is_open
        state = "открыт" if self.__is_open else "закрыт"
        print(f"Маркер теперь {state}.")


# пример с комментариями
class Marker:
    def __init__(self, color, ink_level=100):
        self.__color = color  # Цвет маркера
        self.__ink_level = ink_level  # Уровень чернил (по умолчанию 100)
        self.__is_open = False  # Состояние маркера (открыт или закрыт)

    # писать маркером
    def write(self, text):
        # проверить, закрыт ли маркер
        if not self.__is_open:
            print("Маркер закрыт! Сначала откройте маркер.")
            return

        # проверить, закончились ли чернила
        if self.__ink_level <= 0:
            print("Чернила закончились! Невозможно писать.")
            return

        print(f"Пишем '{text}' цветом {self.__color}")

        ink_used = len(text) * 0.5  # Уменьшение уровня чернил в зависимости от длины текста
        self.__ink_level -= ink_used

        # проверить, закончились ли чернила
        if self.__ink_level < 0:
            self.__ink_level = 0
        print(f"Остаток чернил: {self.__ink_level:.2f}%")

    # закрыть или открыть маркер
    def open_close(self):
        self.__is_open = not self.__is_open
        state = "открыт" if self.__is_open else "закрыт"
        print(f"Маркер теперь {state}.")

# вставил комментарии к методам и полям класса


# №4
# вариант без комментариев
class Kettle:
    def __init__(self, brand, color, capacity):
        self.brand = brand
        self.color = color
        self.capacity_L = capacity
        self.current_water_level_L = 0.0
        self.is_on = False

    def boil_water(self):
        if not self.is_on:
            print("Чайник выключен!")
            return

        if self.current_water_level_L <= 0:
            print("Нет воды!")
            return

        time_to_boil_s = self.current_water_level_L * 4
        print(f"Вода вскипела! Время займет {time_to_boil_s}")

    def toggle_power(self):
        self.is_on = not self.is_on
        state = "включен" if self.is_on else "выключен"
        print(f"Чайник теперь {state}.")


# вариант с комментариями
class Kettle:
    def __init__(self, brand, color, capacity):
        self.brand = brand  # Бренд
        self.color = color  # Цвет
        self.capacity_L = capacity  # Емкость чайника в литрах
        self.current_water_level_L = 0.0  # Текущий уровень воды в литрах
        self.is_on = False  # Состояние чайника (включен или выключен)

    # Кипятить воду в чайнике
    def boil_water(self):
        # проверить, выключен ли чайник
        if not self.is_on:
            print("Чайник выключен!")
            return

        # проверить, осталась ли вода в чайнике
        if self.current_water_level_L <= 0:
            print("Нет воды!")
            return

        time_to_boil_s = self.current_water_level_L * 4  # Рассчитывается время кипячения
        print(f"Вода вскипела! Время займет {time_to_boil_s}")

    # Включение или выключение чайника
    def toggle_power(self):
        self.is_on = not self.is_on
        state = "включен" if self.is_on else "выключен"
        print(f"Чайник теперь {state}.")

# вставил комментарии к методам и полям класса



# №5
# вариант без комментариев
def calculate_pension(current_age, retirement_age, current_income, contribution_percent, current_savings_usd):
    total_savings_usd = current_savings_usd
    years_until_retirement = retirement_age - current_age
    if years_until_retirement <= 0:
        return "Вы уже на пенсии"

    annual_contribution = current_income * (contribution_percent / 100)
    for year in range(years_until_retirement):
        total_savings_usd += annual_contribution
        total_savings_usd *= 1.05

    return total_savings_usd


# вариант с комментариями

# расчитать пенсионные накопления гражданина
def calculate_pension(current_age, retirement_age, current_income, contribution_percent, current_savings_usd):
    total_savings_usd = current_savings_usd  # полные накопления

    years_until_retirement = retirement_age - current_age  # количество лет до отставки

    # проверить, на пенсии ли гражданин
    if years_until_retirement <= 0:
        return "Вы уже на пенсии"

    annual_contribution = current_income * (contribution_percent / 100)  # ежегодный взнос в ПФР

    for year in range(years_until_retirement):
        total_savings_usd += annual_contribution
        total_savings_usd *= 1.05

    return total_savings_usd

# вставил комментарии к переменным и условиям функции



# №6
# вариант без комментариев
class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages
        self.__current_page = 0

    def get_details(self):
        return f"Название: {self.__title}, Автор: {self.__author}, Всего страниц: {self.__pages}"

    def read_pages(self, pages):
        if self.__current_page + pages > self.__pages:
            pages_to_read = self.__pages - self.__current_page
            self.__current_page = self.__pages
            return f"Вы прочитали последние {pages_to_read} страниц и закончили книгу."
        else:
            self.__current_page += pages
            return f"Вы прочитали {pages} страниц. Текущая страница: {self.__current_page}"

# вариант с комментариями
class Book:
    def __init__(self, title, author, pages):
        self.__title = title  # Название
        self.__author = author  # Автор
        self.__pages = pages  # Количество страниц
        self.__current_page = 0  # Текущая страница

    # Получить информация о книге
    def get_details(self):
        return f"Название: {self.__title}, Автор: {self.__author}, Всего страниц: {self.__pages}"

    # Читать оперделенное количество страниц книги
    def read_pages(self, pages):
        # проверить, что читаемая страница не больше всех страниц
        if self.__current_page + pages > self.__pages:
            pages_to_read = self.__pages - self.__current_page
            self.__current_page = self.__pages
            return f"Вы прочитали последние {pages_to_read} страниц и закончили книгу."
        else:
            self.__current_page += pages
            return f"Вы прочитали {pages} страниц. Текущая страница: {self.__current_page}"

# вставил комментарии к методам и полям класса


# №7
# вариант без комментариев
class Fan:
    def __init__(self, brand, speed_levels):
        self.__brand = brand
        self.__speed_levels = speed_levels
        self.__current_speed_ms = 0
        self.__is_on = False

    def toggle_power(self):
        self.__is_on = not self.__is_on

        if self.__is_on:
            self.__current_speed_ms = 1
            state = "включен"
        else:
            self.__current_speed_ms = 0
            state = "выключен"
        return f"Вентилятор {self.__brand} теперь {state}, текущая скорость: {self.__current_speed_ms}"


# вариант с комментариями
class Fan:
    def __init__(self, brand, speed_levels):
        self.__brand = brand  # Бренд вентилятора
        self.__speed_levels = speed_levels  # Количество скоростей
        self.__current_speed_ms = 0  # Текущая скорость
        self.__is_on = False  # включен или выключен

    # Включить или выключить вентилятор
    def toggle_power(self):
        self.__is_on = not self.__is_on

        # Проверить, включен ли вентилятор и поределить состояние
        if self.__is_on:
            self.__current_speed_ms = 1  # Скорость при вкючённом вентиляторе
            state = "включен"
        else:
            self.__current_speed_ms = 0  # Скорость при выключении вентилятора
            state = "выключен"
        return f"Вентилятор {self.__brand} теперь {state}, текущая скорость: {self.__current_speed_ms}"

# вставил комментарии к методам и полям класса



# №8
# неверный вариант

import random

# Расчитать количество повторяющихся значений в списке
def func2(val, N):
    array_out = []  # Выходной список
    dictionary = {}  # Словарь для поиска повторяющихся значений
    for value in val:
        if value in dictionary:
            dictionary[value] += 1
        else:
            dictionary[value] = 1

        if dictionary[value] == N:
            array_out.append(value)
    return array_out

# верный вариант

import random

def find_repeated_val(input_list_100_elem, N):
    repeated_val_list = []
    freq_dict_1_to_10 = {}
    for value in input_list_100_elem:
        if value in freq_dict_1_to_10:
            freq_dict_1_to_10[value] += 1
        else:
            freq_dict_1_to_10[value] = 1

        if freq_dict_1_to_10[value] == N:
            repeated_val_list.append(value)
    return repeated_val_list

# Переименовал метод и переменные внутри него, сделав код более читаемым и избавившись от излишних комментариев


# №9
# неверный вариант
import math
C0 = 5.67  # Константа Больцмана
T = 3000  # Температура в камере сгорния
d_bl = 0.9  # Степень черноты
Dk = 0.1  # Диаметр камеры сгорания
Lc = 0.1  # Длина цилиндрической части

V = math.pi * Dk **2 / 4 * Lc  # Объём излучаемого газа
A = math.pi * Dk * Lc  # Площадь поверхности стенки, окружающ газ
ef_L = 3.6 * V / A  # Эффективная длина излучаемого газового слоя

r_f = d_bl*C0*(T/100)**4  # Излучаемый тепловой поток


# верный вариант
import math
constant_of_Boltzman = 5.67
temper_of_chamber_K = 3000
degree_of_blackness = 0.9
chamber_diameter_m = 0.1
length_cylinder_part_m = 0.1

radiant_gas_volume_m3 = math.pi * chamber_diameter_m **2 / 4 * length_cylinder_part_m
wall_area_m2 = math.pi * chamber_diameter_m * length_cylinder_part_m
effect_radiant_length_m = 3.6 * radiant_gas_volume_m3 / wall_area_m2

radiant_flux_W = degree_of_blackness*constant_of_Boltzman*(temper_of_chamber_K/100)**4

# Переименовал переменные, сделав код более читаемым, из-за чего смог убрать комментарии


# №10
# неверный вариант
from abc import ABC, abstractmethod

# Класс шахматная фигура
class Ch(ABC):
    # перемещение по клеткам
    @abstractmethod
    def st(self, x, y):
        pass

    # убийство name фигуры
    @abstractmethod
    def kl(self, name):
        pass


# Класс короля
class K(Ch):
    def __init__(self, x, y):
        self.x = x  # координата Х
        self.y = y  # координата e

    def st(self, new_x, new_y):
        self.new_x += new_x  # новое положение по Х
        self.new_y += new_y  # новое положение по У

    def kl(self, name):
        print("The king killed ", name)

# верный вариант
from abc import ABC, abstractmethod


class Chess_piece(ABC):
    @abstractmethod
    def make_step(self, x_coordinate, y_coordinate):
        pass

    @abstractmethod
    def kill_chess_piece(self, name_of_killed_piece):
        pass


class Chess_piece_king(Chess_piece):
    def __init__(self, king_position_x, king_position_y):
        self.king_position_x = king_position_x
        self.king_position_y = king_position_y

    def make_step(self, new_x_position, new_y_position):
        self.king_position_x += new_x_position
        self.king_position_y += new_y_position

    def kill_chess_piece(self, name_of_killed_piece):
        print("The king killed ", name_of_killed_piece)

#  Переименовал методы абстрактного класса и класса, который его реализует. Также переименовал
#  названия самих классов и внутренние атрибуты. Убрал лишние комментарии


# №11
# неверный вариант
from abc import ABC, abstractmethod

# Класс Фигуры
class Sh(ABC):
    # метод расчёта площади
    @abstractmethod
    def func_A(self):
        pass

    # метод расчета периметра
    @abstractmethod
    def func_p(self):
        pass


# Класс прямоугольник
class R(Sh):
    def __init__(self, w, h):
        self.w = w  # Ширина
        self.h = h  # Высота

    def func_A(self):
        return self.w * self.h

    def func_p(self):
        return 2 * (self.w + self.h)

# верный вариант
from abc import ABC, abstractmethod


class Shape_factory(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimetr(self):
        pass


class Rectangle(Shape_factory):
    def __init__(self, width_of_figure, height_of_figure):
        self.width_of_figure = width_of_figure
        self.height_of_figure = height_of_figure

    def calculate_area(self):
        return self.width_of_figure * self.height_of_figure

    def calculate_perimetr(self):
        return 2 * (self.width_of_figure + self.height_of_figure)

#  Переименовал методы абстрактного класса и класса, который его реализует. Также переименовал
#  названия самих классов и внутренние атрибуты. Убрал лишние комментарии


# №12
# неверный вариант
V = 0  # Начальная скорость
a = 2  # Начальное ускорение
t = 5  # Время

d = V * t + 0.5 * a * t ** 2  # пройденное расстояние
av_V = d / t  # средняя скорость
f_p = V * t + 0.5 * a * t ** 2  # финальное положение
f_V = V + a * t  # конечная скорость


# верный вариант

initial_speed_ms = 0
acceleration_ms2 = 2
time_s = 5

distance = initial_speed_ms * time_s + 0.5 * acceleration_ms2 * time_s ** 2
average_speed = distance / time_s
final_position = initial_speed_ms * time_s + 0.5 * acceleration_ms2 * time_s ** 2
final_speed = initial_speed_ms + acceleration_ms2 * time_s

# Переименовал переменные и убрал комментарии, повысив читаемость кода

