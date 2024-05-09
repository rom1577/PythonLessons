import seventh_asd.asd_seven3 as inlet
from random import randint
import unittest


class OrderL(unittest.TestCase):
    def test_add_zero_ascTrue(self):
        '''
        :return: Тест метода add когда список пуст и asc=True.
        '''
        for i in range(1000):
            num = randint(0,10**6)
            ol = inlet.OrderedList(True)
            ol.add(num)
            self.assertEqual(ol.to_list(),[num])

    def test_add_zero_ascFalse(self):
        '''
        :return: Тест метода add когда список пуст и asc=False.
        '''
        for i in range(1000):
            num = randint(0,10**6)
            ol = inlet.OrderedList(False)
            ol.add(num)
            self.assertEqual(ol.to_list(),[num])

    def test_add_free_ascTrue(self):
        '''
        :return: Тест метода add при сортировке массива по возрастанию, элементы происзовльны.
        '''
        ol = inlet.OrderedList(True)
        arr = []
        for i in range(1000):
            num_for_add = randint(0,10**6)
            arr.append(num_for_add)
            ol.add(num_for_add)
        self.assertEqual(ol.to_list(),sorted(arr))

    def test_add_free_ascFalse(self):
        '''
        :return: Тест метода add при сортировке массива по убыванию, элементы происзовльны.
        '''
        ol = inlet.OrderedList(False)
        arr = []
        for i in range(1000):
            num_for_add = randint(0,10**6)
            arr.append(num_for_add)
            ol.add(num_for_add)
        self.assertEqual(ol.to_list(),sorted(arr,reverse=True))

    def test_add_big_ascTrue(self):
        '''
        :return: Тест метода add при сортировке массива по возрастснию, каждый добавляемый элемент больше предыдущего.
        '''
        ol = inlet.OrderedList(True)
        arr = []
        num_for_add = randint(0, 10 ** 6)
        for i in range(1000):
            num_for_add += 1
            arr.append(num_for_add)
            ol.add(num_for_add)
        self.assertEqual(ol.to_list(),sorted(arr,reverse=False))

    def test_add_big_ascFalse(self):
        '''
        :return: Тест метода add при сортировке массива по убыванию, каждый добавляемый элемент больше предыдущего.
        '''
        ol = inlet.OrderedList(False)
        arr = []
        num_for_add = randint(0, 10 ** 6)
        for i in range(1000):
            num_for_add += 1
            arr.append(num_for_add)
            ol.add(num_for_add)
        self.assertEqual(ol.to_list(),sorted(arr,reverse=True))

    def test_add_small_ascTrue(self):
        '''
        :return: Тест метода add при сортировке массива по возрастанию, каждый добавляемый элемент меньше предыдущего.
        '''
        ol = inlet.OrderedList(True)
        arr = []
        num_for_add = randint(0, 10 ** 6)
        for i in range(1000):
            num_for_add -= 1
            arr.append(num_for_add)
            ol.add(num_for_add)
        self.assertEqual(ol.to_list(),sorted(arr,reverse=False))

    def test_add_small_ascFalse(self):
        '''
        :return: Тест метода add при сортировке массива по убыванию, каждый добавляемый элемент меньше предыдущего.
        '''
        ol = inlet.OrderedList(False)
        arr = []
        num_for_add = randint(0, 10 ** 6)
        for i in range(1000):
            num_for_add -= 1
            arr.append(num_for_add)
            ol.add(num_for_add)
        self.assertEqual(ol.to_list(),sorted(arr,reverse=True))



if __name__ == '__main__':
    unittest.main()