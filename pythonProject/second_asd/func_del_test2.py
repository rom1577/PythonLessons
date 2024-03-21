import second_asd.second_asd  as inlet
from random import randint
import unittest

class DelTest(unittest.TestCase):
    def test_NoneFalse(self):
        list_link = inlet.LinkedList2()
        for i in range(1000):
            list_link.clean()
            c = randint(1, 2 ** 30)
            list_link.delete(c,False)
            self.assertEqual([],list_link.to_list())
            self.assertEqual(list_link.head, None)
            self.assertEqual(list_link.tail, None)

    def test_NoneTrue(self):
        list_link = inlet.LinkedList2()
        for i in range(1000):
            list_link.clean()
            c = randint(1, 2 ** 30)
            list_link.delete(c,True)
            self.assertEqual([],list_link.to_list())
            self.assertEqual(list_link.head, None)
            self.assertEqual(list_link.tail, None)

    def test_OneNumberFalse(self):
        list_link = inlet.LinkedList2()
        for i in range(100000):
            a = randint(0,2**30)
            list_link.add_in_tail(inlet.Node(a))
            list_link.delete(a,False)
            self.assertEqual([],list_link.to_list())
            self.assertEqual(list_link.head, None)
            self.assertEqual(list_link.tail, None)

    def test_OneNumberTrue(self):
        list_link = inlet.LinkedList2()
        for i in range(100000):
            a = randint(0,2**30)
            list_link.add_in_tail(inlet.Node(a))
            list_link.delete(a,True)
            self.assertEqual([],list_link.to_list())
            self.assertEqual(list_link.head, None)
            self.assertEqual(list_link.tail, None)

    def test_deleteFromHeadFalse(self):
        list_link = inlet.LinkedList2()
        ar1 = []
        for j in range(100):
            list_link.clean()
            ar1.clear()
            a = 2 ** 30 + 1
            list_link.add_in_tail(inlet.Node(a))
            for i in range(100000):
                b = randint(0, 2 ** 30)
                list_link.add_in_tail(inlet.Node(b))
                ar1.append(b)

            list_link.delete(a, False)

            self.assertEqual(ar1, list_link.to_list())
            self.assertEqual(list_link.find(a), None)
            self.assertEqual(list_link.head.value, ar1[0])
            self.assertEqual(list_link.head.next.value, ar1[1])
            self.assertEqual(list_link.tail.value, ar1[-1])
            self.assertEqual(list_link.tail.prev.value, ar1[-2])

    def test_deleteFromHeadTrue(self):
        list_link = inlet.LinkedList2()
        ar1 = []
        for j in range(1000):
            a = 2 ** 30 + 1
            list_link.add_in_tail(inlet.Node(a))
        for i in range(100000):
            b = randint(0, 2 ** 30)
            list_link.add_in_tail(inlet.Node(b))
            ar1.append(b)

        list_link.delete(a, True)

        self.assertEqual(ar1, list_link.to_list())
        self.assertEqual(list_link.find(a),None)
        self.assertEqual(list_link.head.value, ar1[0])
        self.assertEqual(list_link.head.next.value, ar1[1])
        self.assertEqual(list_link.tail.value, ar1[-1])
        self.assertEqual(list_link.tail.prev.value, ar1[-2])

    def test_deleteFromTailFalse(self):
        list_link = inlet.LinkedList2()
        ar1 = []
        for j in range(100):
            list_link.clean()
            ar1.clear()

            for i in range(100000):
                b = randint(0, 2 ** 30)
                list_link.add_in_tail(inlet.Node(b))
                ar1.append(b)
            a = 2 ** 30 + 1
            list_link.add_in_tail(inlet.Node(a))
            list_link.delete(a, False)

            self.assertEqual(ar1, list_link.to_list())
            self.assertEqual(list_link.find(a), None)
            self.assertEqual(list_link.head.value, ar1[0])
            self.assertEqual(list_link.head.next.value, ar1[1])
            self.assertEqual(list_link.tail.value, ar1[-1])
            self.assertEqual(list_link.tail.prev.value, ar1[-2])

    def test_deleteFromTailTrue(self):
        list_link = inlet.LinkedList2()
        ar1 = []


        for i in range(100000):
            b = randint(0, 2 ** 30)
            list_link.add_in_tail(inlet.Node(b))
            ar1.append(b)

        for j in range(100000):
            a = 2 ** 30 + 1
            list_link.add_in_tail(inlet.Node(a))

        list_link.delete(a, True)

        self.assertEqual(ar1, list_link.to_list())
        self.assertEqual(list_link.find(a),None)
        self.assertEqual(list_link.head.value, ar1[0])
        self.assertEqual(list_link.head.next.value, ar1[1])
        self.assertEqual(list_link.tail.value, ar1[-1])
        self.assertEqual(list_link.tail.prev.value, ar1[-2])

    def test_deleteFromMiddleFalse(self):
        list_link = inlet.LinkedList2()
        ar1 = []
        dim = 50000
        list_link.clean()
        ar1.clear()

        for i in range(dim):
            b = randint(0, 2 ** 30)
            list_link.add_in_tail(inlet.Node(b))
            ar1.append(b)

        a = 2 ** 30 + 1
        list_link.add_in_tail(inlet.Node(a))

        for i in range(dim):
            b = randint(0, 2 ** 30)
            list_link.add_in_tail(inlet.Node(b))
            ar1.append(b)

        list_link.delete(a, False)

        self.assertEqual(ar1, list_link.to_list())
        self.assertEqual(list_link.find(a),None)
        self.assertEqual(list_link.head.value, ar1[0])
        self.assertEqual(list_link.head.next.value, ar1[1])
        self.assertEqual(list_link.tail.value, ar1[-1])
        self.assertEqual(list_link.tail.prev.value, ar1[-2])

    def test_deleteFromMiddleTrue(self):
        list_link = inlet.LinkedList2()
        ar1 = []
        dim = 50000
        list_link.clean()
        ar1.clear()

        for i in range(dim):
            b = randint(0, 2 ** 30)
            list_link.add_in_tail(inlet.Node(b))
            ar1.append(b)
        for i in range(dim):
            a = 2 ** 30 + 1
            list_link.add_in_tail(inlet.Node(a))

        for i in range(dim):
            b = randint(0, 2 ** 30)
            list_link.add_in_tail(inlet.Node(b))
            ar1.append(b)

        list_link.delete(a, True)

        self.assertEqual(ar1, list_link.to_list())
        self.assertEqual(list_link.find(a),None)
        self.assertEqual(list_link.head.value, ar1[0])
        self.assertEqual(list_link.head.next.value, ar1[1])
        self.assertEqual(list_link.tail.value, ar1[-1])
        self.assertEqual(list_link.tail.prev.value, ar1[-2])

if __name__ == '__main__':
    unittest.main()

