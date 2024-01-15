'''
Данный код выводит ошибку  "TypeError: method() missing 2 required positional arguments: 'b' and 'c'".
Ad hoc полиморфизм не работает в python. Каждое следующее объявление метода method() перезаписывает предыдущий.
'''

#  класс выполнения расчетов
class Calculations:
    # инициализация поля а
    def __init__(self, user_a):
        self.a = user_a

    # методы с одиннаковым именем
    def method(self):
        return self.a + 1

    def method(self, b):
        return self.a ** b

    def method(self, b, c):
        return b ** c

# создание экземпляра класса
numb = Calculations(1)

# работа с методами класса Calculations
print(numb.method())
print(numb.method(200))
print(method(2, 7))
