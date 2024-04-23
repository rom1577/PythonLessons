class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

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
        index_old = self.hash_fun(key)
        index = index_old
        a = 0
        while self.slots[index] is not None:
            index = (index + 1) % self.size
            if a > self.size:
                index = index_old
                break
            a += 1
        self.slots[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash_fun(key)
        a = 0
        while self.slots[index] != key:
            index = (index + 1) % self.size
            if a > self.size:
                return None
            a += 1
        return self.values[index]

