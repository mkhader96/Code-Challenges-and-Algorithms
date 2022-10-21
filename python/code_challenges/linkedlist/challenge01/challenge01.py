from xml.dom.minidom import Element


class Node:
    def __init__(self,value):
        self.value = value
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
    ll = LinkedList()
    for i in list:
        ll.append(Node(i))
    ll.delete(value)
    return ll.printAll()


    
