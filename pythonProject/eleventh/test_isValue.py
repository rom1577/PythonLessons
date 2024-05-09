import eleventh.asd_eleven as inlet
from random import randint
import random
import string
import unittest


class Hash(unittest.TestCase):
    def test_is_value(self):
        '''
        :return: Проверка метода is_value. Проверяется равенство соответствующих битов единице для поданных в метод
        add() строк.
        '''
        def generate_string(length):
            '''
            :param length: Длина строки.
            :return: Генератор случайной строки.
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
            res_arr = []
            for i in range(num):
                length_str = randint(1, 1000)
                res = generate_string(length_str)
                res_arr.append(res)
                cl.add(res)

                f1 = cl.hash1(res)
                f2 = cl.hash2(res)

                my_array[f1] = '1'
                my_array[f2] = '1'

            for i in range(num):
                res = res_arr[i]
                f1 = cl.hash1(res)
                f2 = cl.hash2(res)
                self.assertEqual(cl.is_value(res),True)
                self.assertEqual(cl.is_value(res),my_array[f1] == '1' and my_array[f2] == '1')

if __name__ == '__main__':
    unittest.main()
