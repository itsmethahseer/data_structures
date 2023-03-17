class MinHeap:
    def __init__(self, array):
        self.heap = None
        self.build_heap(array)

    def build_heap(self, array):
        self.heap = array
        last_index = len(self.heap) - 1
        for i in range(self.parent(last_index), -1, -1):
            self.shift_down(i)
    def shift_down(self, current_index):
        end_index = len(self.heap) - 1
        left_index = self.leftChild(current_index)
        while left_index <= end_index:
            right_index = self.rightChild(current_index)
            #right element exists and right is less than left . So change right
            if right_index <= end_index and self.heap[right_index] < self.heap[left_index]:
                index_to_shift = right_index
            else:
                index_to_shift = left_index
            #now we know which one to swap
            #if current value is gt index to shift value;swap.
            if self.heap[current_index] > self.heap[index_to_shift]:
                self.heap[current_index], self.heap[index_to_shift] = self.heap[index_to_shift], self.heap[
                    current_index]
                current_index = index_to_shift
                left_index = self.leftChild(current_index)
            else:
                #already satisfies heap property.thus break
                return
    def shift_up(self, current_index):
        parent_index = self.parent(current_index)
        while current_index > 0 and self.heap[parent_index] > self.heap[current_index]:
            self.heap[current_index], self.heap[parent_index] = self.heap[parent_index], self.heap[current_index]
            current_index = parent_index
            parent_index = self.parent(current_index)

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
        self.heap.pop()
        self.shift_down(0)

    def insert(self, value):
        self.heap.append(value)
        self.shift_up(len(self.heap) - 1)

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return (i * 2) + 1

    def rightChild(self, i):
        return (i * 2) + 2

    def display(self):
        for i in range(0, len(self.heap), 1):
            print(self.heap[i],end="")


min_heap = MinHeap([6, 2, 8])
print("heap is:")
min_heap.display()
min_heap.insert(1)
min_heap.insert(5)
min_heap.insert(15)
print("\n")
print("After insertion:")
min_heap.display()
min_heap.remove()
print("\n")
print("After removal:")
min_heap.display()