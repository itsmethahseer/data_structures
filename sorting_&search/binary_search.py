def binary_search(list,item):
    start=0
    end = len(list)-1
    while start<=end:
        mid = (start+end)//2
        mid_value= list[mid]
        if mid_value== item:
            return mid
        elif item<mid_value:
            end = mid-1
        else:
            start = mid+1
    return None
x=[6,65,987]
y=65
print(binary_search(x,y))

# O(log n) is its complexity