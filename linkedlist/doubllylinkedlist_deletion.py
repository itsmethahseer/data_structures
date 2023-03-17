class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def addNode(self, data): #at the end of the linkedlist
        newNode = Node(data)

        if (self.head == None):
            self.head = self.tail = newNode
            self.head.nref = None
            self.tail.pref = None
        else:
            self.tail.nref = newNode
            newNode.pref = self.tail
            self.tail = newNode

    def display(self):
        current = self.head
        if (self.head == None):
            print("List is empty")
            return
        print("Nodes of doubly linked list: ")
        while (current != None):
            print(current.data)
            current = current.nref


    def delete_beginning(self):
        temp = self.head
        self.head = temp.nref
        temp.nref = None
        self.head.pref = None


    def delete_end(self):
        temp = self.head.nref
        before = self.head  #node with just before temp
        while temp.nref is not None:
            temp = temp.nref
            before = before.nref
        before.nref = None
        temp.prev = None
    def delete_position(self,pos):
        temp = self.head.nref
        before = self.head
        for i in range(1,pos-1):
            temp = temp.nref
            before = before.nref
        before.nref = temp.nref
        temp.nref.pref = before
        temp.nref = None
        before.pref = None

    def reverse(self):
        pref = None
        current = self.head
        while (current is not None):
            nref = current.nref
            current.nref = pref
            pref = current
            current = nref
        self.head = pref











dList = DoublyLinkedList()
dList.addNode(1)
dList.addNode(2)
dList.addNode(3)
dList.addNode(4)
dList.addNode(5)
# dList.delete_beginning()

# dList.delete_end()
# dList.delete_position(3)
dList.reverse()
dList.display()
