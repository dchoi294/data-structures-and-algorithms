from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        while self.stack2.top:
            item = self.stack2.pop()
            self.stack1.push(item)
        self.stack1.push(value)

    def dequeue(self):
        while self.stack1.top:
            item = self.stack1.pop()
            self.stack2.push(item)
        return self.stack2.pop()
