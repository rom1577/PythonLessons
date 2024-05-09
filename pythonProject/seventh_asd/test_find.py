import seventh_asd.asd_seven3 as inlet
from random import randint
import random
import unittest


class OrderL(unittest.TestCase):
    def test_find_zero_ascTrue(self):
        '''
        :return: Тест функции find при пустом списке и с сортировкой по возрастанию
        '''
        for i in range(1000):
            num = randint(0, 10 ** 6)
            ol = inlet.OrderedList(True)
            self.assertEqual(ol.find(num), None)

    def test_find_zero_ascFalse(self):
        '''
        :return: Тест функции find при пустом списке и с сортировкой по убыванию
        '''
        for i in range(1000):
            num = randint(0, 10 ** 6)
            ol = inlet.OrderedList(False)
            self.assertEqual(ol.find(num), None)

    def test_find_one_ascTrue(self):
        '''
        :return: Тест функции find когда в списке один элемент и с сортировкой по возрастанию
        '''
        for i in range(1000):
            ol = inlet.OrderedList(True)
            num_for_add = randint(0, 10 ** 6)
            ol.add(num_for_add)
            self.assertEqual(ol.find(num_for_add).value, num_for_add)
            ol.delete(num_for_add)

    def test_find_one_ascFalse(self):
        '''
        :return: Тест функции find когда в списке один элемент и с сортировкой по убыванию
        '''
        for i in range(1000):
            ol = inlet.OrderedList(False)
            num_for_add = randint(0, 10 ** 6)
            ol.add(num_for_add)
            self.assertEqual(ol.find(num_for_add).value, num_for_add)
            ol.delete(num_for_add)

    # def test_



    def test_find_free_ascTrue(self):
        '''
        :return: Тест метода find при сортировке массива по возрастанию. Нахождение произвольного элемента.
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
            self.assertEqual(ol.find(per).value, per)

    def test_find_free_ascFalse(self):
        '''
        :return: Тест метода find при сортировке массива по убыванию. Нахождение произвольного элемента.
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
            self.assertEqual(ol.find(per).value, per)

    def test_find_first_ascFalse(self):
        '''
        :return: Не доделано
        '''
        for k in range(1000):
            ol = inlet.OrderedList(False)
            num = randint(2,1000)
            my_arr = []
            i = 0
            while i <= num:
                num_for_add = randint(2, 10 ** 6)
                if num_for_add % 2 != 0:
                    continue
                ol.add(num_for_add)
                my_arr.append(num_for_add)
                i += 1
            num_for_del = randint(0, len(my_arr)-1)
            # print(my_arr)
            my_arr = sorted(my_arr, reverse=True)
            middle = (my_arr[0] + my_arr[-1])//2 + 1
            # per = my_arr[num_for_del]
            self.assertEqual(ol.find(middle), None)



if __name__ == '__main__':
    unittest.main()