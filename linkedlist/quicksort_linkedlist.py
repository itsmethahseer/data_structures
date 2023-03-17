class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def quick_sort(self, start, end):
        if start is None or start == end:
            return
        pivot = self.partition(start, end)
        self.quick_sort(start, pivot)
        self.quick_sort(pivot.next, end)

    def partition(self, start, end):
        pivot = start.data
        p = start
        q = start.next
        while q != end:
            if q.data < pivot:
                p = p.next
                p.data, q.data = q.data, p.data


    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp=temp.next




t=LinkedList()
t.append(23)
t.append(11)
t.append(25)
t.append(5)
t.append(89)

t.display()
