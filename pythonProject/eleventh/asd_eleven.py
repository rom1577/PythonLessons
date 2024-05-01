class BloomFilter:
    def __init__(self, f_len):
        self.filter_len = f_len
        self.arr = [0] * f_len

    def hash1(self, str1):
        sum = 0
        const = 17
        for c in str1:
            if sum == 0:
                sum = 1
            code = ord(c)
            sum = (sum * (const + code)) % self.filter_len
        return sum

    def hash2(self, str1):
        sum = 0
        const = 223
        for c in str1:
            if sum == 0:
                sum = 1
            code = ord(c)
            sum = (sum * (const + code)) % self.filter_len
        return sum

    def add(self, str1):
        res1 = self.hash1(str1)
        res2 = self.hash2(str1)
        self.arr[res1] |= 1
        self.arr[res2] |= 1

    def is_value(self, str1):
        res1 = self.hash1(str1)
        res2 = self.hash2(str1)
        if self.arr[res1] == 1 and self.arr[res2] == 1:
            return True
        return False

