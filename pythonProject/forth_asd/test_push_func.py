import forth_asd.asd_forth as inlet
from random import randint
import unittest



class TestPush(unittest.TestCase):
    def test_push(self):
        stack = inlet.Stack()
        arr = []
        for i in range(1000):
            stack.push(i)
            arr.append(i)
        self.assertEqual(stack.to_list(),arr)
        self.assertEqual(stack.size(),len(arr))

if __name__ == '__main__':
    unittest.main()