class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        newNode = Node(data)
        if self.top is None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode

    def pop(self):
        if self.top is None:
            print('stack underflow')
            return
        else:
            self.top = self.top.next

    def display(self):
        temp = self.top
        if temp is None:
            print("Empty")
            return
        while temp is not None:
            print(temp.data)
            temp = temp.next


newStack = stack()
newStack.push(10)
newStack.push(20)
newStack.push(30)
# newStack.pop()
newStack.display()





