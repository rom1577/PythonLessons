import first_acd.acd_1 as inlet
from random import randint
import unittest

class DelTest(unittest.TestCase):
    def test_NoneFalse(self):
        list_link = inlet.LinkedList()
        list_link.delete(None,False)
        self.assertEqual([],list_link.to_list())

    def test_NoneTrue(self):
        list_link = inlet.LinkedList()
        list_link.delete(None,True)
        self.assertEqual([],list_link.to_list())

    def test_OneNumberFalse(self):
        list_link = inlet.LinkedList()
        for i in range(100000):
            a = randint(0,2**30)
            list_link.add_in_tail(inlet.Node(a))
            list_link.delete(a,False)
            self.assertEqual([],list_link.to_list())

    def test_OneNumberTrue(self):
        list_link = inlet.LinkedList()
        for i in range(100000):
            a = randint(0,2**30)
            list_link.add_in_tail(inlet.Node(a))
            list_link.delete(a,True)
            self.assertEqual([],list_link.to_list())

    def test_MoreNumberFalse(self):
        a = randint(0,2**30)
        b = randint(0,2**30)
        c = randint(0,2**30)
        list_link1 = inlet.LinkedList()
        list_link2 = inlet.LinkedList()
        list_link3 = inlet.LinkedList()
        ar1 = []
        ar2 = []
        ar3 = []

        for i in range(100000):
            if i != 0:
                ar1.append(a)
            ar2.append(a)
            ar3.append(a)
            list_link1.add_in_tail(inlet.Node(a))
            list_link2.add_in_tail(inlet.Node(a))
            list_link3.add_in_tail(inlet.Node(a))

        list_link1.add_in_tail(inlet.Node(b))
        list_link2.add_in_tail(inlet.Node(b))
        list_link3.add_in_tail(inlet.Node(b))
        ar1.append(b)
        ar2.append(b)
        for i in range(100000):
            if i != 0:
                ar2.append(c)
            ar1.append(c)
            ar3.append(c)
            list_link1.add_in_tail(inlet.Node(c))
            list_link2.add_in_tail(inlet.Node(c))
            list_link3.add_in_tail(inlet.Node(c))

        list_link1.delete(a,False)
        list_link2.delete(c,False)
        list_link3.delete(b,False)
        self.assertEqual(ar1,list_link1.to_list())
        self.assertEqual(ar2,list_link2.to_list())
        self.assertEqual(ar3, list_link3.to_list())

    def test_MoreNumberTrue(self):
        a = randint(0, 2 ** 30)
        b = randint(0, 2 ** 30)
        c = randint(0, 2 ** 30)
        list_link1 = inlet.LinkedList()
        list_link2 = inlet.LinkedList()
        list_link3 = inlet.LinkedList()
        ar1 = []
        ar2 = []
        ar3 = []

        for i in range(100000):
            ar2.append(a)
            ar3.append(a)
            list_link1.add_in_tail(inlet.Node(a))
            list_link2.add_in_tail(inlet.Node(a))
            list_link3.add_in_tail(inlet.Node(a))

        list_link1.add_in_tail(inlet.Node(b))
        list_link2.add_in_tail(inlet.Node(b))
        ar1.append(b)
        ar2.append(b)

        for i in range(100000):
            list_link1.add_in_tail(inlet.Node(c))
            list_link2.add_in_tail(inlet.Node(c))
            list_link3.add_in_tail(inlet.Node(c))
            ar1.append(c)
            ar3.append(c)

        list_link1.delete(a,True)
        list_link2.delete(c,True)
        list_link3.delete(b, True)
        self.assertEqual(ar1, list_link1.to_list())
        self.assertEqual(ar2, list_link2.to_list())
        self.assertEqual(ar3, list_link3.to_list())
if __name__ == '__main__':
    unittest.main()

