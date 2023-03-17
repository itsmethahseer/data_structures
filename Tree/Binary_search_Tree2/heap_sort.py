"""class HeapSort:
    def sort(self, arr):
        for i in range(len(arr) // 2 - 1, -1, -1):
            self.heapify(arr, len(arr), i)

        for i in range(len(arr) - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)

        return arr

    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(arr, n, largest)


m = HeapSort()
print(m.sort([9, 10, 23, 56, 7, 8]))"""
class Heap:
    def __init__(self, array):
        self.heap = None
        self.build_heap(array)

    def build_heap(self, array):
        self.heap = array
        last_index = len(self.heap) - 1
        for i in range(self.parent(last_index), -1, -1):
            self.shift_down(i, last_index)

    def shift_down(self, current_index, end_index):
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

    def heap_sort(self):
        for i in reversed(range(1, len(self.heap))):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            self.shift_down(0, i - 1)
            # print(self.heap)
        return self.heap

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return (i * 2) + 1

    def rightChild(self, i):
        return (i * 2) + 2

    def display(self):
        for i in range(0, len(self.heap), 1):
            print(self.heap[i], end=" ")


heap = Heap([1, 5, 2, 6, 4, 8])
# heap.display()
# print(heap.heap_sort())
# print(heap.heap_sort())
x=heap.heap_sort()

print(x)
