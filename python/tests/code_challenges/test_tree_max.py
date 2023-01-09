import pytest
from data_structures.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_max_val_2():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(70)
    tree.root.left.left = Node(60)
    tree.root.left.right = Node(50)
    tree.root.right = Node(-70)
    tree.root.right.left = Node(0)
    tree.root.right.right = Node(100)

    actual = tree.find_maximum_value()
    expected = 100

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_max_val_empty():
    tree = BinaryTree()
    actual = tree.find_maximum_value()
    expected = None
    assert actual == expected
