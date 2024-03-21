import second_asd.second_asd  as inlet
from random import randint
import unittest


class DelTest(unittest.TestCase):

    def test_EmtyList(self):
        '''
        Try to define the length of empty linked list.
        :return:
        '''
        list_link = inlet.LinkedList2()
        self.assertEqual(list_link.len(),0)

    def test_NoEmptyList(self):
        '''
        Try to define the length of non empty linked list.
        :return:
        '''
        list_link = inlet.LinkedList2()

        a = randint(1,10000)
        for i in range(a):
            list_link.add_in_tail(inlet.Node(randint(0,10000)))
        self.assertEqual(list_link.len(),a)

if __name__ == '__main__':
    unittest.main()

