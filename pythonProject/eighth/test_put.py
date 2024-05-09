import eighth.asd_eight2 as inlet
from random import randint
import string
import random
import unittest



class Hash(unittest.TestCase):
    def test_put(self):
        '''
        :return: Тест на то, что когда таблица заполнена, то возвращается None.
        '''
        def generate_string(length):
            '''
            :param length: Длина строки.
            :return: Генератор случайно строки.
            '''
            all_symbols = string.ascii_uppercase + string.digits
            result = ''.join(random.choice(all_symbols) for _ in range(length))
            return result

        def prost_numb(n: int):
            '''
            :param n: Ограничение сверху по выбору простого числа.
            :return: Простое число в диапазоне от 3 до n.
            '''
            lst = []
            a = list(range(n+1))
            i = 2
            while i <= n:
                if a[i] != 0:
                    lst.append(a[i])
                    for j in range(i, n + 1, i):
                        a[j] = 0
                i += 1
            return random.choice(lst)

        for i in range(1000):
            shag = prost_numb(100)
            razmer = prost_numb(1000)
            while shag >= razmer:
                razmer = prost_numb(1000)
            h = inlet.HashTable(razmer, shag)
            num_s = randint(1, 10)

            for i in range(razmer):
                stroka = generate_string(num_s)
                h.put(stroka)

            stroka = generate_string(num_s)
            self.assertEqual(h.seek_slot(stroka), None)

    def test_put2(self):
        '''
        :return: Тест на корректность работы put при незаполненной таблице.
        '''
        def generate_string(length):
            '''
            :param length: Длина строки.
            :return: Генератор случайно строки.
            '''
            all_symbols = string.ascii_uppercase + string.digits
            result = ''.join(random.choice(all_symbols) for _ in range(length))
            return result

        def prost_numb(n: int):
            '''
            :param n: Ограничение сверху по выбору простого числа.
            :return: Простое число в диапазоне от 2 до n.
            '''
            lst = []
            a = list(range(n+1))
            i = 2
            while i <= n:
                if a[i] != 0:
                    lst.append(a[i])
                    for j in range(i, n + 1, i):
                        a[j] = 0
                i += 1
            return random.choice(lst)

        for i in range(50):
            shag = prost_numb(10)
            razmer = prost_numb(30)
            while shag >= razmer:
                razmer = prost_numb(30)
            h = inlet.HashTable(razmer, shag)
            num_s = randint(1, 10)

            for i in range(razmer):
                stroka = generate_string(num_s)
                m = h.put(stroka)
                self.assertEqual(stroka, h.slots[m])

if __name__ == '__main__':
    unittest.main()