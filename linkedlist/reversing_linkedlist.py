class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    def addnode(self,data):
        newnode = Node(data)
        if self.tail is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode

    def listprint(self):
        temp = self.head
        while temp is not None:
            print(temp.data, "-->", end='')
            temp = temp.next

llist = LinkedList()
llist.addnode(1)
llist.addnode(2)
llist.addnode(3)
llist.addnode(4)
llist.reverse()
llist.listprint()