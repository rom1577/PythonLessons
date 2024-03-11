class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        # здесь будет ваш код
            lenth = self.len()
            arr = []
            node = self.head
            for i in range(lenth):
                if node.value == val:
                    arr.append(node)
                node = node.next
            return arr

    def delete(self, val, all=False):
        # здесь будет ваш код
        node = self.head
        prev_node = None
        while node is not None:
            if node.value == val:
                if prev_node is None:
                    self.head = node.next
                    if self.head is None:
                        self.tail = None
                else:
                    prev_node.next = node.next
                    if node.next is None:
                        self.tail = prev_node
                if all:
                    self.delete(val, all=False)
                else:
                    break
            prev_node = node
            node = node.next

    def clean(self):
        # здесь будет ваш код
        self.head = None
        self.tail = None

    def len(self):
        # здесь будет ваш код
        numb = 0
        node = self.head
        while node is not None:
            numb += 1
            node = node.next
        return numb

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode



# n1 = Node(12)
# n2 = Node(55)
# n1.next = n2
# print(n2.value)
s_list = LinkedList()
#
s_list.add_in_tail(Node(11))
s_list.add_in_tail(Node(11))
s_list.add_in_tail(Node(55))
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(11))
s_list.add_in_tail(Node(11))
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(15))
# s_list.delete(55,all = True)
s_list.len()
print(s_list.print_all_nodes())
# print(s_list.find_all())
print()
g = s_list.find(15)
s_list.insert(None,Node(99))
print(s_list.print_all_nodes())
s_list.clean()
print(s_list.len())
# print(s_list.print_all_nodes())
# s_list.print_all_nodes()

