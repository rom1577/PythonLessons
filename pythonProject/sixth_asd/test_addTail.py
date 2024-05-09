import sixth_asd.asd_sixth as inlet
from random import randint
import unittest

class DeEnquque(unittest.TestCase):
    def test_addTail(self):
        '''
        проверка метода addTail в пустую очередь Deque
        :return:
        '''
        q = inlet.Deque()
        arr = []
        a = 100
        for i in range(a):
            b = randint(0,2**30)
            q.addTail(b)
            arr.insert(0,b)
        self.assertEqual(q.to_list(),arr)


if __name__ == '__main__':
    unittest.main()