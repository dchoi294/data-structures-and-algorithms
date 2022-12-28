class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        # initialization here
        self.head = None

    def __str__(self):
        current = self.head
        text = ""
        while current:
            node_string = "{ " + current.value + " } -> "
            text += node_string
            current = current.next
        return text + "NULL"

    def insert(self, value):
        # new_node = Node(value)
        # new_node.next = self.head
        # self.head = new_node

        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value):
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def insert_before(self, find, value):
        current = self.head
        old = None
        try:
            while current.value is not find:
                old = current
                current = current.next
            if old is not None:
                old.next = Node(value, current)
            if old is None:
                self.head = Node(value, current)
        except Exception as error:
            raise TargetError(error)

    def insert_after(self, find, value):
        current = self.head
        try:
            while current.value is not find:
                current = current.next
            new = Node(value)
            new.next = current.next
            current.next = new
        except Exception as error:
            raise TargetError(error)

    def kth_from_end(self, k):
        if k < 0:
            raise TargetError()
        current = self.head
        ll_list = []
        try:
            while current:
                ll_list.append(current.value)
                current = current.next
            return ll_list[-k-1]
        except Exception as error:
            raise TargetError(error)


class TargetError(Exception):
    pass
