from data_structures.binary_tree import BinaryTree


def tree_intersection(tree1, tree2):
    result, progress = [], {}

    def walk(root, is_first_tree):
        if is_first_tree and root.value not in progress:
            progress[root.value] = 1
        if root.value in progress and not is_first_tree:
            result.append(root.value)
        if root.left:
            walk(root.left, is_first_tree)
        if root.right:
            walk(root.right, is_first_tree)
    if tree1.root and tree2.root:
        walk(tree1.root, True)
        walk(tree2.root, False)
    return set(result)
