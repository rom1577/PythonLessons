# №1
# неверный вариант
FUEL_CONSUMPTION_RATE_KGS = 0.1

class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__odometer_reading = 0
        self.__fuel_level = 0

    def drive(self, distance_km):

        if self.__fuel_level <= 0:
            print("Бак пуст")
        else:
            self.__odometer_reading += distance_km
            self.__fuel_level -= distance_km * FUEL_CONSUMPTION_RATE_KGS
            if self.__fuel_level < 0:
                self.__fuel_level = 0
            print(f"Проехали {distance_km} км")

# верный вариант
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__odometer_reading = 0
        self.__fuel_level = 0

    def drive(self, distance_km):
        fuel_consumption_rate_kgs = 0.1
        if self.__fuel_level <= 0:
            print("Бак пуст")
        else:
            self.__odometer_reading += distance_km
            self.__fuel_level -= distance_km * fuel_consumption_rate_kgs
            if self.__fuel_level < 0:
                self.__fuel_level = 0
            print(f"Проехали {distance_km} км")

# заменил консанту FUEL_CONSUMPTION_RATE_KGS на локальную переменную fuel_consumption_rate_kgs метода drive() класса Car


# №2
# Неверный вариант
class Worker:
    bonus = 0
    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary

    def calculate_annual_bonus(self, years):
        Worker.bonus = 0
        for _ in range(years):
            performance_factor = 1.05
            Worker.bonus += self.__salary * performance_factor
            performance_factor += 0.01
        return Worker.bonus

# верный вариант
class Worker:
    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary

    def calculate_annual_bonus(self, years):
        bonus = 0
        for _ in range(years):
            performance_factor = 1.05
            bonus += self.__salary * performance_factor
            performance_factor += 0.01
        return bonus

# заменил переменную bonus класса Worker на локальную переменную метода calculate_annual_bonus

# №3
# неверный вариант
swapped = False

def bubble_sort(list_of_number):
    global swapped
    n = len(list_of_number)
    swapped = True

    while swapped:
        swapped = False
        for i in range(1, n):
            if list_of_number[i - 1] > list_of_number[i]:
                list_of_number[i - 1], list_of_number[i] = list_of_number[i], list_of_number[i - 1]
                swapped = True
        n -= 1  # Уменьшаем n после каждой полной итерации

    return list_of_number

# верный вариант
def bubble_sort(list_of_number):
    n = len(list_of_number)
    swapped = True

    while swapped:
        swapped = False
        for i in range(1, n):
            if list_of_number[i - 1] > list_of_number[i]:
                list_of_number[i - 1], list_of_number[i] = list_of_number[i], list_of_number[i - 1]
                swapped = True
        n -= 1  # Уменьшаем n после каждой полной итерации

    return list_of_number

# в функции сортировки массива пузырьком bubble_sort заменил использование глобальной переменной swapped на
# использование локальной переменной swapped, которая задается внутри функции


# №4
# неверный вариант
class Marker:
    def __init__(self, color, ink_level=100):
        self.color = color  # Цвет маркера
        self.ink_level = ink_level  # Уровень чернил (по умолчанию 100)
        self.is_open = False  # Состояние маркера (открыт или закрыт)

    def write(self, text):
        # Письмо маркера
        if not self.is_open:
            print("Маркер закрыт! Сначала откройте маркер.")
            return

        if self.ink_level <= 0:
            print("Чернила закончились! Невозможно писать.")
            return

        print(f"Пишем '{text}' цветом {self.color}")
        # Уменьшение уровня чернил в зависимости от длины текста
        ink_used = len(text) * 0.5
        self.ink_level -= ink_used
        if self.ink_level < 0:
            self.ink_level = 0
        print(f"Остаток чернил: {self.ink_level:.2f}%")

    def open_close(self):
        self.is_open = not self.is_open
        state = "открыт" if self.is_open else "закрыт"
        print(f"Маркер теперь {state}.")

# верный вариант
class Marker:
    def __init__(self, color, ink_level=100):
        self.__color = color  # Цвет маркера
        self.__ink_level = ink_level  # Уровень чернил (по умолчанию 100)
        self.__is_open = False  # Состояние маркера (открыт или закрыт)

    def write(self, text):
        # Письмо маркера
        if not self.__is_open:
            print("Маркер закрыт! Сначала откройте маркер.")
            return

        if self.__ink_level <= 0:
            print("Чернила закончились! Невозможно писать.")
            return

        print(f"Пишем '{text}' цветом {self.__color}")
        # Уменьшение уровня чернил в зависимости от длины текста
        ink_used = len(text) * 0.5
        self.__ink_level -= ink_used
        if self.__ink_level < 0:
            self.__ink_level = 0
        print(f"Остаток чернил: {self.__ink_level:.2f}%")

    def open_close(self):
        self.__is_open = not self.__is_open
        state = "открыт" if self.__is_open else "закрыт"
        print(f"Маркер теперь {state}.")

# изменил уровень видимости атрибутов класса Marker с публичных до приватных


# №5
# неверный вариант
time_to_boil_s = 0

class Kettle:
    def __init__(self, brand, color, capacity):
        self.brand = brand  # Бренд чайника
        self.color = color  # Цвет чайника
        self.capacity = capacity  # Емкость чайника в литрах
        self.current_water_level = 0.0  # Текущий уровень воды в литрах
        self.is_on = False  # Состояние чайника (включен или выключен)

    def boil_water(self):
        # Кипячение воды
        global time_to_boil  # Объявляем использование глобальной переменной

        if not self.is_on:
            print("Чайник выключен!")
            return

        if self.current_water_level <= 0:
            print("Нет воды!")
            return

        time_to_boil_s = self.current_water_level * 4  # Рассчитываем время кипячения
        print("Вода вскипела!")

    def toggle_power(self):
        # Включение или выключение чайника
        self.is_on = not self.is_on
        state = "включен" if self.is_on else "выключен"
        print(f"Чайник теперь {state}.")


# верный вариант
class Kettle:
    def __init__(self, brand, color, capacity):
        self.brand = brand  # Бренд чайника
        self.color = color  # Цвет чайника
        self.capacity = capacity  # Емкость чайника в литрах
        self.current_water_level = 0.0  # Текущий уровень воды в литрах
        self.is_on = False  # Состояние чайника (включен или выключен)

    def boil_water(self):
        # Кипячение воды
        if not self.is_on:
            print("Чайник выключен!")
            return

        if self.current_water_level <= 0:
            print("Нет воды!")
            return

        time_to_boil_s = self.current_water_level * 4  # Рассчитываем время кипячения
        print(f"Вода вскипела! Время займет {time_to_boil_s}")

    def toggle_power(self):
        # Включение или выключение чайника
        self.is_on = not self.is_on
        state = "включен" if self.is_on else "выключен"
        print(f"Чайник теперь {state}.")

# использовал внутреннюю переменную time_to_boil_s в методе кипячения воды boil_water вместо использования глобальной переменной

# №6
# неверный вариант
total_savings_usd = 0  # сумма накоплений

def calculate_pension(current_age, retirement_age, current_income, contribution_percent, current_savings_usd):
    """
    Рассчитать пенсию на основе текущих данных.
    """
    global total_savings_usd  # Объявляем использование глобальной переменной
    total_savings_usd = current_savings_usd

    years_until_retirement = retirement_age - current_age
    if years_until_retirement <= 0:
        return "Вы уже на пенсии"

    annual_contribution = current_income * (contribution_percent / 100)

    for year in range(years_until_retirement):
        total_savings_usd += annual_contribution
        total_savings_usd *= 1.05

    return total_savings_usd

# верный вариант
def calculate_pension(current_age, retirement_age, current_income, contribution_percent, current_savings_usd):
    """
    Рассчитать пенсию на основе текущих данных.
    """
    total_savings_usd = current_savings_usd

    years_until_retirement = retirement_age - current_age
    if years_until_retirement <= 0:
        return "Вы уже на пенсии"

    annual_contribution = current_income * (contribution_percent / 100)

    for year in range(years_until_retirement):
        total_savings_usd += annual_contribution
        total_savings_usd *= 1.05

    return total_savings_usd

# заменил исопльзование глобальной переменной в функции расчета пенсии на локальную переменную total_savings_usd


# №7
# неверный вариант
class Airplane:
    def __init__(self, model, capacity, fuel_level):
        self.model = model  # Модель самолёта
        self.capacity = capacity  # Вместимость самолёта
        self.current_passengers = 0  # Текущее количество пассажиров
        self.is_flying = False  # Состояние самолёта (в полёте или нет)
        self.fuel_level = fuel_level  # Уровень топлива
        self.traveled_distance_km = 0  # Пройденное расстояние

    def board_passengers(self, number_of_passengers):
        #  Посадка пассажиров на самолёт
        if self.current_passengers + number_of_passengers <= self.capacity:
            self.current_passengers += number_of_passengers
            print(f"Посажено {number_of_passengers} пассажиров. Всего пассажиров: {self.current_passengers}")
        else:
            print("Недостаточно места для всех пассажиров.")

    def take_off(self):
        #  Взлёт самолёта
        if self.fuel_level > 0 and self.current_passengers > 0:
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
        self.traveled_distance_km = 0  # Сброс пройденного расстояния перед полётом

        for km in range(distance):
            if self.fuel_level <= 0:
                print("Топливо закончилось")
                self.is_flying = False
                break
            self.fuel_level -= fuel_consumption_per_km
            self.traveled_distance_km += 1
            print(f"Полетел {self.traveled_distance_km} км")

        if self.fuel_level > 0:
            print(f"Самолёт пролетел {self.traveled_distance_km} км ")
            self.is_flying = False

# верный вариант
class Airplane:
    def __init__(self, model, capacity, fuel_level):
        self.model = model  # Модель самолёта
        self.capacity = capacity  # Вместимость самолёта
        self.current_passengers = 0  # Текущее количество пассажиров
        self.is_flying = False  # Состояние самолёта (в полёте или нет)
        self.fuel_level = fuel_level  # Уровень топлива

    def board_passengers(self, number_of_passengers):
        #  Посадка пассажиров на самолёт
        if self.current_passengers + number_of_passengers <= self.capacity:
            self.current_passengers += number_of_passengers
            print(f"Посажено {number_of_passengers} пассажиров. Всего пассажиров: {self.current_passengers}")
        else:
            print("Недостаточно места для всех пассажиров.")

    def take_off(self):
        #  Взлёт самолёта
        if self.fuel_level > 0 and self.current_passengers > 0:
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
        total_fuel_needed = distance * fuel_consumption_per_km
        traveled_distance_km = 0

        for km in range(distance):
            if self.fuel_level <= 0:
                print("Топливо закончилось")
                self.is_flying = False
                break
            self.fuel_level -= fuel_consumption_per_km
            traveled_distance_km += 1
            print(f"Полетел {traveled_distance_km} км")

        if self.fuel_level > 0:
            print(f"Самолёт пролетел {traveled_distance_km} км")
            self.is_flying = False

# заменил атрибут класса self.traveled_distance_km на переменную traveled_distance_km в методе полёта fly


# №8
# неверный вариант
class Book:
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages
        self._current_page = 0

    def read_pages(self, pages):
        """Чтение определенного количества страниц."""
        if self._current_page + pages > self._pages:
            pages_to_read = self._pages - self._current_page
            self._current_page = self._pages
            return f"Вы прочитали последние {pages_to_read} страниц и закончили книгу."
        else:
            self._current_page += pages
            return f"Вы прочитали {pages} страниц. Текущая страница: {self._current_page}"

# верный вариант
class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages
        self.__current_page = 0

    def get_details(self):
        """Получить информацию о книге."""
        return f"Название: {self.__title}, Автор: {self.__author}, Всего страниц: {self.__pages}"

    def read_pages(self, pages):
        """Чтение определенного количества страниц."""
        if self.__current_page + pages > self.__pages:
            pages_to_read = self.__pages - self.__current_page
            self.__current_page = self.__pages
            return f"Вы прочитали последние {pages_to_read} страниц и закончили книгу."
        else:
            self.__current_page += pages
            return f"Вы прочитали {pages} страниц. Текущая страница: {self.__current_page}"

# заменил атрибуты класа книги с защищенных на приватные, увеличив инкапсуляцию


# №9
# неверный вариант
class Fan:
    def __init__(self, brand, speed_levels):
        self.brand = brand  # Бренд вентилятора
        self.speed_levels = speed_levels  # Количество скоростей
        self.current_speed_ms = 0  # Текущая скорость
        self.is_on = False  # включен или выключен

    def toggle_power(self):
        """Включение или выключение вентилятора."""
        self.is_on = not self.is_on
        if self.is_on:
            self.current_speed_ms = 1  # Скорость при вкючении
            state = "включен"
        else:
            self.current_speed_ms = 0  # Обнуляем скорость при выключении
            state = "выключен"
        return f"Вентилятор {self.brand} теперь {state}, текущая скорость: {self.current_speed_ms}"

# верный вариант
class Fan:
    def __init__(self, brand, speed_levels):
        self.__brand = brand  # Бренд вентилятора
        self.__speed_levels = speed_levels  # Количество скоростей
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
        return f"Вентилятор {self.__brand} теперь {state}, текущая скорость: {self.__current_speed_ms}"

# заменил все атрибуты класса с публичных на приватные


# №10
# неверный вариант

# Класс работника
class Employee:
    def __init__(self, salary, years_of_service,age,marital_status):
        self.salary = salary  # зарплата
        self.years_of_service = years_of_service  # стаж
        self.personal_data = {"age":age,"marital_status":marital_status}  # персональные данные

    def get_salary(self):
        return self.salary

    def get_years_of_service(self):
        return self.years_of_service

    def get_personal_data(self):
        return self.personal_data

# экземпляр класса
employee = Employee(100,10,35,"married")

# функция расчета пенсии
def calculate_pension(employee):
    # Получение данных
    salary = employee.get_salary()
    years_of_service = employee.get_years_of_service()
    personal_data = employee.get_personal_data()

    # Первоначальная пенсия
    print("Вычисление начальной пенсии...")
    base_pension = (salary * 0.5) * (years_of_service / 30)
    print("Начальная пенсия:", base_pension)

    # Условия для надбавок
    if personal_data['age'] >= 65:
        age_bonus = base_pension * 0.1
    else:
        age_bonus = 0

    if personal_data['marital_status'] == 'married':
        family_bonus = base_pension * 0.05
    else:
        family_bonus = 0

    # Изменение пенсии в зависимости от данных
    pension = base_pension + age_bonus + family_bonus

    print("Пенсия до налогов:", pension)

    # Расчет налогов
    tax = 0.2 if pension > 2000 else 0.1
    net_pension = pension * (1 - tax)
    print("Чистая пенсия после налогов:", net_pension)

    return net_pension

# верный вариант

# класс работника
class Employee:
    def __init__(self, salary, years_of_service,age,marital_status):
        self.salary = salary  # зарплата
        self.years_of_service = years_of_service  # стаж
        self.personal_data = {"age":age,"marital_status":marital_status}  # персональные данные

    def get_salary(self):
        return self.salary

    def get_years_of_service(self):
        return self.years_of_service

    def get_personal_data(self):
        return self.personal_data

# экземпляр класса
employee = Employee(100,10,35,"married")

def calculate_base_pension(salary, years_of_service):
    print("Вычисление базовой пенсии...")
    base_pension = (salary * 0.5) * (years_of_service / 30)
    print("Базовая пенсия:", base_pension)
    return base_pension

def calculate_age_bonus(base_pension, age):
    print("Вычисление надбавки за возраст...")
    age_bonus = base_pension * 0.1 if age >= 65 else 0
    print("Надбавка за возраст:", age_bonus)
    return age_bonus

def calculate_family_bonus(base_pension, marital_status):
    print("Вычисление семейной надбавки...")
    family_bonus = base_pension * 0.05 if marital_status == 'married' else 0
    print("Семейная надбавка:", family_bonus)
    return family_bonus

def calculate_taxes(pension):
    print("Расчет налогов...")
    tax_rate = 0.2 if pension > 2000 else 0.1
    taxes = pension * tax_rate
    print("Налоги:", taxes)
    return taxes

def calculate_pension(employee):
    # Получение данных
    salary = employee.get_salary()
    years_of_service = employee.get_years_of_service()
    personal_data = employee.get_personal_data()

    # Обработка данных в специализированных функциях
    base_pension = calculate_base_pension(salary, years_of_service)
    age_bonus = calculate_age_bonus(base_pension, personal_data['age'])
    family_bonus = calculate_family_bonus(base_pension, personal_data['marital_status'])

    pension_before_taxes = base_pension + age_bonus + family_bonus
    print("Пенсия до налогов:", pension_before_taxes)

    taxes = calculate_taxes(pension_before_taxes)
    net_pension = pension_before_taxes - taxes
    print("Чистая пенсия после налогов:", net_pension)

    return net_pension

# в неверном варианте происходит расчет пенсии для экземпляра работника в одной функции, что приводит к
# большому времени жизни переменных, что ухудшает безопасность и читаемость;
# в верном варианте расчет пенсии выполняется последовательно в специальных функциях, разделенным по тематикам



# №11
# неверный вариант
class Computer:
    def __init__(self, purchase_year, model,usage_hours,warranty_period):
        self.purchase_year = purchase_year  # дата покупки
        self.model = model  # модель
        self.usage_hours = usage_hours  # наработанные часы
        self.warranty_period = warranty_period  # гарантийный период

    def get_purchase_year(self):
        return self.purchase_year

    def get_model(self):
        return self.model

    def get_usage_hours(self):
        return self.usage_hours

    def get_warranty_period(self):
        return self.warranty_period

computer = Computer(2020,"Standard",10,5)

# функция расчета срока службы компьютера
def calculate_computer_lifespan(computer):
    # Получение данных
    purchase_year = computer.get_purchase_year()
    model = computer.get_model()
    usage_hours = computer.get_usage_hours()
    warranty_period = computer.get_warranty_period()

    # Первоначальные вычисления
    print("Вычисление предполагаемого срока службы...")
    current_year = 2024
    age = current_year - purchase_year

    # Расчет на основе модели
    if model in ['HighEnd', 'Gaming']:
        base_lifespan = 7
    elif model in ['Business', 'Standard']:
        base_lifespan = 5
    else:
        base_lifespan = 3

    # Корректировка по часам использования
    if usage_hours > 5000:
        usage_penalty = 2
    else:
        usage_penalty = 1

    # Корректировка по гарантии
    if warranty_period >= 3:
        warranty_bonus = 1
    else:
        warranty_bonus = 0

    estimated_lifespan = base_lifespan - age - usage_penalty + warranty_bonus

    print("Предполагаемый срок службы:", estimated_lifespan)

    # Окончательная оценка
    if estimated_lifespan < 0:
        estimated_lifespan = 0
    print("Окончательный срок службы:", estimated_lifespan)

    return estimated_lifespan

# верный вариант
class Computer:
    def __init__(self, purchase_year, model,usage_hours,warranty_period):
        self.purchase_year = purchase_year  # дата покупки
        self.model = model  # модель
        self.usage_hours = usage_hours  # наработанные часы
        self.warranty_period = warranty_period  # гарантийный период

    def get_purchase_year(self):
        return self.purchase_year

    def get_model(self):
        return self.model

    def get_usage_hours(self):
        return self.usage_hours

    def get_warranty_period(self):
        return self.warranty_period

computer = Computer(2020,"Standard",10,5)

def get_base_lifespan(model):
    print("Вычисление базового срока службы на основе модели")
    if model in ['HighEnd', 'Gaming']:
        return 7
    elif model in ['Business', 'Standard']:
        return 5
    else:
        return 3

def calculate_usage_penalty(usage_hours):
    print("Расчет штрафа за часы использования...")
    if usage_hours > 5000:
        return 2
    else:
        return 1

def calculate_warranty_bonus(warranty_period):
    print("Расчет бонуса за гарантийный период...")
    return 1 if warranty_period >= 3 else 0

def calculate_age_penalty(purchase_year, current_year):
    print("Расчет штрафа за возраст...")
    return current_year - purchase_year

def calculate_computer_lifespan(computer):
    # Получение чувствительных данных
    purchase_year = computer.get_purchase_year()
    model = computer.get_model()
    usage_hours = computer.get_usage_hours()
    warranty_period = computer.get_warranty_period()

    # Текущий год
    current_year = 2024

    # Выполнение вычислений в изолированных функциях
    base_lifespan = get_base_lifespan(model)
    usage_penalty = calculate_usage_penalty(usage_hours)
    warranty_bonus = calculate_warranty_bonus(warranty_period)
    age_penalty = calculate_age_penalty(purchase_year, current_year)

    # Объединение результатов
    estimated_lifespan = base_lifespan - age_penalty - usage_penalty + warranty_bonus
    print("Предполагаемый срок службы до окончательной оценки:", estimated_lifespan)

    # Окончательная оценка
    final_lifespan = max(0, estimated_lifespan)
    print("Окончательный предполагаемый срок службы:", final_lifespan)

    return final_lifespan


# в неверном варианте происходит расчет срока службы компьютера; все вычисления делаются в одной функции;
# в верном варианте расчет срока службы выполняется последовательно в специальных функциях, разделенным по тематикам



# №12
# неверный вариант
class Car:
    def __init__(self, purchase_price, model,mileage):
        self.purchase_price = purchase_price  # стоимость покупки
        self.model = model  # модель
        self.mileage = mileage  # пробег

    def get_purchase_price(self):
        return self.purchase_year

    def get_mileage(self):
        return self.model

    def get_model(self):
        return self.usage_hours

car = Car(1000,"Suzuki",1000000)

def calculate_car_value(car):
    # Получение данных
    purchase_price = car.get_purchase_price()
    mileage = car.get_mileage()
    model = car.get_model()

    # Расчет базовой стоимости на основе модели
    if model in ['Luxury', 'Sports']:
        base_value = purchase_price * 0.5
    elif model in ['SUV', 'Sedan']:
        base_value = purchase_price * 0.3
    else:
        base_value = purchase_price * 0.2

    # Корректировка на основе пробега
    if mileage > 100000:
        mileage_penalty = base_value * 0.2
    else:
        mileage_penalty = base_value * 0.1

    estimated_value = base_value - mileage_penalty

    print("Окончательная стоимость автомобиля:", estimated_value)
    return estimated_value

# верный вариант
class Car:
    def __init__(self, purchase_price, model,mileage):
        self.purchase_price = purchase_price  # стоимость покупки
        self.model = model  # модель
        self.mileage = mileage  # пробег

    def get_purchase_price(self):
        return self.purchase_year

    def get_mileage(self):
        return self.model

    def get_model(self):
        return self.usage_hours

car = Car(1000,"Suzuki",1000000)

def get_base_value(purchase_price, model):
    print("Расчет базовой стоимости на основе модели...")
    if model in ['Luxury', 'Sports']:
        return purchase_price * 0.5
    elif model in ['SUV', 'Sedan']:
        return purchase_price * 0.3
    else:
        return purchase_price * 0.2

def calculate_mileage_penalty(base_value, mileage):
    print("Расчет штрафа за пробег...")
    if mileage > 100000:
        return base_value * 0.2
    else:
        return base_value * 0.1

def calculate_car_value(car):
    # Получение  данных
    purchase_price = car.get_purchase_price()
    purchase_date = car.get_purchase_date()
    mileage = car.get_mileage()
    model = car.get_model()

    # Обработка данных в специализированных функциях
    base_value = get_base_value(purchase_price, model)
    mileage_penalty = calculate_mileage_penalty(base_value, mileage)
    age_penalty = calculate_age_penalty(purchase_date)

    # Объединение результатов
    estimated_value = base_value - mileage_penalty - age_penalty
    print("стоимость:", estimated_value)

    return estimated_value

# аналогично в неверном варианте происходит расчет оценки стоимости поддержанного автомобиля в одной функции;
# в верном варианте расчет стоимости машины выполняется последовательно в множестве специальных функций



# №13
# неверный вариант
# класс человека, севшего на диету
class Person:
    def __init__(self, weight, height, age, gender, activity_level, diet_goal):
        self.weight = weight  # вес
        self.height = height  # высота
        self.age = age  # возраст
        self.gender = gender  # рол
        self.activity_level = activity_level  # уровень активности
        self.diet_goal = diet_goal  # цель диеты

    def get_weight(self):
        return self.weight

    def get_height(self):
        return self.height

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_activity_level(self):
        return self.activity_level

    def get_diet_goal(self):
        return self.diet_goal

person = Person(100, 185, 40, "male", "moderate", "lose_weight")

def calculate_caloric_intake(person):
    # Получение данных
    weight = person.get_weight()
    height = person.get_height()
    age = person.get_age()
    gender = person.get_gender()
    activity_level = person.get_activity_level()
    diet_goal = person.get_diet_goal()

    # Первоначальные вычисления
    print("Вычисление базовой нормы калорий...")
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    # Учет уровня активности
    if activity_level == 'sedentary':
        tdee = bmr * 1.2
    elif activity_level == 'light':
        tdee = bmr * 1.375
    elif activity_level == 'moderate':
        tdee = bmr * 1.55
    elif activity_level == 'active':
        tdee = bmr * 1.725
    else:
        tdee = bmr * 1.9

    print("расход энергии", tdee)

    # Корректировка на основе целей диеты
    if diet_goal == 'lose_weight':
        caloric_intake = tdee - 500
    elif diet_goal == 'gain_weight':
        caloric_intake = tdee + 500
    else:
        caloric_intake = tdee

    print("Рекомендуемая дневная норма калорий:", caloric_intake)

    return caloric_intake


# верный вариант
class Person:
    def __init__(self, weight, height, age, gender, activity_level, diet_goal):
        self.weight = weight  # вес
        self.height = height  # высота
        self.age = age  # возраст
        self.gender = gender  # рол
        self.activity_level = activity_level  # уровень активности
        self.diet_goal = diet_goal  # цель диеты

    def get_weight(self):
        return self.weight

    def get_height(self):
        return self.height

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_activity_level(self):
        return self.activity_level

    def get_diet_goal(self):
        return self.diet_goal

person = Person(100, 185, 40, "male", "moderate", "lose_weight")

def calculate_bmr(weight, height, age, gender):
    print("Расчет базового метаболизма (BMR)...")
    if gender == 'male':
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def calculate_tdee(bmr, activity_level):
    print("Расчет общего расхода энергии (TDEE)...")
    if activity_level == 'sedentary':
        return bmr * 1.2
    elif activity_level == 'light':
        return bmr * 1.375
    elif activity_level == 'moderate':
        return bmr * 1.55
    elif activity_level == 'active':
        return bmr * 1.725
    else:
        return bmr * 1.9

def adjust_for_diet_goal(tdee, diet_goal):
    print("Корректировка на основе целей диеты...")
    if diet_goal == 'lose_weight':
        return tdee - 500
    elif diet_goal == 'gain_weight':
        return tdee + 500
    else:
        return tdee

def calculate_caloric_intake(person):
    # Получение данных
    weight = person.get_weight()
    height = person.get_height()
    age = person.get_age()
    gender = person.get_gender()
    activity_level = person.get_activity_level()
    diet_goal = person.get_diet_goal()

    # Обработка данных в функциях
    bmr = calculate_bmr(weight, height, age, gender)
    tdee = calculate_tdee(bmr, activity_level)
    final_caloric_intake = adjust_for_diet_goal(tdee, diet_goal)

    return final_caloric_intake

# в неверном варианте происходит расчет каллорий для диеты человека в одной функции;
# в верном варианте происходит разбивка на короткие методы, где время жизни переменной уменьшается,
# а значит увеличивается бузопасность кода



# №14
# неверный вариант
class Order:
    def __init__(self, distance, delivery_type, traffic_conditions):
        self.distance = distance  # расстояние доставки
        self.delivery_type = delivery_type  # тип доставки
        self.traffic_conditions = traffic_conditions  # пробки

    def get_distance(self):
        return self.distance

    def get_delivery_type(self):
        return self.delivery_type

    def get_traffic_conditions(self):
        return self.traffic_conditions


order = Order(100, 'express', 'heavy')

def calculate_delivery_time(order):
    # Получение чувствительных данных
    distance = order.get_distance()
    delivery_type = order.get_delivery_type()
    traffic_conditions = order.get_traffic_conditions()

    # Первоначальные вычисления
    print("Начало расчета времени доставки...")
    if delivery_type == 'express':
        base_time = distance / 50  # экспресс-доставки
    else:
        base_time = distance / 30  # бычные доставки

    print("Базовое время доставки:", base_time, "часов")

    # Корректировка на основе пробок
    if traffic_conditions == 'heavy':
        traffic_delay = base_time * 0.5  # 50% задержка
    elif traffic_conditions == 'moderate':
        traffic_delay = base_time * 0.3  # 30% задержка
    else:
        traffic_delay = base_time * 0.1  # 10% задержка

    print("Задержка из-за пробок:", traffic_delay, "часов")

    estimated_delivery_time = base_time + traffic_delay

    print("Окончательное время доставки:", estimated_delivery_time, "часов")
    return estimated_delivery_time

# верный вариант
class Order:
    def __init__(self, distance, delivery_type, traffic_conditions):
        self.distance = distance  # расстояние доставки
        self.delivery_type = delivery_type  # тип доставки
        self.traffic_conditions = traffic_conditions  # пробки

    def get_distance(self):
        return self.distance

    def get_delivery_type(self):
        return self.delivery_type

    def get_traffic_conditions(self):
        return self.traffic_conditions


order = Order(100, 'express', 'heavy')

def get_base_delivery_time(distance, delivery_type):
    print("Расчет базового времени доставки...")
    if delivery_type == 'express':
        return distance / 50  # 50 км/ч для экспресс-доставки
    else:
        return distance / 30  # 30 км/ч для обычной доставки

def calculate_traffic_delay(base_time, traffic_conditions):
    print("Расчет задержки из-за пробок...")
    if traffic_conditions == 'heavy':
        return base_time * 0.5  # 50% задержка
    elif traffic_conditions == 'moderate':
        return base_time * 0.3  # 30% задержка
    else:
        return base_time * 0.1  # 10% задержка


def calculate_delivery_time(order):
    # Получение чувствительных данных
    distance = order.get_distance()
    delivery_type = order.get_delivery_type()
    traffic_conditions = order.get_traffic_conditions()

    # Обработка чувствительных данных в специализированных функциях
    base_time = get_base_delivery_time(distance, delivery_type)
    traffic_delay = calculate_traffic_delay(base_time, traffic_conditions)
    final_delivery_time = base_time + traffic_delay
    print("Окончательное время доставки:", final_delivery_time, "часов")

    return final_delivery_time

# аналогично в неверном варианте происходит расчет времени доставки заказа в одной функции;
# разбивка операций на множество фнукций в верном варианте улучшает безопасность и читаемость кода,
# т.к. переменные меньше времени подвержены изменению


# №15
# неверный вариант
class Car:
    def __init__(self, distance, fuel_efficiency, road_type, traffic_conditions):
        self.distance = distance  # сколько проехала машина
        self.fuel_efficiency = fuel_efficiency  # эффективность топлива
        self.road_type = road_type  # тип дороги
        self.traffic_conditions = traffic_conditions  # пробки

    def get_distance(self):
        return self.distance

    def get_fuel_efficiency(self):
        return self.fuel_efficiency

    def get_road_type(self):
        return self.road_type

    def get_traffic_conditions(self):
        return self.traffic_conditions

car = Car(1000, 0.7, "city", 'heavy')

def calculate_fuel_consumption(car):
    # Получение данных
    distance = car.get_distance()
    fuel_efficiency = car.get_fuel_efficiency()
    road_type = car.get_road_type()
    traffic_conditions = car.get_traffic_conditions()

    # Первоначальные вычисления
    print("Начало расчета расхода топлива...")
    if road_type == 'highway':
        base_consumption = distance / fuel_efficiency * 0.8  # 20% меньше расход на трассе
    elif road_type == 'city':
        base_consumption = distance / fuel_efficiency * 1.2  # 20% больше расход в городе
    else:
        base_consumption = distance / fuel_efficiency  # обычный расход

    print("Базовый расход топлива:", base_consumption, "литров")

    # Корректировка на основе условий движения
    if traffic_conditions == 'heavy':
        traffic_penalty = base_consumption * 0.3
    elif traffic_conditions == 'moderate':
        traffic_penalty = base_consumption * 0.1
    else:
        traffic_penalty = base_consumption * 0.05

    estimated_fuel_consumption = base_consumption + traffic_penalty

    print("Окончательный расход топлива:", estimated_fuel_consumption, "литров")
    return estimated_fuel_consumption

# верный вариант
class Car:
    def __init__(self, distance, fuel_efficiency, road_type, traffic_conditions):
        self.distance = distance  # сколько проехала машина
        self.fuel_efficiency = fuel_efficiency  # эффективность топлива
        self.road_type = road_type  # тип дороги
        self.traffic_conditions = traffic_conditions  # пробки

    def get_distance(self):
        return self.distance

    def get_fuel_efficiency(self):
        return self.fuel_efficiency

    def get_road_type(self):
        return self.road_type

    def get_traffic_conditions(self):
        return self.traffic_conditions

car = Car(1000, 0.7, "city", 'heavy')

def calculate_base_consumption(distance, fuel_efficiency, road_type):
    print("Расчет базового расхода топлива...")
    if road_type == 'highway':
        return distance / fuel_efficiency * 0.8
    elif road_type == 'city':
        return distance / fuel_efficiency * 1.2
    else:
        return distance / fuel_efficiency

def calculate_traffic_penalty(base_consumption, traffic_conditions):
    print("Расчет дополнительного расхода из-за условий движения...")
    if traffic_conditions == 'heavy':
        return base_consumption * 0.3
    elif traffic_conditions == 'moderate':
        return base_consumption * 0.1
    else:
        return base_consumption * 0.05


def calculate_fuel_consumption(car):
    # Получение данных
    distance = car.get_distance()
    fuel_efficiency = car.get_fuel_efficiency()
    road_type = car.get_road_type()
    traffic_conditions = car.get_traffic_conditions()

    # Обработка  данных в специализированных функциях
    base_consumption = calculate_base_consumption(distance, fuel_efficiency, road_type)
    traffic_penalty = calculate_traffic_penalty(base_consumption, traffic_conditions)

    final_fuel_consumption = base_consumption + traffic_penalty
    print("Окончательный расход топлива:", final_fuel_consumption, "литров")

    return final_fuel_consumption

# путем разбиения фкнции подсчета расхода топлива машины на несколько малых функций
# уменьшается время, в течении которого
# переменные находятся в состоянии, подверженому изменению


