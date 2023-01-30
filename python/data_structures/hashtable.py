class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        if not self.head:
            return "NULL"
        current = self.head
        string = ""
        while current:
            string += str(current.value) + " -> "
            current = current.next
        string += "NULL"
        return string

    def insert(self, item):
        old = self.head
        self.head = Node(item)
        self.head.next = old

    def display(self):
        current = self.head
        lst = []
        while current:
            lst.append(current.value)
            current = current.next
        return lst[::-1]


class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    # The hashing algorithm
    def _hash(self, key):
        hashed = 0

        for char in key:
            hashed += ord(char)

        hashed = (hashed * 19) % self.size

        return hashed

    def set(self, key, value):
        hashed_key = self._hash(key)
        bucket = self._buckets[hashed_key]

        if not bucket:
            self._buckets[hashed_key] = LinkedList()

        self._buckets[hashed_key].insert([key, value])

    def get(self, key):
        hashed_key = self._hash(key)
        bucket = self._buckets[hashed_key]

        if bucket:
            current = bucket.head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next

        return False

    def keys(self):
        buckets = self._buckets
        filled_buckets = []
        keys = []
        for x in buckets:
            if x is not None:
                filled_buckets.append(x)
        for y in filled_buckets:
            keys.insert(0, y.head.value[0])
        return keys

    def has(self, key):
        keys = self.keys()
        for x in keys:
            if x == key:
                return True
        return False
