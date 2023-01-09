from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)

        new_node = Node(value)
        current = self.root

        while value != current.value:
            if value < current.value:
                if not current.left:
                    current.left = new_node
                    break
                current = current.left
            if value > current.value:
                if not current.right:
                    current.right = new_node
                    break
                current = current.right

    def contains(self, value):

        current = self.root

        while current:
            if value == current.value:
                return True
            if value < current.value:
                current = current.left
            if value > current.value:
                current = current.right
        return False

