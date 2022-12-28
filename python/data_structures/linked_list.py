class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.head = None

    def append(self, value):
        self.linked_list.append(Node(value))

    def insert_before(self, find, value):
        newNode = Node(value)
        node = self.head
        if node is not None:
            if node.value == find:
                newNode.next = self.head
                self.head = newNode
            while node.next is not None:
                if node.next.value == find:
                    newNode.next = node.next
                    node.next = newNode
                    return
                else:
                    node = node.next

    def insert_after(self, find, value):
        pass

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        values = []
        current = self.head
        while current is not None:
            values.append("{ " + str(current.value) + " }")
            current = current.next
        if len(values) == 0:
            return "NULL"
        return " -> ".join(values) + " -> NULL"


class TargetError:
    pass
