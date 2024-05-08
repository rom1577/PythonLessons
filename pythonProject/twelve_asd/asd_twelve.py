class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        s = list(key)
        sum = 0
        for i in range(len(s)):
            sum += ord(s[i])
        return sum % self.size

    def is_key(self, key):
        if key in self.slots:
            return True
        return False

    def put(self, key, value):
        index = self.hash_fun(key)
        a = 0
        del_index = 0
        while self.slots[index] is not None:
            index = (index + 1) % self.size
            a += 1
            if a > self.size:
                for i in range(len(self.hits)):
                    if self.hits[i] == min(self.hits):
                        del_index = i
                        break
                self.slots[del_index] = None
                self.values[del_index] = None
                self.hits[del_index] = 0
                a = 0
        self.slots[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash_fun(key)
        if not self.is_key(key):
            return None
        while self.slots[index] != key:
            index = (index + 1) % self.size
        self.hits[index] += 1
        return self.values[index]

