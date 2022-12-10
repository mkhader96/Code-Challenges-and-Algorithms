import pytest
from challenge01 import Solution, Tree


def test_sum_bst():
    tree1 = Tree(7)
    tree1.left = Tree(2)
    tree1.left.left = Tree(1)
    tree1.left.right = Tree(5)
    tree1.right = Tree(9)
    tree1.right.right = Tree(14)
    actual = Solution(tree1, 3)
    expected = True
    assert actual == expected


def test1_sum_bst():
    tree1 = Tree(7)
    tree1.left = Tree(2)
    tree1.left.left = Tree(1)
    tree1.left.right = Tree(5)
    tree1.right = Tree(9)
    tree1.right.right = Tree(14)
    actual = Solution(tree1, 4)
    expected = False
    assert actual == expected

def test2_sum_bst():
    tree1 = Tree(8)
    tree1.left = Tree(4)
    tree1.left.left = Tree(2)
    tree1.left.right = Tree(6)
    tree1.right = Tree(15)
    tree1.right.right = Tree(16)
    actual = Solution(tree1, 21)
    expected = True
    assert actual == expected

