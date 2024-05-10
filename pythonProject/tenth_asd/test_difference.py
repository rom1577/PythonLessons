import tenth_asd.asd_ten as inlet
from random import randint
import string
import random
import unittest


class MySet(unittest.TestCase):
    def test_difference_null(self):
        '''
        :return: Тест на получение пустого множества.
        '''
        for i in range(1000):
            st = inlet.PowerSet()
            length = 100
            # заполнение множества
            for i in range(length):
                a = randint(1, 1000)
                st.put(a)

            self.assertEqual(st.difference(st).sett, [])

    def test_difference(self):
        '''
        :return: Тест на получение непустого множества в результате вычитания.
        '''
        for i in range(1000):
            st = inlet.PowerSet()
            st2 = inlet.PowerSet()
            my_arr3 = []
            length = 100
            # заполнение множества
            for i in range(length):
                a = randint(1, 1000)
                b = randint(1001, 10000)
                while a in st.sett or b in st2.sett:
                    a = randint(1, 1000)
                    b = randint(1001, 10000)
                st.put(a)
                st2.put(b)

            for i in range(length):
                if st.sett[i] not in st2.sett:
                    my_arr3.append(st.sett[i])

            self.assertEqual(sorted(st.difference(st2).sett), sorted(my_arr3))


if __name__ == '__main__':
    unittest.main()