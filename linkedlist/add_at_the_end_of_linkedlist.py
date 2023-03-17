#  Python 3 Program for
#  Insert linked list element at end position set A

#  Linked list node
class LinkNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLL:
    def __init__(self):
        self.head = None

    #  Add new node at the end of linked list
    def addNode(self, value):
        # Create  node
        node = LinkNode(value)
        if (self.head == None):
            self.head = node
        else:
            temp = self.head
            #  Find the last node
            while (temp.next != None):
                #  Visit to next node
                temp = temp.next

            #  Add node at last position
            temp.next = node

    # Display all Linked List elements
    def display(self):
        if (self.head != None):
            temp = self.head
            while (temp != None):
                #  Display node value
                print("  ", temp.data, end="")
                #  Visit to next node
                temp = temp.next

        else:
            print("Empty Linked list")


def main():
    sll = SingleLL()
    #  Linked list
    #  1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → NULL
    sll.addNode(1)
    sll.addNode(2)
    sll.addNode(3)
    sll.addNode(4)
    sll.addNode(5)
    sll.addNode(6)
    sll.addNode(7)
    sll.addNode(8)
    print(" Linked List ")
    sll.display()


if __name__ == "__main__": main()