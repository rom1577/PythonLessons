import first_acd.acd_1 as inlet
from random import randint
import unittest


class DelTest(unittest.TestCase):

    def test_EmtyList(self):
        list_link = inlet.LinkedList()
        self.assertEqual(list_link.len(),0)

    def test_NoEmptyList(self):
        list_link = inlet.LinkedList()

        a = randint(1,10000)
        for i in range(a):
            list_link.add_in_tail(inlet.Node(randint(0,10000)))
        self.assertEqual(list_link.len(),a)

if __name__ == '__main__':
    unittest.main()

