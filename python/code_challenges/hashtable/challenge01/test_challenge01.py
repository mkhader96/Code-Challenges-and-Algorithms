import pytest
from challenge01 import  TreeNode, Solution


def test_sum_bst():
    tree1 = TreeNode(7)
    tree1.left = TreeNode(2)
    tree1.left.left = TreeNode(1)
    tree1.left.right = TreeNode(5)
    tree1.right = TreeNode(9)
    tree1.right.right = TreeNode(14)
    actual = Solution(tree1,7)
    expected = True
    assert actual == expected


def test1_sum_bst():
    tree1 = TreeNode(7)
    tree1.left = TreeNode(2)
    tree1.left.left = TreeNode(1)
    tree1.left.right = TreeNode(5)
    tree1.right = TreeNode(9)
    tree1.right.right = TreeNode(14)
    actual = Solution(tree1, 4)
    expected = False
    assert actual == expected

def test2_sum_bst():
    tree1 = TreeNode(8)
    tree1.left = TreeNode(4)
    tree1.left.left = TreeNode(2)
    tree1.left.right = TreeNode(6)
    tree1.right = TreeNode(15)
    tree1.right.right = TreeNode(16)
    actual = Solution(tree1, 21)
    expected = True
    assert actual == expected

