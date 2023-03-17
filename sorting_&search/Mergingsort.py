def mergesort(arr):
    if len(arr)>1:
        left_array = arr[:len(arr)//2]
        right_array = arr[len(arr)//2:]

        # Recursion
        mergesort(left_array)
        mergesort(right_array)

        #Merge
        i=0 # Left array index
        j=0 # Right array index
        k = 0 # Merged array index

        while i<len(left_array) and j<len(right_array):
            if left_array[i]<right_array[j]:
                arr[k] = left_array[i]
                i+= 1
            else:
                arr[k]= right_array[j]
                j+=1
            k+=1
        while i<len(left_array):
            arr[k] = left_array[i]
            i+=1
            k+=1
        while j<len(right_array):
            arr[k] = right_array[j]
            j+=1
            k+=1


arr_test = [33,4444,56,4,3,5,7,9,0,1,22,11,3,4,5,9,90,0]
mergesort(arr_test)
print(arr_test)

