class BloomFilter:
    def __init__(self, f_len):
        self.filter_len = f_len
        self.arr = 0

    def hash1(self, str1):
        sum = 0
        const = 17
        for i in range(len(str1)):
            if i == 0:
                continue
            code = ord(str1[i])
            sum = (sum * const + code) % self.filter_len
        return sum

    def hash2(self, str1):
        sum = 0
        const = 223
        for i in range(len(str1)):
            if i == 0:
                continue
            code = ord(str1[i])
            sum = (sum * const + code) % self.filter_len
        return sum

    def add(self, str1):
        res1 = self.hash1(str1)
        res2 = self.hash2(str1)
        self.arr |= 1 << (self.filter_len - res1 - 1)
        self.arr |= 1 << (self.filter_len - res2 - 1)

    def is_value(self, str1):
        res1 = self.hash1(str1)
        res2 = self.hash2(str1)
        if bin(self.arr)[2:].zfill(self.filter_len)[res1] == '1' and bin(self.arr)[2:].zfill(self.filter_len)[res2] == '1':
            return True
        return False

