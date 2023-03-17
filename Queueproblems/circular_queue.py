class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0

    def enqueue(self, data):
        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.size

    def dequeue(self):

        data = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        return data

    def display(self):

        print("Elements in the queue:", end=" ")
        for i in range(self.front, self.rear):
            print(self.queue[i % self.size], end=" ")
        print()


queue = CircularQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()
queue.dequeue()
queue.display()
queue.enqueue(4)
queue.display()


