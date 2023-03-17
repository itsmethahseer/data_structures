

def rev(a):
    sum = 0
    while a>0:
        rem = a % 10
        sum = sum * 10 +rem
        a = a//10
    return sum
y=rev(123)
print(y)

