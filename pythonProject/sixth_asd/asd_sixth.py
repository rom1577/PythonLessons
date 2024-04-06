class Deque:
    def __init__(self):
        self.queue = []

    def addFront(self, item):
        self.queue.append(item)

    def addTail(self, item):
        self.queue.insert(0, item)

    def removeFront(self):
        if self.size() != 0:
            a = self.queue.pop(-1)
            return a
        return None

    def removeTail(self):
        if self.size() != 0:
            a = self.queue.pop(0)
            return a
        return None

    def size(self):
        return len(self.queue)

    def to_list(self):
        a = []
        for i in range(self.size()):
            a.append(self.queue[i])
        return a

