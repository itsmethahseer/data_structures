def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] < arr[largest]:
        largest = l
    if r < n and arr[r] < arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def heap_sort(arr):
    n = len(arr)
    # build a max heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    # extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr
print(heap_sort([33,4,5,666,7,8,9,0,3,22,3,555,6]))


# def NthLargest(arr, k):
#     for i in range(1, k):
#         max_val = max(arr)
#         arr[arr.index(max_val)] =1
#     return max(arr)
# arr = [71,45,56,6,2,76,7,4,443,0]
# k =4
# print(NthLargest(arr, k))
