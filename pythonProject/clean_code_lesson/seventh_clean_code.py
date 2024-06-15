# 3.1
# №1
# Класс комплексного числа, имеющий атрибуты мнимую и реальную части
class Complex:
    def __init__(self, real_part, imagine_part):
        self.real_part = real_part
        self.imagine_part = imagine_part

    @staticmethod
    def from_real_number(real_part):
        return Complex(real_part, 0)

    @staticmethod
    def from_imaginary_number(imagine_part):
        return Complex(0, imagine_part)


# №2
# Класс человек, который имеет атрибуты возраст и денежный капитал
class Human:
    def __init__(self, year_of_human, money_capital_usd):
        self.year_of_human = year_of_human
        self.money_capital_usd = money_capital_usd

    @staticmethod
    def from_middle(year_of_human):
        return Human(year_of_human, 100000)

    @staticmethod
    def from_young(year_of_human):
        return Human(year_of_human, 10)


# №3
# Класс автомобиль, имеющий атрибут мощность двигателя
class Car:
    def __init__(self, power_engine_hp):
        self.power_engine_hp = power_engine_hp

    @staticmethod
    def from_sport_car():
        return Car(1000)

    @staticmethod
    def from_bus():
        return Car(100)

# 3.2
# №1
# Абстрактный класс фабрики фигур, который объявляет метод расчета площиди фигуры и метод расчета периметра фигуры

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


# №2
# Абстрактный класс шахматных фигур, который определяет метод изменения позиции фигуры на доске
# и метод убийства другой фигуры

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

