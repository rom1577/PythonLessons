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
        if self.__ascending and value >= self.tail.value:
            self.add_in_tail(node)
        elif self.__ascending and value <= self.head.value:
            self.add_in_head(node)

        elif not self.__ascending and value >= self.head.value:
            self.add_in_head(node)
        elif not self.__ascending and value <= self.tail.value:
            self.add_in_tail(node)

        elif self.__ascending:
            val1 = self.head
            while self.compare(node.value,val1.value) == 1:
                val1 = val1.next
            node.prev = val1.prev
            val1.prev.next = node
            val1.prev = node
            node.next = val1
        elif not self.__ascending:
            val1 = self.head
            while self.compare(node.value,val1.value) == -1:
                val1 = val1.next
            node.prev = val1.prev
            val1.prev.next = node
            val1.prev = node
            node.next = val1

    def find(self, val):
        val1 = self.head
        if self.__ascending:
            while self.compare(val,val1.value) == 1 and val1.next is not None:
                val1 = val1.next
            if self.compare(val,val1.value) == -1 or val > val1.value:
                return None
            return val1.value

        elif not self.__ascending:
            while self.compare(val,val1.value) == -1 and val1.next is not None:
                val1 = val1.next
            if self.compare(val,val1.value) == 1 or val < val1.value:
                return None
            return val1.value

    def delete(self, val):
        val1 = self.head
        prev_node = None
        while self.compare(val, val1.value) != 0 and val1.next is not None:
            prev_node = val1
            val1 = val1.next
        if val1.prev is None:
            self.head = val1.next
        elif val1.next is None and val == self.tail.value:
            self.tail = prev_node
            self.tail.prev = prev_node.prev
            prev_node.next = None
        elif val1.value != self.tail.value:
            val1.next.prev = val1.prev
            val1.prev.next = val1.next

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
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode

    def add_in_tail(self, item):
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

