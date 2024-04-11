class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        return 1

    def add(self, value):
        node = Node(value)

        if self.head is None:
            self.add_in_tail(node)

        elif self.__ascending and (self.compare(value,self.tail.value) == 1 or self.compare(value,self.tail.value) == 0):
            self.add_in_tail(node)
        elif self.__ascending and (self.compare(value,self.head.value) == -1 or self.compare(value,self.head.value) == 0):
            self.add_in_head(node)

        elif not self.__ascending and (self.compare(value,self.head.value) == 1 or self.compare(value,self.head.value) == 0):
            self.add_in_head(node)
        elif not self.__ascending and value <= self.tail.value:
            self.add_in_tail(node)

        elif self.__ascending:
            cur_node = self.head
            while self.compare(node.value,cur_node.value) == 1:
                cur_node = cur_node.next
            node.prev = cur_node.prev
            cur_node.prev.next = node
            cur_node.prev = node
            node.next = cur_node
        elif not self.__ascending:
            cur_node = self.head
            while self.compare(node.value,cur_node.value) == -1:
                cur_node = cur_node.next
            node.prev = cur_node.prev
            cur_node.prev.next = node
            cur_node.prev = node
            node.next = cur_node

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node.value
            elif self.compare(node.value,val) == -1 and not self.__ascending:
                return None
            elif self.compare(node.value,val) == 1 and self.__ascending:
                return None
            node = node.next
        return None

    def delete(self, val):
        node = self.head
        prev_node = None
        while node is not None:
            if node.value == val and prev_node is None and node.next is not None:
                self.head = node.next
                break
            elif node.value == val and prev_node is None:
                self.head = None
                self.tail = None
                break
            elif node.value == val and prev_node is not None and node.next is None:
                self.tail = prev_node
                self.tail.prev = prev_node.prev
                prev_node.next = None
                break
            elif node.value == val and prev_node is not None and node.next is not None:
                prev_node.next = node.next
                node = node.next
                node.prev = prev_node
                break
            prev_node = node
            node = node.next

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        numb = 0
        node = self.head
        while node is not None:
            numb += 1
            node = node.next
        return numb

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r

    def add_in_head(self, newNode):
        if self.tail is None:
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        else:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def to_list(self):
        ar = []
        node = self.head
        while node is not None:
            ar.append(node.value)
            node = node.next
        return ar

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = v1.strip()
        v2 = v2.strip()
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        return 1

