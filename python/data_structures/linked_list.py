class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.head = None

    def insert(self, value):
        # method body here
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


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class TargetError:
    pass
