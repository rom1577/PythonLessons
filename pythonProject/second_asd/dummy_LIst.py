class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class Node_dum(Node):
    def __init__(self):
        super().__init__(None)

class LinkedList2:
    def __init__(self):
        self.head = Node_dum()
        self.tail = Node_dum()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_in_head(self, newNode):
        node = self.head.next
        node.prev = newNode
        newNode.next = node
        newNode.prev = self.head
        self.head.next = newNode

    def add_in_tail(self, item):
        node = self.tail.prev
        node.next = item
        item.prev = node
        item.next = self.tail
        self.tail.prev = item

    def print_all_nodes(self):
        node = self.head.next
        while node.value is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head.next
        while node.value is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        lenth = self.len()
        arr = []
        node = self.head.next
        for i in range(lenth):
            if node.value == val:
                arr.append(node)
            node = node.next
        return arr

    def delete(self, val, all=False):
        node = self.head.next
        prev_node = node
        while node.value is not None:
            if node.value == val:
                prev_node.next = node.next
                node = node.next
                node.prev = prev_node
                if not all:
                    break
                continue
            prev_node = node
            node = node.next

    def clean(self):
        self.head.next = self.tail
        self.tail.prev = self.head

    def len(self):
        numb = 0
        node = self.head.next
        while node.value is not None:
            numb += 1
            node = node.next
        return numb

    def insert(self, afterNode, newNode):
        node = afterNode.next
        afterNode.next = newNode
        newNode.prev = afterNode
        newNode.next = node
        node.prev = newNode

    def to_list(self):
        ar = []
        node = self.head.next
        while node.value is not None:
            ar.append(node.value)
            node = node.next
        return ar

s_list = LinkedList2()
a1 = Node(1)
a2 = Node(8)
a3 = Node(5)

a4 = Node(8)
a5 = Node(8)
# s_list.add_in_tail(a1)
# s_list.add_in_tail(a2)
# s_list.add_in_tail(a3)
# s_list.add_in_tail(a4)
# s_list.add_in_tail(a5)
# s_list.insert(a5, Node(10))
# s_list.delete(16,True)
# print(s_list.find(10).value)
# print()
# print(s_list.len())
# print()
# print(s_list.find_all(8))
# print()
# s_list.clean()
# print(s_list.len())
# print(s_list.len())
# print(s_list.head.value)
# print()
s_list.print_all_nodes()

# a2 = Node(2)

# s_list.add_in_tail(a1)
# s_list.add_in_tail(a2)
