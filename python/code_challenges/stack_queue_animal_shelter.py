from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.queue = Queue()
        self.queue_next = Queue()

    def enqueue(self, value):
        self.queue.enqueue(value)

    def dequeue(self, pref):
        result = None
        while self.queue.front is not None:
            if self.queue.front.value.input == pref and result is None:
                result = self.queue.front.value
            else:
                self.queue_next.enqueue(self.queue.front.value)
            self.queue.front = self.queue.front.next
        self.queue = self.queue_next
        self.queue_next = Queue()
        return result


class Dog:
    def __init__(self):
        self.input = "dog"


class Cat:
    def __init__(self):
        self.input = "cat"
