# Write your test here
import pytest
from challenge03 import Tree

tree=Tree()

def test_one():
    tree.root=tree.convertArrayToBST([-10,-3,0,5,9])
    expected=[0,-3,9,-10,5]
    actual=tree.breadthFirstSearch()
    assert actual==expected

def test_two():
    tree.root=tree.convertArrayToBST([1,3])
    expected=[3,1]
    actual=tree.breadthFirstSearch()
    assert actual==expected

def test_three():
    tree.root=tree.convertArrayToBST([0,1,2,3,4,5])
    expected=[3, 1, 5, 0, 2, 4]
    actual=tree.breadthFirstSearch()
    assert actual==expected

def test_four():
    tree.root=tree.convertArrayToBST([1,2,3,4,5,6,7])
    expected=[4, 2, 6, 1, 3, 5, 7]
    actual=tree.breadthFirstSearch()
    assert actual==expected
    