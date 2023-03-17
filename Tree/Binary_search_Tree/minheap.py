class MinHeap:
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
        para = (i-1)//2
        if heap[para] > heap[i]:
            heap[i], heap[para] = heap[para], heap[i]
        self.heapify_up(para)
    def delete(self):
        arr = self.heap
        arr[0] = arr[-1]
        arr.pop()
        self.heapify_down(arr, len(arr), 0)
        return arr
    def heapify_down(self, arr, n, i):
        min = i
        left = (2 *i) +1
        right = (2 *i) +2
        if left < n and arr[min] > arr[left]:
            min = left
        if right < n and arr[min] > arr[right]:
            min = right
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
            self.heapify_down(arr, n, min)
h = MinHeap()
print(h.insert([5, 43, 22, 45, 3, 2]))
print(h.delete())
