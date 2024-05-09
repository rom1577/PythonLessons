import ninth_asd.asd_ninth as inlet
from random import randint
import string
import random
import unittest


class NatDict(unittest.TestCase):
    def test_iskey(self):
        '''
        :return: Тест функции is_key на наличие и отсутствие элементов в списке ключей.
        '''
        def generate_string(length):
            '''
            :param length: Длина строки.
            :return: Генератор случайно строки.
            '''
            all_symbols = string.ascii_uppercase + string.digits
            result = ''.join(random.choice(all_symbols) for _ in range(length))
            return result

        for k in range(100):
            size = randint(1, 100)
            csh = inlet.NativeDictionary(size)
            arr = []
            for i in range(size):
                o = generate_string(2)
                csh.put(o,generate_string(3))
                arr.append(o)
            for i in arr:
                self.assertEqual(True, i in csh.slots)
                self.assertEqual(False,generate_string(3) in csh.slots )





if __name__ == '__main__':
    unittest.main()