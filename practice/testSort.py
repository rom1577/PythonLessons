import unittest
from sort import sortlist
from random import randint

# приводится в пример пять видов тестов для функции сортировки массива по возрастанию
class DefTest(unittest.TestCase):

    # проверка корректности работы программы, если подать в функцию сортировки пустой массив
    def test_1(self):
        self.assertEqual(sortlist([]), [])
   
    # проверка корректности работы программы на обычном массиве небольшой длины
    def test_2(self):
        self.assertEqual(sortlist([50, 4, 10, 5, 0]), [0, 4, 5, 10, 50])
    
    # проверка корректности работы программы, если массив состоит из одинаковых элементов
    def test_3(self):
        a = randint(0, 10)
        b = []
        for i in range(10):
            b.append(a) 
        self.assertEqual(sortlist(b), b)

    # проверка корректности работы программы, если в массиве "большие" числа
    def test_4(self):
        a = list(range(1010, 1000, -1))
        b = list(range(1001, 1011))
        self.assertEqual(sortlist(a), b)

    # проверка корректности работы программы, если массив состоит из элементов типа str и int
    def test_5(self):
         with self.assertRaises(TypeError):
             sortlist(["1", "2", 0, -9])

if __name__ == '__main__':
    unittest.main()
       
    


