import ninth_asd.asd_ninth as inlet
from random import randint
import string
import random
import unittest


class NatDict(unittest.TestCase):
    def test_get_None(self):
        '''
        :return: Тест на возвращение None при несуществующем ключе.
        '''
        def generate_string(length):
            '''
            :param length: Длина строки.
            :return: Генератор случайно строки.
            '''
            all_symbols = string.ascii_uppercase + string.digits
            result = ''.join(random.choice(all_symbols) for _ in range(length))
            return result

        for k in range(1000):
            size = randint(1,100)
            t = randint(1,size)
            csh = inlet.NativeDictionary(size)
            for i in range(t):
                key_str = generate_string(randint(1, 10))
                self.assertEqual(csh.get(key_str), None)

    def test_get(self):
        '''
        :return: Тест на корректное возвращение значения.
        '''
        def generate_string(length):
            '''
            :param length: Длина строки.
            :return: Генератор случайно строки.
            '''
            all_symbols = string.ascii_uppercase + string.digits
            result = ''.join(random.choice(all_symbols) for _ in range(length))
            return result

        for k in range(1000):
            size = randint(1,100)
            csh = inlet.NativeDictionary(size)
            for i in range(size):  # заполнили self.slots
                key_str = generate_string(randint(1, 10))
                val_str = generate_string(randint(1, 10))
                while key_str in csh.slots:
                    key_str = generate_string(randint(1, 10))
                csh.put(key_str, val_str)

            for i in range(size):
                self.assertEqual(csh.values[i], csh.get(csh.slots[i]))


if __name__ == '__main__':
    unittest.main()


