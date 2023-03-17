class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enque(self,data):
        newNode = Node(data)
        if self.rear is None:
            self.front=self.rear=newNode
            return
        else:
            self.rear.next=newNode
            self.rear=newNode

    def deque(self):
        if self.front is None:
            print("empty queue")
            return
        self.front = self.front.next
        if self.front is None:
            self.rear = None


    def display(self):
        temp=self.front
        if temp is None:
            print("Empty")
            return
        while temp is not None:
            print(temp.data)
            temp=temp.next

newQueue = queue()
newQueue.enque(10)
newQueue.enque(20)
newQueue.enque(30)
# newQueue.deque()
newQueue.display()






























































# from collections import deque
# class Queue:
#     def __init__(self):
#         self.buffer = deque()
#     def enqueue(self,val):
#         self.buffer.appendleft(val)
#     def dequeue(self):
#         return self.buffer.pop()
#     def is_empty(self):
#         return len(self.buffer)==0
#     def size(self):
#         return len(self.buffer)
#
#
# pq = Queue()
# pq.enqueue({
#     'company':'Google',
#     'address':'Banglure',
#     'profit' :1000
# })
# pq.enqueue({
#     'company':'Google',
#     'address':'Ksrkode',
#     'profit':2000
# })
# print(pq.dequeue())
#
# # print(pq.is_empty())

















