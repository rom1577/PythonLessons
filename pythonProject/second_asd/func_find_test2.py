import second_asd.second_asd  as inlet
from random import randint
import unittest

class DelTest(unittest.TestCase):

    def test_EmptyList(self):
        '''
        Test empty linked list.
        Try to find the non-existent element in the linked list.
        :return:
        '''
        list_link = inlet.LinkedList2()
        # list_link.add_in_tail(inlet.Node(None))

        for i in range(100000):
            c = randint(0, 2 ** 30)
            list_obj = list_link.find(c)

            self.assertEqual(list_obj,None)

    def test_OneNumberList(self):
        '''
        Test the linked list, which consist of the one element.
        Try to find this element.
        :return:
        '''
        list_link = inlet.LinkedList2()
        list_val = []

        for i in range(100000):
            list_val.clear()
            list_link.clean()
            c = randint(0, 2 **30)
            v = inlet.Node(c)
            list_link.add_in_tail(v)
            list_obj = list_link.find(c)
            self.assertEqual(list_obj, v)

    def test_ManyNumbersTest(self):
        '''
        Linked lsit has a much number of varios elements.
        It is supposed to be equals the "i" element of linked list with
        the corresponding node.
        :return:
        '''
        list_link = inlet.LinkedList2()
        list_node = []

        for i in range(10000):

            c = randint(0, 2 ** 30)
            v = inlet.Node(c)
            list_link.add_in_tail(v)

            list_node.append(v)

        for i in range(10000):
            find_num = list_link.find(list_node[i].value)
            self.assertEqual(find_num, list_node[i])


if __name__ == '__main__':
    unittest.main()