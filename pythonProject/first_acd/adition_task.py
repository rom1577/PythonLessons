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

    def len(self):
        numb = 0
        node = self.head
        while node is not None:
            numb += 1
            node = node.next
        return numb

def two_LinkedList(list1,list2):
    '''
    :param list1: linked list №1
    :param list2: linked list №2
    :return: a list consisting of a new linked list and error code. First
            element is linked list of values of elements which equal to the
            sum of the elements the list1 and list2 lists. Second element is the error code.
    '''
    legnth_list1 = list1.len()  # calculate the length of the linked list
    length_list2 = list2.len()
    list3 = LinkedList()  # create the new instance of the linked list
    node1 = list1.head  # set up the pointer to the head of the linked list
    node2 = list2.head
    if legnth_list1 != length_list2:
        return [[], 1]
    for i in range(length_list2):
        # add the element of the linked list. This element is the sum of the elemnts of the list1 and list2 lists
        list3.add_in_tail(Node(node1.value + node2.value))
        node1 = node1.next  # offset of the linked list pointer
        node2 = node2.next
    return [list3,0]

# the creation the instances of the linked lists
list1 = LinkedList()
list2 = LinkedList()

# set the values of linked list items
list1.add_in_tail(Node(1))
list1.add_in_tail(Node(2))
list1.add_in_tail(Node(3))

list2.add_in_tail(Node(4))
list2.add_in_tail(Node(5))
list2.add_in_tail(Node(6))

# call two_LinkedList function
list3 = two_LinkedList(list1,list2)[0]

