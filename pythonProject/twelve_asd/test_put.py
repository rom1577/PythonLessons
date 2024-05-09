import twelve_asd.asd_twelve as inlet
from random import randint
import string
import random
import unittest



class Cash(unittest.TestCase):
    def test_put_None(self):
        '''
        :return: Тест на добавление ключа, когда self.slots не заполнен полностью.
        '''
        def generate_string(length):
            '''
            :param length: Длина строки.
            :return: Генератор случайно строки.
            '''
            all_symbols = string.ascii_uppercase + string.digits
            result = ''.join(random.choice(all_symbols) for _ in range(length))
            return result

        for k in range(1000):
            size = randint(1,100)
            t = randint(1,size)
            csh = inlet.NativeCache(size)
            for i in range(t):
                key_str = generate_string(randint(1, 10))
                val_str = generate_string(randint(1, 10))
                while key_str in csh.slots:
                    key_str = generate_string(randint(1, 10))
                csh.put(key_str, val_str)
                self.assertEqual(csh.get(key_str), val_str)

    def test_put_first(self):
        '''
        :return: Тест метода put, когда self.slots уже заполнен. Но тк. self.hits = [0]*size,
        то заполнение нового key идет в первый элемент self.slots
        '''
        def generate_string(length):
            '''
            :param length: Длина строки.
            :return: Генератор случайно строки.
            '''
            all_symbols = string.ascii_uppercase + string.digits
            result = ''.join(random.choice(all_symbols) for _ in range(length))
            return result

        for k in range(1000):
            size = randint(1,100)
            csh = inlet.NativeCache(size)
            for i in range(size):  # заполнили self.slots
                key_str = generate_string(randint(1, 10))
                val_str = generate_string(randint(1, 10))
                while key_str in csh.slots:
                    key_str = generate_string(randint(1, 10))
                csh.put(key_str, val_str)
            new_slots = ['']*size
            for i in range(len(csh.slots)):
                new_slots[i] = csh.slots[i]
            for i in range(size):
                new_val_str = generate_string(randint(1, 10))
                csh.put(new_slots[i],new_val_str)
                self.assertEqual(csh.values[0],new_val_str)

    def test_put_free(self):
        '''
        :return: Тест метода, когда self.slots заполнены и на вход поступают такие же ключи. Возникают коллизии.
        Отслеживается заполнение списка self.hits и выбор, удаление наименьшего элемента из self.hits при возникновении
        коллизии.
        '''
        def generate_string(length):
            '''
            :param length: Длина строки.
            :return: Генератор случайно строки.
            '''
            all_symbols = string.ascii_uppercase + string.digits
            result = ''.join(random.choice(all_symbols) for _ in range(length))
            return result

        for k in range(1000):
            size = randint(2, 10)
            csh = inlet.NativeCache(size)

            for i in range(size):  # заполнили self.slots ключами
                key_str = generate_string(randint(1, 10))
                val_str = generate_string(randint(1, 10))
                while key_str in csh.slots:
                    key_str = generate_string(randint(1, 10))
                csh.put(key_str, val_str)

            for j in range(100):  # обратились к словарю, тем самым заполнили self.hits
                csh.get(csh.slots[randint(0, size-1)])

            arr_key = [0]*size
            for i in range(size):
                arr_key[i] = csh.slots[i]
            for h in range(size):
                new_val = generate_string(randint(1, 10))
                csh.put(arr_key[h], new_val)
                for i in range(len(csh.hits)):
                    if csh.hits[i] == min(csh.hits):
                        del_index = i
                        break
                # проверка того, что наименьший элемент из self.hits обнулился
                self.assertEqual(csh.hits[del_index], 0)

                # проверка того, что ключ с коллизией встал на место удаленного ключа с наименьшим количеством обращений
                self.assertEqual(csh.slots[del_index], arr_key[h])

                for j in range(50):  #
                    csh.hits[del_index] += 1










if __name__ == '__main__':
    unittest.main()


