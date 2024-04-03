import forth_asd.asd_forth as inlet
from random import randint
import unittest

class TestSize(unittest.TestCase):
    def test_sizeZero(self):
        stack = inlet.Stack()
        self.assertEqual(stack.size(),0)
        for i in range(1000):
            stack.pop()
        self.assertEqual(stack.size(),0)
        self.assertNotEqual(stack.size(),None)

    def test_sizeMuchNumber(self):
        stack = inlet.Stack()
        a = randint(1000000,10**7)
        for i in range(a):
            stack.push(i)
        self.assertEqual(stack.size(),a)
        for i in range(a):
            stack.pop()
        self.assertEqual(stack.size(),0)

if __name__ == '__main__':
    unittest.main()