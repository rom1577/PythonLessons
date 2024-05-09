import third_acd.asd_third as inlet
from random import randint
import unittest
import math


class InsertTest(unittest.TestCase):
    def test_insert1(self):
        '''
        Вставка элемента в динамический массив по любому индексу. Емкость не изменяется и равна 16
        :return:
        '''
        darr = inlet.DynArray()
        arr = []
        constt = 16

        for i in range(constt-1):
            a = randint(0, 9)
            darr.append(a)
            arr.append(a)

        for insert_const in range(constt-1):
            darr.insert(insert_const,10)
            arr.insert(insert_const,10)
            darr_list = darr.to_list()
            self.assertEqual(darr.capacity, constt)
            self.assertEqual(arr, darr_list)

            arr.pop(5)
            darr.delete(5)

    def test_insert2(self):
        '''
        Вставка элемента в динамический массив по любому индексу. Емкость изменяется относительно изначальной
        :return:
        '''
        darr = inlet.DynArray()
        arr = []
        constt = 16

        insert_const = 3

        for i in range(1000):
            n = randint(0, 1000)
        # n=2000
            for i in range(constt):
                a = randint(0, 9)
                darr.append(a)
                arr.append(a)

            for i in range(n):
                darr.insert(insert_const,10)
                arr.insert(insert_const,10)
            darr_list = darr.to_list()

            new_capacity = 16
            while new_capacity < (n+16):
                new_capacity = new_capacity * 2
            # if darr.count / darr.capacity < 0.5 and new_capacity >= 16:
            #     cap = new_capacity
            self.assertEqual(darr.capacity, new_capacity)
            self.assertEqual(arr, darr_list)

            for i in range(n):
                arr.remove(10)
                darr.delete(insert_const)

    def test_deleteError(self):
        '''
        Проверка функции удаления элемента из массива, если элемент выходит за диапазон длины массива
        :return:
        '''
        darr = inlet.DynArray()
        ln = 50
        for i in range(ln):
            b = randint(1, 9)
            darr.append(b)

        for i in range(1000):
            a = randint(-100, -1)
            with self.assertRaises(IndexError):
                darr.delete(a)

            c = randint(ln + 1, ln * 2)
            with self.assertRaises(IndexError):
                darr.delete(c)


if __name__ == '__main__':
    unittest.main()
