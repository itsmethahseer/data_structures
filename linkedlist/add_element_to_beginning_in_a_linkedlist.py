# Represent a node of doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class InsertStart:
    # Represent the head and tail of the doubly linked list
    def __init__(self):
        self.head = None
        self.tail = None

        # addAtStart() will add a node to the starting of the list

    def addAtStart(self, data):
        # Create a new node
        newNode = Node(data)

        # If list is empty
        if (self.head == None):
            # Both head and tail will point to newNode
            self.head = self.tail = newNode
            # head's previous will point to None
            self.head.previous = None
            # tail's next will point to None, as it is the last node of the list
            self.tail.next = None
            # Add newNode as new head of the list
        else:
            # head's previous node will be newNode
            self.head.previous = newNode
            # newNode's next node will be head
            newNode.next = self.head
            # newNode's previous will point to None
            newNode.previous = None
            # newNode will become new head
            self.head = newNode

            # display() will print out the nodes of the list

    def display(self):
        # Node current will point to head
        current = self.head
        if (self.head == None):
            print("List is empty")
            return
        print("Adding a node to the start of the list: ")
        while (current != None):
            # Prints each node by incrementing pointer.
            print(current.data),
            current = current.next

        print()


dList = InsertStart()

# Adding 1 to the list
dList.addAtStart(1)
dList.display()
# Adding 2 to the list
dList.addAtStart(2)
dList.display()
# Adding 3 to the list
dList.addAtStart(3)
dList.display()
# Adding 4 to the list
dList.addAtStart(4)
dList.display()
# Adding 5 to the list
dList.addAtStart(5)
dList.display()