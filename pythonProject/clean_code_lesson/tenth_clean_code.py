# №1
# неверный вариант
import math
c0 = 5.67 # постоянная Стефана Больцмана
temper_of_chamber_K = 3000
degree_of_blackness = 0.9
chamber_diameter_m = 0.1
length_cylyndr_part_m = 0.1

radiant_gas_volume_m3 = math.pi * chamber_diameter_m **2 / 4 * length_cylyndr_part_m  # объём излучаемого газа
wall_area_m2 = math.pi * chamber_diameter_m * length_cylyndr_part_m  # площадь поверхности стенки, окружающ газ
effect_radiant_length_m = 3.6 * radiant_gas_volume_m3 / wall_area_m2  # эффективная длина излучаемого газового слоя

radiant_flux_W = degree_of_blackness*c0*(temper_of_chamber_K/100)**4

# верный вариант
import math

chamber_diameter_m = 0.1
length_cylyndr_part_m = 0.1

radiant_gas_volume_m3 = math.pi * chamber_diameter_m **2 / 4 * length_cylyndr_part_m  # объём излучаемого газа
wall_area_m2 = math.pi * chamber_diameter_m * length_cylyndr_part_m  # площадь поверхности стенки, окружающ газ
effect_radiant_length_m = 3.6 * radiant_gas_volume_m3 / wall_area_m2  # эффективная длина излучаемого газового слоя

CONSTANT_OF_BOLTZMANN = 5.67
temper_of_chamber_K = 3000
DEGREE_OF_BLACKNESS = 0.9

radiant_flux_W = degree_of_blackness*c0*(temper_of_chamber_K/100)**4

# переместил место инициализации переменных CONSTANT_OF_BOLTZMANN, temper_of_chamber_K, DEGREE_OF_BLACKNESS ближе к
# месту использования; также заменил переменные на константы, где это возможно, константы выделил заглавными буквами


# №2
# неверный вариант
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def set_publication_year(self, publication_year):
        self.publication_year = publication_year

    def set_number_of_pages(self, number_of_pages):
        self.number_of_pages = number_of_pages

# верный вариант
class Book:
    def __init__(self, title, author, publication_year, number_of_pages):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.number_of_pages = number_of_pages

# изменил инициализацию атрибутов класса, сделав их инициализацию в конструкторе, а не в отдельных методах

# №3
# неверный вариант
def Startup():
    global initial_speed
    global acceleration
    global time
    initial_speed = 0
    acceleration = 2
    time = 5

Startup()

distance = initial_speed * time + 0.5 * acceleration * time ** 2
average_speed = distance / time
final_position = initial_speed * time + 0.5 * acceleration * time ** 2
final_speed = initial_speed + acceleration * time

# верный вариант
initial_speed = 0
acceleration = 2
time = 5

distance = initial_speed * time + 0.5 * acceleration * time ** 2
average_speed = distance / time
final_position = initial_speed * time + 0.5 * acceleration * time ** 2
final_speed = initial_speed + acceleration * time

# вместо использования блока синхронизации инициализировал переменные непоредственно перед местом расчета

# №4
# неверный вариант
class Car:
    def __init__(self, making_country, model, year, mileage_km):
        self.making_country = making_country
        self.model = model
        self.year = year
        self.mileage_km = mileage_km

    def drive(self, distance_km, velocity_ms):
        self.mileage_km += distance_km
        self.velocity_ms = velocity_ms

    def stop(self):
        self.velocity_ms = 0

    def new_color(self):
        self.color = 'red'

# верный вариант
class Car:
    def __init__(self, making_country, model, year, mileage_km, color):
        self.making_country = making_country
        self.model = model
        self.year = year
        self.mileage_km = mileage_km
        self.color = color

    def drive(self, distance_km, velocity_ms):
        self.mileage_km += distance_km
        self.velocity_ms = velocity_ms

    def stop(self):
        self.velocity_ms = 0

# определил инициализацию поля self.color внутри конструктора, а не в отдельном методе


# №5
# неверный вариант
initial_speed = 0
acceleration = 2
time = 5

distance = initial_speed * time + 0.5 * acceleration * time ** 2
average_speed = distance / time
final_position = initial_speed * time + 0.5 * acceleration * time ** 2
final_speed = initial_speed + acceleration * time
print(final_speed, final_position)

# верный вариант
initial_speed = 0
acceleration = 2
time = 5

distance = initial_speed * time + 0.5 * acceleration * time ** 2
average_speed = distance / time
final_position = initial_speed * time + 0.5 * acceleration * time ** 2
final_speed = initial_speed + acceleration * time

print(final_speed, final_position)

final_speed = -1000.0
final_position = -1.0

# после вывода на экран переменных final_speed, final_position завершил работу с ними, присвоив неадекватные значения


# №6
# неверный вариант
class Car:
    def __init__(self, making_country, model, year, mileage_km, color):
        self.making_country = making_country
        self.model = model
        self.year = year
        self.mileage_km = mileage_km
        self.color = color

    def drive(self, distance_km, velocity_ms):
        self.mileage_km += distance_km
        self.velocity_ms = velocity_ms

    def stop(self):
        self.velocity_ms = 0

lada_sport = Car("Russia", "Vesta", 2020, 5000, "Red")
lada_sport.drive(50, 100)
lada_sport.stop()

# верный вариант
class Car:
    def __init__(self, making_country, model, year, mileage_km, color):
        self.making_country = making_country
        self.model = model
        self.year = year
        self.mileage_km = mileage_km
        self.color = color

    def drive(self, distance_km, velocity_ms):
        self.mileage_km += distance_km
        self.velocity_ms = velocity_ms

    def stop(self):
        self.velocity_ms = 0

lada_sport = Car("Russia", "Vesta", 2020, 5000, "Red")
lada_sport.drive(50, 100)
lada_sport.stop()
lada_sport = None

# добавил завершение работы с переменной lada_sport, хранящая ссылку на объект Car


# №7
# неверный вариант
girl_name = str(input("Введите имя"))
age_of_girl = "25"
living_city = "New York"
occupation_of_girl = "engineer"

print("Dialog_message:")
print("Hello, my name is " + girl_name + ". I am " + age_of_girl + " years old, living in " + living_city +
      ". I work as an " + occupation_of_girl + ".")

# верный вариант
girl_name = str(input("Введите имя"))
age_of_girl = "25"
living_city = "New York"
occupation_of_girl = "engineer"

print("Dialog_message:")
print("Hello, my name is " + girl_name + ". I am " + age_of_girl + " years old, living in " + living_city +
      ". I work as an " + occupation_of_girl + ".")

girl_name = "ERROR"
age_of_girl = "ERROR"
living_city = "ERROR"
occupation_of_girl = "ERROR"

# завершил работу с текстовыми переменными, присвоив им значение "ERROR"


# №8
# неверный вариант
class Book:
    def __init__(self, title, author, publication_year, number_of_pages):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.number_of_pages = number_of_pages
        self.current_page = 0

    def flip_page(self):
        self.current_page += 1

    def set_page(self, user_page):
        self.current_page = user_page

three_musketeers = Book("Three_Musketeers", "Aleks Duma", 1844, 650)
three_musketeers.set_page(100)

# верный вариант
class Book:
    def __init__(self, title, author, publication_year, number_of_pages):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.number_of_pages = number_of_pages
        self.current_page = 0

    def flip_page(self):
        self.current_page += 1

    def set_page(self, user_page):
        self.current_page = user_page

three_musketeers = Book("Three_Musketeers", "Aleks Duma", 1844, 650)
three_musketeers.set_page(100)
three_musketeers.flip_page()

three_musketeers = None

# завершил работу с переменной three_musketeers


# №9
# неверный вариант
heat_flux_W = [1.2, 3.0, 1.0, 9.0]
x_nozzle_coorinate_m = [0.1, 0.2, 0.3, 0.4]
diameter_nozzle_m = [0.5, 0.3, 0.6, 0.9]
heat_flux_throat_W = 10
throat_length_m = 100
throat_diameter_m = 1
zavesa_cooling = 90

CONSTANT_OF_BOLTZMANN = 5.67
temper_of_chamber_K = 3000
DEGREE_OF_BLACKNESS = 0.9

radiant_flux_W = degree_of_blackness*c0*(temper_of_chamber_K/100)**4

for i in range(len(x_nozzle_coorinate_m)):
    is_chamber = x_nozzle_coorinate_m[i] < 0.05
    is_between_chamber_throat = x_nozzle_coorinate_m[i] < throat_length_m and diameter_nozzle_m[i] >= 1.2 * throat_diameter_m
    if is_chamber:
        heat_flux_W.append(heat_flux_throat_W / 2)
    elif is_between_chamber_throat and zavesa_cooling > 100:
        heat_flux_W.append(heat_flux_throat_W * 3)
    elif is_between_chamber_throat:
        heat_flux_W.append(heat_flux_throat_W * 10)

# верный вариант
CONSTANT_OF_BOLTZMANN = 5.67
temper_of_chamber_K = 3000
DEGREE_OF_BLACKNESS = 0.9

radiant_flux_W = degree_of_blackness*c0*(temper_of_chamber_K/100)**4

heat_flux_W = [1.2,3.0,1.0,9.0]
x_nozzle_coorinate_m = [0.1,0.2,0.3,0.4]
diameter_nozzle_m = [0.5,0.3,0.6,0.9]
heat_flux_throat_W = 10
throat_length_m = 100
throat_diameter_m = 1
zavesa_cooling = 90
for i in range(len(x_nozzle_coorinate_m)):
    is_chamber = x_nozzle_coorinate_m[i] < 0.05
    is_between_chamber_throat = x_nozzle_coorinate_m[i] < throat_length_m and diameter_nozzle_m[i] >= 1.2 * throat_diameter_m
    if is_chamber:
        heat_flux_W.append(heat_flux_throat_W / 2)
    elif is_between_chamber_throat and zavesa_cooling > 100:
        heat_flux_W.append(heat_flux_throat_W * 3)
    elif is_between_chamber_throat:
        heat_flux_W.append(heat_flux_throat_W * 10)

# инициализировал переменные, которые будут использованы в цикле перед саими циклом, а не перед промежуточными вычислениями


# №10
# неверный вариант
number_of_sections_max = 100
diameter_chamber_m = 1
diameter_nozzle_list_m = [0.5,0.3,0.6,0.9]
number_of_Mach = 0.001
cur_gas_dyn_func_q = 0
subsonic_nozzle_part_m = 0.3

for i in range(number_of_sections_max):
    if i <= subsonic_nozzle_part_m:
        cur_gas_dyn_func_q = (diameter_chamber_m / diameter_nozzle_list_m[i]) ** 2 / 2 + number_of_Mach
    number_of_Mach += 0.001

print("Всего сечений для разбиений: ", i)

# верный вариант
number_of_sections_max = 100
diameter_chamber_m = 1
diameter_nozzle_list_m = [0.5,0.3,0.6,0.9]
number_of_Mach = 0.001
cur_gas_dyn_func_q = 0
subsonic_nozzle_part_m = 0.3

for i in range(number_of_sections_max):
    if i <= subsonic_nozzle_part_m:
        cur_gas_dyn_func_q = (diameter_chamber_m / diameter_nozzle_list_m[i]) ** 2 / 2 + number_of_Mach
    number_of_Mach += 0.001

print("Всего сечений для разбиений: ", number_of_sections_max)
# прекратил использование счетчика цикла i за пределами цикла в функции print() по выводу максимального количества секций

# №11
# неверный вариант
max_digit = 0
input_user_number = int(input("Введите число для нахождения самой большой цифры в нем: "))

while input_user_number > 0:
    digit_of_number = input_user_number % 10
    if digit_of_number > max_digit:
        max_digit = digit_of_number
    input_user_number //= 10

# верный вариант
input_user_number = int(input("Введите число для нахождения самой большой цифры в нем: "))
max_digit = 0
while input_user_number > 0:
    digit_of_number = input_user_number % 10
    if digit_of_number > max_digit:
        max_digit = digit_of_number
    input_user_number //= 10
# переместил инициализацию переменной максимальной цифры max_digit непосредственно к циклу


# №12
# неверный вариант
day = 1

x = float(input("Введите дистанцию, которую спортсмен пробежал в первый день (в км): "))
y = float(input("Введите необходимую дистанцию спортсмена (в км): "))

total_distance = x

user_name = str(input("Введите имя пользователя"))
print("Hello, my name is " + user_name)

while total_distance < y:
    x *= 1.1
    total_distance += x
    day += 1

# верный вариант
user_name = str(input("Введите имя пользователя"))
print("Hello, my name is " + user_name)

x = float(input("Введите дистанцию, которую спортсмен пробежал в первый день (в км): "))
y = float(input("Введите необходимую дистанцию спортсмена (в км): "))

total_distance = x
day = 1

while total_distance < y:
    x *= 1.1
    total_distance += x
    day += 1

# переместил переменную day и переменную условия цикла total_distance ближе к циклу

# №13
# неверный вариант
def selection_sort(numbers_list):
    length_list = len(numbers_list)
    for i in range(length_list):
        min_index = i
        for j in range(i + 1, length_list):
            if numbers_list[j] < numbers_list[min_index]:
                min_index = j
        numbers_list[i], numbers_list[min_index] = numbers_list[min_index], numbers_list[i]
    return numbers_list

# верный вариант
def selection_sort(numbers_list):
    length_list = len(numbers_list)
    for i in range(length_list):
        min_index = i
        for j in range(i + 1, length_list):
            if numbers_list[j] < numbers_list[min_index]:
                min_index = j
        assert all(numbers_list[k] <= numbers_list[k + 1] for k in range(i))
        numbers_list[i], numbers_list[min_index] = numbers_list[min_index], numbers_list[i]
    return numbers_list

# в функцию сортировки добавил инвариант проверки упорядоченности после каждого обмена значений


# №14
# неверный вариант
class Sales:
    def __init__(self, product_name, quantity, price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price


sweet_sale = Sales("Конфеты", -10, 5)

# верный вариант
class Sales:
    def __init__(self, product_name, quantity, price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.validate_quantity()

    def validate_quantity(self):
        if self.quantity < 0:
            raise ValueError("Количество проданных товаров не может быть отрицательным")
try:
    sweet_sale = Sales("Конфеты", 10, 5)
except ValueError as e:
    print(f"Ошибка: {e}")

# использовал метод validate_quantity() в качестве инварианта
# для запуска его в конструкторе и проверке того, что количество проданных товаров не отрицательно


# №15
# неверный вариант
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw_cash(self, amount):
        self.balance -= amount

account = BankAccount(100)
account.withdraw_cash(200)

# верный вариант
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.check_balance()

    def withdraw_cash(self, amount):
        self.balance -= amount
        self.check_balance()

    def check_balance(self):
        if self.balance < 0:
            raise ValueError("Balance cannot be negative")

account = BankAccount(100)

try:
    account.withdraw_cash(200)
except ValueError as e:
    print("Ошибка!")
# использовал метод check_balance() для проверки инварианта, что баланс на счете не отрицательный, сделал обработку
# исключения при работе с объектом

