import first_acd.acd_1 as inlet
from random import randint
import unittest

class DelTest(unittest.TestCase):

    def test_EmptyList(self):
        list_link = inlet.LinkedList()
        # list_link.add_in_tail(inlet.Node(None))

        for i in range(100000):
            c = randint(0, 2 ** 30)
            list_obj = list_link.find_all(c)

            self.assertEqual(list_obj,[])

    def test_OneNumberList(self):
        list_link = inlet.LinkedList()
        list_val = []

        for i in range(100000):
            list_val.clear()
            list_link.clean()
            c = randint(0, 2 **30)
            list_link.add_in_tail(inlet.Node(c))
            list_obj = list_link.find_all(c)
            list_val.append(list_obj[0].value)
            self.assertEqual(list_val, [c])

    def test_ManyNumbersTest(self):
        list_link = inlet.LinkedList()
        a = randint(0, 2 ** 30)
        b = randint(0, 2 ** 30)
        c = randint(0, 2 ** 30)
        ar1 = []
        ar2 = []
        ar3 = []
        list1_val = []
        list2_val = []
        list3_val = []

        for i in range(100000):
            list_link.add_in_tail(inlet.Node(a))
            ar1.append(a)

        for i in range(100000):
            list_link.add_in_tail(inlet.Node(b))
            ar2.append(b)

        for i in range(100000):
            list_link.add_in_tail(inlet.Node(c))
            ar3.append(c)

        list1_obj = list_link.find_all(a)
        for i in range(len(list1_obj)):
            list1_val.append(list1_obj[i].value)

        list2_obj = list_link.find_all(b)
        for i in range(len(list2_obj)):
            list2_val.append(list2_obj[i].value)

        list3_obj = list_link.find_all(c)
        for i in range(len(list3_obj)):
            list3_val.append(list3_obj[i].value)

        self.assertEqual(ar1, list1_val)
        self.assertEqual(ar2, list2_val)
        self.assertEqual(ar3, list3_val)




if __name__ == '__main__':
    unittest.main()