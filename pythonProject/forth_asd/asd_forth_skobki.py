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

# функция для задания
def skobki(s:str)->bool:
    stack = Stack()
    st = list(s)

    # заполнение стека элементами списка
    for i in range(len(st)):
        stack.push(st[i])

    # счетчики
    i = 0
    k = 0
    # удаление элементов стека в циклах
    while stack.peek() == ')':
        stack.pop()
        i += 1
        while stack.peek() == '(':
            stack.pop()
            k += 1
    return i == k and i != 0 and k != 0

s = '(())(())'
print(skobki(s))


