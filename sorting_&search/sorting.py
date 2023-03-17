a=[3,4,55,3,1,3,5,3,7,8,3,0]
for i in range(0,12):
    for j in range(i+1,12):
        if a[i]>a[j]:
            a[i], a[j] = a[j], a[i]

print('Array after sorting')
print(a)
