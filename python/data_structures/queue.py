from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.head = None
        self.tail = None

    def enqueue(self, value):
        # method body here
        if self.tail:
            self.tail.next = Node(value)
            self.tail = self.tail.next
            return
        self.tail = self.head = Node(value)

    def dequeue(self):
        try:
            dequeued = self.head
            self.head = self.head.next
            return dequeued.value
        except Exception as e:
            raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):
        try:
            return self.head.value
        except Exception as e:
            raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        return self.head is None
