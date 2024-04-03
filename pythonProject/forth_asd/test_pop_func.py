import forth_asd.asd_forth as inlet
from random import randint
import unittest



class TestPop(unittest.TestCase):
    def test_pop(self):
        stack = inlet.Stack()
        arr = []
        b = 1000
        for i in range(b):
            a = randint(1,10**6)
            stack.push(a)
            arr.append(a)
        for i in range(int(b/2)):
            g1 = stack.pop()
            g2 = arr.pop(-1)
            self.assertEqual(g1,g2)
        self.assertEqual(stack.to_list(),arr)
        self.assertEqual(stack.size(),len(arr))

        for i in range(int(b/2)):
            stack.pop()
            arr.pop(-1)
        self.assertEqual(stack.to_list(),arr)
        self.assertEqual(stack.size(), len(arr))

    def test_popNone(self):
        stack = inlet.Stack()
        self.assertEqual(stack.pop(),None)
        self.assertEqual(stack.size(),0)
if __name__ == '__main__':
    unittest.main()