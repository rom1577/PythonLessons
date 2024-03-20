class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        lenth = self.len()
        arr = []
        node = self.head
        for i in range(lenth):
            if node.value == val:
                arr.append(node)
            node = node.next
        return arr

    def delete(self, val, all=False):
        node = self.head
        prev_node = None
        while node is not None:
            if node.value == val:
                if prev_node is None:
                    self.head = node.next
                    node = self.head
                    if node is not None:
                        node.prev = prev_node
                    if self.head is None:
                        self.tail = None
                    if not all:
                        break
                    continue
                else:
                    if node.next is None:
                        self.tail = prev_node
                        self.tail.prev = prev_node.prev
                        prev_node.next = None
                        break
                    prev_node.next = node.next
                    node = node.next  #
                    node.prev = prev_node
                    if not all:
                        break
                    continue
            prev_node = node
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        numb = 0
        node = self.head
        while node is not None:
            numb += 1
            node = node.next
        return numb

    def insert(self, afterNode, newNode):
        if afterNode is None and self.head is not None:
            self.add_in_tail(newNode)
        elif afterNode is None and self.head is None:
            self.add_in_head(newNode)

        elif afterNode == self.tail:
            self.add_in_tail(newNode)

        elif newNode is not None:
            newNode.next = afterNode.next
            afterNode.next = newNode
            newNode.prev = afterNode

    def add_in_head(self, newNode):
        if self.tail is None:
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        else:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode
