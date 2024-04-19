class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        s = list(value)
        sum = 0
        for i in range(len(s)):
            sum += ord(s[i])
        return sum % self.size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        a = 0
        while self.slots[index] is not None:
            index = (index + self.step) % self.size
            if a > self.size:
                return None
            if a > 0 and self.step // self.size == 0 and self.step > 1 and self.step >= self.size:
                return None
            a += 1
        return index

    def put(self, value):
        sl = self.seek_slot(value)
        if sl is not None:
            self.slots[sl] = value
            return sl
        return None

    def find(self, value):
        index = self.hash_fun(value)
        a = 0
        while self.slots[index] != value:
            index = (index + self.step) % self.size
            if a > self.size:
                return None
            a += 1
        return index

