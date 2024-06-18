# №1
# неправильный вариант
max_bike_speed_kmh = 10
def check_speed(current_speed_kmh):
    if current_speed_kmh <= max_bike_speed_kmh:
        print("Скорость в пределах допустимого значения")
    else:
        print("Превышение допустимой скорости")

# правильный вариант
MAX_BIKE_SPEED_KMH = 10
def check_speed(current_speed_kmh):
    if current_speed_kmh <= MAX_BIKE_SPEED_KMH:
        print("Скорость в пределах допустимого значения")
    else:
        print("Превышение допустимой скорости")

# переименовал константу MAX_BIKE_SPEED_KMH согласно соглашению об именовании констант


# №2
# неправильный вариант
import second_asd.second_asd  as inlet
from random import randint
import unittest

class DelTest(unittest.TestCase):
    def test_delete_from_tail_true(self):
        list_link = inlet.LinkedList2()
        reference_list = []
        for i in range(100000):
            number_for_add = randint(0, 2 ** 30)
            list_link.add_in_tail(inlet.Node(number_for_add))
            reference_list.append(number_for_add)
        for j in range(100000):
            number_for_delete = 2 ** 30 + 1
            list_link.add_in_tail(inlet.Node(number_for_delete))
        list_link.delete(number_for_delete, True)
        self.assertEqual(reference_list, list_link.to_list())

# правильный вариант
import second_asd.second_asd  as inlet
from random import randint
import unittest

class DelTest(unittest.TestCase):
    def test_delete_from_tail_true(self):
        list_link = inlet.LinkedList2()
        reference_list = []
        TEST_COUNT = 100000
        for i in range(TEST_COUNT):
            number_for_add = randint(0, 2 ** 30)
            list_link.add_in_tail(inlet.Node(number_for_add))
            reference_list.append(number_for_add)
        for j in range(TEST_COUNT):
            number_for_delete = 2 ** 30 + 1
            list_link.add_in_tail(inlet.Node(number_for_delete))
        list_link.delete(number_for_delete, True)
        self.assertEqual(reference_list, list_link.to_list())

# в данном примере представлен тест метода delete для связного списка;
# использовал константу TEST_COUNT в качестве счетчика цикла вместо магического числа 100000


# №3
# неправильный вариант
vers = "1.0.0"
class MathOperations:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def add(self):
        return self.first_number + self.second_number

    def subtract(self):
        return self.first_number - self.second_number


if __name__ == "__main__":
    number_of_green_apple = 10
    number_of_red_apple = 5
    math_ops = MathOperations(number_of_green_apple, number_of_red_apple)
    print(f"Версия программы: {vers}")
    print(f"Addition: {math_ops.add()}")
    print(f"Subtraction: {math_ops.subtract()}")

# правильный вариант
__version__ = "1.0.0"
class MathOperations:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def add(self):
        return self.first_number + self.second_number

    def subtract(self):
        return self.first_number - self.second_number


if __name__ == "__main__":
    number_of_green_apple = 10
    number_of_red_apple = 5
    math_ops = MathOperations(number_of_green_apple, number_of_red_apple)
    print(f"Версия программы: {__version__}")
    print(f"Addition: {math_ops.add()}")
    print(f"Subtraction: {math_ops.subtract()}")

# использовал константу Дандера __version__ для обозначения версии программы


# №4
# неправильный вариант
def read_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    return file_content

def write_file(file_path, file_content):
    with open(file_path, 'w') as file:
        file.write(file_content)

# правильный вариант
DEFAULT_FILE_PATH = 'file.txt'

def read_file(file_path=DEFAULT_FILE_PATH):
    with open(file_path, 'r') as file:
        file_content = file.read()
    return file_content

def write_file(file_content, file_path=DEFAULT_FILE_PATH):
    with open(file_path, 'w') as file:
        file.write(file_content)

# использование константы DEFAULT_FILE_PATH для значения по умолчанию имени файла для функций считывания и записи в файл


# №5
# неправильный вариант
def calculate_area(diameter):
    return 3.14 * diameter ** 2 / 4

# правильный вариант
class Constants:
    __slots__ = ['PI', 'GRAVITY']
    def __init__(self):
        self.PI = 3.14159
        self.GRAVITY = 9.81

constants = Constants()
def calculate_area(diameter):
    return constants.PI * diameter ** 2 / 4

# определил константы в специальном атрибуте класса __slots__ вместо того, чтобы использовать магическое число для
# оперделения функции расчета площади круга


# №6
# неправильный вариант
gravity = 9.81
def calculate_fall_distance(time):
    distance = 0.5 * gravity * time**2
    return distance

# правильный вариант
class ConstantsNamespace:
    @property
    def GRAVITY(self):
        return 9.81

constants = ConstantsNamespace()

def calculate_fall_distance(time):
    distance = 0.5 * constants.GRAVITY * time**2
    return distance

# переименовал константу GRAVITY согласно соглашению об именовании констант;
# использовал декоратор @property в классе для константы, чтобы нельзя было установить её значение


# №7
# неправильный вариант
def collect_coin(score):
    return score + 10

# правильный вариант
POINTS_PER_COIN = 10

def collect_coin(score):
    return score + POINTS_PER_COIN

# показывается пример функции подсчета очков, где используется константа;
# заменил магическое число константой


# №8
# неправльный вариант
light_speed = 299792458
mass_kg = float(input("Введите массу объекта (в килограммах): "))
energy_of_particles_J = mass_kg * light_speed ** 2

# правильный вариант
from dataclasses import dataclass

@dataclass(frozen=True)
class ConstantsNamespace:
    SPEED_OF_LIGHT_MS = 299792458

constants = ConstantsNamespace()

mass_kg = float(input("Введите массу объекта (в килограммах): "))
energy_of_particles_J = mass_kg * constants.SPEED_OF_LIGHT_MS ** 2
# переименовал константу SPEED_OF_LIGHT_MS согласно соглашению об именовании констант;
# использовал декоратор @dataclass, который помечает класс как класс данных;
# также, используя frozen аргумент, пометил класс как неизменяемый, чтобы было невозмжно изменить аргументы класса


# №9
# неправильный вариант
def draw_rectangle(draw_color):
    print(f"Рисуется {draw_color} прямоугольник")

# правильный вариант
class ConstantsNamespace:
    COLOR = "red"
    def __setattr__(self, name, value):
        raise AttributeError(f"can't reassign constant '{name}'")

constants = ConstantsNamespace()

def draw_rectangle(draw_color=constants.COLOR):
    print(f"Рисуется {draw_color} прямоугольник")

# используетстя константа для инициализации переменной функции черчения прямоугольника определенным цветом;
# для задания констант используются поле класса ConstantsNamespace, также переопределяется метод __setattr__()
# для назначения атрибута класса; если будет попытка назначения атрибута класса, то будет сгенерированно исключение


# №10
# неверный вариант
def calculate_final_velocity(initial_velocity_ms, time_s):
    final_velocity_ms = initial_velocity_ms + 2.5 * time_s
    return final_velocity_ms

initial_velocity_ms = float(input("Введите начальную скорость: "))
time_s = float(input("Введите время: "))

final_velocity_ms = calculate_final_velocity(initial_velocity_ms, time_s)

# верный вариант
def Startup():
    global GRAVITY
    global ACCELERATION
    GRAVITY = 9.81
    ACCELERATION = 2.5

def calculate_final_velocity(initial_velocity_ms, time_s):
    final_velocity_ms = initial_velocity_ms + ACCELERATION * time_s
    return final_velocity_ms

Startup()

initial_velocity_ms = float(input("Введите начальную скорость: "))
time_s = float(input("Введите время: "))

final_velocity_ms = calculate_final_velocity(initial_velocity_ms, time_s)

# в данном примере проводится расчет финальной скорости, с помощью соответствующей функции;
# было заменено магическое число 2.5 на константу, которая инициализируется в функции Startup() и помечается
# как global, чтобы она была доступна в других частях программы


# №11
# неверный вариант
min_sale_percent = 5
total_price_usd = float(input("Введите полную цену: "))
end_cost_usd = min_sale_percent * total_price_usd

# правильный вариант
from dataclasses import dataclass

@dataclass(frozen=True)
class ConstantsNamespace:
    MIN_SALE_PERCENT = 5

constants = ConstantsNamespace()

total_price_usd = float(input("Введите полную цену: "))
end_cost_usd = total_price_usd * constants.MIN_SALE_PERCENT
# переименовал константу MIN_SALE_PERCENT согласно соглашению об именовании константы минимальной скидки покупателю;
# использовал декоратор @dataclass, который помечает класс как класс данных;
# также, используя frozen аргумент, пометил класс как неизменяемый, чтобы было невозмжно изменить аргументы класса


# №12
# неверный вариант
diameter_list = [0] * 50
inlet_velocity_ms = 1
for i in range(50):
    if inlet_velocity_ms > 0:
        diameter_list[i] += 1

for i in range(50):
    print(diameter_list[i])

# верный вариант
def Startup():
    global LENGTH_OF_DIAMETER_LIST
    LENGTH_OF_DIAMETER_LIST = 50

Startup()

diameter_list = [0] * LENGTH_OF_DIAMETER_LIST
inlet_velocity_ms = 1
for i in range(LENGTH_OF_DIAMETER_LIST):
    if inlet_velocity_ms > 0:
        diameter_list[i] += 1

for i in range(LENGTH_OF_DIAMETER_LIST):
    print(diameter_list[i])

# избавился от магического числа, харакетризующую размер массива, путём введения константы LENGTH_OF_DIAMETER_LIS,
# которая была помещена в функцию Startup для инициализации


