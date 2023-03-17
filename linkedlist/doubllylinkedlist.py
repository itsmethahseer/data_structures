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

            self.tail = newNode
    def insert_beginning(self,data):
        n= Node(data)
        temp = self.head
        temp.pref= n
        n.nref = temp
        self.head =n
    def insert_position(self,pos,data):
        n= Node(data)
        temp = self.head
        for i in range(1,pos-1):
            temp = temp.nref
        n.pref = temp
        n.nref = temp.nref
        temp.nref.pref = n
        temp.nref =n
    def display(self):
        current = self.head
        if (self.head == None):
            print("List is empty")
            return
        print("Nodes of doubly linked list: ")
        while (current != None):
            print("<--",current.data,"-->",end="")
            current = current.nref
    def remove_duplicates(self):
        temp =self.head
        while temp.nref !=None:
            if temp.data ==temp.nref.data:
                # delete the next node
                temp.nref= temp.nref.nref
            else:
                temp = temp.nref










dList = DoublyLinkedList()
dList.addNode(1)
dList.addNode(2)
dList.addNode(3)
dList.addNode(4)
dList.addNode(5)
dList.addNode(6)
dList.addNode(8)
dList.addNode(8)
dList.addNode(8)
# dList.remove_duplicates()
# dList.insert_beginning(15)
# dList.insert_position(3,100)


dList.display()
