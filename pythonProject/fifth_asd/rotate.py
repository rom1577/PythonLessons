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
        return len(self.queue) # размер очереди

    def to_list(self):
        a = []
        for i in range(self.size()):
            a.append(self.queue[i])
        return a

def rotate(queue:Queue,N:int)->Queue:
    if queue.size() != 0:
        for i in range(N):
            a = queue.dequeue()
            queue.enqueue(a)
        return queue
    return None

