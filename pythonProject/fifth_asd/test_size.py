import fifth_asd.asd_fifth as inlet
from random import randint
import unittest

class Size(unittest.TestCase):
    def test_Size(self):
        '''
        Проверка длины очереди на пустом массиве и заполненном
        :return:
        '''
        q = inlet.Queue()
        a = 100

        self.assertEqual(q.size(),0)

        for i in range(a):
            b = randint(0,2*30)
            q.enqueue(b)

        self.assertEqual(q.size(), a)

if __name__ == '__main__':
    unittest.main()