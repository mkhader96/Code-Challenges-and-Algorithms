import pytest
from challenge02 import *


def createLinkedList(list):
    '''A function to take a list as input and return the middle node'''
    ll = LinkedList()
    for i in list:
        ll.append(Node(i))
    ll.printAll()
    return ll





def test_middle():
    ll = createLinkedList([1,2,3,4,5,6])
    
    actual = ll.middleNode()
    expected = 4
    assert actual == expected

def test_middle1():
    ll = createLinkedList([1,2,3,4,5,6])  
    actual = ll.middleNode()
    expected = 4
    assert actual == expected

def test_middle2():
    ll = createLinkedList(['A','B','C','D','E','F','G'])  
    actual = ll.middleNode()
    expected = 'D'
    assert actual == expected

def test_middle3():
    ll = createLinkedList(['A','B','C','D','E','F','G','H'])  
    actual = ll.middleNode()
    expected = 'E'
    assert actual == expected