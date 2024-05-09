import eighth.asd_eight2 as inlet
from random import randint
import string
import random
import unittest



class Hash(unittest.TestCase):
    def test_hash_fun_null(self):
        '''
        :return: Тест на подачу "0" в хэеш-функцию.
        '''
        for i in range(1000):
            shag = randint(1, 10)
            razmer = randint(shag+1, 100)
            h = inlet.HashTable(razmer, shag)
            stroka = ''

            s = list(stroka)
            sum = 0
            for i in range(len(s)):
                sum += ord(s[i])
            self.assertEqual(sum % razmer, h.hash_fun(stroka))
            self.assertEqual(0, h.hash_fun(stroka))

    def test_hash_fun(self):
        '''
        :return: Тест на корректность работу hash_fun.
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
            shag = randint(1, 10)
            razmer = randint(shag+1, 100)
            h = inlet.HashTable(razmer, shag)
            num_s = randint(1, 100)
            stroka = generate_string(num_s)

            s = list(stroka)
            sum = 0
            for i in range(len(s)):
                sum += ord(s[i])
            self.assertEqual(sum % razmer, h.hash_fun(stroka))


if __name__ == '__main__':
    unittest.main()