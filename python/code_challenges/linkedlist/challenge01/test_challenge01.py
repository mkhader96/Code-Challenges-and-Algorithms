import pytest
from challenge01 import deleteNodefromlist

def test_one():
    actual = deleteNodefromlist([4,5,1,9], 1)
    expected = [4,5,9]
    assert actual == expected

def test_two():
    actual = deleteNodefromlist([4,5,1,9], 5)
    expected = [4,1,9]
    assert actual == expected

def test_three():
    actual = deleteNodefromlist([4,5,1,9], 4)
    expected = [5,1,9]
    assert actual == expected
def test_three():
    actual = deleteNodefromlist(['A','B','C','D'], 'C')
    expected = ['A','B','D']
    assert actual == expected

def test_four():
    actual = deleteNodefromlist(['A','B','C','D'], 'A')
    expected = ['B','C','D']
    assert actual == expected

def test_five():
    actual = deleteNodefromlist(['A','B','C','D'], 'B')
    expected = ['A','C','D']
    assert actual == expected

