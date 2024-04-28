class PowerSet():

    def __init__(self):
        self.sett = []

    def size(self):
        return len(self.sett)

    def put(self, value):
        if not self.get(value):
            self.sett.append(value)

    def get(self, value):
        if value in self.sett:
            return True
        return False

    def remove(self, value):
        if self.get(value):
            self.sett.remove(value)
            return True
        return False

    def intersection(self, set2):
        set3 = PowerSet()
        for i_sett in self.sett:
            if set2.get(i_sett):
                set3.put(i_sett)
        return set3

    def union(self, set2):
        set3 = PowerSet()
        for i_sett in self.sett:
            set3.put(i_sett)
        for i_set2 in set2.sett:
            set3.put(i_set2)
        return set3

    def difference(self, set2):
        set3 = PowerSet()
        for i_sett in self.sett:
            if not set2.get(i_sett):
                set3.put(i_sett)
        return set3

    def issubset(self, set2):
        for i_set2 in set2.sett:
            if not self.get(i_set2):
                return False
        return True

