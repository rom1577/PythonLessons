import ninth_asd.asd_ninth as inlet
from random import randint
import string
import random
import unittest


class NatDict(unittest.TestCase):
    def test_put_None(self):
        '''
        :return: Тест на добавление ключа, когда self.slots не заполнен полностью.
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
                val_str = generate_string(randint(1, 10))
                while key_str in csh.slots:
                    key_str = generate_string(randint(1, 10))
                csh.put(key_str, val_str)
                self.assertEqual(csh.get(key_str), val_str)

    def test_put_first(self):
        '''
        :return: Тест метода put, когда self.slots уже заполнен.
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

            new_slots = ['']*size
            for i in range(len(csh.slots)):
                new_slots[i] = csh.slots[i]

            for i in range(size):
                new_val_str = generate_string(randint(1, 10))
                csh.put(new_slots[i],new_val_str)
                self.assertEqual(csh.values[csh.hash_fun(new_slots[i])],new_val_str)


if __name__ == '__main__':
    unittest.main()


