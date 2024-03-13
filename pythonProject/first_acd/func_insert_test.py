import first_acd.acd_1 as inlet
from random import randint
import unittest

class DelTest(unittest.TestCase):

    def test_EmptyInsert(self):
        list_link = inlet.LinkedList()
        for i in range(10000):
            list_link.clean()
            a1 = inlet.Node(i)
            list_link.insert(None,a1)
            self.assertEqual(list_link.to_list(),[a1.value])

    def test_NoneInsert(self):
        list_link = inlet.LinkedList()
        a_array = []
        ver_arr = []
        const = 2 ** 30 + 1

        for i in range(1000):
            a = inlet.Node(randint(0,2 ** 30))
            a_array.append(a)
            list_link.add_in_tail(a_array[i])
            ver_arr.append(a.value)

        c = inlet.Node(const)
        list_link.insert(None, c)
        ver_arr.insert(0, const)
        self.assertEqual(list_link.to_list(),ver_arr)


    def test_FullInsert(self):
        list_link = inlet.LinkedList()
        a_array = []
        ver_arr = []
        const = 2 ** 30 + 1

        for i in range(1000):
            a = inlet.Node(randint(0,2 ** 30))
            a_array.append(a)
            list_link.add_in_tail(a_array[i])
            ver_arr.append(a.value)

        for i in range(1000):
            c = inlet.Node(const)
            list_link.insert(a_array[i],c)
            ver_arr.insert(i+1,c.value)
            self.assertEqual(list_link.to_list(),ver_arr)
            list_link.delete(const,False)
            ver_arr.pop(i+1)

if __name__ == '__main__':
    unittest.main()