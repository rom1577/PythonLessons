import fifth_asd.asd_fifth as inlet
from random import randint
import unittest

class DeEnquque(unittest.TestCase):
    def test_De(self):
        '''
        Вставка в пустую очередь и в заполненную.
        Проверка на равенство длины и что вставленный элемент находится в 0-м индексе
        :return:
        '''
        q = inlet.Queue()
        a = 100

        # проверка если очередь пуста
        self.assertEqual(q.dequeue(),None)

        # проверка если очередь заполнена
        arr = []
        for i in range(a):
            b = randint(0,2*30)
            q.enqueue(b)
            arr.insert(0,b)

        for i in range(a):
            self.assertEqual(q.dequeue(),arr.pop(-1))
            self.assertEqual(q.size(),len(arr))

if __name__ == '__main__':
    unittest.main()