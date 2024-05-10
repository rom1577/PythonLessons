import tenth_asd.asd_ten as inlet
from random import randint
import string
import random
import unittest


class MySet(unittest.TestCase):
    def test_issubset1(self):
        '''
        :return: Тест когда все элементы параметра входят в множество.
        '''
        for i in range(1000):
            st = inlet.PowerSet()
            st2 = inlet.PowerSet()
            length = 100
            # заполнение множества
            for i in range(length):
                a = randint(1, 1000)
                st.put(a)
                st2.put(a)

            self.assertEqual(st.issubset(st2), True)

    def test_issubset2(self):
        '''
        :return: Тест когда все элементы множества входят в параметр.
        '''
        for i in range(1000):
            st = inlet.PowerSet()
            st2 = inlet.PowerSet()
            length = 100
            # заполнение множеств
            for i in range(length):
                a = randint(1, 1000)
                st.put(a)
                st2.put(a)

            for i in range(length):
                b = randint(1001, 10000)
                st2.put(b)

            self.assertEqual(st.issubset(st2), False)

    def test_issubset3(self):
        '''
        :return: Тест когда не все элементы параметра входят в множество.
        '''
        for i in range(1000):
            st = inlet.PowerSet()
            st2 = inlet.PowerSet()
            length = 100
            my_arr = []
            # заполнение множеств
            for i in range(length):
                a = randint(1, 1000)
                st.put(a)
                my_arr.append(a)

            for i in range(length//2):
                st2.put(my_arr[i])
            for i in range(length//2):
                a = randint(1001, 10000)
                st2.put(a)

            self.assertEqual(st.issubset(st2), False)


if __name__ == '__main__':
    unittest.main()