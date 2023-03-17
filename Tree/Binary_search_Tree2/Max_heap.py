class MaxHeap:
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
            if right_index <= end_index and self.heap[right_index] > self.heap[left_index]:
                index_to_shift = right_index
            else:
                index_to_shift = left_index

            if self.heap[current_index] < self.heap[index_to_shift]:
                self.heap[current_index], self.heap[index_to_shift] = self.heap[index_to_shift], self.heap[
                    current_index]
                current_index = index_to_shift
                left_index = self.leftChild(current_index)
            else:
                return

    def shift_up(self, current_index):
        parent_index = self.parent(current_index)
        while current_index > 0 and self.heap[parent_index] < self.heap[current_index]:
            self.heap[current_index], self.heap[parent_index] = self.heap[parent_index], self.heap[current_index]
            current_index = parent_index
            parent_index = self.parent(current_index)

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
            print(self.heap[i], end=" ")


max_heap = MaxHeap([1, 6, 2, 5, 4])

max_heap.display()
# class MaxHeap:
#     def __init__(self):
#         self.heap = []
#
#     def insert(self, value):
#         self.heap.append(value)
#         currentIndex = len(self.heap) - 1
#         while currentIndex > 0 and self.heap[currentIndex] > self.heap[(currentIndex - 1) // 2]:
#             self.heap[currentIndex], self.heap[(currentIndex - 1) // 2] = self.heap[(currentIndex - 1) // 2],
#             self.heap[currentIndex]
#             currentIndex = (currentIndex - 1) // 2
#
#     def delete(self):
#         if len(self.heap) == 0:
#             return None
#         if len(self.heap) == 1:
#             return self.heap.pop()
#         max = self.heap[0]
#         self.heap[0] = self.heap.pop()
#
#         currentIndex = 0
#         leftChildIndex = 2 * currentIndex + 1
#         rightChildIndex = 2 * currentIndex + 2
#
#         while (leftChildIndex < len(self.heap) and self.heap[leftChildIndex] > self.heap[currentIndex]) or
#               (rightChildIndex < len(self.heap) and self.heap[rightChildIndex] > self.heap[currentIndex]):
#             if rightChildIndex >= len(self.heap) or self.heap[leftChildIndex] > self.heap[rightChildIndex]:
#                 self.heap[currentIndex], self.heap[leftChildIndex] = self.heap[leftChildIndex],
#                 self.heap[currentIndex]
#                 currentIndex = leftChildIndex
#             else:
#                 self.heap[currentIndex], self.heap[rightChildIndex] = self.heap[rightChildIndex],
#                 self.heap[currentIndex]
#                 currentIndex = rightChildIndex
#             leftChildIndex = 2 * currentIndex + 1
#             rightChildIndex = 2 * currentIndex + 2
#
#     def display(self):
#         return self.heap
#
#
# max = MaxHeap()
# max.insert(10)
# max.insert(20)
# max.insert(45)
# max.delete()
# print(max.display())
