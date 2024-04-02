class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0,item)

    def dequeue(self):
        if self.size() != 0:
            a = self.queue[-1]
            b = self.queue
            b.pop(-1)
            self.queue = b
            return a
        return None

    def size(self):
        return len(self.queue)

