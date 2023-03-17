class MaxHeap:
    def __init__(self):
        self.heap = []
    def insert(self, arr):
        for i in arr:
            self.heap.append(i)
            self.heapify_up()
        return self.heap
    def heapify_up(self, i=None):
        if i is None:
            i = len(self.heap) - 1
        if i <= 0:
            return
        heap = self.heap
        parent_idx = self.parent_idx(i)
        if heap[parent_idx] < heap[i]:
            heap[parent_idx], heap[i] = heap[i], heap[parent_idx]
            self.heapify_up(parent_idx)
    def delete(self):
        arr = self.heap
        arr[0] = arr[-1]
        arr.pop()
        self.heapify_down(arr, len(arr), 0)
        return arr
    def heapify_down(self, arr, n, i):
        max_idx = i
        left_idx = self.left_idx(i)
        right_idx = self.right_idx(i)
        if left_idx < n and arr[max_idx] < arr[left_idx]:
            max_idx = left_idx
        if right_idx < n and arr[max_idx] < arr[right_idx]:
            max_idx = right_idx
        if max_idx != i:
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
            self.heapify_down(arr, n, max_idx)
    def left_idx(self, i):
        return 2 * i + 1
    def right_idx(self, i):
        return 2 * i + 2
    def parent_idx(self, i):
        return (i - 1) // 2
h = MaxHeap()
print(h.insert([5, 43, 22, 45, 3, 2]))
print(h.delete())