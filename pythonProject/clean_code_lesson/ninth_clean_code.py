# №1
# неправильный вариант
def compute_capacity(temper_of_coller_K):
    pass

def compute_alpha_cooler(Nusselt_number, temper_of_coller_K, hydrouic_diameter_m):
    alpha_cooler = Nusselt_number * compute_capacity(temper_of_coller_K) / hydrouic_diameter_m
    return alpha_cooler

# правильный вариант
def compute_capacity(temper_of_coller_K):
    pass

def compute_alpha_cooler(Nusselt_number, temper_of_coller_K, hydrouic_diameter_m):
    try:
        alpha_cooler = Nusselt_number * compute_capacity(temper_of_coller_K) / hydrouic_diameter_m
        return [alpha_cooler, 0]
    except ZeroDivisionError:
        return [1, 1]
# учёл появление нулевого знаменателя в функции compute_alpha_cooler и ввёл обработку исключения;
# в данной функции возвращается список, второй элемент которого - индекс наличия или отсутствия ошибки

# №2
# неправильный вариант
def compute_sum_of_layers(number_of_top_layers, number_of_bot_layers):
    sum_of_layers = number_of_top_layers + number_of_bot_layers
    return sum_of_layers

# правильный вариант
import sys
def check_overflow(is_overflow_number):
    if is_overflow_number > sys.maxsize or is_overflow_number < -sys.maxsize-1:
        return True
    return False

def compute_sum_of_layers(number_of_top_layers, number_of_bot_layers):
    sum_of_layers = number_of_top_layers + number_of_bot_layers
    if check_overflow(sum_of_layers):
        return [sum_of_layers, 0]
    return [1, 1]
# при выполнении сложение двух слоев в функции compute_sum_of_layers, сделал проверку переполнения целого числа,
# добавив метод check_overflow

# №3
# неправильный вариант
def calculate_betta(capacity_cooler, adiabatic_koefficient):
    return capacity_cooler * ((adiabatic_koefficient - 1) // (adiabatic_koefficient + 1))

# правильный вариант
def check_integer_division(is_integer_number):
    if type(is_integer_number) == int:
        return True
    return False

def calculate_betta(capacity_cooler, adiabatic_koefficient):
    betta =  capacity_cooler * (adiabatic_koefficient - 1) // (adiabatic_koefficient + 1)
    if check_integer_division(betta):
        return [betta, 0]
    return [1, 1]
# произвожу целочисленное деление в функции calculate_betta и провожу проверку, что результат целочисленный
# в функции check_integer_division, сравнивая тип числа

# №4
# неправильный вариант
import sys
def check_overflow(is_overflow_number):
    if is_overflow_number > sys.maxsize or is_overflow_number < -sys.maxsize-1:
        return True
    return False

def compute_sum_of_layers(number_of_top_layers, number_of_bot_layers):
    sum_of_layers = number_of_top_layers + number_of_bot_layers
    if check_overflow(sum_of_layers):
        return [sum_of_layers, 0]
    return [1, 1]

wall_layer_pump = 10000
wall_layer_nozzle = 900
wall_lay_pump_nozzle_sum = compute_sum_of_layers(wall_layer_nozzle, wall_layer_pump)

if(wall_lay_pump_nozzle_sum[1] == 0):
    print(f"Суммарное количество пограничного слоя насоса {wall_layer_pump} " \
                   f"и сопла {wall_layer_nozzle} равна {wall_lay_pump_nozzle_sum[0]} и не вызывает пеерполнения")

# правильный вариант
import sys
def check_overflow(is_overflow_number):
    if is_overflow_number > sys.maxsize or is_overflow_number < -sys.maxsize-1:
        return True
    return False

def compute_sum_of_layers(number_of_top_layers, number_of_bot_layers):
    sum_of_layers = number_of_top_layers + number_of_bot_layers
    if check_overflow(sum_of_layers):
        return [sum_of_layers, 0]
    return [1, 1]

wall_layer_pump = 10000
wall_layer_nozzle = 900
wall_lay_pump_nozzle_sum = compute_sum_of_layers(wall_layer_nozzle, wall_layer_pump)

OVERFLOW_MESSAGE = f"Суммарное количество пограничного слоя насоса {wall_layer_pump} " \
                   f"и сопла {wall_layer_nozzle} равна {wall_lay_pump_nozzle_sum[0]} и не вызывает пеерполнения"
if(wall_lay_pump_nozzle_sum[1] == 0):
    print(OVERFLOW_MESSAGE)
# использовал строковую константу OVERFLOW_MESSAGE для информирования об отсутствии переполнения и разместил её рядом
# с местом применения вместо того, чтобы использовать магическую строку в неправильном варианте

# №5
# неправильный вариант
LANGUAGE = 'ru'
Hello_world = 'Hello, World!'
Hello_world_ru = 'Привет, Мир!'
if LANGUAGE == 'ru':
    Hello_world = Hello_world_ru

# правильный вариант
import gettext

locale_directory = 'C:\\Documents'
gettext.bindtextdomain('my_program', locale_directory)
gettext.textdomain('my_program')
LANGUAGE = 'es'  # испанский язык
lang_translations = gettext.translation('my_program', locale_directory, languages=[LANGUAGE])
lang_translations.install()
print(_("Hello, World!"))
# в неправильном варианте использовал неверную интернационализацию переменной Hello_world;
# в правильном варианте реализовал интернационализацию текстовых сообщений с помощью модуля gettext;
# для этого создаются специальные файлы в локальной директории, где хранятся файлы сообщений на разных языках

# №6
# неправильный вариант
heat_flux_W = []
x_nozzle_coorinate_m = []
diameter_nozzle_m = []
heat_flux_throat_W = 10
throat_length_m = 100
throat_diameter_m = 1
zavesa_cooling = 90

for i in range(len(x_nozzle_coorinate_m)):
    if x_nozzle_coorinate_m[i] < 0.05:
        heat_flux_W.append(heat_flux_throat_W / 2)
    elif x_nozzle_coorinate_m[i] < throat_length_m and diameter_nozzle_m[i] >= 1.2 * throat_diameter_m and zavesa_cooling > 100:
        heat_flux_W.append(heat_flux_throat_W * 3)
    elif x_nozzle_coorinate_m[i] < throat_length_m and diameter_nozzle_m[i] >= 1.2 * throat_diameter_m:
        heat_flux_W.append(heat_flux_throat_W * 10)

# правильный вариант
heat_flux_W = []
x_nozzle_coorinate_m = []
diameter_nozzle_m = []
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
# использовал логические переменные для облегчения редактирования и восприятия условия в примере
# расчета теплового потока по длине сопла


# №7
# неправильный вариант
temperature_room_K = 25
wetness_room_gkg = 50
is_light_on = True
wind_velocity_ms = 1
is_open_door = True
is_fire = False

if (temperature_room_K > 20 and (wetness_room_gkg < 60 or is_light_on) and (wind_velocity_ms > 3 and is_open_door) or is_fire):
    print("Пожара не будет")

# правильный вариант
temperature_room_K = 25  # Температура воздуха
wetness_room_gkg = 50    # Уровень влажности
is_light_on = True  # Освещенность
wind_velocity_ms = 1   # Движение в комнате
is_open_door = True    # Дверь открыта
is_fire = False   # Пожарная тревога

is_normal_condition = wetness_room_gkg < 60 or is_light_on
is_normal_temperature = temperature_room_K > 20
is_danger_condition = (wind_velocity_ms > 3 and is_open_door) or is_fire
if (is_normal_temperature and is_normal_condition and is_danger_condition):
    print("Пожара не будет")
# использовал логические переменные для облегчения редактирования и восприятия условия в примере
# проверки помещения не пожаробезопасность


# №8
# неправильный вариант
new_bottle_volume_m3 = 0.1 + 0.2
old_bottle_volume_m3 = 0.3

if new_bottle_volume_m3 == old_bottle_volume_m3:
    print("Числа равны")

# правильный вариант
new_bottle_volume_m3 = 0.1 + 0.2
old_bottle_volume_m3 = 0.3
epsilon_for_equal = 1e-10

if abs(new_bottle_volume_m3) - abs(old_bottle_volume_m3) < epsilon_for_equal:
    print("Числа равны")
# првиеден пример неправильной и правильной проверки двух вещественных чисел на равенство;
# в правильном варианте проверяется является ли "расстояние" между числами меньше наперед заданной точности


# №9
# неправильный вариант
new_bottle_volume_m3 = 0.1 + 0.2
print(f"Объем новой бутылки составляет {new_bottle_volume_m3} литра")
# правильный вариант
new_bottle_volume_m3 = 0.1 + 0.2
print(f"Объем новой бутылки составляет {round(new_bottle_volume_m3,2)} литра")
# учел особенности вычисления чисел с плавающей точкой и применил округление для удобного представления


# №10
# неправильный вариант
class Human:
    def __init__(self):
        self.age = 17.4
        self.weight = 55.1
        self.height = 170.01

# правильны вариант
class Human:
    def __init__(self):
        self.age = 17
        self.weight = 55
        self.height = 170
# использовал целочисленные переменные вместо вещественных, т.к. для типа Human смысловая нагрузка этих атрибутов такой же

# №11
# неправильный вариант
import sys
def check_overflow(is_overflow_number):
    if is_overflow_number > sys.maxsize or is_overflow_number < -sys.maxsize-1:
        return True
    return False

def compute_sum_of_layers(number_of_top_layers, number_of_bot_layers):
    sum_of_layers = number_of_top_layers + number_of_bot_layers - number_of_top_layers * 5
    if check_overflow(sum_of_layers):
        return [sum_of_layers, 0]
    return [1, 1]

# правильный вариант
import sys

def check_overflow(is_overflow_number):
    if is_overflow_number > sys.maxsize or is_overflow_number < -sys.maxsize-1:
        return True
    return False

def compute_sum_of_layers(number_of_top_layers, number_of_bot_layers):
    additional_term = number_of_top_layers * 5
    assert additional_term > sys.maxsize or additional_term < -sys.maxsize-1
    sum_of_layers = number_of_top_layers + number_of_bot_layers - additional_term
    if check_overflow(sum_of_layers):
        return [sum_of_layers, 0]
    return [1, 1]
# сделал дополнительную проверку промежуточных вычислений в выражении на переполнение в функции compute_sum_of_layers
# с помощью добавления assert; конечный результат выражения проверяю на переполнение с помощью функции check_overflow


# №12
# неправильный вариант
def compute_Reynold_number(mass_velocity_kgm2, hydroulic_diameter_m, cooler_density, viscosity_cooler):
    velocity_cooler_ms = mass_velocity_kgm2 / cooler_density
    Reynolds_number = velocity_cooler_ms * hydroulic_diameter_m / viscosity_cooler
    return Reynolds_number

# правильный вариант
def compute_Reynold_number(mass_velocity_kgm2, hydroulic_diameter_m, cooler_density, viscosity_cooler):
    assert cooler_density != 0
    velocity_cooler_ms = mass_velocity_kgm2 / cooler_density
    assert viscosity_cooler != 0
    Reynolds_number = velocity_cooler_ms * hydroulic_diameter_m / viscosity_cooler
    return Reynolds_number
# выполнил проверку на неравенство нулю знаменателя с помощью assert

