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
        self.stack.append(value)

    def peek(self):
        if self.size() != 0:
            return self.stack[0]
        return None

    def to_list(self):
        a = []
        for i in range(self.size()):
            a.append(self.stack[i])
        return a


stack1 = Stack()
stack2 = Stack()

stack1.push(8)
stack1.push(2)
stack1.push('+')
stack1.push(5)
stack1.push('*')
stack1.push(9)
stack1.push('+')
stack1.push('=')

# функция выполнения суммы или произведения двух чисел
def operation(a:int,b:int,s:str)->int:
    d = {"+": a+b,
         "*": a*b}
    return d[s]

# функция для задания. В качестве верхушки стека - голова списка
def postfix(stack1:Stack)->int:
    stack2 = Stack()
    for i in range(stack1.size()):
        # если вершина стека 1 символ "=", то выход из функции
        if stack1.peek() == '=':
            return stack2.pop()

        # записываем число из стека 1 в стек 2
        a = stack1.pop()
        stack2.push(a)

        # если элемент стека типа строка, то выполняем
        # сложение или умножение двух элементов стека 2.
        # Результат помещаем в стек 2.
        if type(stack1.peek()) == str:
            b = stack2.pop()
            c = stack2.pop()
            stack2.push(operation(b,c,stack1.peek()))
            stack1.pop()

print("Ответ =",postfix(stack1))

