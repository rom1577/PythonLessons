import seventh_asd.asd_seven3 as inlet
from random import randint
import unittest


class OrderL(unittest.TestCase):
    def test_delete_zero_ascTrue(self):
        '''
        :return: Тест метода delete когда список пуст и asc=True.
        '''
        for i in range(1000):
            num = randint(0,10**6)
            ol = inlet.OrderedList(True)
            ol.delete(num)
            self.assertEqual(ol.to_list(),[])

    def test_delete_zero_ascFalse(self):
        '''
        :return: Тест метода delete когда список пуст и asc=False.
        '''
        for i in range(1000):
            num = randint(0,10**6)
            ol = inlet.OrderedList(False)
            ol.delete(num)
            self.assertEqual(ol.to_list(), [])

    def test_delete_one_ascTrue(self):
        '''
        :return: Тест метода delete при сортировке массива по возрастанию, список имеет 1 элемент.
        '''
        for i in range(1000):
            ol = inlet.OrderedList(True)
            num_for_add = randint(0, 10 ** 6)
            ol.add(num_for_add)
            ol.delete(num_for_add)
            self.assertEqual(ol.to_list(), [])

    def test_delete_one_ascFalse(self):
        '''
        :return: Тест метода delete при сортировке массива по убыванию, список имеет 1 элемент.
        '''
        for i in range(1000):
            ol = inlet.OrderedList(False)
            num_for_add = randint(0, 10 ** 6)
            ol.add(num_for_add)
            ol.delete(num_for_add)
            self.assertEqual(ol.to_list(), [])

    def test_delete_first_ascTrue(self):
        '''
        :return: Тест метода delete при сортировке массива по возрастанию. Удаление наименьшего элемента (первого).
        '''
        for k in range(1000):
            ol = inlet.OrderedList(True)
            num = randint(1,1000)
            my_arr = []
            for i in range(num):
                num_for_add = randint(0, 10 ** 6)
                ol.add(num_for_add)
                my_arr.append(num_for_add)
            my_arr = sorted(my_arr, reverse=False)
            elem = my_arr.pop(0)
            ol.delete(elem)
            self.assertEqual(ol.to_list(), my_arr)

    def test_delete_first_ascFalse(self):
        '''
        :return: Тест метода delete при сортировке массива по убыванию. Удаление наибольшего элемента (первого).
        '''
        for k in range(1000):
            ol = inlet.OrderedList(False)
            num = randint(1,1000)
            my_arr = []
            for i in range(num):
                num_for_add = randint(0, 10 ** 6)
                ol.add(num_for_add)
                my_arr.append(num_for_add)
            my_arr = sorted(my_arr, reverse=True)
            elem = my_arr.pop(0)
            ol.delete(elem)
            self.assertEqual(ol.to_list(), my_arr)

    def test_delete_last_ascTrue(self):
        '''
        :return: Тест метода delete при сортировке массива по возрастанию. Удаление наибольшего элемента (послденего).
        '''
        for k in range(1000):
            ol = inlet.OrderedList(True)
            num = randint(1,1000)
            my_arr = []
            for i in range(num):
                num_for_add = randint(0, 10 ** 6)
                ol.add(num_for_add)
                my_arr.append(num_for_add)
            my_arr = sorted(my_arr, reverse=False)
            elem = my_arr.pop(len(my_arr)-1)
            ol.delete(elem)
            self.assertEqual(ol.to_list(), my_arr)

    def test_delete_last_ascFalse(self):
        '''
        :return: Тест метода delete при сортировке массива по убыванию. Удаление наименьшего элемента (послденего).
        '''
        for k in range(1000):
            ol = inlet.OrderedList(False)
            num = randint(1,1000)
            my_arr = []
            for i in range(num):
                num_for_add = randint(0, 10 ** 6)
                ol.add(num_for_add)
                my_arr.append(num_for_add)
            my_arr = sorted(my_arr, reverse=True)
            elem = my_arr.pop(len(my_arr)-1)
            ol.delete(elem)
            self.assertEqual(ol.to_list(), my_arr)

    def test_delete_free_ascTrue(self):
        '''
        :return: Тест метода delete при сортировке массива по возрастанию. Удаление произвольного элемента.
        '''
        for k in range(1000):
            ol = inlet.OrderedList(True)
            num = randint(1,1000)
            my_arr = []
            for i in range(num):
                num_for_add = randint(0, 10 ** 6)
                ol.add(num_for_add)
                my_arr.append(num_for_add)
            num_for_del = randint(0, len(my_arr)-1)
            my_arr = sorted(my_arr, reverse=False)
            per = my_arr[num_for_del]
            my_arr.remove(per)
            ol.delete(per)
            self.assertEqual(ol.to_list(), my_arr)

    def test_delete_free_ascFalse(self):
        '''
        :return: Тест метода delete при сортировке массива по убыванию. Удаление произвольного элемента.
        '''
        for k in range(1000):
            ol = inlet.OrderedList(False)
            num = randint(1,1000)
            my_arr = []
            for i in range(num):
                num_for_add = randint(0, 10 ** 6)
                ol.add(num_for_add)
                my_arr.append(num_for_add)
            num_for_del = randint(0, len(my_arr)-1)
            my_arr = sorted(my_arr, reverse=True)
            per = my_arr[num_for_del]
            my_arr.remove(per)
            ol.delete(per)
            self.assertEqual(ol.to_list(), my_arr)


if __name__ == '__main__':
    unittest.main()