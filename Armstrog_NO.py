x= int(input("Enter a Number"))
def armstrong(num):
    order = len(str(x))


    sum = 0
    original = num
    while num>0:
        digit = num % 10
        sum += digit ** order
        num = num//10


    if sum ==original:
        return True
    else:return False

if armstrong(x):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
