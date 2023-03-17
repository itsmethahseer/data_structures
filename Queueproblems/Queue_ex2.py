# Python program for queue using arrays

class queue_array:
    def __init__(self):
        self.queue = [None] * 5
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        self.rear = self.rear + 1
        self.queue[self.rear] = data

    def dequeue(self):
        self.front = self.front + 1

    def display(self):
        if self.front > self.rear:
            print("queue empty nothing to delete")
        for i in range(self.front + 1, self.rear + 1):
            print(self.queue[i])

queue= queue_array()
queue.enqueue(23)
queue.enqueue(89)
queue.enqueue(56)
queue.enqueue(66)
queue.enqueue(69)

# queue.dequeue()
queue.display()
