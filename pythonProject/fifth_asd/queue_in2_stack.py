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

#  класс очереди наследуется от класса стека
class Queue(Stack):
    def __init__(self):
        super().__init__()  # создание первого стека
        self.stack2 = Stack()

    def enqueue(self, item):
        self.push(item)  # вызов метода push для первого стека

    def dequeue(self):
        if self.size() != 0:
            m = self.size()
            for i in range(m):
                self.stack2.push(self.pop())

            res = self.stack2.pop()  # искомый головной элемент из первого стека

            # в цикле перебрасываются элементы из второго стека в первый
            for i in range(m-1):
                self.push(self.stack2.pop())
            return res
        return None

