from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.top = None

    def push(self, value):
        # method body here
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        try:
            value = self.top.value
            self.top = self.top.next
            return value
        except Exception as error:
            raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):
        try:
            return self.top.value
        except Exception as error:
            raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        return self.top is None
