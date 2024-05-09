import sixth_asd.asd_sixth as inlet
from random import randint
import unittest


class DeEnquque(unittest.TestCase):
    def test_removeFront(self):
        '''
        Тест функции removeFront для заранее заполненной очереди. Сравниваем со стандартным списком
        :return:
        '''
        q = inlet.Deque()
        arr = []
        a = 100

        for i in range(a):
            b = randint(0, 2 ** 30)
            q.addTail(b)
            arr.insert(0,b)

        for i in range(a):
            gg1 = q.removeFront()
            gg2 = arr.pop(-1)
            self.assertEqual(gg1,gg2)
            self.assertEqual(q.size(),len(arr))
            self.assertEqual(q.to_list(), arr)
        self.assertEqual(q.to_list(), [])

    def test_NullRemoveFront(self):
        '''
        Тест функции removeFront для пустой очереди.
        Проверка того, что очередь пуста и никакого элемента не возвращается
        :return:
        '''
        q = inlet.Deque()
        gg = q.removeFront()
        self.assertEqual(q.to_list(),[])
        self.assertEqual(gg, None)

if __name__ == '__main__':
    unittest.main()