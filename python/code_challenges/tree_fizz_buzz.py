from data_structures.kary_tree import KaryTree
import copy


def fizz_buzz_tree(tree):

    def fizz_buzz(root):
        if root.value % 3 == 0 and root.value % 5 == 0:
            root.value = "FizzBuzz"
        elif root.value % 3 == 0:
            root.value = "Fizz"
        elif root.value % 5 == 0:
            root.value = "Buzz"
        else:
            root.value = str(root.value)
        for x in root.children:
            fizz_buzz(x)
        return root

    if not tree.root:
        return KaryTree()
    new_tree = copy.deepcopy(tree)
    new_tree.root = fizz_buzz(new_tree.root)
    return new_tree


