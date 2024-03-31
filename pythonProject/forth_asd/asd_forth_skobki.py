class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() != 0:
            a = self.stack[-1]
            b = self.stack
            b.pop(-1)
            self.stack = b
            return a
        return None

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() != 0:
            return self.stack[-1]
        return None

    def to_list(self):
        a = []
        for i in range(self.size()):
            a.append(self.stack[i])
        return a

def skobki2(s: str) -> bool:
    stack = Stack()
    st = list(s)
    for i in st:
        while i == '(':
            stack.push(i)
            break
        while stack.peek() is None:
            return False
        while i == ')':
            stack.pop()
            break
    return stack.size() == 0

