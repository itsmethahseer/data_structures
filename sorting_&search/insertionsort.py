# python program for insertion sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        val_to_sort = arr[i]
        while arr[i-1]> val_to_sort and i>0:
            arr[i],arr[i-1] = arr[i-1],arr[i]
            i = i-1
    return arr
print(insertion_sort([34,56,4,5,6,44,5,66,12,13,2,3,0,5,7]))










