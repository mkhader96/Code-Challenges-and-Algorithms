class Node:
     def __init__(self, x):
         self.val = x
         self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, node):
        '''A function to add values to the linked list'''
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def printAll(self):
        '''A function to print all the values in the linked list'''
        elements=[]
        if self.head is None:
            return("The linked list is empty")
        else:
            current = self.head
            while current is not None:
                elements.append(current.val)
                current = current.next
            return elements

    def middleNode(self):
        '''A function to find the middle node in the linked list'''
        pointer = self.head
        mid_node = self.head
        while ( pointer ) :
            if pointer.next != None :
                pointer = pointer.next.next
                mid_node = mid_node.next
            else : break
        return mid_node.val

def findMiddleNode(list):
    '''A function to take a list as input and return the middle node'''
    ll = LinkedList()
    for i in list:
        ll.append(Node(i))
    ll.printAll()
    return (ll.middleNode())


