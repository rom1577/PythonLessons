import eleventh.asd_eleven as inlet
from random import randint
import random
import string
import unittest

class Hash(unittest.TestCase):
    def test_hash2_zero(self):
        '''
        Тест если подается пустая строка для вычисления хэш-функции
        :return:
        '''
        for j in range(100):
            b = randint(1,10000)
            cl = inlet.BloomFilter(b)
            self.assertEqual(cl.hash2(''),0)

    def test_hash2_one(self):
        '''
        Тест если подается строка из одного элемента для вычисления хэш-функции
        :return:
        '''
        for j in range(100):
            b = randint(1,10000)
            cl = inlet.BloomFilter(b)

            for i in range(10):
                a = randint(0,9)
                self.assertEqual(cl.hash2(str(a)), 0)

    def test_hash2(self):
        '''
        Тест корректности работы алгоритма хэш-функции
        :return:
        '''
        def generate_string(length):
            all_symbols = string.ascii_uppercase + string.digits
            result = ''.join(random.choice(all_symbols) for _ in range(length))
            return result

        for j in range(100):
            b = randint(1, 10000)
            cl = inlet.BloomFilter(b)

            for k in range(1000):
                c = randint(2,1000)
                str1 = str(generate_string(c))

                sum = 0
                const = 17
                for i in range(len(str1)):
                    if i == 0:
                        continue
                    code = ord(str1[i])
                    sum = (sum * const + code) % b

                self.assertEqual(cl.hash2(str1),sum)

if __name__ == '__main__':
    unittest.main()