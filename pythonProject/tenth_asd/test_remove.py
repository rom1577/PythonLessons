import tenth_asd.asd_ten as inlet
from random import randint
import string
import random
import unittest


class MySet(unittest.TestCase):
    def test_remove1(self):
        '''
        :return: Тест на успешное удаление.
        '''
        for i in range(1000):
            st = inlet.PowerSet()
            my_arr = []
            length = 100
            # заполнение множества
            for i in range(length):
                a = randint(1, 1000)
                while a in st.sett:
                    a = randint(1, 1000)
                st.put(a)
                my_arr.append(a)

            for i in range(length-1, -1):
                # c = st.sett
                b = st.remove(my_arr[i])
                my_arr.remove(my_arr[i])
                self.assertEqual(my_arr, st.sett)
                self.assertEqual(True, b)

    def test_remove2(self):
        '''
        :return: Тест на не успешное удаление (несуществующего элемента).
        '''
        for i in range(1000):
            st = inlet.PowerSet()
            length = 100
            # заполнение множества
            for i in range(length):
                a = randint(1, 1000)
                st.put(a)

            for i in range(length):
                b = randint(1001, 10000)
                self.assertEqual(False, st.remove(b))


if __name__ == '__main__':
    unittest.main()