import tenth_asd.asd_ten as inlet
from random import randint
import string
import random
import unittest


class MySet(unittest.TestCase):
    def test_intersection_null(self):
        '''
        :return: Тест на получение пустого множества в результате пересечения.
        '''
        for i in range(1000):
            st = inlet.PowerSet()
            st2 = inlet.PowerSet()
            length = 100
            # заполнение множества
            for i in range(length):
                a = randint(1, 1000)
                b = randint(1001, 10000)
                st.put(a)
                st2.put(b)

            self.assertEqual(st.intersection(st2).sett, [])

    def test_intersection(self):
        '''
        :return: Тест на получение непустого множества в результате пересечения.
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
                if st.sett[i] in st2.sett and st2.sett[i] in st.sett:
                    my_arr3.append(st.sett[i])

            self.assertEqual(sorted(st.intersection(st2).sett), sorted(my_arr3))


if __name__ == '__main__':
    unittest.main()