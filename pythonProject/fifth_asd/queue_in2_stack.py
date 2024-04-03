class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() != 0:
            a = self.stack[0]
            b = self.stack
            b.pop(0)
            self.stack = b
            return a
        return None

    def push(self, value):
        self.stack.insert(0,value)
    def peek(self):
        if self.size() != 0:
            return self.stack[0]
        return None

    def to_list(self):
        a = []
        for i in range(self.size()):
            a.append(self.stack[i])
        return a


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack2.size() != 0:
            return self.stack2.pop()
        elif self.stack1.size() != 0:
            for i in range(self.stack1.size()):
                self.stack2.push(self.stack1.pop())
            return self.stack2.pop()
        return None

