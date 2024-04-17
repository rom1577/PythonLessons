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
        ar = {}
        while self.slots[index] is not None:
            index = (index + self.step) % self.size
            ar[index] = None
            if len(ar) >= self.size:
                return None
        return index

    def put(self, value):
        sl = self.seek_slot(value)
        if sl is not None:
            self.slots[sl] = value
            return sl
        return None

    def find(self, value):
        index = self.hash_fun(value)
        if self.slots[index] == value:
            return index
        ar = {}
        while True:
            index = (index + self.step) % self.size
            ar[index] = None
            if self.slots[index] == value:
                return index
            if len(ar) >= self.size:
                return None

