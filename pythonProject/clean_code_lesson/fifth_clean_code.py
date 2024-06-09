'''
3.1

class DanceRobot - class RobotDancer
# класс танцующего робота; убрал глагол из названия

class FlyingPlane - class Plane
# класс летящего самолета; убрал глагол из названия и убрал слово летящий

class CodingProgrammer - class ProgrammerCoder
# класс кодирующего прогарммиста; убрал глагол из названия

class DesignEngine - class Engine
#  класс проектирования двигателя; убрал глагол из названия

class CalculateTurboPump - class TurboPump
# класс расчета турбонасоса; убрал глагол из названия
'''

'''
3.2
'''
# примеры с методами

# №1
# неправильный вариант
class Bus:
    def __init__(self):
        self.velocity_of_bus_ms = 10

    def stop(self):
        self.velocity_of_bus_ms = 0

class Car:
    def __init__(self):
        self.velocity_of_car_ms = 100

    def stop(self):
        self.velocity_of_car_ms = 0

family_car = Car()
big_car = Car()

# правильный вариант
class Bus:
    def __init__(self):
        self.velocity_of_bus_ms = 10

    def stop_bus(self):
        self.velocity_of_bus_ms = 0


class Car:
    def __init__(self):
        self.velocity_of_car_ms = 100

    def stop_car(self):
        self.velocity_of_car_ms = 0
# конкретизировал метод stop() сброса скорости до нуля для класса автобуса и класса автомобиля

# №2
# неправильный вариант
class UserHero:
    def __init__(self):
        self.velocity_of_hero_ms = 0

    def run(self, speed):
        self.velocity_of_hero_ms = speed


class Dwarf:
    def __init__(self):
        self.velocity_of_dwarf = 0

    def run(self, run_speed_ms):
        self.velocity_of_dwarf = run_speed_ms

# правильный вариант
class UserHero:
    def __init__(self):
        self.velocity_of_hero = 0

    def run_user(self, run_speed_ms):
        self.velocity_of_hero = run_speed_ms


class Dwarf:
    def __init__(self):
        self.velocity_of_dwarf = 0

    def run_dwarf(self, run_speed_ms):
        self.velocity_of_dwarf = run_speed_ms
# конкретизировал метод run() установки скорости для класса UserHero и класса Dwarf

# №3
# неправильный вариант
class Rectangle:
    def __init__(self):
        self.square_of_rectangle_m2 = 0

    def get_square(self):
        return self.square_of_rectangle_m2


class Triangle:
    def __init__(self):
        self.square_of_triangle_m2 = 0

    def get_square(self):
        return self.square_of_triangle_m2

# правильный вариант
class Rectangle:
    def __init__(self):
        self.square_of_rectangle_m2 = 0

    def get_rectangle_square(self):
        return self.square_of_rectangle_m2


class Triangle:
    def __init__(self):
        self.square_of_triangle_m2 = 0

    def get_triangle_square(self):
        return self.square_of_triangle_m2

# конкретизировал метод получения площади для классов треугольник и прямугольника


# №4
# неправильный вариант
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def clean(self):
        self.head = None
        self.tail = None


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class Node_dum(Node):
    def __init__(self):
        super().__init__(None)

class LinkedList2:
    def __init__(self):
        self.dummy = Node_dum()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def clean(self):
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

# правильный вариант
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def clean_lincked_list(self):
        self.head = None
        self.tail = None


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class Node_dum(Node):
    def __init__(self):
        super().__init__(None)

class LinkedList2:
    def __init__(self):
        self.dummy = Node_dum()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def clean_round_list(self):
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

# конкретизировал метод clean() очищения списков для классов связного списка и связного списка с dummy узлом

# №5
# неправильный вариант
class Text:
    def __init__(self):
        self.color_of_text = 0

    def get_color(self):
        return self.color_of_text


class Figure:
    def __init__(self):
        self.color_of_figure = 0

    def get_color(self):
        return self.color_of_figure

# правильный вариант
class Text:
    def __init__(self):
        self.color_of_text = 0

    def get_text_color(self):
        return self.color_of_text


class Figure:
    def __init__(self):
        self.color_of_figure = 0

    def get_figure_color(self):
        return self.color_of_figure

# конкретизировал метод get_color() возвращения цвета для классов текста и фигуры


# №6
# неправильный вариант
class Schedule:
    def __init__(self):
        self.event_day = 0

    def get_day(self):
        return self.event_day


class Holiday:
    def __init__(self):
        self.day_of_holiday = 0

    def get_day(self):
        return self.day_of_holiday

# правильный вариант
class Schedule:
    def __init__(self):
        self.event_day = 0

    def get_shedule_day(self):
        return self.event_day


class Holiday:
    def __init__(self):
        self.day_of_holiday = 0

    def get_holiday_day(self):
        return self.day_of_holiday

# конкретизировал метод возвращения дня для классов расписания и праздник


# №7
# неправильный вариант
class Furniture:
    def __init__(self):
        self.material_of_furniture = 0

    def get_material(self):
        return self.material_of_furniture


class Clothes:
    def __init__(self):
        self.material_of_clothes = 0

    def get_material(self):
        return self.material_of_clothes

# правильный вариант
class Furniture:
    def __init__(self):
        self.material_of_furniture = 0

    def get_furniture_material(self):
        return self.material_of_furniture


class Clothes:
    def __init__(self):
        self.material_of_clothes = 0

    def get_clothes_material(self):
        return self.material_of_clothes

# конкретизировал метод получения материала дня для классов мебель и одежда

# примеры с объектами

# №1
# неправильный вариант
figure_rectangle = Rectangle(), figure_with_four_angle = Rectangle()
# правильный вариант
side_rectangle = Rectangle(), top_rectangle = Rectangle()
# в неправильном варианте создается объект с именем прямоугольник и фигура с черьмя углами,
# из чего не будет понятно, является ли она прямоугольником или нет;
# в правильном вариант в обоих переменных используется слово rectangle и подчеркивается область их применения
# (сбоку, сверху)

# №2
# неправильный вариант
zip_file_manager = File(), txt_file_controller = File()
# правильный вариант
zip_file_manager = File(), txt_file_manager = File()
# использовал единую терминологию для разных переменных

# №3
# неправильный вариант
init_device_driver = Code(), last_device_code = Code()
# правильный вариант
init_device_driver = Code(), last_device_driver = Code()
# переменные подпрограмм для устройства

# №4
# неправильный вариант
translator_eng_ru = Translator(), interpreter_eng_esp = Translator()
# правильный вариант
translator_eng_ru = Translator(), translator_eng_esp = Translator()
# переменные типа переводчик

# №5
# неправильный вариант
driver_Vasya = Driver(), chauffeur_Petya = Driver()
# правильный вариант
driver_Vasya = Driver(), driver_Petya = Driver()
# объекты класса водитель

# №6
# неправильный вариант
programmer_c_sharp = Programmer(), coder_fortran = Programmer()
# правильный вариант
programmer_c_sharp = Programmer(), programmer_fortran = Programmer()
# объекты класса программист

# №7
# неправильный вариант
aircraft_engineer = Staff(), car_mechanic = Staff()
# правильный вариант
aircraft_engineer = Staff(), car_engineer = Staff()
# объекты класса персонал
