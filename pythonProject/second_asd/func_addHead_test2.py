import second_asd.second_asd as inlet
from random import randint
import unittest


class AddHeadTest(unittest.TestCase):

    def test_add_to_headEmpty(self):
        """

        :return:
        """
        linked_list = inlet.LinkedList2()

        for i in range(10000):
            linked_list.clean()
            c = randint(1, 2 ** 30)
            v = inlet.Node(c)
            linked_list.add_in_head(v)
            self.assertEqual(v,linked_list.head)
            self.assertEqual(v, linked_list.tail)

    def test_add_to_headFull(self):
        linked_list = inlet.LinkedList2()

        for i in range(1000):
            c = randint(1,2 ** 30)
            v = inlet.Node(c)
            linked_list.add_in_tail(v)

        tail = linked_list.tail

        for i in range(10000):
            c = randint(1,2 ** 30)
            v = inlet.Node(c)
            linked_list.add_in_head(v)
            self.assertEqual(tail,linked_list.tail)
            self.assertEqual(v,linked_list.head)





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

