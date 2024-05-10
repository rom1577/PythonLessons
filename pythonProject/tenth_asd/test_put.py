import tenth_asd.asd_ten as inlet
from random import randint
import string
import random
import unittest


class MySet(unittest.TestCase):
    def test_put_null(self):
        '''
        :return: Тест на добавление присутствующего элемента.
        '''
        for i in range(1000):
            st = inlet.PowerSet()
            my_arr = []
            length = 100
            # заполнение множества
            for i in range(length):
                a = randint(1, 100)
                st.put(a)
                my_arr.append(a)

            size = st.size()
            my_arr2 = [0]*size
            for i in range(size):
                my_arr2[i] = st.sett[i]
            for i in my_arr:
                st.put(i)
                self.assertEqual(st.size(), size)  # проверка, что длина не меняется
                self.assertEqual(my_arr2, st.sett)  # проверка, что массив множества не меняется

    def test_put_notnull(self):
        '''
        :return: Тест на добавление присутствующего элемента.
        '''
        for i in range(1000):
            st = inlet.PowerSet()
            length = 100

            # заполнение множества
            for i in range(length):
                a = randint(1, 100)
                st.put(a)
                self.assertEqual(st.get(a), True)


if __name__ == '__main__':
    unittest.main()