import second_asd.second_asd  as inlet
from random import randint
import unittest

class DelTest(unittest.TestCase):

    def test_NoneEmptyListInsert(self):
        list_link = inlet.LinkedList2()
        for i in range(10000):
            list_link.clean()
            a1 = inlet.Node(i)

            list_link.insert(None,a1)

            self.assertEqual(list_link.to_list(),[a1.value])
            self.assertEqual(list_link.head.value,a1.value)
            self.assertEqual(list_link.tail.value,a1.value)
            self.assertEqual(list_link.tail.next, None)
            self.assertEqual(list_link.head.next,None)
            self.assertEqual(list_link.head.value, list_link.tail.value)

    def test_NoneListInsert(self):
        list_link = inlet.LinkedList2()
        ar1 = []

        for i in range(10000):
            a = randint(0, 2 ** 30)
            list_link.add_in_tail(inlet.Node(a))
            ar1.append(a)
        for i in range(10000):
            a1 = inlet.Node(i)
            ar1.append(i)
            list_link.insert(None, a1)

            self.assertEqual(list_link.to_list(),ar1)
            self.assertEqual(ar1[-1],list_link.tail.value)
            self.assertEqual(None,list_link.tail.next)
            self.assertEqual(ar1[-2], list_link.tail.prev.value)

    def test_FullInsert(self):
        list_link = inlet.LinkedList2()
        a_array = []
        ver_arr = []
        const = 2 ** 30 + 1

        for i in range(10000):
            a = inlet.Node(randint(0,2 ** 30))
            a_array.append(a) # массив узлов
            list_link.add_in_tail(a_array[i])
            ver_arr.append(a.value) # массив значений

        for i in range(10000):
            c = inlet.Node(const)
            list_link.insert(a_array[i],c)
            ver_arr.insert(i+1,c.value)

            node = list_link.head
            j = 0
            while j != i + 1:
                self.assertEqual(node.value, ver_arr[j])
                if j != i:
                    self.assertEqual(node.next.value, ver_arr[j+1])
                if j != 0:
                    self.assertEqual(node.prev.value, ver_arr[j-1])
                node = node.next
                j += 1

            self.assertEqual(list_link.to_list(),ver_arr)
            self.assertEqual(list_link.head.value,ver_arr[0])
            self.assertEqual(list_link.tail.value,ver_arr[-1])

            list_link.delete(const,False)
            ver_arr.pop(i+1)

    def test_Ignore(self):
        list_link = inlet.LinkedList2()
        a_array = []
        ver_arr = []
        const = 2 ** 30 + 1

        for i in range(1000):
            a = inlet.Node(randint(0,2 ** 30))
            a_array.append(a)
            list_link.add_in_tail(a_array[i])
            ver_arr.append(a.value)

            list_link.insert(inlet.Node(const),inlet.Node(const))

            self.assertEqual(list_link.len(), i+1)
            self.assertEqual(list_link.to_list(),ver_arr)
            self.assertEqual(list_link.head.value, ver_arr[0])
            self.assertEqual(list_link.tail.value, ver_arr[-1])

if __name__ == '__main__':
    unittest.main()