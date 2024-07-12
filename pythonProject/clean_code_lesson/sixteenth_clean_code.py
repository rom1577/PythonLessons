# №1
# вариант до
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__odometer_reading = 0
        self.__fuel_level_L = 0

    # для того, чтобы автомобиль ездил необходим соответствующий метод
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

# вариант после
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__odometer_reading = 0
        self.__fuel_level_L = 0

    # метод вождения автомобиля с увеличением показаний одоментра и уменьшением уровня топлива
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

# согласно с п.1 переделал неочевидный комментарий к методу drive()


# №2
# вариант до
class Airplane:
    def __init__(self, model, capacity, fuel_level_kg):
        self.model = model  # модель
        self.capacity = capacity  # емкость
        self.current_passengers = 0  # текущие пассажиры
        self.is_flying = False  # флаг
        self.fuel_level_L = fuel_level_kg  # уровень топлива

    # посадка
    def board_passengers(self, number_of_passengers):
        if self.current_passengers + number_of_passengers <= self.capacity:
            self.current_passengers += number_of_passengers
            print(f"Посажено {number_of_passengers} пассажиров. Всего пассажиров: {self.current_passengers}")
        else:
            print("Недостаточно места для всех пассажиров.")

    # взлёт
    def take_off(self):
        if self.fuel_level_kg > 0 and self.current_passengers > 0:
            self.is_flying = True
            print(f"Самолёт {self.model} взлетел.")
        else:
            print("Не хватает топлива или нет пассажиров для взлёта.")

# вариант после
class Airplane:
    def __init__(self, model, capacity, fuel_level_kg):
        self.model = model  # модель самолета
        self.capacity = capacity  # сколько пассажиров может вместить самолёт
        self.current_passengers = 0  # текущее количество пассажиров в самолёте
        self.is_flying = False  # флаг летит ли самолёт в данный момент
        self.fuel_level_L = fuel_level_kg  # уровень топлива в баке самолёта

    # посадка пассажиров в самолёт
    def board_passengers(self, number_of_passengers):
        # проверить количество вошедших пассажиров в самолет на превышение посадочных мест
        if self.current_passengers + number_of_passengers <= self.capacity:
            self.current_passengers += number_of_passengers
            print(f"Посажено {number_of_passengers} пассажиров. Всего пассажиров: {self.current_passengers}")
        else:
            print("Недостаточно места для всех пассажиров.")

    # взлёт самолёта
    def take_off(self):
        # проверка возможности взлёта самолёта и установка флага
        if self.fuel_level_kg > 0 and self.current_passengers > 0:
            self.is_flying = True
            print(f"Самолёт {self.model} взлетел.")
        else:
            print("Не хватает топлива или нет пассажиров для взлёта.")

# согласно п.2 написал хорошие комментарии заместо комментариев "на скорую руку"


# №3
# вариант до
import pandas as pd

# Собираемся уменьшить размерность данных
data = pd.read_csv('dataset.csv')
X = data.drop(columns=['target'])
y = data['target']


# вариант после
import pandas as pd

# Загружаем данные и собираемся разделить их на признаки и целевые значения
data = pd.read_csv('dataset.csv')
X = data.drop(columns=['target'])
y = data['target']

# согласно п.3 исправил явно ложный комментарий


# №4
# вариант до
initial_speed = 0  # присвоение значения начальной скорости
acceleration = 2  # присвоение значения ускорению
time = 5  # присвоение значения времени

distance = initial_speed * time + 0.5 * acceleration * time ** 2
average_speed = distance / time
final_position = initial_speed * time + 0.5 * acceleration * time ** 2
final_speed = initial_speed + acceleration * time

# вариант после

# инициализация входных данных
initial_speed = 0
acceleration = 2
time = 5

distance = initial_speed * time + 0.5 * acceleration * time ** 2
average_speed = distance / time
final_position = initial_speed * time + 0.5 * acceleration * time ** 2
final_speed = initial_speed + acceleration * time

# согласно п.4 заменил неинформативные комментарии инициализации значений переменных


# №5
# вариант до
from queue import Queue
############################
'''
Создаем очередь из списка
'''
my_list = [10, 5, 20, 20, 4, 8, 15]
my_queue = Queue()
my_queue.put(my_list)
max_value = my_queue.get()

##############################
'''
Создаем вторую очередь
'''
my_queue2 = Queue()
my_queue2.put(max_value)  # Сохраняем извлеченный элемент во временную очередь

##############################
'''
Поиск максимального значения
'''
while not my_queue.empty():
    current = my_queue.get()  # Извлекаем текущий элемент из очереди
    if current > max_value:
        max_value = current  # Обновляем максимум, если находим большее значение
    my_queue2.put(current)  # Сохраняем текущий элемент во временную очередь

#############################
'''
Заполнение исходной очереди
'''
while not my_queue2.empty():
    my_queue.put(my_queue2.get())


# вариант после
from queue import Queue

my_list = [10, 5, 20, 20, 4, 8, 15]
my_queue = Queue()  # Создаем очередь
my_queue.put(my_list)
max_value = my_queue.get()  # Извлекаем первый элемент и считаем его максимальным

my_queue2 = Queue()
my_queue2.put(max_value)  # Сохраняем извлеченный элемент во временную очередь

'''
Поиск максимального значения
'''
while not my_queue.empty():
    current = my_queue.get()  # Извлекаем текущий элемент из очереди
    if current > max_value:
        max_value = current  # Обновляем максимум, если находим большее значение
    my_queue2.put(current)  # Сохраняем текущий элемент во временную очередь

# Возвращаем все элементы обратно в исходную очередь
while not my_queue2.empty():
    my_queue.put(my_queue2.get())

# согласно п.5 уменьшил количество заголовков, чтобы остались только необходимые


# №6
# вариант до
def func(num1, num2):
    '''
    Эта функция расчитывает сложение двух чисел.
    Два числа определены в переменных num1 num2.
    Результат хранится в переменной sum.
    '''
    # Сложение двух чисел
    sum = num1 + num2
    # Возвращение результата
    return sum

# вариант после
def add_two_numbers(first_number_for_add, second_number_for_add):
    adding_mumber = first_number_for_add + second_number_for_add
    return adding_mumber

# согласно п.7 удалил избыточные комментарии и излишенее описание функции, сделав код более читабельным


# №7
# вариант до
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

    # взлёт самолёта
    # в наше время самолёт сам должен взлетать!
    def take_off(self):
        # проверка возможности взлёта самолёта и установка флага
        # почему самолёт на топливе до сих пор летает, а не на электричестве?
        if self.fuel_level_kg > 0 and self.current_passengers > 0:
            self.is_flying = True
            print(f"Самолёт {self.model} взлетел.")
        else:
            print("Не хватает топлива или нет пассажиров для взлёта.")

# вариант после
class Airplane:
    def __init__(self, model, capacity, fuel_level_kg):
        self.model = model  # модель самолета
        self.capacity = capacity  # сколько пассажиров может вместить самолёт
        self.current_passengers = 0  # текущее количество пассажиров в самолёте
        self.is_flying = False  # флаг летит ли самолёт в данный момент
        self.fuel_level_L = fuel_level_kg  # уровень топлива в баке самолёта

    # посадка пассажиров в самолёт
    def board_passengers(self, number_of_passengers):
        # проверить количество вошедших пассажиров в самолет на превышение посадочных мест
        if self.current_passengers + number_of_passengers <= self.capacity:
            self.current_passengers += number_of_passengers
            print(f"Посажено {number_of_passengers} пассажиров. Всего пассажиров: {self.current_passengers}")
        else:
            print("Недостаточно места для всех пассажиров.")

    # взлёт самолёта
    def take_off(self):
        # проверка возможности взлёта самолёта и установка флага
        if self.fuel_level_kg > 0 and self.current_passengers > 0:
            self.is_flying = True
            print(f"Самолёт {self.model} взлетел.")
        else:
            print("Не хватает топлива или нет пассажиров для взлёта.")


# согласно п.8 удалил комментарии, не относящиеся к делу (к пояснению кода) в методе take_off()


# №8
# вариант до

# Эта программа является частью более крупной системы, которая обрабатывает полёт спутника.
# Она включает в себя несколько модулей для проверки данных, взаимодействия с базами данных.
# Расчитываем скорость и расстояние, на которое пролетит спутник.
initial_speed = 0
acceleration = 2
time = 5

distance = initial_speed * time + 0.5 * acceleration * time ** 2
average_speed = distance / time
final_position = initial_speed * time + 0.5 * acceleration * time ** 2
final_speed = initial_speed + acceleration * time

# вариант после

# Расчитываем скорость и расстояние, на которое пролетит спутник.
initial_speed_ms = 0
acceleration_ms2 = 2
time_s = 5

distance = initial_speed_ms * time_s + 0.5 * acceleration_ms2 * time_s ** 2
average_speed = distance / time_s
final_position = initial_speed_ms * time_s + 0.5 * acceleration_ms2 * time_s ** 2
final_speed = initial_speed_ms + acceleration_ms2 * time_s

# согласно с п.9 убрал изложение информации системного уровня в контексте локального комментария


# №9
# вариант до
class Airplane:
    def __init__(self, model, capacity, fuel_level_kg):
        self.model = model  # модель самолета
        self.capacity = capacity  # сколько пассажиров может вместить самолёт
        self.current_passengers = 0  # текущее количество пассажиров в самолёте
        self.is_flying = False  # флаг летит ли самолёт в данный момент
        self.fuel_level_L = fuel_level_kg  # уровень топлива в баке самолёта

    # посадка пассажиров в самолёт
    def board_passengers(self, number_of_passengers):
        # проверить количество вошедших пассажиров в самолет на превышение посадочных мест
        if self.current_passengers + number_of_passengers <= self.capacity:
            self.current_passengers += number_of_passengers
            print(f"Посажено {number_of_passengers} пассажиров. Всего пассажиров: {self.current_passengers}")
        else:
            print("Недостаточно места для всех пассажиров.")

    # взлёт самолёта
    def take_off(self):
        # проверка возможности взлёта самолёта и установка флага
        if self.fuel_level_kg > 0 and self.current_passengers > 0:
            self.is_flying = True
            print(f"Самолёт {self.model} взлетел.")
        else:
            print("Не хватает топлива или нет пассажиров для взлёта.")

# вариант после
class Airplane:
    def __init__(self, model, capacity, fuel_level_kg):
        self.model = model
        self.capacity = capacity
        self.current_passengers = 0
        self.is_flying = False
        self.fuel_level_L = fuel_level_kg

    def board_passengers(self, number_of_passengers):
        # проверить количество вошедших пассажиров в самолет на превышение посадочных мест
        if self.current_passengers + number_of_passengers <= self.capacity:
            self.current_passengers += number_of_passengers
            print(f"Посажено {number_of_passengers} пассажиров. Всего пассажиров: {self.current_passengers}")
        else:
            print("Недостаточно места для всех пассажиров.")

    def take_off(self):
        # проверка возможности взлёта самолёта и установка флага
        if self.fuel_level_kg > 0 and self.current_passengers > 0:
            self.is_flying = True
            print(f"Самолёт {self.model} взлетел.")
        else:
            print("Не хватает топлива или нет пассажиров для взлёта.")

# согласно п.10 убрал комментарии, которые описывают все атрибуты и методы класса,
# однако их назначение очевидно из названия, оставил комментарии для условий для быстрого понимания


# №10
# вариант до
class Fan:
    def __init__(self, brand, speed_levels):
        # self.__brand = brand  # Бренд вентилятора
        # self.__speed_levels = speed_levels  # Количество скоростей
        self.__current_speed_ms = 0  # Текущая скорость
        self.__is_on = False  # включен или выключен

    def toggle_power(self):
        """Включение или выключение вентилятора."""
        self.__is_on = not self.__is_on
        if self.__is_on:
            self.__current_speed_ms = 1  # Скорость при вкючении
            state = "включен"
        else:
            self.__current_speed_ms = 0  # Обнуляем скорость при выключении
            state = "выключен"
        return f"Вентилятор теперь {state}, текущая скорость: {self.__current_speed_ms}"

# вариант после
class Fan:
    def __init__(self):
        self.__current_speed_ms = 0  # Текущая скорость
        self.__is_on = False  # включен или выключен

    def toggle_power(self):
        """Включение или выключение вентилятора."""
        self.__is_on = not self.__is_on
        if self.__is_on:
            self.__current_speed_ms = 1  # Скорость при вкючении
            state = "включен"
        else:
            self.__current_speed_ms = 0  # Обнуляем скорость при выключении
            state = "выключен"
        return f"Вентилятор теперь {state}, текущая скорость: {self.__current_speed_ms}"

# согласно п.11 удалил закоментированные атрибуты класса


# №11
# вариант до
def func(num1, num2):
    '''
    Эта функция расчитывает сложение двух чисел.
    Два числа определены в переменных num1 num2.
    Результат хранится в переменной sum.
    '''
    sum = num1 + num2
    return sum

# вариант после
def add_two_numbers(first_number_for_add, second_number_for_add):
    return first_number_for_add + second_number_for_add

# согласно п.12 удалил длинный заголовок короткой функции и используя говорящее имя, избавился от комментариев


# №12
# вариант до
def calculate_pension(current_age, retirement_age, current_income, contribution_percent, current_savings_usd):
    """
    Рассчитать пенсию на основе текущих данных.
    """
    total_savings_usd = current_savings_usd

    years_until_retirement = retirement_age - current_age

    # проверить, истекли ли года до выхода на пенсию
    if years_until_retirement <= 0:
        return "Вы уже на пенсии"

    # annual_contribution = current_income
    annual_contribution = current_income * (contribution_percent / 100)

    # подсчёт накоплений
    for year in range(years_until_retirement):
        total_savings_usd += annual_contribution
        total_savings_usd *= 1.05

    return total_savings_usd

# вариант после
def calculate_pension(current_age, retirement_age, current_income, contribution_percent, current_savings_usd):
    """
    Рассчитать пенсию на основе текущих данных.
    """
    total_savings_usd = current_savings_usd

    years_until_retirement = retirement_age - current_age

    # проверить, истекли ли года до выхода на пенсию
    if years_until_retirement <= 0:
        return "Вы уже на пенсии"

    annual_contribution = current_income * (contribution_percent / 100)

    # подсчёт накоплений
    for year in range(years_until_retirement):
        total_savings_usd += annual_contribution
        total_savings_usd *= 1.05

    return total_savings_usd


# согласно п.11 убрал закомментированный код из функции


# №13
# вариант до
class Book:
    def __init__(self, title, author, pages):
        self.__title = title  # заголовок книги
        self.__author = author  # автор книги
        self.__pages = pages  # количество страниц
        self.__current_page = 0  # текущая страница

    def get_details(self):
        """Получить информацию о книге"""
        return f"Название: {self.__title}, Автор: {self.__author}, Всего страниц: {self.__pages}"

    def read_pages(self, pages):
        """Чтение определенного количества страниц"""
        # проверить, что выбранная страница не превышает общее количество страниц
        if self.__current_page + pages > self.__pages:
            pages_to_read = self.__pages - self.__current_page
            self.__current_page = self.__pages
            return f"Вы прочитали последние {pages_to_read} страниц и закончили книгу."
        else:
            self.__current_page += pages
            return f"Вы прочитали {pages} страниц. Текущая страница: {self.__current_page}"

# вариант после
class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages
        self.__current_page = 0

    def get_details(self):
        return f"Название: {self.__title}, Автор: {self.__author}, Всего страниц: {self.__pages}"

    def read_pages(self, pages):
        # проверить, что выбранная страница не превышает общее количество страниц
        if self.__current_page + pages > self.__pages:
            pages_to_read = self.__pages - self.__current_page
            self.__current_page = self.__pages
            return f"Вы прочитали последние {pages_to_read} страниц и закончили книгу."
        else:
            self.__current_page += pages
            return f"Вы прочитали {pages} страниц. Текущая страница: {self.__current_page}"

# согласно п.10 убрал комментарии в описании атрибутов и методов, значения которых понятно из названия


# №14
# вариант до

# создаем класс автомобиля
class Car:
    def __init__(self, make, model, year):
        """Конструктор класса"""
        self.__make = make  # производитель
        self.__model = model  # модель
        self.__year = year  # год выпуска
        self.__odometer_reading = 0  # показания одометра
        self.__fuel_level = 0  # уровень топлива

    # метод вождения автомобиля
    def drive(self, distance_km):
        fuel_consumption_rate_kgs = 0.1  # постоянный расход топлива

        # проверить уровень топлива в баке
        if self.__fuel_level <= 0:
            print("Бак пуст")
        else:
            self.__odometer_reading += distance_km  # увеличиваем показания одометра
            self.__fuel_level -= distance_km * fuel_consumption_rate_kgs  # уменьшается топливо в баке

            # проверить уровень топлива в баке
            if self.__fuel_level < 0:
                self.__fuel_level = 0
            print(f"Проехали {distance_km} км")

# вариант после
class Car:
    def __init__(self, make, model, year):
        self.__make = make  # производитель
        self.__model = model  # модель
        self.__year = year  # год выпуска
        self.__odometer_reading = 0  # показания одометра
        self.__fuel_level = 0  # уровень топлива

    # вождение автомобиля
    def drive(self, distance_km):
        fuel_consumption_rate_kgs = 0.1  # постоянный расход топлива

        # проверить уровень топлива в баке
        if self.__fuel_level <= 0:
            print("Бак пуст")
        else:
            self.__odometer_reading += distance_km  # увеличиваем показания одометра
            self.__fuel_level -= distance_km * fuel_consumption_rate_kgs  # уменьшается топливо в баке

            # проверить уровень топлива в баке
            if self.__fuel_level < 0:
                self.__fuel_level = 0
            print(f"Проехали {distance_km} км")

# согласно п.4 убрал комментарии "шума", которые говорят о наличии класса, конструктора, метода


# №15
# вариант до
def bubble_sort(list_of_number):
    '''Функция сортировки пузырьком списка целых чисел'''
    n = len(list_of_number)
    swapped = True

    # я бы не использовал цикл и вообще это обсуждалось месяц назад
    while swapped:
        swapped = False
        for i in range(1, n):
            if list_of_number[i - 1] > list_of_number[i]:
                list_of_number[i - 1], list_of_number[i] = list_of_number[i], list_of_number[i - 1]
                swapped = True
        n -= 1

    return list_of_number

# вариант после
def bubble_sort(list_of_number):
    '''Функция сортировки пузырьком списка целых чисел'''
    n = len(list_of_number)
    swapped = True

    while swapped:
        swapped = False
        for i in range(1, n):
            if list_of_number[i - 1] > list_of_number[i]:
                list_of_number[i - 1], list_of_number[i] = list_of_number[i], list_of_number[i - 1]
                swapped = True
        n -= 1

    return list_of_number

# согласно п.8 удалил комментарий-обсуждение перед циклом

