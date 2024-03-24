import ctypes

class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)
        pass

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1
        pass

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        if i == self.count:
            self.append(itm)
        else:
            if self.count == self.capacity:
                self.resize(2 * self.capacity)
            new_array = self.make_array(self.capacity)
            cycle_count = 0
            for j in range(self.count+1):
                if i != j:
                    new_array[j] = self.array[cycle_count]
                    cycle_count += 1
                else:
                    new_array[j] = itm
            self.array = new_array
            self.count += 1

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')

        new_array = self.make_array(self.capacity)
        cycle_count = 0
        for j in range(self.count):
            if i == j:
                continue
            new_array[cycle_count] = self.array[j]
            cycle_count += 1
        self.array = new_array
        self.count -= 1
        new_capacity = int(self.capacity / 1.5)
        if self.count / self.capacity < 0.5 and new_capacity >= 16:
            self.resize(new_capacity)

    def to_list(self):
        a = []
        for i in range(self.__len__()):
            a.append(self.array[i])
        return a

