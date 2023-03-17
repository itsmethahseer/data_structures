class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class Singly:
    def __init__(self):
        self.head = None
        self.tail = None

    def printNode(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def addNode(self, val):
        newNode = Node(val)
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode







list1 = Singly()
list1.addNode(1)
list1.addNode(3)
list1.addNode(2)
list1.addNode(9)

list1.printNode()




