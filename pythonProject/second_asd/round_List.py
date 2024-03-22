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
        self.dummy = Node_dum()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def add_in_head(self, newNode):
        node = self.dummy.next
        newNode.prev = self.dummy
        self.dummy.next = newNode
        newNode.next = node
        node.prev = newNode

    def add_in_tail(self, item):
        node = self.dummy.prev
        item.next = self.dummy
        self.dummy.prev = item
        item.prev = node
        node.next = item

    def print_all_nodes(self):
        node = self.dummy.next
        while type(node) != Node_dum:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.dummy.next
        while type(node) != Node_dum:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        lenth = self.len()
        arr = []
        node = self.dummy.next
        for i in range(lenth):
            if node.value == val:
                arr.append(node)
            node = node.next
        return arr

    def delete(self, val, all=False):
        node = self.dummy.next
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
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def len(self):
        numb = 0
        node = self.dummy.next
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
        node = self.dummy.next
        while type(node) != Node_dum:
            ar.append(node.value)
            node = node.next
        return ar

