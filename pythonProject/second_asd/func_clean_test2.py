import second_asd.second_asd  as inlet
from random import randint
import unittest

class DelTest(unittest.TestCase):
    def test_MyTestFull(self):
        list_link = inlet.LinkedList2()
        for i in range(100000):
            a = randint(0, 2 ** 30)
            list_link.add_in_tail(inlet.Node(a))
        list_link.clean()
        self.assertEqual([], list_link.to_list())

    def test_MyTestEmpty(self):
        list_link = inlet.LinkedList2()
        list_link.clean()
        self.assertEqual([], list_link.to_list())

if __name__ == '__main__':
    unittest.main()