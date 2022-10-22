

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        '''A function that adds a new node with the given value to the end of the list'''
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def printAll(self):
        '''A function that returns all the values in the linked list'''
        elements = []
        if self.head is None:
            print("The linked list is empty")
        else:
            current = self.head
            while current is not None:
                elements.append(current.value)
                current = current.next
        return elements

    def delete(self, value):
        '''A function that takes any value as an argument and removes the first node with that value from the list'''
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current.next is not None:
                if current.next.value == value:
                    current.next = current.next.next
                else:
                    current = current.next


def deleteNodefromlist(list,value):
    '''A function that takes a list and a value, converts the list to a linekd list and remove the node with the given value. Then returns the linked list as a list'''
    ll = LinkedList()
    for i in list:
        ll.append(Node(i))
    ll.delete(value)
    return ll.printAll()



    
