import forth_asd.asd_forth as inlet
from random import randint
import unittest

class TestPeek(unittest.TestCase):
    def test_peek(self):
        stack = inlet.Stack()
        arr = []
        b = 1000
        for i in range(b):
            a = randint(1, 10 ** 6)
            stack.push(a)
            arr.append(a)
        for i in range(b):
            g1 = stack.peek()
            g2 = arr[-1]
            self.assertEqual(g1, g2)
            self.assertEqual(stack.size(), len(arr))
            stack.pop()
            arr.pop(-1)

if __name__ == '__main__':
    unittest.main()