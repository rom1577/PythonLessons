import third_acd.asd_third as inlet
from random import randint
import unittest
import math


class DeleteTest(unittest.TestCase):
    def test_delete(self):
        '''
        Удаление элемента динамического массива по любому индексу. Емкость не изменяется и равна 16
        :return:
        '''
        darr = inlet.DynArray()
        arr = []
        constt = 16

        for i in range(constt):
            a = randint(0,9)
            darr.append(a)
            arr.append(a)

        for delete_const in range(constt):
            darr.delete(delete_const)
            arr.pop(delete_const)
            darr_list = darr.to_list()
            self.assertEqual(darr.capacity,constt)
            self.assertEqual(arr,darr_list)

            arr.insert(5,5)
            darr.insert(5,5)

    def test_delete2(self):
        '''
        Удаление элемента динамического массива по любому индексу. Емкость не изменяется относительно изначальной и больше 16
        :return:
        '''
        darr = inlet.DynArray()
        arr = []
        constt = 22


        for i in range(constt):
            a = randint(0, 9)
            darr.append(a)
            arr.append(a)

        for delete_const in range(constt):
            darr.delete(delete_const)
            arr.pop(delete_const)
            darr_list = darr.to_list()

            self.assertEqual(darr.capacity, int(math.ceil(constt/16) * 16))
            self.assertEqual(arr, darr_list)

            arr.insert(5, 5)
            darr.insert(5, 5)


    def test_delete3(self):
        '''
        Удаление элемента динамического массива по любому индексу. Емкость изменяется относительно изначальной
        :return:
        '''
        darr = inlet.DynArray()
        arr = []
        constt = 22
        n = 5
        cap = int(math.ceil(constt/16) * 16)
        delete_const = 3

        for i in range(constt):
            a = randint(0, 9)
            darr.append(a)
            arr.append(a)

        for i in range(n):
            darr.delete(delete_const)
            arr.pop(delete_const)
        darr_list = darr.to_list()
        new_capacity = int(darr.capacity / 1.5)
        if darr.count / darr.capacity < 0.5 and new_capacity >= 16:
            cap = new_capacity
        self.assertEqual(darr.capacity,cap)
        self.assertEqual(arr, darr_list)

        for i in range(n):
            arr.insert(0, 5)
            darr.insert(0, 5)

    def test_deleteError(self):
        '''
        Проверка функции удаления элемента из массива, если элемент выходит за диапазон длины массива
        :return:
        '''
        darr = inlet.DynArray()
        ln = 50
        for i in range(ln):
            b = randint(1,9)
            darr.append(b)

        for i in range(1000):
            a = randint(-100,-1)
            with self.assertRaises(IndexError):
                darr.delete(a)

            c = randint(ln+1,ln * 2)
            with self.assertRaises(IndexError):
                darr.delete(c)


if __name__ == '__main__':
    unittest.main()
