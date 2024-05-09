import eleventh.asd_eleven as inlet
from random import randint
import random
import string
import unittest


class Hash(unittest.TestCase):
    def test_add_zeroStr(self):
        '''
        :return: Тест на правильность работы функции add при различных длинах битового массива и пустой строки.
        Проверяется битовый массив.
        '''
        def generate_string(length):
            '''
            :param length: Длина строки.
            :return: Генератор случайно строки.
            '''
            all_symbols = string.ascii_uppercase + string.digits
            result = ''.join(random.choice(all_symbols) for _ in range(length))
            return result

        for i in range(1000):
            length_arr = randint(1,1000)
            cl = inlet.BloomFilter(length_arr)

            length_str = 0
            cl.add(generate_string(length_str))
            my_array = ['1']
            for i in range(length_arr-1):
                my_array.append('0')
            self.assertEqual(bin(cl.arr)[2:],''.join(my_array))

    def test_add_oneStr(self):
        '''
        :return: Тест на правильность работы функции add при различных длинах битового массива и строки,
        состоящей из одного элемента. Проверяется битовый массив.
        '''
        def generate_string(length):
            '''
            :param length: Длина строки.
            :return: Генератор случайно строки.
            '''
            all_symbols = string.ascii_uppercase + string.digits
            result = ''.join(random.choice(all_symbols) for _ in range(length))
            return result

        for i in range(1000):
            length_arr = randint(1,1000)
            cl = inlet.BloomFilter(length_arr)

            length_str = 1
            cl.add(generate_string(length_str))
            my_array = ['1']
            for i in range(length_arr-1):
                my_array.append('0')
            self.assertEqual(bin(cl.arr)[2:],''.join(my_array))

    def test_add(self):
        '''
        :return: Тест на правильность работы функции add при различных длинах битового массива и различных
                количествах раз заполнения битового массива. Проверяется битовый массив.
        '''
        def generate_string(length):
            '''
            :param length: Длина строки.
            :return: Генератор случайно строки.
            '''
            all_symbols = string.ascii_uppercase + string.digits
            result = ''.join(random.choice(all_symbols) for _ in range(length))
            return result

        for i in range(100):
            length_arr = randint(3,1000)
            cl = inlet.BloomFilter(length_arr)
            num = randint(2,length_arr)
            my_array = []
            for i in range(length_arr):
                my_array.append('0')

            for i in range(num):
                length_str = randint(1, 1000)
                res = generate_string(length_str)

                cl.add(res)

                f1 = cl.hash1(res)
                f2 = cl.hash2(res)

                my_array[f1] = '1'
                my_array[f2] = '1'

                self.assertEqual(bin(cl.arr)[2:].zfill(length_arr),''.join(my_array))
            self.assertEqual(bin(cl.arr)[2:].zfill(length_arr), ''.join(my_array))

if __name__ == '__main__':
    unittest.main()
