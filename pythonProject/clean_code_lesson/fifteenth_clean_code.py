# №1
# вариант до
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

# вариант после
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__odometer_reading = 0
        self.__fuel_level_L = 0

    # метод вождения автомобиля с увеличением показаний одоментра и уменьшением уровян топлива
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

# согласно п.1 вставил информативные комментарии к методу drive()


# №2
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

    def take_off(self):
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

    # посадка пассажирова в самолёт; проверка количества вошедших пассажиров в самолет на превышение посадочных мест
    def board_passengers(self, number_of_passengers):
        if self.current_passengers + number_of_passengers <= self.capacity:
            self.current_passengers += number_of_passengers
            print(f"Посажено {number_of_passengers} пассажиров. Всего пассажиров: {self.current_passengers}")
        else:
            print("Недостаточно места для всех пассажиров.")

    # взлёт самолёта, проверка возможности взлёта и установка флага
    def take_off(self):
        if self.fuel_level_kg > 0 and self.current_passengers > 0:
            self.is_flying = True
            print(f"Самолёт {self.model} взлетел.")
        else:
            print("Не хватает топлива или нет пассажиров для взлёта.")

# согласно п.1 вставил информативные комментарии к методам класса


# №3
# вариант до
import pandas as pd

data = pd.read_csv('dataset.csv')
X = data.drop(columns=['target'])
y = data['target']

# вариант после
import pandas as pd

# Загружаем данные и собираемся разделить их на признаки и целевые значения
data = pd.read_csv('dataset.csv')
X = data.drop(columns=['target'])
y = data['target']


# согласно п.2 записал комментарий представления намерений



# №4
# вариант до
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier

pca = PCA(n_components=0.95)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train_pca, y_train)

# вариант после
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier

# Собираемся уменьшить размерность данных с помощью PCA, чтобы выявить наиболее важные признаки
pca = PCA(n_components=0.95)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

# Собираемся обучить модель случайного леса для классификации
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train_pca, y_train)


# согласно п.2 записал комментарий представления намерений


# №5
# вариант до

import init_file

acceleration = 2
time = 5

distance = init_file.Vel * time + 0.5 * acceleration * time ** 2
average_speed = distance / time
final_position = init_file.Vel * time + 0.5 * acceleration * time ** 2
final_speed = init_file.Vel + acceleration * time

# вариант после

import init_file

initial_speed = init_file.Vel  # начальная скорость мотоцикла
acceleration = 2
time = 5

distance = initial_speed * time + 0.5 * acceleration * time ** 2
average_speed = distance / time
final_position = initial_speed * time + 0.5 * acceleration * time ** 2
final_speed = initial_speed + acceleration * time


# согласно п.3 вставил комментарий прояснение



# №6
# вариант до
import math_operators

first_number_for_adding = int(input("Введите число 1"))
sec_number_for_adding = int(input("Введите число 2"))

added_number = math_operators.add(first_number_for_adding, sec_number_for_adding)

# вариант после
import math_operators

first_number_for_adding = int(input("Введите число 1"))
sec_number_for_adding = int(input("Введите число 2"))

# возвращает сложение двух чисел
added_number = math_operators.add(first_number_for_adding, sec_number_for_adding)

# согласно п.3 вставил комментарий прояснение


# №7
# вариант до
import os

def delete_all_files_in_directory():
    files = os.listdir()
    for file in files:
        if os.path.isfile(file):
            os.remove(file)

# вариант после
import os

# Функция удаляет все файлы в текущем каталоге без подтверждения.
# Использовать с осторожностью.

def delete_all_files_in_directory():
    files = os.listdir()
    for file in files:
        if os.path.isfile(file):
            os.remove(file)

# добавил комментарий согласно п.4 "Предупреждения о последствиях"



# №8
# вариант до
import fifth_asd.asd_fifth as inlet
from random import randint
import unittest


class DeEnquque(unittest.TestCase):

    # Эти тесты могут выполняться в пределах 2 секунд
    def test_De(self):
        tested_queue = inlet.Queue()
        length_of_queue = 100

        # проверка если очередь пуста
        self.assertEqual((), None)

        # проверка если очередь заполнена
        validation_list = []
        for i in range(length_of_queue):
            b = randint(0, 2 * 30)
            tested_queue.enqueue(b)
            validation_list.insert(0, b)

        for i in range(a):
            self.assertEqual(tested_queue.dequeue(), validation_list.pop(-1))
            self.assertEqual(tested_queue.size(), len(validation_list))


# вариант после

import fifth_asd.asd_fifth as inlet
from random import randint
import unittest


class DeEnquque(unittest.TestCase):

    # Эти тесты могут выполняться в пределах 2 секунд
    def test_De(self):
        tested_queue = inlet.Queue()
        length_of_queue = 100

        # проверка если очередь пуста
        self.assertEqual((), None)

        # проверка если очередь заполнена
        validation_list = []
        for i in range(length_of_queue):
            b = randint(0, 2 * 30)
            tested_queue.enqueue(b)
            validation_list.insert(0, b)

        for i in range(a):
            self.assertEqual(tested_queue.dequeue(), validation_list.pop(-1))
            self.assertEqual(tested_queue.size(), len(validation_list))

# добавил комментарий о времени выполнения тестов согласно п.4 "Предупреждения о последствиях"


# №9
# вариант до
class Calculator:
    def add(self, first_number, second_number):
        return first_number + second_number

    def subtract(self, first_number, second_number):
        return first_number - second_number

    def multiply(self, first_number, second_number):
        return first_number * second_number

    def divide(self, first_number, second_number):
        return first_number / second_number

# вариант после
class Calculator:
    def add(self, first_number, second_number):
        return first_number + second_number

    def subtract(self, first_number, second_number):
        return first_number - second_number

    def multiply(self, first_number, second_number):
        return first_number * second_number

    def divide(self, first_number, second_number):
        """
        Этот метод не обрабатывает деление на ноль.
        TODO: Добавить обработку исключения ZeroDivisionError для деления на ноль.
        """
        return first_number / second_number

# согласно п.6 добавил комментарий TODO для пометки того, что метод будет доделан позже



# №10
# вариант до
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number  # номер счета
        self.balance = initial_balance  # баланс

    # внесение средств на счет
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    # снятие средств со сщета
    def withdraw(self, amount):
        self.balance -= amount
        return True

    # получение текущего баланса счета
    def get_balance(self):
        return self.balance

# вариант после
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number  # номер счета
        self.balance = initial_balance  # баланс

    # внесение средств на счет
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    # снятие средств со сщета
    def withdraw(self, amount):
        """
        Этот метод не проверяет наличие достаточного баланса.
        TODO: Добавить проверку на наличие достаточного баланса перед снятием средств.
        """
        self.balance -= amount
        return True

    # получение текущего баланса счета
    def get_balance(self):
        return self.balance

# согласно п.6 добавил комментарий TODO для пометки того, что метод будет доделан позже и указывается,
#  что именно нужно сделать



# №11
# вариант до
with open('file.txt', 'r') as file:
    data = file.read()
    data = data[2:]

# вариант после

# Использование среза, начиная с 3-го символа необходимо, т.к. это номер параграфа и он для анализа файла не нужен
with open('file.txt', 'r') as file:
    data = file.read()
    data = data[2:]

# согласно п.5 указал в комментарии важность обстоятельства (параметра среза в списке)



# №12
# вариант до

from scipy import interpolate as intr

cooling_capacity_interp = intr.interp1d(coller_temperature, cooling_capacity, kind='cubic')
density_interp = intr.interp1d(coller_temperature, density, kind='linear')

# вариант после

from scipy import interpolate as intr

# важно для любого компонента для теплоёмкости исплользовать кубическую интерполяцию, а для плотности - линейную
# в силу физического смысла переменных
cooling_capacity_interp = intr.interp1d(coller_temperature, cooling_capacity, kind='cubic')
density_interp = intr.interp1d(coller_temperature, density, kind='linear')

# согласно п.5 указал в комментарии важность обстоятельства (вид интерполяции)

