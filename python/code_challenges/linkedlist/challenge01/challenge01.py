class Node:
     def __init__(self, x):
         self.val = x
         self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def printAll(self):
        elements=[]
        if self.head is None:
            return("The linked list is empty")
        else:
            current = self.head
            while current is not None:
                elements.append(current.val)
                current = current.next
            return elements

def deleteNode(node):
    if not node:
        return
    node.val = node.next.val
    node.next = node.next.next

