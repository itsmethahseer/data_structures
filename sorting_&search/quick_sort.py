def quick_sort(list1):
    length = len(list1)
    if length<=1:
        return list1
    else:
        pivot = list1.pop()
    greater=[]
    lower = []
    for items in list1:
        if items>pivot:
            greater.append(items)
        else:
            lower.append(items)
    return quick_sort(lower)+[pivot]+quick_sort(greater)
x=[43,3,54,5,5,55,53,67,8,33,4,1,0]
print(quick_sort(x))

# O(n) is its complexity