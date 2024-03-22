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
        while type(node) != Node_dum:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head.next
        while type(node) != Node_dum:
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
        prev_node = node.prev
        while type(node) != Node_dum:
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
        while type(node) != Node_dum:
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
        while type(node) != Node_dum:
            ar.append(node.value)
            node = node.next
        return ar

