import fifth_asd.asd_fifth as inlet
from random import randint
import unittest

class Enquque(unittest.TestCase):
    def test_In(self):
        '''
        Вставка в пустую очередь и в заполненную.
        Проверка на равенство длины и что вставленный элемент находится в 0-м индексе
        :return:
        '''
        q = inlet.Queue()
        a = 100

        q.enqueue(1)
        self.assertEqual(q.size(),1)

        for i in range(a):
            b = randint(0,2*30)
            q.enqueue(b)

        self.assertEqual(q.size(), a + 1)
        self.assertEqual(q.to_list()[0],b)

if __name__ == '__main__':
    unittest.main()