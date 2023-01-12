from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.front is None:
            self.front = new_node
        if self.back:
            self.back.next = new_node
            self.back = self.back.next
        else:
            self.back = new_node

    def dequeue(self):
        try:
            dequeued = self.front
            self.front = self.front.next
            return dequeued.value
        except Exception as e:
            raise InvalidOperationError(e)

    def peek(self):
        try:
            return self.front.value
        except Exception as e:
            raise InvalidOperationError(e)

    def is_empty(self):
        return self.front is None
